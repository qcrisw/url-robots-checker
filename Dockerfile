FROM python:3.7.6
LABEL maintainer="QCRI Software Group <qcriswgroup@hbku.edu.qa>"

WORKDIR /home

# upgrade pip itself
RUN pip3 install --upgrade pip

COPY requirements.txt /home/requirements.txt
RUN pip3 install -r requirements.txt

COPY setup.py /home/setup.py

RUN pip3 install .

COPY / /home
