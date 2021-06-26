from youtube_transcript_api import YouTubeTranscriptApi
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np


def create_string_from_transcript(transcript: list[dict]) -> str:
    text_list = [item['text'] for item in transcript]
    flat_text_string = " ".join(text_list)
    return flat_text_string


def get_words_from_videos(video_list: str) -> str:
    words = ""
    for video in video_list:
        transcript = YouTubeTranscriptApi.get_transcript(video)
        words += create_string_from_transcript(transcript=transcript)

    return words


def build_wordcloud(text: str, addl_stop_words: list, mask: str = None) -> WordCloud:
    stopwords = set(STOPWORDS)
    if addl_stop_words:
        stopwords.update(addl_stop_words)

    if mask:
        icon = Image.open(mask)
        image_mask = Image.new(mode='RGB', size=icon.size, color=(255, 255, 255))
        image_mask.paste(icon, box=icon)

        rgb_array = np.array(image_mask)
        wordcloud = WordCloud(mask=rgb_array, stopwords=stopwords, background_color="black", max_words=400).generate(
            text)
    else:
        wordcloud = WordCloud(stopwords=stopwords, background_color="black").generate(text)

    return wordcloud


if __name__ == '__main__':
    video_list = ['EjB1kz2tn5s',
                  'AifnGzNrdwE',
                  'YV7ZilaSdaU',
                  'wgGXfRV6GyQ',
                  'UhR7U8ZD3_s',
                  'FlxiFv7KAEk',
                  '2MYag92llCw',
                  '0u5KXmWpfbQ',
                  'l9UqMSZEs8w',
                  'udojj8-pqCM',
                  'Z4483_8qT7U',
                  'm4V375FuO0Q',
                  'RRTwQuVdIRE']

    flat_transcript = get_words_from_videos(video_list=video_list)
    cloud = build_wordcloud(text=flat_transcript, mask="mickey_mask.png", addl_stop_words=["[Music]", "Music"])

    cloud.to_file("wordcloud.png")
