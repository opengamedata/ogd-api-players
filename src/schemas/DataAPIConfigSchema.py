"""
ServerConfigSchema

Contains a Schema class for managing config data for server configurations.
"""

# import standard libraries
import logging
from pathlib import Path
from typing import Any, Dict, List

# import 3rd-party libraries

# import OGD libraries
from ogd.core.schemas.configs.data_sources.MySQLSourceSchema import MySQLSchema
from ogd.apis.configs.ServerConfig import ServerConfig

# import local files

class DataAPIConfigSchema(ServerConfig):
    """_summary_

    TODO : Rename to PlayerAPIConfig

    :param ServerConfig: _description_
    :type ServerConfig: _type_
    """
    def __init__(self, name:str, all_elements:Dict[str, Any], logger:logging.Logger):
        self._state_dbs        : Dict[str, MySQLSchema]
        self._ogd_core         : Path
        self._google_client_id : str
        self._dbg_level        : int
        self._version          : int

        if "DB_CONFIG" in all_elements.keys():
            self._data_src = DataAPIConfigSchema._parseDataSources(all_elements["DB_CONFIG"], logger=logger)
        else:
            self._data_src = {}
            logger.warning(f"{name} config does not have a 'DB_CONFIG' element; defaulting to game_sources={self._data_src}", logging.WARN)
        if "OGD_CORE_PATH" in all_elements.keys():
            self._ogd_core = DataAPIConfigSchema._parseOGDPath(path=all_elements["OGD_CORE_PATH"], logger=logger)
        else:
            self._ogd_core = Path("./") / "opengamedata"
            logger.warning(f"{name} config does not have a 'OGD_CORE_PATH' element; defaulting to ogd_core_path={self._ogd_core}", logging.WARN)
        if "GOOGLE_CLIENT_ID" in all_elements.keys():
            self._google_client_id = DataAPIConfigSchema._parseGoogleID(google_id=all_elements["GOOGLE_CLIENT_ID"], logger=logger)
        else:
            self._google_client_id = "UNKNOWN ID"
            logger.warning(f"{name} config does not have a 'GOOGLE_CLIENT_ID' element; defaulting to google_client_id={self._google_client_id}", logging.WARN)

        _used = {"DB_CONFIG", "OGD_CORE_PATH", "GOOGLE_CLIENT_ID"}
        _leftovers = { key : val for key,val in all_elements.items() if key not in _used }
        super().__init__(
            name=name,
            debug_level=None,
            version=None,
            other_elements=_leftovers
        )

    @property
    def StateDatabases(self) -> Dict[str, MySQLSchema]:
        return self._state_dbs

    @property
    def OGDCore(self) -> Path:
        return self._ogd_core

    @property
    def GoogleClientID(self) -> str:
        return self._google_client_id

    @property
    def AsMarkdown(self) -> str:
        ret_val : str

        ret_val = f"{self.Name}"
        return ret_val

    @staticmethod
    def _parseDataSources(sources, logger:logging.Logger) -> Dict[str, MySQLSchema]:
        ret_val : Dict[str, MySQLSchema]
        if isinstance(sources, dict):
            ret_val = {}
            for key,val in sources.items():
                ret_val[key] = MySQLSchema(name=key, all_elements=val)
        else:
            ret_val = {}
            logger.warning(f"Config data sources was unexpected type {type(sources)}, defaulting to empty dict: {ret_val}.", logging.WARN)
        return ret_val

    @staticmethod
    def _parseOGDPath(path, logger:logging.Logger) -> Path:
        ret_val : Path
        if isinstance(path, str):
            ret_val = Path(path)
        else:
            ret_val = Path("./") / "opengamedata"
            logger.warning(f"Data Source DB type was unexpected type {type(path)}, defaulting to path={ret_val}.", logging.WARN)
        return ret_val

    @staticmethod
    def _parseGoogleID(google_id, logger:logging.Logger) -> str:
        ret_val : str
        if isinstance(google_id, str):
            ret_val = google_id
        else:
            ret_val = str(google_id)
            logger.warning(f"Google Client ID type was unexpected type {type(google_id)}, defaulting to google_client_id=str({ret_val}).", logging.WARN)
        return ret_val
