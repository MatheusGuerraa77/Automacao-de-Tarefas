from pathlib import Path
from datetime import datetime

path = Path('files', 'dados', 'a.txt')

# print(path.stat())
stats = path.stat()
second_created = stats.st_ctime
date_created = datetime.fromtimestamp(second_created)
# print(date_created)
date_created_str = date_created.strftime('%Y-%m-%d_%H_%M_%S')
print(date_created_str)

# st_ctime=1721791457
# st_ctime=1721792007