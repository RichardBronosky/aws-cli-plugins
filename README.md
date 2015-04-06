# aws-cli-plugins
Examples of how to add custom commands to the [aws-cli].

--------

### Warning

This is a work in progress that doesn't currently work.

### Usage

Install the plugin as a python package.

    pip install -U git+https://github.com/RichardBronosky/aws-cli-plugins.git

Add the plugin to your `~/.aws/config` file.

```
# ~/.aws/config
[default]
region = us-east-1
output = json

[plugins]
helloworld = awshelloworld
```

Call the helloworld command.

    aws helloworld say-hello

### Expected Behavior

```
$ aws helloworld say-hello
['NOTIFY',
 'File "/usr/local/lib/python2.7/site-packages/awshelloworld.py", line 53, in awscli_initialize']
['NOTIFY',
 'File "/usr/local/lib/python2.7/site-packages/awshelloworld.py", line 66, in inject_commands']
['NOTIFY',
 'File "/usr/local/lib/python2.7/site-packages/awshelloworld.py", line 84, in __init__']
['NOTIFY',
 'File "/usr/local/lib/python2.7/site-packages/awshelloworld.py", line 89, in _run_main']
['NOTIFY',
 'File "/usr/local/lib/python2.7/site-packages/awshelloworld.py", line 109, in _call']
['NOTIFY',
 'options',
 [...list of options...]]
['NOTIFY',
 'parsed_globals',
 [...list of parsed_globals...]]
```

### Actual Behavior
$ aws helloworld say-hello
```
['NOTIFY',
 'File "/usr/local/lib/python2.7/site-packages/awshelloworld.py", line 53, in awscli_initialize']
usage: aws [options] <command> <subcommand> [parameters]
aws: error: argument command: Invalid choice, valid choices are:

autoscaling                              | cloudformation
cloudfront                               | cloudhsm
cloudsearch                              | cloudsearchdomain
cloudtrail                               | cloudwatch
cognito-identity                         | cognito-sync
datapipeline                             | directconnect
dynamodb                                 | ec2
ecs                                      | elasticache
elasticbeanstalk                         | elastictranscoder
elb                                      | emr
glacier                                  | iam
importexport                             | kinesis
kms                                      | lambda
logs                                     | opsworks
rds                                      | redshift
route53                                  | route53domains
sdb                                      | ses
sns                                      | sqs
ssm                                      | storagegateway
sts                                      | support
swf                                      | s3api
s3                                       | configure
deploy                                   | configservice
help
```

[aws-cli]: https://github.com/aws/aws-cli/ 
