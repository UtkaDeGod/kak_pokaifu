import requests


class YandexAPI:
    static_map_adress = 'https://static-maps.yandex.ru/1.x/'

    def get_map_image(self, ll='42.028803,45.129667', z=17, l='map'):
        params = {'ll': ll, 'z': z, 'l': l}
        response = requests.get(self.static_map_adress, params=params)
        if response:
            return response.content
        return None
