import pytest
from flask import json
from unittest.mock import Mock, patch

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def mock_gpt_api():
    with patch('app.imitate_style', return_value="Generated text") as mock_imitate_style:
        yield mock_imitate_style

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_submit(client):
    test_data = {
        "text_inputs": ["Text 1", "Text 2", "Text 3"],
        "subject_input": "Subject",
    }
    response = client.post('/submit', data=json.dumps(test_data), content_type='application/json')

    assert response.status_code == 200
    assert response.is_json
    assert "generated_text" in response.get_json()
