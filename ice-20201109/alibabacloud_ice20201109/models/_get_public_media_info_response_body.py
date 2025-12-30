# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetPublicMediaInfoResponseBody(DaraModel):
    def __init__(
        self,
        media_info: main_models.GetPublicMediaInfoResponseBodyMediaInfo = None,
        request_id: str = None,
    ):
        self.media_info = media_info
        # RequestId
        self.request_id = request_id

    def validate(self):
        if self.media_info:
            self.media_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_info is not None:
            result['MediaInfo'] = self.media_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaInfo') is not None:
            temp_model = main_models.GetPublicMediaInfoResponseBodyMediaInfo()
            self.media_info = temp_model.from_map(m.get('MediaInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPublicMediaInfoResponseBodyMediaInfo(DaraModel):
    def __init__(
        self,
        dynamic_meta_data: main_models.GetPublicMediaInfoResponseBodyMediaInfoDynamicMetaData = None,
        file_info_list: List[main_models.GetPublicMediaInfoResponseBodyMediaInfoFileInfoList] = None,
        media_basic_info: main_models.GetPublicMediaInfoResponseBodyMediaInfoMediaBasicInfo = None,
        media_id: str = None,
    ):
        self.dynamic_meta_data = dynamic_meta_data
        # FileInfos
        self.file_info_list = file_info_list
        # BasicInfo
        self.media_basic_info = media_basic_info
        self.media_id = media_id

    def validate(self):
        if self.dynamic_meta_data:
            self.dynamic_meta_data.validate()
        if self.file_info_list:
            for v1 in self.file_info_list:
                 if v1:
                    v1.validate()
        if self.media_basic_info:
            self.media_basic_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_meta_data is not None:
            result['DynamicMetaData'] = self.dynamic_meta_data.to_map()

        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k1 in self.file_info_list:
                result['FileInfoList'].append(k1.to_map() if k1 else None)

        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicMetaData') is not None:
            temp_model = main_models.GetPublicMediaInfoResponseBodyMediaInfoDynamicMetaData()
            self.dynamic_meta_data = temp_model.from_map(m.get('DynamicMetaData'))

        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k1 in m.get('FileInfoList'):
                temp_model = main_models.GetPublicMediaInfoResponseBodyMediaInfoFileInfoList()
                self.file_info_list.append(temp_model.from_map(k1))

        if m.get('MediaBasicInfo') is not None:
            temp_model = main_models.GetPublicMediaInfoResponseBodyMediaInfoMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m.get('MediaBasicInfo'))

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class GetPublicMediaInfoResponseBodyMediaInfoMediaBasicInfo(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        category: str = None,
        cover_url: str = None,
        create_time: str = None,
        deleted_time: str = None,
        description: str = None,
        media_id: str = None,
        media_tags: str = None,
        media_type: str = None,
        modified_time: str = None,
        source: str = None,
        sprite_images: str = None,
        status: str = None,
        title: str = None,
        user_data: str = None,
    ):
        self.business_type = business_type
        self.category = category
        self.cover_url = cover_url
        self.create_time = create_time
        self.deleted_time = deleted_time
        self.description = description
        # MediaId
        self.media_id = media_id
        self.media_tags = media_tags
        self.media_type = media_type
        self.modified_time = modified_time
        self.source = source
        self.sprite_images = sprite_images
        self.status = status
        self.title = title
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.category is not None:
            result['Category'] = self.category

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time

        if self.description is not None:
            result['Description'] = self.description

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.source is not None:
            result['Source'] = self.source

        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetPublicMediaInfoResponseBodyMediaInfoFileInfoList(DaraModel):
    def __init__(
        self,
        audio_stream_info_list: List[main_models.GetPublicMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList] = None,
        file_basic_info: main_models.GetPublicMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo = None,
        subtitle_stream_info_list: List[main_models.GetPublicMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList] = None,
        video_stream_info_list: List[main_models.GetPublicMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList] = None,
    ):
        self.audio_stream_info_list = audio_stream_info_list
        self.file_basic_info = file_basic_info
        self.subtitle_stream_info_list = subtitle_stream_info_list
        self.video_stream_info_list = video_stream_info_list

    def validate(self):
        if self.audio_stream_info_list:
            for v1 in self.audio_stream_info_list:
                 if v1:
                    v1.validate()
        if self.file_basic_info:
            self.file_basic_info.validate()
        if self.subtitle_stream_info_list:
            for v1 in self.subtitle_stream_info_list:
                 if v1:
                    v1.validate()
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

        result['SubtitleStreamInfoList'] = []
        if self.subtitle_stream_info_list is not None:
            for k1 in self.subtitle_stream_info_list:
                result['SubtitleStreamInfoList'].append(k1.to_map() if k1 else None)

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
                temp_model = main_models.GetPublicMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList()
                self.audio_stream_info_list.append(temp_model.from_map(k1))

        if m.get('FileBasicInfo') is not None:
            temp_model = main_models.GetPublicMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m.get('FileBasicInfo'))

        self.subtitle_stream_info_list = []
        if m.get('SubtitleStreamInfoList') is not None:
            for k1 in m.get('SubtitleStreamInfoList'):
                temp_model = main_models.GetPublicMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList()
                self.subtitle_stream_info_list.append(temp_model.from_map(k1))

        self.video_stream_info_list = []
        if m.get('VideoStreamInfoList') is not None:
            for k1 in m.get('VideoStreamInfoList'):
                temp_model = main_models.GetPublicMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList()
                self.video_stream_info_list.append(temp_model.from_map(k1))

        return self

class GetPublicMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList(DaraModel):
    def __init__(
        self,
        avg_fps: str = None,
        bitrate: str = None,
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
        nb_frames: str = None,
        num_frames: str = None,
        pix_fmt: str = None,
        profile: str = None,
        rotate: str = None,
        sar: str = None,
        start_time: str = None,
        timebase: str = None,
        width: str = None,
    ):
        self.avg_fps = avg_fps
        self.bitrate = bitrate
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
        self.nb_frames = nb_frames
        self.num_frames = num_frames
        self.pix_fmt = pix_fmt
        self.profile = profile
        self.rotate = rotate
        self.sar = sar
        self.start_time = start_time
        self.timebase = timebase
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_fps is not None:
            result['AvgFPS'] = self.avg_fps

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

        if self.dar is not None:
            result['Dar'] = self.dar

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes

        if self.height is not None:
            result['Height'] = self.height

        if self.index is not None:
            result['Index'] = self.index

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.level is not None:
            result['Level'] = self.level

        if self.nb_frames is not None:
            result['Nb_frames'] = self.nb_frames

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
            result['StartTime'] = self.start_time

        if self.timebase is not None:
            result['Timebase'] = self.timebase

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgFPS') is not None:
            self.avg_fps = m.get('AvgFPS')

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

        if m.get('Dar') is not None:
            self.dar = m.get('Dar')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Nb_frames') is not None:
            self.nb_frames = m.get('Nb_frames')

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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class GetPublicMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList(DaraModel):
    def __init__(
        self,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        duration: str = None,
        index: str = None,
        lang: str = None,
        start_time: str = None,
        timebase: str = None,
    ):
        self.codec_long_name = codec_long_name
        self.codec_name = codec_name
        self.codec_tag = codec_tag
        self.codec_tag_string = codec_tag_string
        self.codec_time_base = codec_time_base
        self.duration = duration
        self.index = index
        self.lang = lang
        self.start_time = start_time
        self.timebase = timebase

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.timebase is not None:
            result['Timebase'] = self.timebase

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')

        return self

class GetPublicMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo(DaraModel):
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

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class GetPublicMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList(DaraModel):
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
        fps: str = None,
        index: str = None,
        lang: str = None,
        num_frames: str = None,
        profile: str = None,
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
        self.fps = fps
        self.index = index
        self.lang = lang
        self.num_frames = num_frames
        self.profile = profile
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

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.index is not None:
            result['Index'] = self.index

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames

        if self.profile is not None:
            result['Profile'] = self.profile

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

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('SampleFmt') is not None:
            self.sample_fmt = m.get('SampleFmt')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')

        return self

class GetPublicMediaInfoResponseBodyMediaInfoDynamicMetaData(DaraModel):
    def __init__(
        self,
        data: str = None,
        type: str = None,
    ):
        self.data = data
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

