if status is-interactive
    # Commands to run in interactive sessions can go here
end

set -U fish_greeting

alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

fish_add_path ~/.local/bin

theme_gruvbox dark medium

starship init fish | source
