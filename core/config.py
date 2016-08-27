import json

class Config:
    """
    This class handles parsing the configuration file
    and returns the appropriate information through functions
    """

    sources = []
    backup_rootdir = None

    def __init__(self, config_filename):
        """ Load the configuration file """
        self.load_config(config_filename)

    def load_config(self, filename):
        """ Parses the configuration using json and sets internal variables """
        with open(filename) as config_file:
            raw_config = json.load(config_file)

        self.parse_sources(raw_config)
        self.backup_rootdir = raw_config['root-dir']

    def parse_sources(self, raw_config):
        """ Parse the sources and add to internal array """
        self.sources = raw_config['backup-sources']
        # TODO: This function should validate if the config is ok

    def get_computer_names(self):
        """ For convinience, this method returns the names of the computers """
        return [x['name'] for x in self.sources]
        # return map(lambda x: x['name'], self.sources)
