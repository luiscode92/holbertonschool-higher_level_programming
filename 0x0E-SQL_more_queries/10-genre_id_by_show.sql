-- List all shows in hbtn_0d-tvshows with at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show LEFT JOIN tv_show_genres ON tv_show.id = tv_show_genres.show_id WHERE tv_show_genres.genre_id IS NOT NULL ORDER BY tv_shows.title, tv_show_genres.genre_id;
