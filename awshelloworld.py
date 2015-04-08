"""
Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"). You
may not use this file except in compliance with the License. A copy of
the License is located at

    http://aws.amazon.com/apache2.0/

or in the "license" file accompanying this file. This file is
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
ANY KIND, either express or implied. See the License for the specific
language governing permissions and limitations under the License.
"""


import logging

from awscli.customizations.commands import BasicCommand

LOG = logging.getLogger(__name__)

# Debugging helpers
from pprint import pprint
import inspect


def notify(*args):
    """Show debug info.

    Always use a pretty printed list to make it stand out more.
    """
    out = ['NOTIFY']
    if len(args):
        out.extend(args)
    else:
        frame = inspect.stack()[1][0]
        info = inspect.getframeinfo(frame)
        out.extend(['File "{filename}", line {lineno}, in {function}'.format(
            **info.__dict__)])
    pprint(out, width=1)


class HelloWorldError(Exception):

    """Our standard Exception."""

    pass


def awscli_initialize(cli):
    """The entry point for HelloWorld high level commands."""
    notify()  # fires
    # drop to an IPython shell for debugging
    # from pprint import pprint; import IPython; IPython.embed()

    # cli.register('building-command-table.helloworld', HelloWorld.add_command)
    cli.register('building-command-table.main', inject_commands)


def inject_commands(command_table, session, **kwargs):
    """Basically the same as BasicCommand.add_command.

    https://github.com/aws/aws-cli/blob/master/awscli/customizations/commands.py#L282-L283
    """
    notify()  # does NOT fire
    command_table['say-hello'] = HelloWorld(session)


class HelloWorld(BasicCommand):

    """Greet the user."""

    NAME = 'say-hello'
    DESCRIPTION = ('Says hello')
    SYNOPSIS = ('aws helloworld say-hello [--name Name]\n')

    ARG_TABLE = [
        {'name': 'name', 'help_text': 'Helloworld name'},
    ]

    def __init__(self, session):
        """Just trying to see what get's called."""
        notify()  # does NOT fire
        super(HelloWorld, self).__init__(session)

    def _run_main(self, args, parsed_globals):
        """Run the command and report success."""
        notify()  # does NOT fire
        self.setup_services(args, parsed_globals)  # grasping at straws
        self._call(args, parsed_globals)

        return 0

    def setup_services(self, args, parsed_globals):
        """Create self.helloworld on the off chance that it matters.

        https://github.com/aws/aws-cli/blob/develop/awscli/customizations/cloudtrail.py#L115
        """
        client_args = {
            'region_name': None,
            'verify': None
        }
        self.helloworld = self._session.create_client('helloworld',
                                                      **client_args)

    def _call(self, options, parsed_globals):
        """Run the command."""
        notify()  # does NOT fire
        notify('options', options)
        notify('parsed_globals', parsed_globals)
