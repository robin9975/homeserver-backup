class Logger:

    ansi_reset = "\033[0m"
    ansi_red = "\033[31m"

    def __init__(self):
        pass

    def log_notice(self, message):
        """ log a notice message """
        self.write_line("[notice]: " + message)

    def log_warning(self, message):
        """ log a warning message """
        self.write_line(self.color_red("[warning]: ") + message)

    def log_error(self, message):
        """ log an error message """
        self.write_line("[error]: " + message)

    def write_line(self, message):
        """ outputs an log message, for now just prints to console """
        print(message)

    def color_red(self, message):
        return "{}{}{}".format(self.ansi_red, message, self.ansi_reset)
