from organs.cyclus.cyclus import Cyclus
from organs.nexus.nexus import Nexus
from stations.station_9_superdrob.superdrob_dispatch import SuperDrobDispatch

def run_demo():
    print("--- Starting Agro-Organism Demo ---")
    nexus = Nexus()
    cyclus = Cyclus()
    dispatch = SuperDrobDispatch()
    
    sscc = dispatch.generate_sscc()
    print(f"Generated SSCC: {sscc}")
    dispatch.validate_and_dispatch(sscc)
    
    step = cyclus.process_next()
    print(f"Cyclus Step: {step}")
    
    nexus.handle_event({\"step\": step, \"sscc\": sscc})
    print("--- Demo Completed ---")

if __name__ == \"__main__\":
    run_demo()
