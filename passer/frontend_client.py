"""
A Python client to the Passer scheduling service. Once a client is initialized,
it can be safely used from multiple threads.

Based on: https://github.com/radlab/sparrow/blob/master/src/main/java/edu/berkeley/sparrow/api/SparrowFrontendClient.java
"""

class PasserFrontendClient(self):
    """
     Initialize a connection to a sparrow scheduler.
     @param passerSchedulerAddr. The socket address of the Sparrow scheduler.
     @param app. The application id. Note that this must be consistent across frontends
                 and backends.
     @param frontendServer. A class which implements the frontend server interface (for
                            communication from Sparrow).
     @throws IOException
    """
    def __init__(scheduler_addr, app, frontend_server):
        self.server_launched = False
        self.logger = "" # TBD
        self.num_clients = 8
        self.default_listen_port = 50201