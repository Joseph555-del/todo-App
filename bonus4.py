filenames = ["1.Raw Date.txt", "2.Reports.txt", "3.Presentaton.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)