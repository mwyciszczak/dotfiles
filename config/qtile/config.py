# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import subprocess
from libqtile import qtile
from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.command import lazy
from libqtile.utils import guess_terminal

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration

mod = "mod4"
terminal = guess_terminal('alacritty')

keys = [
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
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    #dmenu
    Key(['mod4'], 'p', lazy.run_extension(extension.DmenuRun(
    	dmenu_prompt=':',
	background='#1d1f21',
	foreground='#7BC0F5',
	selected_background='#E270A4',
	selected_foreground='#1d1f21',
	dmenu_bottom=False,
	font='Terminus',
	fontsize=12,
	dmenu_lines=42,
    ))),
]


colors = [["#282c34", "#282c34"], #kolor czcionki
          ["#c678dd", "#c678dd"], #fioletowy
          ["#51afef", "#51afef"], #niebieski
          ["#da8548", "#da8548"], #pomaranczowy
          ["#98be65", "#98be65"], #zielony
          ['#e7d15f', '#e7d15f'], #zolty
          ['#ffffff', '#ffffff'], #bialy
          ['#ffc0cb', '#ffc0cb']]  #rozowy

#Nazwy workspace, domyslny layout
def init_group_names():
    return [('TER',{'layout':'columns'}),
            ('WWW',{'layout':'columns'}),
            ('DEV',{'layout':'columns'}),
            ('DOC',{'layout':'columns'}),
            ('DC',{'layout':'columns'}),
            ('MUS',{'layout':'columns'}),
            ('ETC1',{'layout':'columns'}),
            ('ETC2',{'layout':'columns'}),
        ]

def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ['config', '__main__']:
    group_names = init_group_names()
    groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, 'shift'], str(i), lazy.window.togroup(name)))


layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=1, margin=2),
    layout.Max(),
    layout.Floating()
]

widget_defaults = dict(
    font="Roboto Regular",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

powerline = {
    "decorations": [
        PowerLineDecoration(path='arrow_right')
    ]}


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(

                ),
                widget.Spacer(),
                #widget.WindowName(),
                widget.Systray(
                ),
                widget.TextBox(
                    **powerline
                ),
                #widget.GenPollText( #jesus take the wheel
                #    **powerline,
                #   foreground=colors[0],
                #   background=colors[7],
                #    func=lambda: subprocess.check_output("/home/maciej/Scripts/jesus.sh").decode('utf-8'),
                #   update_interval=2
                #),
                widget.ThermalSensor(
                    **powerline,
                    foreground=colors[0],
                    background=colors[6]
                ),
                widget.Memory(
                    measure_mem='G',
                    foreground=colors[0],
                    background=colors[5],
                    format = '{MemUsed:.1f}G/{MemTotal:.1f}G',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                    **powerline
                ),
                widget.Clock(
                    format="%Y-%m-%d %I:%M %p",
                    foreground=colors[0],
                    background=colors[1],
                    **powerline),
                widget.Backlight(
                    backlight_name='intel_backlight',
                    foreground=colors[0],
                    background=colors[2],
                    fmt="J:{}", step=1,
                    change_command="light -S {0}",
                    **powerline),
                widget.GenPollText(
                    mouse_callbacks={'Button4': lambda: qtile.cmd_spawn('pamixer -i 1'), 'Button5': lambda: qtile.cmd_spawn('pamixer -d 1')},
                    func=lambda: subprocess.check_output("/home/maciej/.config/qtile/vol.sh").decode('utf-8'),
                    fmt='Vol:{}',
                    update_interval=0.1,
                    foreground=colors[0],
                    background=colors[3],
                    **powerline),
                widget.Battery(
                    charge_char='Ładuje',
                    discharge_char='Rozładowuje',
                    format='{char} {percent:2.0%}',
                    foreground=colors[0],
                    background=colors[4],
                    **powerline,
                    update_interval=2),
                widget.CurrentLayout(
                    fmt='Layout: {}',
                    foreground=colors[0],
                    background=colors[7],
                    **powerline
                ),
            ],
            30
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
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
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
