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

from passer.daemon.monitor import node_monitor_state
from passer.daemon.monitor import fifo_task_scheduler
from passer.daemon.monitor import priority_task_scheduler
from passer.daemon.monitor import round_robin_task_scheduler
from passer.daemon.monitor import task_launcher_service

class NodeMonitor():
    def __init__(conf, internal_port):
        self.conf = conf
        try: 
            self.state = NodeMonitorState(conf)
        except:
            # "Error initializing node monitor state."
        
        self.app_sockets = dict()
        self.app_tasks = dict()
        
        # Map to scheduler socket address for each request id.
        self.request_schedulers = dict()
        
        self.mem = "" # Resources.getSystemMemoryMb(conf);
        # LOG.info("Using memory allocation: " + mem);
        
        self.task_scheduler_type = ""
        #conf.getString(SparrowConf.NM_TASK_SCHEDULER_TYPE, "fifo");
        
        if self.task_scheduler_type == "fifo":
            self.scheduler = FifoTaskScheduler(cores, internal_port)
        elif self.task_scheduler_type == "priority":
            self.scheduler = PriorityTaskScheduler(cores, internal_port)
        elif self.task_scheduler_type == "round_robin":
            self.scheduler = RoundRobinTaskScheduler(cores, internal_port)
        else:
            #throw new RuntimeException("Unsupported task scheduler type: ");

        self.task_launcher_service = TaskLauncherService(conf, self.scheduler, internal_port)
    
    def register_backend(app_id, nm_addr, backend_addr):
        if app_id in self.app_sockets:
            # LOG.warn("Attempt to re-register app " + appId);
            return False
            
        self.app_sockets[app_id] = backend_addr
        self.app_tasks[app_id] = []
        
        return self.state.register_backend(app_id, nm_addr)
    
    """
    Account for tasks which have finished.
    """
    def tasks_finished(tasks):
        self.scheduler.tasks_finished(tasks)
        
    def enqueue_task_reservations(request):
        pass
# https://github.com/radlab/sparrow/blob/master/src/main/java/edu/berkeley/sparrow/daemon/nodemonitor/NodeMonitor.java
        