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
	vivaldi-ffmpeg-codecs	# vivaldi proprietary codecs
	telegram-desktop      # chatting
	texlive-most          # for latex!
	atom                  # text editor of choice
	bluez                 # bluetooth protocol
	bluez-utils           # provides bluetoothctl utility
	xournalpp             # for using wacom one
	xf86-input-wacom      # for helping map wacom one to a single monitor
	neovim								# wowowow
	noto-fonts            # a nice font
	fuse2                 # it is required to tun AppImages
	obs-studio            # cameras and recording
	neofetch              # this is nice
	htop									# process monitor
	hunspell-en_GB        # english dictionary
	zathura								# document viewer
	zathura-pdf-poppler   # pdf support
	zathura-djvu          # djvu support
	maim                  # for taking screenshots
 	keepassxc             # I'm trying to deprecate this.. use pass instead
	nano                  # I'm trying to deprecate this.. use neovim instead
)

AUR_PACKAGES=(
	bashmount                   # handle external media ('Im not quite sure if I need it)
	dtrx                        # extract compressed files
	nerd-fonts-source-code-pro  # nice font
	nerd-fonts-ubuntu-mono      # nice font
	nerd-fonts-hack             # nice font
	nerd-fonts-mononoki         # nice font
	nerd-fonts-go-mono          # nice font
	redshift-minimal            # colour temperature of screens
	ncurses5-compat-libs        # required for pyenv as instructed in https://github.com/pyenv/pyenv/wiki/Common-build-problems
)

ATOM_PACKAGES=(
	atom-latex                  # latex utilities
	dracula-syntax              # theme of choice
	dracula-ui                  # theme of choice
	language-latex              # syntax highlight for latex
	language-markdown           # syntax highlight for markdown
	language-restructuredtext   # syntax highlight for sphynx
	language-splunk-conf        # syntax highlight for .conf files
	markdown-preview-enhanced   # better themes for markdown
	right-click-external-app    # open .pdf files direct from atom
	terminus                    # embedded terminal
)


sudo pacman -S "${ARCH_PACKAGES[@]}" --noconfirm

paru -S "${AUR_PACKAGES[@]}" --noconfirm

apm install "${ATOM_PACKAGES[@]}"

curl https://pyenv.run | bash
