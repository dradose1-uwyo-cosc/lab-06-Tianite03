# Talon Bluemel
# 11-12-24
# Lab Section: 12
# Sources, people worked with, help given to: 

input_file_path = 'prompt.txt'
output_file_path = 'out.txt'

input_file = open(input_file_path, 'r')
output_file = open(output_file_path, 'w')

try:
    for line in input_file:
        if not line.strip():
            continue
        pairs = line.strip().split("\t")
        output_line = ""

        for pair in pairs:
            key_value = pair.split(':')
            if len(key_value) == 2:
                key, value = key_value
                if key == 'w':
                    output_line += ' ' * int(value)
                elif key == "*":
                    output_line += '*' * int(value)
            else:
                print("Invalid key-value pair: ", pair)
        print(output_line)
except Exception as e:
    print("Error has occured: ", e)      
