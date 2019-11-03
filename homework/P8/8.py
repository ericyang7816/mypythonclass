import zipfile
# write files
z1 = zipfile.ZipFile("z1.zip", "w")
z1.write("1.txt")
z1.write("2.txt")
z1.close()
# extract files
z2 = zipfile.ZipFile("z1.zip")
z2.extractall()
z2.close()
