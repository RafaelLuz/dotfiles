# from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from libqtile.widget import TextBox, Memory, CPU, Clock, Backlight


# from custom_configs import SagittariusConfig

# from configuration.core import widget_defaults
#
# import socket
#
# from custom_configs import Sagittarius, Cygnus, Divenger, Taurus
#
# hostname = socket.gethostname()
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
    interface="wlan0",
    format='{down}\uf175 {up}\uf176',
    **colours['net'],
    **widget_defaults
)

net = WidgetContainer(net)






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
    Key([mod, "control"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "w", lazy.group['internet'].toscreen(), desc="change to internet group"),
    Key([mod], "Return", lazy.spawn("rofi -show drun -show-icons"), desc="Spawn a command using a prompt widget"),
]


telegram = Match(wm_class="telegram-desktop")
vivaldi = Match(wm_class="vivaldi-stable")

groups = [
    {'name': 'terminal', 'label': '\ue795', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._right)]},
    {'name': 'python', 'label': '\ue235', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._right)]},
    {'name': 'math', 'label': '\ufc06', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._right)]},
    # {'name': 'internet', 'label': '\ufbdf', 'layouts': [layout.MonadTall(ratio=0.75, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._right)], 'matches': [telegram, vivaldi]},
    {'name': 'internet', 'label': '\ufbdf', 'layouts': [layout.MonadTall(ratio=0.75, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._right)]},
    {'name': 'private', 'label': '\ue780', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._right)]},
    {'name': 'camera', 'label': '\uf5ff', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._right)]},
    {'name': 'dotfiles', 'label': '\uf303', 'layouts': [layout.MonadTall(ratio=0.50, margin=9, border_focus="93bbff", border_normal="1D2330", align=layout.MonadTall._right)]},
]

def go_to_group(group):
    def f(qtile):
        if group in '123':
            qtile.cmd_to_screen(0)
            qtile.groupMap[group].cmd_toscreen()
        elif group in '4567':
            qtile.cmd_to_screen(1)
            qtile.groupMap[group].cmd_toscreen()
        else:
            qtile.cmd_to_screen(2)
            qtile.groupMap[group].cmd_toscreen()   

    return f

groups = [Group(**param) for param in groups]

for idx, group in enumerate(groups, start=1):

    idxstr = str(idx)
    name = group.name

    keys.append(Key([mod], idxstr, lazy.group[name].toscreen(), desc=f"Switch to group {name}"))
    keys.append(Key([mod, "shift"], idxstr, lazy.window.togroup(name, switch_group=False), desc=f"Send windown to group {name}"))


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

groupbox = WidgetContainer(groupbox)

screens = [
    Screen(
        top=bar.Bar(
            widgets=[
                widget.Sep(linewidth=0, padding=2),
                *ram, widget.Sep(linewidth=0, padding=6),
                *cpu, widget.Sep(linewidth=0, padding=6),
                # *net, widget.Sep(linewidth=0, padding=6),
                widget.Spacer(),
                *groupbox,
                widget.Spacer(),
                # widget.PulseVolume(),
                # widget.WindowName(), widget.Sep(linewidth=0, padding=6),
                # *backlight, widget.Sep(linewidth=0, padding=6),
                # *battery, widget.Sep(linewidth=0, padding=6),
                # widget.Net(interface='enp0s3'),
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
    ),
    Screen(
        top=bar.Bar(
            widgets=[
                widget.Sep(linewidth=0, padding=2),
                *ram, widget.Sep(linewidth=0, padding=6),
                *cpu, widget.Sep(linewidth=0, padding=6),
                # *net, widget.Sep(linewidth=0, padding=6),
                widget.Spacer(),
                *groupbox,
                widget.Spacer(),
                # widget.PulseVolume(),
                # widget.WindowName(), widget.Sep(linewidth=0, padding=6),
                # *backlight, widget.Sep(linewidth=0, padding=6),
                # *battery, widget.Sep(linewidth=0, padding=6),
                # widget.Net(interface='enp0s3'),
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
    ),
    Screen(
        top=bar.Bar(
            widgets=[
                widget.Sep(linewidth=0, padding=2),
                *ram, widget.Sep(linewidth=0, padding=6),
                *cpu, widget.Sep(linewidth=0, padding=6),
                # *net, widget.Sep(linewidth=0, padding=6),
                widget.Spacer(),
                *groupbox,
                widget.Spacer(),
                # widget.PulseVolume(),
                # widget.WindowName(), widget.Sep(linewidth=0, padding=6),
                # *backlight, widget.Sep(linewidth=0, padding=6),
                # *battery, widget.Sep(linewidth=0, padding=6),
                # widget.Net(interface='enp0s3'),
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
