from configparser import SafeConfigParser
from configparser import NoSectionError
from collections.abc import Iterable


class Configuration(object):

    def __init__(self, *file_names, sectionNames="None"):
        """File Names, Section Names"""
        parser = SafeConfigParser()
        parser.optionxform = str  # make option names case sensitive
        found = parser.read(file_names)
        if not found:
            raise ValueError('No config file found!')

        """Checking section input for list of sections to return or just single section"""
        try:
            if check_iterator(sectionNames):
                for name in sectionNames:
                    self.__dict__.update(parser.items(name))  # <-- here the magic happens
            else:
                self.__dict__.update(parser.items(sectionNames))  # <-- here the magic happens
        except NoSectionError and Exception as e:
            print(e)
            print(f"Could not find section '{sectionNames}'. Please check Config.ini file.")


def check_iterator(item):
    """Check if object is iterable"""
    excluded_types = str
    if isinstance(item, Iterable) and not isinstance(item, excluded_types):
        return True
    else:
        return False
