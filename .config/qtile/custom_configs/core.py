#  -*- coding: utf-8 -*-
"""

Author: Rafael R. L. Benevides
Date: 3/5/22

"""

from abc import ABCMeta, abstractmethod

from typing import List, Dict

from libqtile import layout
from libqtile.config import Match, Group, Key, Screen, Mouse
from libqtile.utils import guess_terminal
from libqtile.layout.base import Layout


# ========== ========== ========== ========== ========== ==========
class WidgetTheme(metaclass=ABCMeta):

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

    @property
    @abstractmethod
    def colour(self) -> Dict[str, str]:
        ...

    @property
    @abstractmethod
    def widget_defaults(self) -> Dict:
        ...


# ========== ========== ========== ========== ========== ==========
class QtileConfig(metaclass=ABCMeta):

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

    # ========== ========== ========== ========== ========== required properties
    ...

    # ---------- ---------- ---------- ---------- ---------- abstract
    @property
    @abstractmethod
    def groups(self) -> List[Group]:
        ...

    @property
    @abstractmethod
    def layouts(self) -> List[Layout]:
        ...

    @property
    @abstractmethod
    def keys(self) -> List[Key]:
        ...

    @property
    @abstractmethod
    def screens(self) -> List[Screen]:
        ...

    @property
    @abstractmethod
    def mouse(self) -> List[Mouse]:
        ...

    # ---------- ---------- ---------- ---------- ---------- default
    @property
    def auto_fullscreen(self):
        """
        If a window requests to be fullscreen, it is automatically
        fullscreened. Set this to false if you only want windows to be
        fullscreen if you ask them to be.
        """
        return True

    @property
    def bring_front_click(self):
        """
        When clicked, should the window be brought to the front or not. If this
        is set to "floating_only", only floating windows will get affected
        (This sets the X Stack Mode to Above.)
        """
        return False

    @property
    def cursor_warp(self):
        """
        If true, the cursor follows the focus as directed by the keyboard,
        warping to the center of the focused window. When switching focus
        between screens, If there are no windows in the screen, the cursor will
        warp to the center of the screen.
        """
        return False

    @property
    def dgroups_key_binder(self):
        """
        A function which generates group binding hotkeys. It takes a single
        argument, the DGroups object, and can use that to set up dynamic key
        bindings.

        A sample implementation is available in libqtile/dgroups.py called
        simple_key_binder(), which will bind groups to mod+shift+0-10 by
        default.
        """
        return None

    @property
    def dgroups_app_rules(self):
        """
        A list of Rule objects which can send windows to various groups based
        on matching criteria.
        """
        return []

    @property
    def extension_defaults(self):
        """
        Default settings for extensions.
        """
        return self.widget_defaults

    @property
    def floating_layout(self):
        """
        The default floating layout to use. This allows you to set custom
        floating rules among other things if you wish.

        See the configuration file for the default float_rules.
        """
        return layout.Floating(
            float_rules=[
                # Run the utility of `xprop` to see the wm class and name of an X client.
                *layout.Floating.default_float_rules,
                Match(wm_class="confirmreset"),  # gitk
                Match(wm_class="makebranch"),  # gitk
                Match(wm_class="maketag"),  # gitk
                Match(wm_class="ssh-askpass"),  # ssh-askpass
                Match(title="branchdialog"),  # gitk
                Match(title="pinentry"),  # GPG key password entry
            ]
        )

    @property
    def focus_on_window_activation(self):
        """
        Behavior of the _NET_ACTIVATE_WINDOW message sent by applications

        urgent: urgent flag is set for the window
        focus: automatically focus the window
        smart: automatically focus if the window is in the current group
        never: never automatically focus any window that requests it
        """
        return 'smart'

    @property
    def follow_mouse_focus(self):
        """
        Controls whether or not focus follows the mouse around as it moves
        across windows in a layout.
        """
        return True

    @property
    def widget_defaults(self):
        """
        Default settings for bar widgets. Note: if the font file associated
        with the font selected here is modified while Qtile is running, Qtile
        may segfault (for details see issue #2656).
        """

        if self.theme:
            return self.theme.widget_defaults

        return dict(font='sans', fontsize=12, padding=3)

    @property
    def reconfigure_screens(self):
        """
        Controls whether or not to automatically reconfigure screens when there
        are changes in randr output configuration.
        """
        return True

    @property
    def wmname(self):
        """
        Gasp! We're lying here. In fact, nobody really uses or cares about this
        string besides java UI toolkits; you can see several discussions on the
        mailing lists, GitHub issues, and other WM documentation that suggest
        setting this string if your java app doesn't work correctly. We may as
        well just lie and say that we're a working one by default. We choose
        LG3D to maximize irony: it is a 3D non-reparenting WM written in java
        that happens to be on java's whitelist.
        """
        return 'LG3D'

    @property
    def auto_minimize(self):
        """
        If things like steam games want to auto-minimize themselves when losing
        focus, should we respect this or not?
        """
        return True

    # ========== ========== ========== ========== ========== convenient properties
    @property
    def mod(self):
        return 'mod4'

    @property
    def terminal(self):
        return guess_terminal()

    @property
    def theme(self):
        return None


