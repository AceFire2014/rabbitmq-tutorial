FROM centos:7

# Install python
RUN \
    yum install -y python36 python36-libs python36-devel python36-pip && \
    yum clean all

# Upgrade pip
RUN pip3.6 install --upgrade pip

WORKDIR /app
ENV PYTHONPATH=/app/

ENV RABBITMQ_USER=
ENV RABBITMQ_PASSWORD=

ADD requirements.txt .
RUN pip3.6 install -r requirements.txt

