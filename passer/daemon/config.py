class PasserConfig(object):
    def __init__(self):
        # The number of usable CPUs in the system. Defaults to 2.
        self.system_cpus = 2
        # The number of threads to use. Defaults to 4.
        self.system_threads = 4
        # Values: 1-5 "fatal", "error", "warn", "info", "debug"
        self.verbosity = 0
        # Listen port for the scheduler
        self.scheduler_port = 5010
        # Listen port for the state store -> scheduler interface
        self.scheduler_state_port = 5011
        # Should the scheduler cancel outstanding reservations when all of a 
        # job's tasks have been scheduled? True or False
        self.default_cancellation = True
        # List of ports corresponding to the node monitors (backend interface)
        # that this daemon is supposed to run. In most deployment scenarios this
        # will consist of a single port or will be left unspecified.
        self.nm_ports = []
        # List of ports corresponding to node monitors (internal interface)
        # that this daemon is supposed to run. In most deployment scenarios this
        # will consist of a single port or will be left unspecified.
        self.internal_ports = []
        # The type of task scheduler to use on our node monitor.
        # Values: "fifo", "round_robin", "priority"
        self.nm_task_scheduler_type = "fifo"
        # The ratio of probes used in a scheduling decision to tasks.
        # For requests without constraints...
        self.default_sample_ratio = 1.05
        # For requests with constraints...
        self.default_sample_ratio_constrained = 2
        # The hostname of this machine.
        self.hostname = "hostname"
        # Use an invalid initial value so that the "special task set" is only 
        # used by those who know what they're doing.
        self.default_special_task_set_size = -1
        # Parameters for static operation.
        # Expects a comma-separated list of host:port pairs describing the 
        # address of the internal interface of the node monitors.
        self.static_node_monitors = ""
        self.static_app_name = ""
        self.get_task_port = ""
        self.spread_evenly_task_set_size = "1"
