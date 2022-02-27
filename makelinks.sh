DOTFILES=(
        ".bashrc"
        ".xinitrc"
        ".xprofile"
	".config"
)
 
function create_symbolic_link() {
	
	if [ -f "$HOME/$1" ]; then

                echo "$HOME/$1 already exists. Removing it..."
                rm "$HOME/$1"

	elif [ -d "$HOME/$1" ]; then

		for content in "$HOME/$1"/*; do
			echo "Moving $content to $HOME/dotfiles/$1"
			mv -vn "$content" "$HOME/dotfiles/$1" 
		done
	
		echo "Removing $HOME/$1"
		rm -rf "$HOME/$1"	
	fi

	echo "Creating link to $HOME"
	ln -s "$HOME/dotfiles/$1" "/$HOME/$1"
}



for filename in "${DOTFILES[@]}"; do
	create_symbolic_link $filename
done

