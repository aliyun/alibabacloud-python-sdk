# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class SubmitMediaInfoJobResponseBody(DaraModel):
    def __init__(
        self,
        media_info_job: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJob = None,
        request_id: str = None,
    ):
        # The details of the media information analysis job.
        self.media_info_job = media_info_job
        # The ID of the request.
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
        code: str = None,
        creation_time: str = None,
        input: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobInput = None,
        job_id: str = None,
        mnsmessage_result: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobMNSMessageResult = None,
        message: str = None,
        pipeline_id: str = None,
        properties: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobProperties = None,
        state: str = None,
        user_data: str = None,
    ):
        # Indicates whether the job is run in asynchronous mode.
        self.async_ = async_
        # The error code returned if the job fails.
        self.code = code
        # The time when the job was created.
        self.creation_time = creation_time
        # The information about the input media file.
        self.input = input
        # The ID of the job.
        self.job_id = job_id
        # The message sent by Message Service (MNS) to notify users of the job result.
        self.mnsmessage_result = mnsmessage_result
        # The error message returned if the job fails.
        self.message = message
        # The ID of the MPS queue to which the analysis job is submitted.
        self.pipeline_id = pipeline_id
        # The properties of the input media file.
        self.properties = properties
        # The status of the job. Valid values:
        # 
        # *   **Success**: The job is successful.
        # *   **Fail**: The job fails.
        # *   **Analyzing**: The job is being run.
        self.state = state
        # The custom data.
        self.user_data = user_data

    def validate(self):
        if self.input:
            self.input.validate()
        if self.mnsmessage_result:
            self.mnsmessage_result.validate()
        if self.properties:
            self.properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_ is not None:
            result['Async'] = self.async_

        if self.code is not None:
            result['Code'] = self.code

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.mnsmessage_result is not None:
            result['MNSMessageResult'] = self.mnsmessage_result.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.properties is not None:
            result['Properties'] = self.properties.to_map()

        if self.state is not None:
            result['State'] = self.state

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Input') is not None:
            temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MNSMessageResult') is not None:
            temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobMNSMessageResult()
            self.mnsmessage_result = temp_model.from_map(m.get('MNSMessageResult'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('Properties') is not None:
            temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobProperties()
            self.properties = temp_model.from_map(m.get('Properties'))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitMediaInfoJobResponseBodyMediaInfoJobProperties(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        duration: str = None,
        file_format: str = None,
        file_size: str = None,
        format: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesFormat = None,
        fps: str = None,
        height: str = None,
        md5: str = None,
        streams: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreams = None,
        width: str = None,
    ):
        # The bitrate. Unit: Kbit/s.
        self.bitrate = bitrate
        # The duration of the input media file. Unit: seconds.
        self.duration = duration
        # The format of the input media file.
        self.file_format = file_format
        # The size of the file. Unit: bytes.
        self.file_size = file_size
        # The format information.
        self.format = format
        # The frame rate.
        self.fps = fps
        # The height of the video. Unit: pixel.
        self.height = height
        self.md5 = md5
        # The media streams that are contained in the input media file.
        self.streams = streams
        # The width of the video. Unit: pixel.
        self.width = width

    def validate(self):
        if self.format:
            self.format.validate()
        if self.streams:
            self.streams.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_format is not None:
            result['FileFormat'] = self.file_format

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.format is not None:
            result['Format'] = self.format.to_map()

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.height is not None:
            result['Height'] = self.height

        if self.md5 is not None:
            result['MD5'] = self.md5

        if self.streams is not None:
            result['Streams'] = self.streams.to_map()

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileFormat') is not None:
            self.file_format = m.get('FileFormat')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('Format') is not None:
            temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesFormat()
            self.format = temp_model.from_map(m.get('Format'))

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('MD5') is not None:
            self.md5 = m.get('MD5')

        if m.get('Streams') is not None:
            temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreams()
            self.streams = temp_model.from_map(m.get('Streams'))

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreams(DaraModel):
    def __init__(
        self,
        audio_stream_list: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsAudioStreamList = None,
        subtitle_stream_list: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsSubtitleStreamList = None,
        video_stream_list: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsVideoStreamList = None,
    ):
        self.audio_stream_list = audio_stream_list
        self.subtitle_stream_list = subtitle_stream_list
        self.video_stream_list = video_stream_list

    def validate(self):
        if self.audio_stream_list:
            self.audio_stream_list.validate()
        if self.subtitle_stream_list:
            self.subtitle_stream_list.validate()
        if self.video_stream_list:
            self.video_stream_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_stream_list is not None:
            result['AudioStreamList'] = self.audio_stream_list.to_map()

        if self.subtitle_stream_list is not None:
            result['SubtitleStreamList'] = self.subtitle_stream_list.to_map()

        if self.video_stream_list is not None:
            result['VideoStreamList'] = self.video_stream_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioStreamList') is not None:
            temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsAudioStreamList()
            self.audio_stream_list = temp_model.from_map(m.get('AudioStreamList'))

        if m.get('SubtitleStreamList') is not None:
            temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsSubtitleStreamList()
            self.subtitle_stream_list = temp_model.from_map(m.get('SubtitleStreamList'))

        if m.get('VideoStreamList') is not None:
            temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsVideoStreamList()
            self.video_stream_list = temp_model.from_map(m.get('VideoStreamList'))

        return self

class SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsVideoStreamList(DaraModel):
    def __init__(
        self,
        video_stream: List[main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsVideoStreamListVideoStream] = None,
    ):
        self.video_stream = video_stream

    def validate(self):
        if self.video_stream:
            for v1 in self.video_stream:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VideoStream'] = []
        if self.video_stream is not None:
            for k1 in self.video_stream:
                result['VideoStream'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_stream = []
        if m.get('VideoStream') is not None:
            for k1 in m.get('VideoStream'):
                temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsVideoStreamListVideoStream()
                self.video_stream.append(temp_model.from_map(k1))

        return self

class SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsVideoStreamListVideoStream(DaraModel):
    def __init__(
        self,
        avg_fps: str = None,
        bitrate: str = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        color_primaries: str = None,
        color_range: str = None,
        color_transfer: str = None,
        dar: str = None,
        dolby_vision: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsVideoStreamListVideoStreamDolbyVision = None,
        duration: str = None,
        duration_inaccurate: str = None,
        fps: str = None,
        has_bframes: str = None,
        height: str = None,
        index: str = None,
        lang: str = None,
        level: str = None,
        network_cost: main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsVideoStreamListVideoStreamNetworkCost = None,
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
        self.color_primaries = color_primaries
        self.color_range = color_range
        self.color_transfer = color_transfer
        self.dar = dar
        self.dolby_vision = dolby_vision
        self.duration = duration
        self.duration_inaccurate = duration_inaccurate
        self.fps = fps
        self.has_bframes = has_bframes
        self.height = height
        self.index = index
        self.lang = lang
        self.level = level
        self.network_cost = network_cost
        self.num_frames = num_frames
        self.pix_fmt = pix_fmt
        self.profile = profile
        self.rotate = rotate
        self.sar = sar
        self.start_time = start_time
        self.timebase = timebase
        self.width = width

    def validate(self):
        if self.dolby_vision:
            self.dolby_vision.validate()
        if self.network_cost:
            self.network_cost.validate()

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

        if self.color_primaries is not None:
            result['ColorPrimaries'] = self.color_primaries

        if self.color_range is not None:
            result['ColorRange'] = self.color_range

        if self.color_transfer is not None:
            result['ColorTransfer'] = self.color_transfer

        if self.dar is not None:
            result['Dar'] = self.dar

        if self.dolby_vision is not None:
            result['DolbyVision'] = self.dolby_vision.to_map()

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.duration_inaccurate is not None:
            result['DurationInaccurate'] = self.duration_inaccurate

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

        if self.network_cost is not None:
            result['NetworkCost'] = self.network_cost.to_map()

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

        if m.get('ColorPrimaries') is not None:
            self.color_primaries = m.get('ColorPrimaries')

        if m.get('ColorRange') is not None:
            self.color_range = m.get('ColorRange')

        if m.get('ColorTransfer') is not None:
            self.color_transfer = m.get('ColorTransfer')

        if m.get('Dar') is not None:
            self.dar = m.get('Dar')

        if m.get('DolbyVision') is not None:
            temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsVideoStreamListVideoStreamDolbyVision()
            self.dolby_vision = temp_model.from_map(m.get('DolbyVision'))

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('DurationInaccurate') is not None:
            self.duration_inaccurate = m.get('DurationInaccurate')

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

        if m.get('NetworkCost') is not None:
            temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsVideoStreamListVideoStreamNetworkCost()
            self.network_cost = temp_model.from_map(m.get('NetworkCost'))

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

class SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsVideoStreamListVideoStreamNetworkCost(DaraModel):
    def __init__(
        self,
        avg_bitrate: str = None,
        cost_bandwidth: str = None,
        preload_time: str = None,
    ):
        self.avg_bitrate = avg_bitrate
        self.cost_bandwidth = cost_bandwidth
        self.preload_time = preload_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_bitrate is not None:
            result['AvgBitrate'] = self.avg_bitrate

        if self.cost_bandwidth is not None:
            result['CostBandwidth'] = self.cost_bandwidth

        if self.preload_time is not None:
            result['PreloadTime'] = self.preload_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgBitrate') is not None:
            self.avg_bitrate = m.get('AvgBitrate')

        if m.get('CostBandwidth') is not None:
            self.cost_bandwidth = m.get('CostBandwidth')

        if m.get('PreloadTime') is not None:
            self.preload_time = m.get('PreloadTime')

        return self

class SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsVideoStreamListVideoStreamDolbyVision(DaraModel):
    def __init__(
        self,
        level: str = None,
        profile: str = None,
    ):
        self.level = level
        self.profile = profile

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['Level'] = self.level

        if self.profile is not None:
            result['Profile'] = self.profile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        return self

class SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsSubtitleStreamList(DaraModel):
    def __init__(
        self,
        subtitle_stream: List[main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsSubtitleStreamListSubtitleStream] = None,
    ):
        self.subtitle_stream = subtitle_stream

    def validate(self):
        if self.subtitle_stream:
            for v1 in self.subtitle_stream:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubtitleStream'] = []
        if self.subtitle_stream is not None:
            for k1 in self.subtitle_stream:
                result['SubtitleStream'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subtitle_stream = []
        if m.get('SubtitleStream') is not None:
            for k1 in m.get('SubtitleStream'):
                temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsSubtitleStreamListSubtitleStream()
                self.subtitle_stream.append(temp_model.from_map(k1))

        return self

class SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsSubtitleStreamListSubtitleStream(DaraModel):
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

class SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsAudioStreamList(DaraModel):
    def __init__(
        self,
        audio_stream: List[main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsAudioStreamListAudioStream] = None,
    ):
        self.audio_stream = audio_stream

    def validate(self):
        if self.audio_stream:
            for v1 in self.audio_stream:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioStream'] = []
        if self.audio_stream is not None:
            for k1 in self.audio_stream:
                result['AudioStream'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_stream = []
        if m.get('AudioStream') is not None:
            for k1 in m.get('AudioStream'):
                temp_model = main_models.SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsAudioStreamListAudioStream()
                self.audio_stream.append(temp_model.from_map(k1))

        return self

class SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesStreamsAudioStreamListAudioStream(DaraModel):
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
        duration_inaccurate: str = None,
        index: str = None,
        lang: str = None,
        num_frames: str = None,
        sample_fmt: str = None,
        samplerate: str = None,
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
        self.duration_inaccurate = duration_inaccurate
        self.index = index
        self.lang = lang
        self.num_frames = num_frames
        self.sample_fmt = sample_fmt
        self.samplerate = samplerate
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

        if self.duration_inaccurate is not None:
            result['DurationInaccurate'] = self.duration_inaccurate

        if self.index is not None:
            result['Index'] = self.index

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames

        if self.sample_fmt is not None:
            result['SampleFmt'] = self.sample_fmt

        if self.samplerate is not None:
            result['Samplerate'] = self.samplerate

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

        if m.get('DurationInaccurate') is not None:
            self.duration_inaccurate = m.get('DurationInaccurate')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')

        if m.get('SampleFmt') is not None:
            self.sample_fmt = m.get('SampleFmt')

        if m.get('Samplerate') is not None:
            self.samplerate = m.get('Samplerate')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')

        return self

class SubmitMediaInfoJobResponseBodyMediaInfoJobPropertiesFormat(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        duration: str = None,
        format_long_name: str = None,
        format_name: str = None,
        num_programs: str = None,
        num_streams: str = None,
        size: str = None,
        start_time: str = None,
        tags: Dict[str, Any] = None,
    ):
        # The total bitrate. Unit: Kbit/s.
        self.bitrate = bitrate
        # The duration of the input media file. Unit: seconds.
        self.duration = duration
        # The full name of the container format.
        self.format_long_name = format_long_name
        # The short name of the container format. For more information about the parameters, see [Parameter details](https://help.aliyun.com/document_detail/29253.html).
        self.format_name = format_name
        # The total number of program streams.
        self.num_programs = num_programs
        # The total number of media streams.
        self.num_streams = num_streams
        # The size of the file. Unit: bytes.
        self.size = size
        # The start time.
        self.start_time = start_time
        self.tags = tags

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

        if self.format_long_name is not None:
            result['FormatLongName'] = self.format_long_name

        if self.format_name is not None:
            result['FormatName'] = self.format_name

        if self.num_programs is not None:
            result['NumPrograms'] = self.num_programs

        if self.num_streams is not None:
            result['NumStreams'] = self.num_streams

        if self.size is not None:
            result['Size'] = self.size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FormatLongName') is not None:
            self.format_long_name = m.get('FormatLongName')

        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')

        if m.get('NumPrograms') is not None:
            self.num_programs = m.get('NumPrograms')

        if m.get('NumStreams') is not None:
            self.num_streams = m.get('NumStreams')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

class SubmitMediaInfoJobResponseBodyMediaInfoJobMNSMessageResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        message_id: str = None,
    ):
        # The error code that is returned if the job fails. This parameter is not returned if the job is successful.
        self.error_code = error_code
        # The error message that is returned if the job fails. This parameter is not returned if the job is successful.
        self.error_message = error_message
        # The ID of the message that is returned if the job is successful. This parameter is not returned if the job fails.
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        return self

class SubmitMediaInfoJobResponseBodyMediaInfoJobInput(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
    ):
        # The name of the OSS bucket in which the input media file is stored.
        self.bucket = bucket
        # The region in which the OSS bucket that stores the input media file resides.
        self.location = location
        # The name of the OSS object that is used as the input media file.
        self.object = object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.location is not None:
            result['Location'] = self.location

        if self.object is not None:
            result['Object'] = self.object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        return self

