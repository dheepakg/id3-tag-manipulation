def fetch_tag_header(tag_output_file,delimiter):
    header_data = 'file_name'+ delimiter+ 'album' + delimiter + 'artist' + delimiter + 'track_name' + delimiter + 'year' + delimiter + 'genre' + delimiter + \
                  'track_number' + delimiter + 'title' + delimiter + 'song_writer' + delimiter + 'length(secs)'
    f = open(tag_output_file, 'w')
    f.write(header_data + '\n')
    f.close