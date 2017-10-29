def insights(file_path):
    import pandas as pd
    extract_path = file_path  # 'C:\\Users\\dheepak\\Desktop\\Projects\\test.csv'
    df = pd.read_csv(extract_path, sep='|')

    album_count = len(df.album.unique())

    composer_count = len(df.track_name.unique())
    album_len = df["length(mins)"].mean()
    album_len_mins = int(album_len % 10)
    album_len_secs = int((album_len % 1) * 100)
    com = df.groupby(['track_name']).size().reset_index(name='tracks').sort_values(['tracks'], ascending=False).head(3)
    top_composers = list(com.track_name.values)

    print("Total number of columns ", len(df.index))
    print("Average length of the songs that I hear", album_len_mins, ':', round(album_len_secs, 2), ' mins')
    print("On average the ALbum was released on ", int(round(df["year"].mean(), 0)))
    print("Tracks are spread across", album_count, " Albums")
    print("These songs are composed by ", composer_count, " Composers")
    print("Top composers are ", top_composers[0], top_composers[1], top_composers[2])