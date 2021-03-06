import recommender

def auto_rec_add(username, add_tracks='max', clientID = '<>', clientSecret = '<>'):
    pl_uri = raw_input('Please enter playlist URI: ')
    uri = pl_uri.split(':')[-1]
    username = username.split(':')[-1]

    test_class = recommender.recommender(username=username, clientID=clientID, clientSecret=clientSecret)
    print('Token Retrieved')
    test_class.create_user_instance()
    print('User Instance Created')
    test_class.user_get_playlist_tracks(uri)
    print('Playlist Tracks Retrieved')
    test_class.user_get_playlist_track_audio_feat()
    print('Track features Retrieved')
    test_class.user_playlist_recommend_tracks()
    print('Tracks recommended')
    test_class.user_playlist_add_tracks(playlist_id=uri, num_tracks_add=add_tracks)


if __name__ == '__main__':
    username = raw_input('Playlist Owner URI: ')
    clientID = raw_input('clientID: ')
    clientSecret = raw_input('clientSecret: ')
    auto_rec_add(username=username, clientID= clientID, clientSecret=clientSecret)