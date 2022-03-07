[ -f /etc/xprofile ] && . /etc/xprofile
[ -f ~/.xprofile ] && . ~/.xprofile


if [ "$HOSTNAME" = "taurus"  ]; then
	xrandr --output Virtual1 --primary --mode 1920x1080

elif [ "$HOSTNAME" = "sagittarius"  ]; then
	xrandr --output DVI-D-0 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-0 --mode 1920x1080 --pos 1920x0 --rotate normal --output DP-1 --mode 1920x1080 --pos 3840x0 --rotate normal

elif [ "$HOSTNAME" = "divenger"  ]; then
	xrandr --output DP-3 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1 --mode 1920x1080 --pos 1920x0 --rotate normal --output DP-2 --mode 1920x1080 --pos 3840x0 --rotate normal

fi

exec qtile start
