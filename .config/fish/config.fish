if status is-interactive
    # Commands to run in interactive sessions can go here
end

set -U fish_greeting

alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

fish_add_path ~/.local/bin

theme_gruvbox dark medium

starship init fish | source

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
if test -f /home/max/miniforge3/bin/conda
    eval /home/max/miniforge3/bin/conda "shell.fish" "hook" $argv | source
end

if test -f "/home/max/miniforge3/etc/fish/conf.d/mamba.fish"
    source "/home/max/miniforge3/etc/fish/conf.d/mamba.fish"
end
# <<< conda initialize <<<

