# My Dotfiles

[![OS EndeavourOS](https://img.shields.io/badge/OS-EndeavourOS-B16286)](https://endeavouros.com/) [![WM Qtile](https://img.shields.io/badge/WM-Qtile-458588)](http://www.qtile.org/) [![Colors gruvbox](https://img.shields.io/badge/Colors-gruvbox-98971A)](https://github.com/morhetz/gruvbox)

# Screenshots

![2023-08-01-113320_1920x1080_scrot](https://github.com/maximilian-franz/dotfiles/assets/80772628/44d6e19e-9798-49b5-a943-0161606dd99c)
![2023-08-01-113415_1920x1080_scrot](https://github.com/maximilian-franz/dotfiles/assets/80772628/7ebf883a-8c9e-4a1d-8d33-c5f7d0709e84)
![2023-08-01-113448_1920x1080_scrot](https://github.com/maximilian-franz/dotfiles/assets/80772628/f0e62a3d-5958-4a07-b56f-a0b851095acf)

## Installation

### Repository Setup

Run the following to clone the repository.

```bash
alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME' >> $HOME/.bashrc && \
source .bashrc && \
echo ".dotfiles" >> .gitignore && \
git clone --bare https://github.com/maximilian-franz/dotfiles.git $HOME/.dotfiles && \
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
brillo
cura-bin
lightdm-settings
qtile-extras-git
spicetify-cli
spotify
visual-studio-code-bin
xcursor-simp1e-gruvbox-dark
```

### Installing themes

Download the latest release of [Gruvbox GTK Theme](https://www.pling.com/p/1681313/) and extract it to `$HOME/.themes`.

Download the latest release of [gruvbox-plus-icon-pack](https://github.com/SylEleuth/gruvbox-plus-icon-pack) and extract it to `$HOME/.icons`.
