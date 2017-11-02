def insights_mp3(file_path):
    import pandas as pd
    extract_path = file_path  # 'C:\\Users\\dheepak\\Desktop\\Projects\\test.csv'
    df = pd.read_csv(extract_path, sep='|')

    album_count = len(df.album.unique())

    composer_count = len(df.track_name.unique())
    album_len = df["length(secs)"].mean()

    album_len_mins = int(album_len / 60)
    album_len_secs = int((album_len % 60) )
    com = df.groupby(['track_name']).size().reset_index(name='tracks').sort_values(['tracks'], ascending=False).head(3)
    top_composers = list(com.track_name.values)

    print("Total number of columns ", len(df.index))
    print("Average length of the songs that I hear", album_len_mins, ':', round(album_len_secs, 2), ' mins')
    print("On average the ALbum was released on ", int(round(df["year"].mean(), 0)))
    print("Tracks are spread across", album_count, " Albums")
    print("These songs are composed by ", composer_count, " Composers")
    print("Top Composers")

    if len(top_composers) < 3:
        for composers in top_composers:
            print('\t\t',composers)
    else:
        for composers in top_composers[:3]:
            print('\t\t',composers)
