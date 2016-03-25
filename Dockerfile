FROM jiss/python2
MAINTAINER Anton Iskov <aiskov@jiss-software.com>

# Install app
ADD . /usr/lib/rendering-service
WORKDIR /usr/lib/rendering-service

RUN apt-get -y build-dep python-imaging
RUN apt-get -y install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev fonts-liberation

RUN apt-get -y install xfonts-75dpi

RUN wget http://download.gna.org/wkhtmltopdf/0.12/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
RUN tar -xf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
RUN rm wkhtmltox-0.12.3_linux-generic-amd64.tar.xz

RUN cp wkhtmltox/bin/* /usr/bin/
RUN rm -rf wkhtmltox

RUN python setup.py install

# Run
EXPOSE 33005

ENV SHELL /bin/bash

ENTRYPOINT ["python", "server.py"]
CMD []
