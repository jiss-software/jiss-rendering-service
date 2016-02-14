apt-get build-dep python-imaging
apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev fonts-liberation -y

apt-get install xfonts-75dpi -y

wget http://download.gna.org/wkhtmltopdf/0.12/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
dpkg -i wkhtmltox-0.12.2_linux-trusty-amd64.deb

cd /usr/local/bin
cp wkhtmltoimage /usr/bin/wkhtmltoimage
cp wkhtmltopdf /usr/bin/wkhtmltopdf