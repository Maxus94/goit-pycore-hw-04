def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            file_content = file.readlines()
    except: 
        return "File not found or damaged"
    total_amount = 0
    for emploee in file_content:
        try:
            total_amount = total_amount + int(emploee.split(',')[-1])
        except: 
            return "Information in file is incorrect or invalid format"
    return(f"Загальна сума заробітної плати: {total_amount}, Середня заробітна плата: {int(total_amount/len(file_content))}")

# print(total_salary('salary.txt'))

def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            file_content = file.readlines()
    except:
        return "File not found or damaged"
    cats_info = []
    for cat in file_content:
        try:
            cat_info = cat.strip().split(',')
            cat_info = {"id":cat_info[0], "name":cat_info[1], "age":cat_info[2]}
            cats_info.append(cat_info)
        except:
            return "Information in file is incorrect or invalid format"
    return cats_info

# print(get_cats_info('cats.txt'))