import csv

import pandas as pd
df = pd.read_csv(
  "rat.9.690389633178711-53.39692306518555.csv",
  index_col=0,
  parse_dates=True
)
columns = 4
train_data = [tuple(values) for values in df.iloc[:1122, 0:columns].values]

test_data=[tuple(values) for values in df.iloc[1122:, 0:columns].values]
#print(len(test_data))

#print(test_data[1])
scores = pd.DataFrame(index=range(len(test_data)))

for column in range(4):
    scores[column] = None
    with open("histogram{}.csv".format(column + 1)) as csvfile:
        reader = csv.DictReader(
            csvfile, fieldnames=["start","stop","diff","nor"]
        )
        rows = list(reader)[1:]
    for index in range(len(test_data)):
        for row in rows:
            if (test_data[index][column] >= float(row["start"])) and (test_data[index][column] <= float(row["stop"])
            ):
                scores[column][index] = float(row["nor"])

scores = scores.transpose()
average_scores = scores.sum() / len(scores)

with open("result_hbos.csv", "w") as f5:
    writer = csv.writer(f5)
    writer.writerow(["Data","Score","Is_outlier?"])
    for s in range(len(test_data)):
        if average_scores[s]>.6:
            th=0
        else:
            th=1
        writer.writerow((test_data[s],)+(average_scores[s],)+(th,))
        
#print(average_scores)
