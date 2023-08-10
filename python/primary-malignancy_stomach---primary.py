# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"100584.0","system":"med"},{"code":"14800.0","system":"med"},{"code":"19318.0","system":"med"},{"code":"21620.0","system":"med"},{"code":"22894.0","system":"med"},{"code":"32022.0","system":"med"},{"code":"32362.0","system":"med"},{"code":"37859.0","system":"med"},{"code":"41215.0","system":"med"},{"code":"42193.0","system":"med"},{"code":"43572.0","system":"med"},{"code":"48237.0","system":"med"},{"code":"49447.0","system":"med"},{"code":"51690.0","system":"med"},{"code":"55019.0","system":"med"},{"code":"55434.0","system":"med"},{"code":"59092.0","system":"med"},{"code":"65312.0","system":"med"},{"code":"65372.0","system":"med"},{"code":"8386.0","system":"med"},{"code":"94278.0","system":"med"},{"code":"96094.0","system":"med"},{"code":"96802.0","system":"med"},{"code":"97499.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_stomach-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["primary-malignancy_stomach---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["primary-malignancy_stomach---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["primary-malignancy_stomach---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
