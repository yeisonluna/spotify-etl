-- Consultas SQL de análisis

-- Canciones más escuchadas

SELECT track_name, COUNT(*) AS play_count
FROM spotify_tracks
GROUP BY track_name
ORDER BY play_count DESC;

-- Artistas más escuchados

SELECT artist, COUNT(*) AS play_count
FROM spotify_tracks
GROUP BY artist
ORDER BY play_count DESC;

-- Popularidad promedio de las canciones escuchadas

SELECT AVG(popularity) AS avg_popularity
FROM spotify_tracks;

-- Duración promedio de las canciones escuchadas
SELECT AVG(duration_min) AS avg_duration
FROM spotify_tracks;