def getBinary(no, length):
    """Returns the binary representation of the number as a string."""

    return bin(no)[2:].zfill(length)


def get4BitSpace(instruction):
    """Returns the instruction as a string of 4-bit nibbles."""

    nibble = []
    for i in range(0, len(instruction), 4):
        nibble.append(instruction[i:i + 4])

    return " ".join(nibble)


def getFinalCode(instruction):
    """Return the instruction as hex of 4-bit nibbles."""

    code = []
    for i in range(0, len(instruction), 4):
        hex_digit = hex(int(instruction[i:i + 4], 2))[2:]
        code.append(hex_digit)

    return " ".join(code)


def getInstructionTemplate(command):
    """Returns the 16-bit instruction template as a string.
        Assumptions:
        - 4 bit immediate values
        - 3 bit register values
        - 16 bit instruction template
        - OPcode: 3 bits
    """

    # Eg: MOV #5, R1
    # Eg: ADD R1, R2, R3

    print(f"Command: {command}")

    # Remove all spaces
    command = command.strip()

    # Remove commas
    command = command.replace(",", "")

    # Convert to lower case
    command = command.lower()

    words = command.split()

    instruction = ["0" for i in range(16)]

    # Destination Register (Common for all instructions)
    Rd = int(words[-1][1])
    Rd = getBinary(Rd, 3)
    instruction[13:16] = Rd

    # MOV
    if words[0] == "mov" or words[0] == "move":
        instruction[0] = "0"
        instruction[1] = "0"

        immd = int(words[1][1:])
        immd = getBinary(immd, 4)
        instruction[9:13] = immd

    # Data Manipulation
    else:
        instruction[0] = "1"
        instruction[1] = "1"

        if words[0] == "add":
            instruction[2] = "0"
            instruction[3] = "0"
            instruction[4] = "0"
        elif words[0] == "and":
            instruction[2] = "0"
            instruction[3] = "0"
            instruction[4] = "1"
        elif words[0] == "or":
            instruction[2] = "0"
            instruction[3] = "1"
            instruction[4] = "0"
        elif words[0] == "xor":
            instruction[2] = "0"
            instruction[3] = "1"
            instruction[4] = "1"
        elif words[0] == "sub":
            instruction[2] = "1"
            instruction[3] = "0"
            instruction[4] = "0"

        Rb = int(words[-2][1])
        Rb = getBinary(Rb, 3)
        instruction[10:13] = Rb

        Ra = int(words[-3][1])
        Ra = getBinary(Ra, 3)
        instruction[7:10] = Ra

    instruction = "".join(instruction)

    machine_code = get4BitSpace(instruction)
    print(f"Machine Code: {machine_code}")

    final_code = getFinalCode(instruction)

    print(f"Final Code: {final_code}\n")

    return final_code


getInstructionTemplate("MOV #5, R3")
getInstructionTemplate("ADD R2, R3, R7")
