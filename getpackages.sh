ARCH_PACKAGES=(
	xorg-xrandr           # handle monitors
	qtile                 # window manager
	picom                 # compositor
	python-psutil         # for sensor widgets
	rofi                  # app launcher
	pass                  # handle passwords
	ncdu                  # disk usage
	feh                   # images
	rsync                 # for syncing backups
        alacritty             # terminal emulator
	vivaldi               # browser
	vivaldi-ffmpeg-codecs  # vivaldi proprietary codecs
	telegram-desktop      # chatting
	texlive-most          # for latex!
	atom                  # text editor of choice
	keepassxc             # I'm trying to deprecate this.. use pass instead
	nano                  # I'm trying to deprecate this.. use neovim instead
)

AUR_PACKAGES=(
	bashmount                   # handle external media ('Im not quite sure if I need it)
	dtrx                        # extract compressed files
	nerd-fonts-source-code-pro  # nice font for qtile widgets
)



sudo pacman -S "${ARCH_PACKAGES[@]}" --noconfirm

paru -S "${AUR_PACKAGES[@]}" --noconfirm

