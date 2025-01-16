import requests

from urllib.parse import urlencode

BASE_URL = "https://api.docchi.pl/v1"
SITE_URL = "https://docchi.pl/api"
TIMEOUT = 30


class DocchiAPI:
    """
    Docchi API wrapper
    """

    def __init__(self):
        """
        Initialize the Docchi API wrapper
        """

    @staticmethod
    def get_anime_details(slug: str):
        """
        Get anime details from Docchi
        :param slug: anime slug
        :return: JSON response
        """

        if slug is None:
            raise Exception("A Valid Anime slug Must Be Provided")

        url = f'{BASE_URL}/series/find/{slug}'

        resp = requests.get(url=url, timeout=TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    @staticmethod
    def get_episode_players(slug: str, episode: int):
        """
        Get anime details from Docchi
        :param slug: anime slug
        :param episode: episode number
        :return: JSON response
        """

        if episode is None:
            raise Exception("A Valid episode number Must Be Provided")

        url = f'{BASE_URL}/episodes/find/{slug}/{episode}'

        resp = requests.get(url=url, timeout=TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    @staticmethod
    def get_slug_from_mal_id(mal_id: str):
        """
        Get anime details from Docchi
        :param mal_id: anime slug
        :return: slug
        """

        if mal_id is None:
            raise Exception("A Valid mal id Must Be Provided")

        url = f'{BASE_URL}/series/related/{mal_id}'

        resp = requests.get(url=url, timeout=TIMEOUT)
        resp.raise_for_status()
        related_items = resp.json()
        for item in related_items:
            if item['mal_id'] == int(mal_id):
                return item['slug']
        return None

    @staticmethod
    def get_available_episodes(slug: str):
        """
        Get anime details from Docchi
        :param slug: anime slug
        :return: JSON response
        """

        url = f'{BASE_URL}/episodes/count/{slug}'

        resp = requests.get(url=url, timeout=TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    @staticmethod
    def search_anime(name: str):
        """
        Get anime details from Docchi
        :param name: anime name
        :return: JSON response
        """

        if name is None:
            raise Exception("A valid search string Must Be Provided")

        url = f'{SITE_URL}/search/search'
        query_params = DocchiAPI.__to_query_string({'string': name})
        if query_params:
            url += f'?{query_params}'
        url += f'?{query_params}'

        resp = requests.get(url=url, timeout=TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    @staticmethod
    def get_anime_by_genre(genre: str):
        """
        Get anime details from Docchi
        :param genre: anime genre
        :return: JSON response
        """

        if genre is None:
            raise Exception("A valid genre Must Be Provided")

        url = f'{BASE_URL}/series/category?name={genre}&sort=DESC'

        resp = requests.get(url=url, timeout=TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    @staticmethod
    def get_anime_list(**kwargs):
        """
        Get anime list from Docchi
        :param kwargs: Additional query parameters
        :return: JSON response
        """

        url = f'{BASE_URL}/series/list'
        query_params = DocchiAPI.__to_query_string(kwargs)
        if query_params:
            url += f'?{query_params}'

        resp = requests.get(url=url, timeout=TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    @staticmethod
    def get_latest_episodes(**kwargs):
        """
        Get anime list from Docchi
        :param kwargs: Additional query parameters
        :return: JSON response
        """

        url = f'{BASE_URL}/episodes/latest'
        query_params = DocchiAPI.__to_query_string(kwargs)
        if query_params:
            url += f'?{query_params}'

        resp = requests.get(url=url, timeout=TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    @staticmethod
    def get_trending_anime(**kwargs):
        """
        Get trending anime list from Docchi
        :param kwargs: Additional query parameters
        :return: JSON response
        """

        url = f'{BASE_URL}/homepage/trending'
        query_params = DocchiAPI.__to_query_string(kwargs)
        if query_params:
            url += f'?{query_params}'

        resp = requests.get(url=url, timeout=TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    @staticmethod
    def get_seasonal_anime(season: str, year: str, **kwargs):
        """
        Get seasonal anime list from Docchi
        :param season: Season
        :param year: Year
        :param kwargs: Additional query parameters
        :return: JSON response
        """

        url = f'{BASE_URL}/homepage/season?season={season}&season_year={year}'
        query_params = DocchiAPI.__to_query_string(kwargs)
        if query_params:
            url += f'?{query_params}'

        resp = requests.get(url=url, timeout=TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    @staticmethod
    def __to_query_string(kwargs):
        """
        Convert Keyword arguments to a query string
        :param kwargs: The keyword arguments
        :return: query string
        """
        data = dict(**kwargs)
        return urlencode(data) if data else None
