import json


class Reader:
    """
    Class to read and parse a text file with a single JSON object per readline

    Provides an iterator that will iterate over the lines in the file and yield
    a dict of fields.

    """
    def __init__(self, file_obj):
        self._file_obj = file_obj

    def __iter__(self):
        return self

    def __next__(self):
        line = self._file_obj.readline()
        if line == '':
            raise StopIteration

        return json.loads(line)
