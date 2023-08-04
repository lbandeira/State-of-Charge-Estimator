import time
import math
import matplotlib.pyplot as plt
class print_colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING_YELLOW = '\033[93m'
    FAIL_RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def coulomb_counting(current, time_delta, charge_factor, initial_charge=0):
    """
    Calculates the state of charge (SOC) of a battery using Coulomb counting.

    :param current: The current flowing into or out of the battery, in amperes.
    :param time_delta: The time elapsed since the last measurement, in seconds.
    :param initial_charge: The initial state of charge (SOC) of the battery, in ampere-hours. Defaults to 0.
    :return: The current state of charge (SOC) of the battery, in ampere-hours.
    """
    charge_delta = charge_factor*(current * time_delta / 3600)  # convert seconds to hours (Ah)
    updated_charge = initial_charge + charge_delta 
    return updated_charge #(Ah)

def Soc_calculator(updated_charge, nominal_capacity):
    temp_soc = round((updated_charge/nominal_capacity), 2)
    soc = 100 * temp_soc
    return soc

# Measure the current flowing in and out of the battery every second
current = 100  # amps
time_delta = 1  # seconds

# Initialize the state of charge to 0 ampere-hours
updated_charge = 0
factor = 1.5
soc = 0
socs = []

# Update the state of charge using Coulomb counting
print(print_colors.HEADER + "=========== CHARGING ===========" + print_colors.ENDC)
while(soc < 100):
    updated_charge = coulomb_counting(current, time_delta, factor, initial_charge=updated_charge)
    soc = Soc_calculator(updated_charge, 540)
    socs.append(soc)
    print (print_colors.OKGREEN +"======== \nQ = "+ str(updated_charge) + "   SoC = " + str(soc) + print_colors.ENDC)
    ##time_delta=time_delta+1
    #time.sleep(0.01)
print(print_colors.HEADER + "=========== DISCHARGING ===========" + print_colors.ENDC)
while(soc > 0):
    updated_charge = coulomb_counting(-current, time_delta, factor, initial_charge=updated_charge)
    soc = Soc_calculator(updated_charge, 540)
    socs.append(soc)
    print (print_colors.FAIL_RED + "======== \nQ = "+ str(updated_charge) + "   SoC = " + str(soc) + print_colors.ENDC)
    ##time_delta=time_delta+1
    #time.sleep(0.01)

plt.plot(socs)
plt.xlabel('Time (s)')
plt.ylabel('State of Charge (Ah)')
plt.title('Battery State of Charge')
plt.show()