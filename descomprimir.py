import zipfile
import os

# Especificar o caminho do arquivo zip
zip_file_path = '/home/DuarteChen/project/static/meteo/icons_ipma_weather.zip'

# Especificar o diretório de destino
dest_dir = '/home/DuarteChen/project/static/meteo'

# Criar o diretório de destino, se não existir
os.makedirs(dest_dir, exist_ok=True)

# Descomprimir o arquivo zip
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(dest_dir)

print(f'Icons extracted to {dest_dir}')
