

with open('./temp_input.txt', 'r', encoding='utf-8') as file:

    CON = file.read()

    LINS = CON.split('\n')

    STR = "select '" + r"' union all select '".join(LINS) + "'"

    print(STR)

    #print(content)

with open('./temp_output.txt', 'w', encoding='utf-8') as file:
    file.write(STR)
