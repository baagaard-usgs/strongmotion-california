import csv

edc = []
vdc = []

with open("earthquakes_pre2000.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter="|")
    for row in reader:
        if row["EDC Name"] != "-999":
            edc.append(row["EDC Name"])
        if row["VDC id"] != "-999":
            vdc.append((row["VDC Name"], row["VDC id"],))

print("Engineering Data Center\n")
for eq in edc:
    print(eq)


print("\nVirtual Data Center\n")
for eq,eqid in vdc:
    print("{} {}".format(eq, eqid))

