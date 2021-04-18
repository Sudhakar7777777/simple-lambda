FROM node:14.16.1-slim

RUN apt-get update

# Official AWS documentation recommends using python3 and associated tooling.That doesn't work, or at least it does not work as easily as advertised.
RUN apt-get install python-dev python-pip -y

# The awsebcli has a dependency issue and this resolves it
RUN easy_install --upgrade six

RUN pip install awscli

WORKDIR /usr/src/app
COPY package.json yarn.lock /usr/src/app/

RUN yarn

COPY . /usr/src/app

CMD ["yarn", "dev"]