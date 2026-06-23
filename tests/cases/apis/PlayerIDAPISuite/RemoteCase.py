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

class t_PlayerIDAPI(TestCase):
    """Testbed class for the PlayerID API.
    """
    @classmethod
    def setUpClass(cls):
        cls.testing_config = PlayerAPITestConfig.FromDict(name="PlayerAPITestConfig", unparsed_elements=t_config.settings)

        _level = logging.DEBUG if cls.testing_config.Verbose else logging.INFO
        Logger.std_logger.setLevel(_level)

        cls.TEST_PLAYER_ID = "ImmortanJoe"
        cls.TEST_GAME      = "AQUALAB"

    def test_home(self):
        result = requests.get(url=self.testing_config.ExternEndpoint)
        if result is not None:
            print(f"Result of get:\n{result.text}")
        else:
            print(f"No response to GET request.")
        print()

    def test_get(self):
        url = f"{self.testing_config.ExternEndpoint}/player/"
        print(f"GET test at {url}")
        result = requests.get(url=url)
        if result is not None:
            print(f"Result of get:\n{result.text}")
        else:
            print(f"No response to GET request.")

    def test_put(self):
        url = f"{self.testing_config.ExternEndpoint}/player/"
        print(f"POST test at {url}")
        params = { "player_id":"test_player", "name":"Test" }
        result = requests.put(url=url, params=params)
        if result is not None:
            print(f"Result of post:\n{result.text}")
        else:
            print(f"No response to POST request.")