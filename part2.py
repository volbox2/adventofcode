def crt(input_file: str,width=40):
    x = 1
    row_pos = 0
    crt = list()
    line = list()
    with open(input_file) as prog:
        program = prog.readlines()
        for inst in program:
            if x-1 <= row_pos <= x+1:
                line.append("#")
            else:
                line.append(".")
            # Position in the row starts at 0 and is incremented at the end of the cycle
            row_pos += 1
            # Check if a new line and a reset of the position are needed
            if row_pos % width == 0:
                crt.append(line)
                line = []
                row_pos = 0
            if inst.startswith("addx"):
                if x-1 <= row_pos <= x+1:
                    line.append("#")
                else:
                    line.append(".")
                row_pos +=1
                x += int(inst.split()[1])
                if row_pos % width == 0:
                    crt.append(line)
                    line = []
                    row_pos = 0
        print("PART 2")
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in crt]))
        



