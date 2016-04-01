import daemon
import lockfile
import grp
import signal
import argparse

context = daemon.DaemonContext(
    working_directory='/tmp',
    umask=0o002,
    pidfile=lockfile.FileLock('/tmp/passerd.pid'),
    )

context.signal_map = {
    #signal.SIGTERM: passerd_cleanup,
    signal.SIGHUP: 'terminate' #,
    #signal.SIGUSR1: reload_config,
    }
    
nobody_gid = grp.getgrnam('nobody').gr_gid
#context.gid = nobody_gid

def main():
    """passerd - the passer daemon"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", help="set logging verbosity" , action="count", default=0)
    parser.add_argument("-m", "--mem", help="memory limit (in MB)")
    parser.add_argument("-c", "--cpus", help="# of CPUs to use")
    parser.add_argument("-p", "--port", help="scheduler listen port")
    parser.add_argument("-sp", "--state-port", help="state store listen port")

    args = parser.parse_args()
    
    if args.verbosity >= 0 and args.verbosity <= 5:
        print("Setting verbosity to:", args.verbosity)
        # set config verbosity to args.verbosity
    else:
        print("WARNING: Setting log verbosity to 5")
        # set config verbosity to 5
    
    with context:
        print("Hello")