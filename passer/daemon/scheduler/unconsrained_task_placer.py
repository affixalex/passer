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

from collections import deque

"""
A task placer for jobs whose tasks have no placement constraints.
"""
class UnconstrainedTaskPlacer():
    def __init__(request_id, probe_ratio):
        # ID of the request associated with this task placer.
        self.request_id = request_id
        self.probe_ratio = probe_ratio
        # Specifications for tasks that have not yet been launched.
        self.unlaunched_tasks = []
        # For each node monitor where reservations were enqueued, the number 
        # of reservations that were enqueued there.
        self.outstanding_reservations = dict()
        # Whether the remaining reservations have been cancelled.
        self.cancelled = False
        
    def get_enqueue_task_reservations_requests(
      scheduling_request,
      request_id,
      nodes,
      scheduler_address):

        print("test")