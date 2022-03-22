import os
import shutil

folder = "A:\\Samples\\KKL SoundFX\\Sound Ideas\\6040\\"
refdir = "A:\\Samples\\Ljudbang Filmljudeffekter\\General6000\\6040_Sound Designer-Alan Horwarth"
newNames = []


#print(newNames)
os.chdir(folder)
print(os.getcwd())

print(folder)

#PYnative
for path in os.listdir(refdir):
    if os.path.isfile(os.path.join(refdir, path)):
        #Remove the mp3 extension
        pathname, extension = os.path.splitext(path)
        path = pathname
        #Append the filename to the list
        newNames.append(path)
print(newNames[0])

i = 0

for file_name in os.listdir(folder):
    source = folder + file_name

    # Adding the new name to the file
    destination = folder + str(newNames[i]) + ".wav"
    os.rename(source, destination)
    i +=1

print('All files have been renamed,')
print('New filenames are')
# verify the result
res = os.listdir(folder)
print(res)


#for i in os.walk():
#    shutil.move(, refdir\\newNames[i])