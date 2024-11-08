# utils/spotify_api.py
def get_recently_played(sp):
    results = sp.current_user_recently_played(limit=100)
    track_data = []
    for item in results['items']:
        track = item['track']
        track_data.append({
            'track_id': track['id'],
            'track_name': track['name'],
            'artist': track['artists'][0]['name'],
            'album': track['album']['name'],
            'duration_ms': track['duration_ms'],
            'popularity': track['popularity'],
            'played_at': item['played_at']
        })
    return track_data
