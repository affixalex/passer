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
"""
 A TaskScheduler is a buffer that holds task reservations until an application 
 backend is available to run the task. When a backend is ready, the TaskScheduler 
 requests the task from the {@link Scheduler} that submitted the reservation.

 Each scheduler will implement a different policy determining when to launch tasks.

 Schedulers are required to be thread safe, as they will be accessed concurrently 
 from multiple threads.
"""
class TaskScheduler(self):
    self.app_id = 0
    self.request_id = 0
    
    #public InetSocketAddress schedulerAddress;
    #public InetSocketAddress appBackendAddress;
    
    """
     ID of the task that previously ran in the slot this task is using. Used
     to track how long it takes to fill an empty slot on a slave. Empty if this 
     task was launched immediately, because there were empty slots available on 
     the slave.  Filled in when the task is launched.
    """
    self.previous_request_id = 0
    self.previous_task_id = 0
    # Filled in after the getTask() RPC completes. */
    #public TTaskLaunchSpec taskSpec;

    """
    public TaskSpec(TEnqueueTaskReservationsRequest request, InetSocketAddress appBackendAddress) {
      appId = request.getAppId();
      user = request.getUser();
      requestId = request.getRequestId();
      schedulerAddress = new InetSocketAddress(request.getSchedulerAddress().getHost(),
                                               request.getSchedulerAddress().getPort());
      this.appBackendAddress = appBackendAddress;
      previousRequestId = "";
      previousTaskId = "";
    }
    """
    
    