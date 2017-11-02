def fetch_tag_details(song_location,song_name,tag_output_file,delimiter):
    import mutagen

    song_file = song_location+song_name
    song_tags = mutagen.File(song_file)

    try:
        album = song_tags['TALB'].text[0]
    except KeyError:
        album = 'NaN'
    try:
        artist = song_tags['TPE1'].text[0]
    except KeyError :
        artist = 'NaN'
    try:
        track_name = song_tags['TCOM'].text[0]
    except KeyError :
        track_name = 'NaN'
    try:
        year = song_tags['TDRC'].text[0]
    except KeyError :
        year = 'NaN'
    try:
        genre = song_tags['TCON'].text[0]
    except KeyError :
        genre = 'NaN'
    try:
        track_number = song_tags['TRCK'].text[0]
    except KeyError :
        track_number = 'NaN'
    try:
        title = song_tags['TIT2'].text[0]
    except KeyError:
        title = 'NaN'
    try:
        song_writer = song_tags['TEXT'].text[0]
    except KeyError :
        song_writer = 'NaN'
    length = song_tags.info.length


    tag_data = song_name+delimiter+album + delimiter + artist + delimiter + track_name + delimiter + str(
        year) + delimiter + genre + delimiter + track_number + \
               delimiter + title + delimiter + song_writer + delimiter + str(round(length,2))

    f = open(tag_output_file,'a')
    f.write(tag_data + '\n')
    f.flush()
