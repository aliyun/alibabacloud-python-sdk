# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VideoStream(DaraModel):
    def __init__(
        self,
        average_frame_rate: str = None,
        bit_depth: int = None,
        bitrate: int = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        color_primaries: str = None,
        color_range: str = None,
        color_space: str = None,
        color_transfer: str = None,
        display_aspect_ratio: str = None,
        duration: float = None,
        frame_count: int = None,
        frame_rate: str = None,
        has_bframes: int = None,
        height: int = None,
        index: int = None,
        language: str = None,
        level: int = None,
        pixel_format: str = None,
        profile: str = None,
        rotate: str = None,
        sample_aspect_ratio: str = None,
        start_time: float = None,
        time_base: str = None,
        width: int = None,
    ):
        # The average frame rate of the video stream.
        self.average_frame_rate = average_frame_rate
        # The bit depth.
        self.bit_depth = bit_depth
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
        # The time base of the codec.
        self.codec_time_base = codec_time_base
        # The primary colors.
        self.color_primaries = color_primaries
        # The color range.
        self.color_range = color_range
        # The color space.
        self.color_space = color_space
        # The color transfer function.
        self.color_transfer = color_transfer
        # The display aspect ratio of the video stream.
        self.display_aspect_ratio = display_aspect_ratio
        # The duration of the video stream. Unit: seconds.
        self.duration = duration
        # The number of frames.
        self.frame_count = frame_count
        # The frame rate of the video stream.
        self.frame_rate = frame_rate
        # Specifies whether the video stream contains B frames.
        self.has_bframes = has_bframes
        # The image height of the video stream. Unit: pixels.
        self.height = height
        # The index number of the video stream.
        self.index = index
        # The language used in the video stream. The language is indicated by using a BCP 47 language tag.
        self.language = language
        # The level.
        self.level = level
        # The pixel format of the video stream.
        self.pixel_format = pixel_format
        # The profile.
        self.profile = profile
        # The image rotation angle of the video stream.
        self.rotate = rotate
        # The sampling aspect ratio of the video stream.
        self.sample_aspect_ratio = sample_aspect_ratio
        # The start time of the video stream. Unit: seconds.
        self.start_time = start_time
        # The time base.
        self.time_base = time_base
        # The image width of the video stream. Unit: pixels.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average_frame_rate is not None:
            result['AverageFrameRate'] = self.average_frame_rate

        if self.bit_depth is not None:
            result['BitDepth'] = self.bit_depth

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

        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base

        if self.color_primaries is not None:
            result['ColorPrimaries'] = self.color_primaries

        if self.color_range is not None:
            result['ColorRange'] = self.color_range

        if self.color_space is not None:
            result['ColorSpace'] = self.color_space

        if self.color_transfer is not None:
            result['ColorTransfer'] = self.color_transfer

        if self.display_aspect_ratio is not None:
            result['DisplayAspectRatio'] = self.display_aspect_ratio

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.frame_count is not None:
            result['FrameCount'] = self.frame_count

        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate

        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes

        if self.height is not None:
            result['Height'] = self.height

        if self.index is not None:
            result['Index'] = self.index

        if self.language is not None:
            result['Language'] = self.language

        if self.level is not None:
            result['Level'] = self.level

        if self.pixel_format is not None:
            result['PixelFormat'] = self.pixel_format

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.rotate is not None:
            result['Rotate'] = self.rotate

        if self.sample_aspect_ratio is not None:
            result['SampleAspectRatio'] = self.sample_aspect_ratio

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_base is not None:
            result['TimeBase'] = self.time_base

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AverageFrameRate') is not None:
            self.average_frame_rate = m.get('AverageFrameRate')

        if m.get('BitDepth') is not None:
            self.bit_depth = m.get('BitDepth')

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

        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')

        if m.get('ColorPrimaries') is not None:
            self.color_primaries = m.get('ColorPrimaries')

        if m.get('ColorRange') is not None:
            self.color_range = m.get('ColorRange')

        if m.get('ColorSpace') is not None:
            self.color_space = m.get('ColorSpace')

        if m.get('ColorTransfer') is not None:
            self.color_transfer = m.get('ColorTransfer')

        if m.get('DisplayAspectRatio') is not None:
            self.display_aspect_ratio = m.get('DisplayAspectRatio')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FrameCount') is not None:
            self.frame_count = m.get('FrameCount')

        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')

        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('PixelFormat') is not None:
            self.pixel_format = m.get('PixelFormat')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')

        if m.get('SampleAspectRatio') is not None:
            self.sample_aspect_ratio = m.get('SampleAspectRatio')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeBase') is not None:
            self.time_base = m.get('TimeBase')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

