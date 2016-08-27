from core import logger
import subprocess

import os
import datetime

class BackupRunner:
    """
    This class is able to run the actual backup.

    It will, for each source, lookup the latest backup,
    and execute a rsync command, for each folder to be backed up
    using the precious as link-dir option (which copies it using hard links).
    """

    def __init__(self, config):
        self.logger = logger.Logger()
        self.config = config

    def run_backup(self):
        """ Start running the backup for the total config """
        init_string = "Initializing backup for ({})"
        self.logger.log_notice(init_string.format(", ".join(self.config.get_computer_names())))
        for source in self.config.sources:
            self.backup_source(source)

    def backup_source(self, source):
        """ Run a backup for a single source in the config """
        self.logger.log_notice("Starting backup for {}".format(source['name']))
        target_dirname = self.get_target_dirname(source)
        latest_backup = self.get_latest_backup(self.base_dir(source))
        self.execute_rsync(source, target_dirname, latest_backup)

    def base_dir(self, source):
        """ Get the base directory for a source """
        return "{}/{}".format(self.config.backup_rootdir, source['name'])

    def get_target_dirname(self, source):
        """ Get the target directory name where the backup will be stored """
        new_target_dir = datetime.datetime.now().strftime('%Y%m%d_%H%M')
        return self.base_dir(source) + "/" + new_target_dir

    def get_latest_backup(self, basedir):
        """ Find the directory with the latest backup, based on dirname """
        walk_tuple = [x for x in os.walk(basedir)][0]
        dirs = walk_tuple[1]
        if len(dirs) == 0:
            return None
        latest_dir = sorted(dirs, reverse=True)[0]
        return walk_tuple[0] + '/' + latest_dir

    def execute_rsync(self, source, target_dir, link_dir=None):
        """ Execute the actual rsync functionality """
        for folder in source['folders']:
            self.logger.log_notice("Backing up folder {}".format(folder))
            ssh_source = "{}@{}:{}/".format(source['user'], source['location'], folder)
            ssh_destination = "{}{}/".format(target_dir, folder)
            if not os.path.exists(ssh_destination):
                os.makedirs(ssh_destination)
            command = ["rsync", "-arve", "ssh", "--delete", ssh_source, ssh_destination]
            if link_dir is not None and os.path.exists(link_dir + folder):
                command.append("--link-dest={}{}".format(link_dir, folder))
            subprocess.call(command)
