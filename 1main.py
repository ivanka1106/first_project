import datetime

now = datetime.datetime.now()
print(now)

specific_date = datetime.datetime(year=2024, month=6, day=11)

print(specific_date)  

from datetime import datetime

current_date = datetime.now()
print(now)

days_since = current_date.toordinal() - specific_date.toordinal()
    
print(days_since)

