# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetMezzanineInfoResponseBody(DaraModel):
    def __init__(
        self,
        mezzanine: main_models.GetMezzanineInfoResponseBodyMezzanine = None,
        request_id: str = None,
    ):
        # The information about the source file.
        self.mezzanine = mezzanine
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.mezzanine:
            self.mezzanine.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mezzanine is not None:
            result['Mezzanine'] = self.mezzanine.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mezzanine') is not None:
            temp_model = main_models.GetMezzanineInfoResponseBodyMezzanine()
            self.mezzanine = temp_model.from_map(m.get('Mezzanine'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMezzanineInfoResponseBodyMezzanine(DaraModel):
    def __init__(
        self,
        audio_stream_list: List[main_models.GetMezzanineInfoResponseBodyMezzanineAudioStreamList] = None,
        bitrate: str = None,
        creation_time: str = None,
        duration: str = None,
        file_md5: str = None,
        file_name: str = None,
        file_url: str = None,
        fps: str = None,
        height: int = None,
        output_type: str = None,
        preprocess_status: str = None,
        restore_expiration: str = None,
        restore_status: str = None,
        size: int = None,
        status: str = None,
        storage_class: str = None,
        video_id: str = None,
        video_stream_list: List[main_models.GetMezzanineInfoResponseBodyMezzanineVideoStreamList] = None,
        width: int = None,
    ):
        # The codec time base.
        self.audio_stream_list = audio_stream_list
        # The bitrate of the file. Unit: Kbit/s.
        self.bitrate = bitrate
        # The time when the file was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The duration of the file. Unit: seconds.
        self.duration = duration
        self.file_md5 = file_md5
        # The name of the file.
        self.file_name = file_name
        # The URL of the file.
        self.file_url = file_url
        # The frame rate of the file. Unit: frames per second.
        self.fps = fps
        # The height of the file. Unit: pixel.
        self.height = height
        # The type of the mezzanine file URL. Valid values:
        # 
        # - **oss**: OSS URL
        # - **cdn** (default): CDN URL
        # 
        # > If you specify an OSS URL for the video stream, the video stream must be in the MP4 format.
        self.output_type = output_type
        # The preprocess status od the media.
        self.preprocess_status = preprocess_status
        # The period of time in which the object remains in the restored state.
        self.restore_expiration = restore_expiration
        # The restoration status of the audio or video file. Valid values:
        # 
        # *   **Processing**
        # *   **Success**
        # *   **Failed**
        self.restore_status = restore_status
        # The size of the file. Unit: byte.
        self.size = size
        # The status of the file. Valid values:
        # 
        # *   **Uploading**: The file is being uploaded. This is the initial status.
        # *   **Normal**: The file is uploaded.
        # *   **UploadFail**: The file fails to be uploaded.
        # *   **Deleted**: The file is deleted.
        self.status = status
        # The storage class of the audio file. Valid values:
        # 
        # *   **Standard**: All media resources are stored as Standard objects.
        # *   **IA**: All media resources are stored as IA objects.
        # *   **Archive**: All media resources are stored as Archive objects.
        # *   **ColdArchive**: All media resources are stored as Cold Archive objects.
        # *   **SourceIA**: Only the source files are IA objects.
        # *   **SourceArchive**: Only the source files are Archive objects.
        # *   **SourceColdArchive**: Only the source files are Cold Archive objects.
        # *   **Changing**: The storage class of the audio file is being changed.
        # *   **SourceChanging**: The storage class of the source file is being changed.
        self.storage_class = storage_class
        # The ID of the video.
        self.video_id = video_id
        # The HDR type of the video stream.
        self.video_stream_list = video_stream_list
        # The width of the file. Unit: pixel.
        self.width = width

    def validate(self):
        if self.audio_stream_list:
            for v1 in self.audio_stream_list:
                 if v1:
                    v1.validate()
        if self.video_stream_list:
            for v1 in self.video_stream_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioStreamList'] = []
        if self.audio_stream_list is not None:
            for k1 in self.audio_stream_list:
                result['AudioStreamList'].append(k1.to_map() if k1 else None)

        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_md5 is not None:
            result['FileMD5'] = self.file_md5

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url is not None:
            result['FileURL'] = self.file_url

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.height is not None:
            result['Height'] = self.height

        if self.output_type is not None:
            result['OutputType'] = self.output_type

        if self.preprocess_status is not None:
            result['PreprocessStatus'] = self.preprocess_status

        if self.restore_expiration is not None:
            result['RestoreExpiration'] = self.restore_expiration

        if self.restore_status is not None:
            result['RestoreStatus'] = self.restore_status

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        result['VideoStreamList'] = []
        if self.video_stream_list is not None:
            for k1 in self.video_stream_list:
                result['VideoStreamList'].append(k1.to_map() if k1 else None)

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_stream_list = []
        if m.get('AudioStreamList') is not None:
            for k1 in m.get('AudioStreamList'):
                temp_model = main_models.GetMezzanineInfoResponseBodyMezzanineAudioStreamList()
                self.audio_stream_list.append(temp_model.from_map(k1))

        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileMD5') is not None:
            self.file_md5 = m.get('FileMD5')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileURL') is not None:
            self.file_url = m.get('FileURL')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')

        if m.get('PreprocessStatus') is not None:
            self.preprocess_status = m.get('PreprocessStatus')

        if m.get('RestoreExpiration') is not None:
            self.restore_expiration = m.get('RestoreExpiration')

        if m.get('RestoreStatus') is not None:
            self.restore_status = m.get('RestoreStatus')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        self.video_stream_list = []
        if m.get('VideoStreamList') is not None:
            for k1 in m.get('VideoStreamList'):
                temp_model = main_models.GetMezzanineInfoResponseBodyMezzanineVideoStreamList()
                self.video_stream_list.append(temp_model.from_map(k1))

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class GetMezzanineInfoResponseBodyMezzanineVideoStreamList(DaraModel):
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
        hdrtype: str = None,
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
        timebase: str = None,
        width: str = None,
    ):
        # The average frame rate.
        self.avg_fps = avg_fps
        # The bitrate. Unit: Kbit/s.
        self.bitrate = bitrate
        # The full name of the encoding format.
        self.codec_long_name = codec_long_name
        # The short name of the encoding format.
        self.codec_name = codec_name
        # The tag of the encoding format.
        self.codec_tag = codec_tag
        # The tag string of the encoding format.
        self.codec_tag_string = codec_tag_string
        # The codec time base.
        self.codec_time_base = codec_time_base
        # The display aspect ratio (DAR) of the video stream.
        self.dar = dar
        # The duration of the audio file.
        self.duration = duration
        # The frame rate of the output file.
        self.fps = fps
        # The HDR type of the video stream.
        self.hdrtype = hdrtype
        # Indicates whether the video stream contains B-frames.
        self.has_bframes = has_bframes
        # The height of the video stream.
        self.height = height
        # The sequence number of the video stream. The value indicates the position of the video stream in all video streams.
        self.index = index
        # The language.
        self.lang = lang
        # The codec level.
        self.level = level
        # The total number of frames.
        self.num_frames = num_frames
        # The pixel format.
        self.pix_fmt = pix_fmt
        # The codec profile.
        self.profile = profile
        # The rotation angle of the video. Valid values: **[0,360)**.
        self.rotate = rotate
        # The sample aspect ratio (SAR) of the video stream.
        self.sar = sar
        # The beginning of the time range during which the data was queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time
        # The time base of the audio stream.
        self.timebase = timebase
        # The width of the video in pixels.
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

        if self.hdrtype is not None:
            result['HDRType'] = self.hdrtype

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

        if m.get('HDRType') is not None:
            self.hdrtype = m.get('HDRType')

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

class GetMezzanineInfoResponseBodyMezzanineAudioStreamList(DaraModel):
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
        num_frames: str = None,
        sample_fmt: str = None,
        sample_rate: str = None,
        start_time: str = None,
        timebase: str = None,
    ):
        # The bitrate.
        self.bitrate = bitrate
        # The output layout of the sound channels. Valid values:
        # 
        # *   **mono**
        # *   **stereo**
        self.channel_layout = channel_layout
        # The number of sound channels.
        self.channels = channels
        # The full name of the encoding format.
        self.codec_long_name = codec_long_name
        # The short name of the encoding format.
        self.codec_name = codec_name
        # The tag of the encoding format.
        self.codec_tag = codec_tag
        # The tag string of the encoding format.
        self.codec_tag_string = codec_tag_string
        # The codec time base.
        self.codec_time_base = codec_time_base
        # The duration of the audio file.
        self.duration = duration
        # The sequence number of the audio stream. The value indicates the position of the audio stream in all audio streams.
        self.index = index
        # The language.
        self.lang = lang
        # The total number of frames.
        self.num_frames = num_frames
        # The sampling format.
        self.sample_fmt = sample_fmt
        # The sampling rate of the audio stream.
        self.sample_rate = sample_rate
        # The beginning of the time range during which the data was queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time
        # The time base of the audio stream.
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

        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames

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

        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')

        if m.get('SampleFmt') is not None:
            self.sample_fmt = m.get('SampleFmt')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')

        return self

