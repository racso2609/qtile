# install=sudo apt-get install -y

sudo apt install -y npm arandr autorandr clipman docker-compose feh firefox git flameshot udiskie zsh neovim python3 conky dunst picom

sudo npm i -g n pnpm yarn typescript typescript-language-server


curl https://pyenv.run | bash

pyenv global 3.12.5

pyenv virtualenv 3.12.5 nvim 
pyenv virtualenv 3.12.5 qtile 

pyenv activate nvim
pip install neovim 
