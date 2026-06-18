# opengamedata-api-players

Repository for the OpenGameData Player ID + Game-State Saving API. These allow users of `opengamedata-unity` and `opengamedata-js-log` to obtain randomly-generated IDs to display for users, which can then be used to save and restore game states.

## API Endpoints

Below is a listing of the current API calls available, in function format to indicate what the request parameters.
For each API, there is also an api path, with path parameters in angle bracket (<, >) format.
Lastly, at this point in time, the `<server_path>` is `https://fieldday-web.wcer.wisc.edu/opengamedata.wsgi`

### Player ID API

#### Generate and save players

`<server_path>/player`  
`GET()`

* returns an unused, randomized player name, or a null value and error message  

`PUT(str player_id, str name = None)`

* Returns no value, and either a success or error message  

---

### Players API

#### Save and retrieve game states

`<server_path>/player/<player_id>/game/<game_id>/state:`  
`GET(int count = 1, int offset = 0)`  

* Returns a list of game states, length == count, starting from the nth most-recent state, where n == offset, or a null value and an error message.

`POST(str state)`

* Attemps to save the state. Returns a null value and a success/error message.

### Hello API

#### Verify the API is alive

`<server_path>/hello`  
`GET()`

* returns no value, and a success message  

`POST()`

* returns no value, and a success message

`PUT()`

* returns no value, and a success message

## Developer Instructions

### Running the app locally via the development Flask server

Steps to run:

1. Ensure you have Python and pip installed in your development environment.
2. (optional) From the project root folder, run `python -m venv .venv` to create the `.venv` directory that will contain the virtual environment.
3. (optional) Activate the environment with `source .venv/bin/activate` on Mac/Linux, or `.venv/Scripts/activate` on Windows.
4. From the app's root directory run `pip install -r requirements.txt` to ensure you have Flask and other dependencies installed for the app.
5. Set up configuration files:
    * Copy `src/config/config.py.template` to `src/config/config.py` to create a config. Update `config.py` configuration values as needed.
    * Copy `src/config/coreconfig.py.template` to `src/config/coreconfig.py` to create a config. Update `coreconfig.py` configuration values as needed.
6. Enter the source folder with `cd src` and then run `python -m flask run`, or optionally include the `--debug` flag.
    * Optionally, you can run `export FLASK_APP=src/app.wsgi` in order to run from the root project directory.
7. A web server should begin running at `http://localhost:5000`
8. Open localhost:5000 or localhost:5000/hello to verify that the server has started correctly and is able to service a request.
