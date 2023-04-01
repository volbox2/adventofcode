from part1 import signal_strength
from part2 import crt
import optparse




if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("-i", action="store", type="string", dest="input", default="input.txt")
    options, args = parser.parse_args()
    signal_strength(options.input,20,40)
    crt(options.input)