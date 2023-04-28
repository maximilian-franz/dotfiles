# dotfiles

My dotfiles

## 1 Installation

### 1.1 Setup repository on new machine

Run the following to clone the repository.

```bash
alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME' >> $HOME/.bashrc && \
source .bashrc && \
echo ".dotfiles" >> .gitignore && \
git clone --bare git@github.com:maximilian-franz/dotfiles.git $HOME/.dotfiles && \
config config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*" && \
config config --local status.showUntrackedFiles no && \
config checkout
```

In case `config checkout` fails, either remove the offending files or move them to a backup folder.

### 1.2 Install packages

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

### 1.3 Install themes

Download the latest release of [Gruvbox GTK Theme](https://www.pling.com/p/1681313/) and extract it to `$HOME/.themes`.

Download the latest release of [gruvbox-plus-icon-pack](https://github.com/SylEleuth/gruvbox-plus-icon-pack) and extract it to `$HOME/.icons`.
