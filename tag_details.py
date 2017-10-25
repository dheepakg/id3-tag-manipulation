def fetch_tag_details(song_location,song_name,tag_output_file,delimiter):
    import mutagen

    song_file = song_location+song_name
    song_tags = mutagen.File(song_file)

    try:
        album = song_tags['TALB'].text[0]
    except KeyError:
        album = 'error'
    try:
        artist = song_tags['TPE1'].text[0]
    except KeyError :
        artist = 'error'
    try:
        track_name = song_tags['TCOM'].text[0]
    except KeyError :
        track_name = 'error'
    try:
        year = song_tags['TDRC'].text[0]
    except KeyError :
        year = 'error'
    try:
        genre = song_tags['TCON'].text[0]
    except KeyError :
        genre = 'error'
    try:
        track_number = song_tags['TRCK'].text[0]
    except KeyError :
        track_number = 'error'
    try:
        title = song_tags['TIT2'].text[0]
    except KeyError:
        title = 'error'
    try:
        song_writer = song_tags['TEXT'].text[0]
    except KeyError :
        song_writer = 'error'
    length = song_tags.info.length
    length_mins = int(length / 60)
    length_secs = length % 60
    length_human_read = str(length_mins) + ':' + str(length_secs)[:2]

    tag_data = song_name+delimiter+album + delimiter + artist + delimiter + track_name + delimiter + str(
        year) + delimiter + genre + delimiter + track_number + \
               delimiter + title + delimiter + song_writer + delimiter + str(length_human_read)

    f = open(tag_output_file,'a')
    f.write(tag_data + '\n')
    f.flush()
