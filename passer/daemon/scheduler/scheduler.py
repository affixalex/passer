#
# Copyright 2013 The Regents of The University California
# Copyright 2016 Alex Caudill
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import ../config
from concurrent.futures import ThreadPoolExecutor

"""
This class implements the Passer scheduling functionality.
"""
# Based on:
# https://github.com/radlab/sparrow/blob/master/src/main/java/edu/berkeley/sparrow/daemon/scheduler/Scheduler.java
# https://github.com/radlab/sparrow/blob/master/src/main/java/edu/berkeley/sparrow/daemon/scheduler/SchedulerThrift.java
class Scheduler():
    def __init__(conf, socket):
        self.logger = ""
        self.audit_logger = ""
        # Used to uniquely identify requests arriving at this scheduler.
        self.counter = 0
        # How many times the special case has been triggered
        self.special_case_counter = 0
        # A THostPort describing the address of this scheduler
        self.address = ""
        # A client pool for communicating with node monitors
        self.node_monitor_client_pool = ThreadPoolExecutor(conf.system_cpus)
        # A client pool for communicating with front ends
        self.frontend_client_pool = ThreadPoolExecutor(conf.system_cpus)
        # Information about cluster workload due to other schedulers
        self.state = ""
        # Probe ratios to use if the probe ratio is not explicitly set 
        self.default_probe_ratio_unconstrained = ""
        self.default_probe_ratio_constrained = ""
        # For each request, the task placer that should be used to place the 
        # request's tasks. Indexed by the request ID.
        self.request_task_placers = "" #dict