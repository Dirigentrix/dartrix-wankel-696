from cycleflow_6_9_6.cyclus_nexus_dualcore import DualCoreManager
from cycleflow_6_9_6.ninia_interceptor_layer import NiniaRouter
import sys

class Playground:
    def __init__(self):
        self.manager = DualCoreManager()
        self.router = NiniaRouter()

    def run(self):
        print(\"=== CycleFlow 6-9-6 Interactive Playground ===\")
        print(\"Commands: tick, status, route <msg>, exit\")
        
        while True:
            try:
                cmd_input = input(\"CF> \").strip().split(\" \", 1)
                cmd = cmd_input[0].lower()
                
                if cmd == \"exit\": break
                elif cmd == \"tick\":
                    res = self.manager.process()
                    print(f\"Result: {res}\")
                elif cmd == \"status\":
                    print(f\"Cyclus: {self.manager.cyclus.get_status()}\")
                    print(f\"Nexus: {self.manager.nexus.get_status()}\")
                elif cmd == \"route\":
                    msg = cmd_input[1] if len(cmd_input) > 1 else \"empty\"
                    res = self.router.route(\"user_cmd\", {\"msg\": msg})
                    print(f\"Router Output: {res}\")
                else:
                    print(\"Unknown command.\")
            except KeyboardInterrupt:
                break
        print(\"Exiting playground...\")

if __name__ == \"__main__\":
    p = Playground()
    p.run()
