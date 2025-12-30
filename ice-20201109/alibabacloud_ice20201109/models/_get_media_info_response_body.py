# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetMediaInfoResponseBody(DaraModel):
    def __init__(
        self,
        media_info: main_models.GetMediaInfoResponseBodyMediaInfo = None,
        request_id: str = None,
    ):
        # The information about the media asset.
        self.media_info = media_info
        # The request ID.
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
            temp_model = main_models.GetMediaInfoResponseBodyMediaInfo()
            self.media_info = temp_model.from_map(m.get('MediaInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMediaInfoResponseBodyMediaInfo(DaraModel):
    def __init__(
        self,
        ai_rough_data: main_models.GetMediaInfoResponseBodyMediaInfoAiRoughData = None,
        file_info_list: List[main_models.GetMediaInfoResponseBodyMediaInfoFileInfoList] = None,
        media_basic_info: main_models.GetMediaInfoResponseBodyMediaInfoMediaBasicInfo = None,
        media_id: str = None,
    ):
        # The original AI analysis data.
        self.ai_rough_data = ai_rough_data
        # The file information.
        self.file_info_list = file_info_list
        # The basic information about the media asset.
        self.media_basic_info = media_basic_info
        # The ID of the media asset.
        self.media_id = media_id

    def validate(self):
        if self.ai_rough_data:
            self.ai_rough_data.validate()
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
        if self.ai_rough_data is not None:
            result['AiRoughData'] = self.ai_rough_data.to_map()

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
        if m.get('AiRoughData') is not None:
            temp_model = main_models.GetMediaInfoResponseBodyMediaInfoAiRoughData()
            self.ai_rough_data = temp_model.from_map(m.get('AiRoughData'))

        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k1 in m.get('FileInfoList'):
                temp_model = main_models.GetMediaInfoResponseBodyMediaInfoFileInfoList()
                self.file_info_list.append(temp_model.from_map(k1))

        if m.get('MediaBasicInfo') is not None:
            temp_model = main_models.GetMediaInfoResponseBodyMediaInfoMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m.get('MediaBasicInfo'))

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class GetMediaInfoResponseBodyMediaInfoMediaBasicInfo(DaraModel):
    def __init__(
        self,
        biz: str = None,
        business_type: str = None,
        cate_id: int = None,
        cate_name: str = None,
        category: str = None,
        cover_url: str = None,
        create_time: str = None,
        deleted_time: str = None,
        description: str = None,
        input_url: str = None,
        media_id: str = None,
        media_tags: str = None,
        media_type: str = None,
        modified_time: str = None,
        reference_id: str = None,
        snapshots: str = None,
        source: str = None,
        sprite_images: str = None,
        status: str = None,
        title: str = None,
        upload_source: str = None,
        user_data: str = None,
    ):
        # The service to which the media asset belongs.
        self.biz = biz
        # The business type.
        self.business_type = business_type
        # The category ID.
        self.cate_id = cate_id
        # The category name.
        self.cate_name = cate_name
        # The category.
        self.category = category
        # The URL of the thumbnail.
        self.cover_url = cover_url
        # The time when the media asset was created.
        self.create_time = create_time
        # The time when the media asset was deleted.
        self.deleted_time = deleted_time
        # The content description.
        self.description = description
        # The input URL of the media asset in another service.
        self.input_url = input_url
        # The ID of the media asset.
        self.media_id = media_id
        # The tags.
        self.media_tags = media_tags
        # The type of the media asset.
        self.media_type = media_type
        # The time when the media asset was last modified.
        self.modified_time = modified_time
        # The custom ID. The ID can be 6 to 64 characters in length and can contain only letters, digits, hyphens (-), and underscores (_). The ID is unique among users.
        self.reference_id = reference_id
        # The snapshots.
        self.snapshots = snapshots
        # The source.
        self.source = source
        # The sprite.
        self.sprite_images = sprite_images
        # The resource status.
        self.status = status
        # The title.
        self.title = title
        # The upload source of the media asset.
        self.upload_source = upload_source
        # The user data.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz is not None:
            result['Biz'] = self.biz

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cate_name is not None:
            result['CateName'] = self.cate_name

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

        if self.input_url is not None:
            result['InputURL'] = self.input_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots

        if self.source is not None:
            result['Source'] = self.source

        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        if self.upload_source is not None:
            result['UploadSource'] = self.upload_source

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

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

        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UploadSource') is not None:
            self.upload_source = m.get('UploadSource')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class GetMediaInfoResponseBodyMediaInfoFileInfoList(DaraModel):
    def __init__(
        self,
        audio_stream_info_list: List[main_models.GetMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList] = None,
        file_basic_info: main_models.GetMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo = None,
        subtitle_stream_info_list: List[main_models.GetMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList] = None,
        video_stream_info_list: List[main_models.GetMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList] = None,
    ):
        # The information about the audio tracks. A media asset may have multiple audio tracks.
        self.audio_stream_info_list = audio_stream_info_list
        # The basic information about the file, including the duration and size.
        self.file_basic_info = file_basic_info
        # The information about the subtitle tracks. A media asset may have multiple subtitle tracks.
        self.subtitle_stream_info_list = subtitle_stream_info_list
        # The information about the video tracks. A media asset may have multiple video tracks.
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
                temp_model = main_models.GetMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList()
                self.audio_stream_info_list.append(temp_model.from_map(k1))

        if m.get('FileBasicInfo') is not None:
            temp_model = main_models.GetMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m.get('FileBasicInfo'))

        self.subtitle_stream_info_list = []
        if m.get('SubtitleStreamInfoList') is not None:
            for k1 in m.get('SubtitleStreamInfoList'):
                temp_model = main_models.GetMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList()
                self.subtitle_stream_info_list.append(temp_model.from_map(k1))

        self.video_stream_info_list = []
        if m.get('VideoStreamInfoList') is not None:
            for k1 in m.get('VideoStreamInfoList'):
                temp_model = main_models.GetMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList()
                self.video_stream_info_list.append(temp_model.from_map(k1))

        return self

class GetMediaInfoResponseBodyMediaInfoFileInfoListVideoStreamInfoList(DaraModel):
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
        # The average video frame rate.
        self.avg_fps = avg_fps
        # The bitrate.
        self.bitrate = bitrate
        # The full name of the codec.
        self.codec_long_name = codec_long_name
        # The short name of the codec.
        self.codec_name = codec_name
        # The tag of the codec.
        self.codec_tag = codec_tag
        # The tag string of the codec.
        self.codec_tag_string = codec_tag_string
        # The time base of the codec.
        self.codec_time_base = codec_time_base
        # The display aspect ratio (DAR).
        self.dar = dar
        # The duration.
        self.duration = duration
        # The video frame rate.
        self.fps = fps
        # Indicates whether the video track contains bidirectional frames (B-frames).
        self.has_bframes = has_bframes
        # The height.
        self.height = height
        # The sequence number of the video track.
        self.index = index
        # The language.
        self.lang = lang
        # The codec level.
        self.level = level
        # The total number of frames.
        self.nb_frames = nb_frames
        # The number of frames.
        self.num_frames = num_frames
        # The pixel format.
        self.pix_fmt = pix_fmt
        # The codec profile.
        self.profile = profile
        # The rotation angle.
        self.rotate = rotate
        # The sample aspect ratio (SAR).
        self.sar = sar
        # The start time.
        self.start_time = start_time
        # The time base.
        self.timebase = timebase
        # The width.
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

class GetMediaInfoResponseBodyMediaInfoFileInfoListSubtitleStreamInfoList(DaraModel):
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
        # The full name of the codec.
        self.codec_long_name = codec_long_name
        # The short name of the codec.
        self.codec_name = codec_name
        # The tag of the codec.
        self.codec_tag = codec_tag
        # The tag string of the codec.
        self.codec_tag_string = codec_tag_string
        # The time base of the codec.
        self.codec_time_base = codec_time_base
        # The duration.
        self.duration = duration
        # The sequence number of the subtitle track.
        self.index = index
        # The language.
        self.lang = lang
        # The start time.
        self.start_time = start_time
        # The time base.
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

class GetMediaInfoResponseBodyMediaInfoFileInfoListFileBasicInfo(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        create_time: str = None,
        duration: str = None,
        file_name: str = None,
        file_size: str = None,
        file_status: str = None,
        file_type: str = None,
        file_url: str = None,
        format_name: str = None,
        height: str = None,
        modified_time: str = None,
        region: str = None,
        width: str = None,
    ):
        # The bitrate.
        self.bitrate = bitrate
        # The time when the file was created.
        self.create_time = create_time
        # The duration.
        self.duration = duration
        # The file name.
        self.file_name = file_name
        # The file size. Unit: bytes.
        self.file_size = file_size
        # The file status.
        self.file_status = file_status
        # The file type.
        self.file_type = file_type
        # The OSS URL of the file.
        self.file_url = file_url
        # The container format.
        self.format_name = format_name
        # The height.
        self.height = height
        # The time when the file was last modified.
        self.modified_time = modified_time
        # The region in which the file is stored.
        self.region = region
        # The width.
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.region is not None:
            result['Region'] = self.region

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

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

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class GetMediaInfoResponseBodyMediaInfoFileInfoListAudioStreamInfoList(DaraModel):
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
        # The bitrate.
        self.bitrate = bitrate
        # The output layout of sound channels.
        self.channel_layout = channel_layout
        # The number of sound channels.
        self.channels = channels
        # The full name of the codec.
        self.codec_long_name = codec_long_name
        # The short name of the codec.
        self.codec_name = codec_name
        # The tag of the codec.
        self.codec_tag = codec_tag
        # The tag string of the codec.
        self.codec_tag_string = codec_tag_string
        # The time base of the codec.
        self.codec_time_base = codec_time_base
        # The duration.
        self.duration = duration
        # The audio frame rate.
        self.fps = fps
        # The sequence number of the audio track.
        self.index = index
        # The language.
        self.lang = lang
        # The number of frames.
        self.num_frames = num_frames
        # The codec profile.
        self.profile = profile
        # The sampling format.
        self.sample_fmt = sample_fmt
        # The sampling rate.
        self.sample_rate = sample_rate
        # The start time.
        self.start_time = start_time
        # The time base.
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

class GetMediaInfoResponseBodyMediaInfoAiRoughData(DaraModel):
    def __init__(
        self,
        ai_category: str = None,
        ai_job_id: str = None,
        result: str = None,
        save_type: str = None,
        standard_smart_tag_job: main_models.GetMediaInfoResponseBodyMediaInfoAiRoughDataStandardSmartTagJob = None,
        status: str = None,
    ):
        # The AI category. Valid values:
        # 
        # *   Life
        # *   Good-looking
        # *   Cute pets
        # *   News
        # *   Ads
        # *   Environmental resources
        # *   Automobile
        self.ai_category = ai_category
        # The ID of the AI task.
        self.ai_job_id = ai_job_id
        # The analysis result.
        self.result = result
        # The storage type. This parameter indicates the library in which the analysis data is stored. Valid values:
        # 
        # *   TEXT: the text library.
        self.save_type = save_type
        # The information about the tagging job.
        self.standard_smart_tag_job = standard_smart_tag_job
        # The analysis status. Valid values:
        # 
        # *   Analyzing
        # *   AnalyzeSuccess
        # *   AnalyzeFailed
        # *   Saving
        # *   SaveSuccess
        # *   SaveFailed
        # *   Deleting
        # *   DeleteSuccess
        # *   DeleteFailed
        self.status = status

    def validate(self):
        if self.standard_smart_tag_job:
            self.standard_smart_tag_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_category is not None:
            result['AiCategory'] = self.ai_category

        if self.ai_job_id is not None:
            result['AiJobId'] = self.ai_job_id

        if self.result is not None:
            result['Result'] = self.result

        if self.save_type is not None:
            result['SaveType'] = self.save_type

        if self.standard_smart_tag_job is not None:
            result['StandardSmartTagJob'] = self.standard_smart_tag_job.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiCategory') is not None:
            self.ai_category = m.get('AiCategory')

        if m.get('AiJobId') is not None:
            self.ai_job_id = m.get('AiJobId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('SaveType') is not None:
            self.save_type = m.get('SaveType')

        if m.get('StandardSmartTagJob') is not None:
            temp_model = main_models.GetMediaInfoResponseBodyMediaInfoAiRoughDataStandardSmartTagJob()
            self.standard_smart_tag_job = temp_model.from_map(m.get('StandardSmartTagJob'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetMediaInfoResponseBodyMediaInfoAiRoughDataStandardSmartTagJob(DaraModel):
    def __init__(
        self,
        ai_job_id: str = None,
        result_url: str = None,
        results: List[main_models.GetMediaInfoResponseBodyMediaInfoAiRoughDataStandardSmartTagJobResults] = None,
        status: str = None,
    ):
        # The ID of the AI task.
        self.ai_job_id = ai_job_id
        # The URL of the tagging result.
        self.result_url = result_url
        # The recognized tags.
        self.results = results
        # The analysis status. Valid values:
        # 
        # *   Analyzing
        # *   AnalyzeSuccess
        # *   AnalyzeFailed
        self.status = status

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_job_id is not None:
            result['AiJobId'] = self.ai_job_id

        if self.result_url is not None:
            result['ResultUrl'] = self.result_url

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiJobId') is not None:
            self.ai_job_id = m.get('AiJobId')

        if m.get('ResultUrl') is not None:
            self.result_url = m.get('ResultUrl')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.GetMediaInfoResponseBodyMediaInfoAiRoughDataStandardSmartTagJobResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetMediaInfoResponseBodyMediaInfoAiRoughDataStandardSmartTagJobResults(DaraModel):
    def __init__(
        self,
        data: str = None,
        type: str = None,
    ):
        # The result data. The value is a JSON string. For information about the data structures of different data types<props="china">, see [Description of the Results parameter](https://help.aliyun.com/zh/ims/developer-reference/api-ice-2020-11-09-querysmarttagjob?spm=a2c4g.11186623.0.0.521d48b7KfapOL#api-detail-40).
        self.data = data
        # The tagging type. Valid values:
        # 
        # *   NLP: natural language processing (NLP)-based tagging
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

