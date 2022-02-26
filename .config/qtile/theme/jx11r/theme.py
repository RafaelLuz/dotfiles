#  -*- coding: utf-8 -*-
"""

Author: Rafael R. L. Benevides
Date: 2/23/22

"""

import json
from pathlib import Path

from ..base import Theme


class Colour:

    here = Path(__file__).parent
    filename_default = 'colours'

    def __init__(self, filename=filename_default):

        filepath = self.here / f'{filename}.json'

        if not filepath.is_file():
            filepath = self.here / f'{self.filename_default}.json'

        with filepath.open():
            self._colours = json.load(filepath)

    def __getattr__(self, item):
        return self[item]

    def __getitem__(self, item):
        return self._colours[item]


class JX11R(Theme):

    def __init__(self, colours=None):

        pass




    @property
    def widgets_default(self):
        return {
            'font': 'SauceCodePro Nerd Font',
            'fontsize': 13,
            'padding': 4
        }
