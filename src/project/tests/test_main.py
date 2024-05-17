from project.main import hello


def test_hello() -> None:
    assert hello() == "Hello, world!"
