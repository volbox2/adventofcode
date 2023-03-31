def check_cycle(first_check,check_interval,cycle):
     return 0 <= cycle <= 220 and (cycle == first_check or (cycle-first_check)%check_interval ==0) 


def signal_strength(input: str ,first_check: int,check_interval: int) -> None:
    x = 1
    cycle = 0
    check = first_check
    signal_strength  = 0
    with open(input) as prog:
        program = prog.readlines()
        for inst in program:
            # Whatever the instruction is, the cycle count should be incremented
            cycle += 1
            if check_cycle(first_check,check_interval,cycle):
                     signal_strength += x*cycle 
            if inst.startswith("addx"):
                cycle+=1
                if check_cycle(first_check,check_interval,cycle):
                     signal_strength += x*cycle
                # The operand is only added at the end of the cycle and the modification is seen during the next cycle 
                x += int(inst.split()[1])
                
    print("PART1: The signal strength is", signal_strength)