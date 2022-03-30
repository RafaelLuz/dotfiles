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
	python-dbus-next      # required by qtile bluetooth widget
	alsa-utils            # required volume widget
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
	ranger                # terminal based file manager
	ueberzug              # image preview in ranger
	maim                  # for taking screenshots
	xclip                 # handle clipboard
	vlc                   # videos
	unzip                 # dtrx needs it
	socat                 # to configure ssh over proxy
	lsof                  # list process open in process
	slock                 # lock screen
	# virtualbox
	kvantum-qt5
 	keepassxc             # I'm trying to deprecate this.. use pass instead
	nano                  # I'm trying to deprecate this.. use neovim instead
	cowsay                # unnecessary funny stuff
	fortune-mod           # unnecessary funny stuff
)

AUR_PACKAGES=(
	bashmount                   # handle external media ('Im not quite sure if I need it)
	dtrx                        # extract compressed files
	#vim-plug                    # plugins for nvim
	nerd-fonts-source-code-pro  # nice font
	nerd-fonts-ubuntu-mono      # nice font
	nerd-fonts-hack             # nice font
	nerd-fonts-mononoki         # nice font
	nerd-fonts-go-mono          # nice font
	redshift-minimal            # colour temperature of screens
	onlyoffice-bin
	ncurses5-compat-libs        # required for pyenv as instructed in https://github.com/pyenv/pyenv/wiki/Common-build-problems
	hollywood                   # unnecessary funny stuff
	nvim-packer-git             # plugin manager for nvim
)

ATOM_PACKAGES=(
	atom-latex                  # latex utilities
	dracula-syntax              # theme of choice
	dracula-ui                  # theme of choice
	language-latex              # syntax highlight for latex
	language-cython
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
