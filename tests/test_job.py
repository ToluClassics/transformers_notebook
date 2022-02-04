from transformers import pipeline


def test_secured_server(container, http_client):
    """Notebook server should eventually request user login."""
    container.run()
    resp = http_client.get("http://localhost:8888")
    resp.raise_for_status()
    assert "login_submit" in resp.text


print(pipeline("sentiment-analysis")("I hate you"))
