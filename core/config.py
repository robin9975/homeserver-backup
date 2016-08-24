
import json

class Config:

    sources = []
    backup_rootdir = None

    def __init__(self):
        self.load_config('config.json')

    def load_config(self, filename):
        with open(filename) as file:
            raw_config = json.load(file)

        self.parse_sources(raw_config)
        self.backup_rootdir = raw_config['root-dir']

    def parse_sources(self, raw_config):
        self.sources = raw_config['backup-sources']
        # TODO: VALIDATION

    def get_computer_names(self):
        return map(lambda x: x['name'], self.sources)
