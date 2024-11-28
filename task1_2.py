def total_salary(path):
    with open(path, 'r', encoding='utf-8') as file:
        file_content = file.readlines()        
    total_amount = 0
    for emploee in file_content:
        total_amount = total_amount + int(emploee.split(',')[-1])
    return(total_amount, total_amount/len(file_content))

print(total_salary('salary.txt'))