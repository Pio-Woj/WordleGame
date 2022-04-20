
with open(".\slowa.txt", "r", encoding="UTF-8") as input_file, open(".\slowa_5_liter.txt","w", encoding="UTF-8") as output_file:
    for line in input_file:
        # 5 letter word plus "\n"
        if len(line) == 6:
            output_file.write(line)
