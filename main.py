from youtube_transcript_api import YouTubeTranscriptApi


def create_string_from_transcript(transcript: list[dict]) -> str:
    text_list = [item['text'] for item in transcript]
    flat_text_string = " ".join(text_list)
    return flat_text_string


transcript = YouTubeTranscriptApi.get_transcript("i6bORQh_9LQ")
