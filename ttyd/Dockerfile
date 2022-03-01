FROM ubuntu
EXPOSE 7681
RUN apt update \
    && apt upgrade -y \
    && apt install wget -y \
    && wget -c -O ttyd https://github.com/tsl0922/ttyd/releases/download/1.6.3/ttyd.x86_64 \
    && chmod u+x ttyd