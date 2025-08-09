from fastapi.testclient import TestClient
from app.main import app
from app.model import SentimentModel

client = TestClient(app)

def test_predict_api():
    response = client.post("/predict", json={"text": "I love this!"})
    assert response.status_code == 200
    data = response.json()
    assert "label" in data
    assert data["label"] in ["POSITIVE", "NEGATIVE"]
    assert 0.0 <= data["score"] <= 1.0

def test_model_predict():
    model = SentimentModel()
    result = model.predict("I hate bugs.")
    assert "label" in result
    assert result["label"] in ["POSITIVE", "NEGATIVE"]
    assert 0.0 <= result["score"] <= 1.0
