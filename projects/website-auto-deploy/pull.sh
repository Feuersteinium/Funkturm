cd /home/app

git clone https://github.com/Feuersteinium/feuersteinium.github.io.git --branch master
git fetch
git reset --hard HEAD
git pull

nginx