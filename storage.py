import csv 

all_art = []
liked_art = []
disliked_art = []

with open("final.csv","r",errors = "ignore") as f:
    reader = csv.reader(f)
    reader = list(reader)
    all_art = reader[1:]