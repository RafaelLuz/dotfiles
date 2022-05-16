# from typing import List  # noqa: F401

import subprocess
from datetime import datetime
from pathlib import Path

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from libqtile.widget import TextBox, Memory, CPU, Clock, Backlight


# from custom_configs import SagittariusConfig

# from configuration.core import widget_defaults
#
import socket
#
# from custom_configs import Sagittarius, Cygnus, Divenger, Taurus
#
hostname = socket.gethostname()
#
# if hostname == 'sagittarius':
#     config = Sagittarius()
#
# elif hostname == 'divenger':
#     config = Divenger()
#
# elif hostname == 'cygnus':
#     config = Cygnus()
#
# elif hostname == 'taurus':
#     config = Taurus()
#
# else:
#     raise ValueError()
#
#
# # please note that this order matters
# qtile_global_variable_names = [
#     'widget_defaults',
# ]
#
# for name in qtile_global_variable_names:
#     globals()[name] = getattr(config, name)



# ========== ========== ========== ========== ========== ========== Widgets
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


# ---------- ---------- ---------- ---------- ---------- ---------- settings
colours = {
    'memory': {'foreground': '#FFD47E', 'background': '#181A29'},
    'CPU': {'foreground': '#D3A7EE', 'background': '181A29'},
    'clock': {'foreground': '#93bbff', 'background': '181A29'},
    'backlight': {'foreground': '#f07178', 'background': '181A29'},
    'battery': {'foreground': '#cdea9f', 'background': '181A29'},
    'net': {'foreground': '#98e4ff', 'background': '181A29'},
    'groupbox': {'background': '181A29'},
    'systray': {'background': '181A29'},
}

widget_defaults = dict(
    font='SauceCodePro Nerd Font',
    fontsize=13,
    padding=4,
)

extension_defaults = widget_defaults.copy()


# ---------- ---------- ---------- ---------- ---------- ---------- memory
ram_widget = Memory(
    format='{MemUsed:2.1f}{mm} / {MemTotal:.1f}{mm}',
    measure_mem='G',
    **colours['memory'],
    **widget_defaults
)
ram = WidgetContainer(ram_widget, icon_char='\ufb19')

# ---------- ---------- ---------- ---------- ---------- ---------- CPU
cpu_widget = CPU(
    format='{load_percent:>2.0f}%',
    # padding=None,
    # update_interval = 1.0,
    **colours['CPU'],
    **widget_defaults
)
cpu = WidgetContainer(cpu_widget, icon_char='\uF85A')

# ---------- ---------- ---------- ---------- ---------- ---------- clock
clock_widget = Clock(
    format="%Y-%m-%d  %a  %H:%M:%S",
    **colours['clock'],
    **widget_defaults
)
clock = WidgetContainer(clock_widget, icon_char='\uf64f ')

# ---------- ---------- ---------- ---------- ---------- ---------- backlight
backlight_widget = Backlight(
    format='{percent:2.0%}',
    # padding=0,
    update_interval=0.2,
    backlight_name='intel_backlight',
    **colours['backlight'],
    **widget_defaults
)
backlight = WidgetContainer(backlight_widget, icon_char='\uf5dc ')

# ---------- ---------- ---------- ---------- ---------- ---------- battery
battery = widget.Battery(
    charge_char='\uf583',
    discharge_char='\uf57d',
    full_char='\uf578',
    empty_char='\uf579',
    format='{char} {percent:2.0%}',
    **colours['battery'],
    **widget_defaults
)
battery = WidgetContainer(battery)

# ---------- ---------- ---------- ---------- ---------- ---------- Net
net = widget.Net(
    interface="wlan0" if hostname=='cygnus' else 'enp5s0',
    format='{down}\uf175 {up}\uf176',
    **colours['net'],
    **widget_defaults
)
net = WidgetContainer(net)

# ---------- ---------- ---------- ---------- ---------- ----------
systray = widget.Systray()



# ========== ========== ========== ========== ========== ==========
def send_group_to_screen(group):

    def arrange_groups(qtile):
        if group in ['internet', 'git', 'camera']:
            qtile.cmd_to_screen(0)
            qtile.groups_map[group].cmd_toscreen()

        elif group in ['math', 'python', 'books', 'dotfiles']:
            qtile.cmd_to_screen(1)
            qtile.groups_map[group].cmd_toscreen()

        else:
            qtile.cmd_to_screen(2)
            qtile.groups_map[group].cmd_toscreen()

    return arrange_groups


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


# ========== ========== ========== ========== ========== ==========
mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "Left", lazy.prev_screen(), desc="Move focus to left"),
    Key([mod], "Right", lazy.next_screen(), desc="Move focus to right"),
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key(
    #     [mod, "shift"],
    #     "Return",
    #     lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Key([mod], "w", lazy.function(send_group_to_screen('internet')))), desc="switch to internet group"),
    Key([mod, "control"], "Return", lazy.spawn("rofi -show drun -show-icons"), desc="Spawn a command using a prompt widget"),

    Key([mod], "Print", lazy.function(screenshot(select=False))),
    Key([mod, 'shift'], "Print", lazy.function(screenshot())),
    # Key([mod], "z", lazy.function(launc_dissertation_pdf())),

    Key([mod], "m", lazy.spawn("slock")),

    Key([mod], "c", lazy.spawn("atom -n /home/rafael/dotfiles --in-process-gpu")),
    Key([mod], "d", lazy.spawn("atom -n /home/rafael/Workspace/Development/Projects/MSc/RafaelBenevides-MScProject/dissertation --in-process-gpu")),
    Key([mod], "z", lazy.spawn("zathura /home/rafael/Workspace/Development/Projects/MSc/RafaelBenevides-MScProject/dissertation/main.pdf")),
]


telegram = Match(wm_class="telegram-desktop")
vivaldi = Match(wm_class="vivaldi-stable")
zathura = Match(wm_class='Zathura')
matplotlib = Match(wm_class='matplotlib')


groups = [
    {'name': 'internet', 'label': '\ufbdf 1', 'layouts': [layout.MonadTall(ratio=0.75, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._right, border_width=2, single_border_width=2)]},
    {'name': 'git', 'label': '2 \ue725', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._left, border_width=2, single_border_width=2)]},
    {'name': 'camera', 'label': '3 \uf5ff', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._left, border_width=2, single_border_width=2)]},

    {'name': 'math', 'label': '\ufc06 4', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._left, border_width=2, single_border_width=2)]},
    {'name': 'python', 'label': '5 \ue235', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._left, border_width=2, single_border_width=2)]},
    {'name': 'books', 'label': '6 \ue28a', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._left, border_width=2, single_border_width=2)]},
    {'name': 'dotfiles', 'label': '7 \uf303', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._left, border_width=2, single_border_width=2)]},

    # {'name': 'internet', 'label': '\ufbdf', 'layouts': [layout.MonadTall(ratio=0.75, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._right)], 'matches': [telegram, vivaldi]},

    # {'name': 'document', 'label': '8 \uf725', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._left, border_width=2, single_border_width=2)], 'matches': [zathura]},
    {'name': 'document', 'label': '8 \uf725', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._left, border_width=2, single_border_width=2)]},
    {'name': 'private', 'label': '9 \ue780', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._left, border_width=2, single_border_width=2)], 'matches': [matplotlib]},
    {'name': 'terminal', 'label': '0 \ue795', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._left, border_width=2, single_border_width=2)]},
]

groups = [Group(**param) for param in groups]

for idx, group in enumerate(groups, start=1):

    idxstr = str(idx % 10)
    name = group.name

    # keys.append(Key([mod], idxstr, lazy.group[name].toscreen(), desc=f"Switch to group {name}"))
    # keys.append(Key([mod, "shift"], idxstr, lazy.window.togroup(name, switch_group=False), desc=f"Send windown to group {name}"))

    keys.append(Key([mod], idxstr, lazy.function(send_group_to_screen(name))))
    keys.append(Key([mod, "shift"], idxstr, lazy.window.togroup(name, switch_group=False)))


layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(
    #     # ratio=0.75,
    #     # margin=8,
    #     # border_focus= "e1acff",
    #     # border_normal= "1D2330"
    # ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

colors = [
    ["#282a36", "#282a36"], # panel background
    ["#434758", "#434758"], # background for current screen tab
    ["#ffffff", "#ffffff"], # font colour for group names
    ["#ff5555", "#ff5555"], # background colour for layout widget
    ["#000000", "#000000"], # background for other screen tabs
    ["#a77ac4", "#a77ac4"], # dark green radiant for other screen tabs
    ["#50fa7b", "#50fa7b"], # background colour for network widget
    ["#7197e7", "#7197e7"], # background colour for pacman widget
    ["#9aedfe", "#9aedfe"], # background colour for cmus widget
    ["#000000", "#000000"], # background colour for clock widget
    ["#434758", "#434758"], # background colour for systray widget
]

# ---------- ---------- ---------- ---------- ---------- ---------- groupbox
groupbox = widget.GroupBox(
    # fontsize=18,
    borderwidth=0,
    active='#F5F5F5',
    inactive="727272",
    highlight_method='text',
    this_current_screen_border='#ffd47e',
    # spacing=1,
    urgent_alert_method='text',
    **colours['groupbox'],
    **widget_defaults
)

groupbox0 = widget.GroupBox(
    # fontsize=18,
    borderwidth=0,
    active='#F5F5F5',
    inactive="727272",
    highlight_method='text',
    this_current_screen_border='#ffd47e',
    spacing=20,
    urgent_alert_method='text',
    visible_groups=['internet', 'git', 'camera'],
    **colours['groupbox'],
    **widget_defaults
)

groupbox1 = widget.GroupBox(
    # fontsize=18,
    borderwidth=0,
    active='#F5F5F5',
    inactive="727272",
    highlight_method='text',
    this_current_screen_border='#ffd47e',
    spacing=20,
    urgent_alert_method='text',
    visible_groups=['math', 'python', 'books', 'dotfiles'],
    **colours['groupbox'],
    **widget_defaults
)

groupbox2 = widget.GroupBox(
    # fontsize=18,
    borderwidth=0,
    active='#F5F5F5',
    inactive="727272",
    highlight_method='text',
    this_current_screen_border='#ffd47e',
    spacing=20,
    urgent_alert_method='text',
    visible_groups=['document', 'private', 'terminal'],
    **colours['groupbox'],
    **widget_defaults
)

if hostname in ['sagittarius', 'divenger']:
    screens = [
        Screen(
            top=bar.Bar(
                widgets=[
                    widget.Sep(linewidth=0, padding=2),
                    *ram, widget.Sep(linewidth=0, padding=6),
                    *cpu, widget.Sep(linewidth=0, padding=6),
                    *WidgetContainer(
                        widget.Bluetooth(hci='/dev_F8_AB_E5_26_D7_5B', **colours['clock'], **widget_defaults),
                        icon_char='\uf5ae'), widget.Sep(linewidth=0, padding=6),
                    *WidgetContainer(widget.Volume(fmt=" {}", **widget_defaults, **colours['systray']), icon_char='\ufa7d'),
                    widget.Spacer(),
                    *WidgetContainer(groupbox0),
                    widget.Spacer(),
                    systray,
                    # widget.WindowName(), widget.Sep(linewidth=0, padding=6),
                    # *backlight, widget.Sep(linewidth=0, padding=6),
                    # *battery, widget.Sep(linewidth=0, padding=6),
                    # widget.Net(interface='enp0s3'),
                    # *clock, widget.Sep(linewidth=0, padding=2)
                ],
                size=24,
                opacity=0.75,
                background='#00000000',
                margin=[9, 9, 0, 9],  # N E S W
                # border_width=[0, 0, 0, 0],  # Draw top and bottom borders
                border_color='#000000',
                border_width=0
            ),
            wallpaper='/home/rafael/Workspace/Pictures/Wallpaper/single/9khyjmypmg471.jpg'
        ),
        Screen(
            top=bar.Bar(
                widgets=[
                    widget.Sep(linewidth=0, padding=2),

                    widget.Spacer(),
                    *WidgetContainer(groupbox1),
                    widget.Spacer(),
                    # widget.PulseVolume(),
                    # widget.WindowName(), widget.Sep(linewidth=0, padding=6),
                    # *backlight, widget.Sep(linewidth=0, padding=6),
                    # *battery, widget.Sep(linewidth=0, padding=6),
                    # widget.Net(interface='enp0s3'),
                    # *clock, widget.Sep(linewidth=0, padding=2)
                ],
                size=24,
                opacity=0.75,
                background='#00000000',
                margin=[9, 9, 0, 9],  # N E S W
                # border_width=[0, 0, 0, 0],  # Draw top and bottom borders
                border_color='#000000',
                border_width=0
            ),
            wallpaper='/home/rafael/Workspace/Pictures/Wallpaper/single/9khyjmypmg471.jpg'
        ),
        Screen(
            top=bar.Bar(
                widgets=[
                    # widget.Sep(linewidth=0, padding=2),
                    # *ram, widget.Sep(linewidth=0, padding=6),
                    # *cpu, widget.Sep(linewidth=0, padding=6),
                    *net, widget.Sep(linewidth=0, padding=6),
                    widget.Spacer(),
                    *WidgetContainer(groupbox2),
                    widget.Spacer(),
                    # widget.PulseVolume(),
                    # widget.WindowName(), widget.Sep(linewidth=0, padding=6),
                    # *backlight, widget.Sep(linewidth=0, padding=6),
                    # *battery, widget.Sep(linewidth=0, padding=6),
                    # widget.Net(interface='enp0s3'),
                    *WidgetContainer(widget.OpenWeather(location='brasilia', format='{location_city}: {temp}\u00b0C, {humidity}%', **colours['CPU'], **widget_defaults)), widget.Sep(linewidth=0, padding=6),
                    *clock, widget.Sep(linewidth=0, padding=2)
                ],
                size=24,
                opacity=0.75,
                background='#00000000',
                margin=[9, 9, 0, 9],  # N E S W
                # border_width=[0, 0, 0, 0],  # Draw top and bottom borders
                border_color='#000000',
                border_width=0
            ),
            wallpaper='/home/rafael/Workspace/Pictures/Wallpaper/single/9khyjmypmg471.jpg'
        )
    ]

else:
    screens = [
        Screen(
            top=bar.Bar(
                widgets=[
                    widget.Sep(linewidth=0, padding=2),
                    *ram, widget.Sep(linewidth=0, padding=6),
                    *cpu, widget.Sep(linewidth=0, padding=6),
                    *net, widget.Sep(linewidth=0, padding=6),
                    widget.Spacer(),
                    *WidgetContainer(groupbox),
                    widget.Spacer(),
                    # widget.PulseVolume(),
                    # widget.WindowName(), widget.Sep(linewidth=0, padding=6),
                    # *backlight, widget.Sep(linewidth=0, padding=6),
                    *battery, widget.Sep(linewidth=0, padding=6),
                    *clock, widget.Sep(linewidth=0, padding=2)
                ],
                size=24,
                opacity=0.75,
                background='#00000000',
                margin=[9, 9, 0, 9],  # N E S W
                # border_width=[0, 0, 0, 0],  # Draw top and bottom borders
                border_color='#000000',
                border_width=0
            ),
            wallpaper='/home/rafael/Workspace/Pictures/Wallpaper/single/9khyjmypmg471.jpg'
        )
    ]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="jetbrains-toolbox"),  # GPG key password entry
        matplotlib
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
