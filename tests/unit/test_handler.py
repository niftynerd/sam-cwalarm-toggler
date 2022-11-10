import json

import pytest

from toggle_alarms import app


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "enable": "false",
        "alarm": ["alarm1", "alarm2", "alarm3"]
    }


def test_lambda_handler(apigw_event, mocker):

    ret = app.lambda_handler(apigw_event, "")
    print("ret",ret)
    data = json.loads(f'{ret["statusCode"]}')

    assert ret["statusCode"] == 200
    assert "statusCode" in ret
    assert data == 200
    # assert "location" in data.dict_keys()
