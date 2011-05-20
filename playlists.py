import os
import pickle
from os.path import join, getsize

startdir_default = 'c:/bak/musik'

print "\n\nCreating playlists for all directories containing mp3-files!\n"
print "default directory:", startdir_default
startdir = str(raw_input("input for new starting directory (or 'enter' for default): "))
if not startdir:
    startdir = startdir_default


list_mp3 = list()
    
for root, dirs, files in os.walk(startdir):
    
    mp3_files = str()
    for filename in files:
        if str.lower(filename[-4:]) == '.mp3':
            mp3_files += filename + "\n"
            #mp3.append("\n")
    
    if mp3_files:
        tmp_list = [root, os.path.split(root)[1], len(mp3_files), mp3_files]
        list_mp3.append(tmp_list)

if list_mp3:
    print "\n\nwriting playlists...\n\n"
else:
    print"\n\nNothing to write!\n"

for playlist in list_mp3:
    m3u_filename = "0-" + playlist[1] + ".m3u"
    m3u_path = playlist[0]
    m3u_file = m3u_path + "/" + m3u_filename
   
    print "playlist name:", m3u_filename
    print "\nsongs:\n", playlist[3]

    myfile = file(m3u_file, "w")
    myfile.write(playlist[3])
    myfile.close()
    print "Playlist written!\n\n"

print "all done..."
