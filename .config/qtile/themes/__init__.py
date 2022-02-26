#  -*- coding: utf-8 -*-
"""

Author: Rafael R. L. Benevides
Date: 2/23/22

"""

import json
from pathlib import Path


class Theme:

    here = Path(__file__).parent
    default_theme_name = 'dark-grey'

    def __init__(self, name):

        file_path = self.here / f'{name}.json'

        if not file_path.is_file():
            file_path = self.here / f'{self.default_theme_name}.json'

        with file_path.open():
            self._data = json.load(file_path)

    def __getattr__(self, item):
        return self._data[item]

    @property
    def fg_and_bg_colours(self):
        return {
            'foreground': self.foreground,
            'background': self.background
        }


