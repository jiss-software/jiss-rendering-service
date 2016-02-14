apt-get build-dep python-imaging
apt-get -y install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev fonts-liberation

wget http://download.gna.org/wkhtmltopdf/0.12/0.12.1/wkhtmltox-0.12.1_linux-trusty-amd64.deb
dpkg -i wkhtmltox-0.12.1_linux-trusty-amd64.deb

cd /usr/local/bin
cp wkhtmltoimage /usr/bin/wkhtmltoimage
cp wkhtmltopdf /usr/bin/wkhtmltopdf