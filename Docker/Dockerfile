FROM ubuntu:18.10

COPY ./dana ./home/roberto/dana
COPY ./emergent_web_server ./home/roberto/emergent_web_server
ENV DANA_HOME=/home/roberto/dana/
ENV PATH="${PATH}:/home/roberto/dana/"
WORKDIR /home/roberto/emergent_web_server/pal/

ENTRYPOINT ["/bin/bash", "./../docker/emergentsys.sh"]