
class Logger:

    def log_notice(self, message):
        self.write_line(message)

    def log_warning(self, message):
        self.write_line(message)

    def log_error(self, message):
        self.write_line(message)

    def write_line(self, message):
        print message

