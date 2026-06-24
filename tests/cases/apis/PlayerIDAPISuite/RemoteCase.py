# import libraries
import logging
from unittest import TestCase
# import ogd libraries
from ogd.apis.models.APIRequest import APIRequest
from ogd.apis.models.APIResponse import APIResponse
from ogd.apis.models.enums.RESTType import RESTType
from ogd.common.utils.Logger import Logger
# import locals
from tests.PlayerAPITestConfig import PlayerAPITestConfig
from tests.config import t_config

class t_PlayerIDAPI(TestCase):
    """Testbed class for the PlayerID API.
    """
    @classmethod
    def setUpClass(cls):
        cls.testing_cfg = PlayerAPITestConfig.FromDict(name="PlayerAPITestConfig", unparsed_elements=t_config.settings)
        Logger.InitializeLogger(
            level       = logging.DEBUG if cls.testing_cfg.Verbose else logging.INFO,
            use_logfile = False
        )
        cls.TEST_PLAYER_ID = "ImmortanJoe"
        cls.TEST_GAME      = "AQUALAB"

    def test_home(self):
        url=self.testing_cfg.ExternEndpoint
        # 1. Run request
        try:
            response : APIResponse = APIRequest(
                url=url,
                request_type=RESTType.GET,
                params={},
                timeout=2
            ).Execute(logger=Logger.std_logger)
        except Exception as err: # pylint: disable=broad-exception-caught
            self.fail(str(err))
        else:
        # 2. Perform assertions
            self.assertIsNotNone(response, f"No response from {url}")
            self.assertTrue(response.OK, f"Bad status from {url}: {response.Status}")
            self.assertEqual(response.Type, RESTType.GET, f"Bad type from {url}")
            self.assertIsNone(response.Value, f"Bad value type from {url}")

    def test_get(self):
        url = f"{self.testing_cfg.ExternEndpoint}/player/"
        try:
            response : APIResponse = APIRequest(
                url=url,
                request_type=RESTType.GET,
                params={},
                timeout=2
            ).Execute(logger=Logger.std_logger)
        except Exception as err: # pylint: disable=broad-exception-caught
            self.fail(str(err))
        else:
        # 2. Perform assertions
            self.assertIsNotNone(response, f"No response from {url}")
            self.assertTrue(response.OK, f"Bad status from {url}: {response.Status}")
            self.assertEqual(response.Type, RESTType.GET, f"Bad type from {url}")
            self.assertIsNone(response.Value, f"Bad value type from {url}")

    def test_put(self):
        url = f"{self.testing_cfg.ExternEndpoint}/player/"
        try:
            response : APIResponse = APIRequest(
                url=url,
                request_type=RESTType.POST,
                params={ "player_id":"test_player", "name":"Test" },
                timeout=2
            ).Execute(logger=Logger.std_logger)
        except Exception as err: # pylint: disable=broad-exception-caught
            self.fail(str(err))
        else:
        # 2. Perform assertions
            self.assertIsNotNone(response, f"No response from {url}")
            self.assertTrue(response.OK, f"Bad status from {url}: {response.Status}")
            self.assertEqual(response.Type, RESTType.POST, f"Bad type from {url}")
            self.assertIsNone(response.Value, f"Bad value type from {url}")