import json
import data as data

with open("teachers.txt", "w") as f:
   json.dump(data.teachers, f)

with open("goals .txt", "w") as f:
   json.dump(data.goals , f)