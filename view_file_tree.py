import os


print(os.walk("folder"))
print([i for i in os.walk('folder')])


for root, dirs, files in os.walk("folder"):
    path = root.split(os.sep)
    # print(root.count(os.sep))
    print((len(path)-1) * "----", os.path.basename(root))

    for file in files:
        print(len(path) * "----", file)
