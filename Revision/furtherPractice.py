# 1. Open the 'records.txt' file in read mode
# 2. Populate a 2D list of records to hold the information (remember to strip new lines etc)
# 3. Print the contents in a nice format e.g.
# Record1: Bill Williams, age: 60, sport: football
# 4. Add a filter so that only those under an age inputted by the user are printed
# 4. In your 2D list, replace the 'RecordX' field with just a number e.g.
# e.g. Record1,Bill,Williams,60,football becomes 1,Bill,Williams,60,football

# Open the 'records.txt' file in read mode
with open('records.txt', 'r') as records:
    records_list = []
    for line in records:
        records_list.append(line.strip().split(','))


for i, record in enumerate(records_list):
    record[0] = str(i + 1)


print("All records:")
for record in records_list:
    print(f"{record[0]}: {record[1]} {record[2]}, age: {record[3]}, sport: {record[4]}")


age_limit = int(input("\nEnter an age limit to filter records: "))

print(f"\nRecords with age under {age_limit}:")
for record in records_list:
    if int(record[3]) < age_limit: 
        print(f"{record[0]}: {record[1]} {record[2]}, age: {record[3]}, sport: {record[4]}")
