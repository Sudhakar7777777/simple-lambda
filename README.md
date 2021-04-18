# simple-localstack

Why Use LocalStack?
The method of temporarily using dummy (or mock, fake, proxy) objects in place of actual ones is a popular way of running tests for applications with external dependencies. Most appropriately, these dummies are called test doubles.

With LocalStack, we will implement test doubles of our AWS services with LocalStack. LocalStack supports:

running our applications without connecting to AWS.
avoiding the complexity of AWS configuration and focus on development.
running tests in our CI/CD pipeline.
configuring and testing error scenarios.

## Usage instructions

Start the docker container
```
docker compose up -d
docker ps
```

You can access the services here:
http://localhost:4566

http://localhost:4566/health?reload


Stop the docker container
```
docker compose stop
```

Use bash to connect into the docker container
```
docker exec -ti localstack bash
```

Alternatively use the make commands
```
make up

make down

make reboot
```

## Running Commandeer on Docker
Read the README file under commandeer-docker folder.

## Reference:
Primary:
1. https://github.com/localstack/localstack/tree/master/doc/developer_guides
1. https://github.com/localstack/localstack -- Remember other tutorials are outdated always look at latest here.
1. https://hub.docker.com/r/localstack/localstack
1. https://github.com/commandeer/open
1. https://github.com/aaronshaf/dynamodb-admin


Useful links:
1. https://www.apress.com/gp/blog/all-blog-posts/developing-for-aws-docker/18515442
1. https://betterprogramming.pub/dont-be-intimidated-learn-how-to-run-aws-on-your-local-machine-with-localstack-2f3448462254
1. https://dev.to/goodidea/how-to-fake-aws-locally-with-localstack-27me
1. https://lobster1234.github.io/2017/04/05/working-with-localstack-command-line/
1. https://anthony-f-tannous.medium.com/using-commandeer-as-a-front-end-console-for-aws-local-resources-32c26b290d39

Other links:
1. https://github.com/localstack/localstack#overview
1. https://reflectoring.io/aws-localstack/
1. https://dev.to/cjjenkinson/the-effortless-serverless-development-environment-with-docker-and-localstack-fgd
