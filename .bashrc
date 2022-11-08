#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
# PS1='[\u@\h \W]\$ '

PS1="\[\033[32m\]異 \[\033[37m\]\[\033[34m\]\W \[\033[0m\]\$ "
PS2="\[\033[32m\]  > \[\033[0m\]"

export VISUAL=nvim;
export EDITOR=nvim;


if [ -d "$HOME/.pyenv" ]; then
  export PYENV_ROOT="$HOME/.pyenv"
  export PATH="$PYENV_ROOT/bin:$PATH"
  eval "$(pyenv init --path)"
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
fi

export QT_STYLE_OVERRIDE=kvantum
export PATH="$HOME/texmf/tex/latex/equinox:$PATH"
export PATH="$HOME/texmf/tex/latex/sparta:$PATH"
export PATH="$HOME/texmf/tex/latex/copeTD:$PATH"
