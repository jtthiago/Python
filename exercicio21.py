import zipfile
import os

def compactar_arquivos(arquivo_zip, arquivos):
    with zipfile.ZipFile(arquivo_zip, 'w') as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo, os.path.basename(arquivo))
    print(f"Arquivos compactados em {arquivo_zip}")



arquivo_para_compactar = ['arquivo1.txt', 'arquivo2.txt']
compactar_arquivos('arquivos_compactados.zip', arquivo_para_compactar)