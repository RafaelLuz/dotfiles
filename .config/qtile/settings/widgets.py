#  -*- coding: utf-8 -*-
"""

Author: Rafael R. L. Benevides
Date: 2/23/22

"""

from libqtile.widget import TextBox, Memory


class IconWidget(list):

    left_char = '\ue0b6'
    right_char = '\ue0b4'

    def __init__(self, icon_char, widget):

        self.icon_settings = {
            'foreground': widget.foreground,
            'background': widget.background,
            'font': widget.font,
            'fontsize': widget.fontsize,
        }

        self.edge_settings = {
            'foreground': widget.background,
            'background': "#00000000",
            'font': widget.font,
            'fontsize': widget.fontsize+7,
        }




        self.extend([
            self.get_left_widget(),
            self.get_icon(icon_char),
            widget,
            self.get_right_widget()
        ])

    def get_left_widget(self):
        return TextBox(text=self.left_char, padding=0, **self.edge_settings)

    def get_right_widget(self):
        return TextBox(text=self.right_char, padding=0, **self.edge_settings)

    def get_icon(self, icon_char):
        return TextBox(text=icon_char, padding=3, **self.icon_settings)


colours = {
    'memory': {'foreground': '#FFD47E', 'background': '#181A29'},
    'CPU': {'foreground': '#D3A7EE', 'background': '181A29'},
}


ram_widget = Memory(
    format='{MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}',
    measure_mem='G',
    **colours['memory']
)


ram_widget = IconWidget(icon_char='\ufb19', widget=ram_widget)








# class WidgetManager:
#
#     def __init__(self, theme):
#         self.__theme = theme
#
#     @property
#     def groupbox(self):
#
#         kwargs = {
#
#         }
#
#         return widget.Groupbox(**kwargs)