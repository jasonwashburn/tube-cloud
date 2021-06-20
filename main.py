from youtube_transcript_api import YouTubeTranscriptApi
from wordcloud import WordCloud, STOPWORDS


def create_string_from_transcript(transcript: list[dict]) -> str:
    text_list = [item['text'] for item in transcript]
    flat_text_string = " ".join(text_list)
    return flat_text_string


def build_wordcloud(text: str, addl_stop_words: list) -> WordCloud:
    stopwords = set(STOPWORDS)
    if addl_stop_words:
        stopwords.update(addl_stop_words)

    wordcloud = WordCloud(stopwords=stopwords).generate(text)
    return wordcloud

transcript = YouTubeTranscriptApi.get_transcript("i6bORQh_9LQ")

flat_transcript = create_string_from_transcript(transcript=transcript)
wordcloud = build_wordcloud(text=flat_transcript, addl_stop_words=["[Music]", "Music"])

wordcloud.to_file("wordcloud.png")
