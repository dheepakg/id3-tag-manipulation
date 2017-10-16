def fetch_tag_details(song_location,song_name,tag_output_file,delimiter):
    import mutagen

    song_file = song_location+song_name
    song_tags = mutagen.File(song_file)
	#Fetches all the required tas from an mp3 file
    album = song_tags['TALB'].text[0]
    artist = song_tags['TPE1'].text[0]
    track_name = song_tags['TCOM'].text[0]
    year = song_tags['TDRC'].text[0]
    genre = song_tags['TCON'].text[0]
    track_number = song_tags['TRCK'].text[0]
    title = song_tags['TIT2'].text[0]
    song_writer = song_tags['TEXT'].text[0]
    length = song_tags.info.length
    length_mins = int(length / 60)
    length_secs = length % 60
    length_human_read = str(length_mins) + ':' + str(length_secs)[:2] + ' mins'

    header_data = 'album' + delimiter + 'artist' + delimiter + 'track_name' + delimiter + 'year' + delimiter + 'genre' + delimiter + \
                  'track_number' + delimiter + 'title' + delimiter + 'song_writer' + delimiter + 'length'
    f = open(tag_output_file, 'w')
    f.write(header_data + '\n')
    f.close

    tag_data = album + delimiter + artist + delimiter + track_name + delimiter + str(
        year) + delimiter + genre + delimiter + track_number + \
               delimiter + title + delimiter + song_writer + delimiter + str(length_human_read)
	#writing tag details into a flat file for further processing
    f = open(tag_output_file,'a')
    #f.write(header_data + '\n')
    f.write(tag_data + '\n')
    f.close