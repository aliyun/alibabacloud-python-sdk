# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class MediaConvertOutputDetailFileMeta(DaraModel):
    def __init__(
        self,
        audio_stream_info_list: List[main_models.MediaConvertOutputDetailFileMetaAudioStreamInfoList] = None,
        file_basic_info: main_models.MediaConvertOutputDetailFileMetaFileBasicInfo = None,
        video_stream_info_list: List[main_models.MediaConvertOutputDetailFileMetaVideoStreamInfoList] = None,
    ):
        self.audio_stream_info_list = audio_stream_info_list
        self.file_basic_info = file_basic_info
        self.video_stream_info_list = video_stream_info_list

    def validate(self):
        if self.audio_stream_info_list:
            for v1 in self.audio_stream_info_list:
                 if v1:
                    v1.validate()
        if self.file_basic_info:
            self.file_basic_info.validate()
        if self.video_stream_info_list:
            for v1 in self.video_stream_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioStreamInfoList'] = []
        if self.audio_stream_info_list is not None:
            for k1 in self.audio_stream_info_list:
                result['AudioStreamInfoList'].append(k1.to_map() if k1 else None)

        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()

        result['VideoStreamInfoList'] = []
        if self.video_stream_info_list is not None:
            for k1 in self.video_stream_info_list:
                result['VideoStreamInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_stream_info_list = []
        if m.get('AudioStreamInfoList') is not None:
            for k1 in m.get('AudioStreamInfoList'):
                temp_model = main_models.MediaConvertOutputDetailFileMetaAudioStreamInfoList()
                self.audio_stream_info_list.append(temp_model.from_map(k1))

        if m.get('FileBasicInfo') is not None:
            temp_model = main_models.MediaConvertOutputDetailFileMetaFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m.get('FileBasicInfo'))

        self.video_stream_info_list = []
        if m.get('VideoStreamInfoList') is not None:
            for k1 in m.get('VideoStreamInfoList'):
                temp_model = main_models.MediaConvertOutputDetailFileMetaVideoStreamInfoList()
                self.video_stream_info_list.append(temp_model.from_map(k1))

        return self

class MediaConvertOutputDetailFileMetaVideoStreamInfoList(DaraModel):
    def __init__(
        self,
        avg_fps: str = None,
        bit_rate: str = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        dar: str = None,
        duration: str = None,
        fps: str = None,
        has_bframes: str = None,
        height: str = None,
        index: str = None,
        lang: str = None,
        level: str = None,
        num_frames: str = None,
        pix_fmt: str = None,
        profile: str = None,
        rotate: str = None,
        sar: str = None,
        start_time: str = None,
        time_base: str = None,
        width: str = None,
    ):
        self.avg_fps = avg_fps
        self.bit_rate = bit_rate
        self.codec_long_name = codec_long_name
        self.codec_name = codec_name
        self.codec_tag = codec_tag
        self.codec_tag_string = codec_tag_string
        self.codec_time_base = codec_time_base
        self.dar = dar
        self.duration = duration
        self.fps = fps
        self.has_bframes = has_bframes
        self.height = height
        self.index = index
        self.lang = lang
        self.level = level
        self.num_frames = num_frames
        self.pix_fmt = pix_fmt
        self.profile = profile
        self.rotate = rotate
        self.sar = sar
        self.start_time = start_time
        self.time_base = time_base
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_fps is not None:
            result['Avg_fps'] = self.avg_fps

        if self.bit_rate is not None:
            result['Bit_rate'] = self.bit_rate

        if self.codec_long_name is not None:
            result['Codec_long_name'] = self.codec_long_name

        if self.codec_name is not None:
            result['Codec_name'] = self.codec_name

        if self.codec_tag is not None:
            result['Codec_tag'] = self.codec_tag

        if self.codec_tag_string is not None:
            result['Codec_tag_string'] = self.codec_tag_string

        if self.codec_time_base is not None:
            result['Codec_time_base'] = self.codec_time_base

        if self.dar is not None:
            result['Dar'] = self.dar

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.has_bframes is not None:
            result['Has_b_frames'] = self.has_bframes

        if self.height is not None:
            result['Height'] = self.height

        if self.index is not None:
            result['Index'] = self.index

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.level is not None:
            result['Level'] = self.level

        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames

        if self.pix_fmt is not None:
            result['PixFmt'] = self.pix_fmt

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.rotate is not None:
            result['Rotate'] = self.rotate

        if self.sar is not None:
            result['Sar'] = self.sar

        if self.start_time is not None:
            result['Start_time'] = self.start_time

        if self.time_base is not None:
            result['Time_base'] = self.time_base

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avg_fps') is not None:
            self.avg_fps = m.get('Avg_fps')

        if m.get('Bit_rate') is not None:
            self.bit_rate = m.get('Bit_rate')

        if m.get('Codec_long_name') is not None:
            self.codec_long_name = m.get('Codec_long_name')

        if m.get('Codec_name') is not None:
            self.codec_name = m.get('Codec_name')

        if m.get('Codec_tag') is not None:
            self.codec_tag = m.get('Codec_tag')

        if m.get('Codec_tag_string') is not None:
            self.codec_tag_string = m.get('Codec_tag_string')

        if m.get('Codec_time_base') is not None:
            self.codec_time_base = m.get('Codec_time_base')

        if m.get('Dar') is not None:
            self.dar = m.get('Dar')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Has_b_frames') is not None:
            self.has_bframes = m.get('Has_b_frames')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')

        if m.get('PixFmt') is not None:
            self.pix_fmt = m.get('PixFmt')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')

        if m.get('Sar') is not None:
            self.sar = m.get('Sar')

        if m.get('Start_time') is not None:
            self.start_time = m.get('Start_time')

        if m.get('Time_base') is not None:
            self.time_base = m.get('Time_base')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class MediaConvertOutputDetailFileMetaFileBasicInfo(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        duration: str = None,
        file_name: str = None,
        file_size: str = None,
        file_status: str = None,
        file_type: str = None,
        file_url: str = None,
        format_name: str = None,
        height: str = None,
        media_id: str = None,
        region: str = None,
        width: str = None,
    ):
        self.bitrate = bitrate
        self.duration = duration
        self.file_name = file_name
        self.file_size = file_size
        self.file_status = file_status
        self.file_type = file_type
        self.file_url = file_url
        self.format_name = format_name
        self.height = height
        self.media_id = media_id
        self.region = region
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

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.file_status is not None:
            result['FileStatus'] = self.file_status

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.format_name is not None:
            result['FormatName'] = self.format_name

        if self.height is not None:
            result['Height'] = self.height

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.region is not None:
            result['Region'] = self.region

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class MediaConvertOutputDetailFileMetaAudioStreamInfoList(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channel_layout: str = None,
        channels: str = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        duration: str = None,
        index: str = None,
        lang: str = None,
        sample_fmt: str = None,
        sample_rate: str = None,
        start_time: str = None,
        timebase: str = None,
    ):
        self.bitrate = bitrate
        self.channel_layout = channel_layout
        self.channels = channels
        self.codec_long_name = codec_long_name
        self.codec_name = codec_name
        self.codec_tag = codec_tag
        self.codec_tag_string = codec_tag_string
        self.codec_time_base = codec_time_base
        self.duration = duration
        self.index = index
        self.lang = lang
        self.sample_fmt = sample_fmt
        self.sample_rate = sample_rate
        self.start_time = start_time
        self.timebase = timebase

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

        if self.index is not None:
            result['Index'] = self.index

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.sample_fmt is not None:
            result['SampleFmt'] = self.sample_fmt

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.timebase is not None:
            result['Timebase'] = self.timebase

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

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SampleFmt') is not None:
            self.sample_fmt = m.get('SampleFmt')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')

        return self

