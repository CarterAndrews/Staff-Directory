#error on line 176. Requires matching div tag
print("hello world")
import os
import errno
import csv
file_contents=""
name_list=""
with open("ProfileTemplate.pcf", "r") as f:
    file_contents=f.read()
with open("names.csv", newline='') as f:
    reader = csv.reader(f)
    name_list=list(reader)
for row in name_list:

    filename="output/"+row[0].lower()+".pcf"
    file_version=file_contents
    file_version=file_version.replace("*name*",row[0].replace("-"," ").title())
    with open(filename, "w") as f:
        f.write(file_version)