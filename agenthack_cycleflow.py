#!/usr/bin/env python3
"""
CYCLEFLOW_6_9_6 — AGENTHACK EDITION
Minimalna, szybka, deterministyczna wersja systemu.
Bez Qwen. Bez API key. Bez zależności.
Gotowa do prezentacji i nagrania demo.
"""

from datetime import datetime
import json

# ============================================================
# CYCLUS — deterministyczny obieg 6→9→3→6
# ============================================================

class CyclusCore:
    def __init__(self):
        self.stations = ["STATION_6", "STATION_9", "STATION_3"]
        self.current_station_index = 0
        self.pass_count = 0
        self.win_count = 0
        self.cycle_count = 0
        self.max_passes = 6
        self.target_wins = 9

    def step(self, context):
        station = context.get("station")
        if station not in [6, 9, 3]:
            return {"phase": "ERROR", "message": "Invalid station"}

        station_name = f"STATION_{station}"
        self.current_station_index = self.stations.index(station_name)

        next_station = self.stations[(self.current_station_index + 1) % 3]
        self.pass_count += 1

        result = {
            "phase": "CYCLE",
            "from": station_name,
            "to": next_station,
            "pass_number": self.pass_count,
            "payload": context.get("payload"),
            "timestamp": datetime.now().isoformat()
        }

        if self.pass_count >= self.max_passes:
            result["space_change"] = self._change_space()

        return result

    def _change_space(self):
        self.pass_count = 0
        self.win_count += 1

        result = {
            "type": "SPACE_CHANGE",
            "win_number": self.win_count,
            "remaining": self.target_wins - self.win_count
        }

        if self.win_count >= self.target_wins:
            result["portal"] = self._activate_portal()

        return result

    def _activate_portal(self):
        self.cycle_count += 1
        self.win_count = 0
        self.pass_count = 0

        return {
            "type": "PORTAL_ACTIVATED",
            "value": 11,
            "new_cycle": self.cycle_count
        }


# ============================================================
# NEXUS — X‑węzeł (deterministyczny)
# ============================================================

class NexusCore:
    def route(self, context):
        anomaly = context.get("anomaly_score", 0.0)

        if anomaly >= 0.8:
            action = "INTERCEPT"
        elif anomaly >= 0.5:
            action = "SCATTER"
        else:
            action = "PASS"

        return {
            "phase": "NEXUS",
            "action": action,
            "anomaly_score": anomaly,
            "context": context,
            "timestamp": datetime.now().isoformat()
        }


# ============================================================
# NINIA — intercept + shadow
# ============================================================

class NiniaAgent:
    def intercept(self, payload):
        return payload  # deterministycznie przepuszcza


class NiniaShadow:
    def __init__(self):
        self.trace = []

    def observe(self, payload):
        self.trace.append(payload)

    def recent(self, n=10):
        return self.trace[-n:]


# ============================================================
# DualCoreManager — AUTO mode (deterministyczny)
# ============================================================

class DualCoreManager:
    def __init__(self):
        self.cyclus = CyclusCore()
        self.nexus = NexusCore()

    def process(self, context, mode="AUTO"):
        anomaly = context.get("anomaly_score", 0.0)

        if mode == "AUTO":
            if anomaly >= 0.5:
                mode = "NEXUS"
            else:
                mode = "CYCLE"

        if mode == "CYCLE":
            return self.cyclus.step(context)
        if mode == "NEXUS":
            return self.nexus.route(context)

        return {"phase": "UNKNOWN", "context": context}


# ============================================================
# NINIA ROUTER — spina wszystko
# ============================================================

class NiniaRouter:
    def __init__(self):
        self.manager = DualCoreManager()
        self.agent = NiniaAgent()
        self.shadow = NiniaShadow()

    def route(self, context, mode="AUTO"):
        self.shadow.observe({"before": context, "mode": mode})
        intercepted = self.agent.intercept(context)
        result = self.manager.process(intercepted, mode)
        self.shadow.observe({"after": result, "mode": mode})
        return result

    def status(self):
        return {
            "shadow_trace": self.shadow.recent(),
            "cyclus": {
                "pass_count": self.manager.cyclus.pass_count,
                "win_count": self.manager.cyclus.win_count,
                "cycle_count": self.manager.cyclus.cycle_count
            }
        }


# ============================================================
# PLAYGROUND — interaktywny terminal
# ============================================================

def main():
    router = NiniaRouter()

    print("\n=== CYCLEFLOW_6_9_6 — AGENTHACK EDITION ===\n")
    print("Komendy:")
    print("  send <station> <payload> [anomaly]")
    print("  status")
    print("  exit\n")

    while True:
        cmd = input("CYCLEFLOW> ").strip().split()

        if not cmd:
            continue

        if cmd[0] == "exit":
            break

        if cmd[0] == "status":
            print(json.dumps(router.status(), indent=2))
            continue

        if cmd[0] == "send":
            if len(cmd) < 3:
                print("Użycie: send <station> <payload> [anomaly]")
                continue

            try:
                station = int(cmd[1])
                payload = cmd[2]
                anomaly = float(cmd[3]) if len(cmd) > 3 else None
            except ValueError:
                print("Niepoprawne argumenty")
                continue

            context = {"station": station, "payload": payload}
            if anomaly is not None:
                context["anomaly_score"] = anomaly

            result = router.route(context)
            print(json.dumps(result, indent=2))
            continue

        print("Nieznana komenda")


if __name__ == "__main__":
    main()
