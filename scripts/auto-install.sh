install(){
  sudo pacman -S $1
}

installNode(){
  sudo npm i -g $1
}


install picom
install nitrogen 
install clipman 
install dunst
install conky
install zsh
install udiskie
install flameshot
install git
install clipman
install arandr
install autorandr 
install npm
install qtile
install neovim
install zsh
install ruby
install eza
install zoxide
install bat
install thefuck
install extra/xorg-fonts-misc


# set zsj like default shell
chsh -s $(which zsh)

# install pyenv with virtualenv
curl https://pyenv.run | bash

eval "$(pyenv init - bash)"
eval "$(pyenv virtualenv-init -)"

# install neovim on python env
pyenv virtualenv 3.17.7 neovim 
pyenv active neovim
pip install neovim
pyenv deactivate

# install all node libraries
installNode neovim
installNode typescript 
installNode pnpm 
installNode yarn 
installNode typescript-language-server

gem install neovim


# clone my config repos
git clone https://github.com/racso2609/nvim ~/.config
git clone https://github.com/racso2609/qtile ~/.config
git clone https://github.com/racso2609/wezterm ~/.config
git clone https://github.com/racso2609/picom ~/.config
