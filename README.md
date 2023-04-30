# My Dotfiles

[![OS EndeavourOS](https://img.shields.io/badge/OS-EndeavourOS-B16286)](https://endeavouros.com/) [![WM Qtile](https://img.shields.io/badge/WM-Qtile-458588)](http://www.qtile.org/) [![Colors gruvbox](https://img.shields.io/badge/Colors-gruvbox-98971A)](https://github.com/morhetz/gruvbox)

# Screenshots

![rice](https://user-images.githubusercontent.com/80772628/235314311-668f7d1c-e526-4400-a86f-8db7fe8ed5e0.png)

## Installation

### Repository Setup

Run the following to clone the repository.

```bash
alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME' >> $HOME/.bashrc && \
source .bashrc && \
echo ".dotfiles" >> .gitignore && \
git clone --bare git@github.com:maximilian-franz/private-dotfiles.git $HOME/.dotfiles && \
config config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*" && \
config config --local status.showUntrackedFiles no && \
config checkout
```

In case `config checkout` fails, either remove the offending files or move them to a backup folder.

### Installing packages

Run `pacman -S - < package-list.txt`.

After that, install the following packages from the AUR.

```
appimagelauncher-git
betterlockscreen
clight
cura-bin
lightdm-settings
ocs-2url
spicetify-cli
spotify
visual-studio-code-bin
xcursor-simp1e-gruvbox-dark
```

### Installing themes

Download the latest release of [Gruvbox GTK Theme](https://www.pling.com/p/1681313/) and extract it to `$HOME/.themes`.

Download the latest release of [gruvbox-plus-icon-pack](https://github.com/SylEleuth/gruvbox-plus-icon-pack) and extract it to `$HOME/.icons`.
