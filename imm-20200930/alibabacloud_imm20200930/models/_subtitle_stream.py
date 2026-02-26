# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubtitleStream(DaraModel):
    def __init__(
        self,
        bitrate: int = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        content: str = None,
        duration: float = None,
        height: int = None,
        index: int = None,
        language: str = None,
        start_time: float = None,
        width: int = None,
    ):
        # The bitrate. Unit: bit/s.
        self.bitrate = bitrate
        # The full name of the codec.
        self.codec_long_name = codec_long_name
        # The abbreviated name of the codec.
        self.codec_name = codec_name
        # The tag of the codec.
        self.codec_tag = codec_tag
        # The description of the codec tag.
        self.codec_tag_string = codec_tag_string
        # The subtitle content.
        self.content = content
        # The duration of the subtitle stream in seconds.
        self.duration = duration
        # The height of the subtitles. Unit: pixels.
        self.height = height
        # The index number of the subtitle stream.
        self.index = index
        # The subtitle language in the BCP 47 standard.
        self.language = language
        # The start time of the subtitle stream in seconds.
        self.start_time = start_time
        # The width of the subtitles. Unit: pixels.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name

        if self.codec_name is not None:
            result['CodecName'] = self.codec_name

        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag

        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string

        if self.content is not None:
            result['Content'] = self.content

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.height is not None:
            result['Height'] = self.height

        if self.index is not None:
            result['Index'] = self.index

        if self.language is not None:
            result['Language'] = self.language

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')

        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')

        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')

        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

