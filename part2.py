def crt(input_file: str,width=40):
    x = 1
    row_pos = 0
    screen = list()
    line = list()
    with open(input_file) as prog:
        program = prog.readlines()
        for inst in program:
            if x-1 <= row_pos <= x+1:
                line.append("#")
            else:
                line.append(".")
            # Position in the row starts at 0 and is incremented at the end of the cycle
            row_pos = (row_pos+1) %40
            # Check if a new line and a reset of the position are needed
            if row_pos == 0:
                screen.append(line)
                line = []
            if inst.startswith("addx"):
                if x-1 <= row_pos <= x+1:
                    line.append("#")
                else:
                    line.append(".")
                row_pos = (row_pos+1) %40
                x += int(inst.split()[1])
                if row_pos == 0:
                    screen.append(line)
                    line = []
        print("PART 2")
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in screen]))
        



