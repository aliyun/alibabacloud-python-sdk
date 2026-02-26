# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AudioStream(DaraModel):
    def __init__(
        self,
        bitrate: int = None,
        channel_layout: str = None,
        channels: int = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        duration: float = None,
        frame_count: int = None,
        index: int = None,
        language: str = None,
        lyric: str = None,
        sample_format: str = None,
        sample_rate: int = None,
        start_time: float = None,
        time_base: str = None,
    ):
        # The bitrate. Unit: bit/s.
        self.bitrate = bitrate
        # The sound channel layout.
        self.channel_layout = channel_layout
        # The number of sound channels.
        self.channels = channels
        # The full name of the codec.
        self.codec_long_name = codec_long_name
        # The abbreviated name of the codec.
        self.codec_name = codec_name
        # The tag of the codec.
        self.codec_tag = codec_tag
        # The description of the codec tag.
        self.codec_tag_string = codec_tag_string
        # The time base of the codec.
        self.codec_time_base = codec_time_base
        # The duration of the audio stream in seconds.
        self.duration = duration
        # The number of frames.
        self.frame_count = frame_count
        # The index number of the audio stream.
        self.index = index
        # The audio language in the BCP 47 standard.
        self.language = language
        # The lyric.
        self.lyric = lyric
        # The sample format.
        self.sample_format = sample_format
        # The sampling rate. Unit: Hz.
        self.sample_rate = sample_rate
        # The start time of the audio stream in seconds.
        self.start_time = start_time
        # The time base.
        self.time_base = time_base

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.channel_layout is not None:
            result['ChannelLayout'] = self.channel_layout

        if self.channels is not None:
            result['Channels'] = self.channels

        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name

        if self.codec_name is not None:
            result['CodecName'] = self.codec_name

        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag

        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string

        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.frame_count is not None:
            result['FrameCount'] = self.frame_count

        if self.index is not None:
            result['Index'] = self.index

        if self.language is not None:
            result['Language'] = self.language

        if self.lyric is not None:
            result['Lyric'] = self.lyric

        if self.sample_format is not None:
            result['SampleFormat'] = self.sample_format

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_base is not None:
            result['TimeBase'] = self.time_base

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('ChannelLayout') is not None:
            self.channel_layout = m.get('ChannelLayout')

        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')

        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')

        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')

        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')

        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FrameCount') is not None:
            self.frame_count = m.get('FrameCount')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Lyric') is not None:
            self.lyric = m.get('Lyric')

        if m.get('SampleFormat') is not None:
            self.sample_format = m.get('SampleFormat')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeBase') is not None:
            self.time_base = m.get('TimeBase')

        return self

