[ -f /etc/xprofile ] && . /etc/xprofile
[ -f ~/.xprofile ] && . ~/.xprofile


if [ "$HOSTNAME" = "taurus"  ]; then
	xrandr --output Virtual1 --primary --mode 1920x1080
fi

exec qtile start
