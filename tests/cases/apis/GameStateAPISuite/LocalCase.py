# import libraries
import logging
from json.decoder import JSONDecodeError
from unittest import TestCase
# import 3rd-party libraries
from flask import Flask
# import ogd libraries
from ogd.apis.models.APIRequest import APIRequest
from ogd.apis.models.APIResponse import APIResponse
from ogd.apis.models.enums.RESTType import RESTType
from ogd.common.utils.Logger import Logger
# import locals
from src.schemas.DataAPIConfigSchema import DataAPIConfigSchema
from src.apis.GameStateAPI import GameStateAPI
from tests.PlayerAPITestConfig import PlayerAPITestConfig
from tests.config import t_config

class LocalCase(TestCase):
    @classmethod
    def setUpClass(cls):
        testing_cfg = PlayerAPITestConfig.FromDict(name="PlayerAPITestConfig", unparsed_elements=t_config.settings)

        _level     = logging.DEBUG if testing_cfg.Verbose else logging.INFO
        _str_level =       "DEBUG" if testing_cfg.Verbose else "INFO"
        Logger.InitializeLogger(level=_level, use_logfile=False)

        # 2. Set up local Flask app to run tests
        cls.application = Flask(__name__)
        cls.application.logger.setLevel(_level)
        cls.application.secret_key = b'thisisafakesecretkey'

        _server_cfg_elems = {
            "DB_CONFIG":
            {
                "id_gen": {
                    "DB_HOST" : "127.0.0.1",
                    "DB_USER" : "username",
                    "DB_PW"   : "password",
                    "DB_NAME" : "id_generator",
                    "DB_PORT" : 3306
                },
                "fd_users": {
                    "DB_HOST" : "127.0.0.1",
                    "DB_USER" : "username",
                    "DB_PW"   : "password",
                    "DB_NAME" : "fieldday_users",
                    "DB_PORT" : 3306
                }
            },
            "OGD_CORE_PATH":"Path/To/opengamedata-core",
            "GOOGLE_CLIENT_ID":"client_id",
            "DEBUG_LEVEL":"INFO",
            "VER":0
        }
        _server_cfg = DataAPIConfigSchema.FromDict(name="HelloAPITestServer", unparsed_elements=_server_cfg_elems)
        GameStateAPI.register(app=cls.application, settings=_server_cfg)

        cls.server = cls.application.test_client()
        cls.TEST_PLAYER_ID = "ImmortanJoe"
        cls.TEST_GAME      = "AQUALAB"

    def test_home(self):
        url = self.testing_cfg.ExternEndpoint
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
        url = f"{self.testing_cfg.ExternEndpoint}/player/{self.TEST_PLAYER_ID}/game/{self.TEST_GAME}/state"
        try:
            response : APIResponse = APIRequest(
                url=url,
                request_type=RESTType.GET,
                params={ 'count':1, 'offset':0 },
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

    def test_get_multi(self):
        url = f"{self.testing_cfg.ExternEndpoint}/player/{self.TEST_PLAYER_ID}/game/{self.TEST_GAME}/state"
        try:
            response : APIResponse = APIRequest(
                url=url,
                request_type=RESTType.GET,
                params={ 'count':3, 'offset':0 },
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

    def test_post(self):
        url = f"{self.testing_cfg.ExternEndpoint}/player/{self.TEST_PLAYER_ID}/game/{self.TEST_GAME}/state"
        try:
            response : APIResponse = APIRequest(
                url=url,
                request_type=RESTType.POST,
                params={ 'state':"{'data':'test data'}" },
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