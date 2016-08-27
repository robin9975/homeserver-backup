class Logger:
    """ 
    Class to log messages with different serverity levels,
    supports notice, warning and error

    Now just prints to the commandline,
    may be improved to write to a log file
    """ 

    ansi_reset = "\033[0m"
    ansi_red = "\033[31m"
    ansi_yellow = "\033[33m"

    def __init__(self):
        pass

    def log_notice(self, message):
        """ log a notice message """
        self.write_line("[notice]: " + message)

    def log_warning(self, message):
        """ log a warning message """
        self.write_line(self.color_yellow("[warning]: ") + message)

    def log_error(self, message):
        """ log an error message """
        self.write_line(self.color_red("[error]: ") + message)

    def write_line(self, message):
        """ outputs an log message, for now just prints to console """
        print(message)

    def color_red(self, message):
        return self.color(message, self.ansi_red)

    def color_yellow(self, message):
        return self.color(message, self.ansi_yellow)

    def color(self, message, color):
        return "{}{}{}".format(color, message, self.ansi_reset)
