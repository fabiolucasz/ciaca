
import os
# usar o docling para transformar a apostila.md em um arquivo pdf
path = "juventude no mundo do trabalho/apostila.md"
if not os.path.exists(path):
    raise FileNotFoundError(f"Arquivo {path} não encontrado")

# TODO: usar o docling para transformar o arquivo md em pdf


    