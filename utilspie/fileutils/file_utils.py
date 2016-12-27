import os


class _File(object):

    @staticmethod
    def copy(source, destination, unique, sort, case_sensitive, create_path):

        source, destination = os.path.abspath(source), os.path.abspath(destination)

        if create_path:
            _dir_name = os.path.dirname(destination)
            if not os.path.exists(_dir_name):
                os.makedirs(os.path.dirname(destination))

        with open(source, 'r') as s:
            s = s.readlines()

        if case_sensitive:
            _temp_list = s
        else:
            _temp_list = [line.lower() for line in s]

        if unique:
            _temp_list = set(_temp_list)

        if sort:
            _temp_list = sorted(_temp_list)

        with open(destination, 'w+') as d:
            d.writelines(_temp_list)


def copy_file(source, destination, unique=False, sort=False, case_sensitive=True, create_path=False):
    """
    Python utility to create file

    Args:
        source: absolute/relative path of source file
        destination: absolute/relative path of destination file.
                     Use same as source for replacing the content of existing file.
        unique: Copy only unique lines from file
        sort: Sort the content of file
        case_sensitive: unique/sort operations to be performed case-sensitive string
        create_path: Recursively create the path to destination directory in case not found

    Returns: None

    """
    _File.copy(source, destination, unique, sort, case_sensitive, create_path)
