### 2. Energy Distribution (Battery Problem)
# Task: Distribute energy so all stations have energy <= 10.
def energy_distribution(stations):
    rounds = 0
    while any(s > 10 for s in stations):
        updated = stations[:]
        for i in range(len(stations)):
            if stations[i] > 10:
                updated[i] -= 1
                if i > 0:
                    updated[i - 1] += 1
                elif i < len(stations) - 1:
                    updated[i + 1] += 1
        if stations == updated:
            break
        stations = updated
        rounds += 1
    return rounds
