import os 

# 1 - Diretório raiz do SO
base_path = os.path.expanduser('~')
print(base_path)

# 2 - Navega no diretório dowwnload
path = os.path.join(base_path, 'Downloads')
print(path)
work_dir = os.chdir(path)

# 3 - Lista arquivos do diretório
list_files = os.listdir(work_dir)
# print(list_files)

# 4 - Criar Pastas
type_files = ['exe', 'csv', 'jpg', 'pdf', 'zip', 'txt', 'py', 'xlsx']
for type in type_files:
    if type not in os.listdir():
        os.mkdir(type)
        
# 5 - Organizando arquivos
for file in list_files:
    for type in type_files:
        if '.' +type in file:
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, type, file)
            os.replace(old_path, new_path)