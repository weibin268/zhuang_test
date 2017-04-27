with open("./temp_input.txt", 'r',encoding='utf-8') as file:
    content=file.read()
    
    lines = content.split('\n')

    str="select '"+r"' union all select '".join(lines)+"'"

    print(str)

    #print(content)

with open('./temp_output.txt','w',encoding='utf-8') as file:
    file.write(str)