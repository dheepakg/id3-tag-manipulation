def fetch_tag_header(song_location,song_name,tag_output_file,delimiter):
    header_data = 'file_name'+ delimiter+ 'album' + delimiter + 'artist' + delimiter + 'track_name' + delimiter + 'year' + delimiter + 'genre' + delimiter + \
                  'track_number' + delimiter + 'title' + delimiter + 'song_writer' + delimiter + 'length(mins)'
    f = open(tag_output_file, 'w')
    f.write(header_data + '\n')
    f.close
