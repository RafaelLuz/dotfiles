#  -*- coding: utf-8 -*-
"""

Author: Rafael R. L. Benevides
Date: 2/23/22

"""

from abc import ABCMeta, abstractmethod


class Theme(metaclass=ABCMeta):

    @property
    @abstractmethod
    def screens(self):
        ...

    @property
    @abstractmethod
    def widgets_default(self):
        ...
