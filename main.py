# import
import os;

# init empty list
list = [];

# import
import os;
import json;

# init empty list
list = [];

# init empty csv
csv = "";

# init file path
filepath = "username-password-recovery-code.csv";

# read csv from file
if os.path.exists(filepath):
    file = open(filepath, "r");
    csv = file.read();
    file.close();
else:
    print("Warning: file does not exits.");
    print("Path: " + filepath);

# split file into rows
rows = csv.split("\n");

# go for each row
for i in range(0, len(rows)):

    # skip first line, it is header
    if i > 0:

        # split row into columns
        columns = rows[i].split(";");

        # init new empty dictionary
        dictionary = {};

        # go for each column
        for j in range(0, len(columns)):

            # write each column into dictionary
            if j == 0:
                dictionary["Username"] = columns[j];
            elif j == 1:
                dictionary["Identifier"] = columns[j];
            elif j == 2:
                dictionary["One-time password"] = columns[j];
            elif j == 3:
                dictionary["Recovery code"] = columns[j];
            elif j == 4:
                dictionary["First name"] = columns[j];
            elif j == 5:
                dictionary["Last name"] = columns[j];
            elif j == 6:
                dictionary["Department"] = columns[j];
            elif j == 7:
                dictionary["Location"] = columns[j];

        # append dictionary to list
        list.append(dictionary)


# print
print(json.dumps(list, indent=4));