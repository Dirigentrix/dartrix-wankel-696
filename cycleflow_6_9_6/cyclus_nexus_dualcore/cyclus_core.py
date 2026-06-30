from typing import Dict

class CyclusCore:
    \"\"\"Rdzeń CYCLUS (Archetyp 1) - Logika 6->9->6\"\"\"
    def __init__(self):
        self.stations = [\"STATION_6\", \"STATION_9\", \"STATION_6_REBORN\"]
        self.current_index = 0
        self.passes = 0
        self.wins = 0
        self.max_passes = 6
        self.target_wins = 9

    def next_step(self) -> Dict:
        station = self.stations[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.stations)
        
        if self.current_index == 0:
            self.passes += 1
            if self.passes >= self.max_passes:
                self.wins += 1
                self.passes = 0
        
        return {
            \"station\": station,
            \"passes\": self.passes,
            \"wins\": self.wins,
            \"completed\": self.wins >= self.target_wins
        }

    def get_status(self) -> Dict:
        return {
            \"core\": \"CYCLUS\",
            \"numerology\": \"153 -> 9 -> 1\",
            \"passes\": f\"{self.passes}/{self.max_passes}\",
            \"wins\": f\"{self.wins}/{self.target_wins}\"
        }
