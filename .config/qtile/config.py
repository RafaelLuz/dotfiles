#  -*- coding: utf-8 -*-
"""

Author: Rafael R. L. Benevides
Date: 9/4/22

"""

import socket


hostname = socket.gethostname()

match hostname:

    case 'sagittarius':
        from sagittarius import config

    case 'cygnusX1':
        pass

    case 'divenger':
        pass

    case default:
        pass


# ========== ========== ========== ========== ========== ==========
widget_defaults = config.widget_defaults
extension_defaults = config.extension_defaults

keys = config.keys
groups = config.groups
layouts = config.layouts
screens = config.screens
mouse = config.mouse

auto_fullscreen = config.auto_fullscreen
bring_front_click = config.bring_front_click
cursor_warp = config.cursor_warp
dgroups_key_binder = config.dgroups_key_binder
dgroups_app_rules = config.dgroups_app_rules
floating_layout = config.floating_layout
focus_on_window_activation = config.focus_on_window_activation
follow_mouse_focus = config.follow_mouse_focus
reconfigure_screens = config.reconfigure_screens
wmname = config.wmname
auto_minimize = config.auto_minimize
