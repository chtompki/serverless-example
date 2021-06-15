serverless-example
==================

Installation requirements. It's preferred that you install both [python3](https://www.python.org/downloads/) 
as well as [node.js](https://nodejs.org/en/download/). The reason that we do this is because our lambda function is written in python3,
and the serverless framework itself is written in javascript and is delivered as a node package.

Installing the serverless cli is as simple as:

1. Install node.js (using the previously mentioned installer)
2. Run `npm install -g serverless`

Make sure you also install Python. Note, the reason that we chose Python as the function's runtime is that we generally write
Python lambda functions because Python was the first supported langauge in AWS lambda. That said, these days, a host of other runtimes
are available. We also are using *GNU Make* for the sake of building, testing, and deploying the function. We suggest that you also do this.

### Makefile targets

* `make venv` - installs the requisite python dependencies
  * Note this only currently installs boto3 which isn't used by the function (yet)
* `make test` - runs the unit tests and validates coverage is above a certain level 95% for now
* `make lint` - runs *flake8* on function and test code
* `make build` - aggregate target that is identical to `make test lint`
* `make deploy` - runs `sls deploy` note this requires that the command line have aws account credentials setup in your
                  `~/.aws` directory. This is achieved by running `aws configure` with the AWS CLI installed.