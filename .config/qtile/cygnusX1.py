#  -*- coding: utf-8 -*-
"""

Author: Rafael R. L. Benevides
Date: 10/11/22

"""

import subprocess
from datetime import datetime
from pathlib import Path

from typing import List

from libqtile import bar, layout, widget
from libqtile.config import Mouse, Screen, Key, Group, Match, Drag, Click
from libqtile.layout.base import Layout
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from settings import QtileConfig, colours


class CygnusCatppuccinConfig(QtileConfig):

    bg = '#1D1D2D'
    fg = '#CDD6F4'
    blue = '#6791C9'
    red = '#DF5B61'
    black = '#24283B'
    cyan = '#89DCEB'
    green = '#81C19B'
    orange = '#F5E0DC'
    yellow = '#ECD28B'
    grey = '#343637'
    pink = '#F5C2E7'

    @property
    def groups(self) -> List[Group]:

        try:
            return self.__groups

        except AttributeError:

            telegram = Match(wm_class="telegram-desktop")
            vivaldi = Match(wm_class="vivaldi-stable")
            zathura = Match(wm_class='Zathura')
            matplotlib = Match(wm_class='matplotlib')
            vtk = Match(wm_class='vtk')
            pycharm_exit_dialog = Match(wm_class='jetbrains-pycharm', title='Confirm Exit')

            groups = [
                # ===================================================================== Left
                {
                    'name': '1',
                    'label': '',
                    'layouts': [
                        layout.MonadTall(
                            ratio=0.75,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            align=layout.MonadTall._right,
                            border_width=2,
                            single_border_width=2
                        ),
                        layout.Stack(
                            num_stacks=1,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            border_width=2,
                        )
                    ]
                },
                {
                    'name': '2',
                    'label': '',
                    'layouts': [
                        layout.MonadTall(
                            ratio=0.50,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            align=layout.MonadTall._right,
                            border_width=2,
                            single_border_width=2
                        ),
                        layout.Stack(
                            num_stacks=1,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            border_width=2,
                        )
                    ]
                },
                {
                    'name': '3',
                    'label': '',
                    'layouts': [
                        layout.MonadTall(
                            ratio=0.50,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            align=layout.MonadTall._right,
                            border_width=2,
                            single_border_width=2
                        ),
                        layout.Stack(
                            num_stacks=1,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            border_width=2,
                        )
                    ]
                },
                {
                    'name': '4',
                    'label': '',
                    'layouts': [
                        layout.MonadTall(
                            ratio=0.50,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            align=layout.MonadTall._right,
                            border_width=2,
                            single_border_width=2
                        ),
                        layout.Stack(
                            num_stacks=1,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            border_width=2,
                        )
                    ]
                },
                {
                    'name': '5',
                    'label': '',
                    'layouts': [
                        layout.MonadTall(
                            ratio=0.50,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            align=layout.MonadTall._left,
                            border_width=2,
                            single_border_width=2
                        ),
                        layout.Stack(
                            num_stacks=1,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            border_width=2,
                        )
                    ],
                    'matches': [pycharm_exit_dialog]
                },
                {
                    'name': '6',
                    'label': '',
                    'layouts': [
                        layout.MonadTall(
                            ratio=0.50,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            align=layout.MonadTall._left,
                            border_width=2,
                            single_border_width=2
                        ),
                        layout.Stack(
                            num_stacks=1,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            border_width=2,
                        )
                    ],
                    'matches': [pycharm_exit_dialog]
                },
                {
                    'name': '7',
                    'label': '',
                    'layouts': [
                        layout.MonadTall(
                            ratio=0.50,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            align=layout.MonadTall._left,
                            border_width=2,
                            single_border_width=2
                        ),
                        layout.Stack(
                            num_stacks=1,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            border_width=2,
                        )
                    ],
                    'matches': [matplotlib, vtk]
                },
                {
                    'name': '8',
                    'label': '',
                    'layouts': [
                        layout.MonadTall(
                            ratio=0.50,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            align=layout.MonadTall._left,
                            border_width=2,
                            single_border_width=2
                        ),
                        layout.Stack(
                            num_stacks=1,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            border_width=2,
                        )
                    ],
                    'matches': [matplotlib, vtk]},
                {
                    'name': '9',
                    'label': '',
                    'layouts': [
                        layout.MonadTall(
                            ratio=0.50,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            align=layout.MonadTall._left,
                            border_width=2,
                            single_border_width=2
                        ),
                        layout.Stack(
                            num_stacks=1,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            border_width=2,
                        )
                    ],
                    'matches': [matplotlib, vtk]
                },
                {
                    'name': '0',
                    'label': '',
                    'layouts': [
                        layout.MonadTall(
                            ratio=0.50,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            align=layout.MonadTall._left,
                            border_width=2,
                            single_border_width=2
                        ),
                        layout.Stack(
                            num_stacks=1,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            border_width=2,
                        )
                    ]
                },
                {
                    'name': 'A',
                    'label': '',
                    'layouts': [
                        layout.MonadTall(
                            ratio=0.50,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            align=layout.MonadTall._left,
                            border_width=2,
                            single_border_width=2
                        ),
                        layout.Stack(
                            num_stacks=1,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            border_width=2,
                        ),
                        layout.Matrix(
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            border_width=2,
                            columns=2
                        ),
                        layout.Matrix(
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            border_width=2,
                            columns=3
                        )
                    ],
                    'matches': [pycharm_exit_dialog]
                },  # A
                {
                    'name': 'S',
                    'label': '',
                    'layouts': [
                        layout.MonadTall(
                            ratio=0.50,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            align=layout.MonadTall._left,
                            border_width=2,
                            single_border_width=2
                        ),
                        layout.Stack(
                            num_stacks=1,
                            margin=9,
                            border_focus="93bbff",
                            border_normal="1D2330",
                            border_width=2,
                        )
                    ],
                    'matches': [pycharm_exit_dialog]
                },  # S
            ]

            # self.__groups = [Group(f'{i+1 % 10}', label="") for i in range(10)]

            self.__groups = [Group(**param) for param in groups]

            return self.__groups

    @property
    def layouts(self) -> List[Layout]:
        return []

    @property
    def keys(self) -> List[Key]:
        """
        A list of available commands that can be bound to keys can be found
        at https://docs.qtile.org/en/latest/manual/config/lazy.html
        """

        try:
            return self.__keys

        except AttributeError:

            mod = self.mod
            terminal = guess_terminal()

            def screenshot(save=True, copy=True, select=True):
                def f(qtile):
                    name = str(datetime.now()).replace('-', '').replace(':', '').replace('.', '').replace(' ', '')
                    path = Path.home() / 'Workspace' / 'Pictures' / 'Screenshot'
                    path /= f'screenshot_{name}.png'

                    if select:
                        shot = subprocess.run(['maim', '-s'], stdout=subprocess.PIPE)
                    else:
                        shot = subprocess.run(['maim'], stdout=subprocess.PIPE)

                    if save:
                        with open(path, 'wb') as sc:
                            sc.write(shot.stdout)

                    if copy:
                        subprocess.run(['xclip', '-selection', 'clipboard', '-t',
                                        'image/png'], input=shot.stdout)

                return f

            self.__keys = [
                Key([mod], "Left", lazy.prev_screen(), desc="Move focus to left"),
                Key([mod], "Right", lazy.next_screen(), desc="Move focus to right"),

                Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
                Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
                Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
                Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
                Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
                Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
                Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
                Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
                Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
                Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
                Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
                Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
                Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
                Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
                Key([mod], "i", lazy.layout.grow()),
                Key([mod], "o", lazy.layout.shrink()),

                Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
                Key([mod], "m", lazy.spawn("slock")),
                Key([mod], "c", lazy.spawn("alacritty -e nvim /home/rafael/dotfiles")),
                Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
                Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

                Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
                Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
                Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
                # Key([mod], "w", lazy.function(send_group_to_screen('internet')))), desc="switch to internet group"),
                Key([mod, "control"], "Return", lazy.spawn("rofi -show drun -show-icons")),
                Key([mod], "Print", lazy.function(screenshot(select=False))),
                Key([mod, 'shift'], "Print", lazy.function(screenshot())),
            ]

            for group in self.groups:

                self.__keys.append(Key([mod],
                                       group.name,
                                       lazy.group[group.name].toscreen()
                                    ))
                self.__keys.append(Key([mod, "shift"], group.name,
                                       lazy.window.togroup(
                    group.name, switch_group=False)))

            return self.__keys

    @property
    def screens(self) -> List[Screen]:

        bar_params = {
            'size': 24,
            'margin': [9, 9, 0, 9],  # N E S W
            # 'opacity': 0.75,
            'background': '#00000000',
            'border_color': '#000000',
            'border_width': 0
        }

        # ---------- ---------- ---------- ---------- ---------- left
        widgets_left = [
            widget.GroupBox(
                highlight_method='text',
                urgent_alert_method='text',
                this_current_screen_border=self.yellow,
                active=self.blue,
                inactive=self.grey,
                background="#101213",
                visible_groups=['L1', 'L2', 'L3', 'L4']
            ),
            widget.TextBox(
                text='\uE0B0',
                foreground="#101213",
                background=self.grey,
                padding=0,
                fontsize=20,
            ),
            widget.CurrentLayoutIcon(
                background=self.grey,
                foreground=self.fg,
                padding=0,
                scale=0.5,
            ),
            widget.CurrentLayout(
                background=self.grey,
                foreground=self.fg,
            ),
            widget.TextBox(
                text='\uE0B0',
                # background="#27292a",
                foreground=self.grey,
                padding=0,
                fontsize=20,
            ),
            widget.Spacer(),
            widget.Systray(),
            widget.Spacer(length=10),
            widget.TextBox(
                text='\uE0B2',
                foreground=self.grey,
                padding=0,
                fontsize=20
            ),
            # widget.TextBox(
            #     text='  ',
            #     background=self.grey,
            #     padding=0,
            # ),
            widget.TextBox(
                text='\uE0B2',
                background=self.grey,
                foreground=self.blue,
                padding=0,
                fontsize=20
            ),
            # widget.TextBox(
            #     text='  ',
            #     background=self.blue,
            #     padding=0,
            # ),
            widget.TextBox(
                text='\uE0B2',
                background=self.blue,
                foreground=self.pink,
                padding=0,
                fontsize=20
            ),
            # widget.TextBox(
            #     text='  ',
            #     background=self.pink,
            #     padding=0,
            # ),
            widget.TextBox(
                text='\uE0B2',
                background=self.pink,
                foreground=self.orange,
                padding=0,
                fontsize=20
            ),
            # widget.TextBox(
            #     text='  ',
            #     background=self.orange,
            #     padding=0,
            # ),
            widget.TextBox(
                text='\uE0B2',
                background=self.orange,
                foreground=self.green,
                padding=0,
                fontsize=20
            ),
            # widget.TextBox(
            #     text='  ',
            #     background=self.green,
            #     padding=0,
            # ),
            widget.TextBox(
                text='\uE0B2',
                background=self.green,
                foreground=self.yellow,
                padding=0,
                fontsize=20
            ),
            # widget.TextBox(
            #     text='  ',
            #     background=self.yellow,
            #     padding=0,
            # ),
        ]

        bar_left = bar.Bar(widgets=widgets_left, **bar_params)
        wallpaper_left = '/home/rafael/Workspace/Pictures/Wallpaper/single/9khyjmypmg471.jpg'
        screen_left = Screen(top=bar_left, wallpaper=wallpaper_left)

        # ---------- ---------- ---------- ---------- ---------- centre
        widgets_centre = [
            widget.GroupBox(
                highlight_method='text',
                urgent_alert_method='text',
                this_current_screen_border=self.yellow,
                active=self.blue,
                inactive=self.grey,
                background="#101213",
                visible_groups=['C1', 'C2', 'C3', 'C4']
            ),
            widget.TextBox(
                text='\uE0B0',
                foreground="#101213",
                background=self.grey,
                padding=0,
                fontsize=20,
            ),
            widget.CurrentLayoutIcon(
                background=self.grey,
                foreground=self.fg,
                padding=0,
                scale=0.5,
            ),
            widget.CurrentLayout(
                background=self.grey,
                foreground=self.fg,
            ),
            widget.TextBox(
                text='\uE0B0',
                # background="#27292a",
                foreground=self.grey,
                padding=0,
                fontsize=20,
            ),
            widget.Spacer(),
            widget.TextBox(
                text='\uE0B2',
                foreground=self.grey,
                padding=0,
                fontsize=20
            ),
            # widget.TextBox(
            #     text='  ',
            #     background=self.grey,
            #     padding=0,
            # ),
            widget.TextBox(
                text='\uE0B2',
                background=self.grey,
                foreground=self.blue,
                padding=0,
                fontsize=20
            ),
            # widget.TextBox(
            #     text='  ',
            #     background=self.blue,
            #     padding=0,
            # ),
            widget.TextBox(
                text='\uE0B2',
                background=self.blue,
                foreground=self.pink,
                padding=0,
                fontsize=20
            ),
            widget.TextBox(
                text='\uE0B2',
                background=self.pink,
                foreground=self.orange,
                padding=0,
                fontsize=20
            ),
            # widget.Memory(
            #     format=' {MemUsed:2.1f}{mm} / {MemTotal:.1f}{mm}',
            #     measure_mem='G',
            #     background=self.orange,
            # ),
            widget.TextBox(
                text='\uE0B2',
                background=self.orange,
                foreground=self.green,
                padding=0,
                fontsize=20
            ),
            # widget.CPU(
            #     format='\uF85A {load_percent:>2.0f}%',
            #     background=self.green
            # ),
            widget.TextBox(
                text='\uE0B2',
                background=self.green,
                foreground=self.yellow,
                padding=0,
                fontsize=20
            ),
            # widget.Net(
            #     background=self.yellow,
            #     format='{down}\uf175 {up}\uf176',
            # ),
        ]

        bar_centre = bar.Bar(widgets=widgets_centre, **bar_params)
        wallpaper_centre = '/home/rafael/Workspace/Pictures/Wallpaper/single/filtered/W0126.jpg'
        screen_centre = Screen(top=bar_centre, wallpaper=wallpaper_centre, wallpaper_mode='fill')

        # ---------- ---------- ---------- ---------- ---------- right
        widgets = [
            widget.GroupBox(
                highlight_method='text',
                urgent_alert_method='text',
                this_current_screen_border=self.yellow,
                active=self.blue,
                inactive=self.grey,
                background="#101213",
                visible_groups=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'S']
            ),
            widget.TextBox(
                text='\uE0B0',
                foreground="#101213",
                background=self.grey,
                padding=0,
                fontsize=20,
            ),
            widget.CurrentLayoutIcon(
                background=self.grey,
                foreground=self.fg,
                padding=0,
                scale=0.5,
            ),
            widget.CurrentLayout(
                background=self.grey,
                foreground=self.fg,
            ),
            widget.TextBox(
                text='\uE0B0',
                # background="#27292a",
                foreground=self.grey,
                padding=0,
                fontsize=20,
            ),
            widget.Spacer(),
            widget.TextBox(
                text='\uE0B2',
                foreground=self.grey,
                padding=0,
                fontsize=20
            ),
            # widget.TextBox(
            #     text='  ',
            #     background=self.grey,
            #     padding=0,
            # ),
            widget.Volume(
                fmt="\ufa7d {}",
                background=self.grey,
                foreground=self.fg
            ),
            widget.Battery(
                charge_char='\uf583',
                discharge_char='\uf57d',
                full_char='\uf578',
                empty_char='\uf579',
                format='{char} {percent:2.0%}',
                background=self.grey,
                foreground=self.fg
            ),
            widget.TextBox(
                text='\uE0B2',
                foreground=self.blue,
                background=self.grey,
                padding=0,
                fontsize=20
            ),
            widget.Net(
                # foreground=self.grey,
                background=self.blue,
                format='{down}\uf175 {up}\uf176',
            ),
            widget.TextBox(
                text='\uE0B2',
                foreground=self.pink,
                background=self.blue,
                padding=0,
                fontsize=20
            ),
            widget.CPU(
                format='\uF85A {load_percent:>2.0f}%',
                background=self.pink
            ),
            widget.TextBox(
                text='\uE0B2',
                foreground=self.orange,
                background=self.pink,
                padding=0,
                fontsize=20
            ),
            widget.Memory(
                format=' {MemUsed:2.1f}{mm} / {MemTotal:.1f}{mm}',
                measure_mem='G',
                background=self.orange,
            ),
            widget.TextBox(
                text='\uE0B2',
                foreground=self.green,
                background=self.orange,
                padding=0,
                fontsize=20
            ),
            widget.OpenWeather(
                location='brasilia',
                format='\uE33d {location_city}: {temp}\u00b0C, {humidity}%',
                background=self.green,
            ),
            widget.TextBox(
                text='\uE0B2',
                background=self.green,
                foreground=self.yellow,
                padding=0,
                fontsize=20
            ),
            widget.Clock(
                format='\uf64f  %Y-%m-%d  %a  %H:%M:%S',
                background=self.yellow,
            ),
        ]

        topbar = bar.Bar(widgets=widgets, **bar_params)
        # wallpaper_right = '/home/rafael/Workspace/Pictures/Wallpaper/single/9khyjmypmg471.jpg'
        wallpaper_right = '/home/rafael/Workspace/Pictures/Wallpaper/single/filtered/W0014.png'
        screen_right = Screen(top=topbar, wallpaper=wallpaper_right,
                              wallpaper_mode='fill')

        # ---------- ---------- ---------- ---------- ---------- returning
        return [screen_right]

    @property
    def mouse(self) -> List[Mouse]:
        return [
            Drag([self.mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
            Drag([self.mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
            Click([self.mod], "Button2", lazy.window.bring_to_front()),
        ]

    @property
    def widget_defaults(self):
        return {
            'font': 'SauceCodePro Nerd Font',
            'fontsize': 13,
            'padding': 4,
            # 'background': self.bg,
            'background': '#00000000',
            'foreground': self.black
        }


config = CygnusCatppuccinConfig()
