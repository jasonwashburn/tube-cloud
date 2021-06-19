import pytest
from main import create_string_from_transcript


@pytest.fixture
def sample_transcript() -> list[dict]:
    sample_transcript = [{'text': "hey everybody it's me Mickey Mouse",
                          'start': 1.79,
                          'duration': 7.62},
                         {'text': 'say you want to come inside my Clubhouse',
                          'start': 5.24,
                          'duration': 4.17},
                         {'text': "well alright let's go huh I almost",
                          'start': 10.34,
                          'duration': 10.15}]
    return sample_transcript


def test_create_string_from_transcript_returns_expected_result(sample_transcript) -> None:
    result = create_string_from_transcript(sample_transcript)
    assert result == "hey everybody it's me Mickey Mouse say you want to come inside my Clubhouse well alright let's " \
                     "go huh I almost"
