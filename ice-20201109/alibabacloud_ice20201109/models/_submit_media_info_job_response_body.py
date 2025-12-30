# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitMediaInfoJobResponseBody(DaraModel):
    def __init__(
        self,
        media_info_job: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJob = None,
        request_id: str = None,
    ):
        # MediaInfoJobDTO
        self.media_info_job = media_info_job
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.media_info_job:
            self.media_info_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_info_job is not None:
            result['MediaInfoJob'] = self.media_info_job.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaInfoJob') is not None:
            temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJob()
            self.media_info_job = temp_model.from_map(m.get('MediaInfoJob'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SubmitMediaInfoJobResponseBodyMediaInfoJob(DaraModel):
    def __init__(
        self,
        async_: bool = None,
        finish_time: str = None,
        input: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobInput = None,
        job_id: str = None,
        media_info_property: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobMediaInfoProperty = None,
        name: str = None,
        request_id: str = None,
        schedule_config: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobScheduleConfig = None,
        status: str = None,
        submit_result_json: Dict[str, Any] = None,
        submit_time: str = None,
        trigger_source: str = None,
        user_data: str = None,
    ):
        # Indicates whether asynchronous processing was performed.
        self.async_ = async_
        # The time when the job was complete.
        self.finish_time = finish_time
        # The input of the job.
        self.input = input
        # The job ID.
        self.job_id = job_id
        # The details of the media information.
        self.media_info_property = media_info_property
        # The job name.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The scheduling information.
        self.schedule_config = schedule_config
        # The state of the job. Valid values: Init (the job is submitted), Success (the job is successful), and Fail (the job failed).
        self.status = status
        # The job submission information.
        self.submit_result_json = submit_result_json
        # The time when the job was submitted.
        self.submit_time = submit_time
        # The source of the job. Valid values: API, WorkFlow, and Console.
        self.trigger_source = trigger_source
        # The user data.
        self.user_data = user_data

    def validate(self):
        if self.input:
            self.input.validate()
        if self.media_info_property:
            self.media_info_property.validate()
        if self.schedule_config:
            self.schedule_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_ is not None:
            result['Async'] = self.async_

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.media_info_property is not None:
            result['MediaInfoProperty'] = self.media_info_property.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.submit_result_json is not None:
            result['SubmitResultJson'] = self.submit_result_json

        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time

        if self.trigger_source is not None:
            result['TriggerSource'] = self.trigger_source

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Input') is not None:
            temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MediaInfoProperty') is not None:
            temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobMediaInfoProperty()
            self.media_info_property = temp_model.from_map(m.get('MediaInfoProperty'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmitResultJson') is not None:
            self.submit_result_json = m.get('SubmitResultJson')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        if m.get('TriggerSource') is not None:
            self.trigger_source = m.get('TriggerSource')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitMediaInfoJobResponseBodyMediaInfoJobScheduleConfig(DaraModel):
    def __init__(
        self,
        pipeline_id: str = None,
        priority: int = None,
    ):
        # The ID of the ApsaraVideo Media Processing (MPS) queue that is used to run the job.
        self.pipeline_id = pipeline_id
        # The priority of the job. Valid values: 1 to 10. The greater the value, the higher the priority.
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

class SubmitMediaInfoJobResponseBodyMediaInfoJobMediaInfoProperty(DaraModel):
    def __init__(
        self,
        audio_stream_info_list: List[main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobMediaInfoPropertyAudioStreamInfoList] = None,
        file_basic_info: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobMediaInfoPropertyFileBasicInfo = None,
        video_stream_info_list: List[main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobMediaInfoPropertyVideoStreamInfoList] = None,
    ):
        # The information about the audio stream.
        self.audio_stream_info_list = audio_stream_info_list
        # The basic file information.
        self.file_basic_info = file_basic_info
        # The information about the video stream.
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
                temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobMediaInfoPropertyAudioStreamInfoList()
                self.audio_stream_info_list.append(temp_model.from_map(k1))

        if m.get('FileBasicInfo') is not None:
            temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobMediaInfoPropertyFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m.get('FileBasicInfo'))

        self.video_stream_info_list = []
        if m.get('VideoStreamInfoList') is not None:
            for k1 in m.get('VideoStreamInfoList'):
                temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobMediaInfoPropertyVideoStreamInfoList()
                self.video_stream_info_list.append(temp_model.from_map(k1))

        return self

class SubmitMediaInfoJobResponseBodyMediaInfoJobMediaInfoPropertyVideoStreamInfoList(DaraModel):
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
        # The average frame rate.
        self.avg_fps = avg_fps
        # The bitrate.
        self.bit_rate = bit_rate
        # The name of the encoding format.
        self.codec_long_name = codec_long_name
        # The encoding format.
        self.codec_name = codec_name
        # The tag of the encoding format.
        self.codec_tag = codec_tag
        # The tag string of the encoding format.
        self.codec_tag_string = codec_tag_string
        # The time base of the encoder.
        self.codec_time_base = codec_time_base
        # The display aspect ratio.
        self.dar = dar
        # The duration of the file.
        self.duration = duration
        # The frame rate.
        self.fps = fps
        # Indicates whether the video stream contains bidirectional frames (B-frames). Valid values:
        # 
        # *   0: The stream contains no B-frames.
        # *   1: The stream contains one B-frame.
        # *   2: The stream contains multiple consecutive B-frames.
        self.has_bframes = has_bframes
        # The height of the output video.
        self.height = height
        # The sequence number of the stream.
        self.index = index
        # The language of the stream.
        self.lang = lang
        # The codec level.
        self.level = level
        # The total number of frames.
        self.num_frames = num_frames
        # The pixel format.
        self.pix_fmt = pix_fmt
        # The encoder profile.
        self.profile = profile
        # The rotation angle of the video image.
        self.rotate = rotate
        # The aspect ratio of the area from which the sampling points are collected.
        self.sar = sar
        # The start time of the stream.
        self.start_time = start_time
        # The time base.
        self.time_base = time_base
        # The width of the output video.
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

class SubmitMediaInfoJobResponseBodyMediaInfoJobMediaInfoPropertyFileBasicInfo(DaraModel):
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
        # The video bitrate.
        self.bitrate = bitrate
        # The duration of the video.
        self.duration = duration
        # The file name.
        self.file_name = file_name
        # The file size.
        self.file_size = file_size
        # The state of the file.
        self.file_status = file_status
        # The file type.
        self.file_type = file_type
        # The URL of the file.
        self.file_url = file_url
        # The name of the video format.
        self.format_name = format_name
        # The height of the output video.
        self.height = height
        # The ID of the media asset.
        self.media_id = media_id
        # The region in which the file resides.
        self.region = region
        # The width of the output video.
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

class SubmitMediaInfoJobResponseBodyMediaInfoJobMediaInfoPropertyAudioStreamInfoList(DaraModel):
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
        # The bitrate.
        self.bitrate = bitrate
        # The sound channel layout.
        self.channel_layout = channel_layout
        # The number of sound channels.
        self.channels = channels
        # The name of the encoding format.
        self.codec_long_name = codec_long_name
        # The encoding format.
        self.codec_name = codec_name
        # The encoder tag.
        self.codec_tag = codec_tag
        # The name of the encoder tag.
        self.codec_tag_string = codec_tag_string
        # The time base of the encoder.
        self.codec_time_base = codec_time_base
        # The duration of the stream. Unit: seconds.
        self.duration = duration
        # The sequence number of the stream.
        self.index = index
        # The language of the stream.
        self.lang = lang
        # The sample format.
        self.sample_fmt = sample_fmt
        # The sampling rate. Unit: Hz.
        self.sample_rate = sample_rate
        # The start time of the stream.
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

class SubmitMediaInfoJobResponseBodyMediaInfoJobInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The media object. If Type is set to OSS, the URL of an OSS object is returned. Both the OSS and HTTP protocols are supported. If Type is set to Media, set this parameter to the ID of a media asset.
        self.media = media
        # The type of the media object. Valid values: OSS and Media. A value of OSS indicates an OSS object. A value of Media indicates a media asset.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

