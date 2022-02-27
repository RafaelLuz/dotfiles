# Rafael's dotfiles


### Contents
- [Introduction](#introduction)
- [Installing Arch](#installing-arch)
- [Configuring the fresh installation](#configuring-the-fresh-installation)

---
# Introduction



---
# Installing Arch

## Load brazilian keyboard layout:
  ```shell
  $ loadkeys br-abnt
  ```

## Configure wifi (skip if using cable):
  ```shell
    $ iwctl
  ```

  - follow the interactive instructions using the following commands (mind the order):
  ```shell
    device list
    station <device> scan
    station <device> get-networks
    station <device> connect <network>
    station <device> show
    exit
  ```

## Check connection and interfaces:
  ```shell
  $ ip a
  ```

## Install Arch:
  ```shell
  $ pacman -Sy python-archinstall
  $ python -m archinstall
  ```
  * follow the interactive instructions.
  * after install, reboot without livemedia


## Sync Arch keys and packages
  ```shell
  $ sudo pacman -S archlinux-keyring
  $ sudo pacman -Syu
  ```
---
# Configuring the fresh installation

## Install git related packages:

  ```shell
  $ sudo pacman -S openssh git
  ```

## Allowing SSH connection (as server):

  ```shell
  $ systemctl start sshd.service
  $ systemctl status sshd.service  # just to check
  ```

## [REMOTE VIA SSH] Creating public key:

  ```shell
  $ ssh-keygen -o
  ```
  * follow the interactive instructions.
  * mind the quality of the passphrase.
  * add the key to github

<!-- ## [REMOTE VIA SSH] Adding public to github:
  ``` shell
  $ gh auth login
  ```
  * follow the interactive instructions.
  * use only the minimum required scopes for the token.
  * set expiration date to 7 days (or less if available) -->

## [REMOTE VIA SSH] Cloning dotfiles repository:

  ``` shell
  $ git clone git@github.com:RafaelLuz/dotfiles.git
  ```

## Creating symbolic links

  ```shell
  $ cd ~/dotfiles
  $ bash makelinks.sh
  ```

## Install `paru`:

  ```shell
  $ sudo pacman -S --needed base-devel
  $ cd ~/.local/share
  $ git clone https://aur.archlinux.org/paru.git
  $ cd paru
  $ makepkg -si
  ```
  * follow the interactive instructions.

## Download and install packages:

  ```SHELL
  $ cd ~/dotfiles
  $ bash getpackages.sh
  ```
