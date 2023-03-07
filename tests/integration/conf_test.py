from shutil import copy

import pytest
from farm_api.api import create_app
from farm_api.constants import INGRID_FARM_DATABASE, PROJECT_ROOT


@pytest.fixture
def client(tmpdir):
    copy(f"{PROJECT_ROOT}/{INGRID_FARM_DATABASE}", tmpdir.dirpath())

    temp_db_file = f"sqlite:///{tmpdir.dirpath()}/{INGRID_FARM_DATABASE}"

    app = create_app(temp_db_file)
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client