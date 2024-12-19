 # battery basket
batteries = [50, 30, 4, 45, 12, 18, 30]
minimum_battery_power = 20 # battery use minimum 20% charge

usuable_battery_power = 0 # battery 0 power 0
usuable_battery_count = 0 # usuable battery 0

for battery in batteries: # check every battery
    if battery > minimum_battery_power:
        usuable_battery_power += battery
        usuable_battery_count += 1

print(usuable_battery_power, usuable_battery_count)