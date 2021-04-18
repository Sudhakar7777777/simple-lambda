FROM ubuntu:20.04

RUN apt-get update && \
  apt-get install -y wget && \
  echo 2 85 | apt-get install -y libgtk-3-0 libnotify4 libnss3 libxss1 libxtst6 xdg-utils libatspi2.0-0 libappindicator3-1 libsecret-1-0

RUN wget https://commandeer-prd-releases.s3.amazonaws.com/Commandeer_1.8.1_amd64.deb && \
  dpkg -i Commandeer_1.8.1_amd64.deb

# ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["commandeer", "--no-sandbox"]