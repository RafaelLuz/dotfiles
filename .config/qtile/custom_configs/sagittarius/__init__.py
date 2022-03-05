#  -*- coding: utf-8 -*-
"""

Author: Rafael R. L. Benevides
Date: 3/5/22

"""

from libqtile.widget import TextBox

from ..core import QtileConfig, WidgetTheme


class WidgetContainer(list):

    left_char = '\ue0b6'
    right_char = '\ue0b4'

    def __init__(self, wid, icon_char=None):

        self.widget = wid

        self.icon_settings = {
            'foreground': self.widget.foreground,
            'background': self.widget.background,
            'font': self.widget.font,
            'fontsize': self.widget.fontsize,
        }

        self.edge_settings = {
            'foreground': self.widget.background,
            'background': "#00000000",
            'font': self.widget.font,
            'fontsize': self.widget.fontsize+7,
        }

        if icon_char:
            self.extend([
                self.get_left_widget(),
                self.get_icon(icon_char),
                self.widget,
                self.get_right_widget()
            ])

        else:
            self.extend([
                self.get_left_widget(),
                self.widget,
                self.get_right_widget()
            ])

    def get_left_widget(self):
        return TextBox(text=self.left_char, padding=0, **self.edge_settings)

    def get_right_widget(self):
        return TextBox(text=self.right_char, padding=0, **self.edge_settings)

    def get_icon(self, icon_char):
        return TextBox(text=icon_char, padding=3, **self.icon_settings)


class MemoryContainer(WidgetContainer):

    def __init__(self):
        pass


class IslandTheme(WidgetTheme):

    # ========== ========== ========== ========== ========== class attributes
    class WidgetContainer(list):

        left_char = '\ue0b6'
        right_char = '\ue0b4'

        def __init__(self, wid, icon_char=None):

            self.widget = wid

            self.icon_settings = {
                'foreground': self.widget.foreground,
                'background': self.widget.background,
                'font': self.widget.font,
                'fontsize': self.widget.fontsize,
            }

            self.edge_settings = {
                'foreground': self.widget.background,
                'background': "#00000000",
                'font': self.widget.font,
                'fontsize': self.widget.fontsize + 7,
            }

            if icon_char:
                self.extend([
                    self.get_left_widget(),
                    self.get_icon(icon_char),
                    self.widget,
                    self.get_right_widget()
                ])

            else:
                self.extend([
                    self.get_left_widget(),
                    self.widget,
                    self.get_right_widget()
                ])

        def get_left_widget(self):
            return TextBox(text=self.left_char, padding=0, **self.edge_settings)

        def get_right_widget(self):
            return TextBox(text=self.right_char, padding=0, **self.edge_settings)

        def get_icon(self, icon_char):
            return TextBox(text=icon_char, padding=3, **self.icon_settings)

    # ========== ========== ========== ========== ========== special methods
    ...

    # ========== ========== ========== ========== ========== private methods
    ...

    # ========== ========== ========== ========== ========== protected methods
    ...

    # ========== ========== ========== ========== ========== public methods
    ...

    # ---------- ---------- ---------- ---------- ---------- properties
    @property
    def colour(self):

        return {
            'memory': {'foreground': '#FFD47E', 'background': '#181A29'},
            'CPU': {'foreground': '#D3A7EE', 'background': '181A29'},
            'clock': {'foreground': '#93bbff', 'background': '181A29'},
            'backlight': {'foreground': '#f07178', 'background': '181A29'},
            'battery': {'foreground': '#cdea9f', 'background': '181A29'},
            'net': {'foreground': '#98e4ff', 'background': '181A29'},
            'groupbox': {'background': '181A29'},
        }

    @property
    def widget_defaults(self):
        return {
            'font': 'SauceCodePro Nerd Font',
            'fontsize': 13,
            'padding': 4
        }





class SagittariusConfig(QtileConfig):

    # ========== ========== ========== ========== ========== class attributes
    ...

    # ========== ========== ========== ========== ========== special methods
    ...

    # ========== ========== ========== ========== ========== private methods
    ...

    # ========== ========== ========== ========== ========== protected methods
    ...

    # ========== ========== ========== ========== ========== public methods
    ...

    # ---------- ---------- ---------- ---------- ---------- properties
    ...