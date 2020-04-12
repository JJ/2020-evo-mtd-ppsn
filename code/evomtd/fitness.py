#!/usr/bin/env python3
"""
    This script calculate the fitnes of a configuration via this steps:
     1. Generate a NGINX configuration file based on the given config
     2. Test the configuration throught the `nginx -t` tool
     3. Run NGINX with the generated configuration
     4. Uses ZAP to know the security score of the configuration
"""
__author__ = "Ernesto Serrano"
__license__ = "GPLv3"
__email__ = "erseco@correo.ugr.es"

from evomtd.config.nginx import *

from subprocess import run, Popen, PIPE
import tempfile
import os
import sys
import time
import tempfile

import signal

import os
import sys
import logging
import copy

from gixy.core.manager import Manager as Gixy
from gixy.formatters import get_all as formatters


from gixy.core.exceptions import InvalidConfiguration

from io import StringIO

formatter = formatters()["text"]()


def calculate_fitness(config):

    nginx = generate(config)

    # By default return a high value
    score = 999

    s = StringIO(str(nginx))

    # risk_score = { 'Informational' : 0, 'Low' : 1, 'Medium': 2, 'High': 4 }
    # ValueError: ['UNSPECIFIED', 'LOW', 'MEDIUM', 'HIGH'] is not in list

    # print(str(nginx))

    with Gixy() as yoda:
        try:

            yoda.audit('<stdin>', s, is_stdin=True)
            score = sum(yoda.stats.values())
            # score + risk_score[i['risk']]

        except InvalidConfiguration:
            score = 999

        # Show the vulnerabilities
        if sum(yoda.stats.values()) > 0:
            formatter.feed(None, yoda)
            print(formatter.flush())

    return score
