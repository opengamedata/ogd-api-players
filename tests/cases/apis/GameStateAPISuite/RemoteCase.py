# import libraries
import logging
import requests
from unittest import TestCase
# import ogd libraries
from ogd.apis.models.APIRequest import APIRequest
from ogd.apis.models.APIResponse import APIResponse
from ogd.common.utils.Logger import Logger
# import locals
from tests.PlayerAPITestConfig import PlayerAPITestConfig
from tests.config import t_config

class t_GameStateAPI(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.testing_config = PlayerAPITestConfig.FromDict(name="PlayerAPITestConfig", unparsed_elements=t_config.settings)

        _level = logging.DEBUG if cls.testing_config.Verbose else logging.INFO
        Logger.std_logger.setLevel(_level)
        cls.TEST_PLAYER_ID = "ImmortanJoe"
        cls.TEST_GAME      = "AQUALAB"

    def test_home(self):
        print(f"GET test at {self.testing_config.ExternEndpoint}")
        result = requests.get(url=base)
        if result is not None:
            print(f"Result of get:\n{result.text}")
        else:
            print(f"No response to GET request.")
        print()

    def test_get(self):
        url = f"{self.testing_config.ExternEndpoint}/player/{self.TEST_PLAYER_ID}/game/{self.TEST_GAME}/state"
        print(f"GET test at {url}")
        params = { 'count':1, 'offset':0 }
        result = requests.get(url=url, params=params)
        if result is not None:
            print(f"Result of get:\n{result.text}")
        else:
            print(f"No response to GET request.")

    def test_get_multi(self):
        url = f"{self.testing_config.ExternEndpoint}/player/{self.TEST_PLAYER_ID}/game/{self.TEST_GAME}/state"
        print(f"GET test at {url}")
        params = { 'count':3, 'offset':0 }
        result = requests.get(url=url, params=params)
        if result is not None:
            print(f"Result of get:\n{result.text}")
        else:
            print(f"No response to GET request.")

    def test_post(self):
        url = f"{self.testing_config.ExternEndpoint}/player/{self.TEST_PLAYER_ID}/game/{self.TEST_GAME}/state"
        print(f"POST test at {url}")
        params = { 'state':"{'data':'test data'}" }
        result = requests.post(url=url, params=params)
        if result is not None:
            print(f"Result of post:\n{result.text}")
        else:
            print(f"No response to POST request.")