import datetime
import shutil
import os
ora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

origine = "/home/lulu/progetti_it/log_analyzer"
destinazione = "/home/lulu/backup"

if not os.path.exists(destinazione):
      os.makedirs(destinazione)

for file in os.listdir(origine):
    percorso = os.path.join(origine, file)
    if os.path.isfile(percorso):
        nome_backup = f"{file}_{ora}"
        shutil.copy(
            percorso,
            os.path.join(destinazione, nome_backup)
        )
        print(f"Copiato: {file} - {nome_backup}")



