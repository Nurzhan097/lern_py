import zipfile
import os

# with open("file_test.txt", 'w', encoding="UTF-8") as f:
#     f.write("Hello page")


# def read_dir(folder):
#     for root, dirs, files in os.walk(folder):
#         print(f"{root.count(os.sep) * '----'} [{os.path.basename(root)}]")
#         for file in files:
#             print(f"{root.count(os.sep) * '----'} {file}")


# read_dir('folder')

# print(list(os.walk('folder')))

zip_file = zipfile.ZipFile("archive.zip", 'w', zipfile.ZIP_DEFLATED)
for folder in list(os.walk('folder')):
    zip_file.write(folder[0])
    for file in folder[2]:
        print(folder[0], file)
        zip_file.write(f"{folder[0]}{os.sep}{file}")

# zip_file.write('file_test.txt')

zip_file.close()