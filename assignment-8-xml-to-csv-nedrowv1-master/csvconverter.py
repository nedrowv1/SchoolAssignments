import xml.etree.ElementTree as xml
import sys


def UnexpectedError(type="r"):
    if type == "r":
        txt = "reading"
    elif type == "w":
        txt = "writing to"
    else:
        txt = "with"
    print("There was an unexpected error {} the file.  Please check the data and restart the program.".format(txt))
    sys.exit()


def xml_to_csv(xml_file, csv_file="csv_file.csv"):
    csv_file_to_write = open(csv_file, "w")  # look up cyclomatic complexity if you haven't
    try:
        orig_xml = xml.parse(xml_file)
    except FileNotFoundError:
        print("The file or directory supplied was not found.  Please check that the filename is spelled correctly.")
        exit()
    except IOError:
        UnexpectedError("r")
    top_of_file = orig_xml.getroot()
    tags = []
    for item in top_of_file:
        for data in item:
            tags.append('"' + data.tag + '",')
        tags[-1] = tags[-1][:-1]
        break
    for cell in tags:
        try:
            csv_file_to_write.write(str(cell))
        except IOError:
            UnexpectedError("w")

    try:
        csv_file_to_write.write("\n")
    except IOError:
        UnexpectedError("w")

    for item in top_of_file:
        tags = []
        for data in item:
            tags.append('"' + data.text + '",')
        tags[-1] = tags[-1][:-1]
        for cell in tags:
            try:
                csv_file_to_write.write(str(cell))
            except IOError:
                UnexpectedError("w")
        try:
            csv_file_to_write.write("\n")
        except IOError:
            UnexpectedError("w")


if __name__ == "__main__":
    my_file = input("Enter file path.  If in root directory, you may enter filename only.\n>>>")
    csv_file_name = input("Enter the file name for the csv file.  Unless path specified, it will save in "
                          "the root directory.\n>>>")
    if csv_file_name[-3:] != "csv":
        if csv_file_name[-4] != ".":
            csv_file_name += ".csv"
        else:
            not_CSV = input("This will save your file as a {} not a .csv file.  "
                            "Continue?".format(csv_file_name[-4:]))
            if "n".casefold() in not_CSV.casefold():
                print("Exiting program.")
                exit()
    xml_to_csv(my_file, csv_file_name)

# Great work as always.  You didn't want to reinvent the XML reading function?
# Search cyclomatic complexity if you haven't previously.  Also, the file is
# written to the working directory not root directory on Windows (not sure about others).
