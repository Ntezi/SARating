import sys
import json
import csv

ifilename = sys.argv[1]
try:
    ofilename = sys.argv[2]
except:
    ofilename = ifilename + ".csv"

# LOAD DATA
json_lines = [json.loads(l.strip()) for l in open(ifilename).readlines()]
OUT_FILE = open(ofilename, "w")
root = csv.writer(OUT_FILE)
root.writerow(
    ["date", "user_id", "text", "cool", "review_id", "stars", "useful", "business_id", "funny"])
json_no = 0
for l in json_lines:
    root.writerow(
        [l["date"], l["user_id"], l["text"], l["cool"], l["review_id"], l["stars"], l["useful"], l["business_id"],
         l["funny"]])
    json_no += 1

print('Finished {0} lines'.format(json_no))
OUT_FILE.close()