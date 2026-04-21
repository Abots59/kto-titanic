FROM debian:bullseye

RUN apt update
RUN apt install python
RUN apt install vim

RUN mkdir /opt/app-root
RUN cd /opt/app-root
RUN touch my_script.py

RUN vim my_script.py