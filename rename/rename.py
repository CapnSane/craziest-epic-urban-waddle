import os

# Path para a pasta jorge
path = "rename/jorge"

# Entra na pasta
os.chdir(path)
  
# Lê o arquivo
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())
  
  
# iterate through all file
# Renomeia arquivos começando do número 1
i = 1
for file in os.listdir():
    os.system(f'mv {file} {i}.tex')
    i += 1
    print(file)