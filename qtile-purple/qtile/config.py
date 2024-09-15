from libqtile import bar, layout, qtile, hook
from qtile_extras import widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget.decorations import PowerLineDecoration

from subprocess import Popen
from os.path import expanduser

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "h", lazy.layout.move_left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.move_right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.move_down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.move_up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.integrate_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.integrate_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.integrate_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.integrate_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_width(30), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_width(-30), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_height(30), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_height(-30), desc="Grow window up"),

    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "space", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Spawn rofi"),
    Key([mod], "tab", lazy.spawn("rofi -show window"), desc="Spawn rofi"),
    Key([], "Page_Down", lazy.spawn("/home/catniped/.config/qtile/screenshot.sh"), desc="Selection screenshot"),
]

for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(f"{i+1}", label="") for i in range(8)]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.Plasma(
        margin=5,
        border_normal="#76588a",
        border_focus="#a57cbf",
        border_normal_fixed="#76588a",
        border_focus_fixed="#a57cbf",
        border_width=3,
        border_width_single=3,
    ),
]

widget_defaults = dict(
    font="EnvyCodeR Nerd Font",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

color1 = "#9a7dc9"
color2 = "#8f63b8"
color3 = "#76588a"

decor = {
    "decorations": [
        RectDecoration(colour="#8e6aa6", radius=10, filled=True, padding_y=5)
    ],
    "padding": 28,
}

powerline_left_1 = {
    "decorations": [
        PowerLineDecoration(path="rounded_left")
    ]
}

powerline_right_1 = {
    "decorations": [
        PowerLineDecoration(path="rounded_right")
    ]
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(background=color1, highlight_method="block", this_current_screen_border="#835ac4", inactive="#9e9e9e", padding=7, **powerline_left_1),
                widget.Spacer(100, background=color2, **powerline_left_1),
                widget.Spacer(820),
                widget.Clock(fmt="<b>{}</b>", **decor),
                widget.Spacer(**powerline_right_1),
                widget.Spacer(100, background=color2, **powerline_right_1),
                widget.GenPollCommand(cmd="playerctl metadata --format '{{ artist }} - {{ title }}'", update_interval=10, shell=True, background=color1),
                widget.Spacer(10, background=color1),
            ],
            35,
            margin=5,
            background=color3,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

@hook.subscribe.startup_once
def autostart():
    home = expanduser('~/.config/qtile/autostart.sh')
    Popen([home])

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_normal="#76588a",
    border_focus="#a57cbf",
    border_width=3,
    float_rules=[
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

auto_minimize = True

wl_input_rules = None

wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "LG3D"
