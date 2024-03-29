# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# Thomas Quintana <quintana.thomas@gmail.com>

from logging import CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET

# The level of logging desired. The possible values are:
#   CRITICAL
#   ERROR
#   WARNING
#   INFO
#   DEBUG
#   NOTSET
logging_level = DEBUG
logging_format = '%(asctime)s %(levelname)s - %(name)s - %(message)s'
logging_filename = None # '/usr/lib/freepy/log/freepy.log'

# The Event Socket configuration used to connect to FreeSWITCH.
freeswitch_host = {
    'name':     'FreeSwITCH Test VM',
    'address':  '127.0.0.1',
    'port':      8021,
    'password': 'ClueCon'
}

# A list of services to register with the dispatcher.
dispatcher_services = [
  {
    'name': 'Timer Service',                # The service name.
    'events': [                             # A list of events to forward to the service.
      'ReceiveTimeoutCommand',
      'StopTimeoutCommand'
    ],
    'target': 'lib.services.TimerService'  # The path to the service.
  }
]

# Import the dispatch rules for the dispatcher.
from rules import *