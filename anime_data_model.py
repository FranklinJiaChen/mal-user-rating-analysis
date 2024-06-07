"""
Anime object classes
"""

class Anime:
    def __init__(self, anime_data) -> None:
        """
        anime_data - data of the anime from MAL API

        anime_id - ID of the anime in MyAnimeList
        title - title of the anime
        rating - rating of the anime
        """
        self.id = anime_data['id']
        self.title = anime_data['title']
        self.rating = anime_data['mean']

    def get_mal_link(self) -> str:
        return f"https://myanimelist.net/anime/{self.id}"

    def __repr__(self) -> str:
        return f"{self.title}"


class UserAnime(Anime):
    def __init__(self, anime_data, user_rating) -> None:
        """
        user_rating - rating of the anime by the user
        """
        super().__init__(anime_data)
        self.user_rating = user_rating