
# Program to read and write to local file on disk
# Assumes files are in the same folder as the files

# Setting up file variables
FILENAME_IN = "file1.txt"
FILENAME_OUT=  "file_out.txt"

if __name__=='__main__':

    # Parse a file and write output on stdout to join each line
    try:
        with open(FILENAME_IN, "r") as file:
            one_line = []
            for line in file.readlines():
                one_line.append(line.rstrip())
                print_line = " ".join(one_line)
                print(print_line)
    except IOError:
        print("Error: could not read file: ", FILENAME_IN)

    # Read from one file and write to another
    try:
        with open(FILENAME_IN, "r") as file:
            one_line = []
            for line in file.readlines():
                one_line.append(line.rstrip("\n"))
                print_line=" ".join(one_line)
                try:
                    with open(FILENAME_OUT, "w") as file_out:
                        file_out.write(print_line)
                except IOError:
                    print("Error: could not open write for write", FILENAME_OUT)
    except IOError:
        print("Error: could not read file", FILENAME_IN)
