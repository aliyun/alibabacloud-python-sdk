# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveUpVideoAudioInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        up_items: main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItems = None,
    ):
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.request_id = request_id
        # The request ID.
        self.up_items = up_items

    def validate(self):
        if self.up_items:
            self.up_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.up_items is not None:
            result['UpItems'] = self.up_items.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UpItems') is not None:
            temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItems()
            self.up_items = temp_model.from_map(m.get('UpItems'))

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItems(DaraModel):
    def __init__(
        self,
        publish_item: List[main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItem] = None,
    ):
        self.publish_item = publish_item

    def validate(self):
        if self.publish_item:
            for v1 in self.publish_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PublishItem'] = []
        if self.publish_item is not None:
            for k1 in self.publish_item:
                result['PublishItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.publish_item = []
        if m.get('PublishItem') is not None:
            for k1 in m.get('PublishItem'):
                temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItem()
                self.publish_item.append(temp_model.from_map(k1))

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItem(DaraModel):
    def __init__(
        self,
        aac_headers: main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAacHeaders = None,
        app_name: str = None,
        audio_bit_rate: main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioBitRate = None,
        audio_frames: main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioFrames = None,
        audio_interval: main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioInterval = None,
        audio_stamps: main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioStamps = None,
        avc_headers: main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAvcHeaders = None,
        codec_info: str = None,
        domain_name: str = None,
        error_flags: main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemErrorFlags = None,
        publish_interval: str = None,
        publish_ip: str = None,
        publish_status: str = None,
        publish_time: str = None,
        stop_time: str = None,
        stream_name: str = None,
        unique_id: str = None,
        video_and_audio_stamp: main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoAndAudioStamp = None,
        video_bit_rate: main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoBitRate = None,
        video_frames: main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoFrames = None,
        video_interval: main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoInterval = None,
        video_stamps: main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoStamps = None,
    ):
        # The details about the audio and video data of the stream ingest occurrences.
        self.aac_headers = aac_headers
        # The metric value at a granularity of seconds at the query time.
        self.app_name = app_name
        # The name of the application to which the ingested stream belongs.
        self.audio_bit_rate = audio_bit_rate
        # The metric value at a granularity of seconds at the query time.
        self.audio_frames = audio_frames
        # The metric value at a granularity of seconds at the query time.
        self.audio_interval = audio_interval
        # The metric value at a granularity of seconds at the query time.
        self.audio_stamps = audio_stamps
        # The metric value at a granularity of seconds at the query time.
        self.avc_headers = avc_headers
        # The metric value at a granularity of seconds at the query time.
        self.codec_info = codec_info
        # The audio and video encoding information.
        self.domain_name = domain_name
        # The ingest domain.
        self.error_flags = error_flags
        # The metric value at a granularity of seconds at the query time.
        self.publish_interval = publish_interval
        # The stream ingest duration. Unit: seconds. A hyphen (-) indicates that the stream is being ingested and the duration cannot be returned.
        self.publish_ip = publish_ip
        # The IP address of the stream ingest client.
        self.publish_status = publish_status
        # The stream ingest status. A value of 1 indicates that the stream is being ingested. A value of 0 indicates that the stream was ingested.
        self.publish_time = publish_time
        # The start time of stream ingest. The time is displayed in UTC.
        self.stop_time = stop_time
        # The end time of stream ingest. The time is displayed in UTC.
        self.stream_name = stream_name
        # The name of the stream.
        self.unique_id = unique_id
        # The unique ID of each stream ingest occurrence.
        self.video_and_audio_stamp = video_and_audio_stamp
        # The metric value at a granularity of seconds at the query time.
        self.video_bit_rate = video_bit_rate
        # The metric value at a granularity of seconds at the query time.
        self.video_frames = video_frames
        # The metric value at a granularity of seconds at the query time.
        self.video_interval = video_interval
        # The metric value at a granularity of seconds at the query time.
        self.video_stamps = video_stamps

    def validate(self):
        if self.aac_headers:
            self.aac_headers.validate()
        if self.audio_bit_rate:
            self.audio_bit_rate.validate()
        if self.audio_frames:
            self.audio_frames.validate()
        if self.audio_interval:
            self.audio_interval.validate()
        if self.audio_stamps:
            self.audio_stamps.validate()
        if self.avc_headers:
            self.avc_headers.validate()
        if self.error_flags:
            self.error_flags.validate()
        if self.video_and_audio_stamp:
            self.video_and_audio_stamp.validate()
        if self.video_bit_rate:
            self.video_bit_rate.validate()
        if self.video_frames:
            self.video_frames.validate()
        if self.video_interval:
            self.video_interval.validate()
        if self.video_stamps:
            self.video_stamps.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aac_headers is not None:
            result['AacHeaders'] = self.aac_headers.to_map()

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.audio_bit_rate is not None:
            result['AudioBitRate'] = self.audio_bit_rate.to_map()

        if self.audio_frames is not None:
            result['AudioFrames'] = self.audio_frames.to_map()

        if self.audio_interval is not None:
            result['AudioInterval'] = self.audio_interval.to_map()

        if self.audio_stamps is not None:
            result['AudioStamps'] = self.audio_stamps.to_map()

        if self.avc_headers is not None:
            result['AvcHeaders'] = self.avc_headers.to_map()

        if self.codec_info is not None:
            result['CodecInfo'] = self.codec_info

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.error_flags is not None:
            result['ErrorFlags'] = self.error_flags.to_map()

        if self.publish_interval is not None:
            result['PublishInterval'] = self.publish_interval

        if self.publish_ip is not None:
            result['PublishIp'] = self.publish_ip

        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.stop_time is not None:
            result['StopTime'] = self.stop_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id

        if self.video_and_audio_stamp is not None:
            result['VideoAndAudioStamp'] = self.video_and_audio_stamp.to_map()

        if self.video_bit_rate is not None:
            result['VideoBitRate'] = self.video_bit_rate.to_map()

        if self.video_frames is not None:
            result['VideoFrames'] = self.video_frames.to_map()

        if self.video_interval is not None:
            result['VideoInterval'] = self.video_interval.to_map()

        if self.video_stamps is not None:
            result['VideoStamps'] = self.video_stamps.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AacHeaders') is not None:
            temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAacHeaders()
            self.aac_headers = temp_model.from_map(m.get('AacHeaders'))

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AudioBitRate') is not None:
            temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioBitRate()
            self.audio_bit_rate = temp_model.from_map(m.get('AudioBitRate'))

        if m.get('AudioFrames') is not None:
            temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioFrames()
            self.audio_frames = temp_model.from_map(m.get('AudioFrames'))

        if m.get('AudioInterval') is not None:
            temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioInterval()
            self.audio_interval = temp_model.from_map(m.get('AudioInterval'))

        if m.get('AudioStamps') is not None:
            temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioStamps()
            self.audio_stamps = temp_model.from_map(m.get('AudioStamps'))

        if m.get('AvcHeaders') is not None:
            temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAvcHeaders()
            self.avc_headers = temp_model.from_map(m.get('AvcHeaders'))

        if m.get('CodecInfo') is not None:
            self.codec_info = m.get('CodecInfo')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ErrorFlags') is not None:
            temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemErrorFlags()
            self.error_flags = temp_model.from_map(m.get('ErrorFlags'))

        if m.get('PublishInterval') is not None:
            self.publish_interval = m.get('PublishInterval')

        if m.get('PublishIp') is not None:
            self.publish_ip = m.get('PublishIp')

        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')

        if m.get('VideoAndAudioStamp') is not None:
            temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoAndAudioStamp()
            self.video_and_audio_stamp = temp_model.from_map(m.get('VideoAndAudioStamp'))

        if m.get('VideoBitRate') is not None:
            temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoBitRate()
            self.video_bit_rate = temp_model.from_map(m.get('VideoBitRate'))

        if m.get('VideoFrames') is not None:
            temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoFrames()
            self.video_frames = temp_model.from_map(m.get('VideoFrames'))

        if m.get('VideoInterval') is not None:
            temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoInterval()
            self.video_interval = temp_model.from_map(m.get('VideoInterval'))

        if m.get('VideoStamps') is not None:
            temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoStamps()
            self.video_stamps = temp_model.from_map(m.get('VideoStamps'))

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoStamps(DaraModel):
    def __init__(
        self,
        video_stamps: List[main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoStampsVideoStamps] = None,
    ):
        self.video_stamps = video_stamps

    def validate(self):
        if self.video_stamps:
            for v1 in self.video_stamps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VideoStamps'] = []
        if self.video_stamps is not None:
            for k1 in self.video_stamps:
                result['VideoStamps'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_stamps = []
        if m.get('VideoStamps') is not None:
            for k1 in m.get('VideoStamps'):
                temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoStampsVideoStamps()
                self.video_stamps.append(temp_model.from_map(k1))

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoStampsVideoStamps(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: int = None,
    ):
        # The video timestamp. Unit: milliseconds.
        self.time = time
        # The query time. The value is a UNIX timestamp in milliseconds.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoInterval(DaraModel):
    def __init__(
        self,
        video_interval: List[main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoIntervalVideoInterval] = None,
    ):
        self.video_interval = video_interval

    def validate(self):
        if self.video_interval:
            for v1 in self.video_interval:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VideoInterval'] = []
        if self.video_interval is not None:
            for k1 in self.video_interval:
                result['VideoInterval'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_interval = []
        if m.get('VideoInterval') is not None:
            for k1 in m.get('VideoInterval'):
                temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoIntervalVideoInterval()
                self.video_interval.append(temp_model.from_map(k1))

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoIntervalVideoInterval(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: int = None,
    ):
        # The maximum video frame interval. Unit: milliseconds.
        self.time = time
        # The query time. The value is a UNIX timestamp in milliseconds.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoFrames(DaraModel):
    def __init__(
        self,
        video_frames: List[main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoFramesVideoFrames] = None,
    ):
        self.video_frames = video_frames

    def validate(self):
        if self.video_frames:
            for v1 in self.video_frames:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VideoFrames'] = []
        if self.video_frames is not None:
            for k1 in self.video_frames:
                result['VideoFrames'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_frames = []
        if m.get('VideoFrames') is not None:
            for k1 in m.get('VideoFrames'):
                temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoFramesVideoFrames()
                self.video_frames.append(temp_model.from_map(k1))

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoFramesVideoFrames(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: int = None,
    ):
        # The frame rate of the video. Unit: frames.
        self.time = time
        # The query time. The value is a UNIX timestamp in milliseconds.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoBitRate(DaraModel):
    def __init__(
        self,
        video_bit_rate: List[main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoBitRateVideoBitRate] = None,
    ):
        self.video_bit_rate = video_bit_rate

    def validate(self):
        if self.video_bit_rate:
            for v1 in self.video_bit_rate:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VideoBitRate'] = []
        if self.video_bit_rate is not None:
            for k1 in self.video_bit_rate:
                result['VideoBitRate'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_bit_rate = []
        if m.get('VideoBitRate') is not None:
            for k1 in m.get('VideoBitRate'):
                temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoBitRateVideoBitRate()
                self.video_bit_rate.append(temp_model.from_map(k1))

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoBitRateVideoBitRate(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: int = None,
    ):
        # The bitrate of the video. Unit: bit/s.
        self.time = time
        # The query time. The value is a UNIX timestamp in milliseconds.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoAndAudioStamp(DaraModel):
    def __init__(
        self,
        v_astamp: List[main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoAndAudioStampVAStamp] = None,
    ):
        self.v_astamp = v_astamp

    def validate(self):
        if self.v_astamp:
            for v1 in self.v_astamp:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['V_AStamp'] = []
        if self.v_astamp is not None:
            for k1 in self.v_astamp:
                result['V_AStamp'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.v_astamp = []
        if m.get('V_AStamp') is not None:
            for k1 in m.get('V_AStamp'):
                temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoAndAudioStampVAStamp()
                self.v_astamp.append(temp_model.from_map(k1))

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemVideoAndAudioStampVAStamp(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: int = None,
    ):
        # The difference between the audio and video timestamps. Unit: milliseconds.
        self.time = time
        # The query time. The value is a UNIX timestamp in milliseconds.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemErrorFlags(DaraModel):
    def __init__(
        self,
        error_flags: List[main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemErrorFlagsErrorFlags] = None,
    ):
        self.error_flags = error_flags

    def validate(self):
        if self.error_flags:
            for v1 in self.error_flags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ErrorFlags'] = []
        if self.error_flags is not None:
            for k1 in self.error_flags:
                result['ErrorFlags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_flags = []
        if m.get('ErrorFlags') is not None:
            for k1 in m.get('ErrorFlags'):
                temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemErrorFlagsErrorFlags()
                self.error_flags.append(temp_model.from_map(k1))

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemErrorFlagsErrorFlags(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: int = None,
    ):
        # The number of times the error code that indicates interrupted stream ingest was returned.
        self.time = time
        # The query time. The value is a UNIX timestamp in milliseconds.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAvcHeaders(DaraModel):
    def __init__(
        self,
        avc_headers: List[main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAvcHeadersAvcHeaders] = None,
    ):
        self.avc_headers = avc_headers

    def validate(self):
        if self.avc_headers:
            for v1 in self.avc_headers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvcHeaders'] = []
        if self.avc_headers is not None:
            for k1 in self.avc_headers:
                result['AvcHeaders'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.avc_headers = []
        if m.get('AvcHeaders') is not None:
            for k1 in m.get('AvcHeaders'):
                temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAvcHeadersAvcHeaders()
                self.avc_headers.append(temp_model.from_map(k1))

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAvcHeadersAvcHeaders(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: int = None,
    ):
        # The number of AVC headers in the audio.
        self.time = time
        # The query time. The value is a UNIX timestamp in milliseconds.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioStamps(DaraModel):
    def __init__(
        self,
        audio_stamps: List[main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioStampsAudioStamps] = None,
    ):
        self.audio_stamps = audio_stamps

    def validate(self):
        if self.audio_stamps:
            for v1 in self.audio_stamps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioStamps'] = []
        if self.audio_stamps is not None:
            for k1 in self.audio_stamps:
                result['AudioStamps'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_stamps = []
        if m.get('AudioStamps') is not None:
            for k1 in m.get('AudioStamps'):
                temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioStampsAudioStamps()
                self.audio_stamps.append(temp_model.from_map(k1))

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioStampsAudioStamps(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: int = None,
    ):
        # The audio timestamp. Unit: milliseconds.
        self.time = time
        # The query time. The value is a UNIX timestamp in milliseconds.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioInterval(DaraModel):
    def __init__(
        self,
        audio_interval: List[main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioIntervalAudioInterval] = None,
    ):
        self.audio_interval = audio_interval

    def validate(self):
        if self.audio_interval:
            for v1 in self.audio_interval:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioInterval'] = []
        if self.audio_interval is not None:
            for k1 in self.audio_interval:
                result['AudioInterval'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_interval = []
        if m.get('AudioInterval') is not None:
            for k1 in m.get('AudioInterval'):
                temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioIntervalAudioInterval()
                self.audio_interval.append(temp_model.from_map(k1))

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioIntervalAudioInterval(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: int = None,
    ):
        # The maximum audio frame interval. Unit: milliseconds.
        self.time = time
        # The query time. The value is a UNIX timestamp in milliseconds.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioFrames(DaraModel):
    def __init__(
        self,
        audio_frames: List[main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioFramesAudioFrames] = None,
    ):
        self.audio_frames = audio_frames

    def validate(self):
        if self.audio_frames:
            for v1 in self.audio_frames:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioFrames'] = []
        if self.audio_frames is not None:
            for k1 in self.audio_frames:
                result['AudioFrames'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_frames = []
        if m.get('AudioFrames') is not None:
            for k1 in m.get('AudioFrames'):
                temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioFramesAudioFrames()
                self.audio_frames.append(temp_model.from_map(k1))

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioFramesAudioFrames(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: int = None,
    ):
        # The frame rate of the audio. Unit: frames.
        self.time = time
        # The query time. The value is a UNIX timestamp in milliseconds.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioBitRate(DaraModel):
    def __init__(
        self,
        audio_bit_rate: List[main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioBitRateAudioBitRate] = None,
    ):
        self.audio_bit_rate = audio_bit_rate

    def validate(self):
        if self.audio_bit_rate:
            for v1 in self.audio_bit_rate:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioBitRate'] = []
        if self.audio_bit_rate is not None:
            for k1 in self.audio_bit_rate:
                result['AudioBitRate'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_bit_rate = []
        if m.get('AudioBitRate') is not None:
            for k1 in m.get('AudioBitRate'):
                temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioBitRateAudioBitRate()
                self.audio_bit_rate.append(temp_model.from_map(k1))

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAudioBitRateAudioBitRate(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: int = None,
    ):
        # The bitrate of the audio. Unit: bit/s.
        self.time = time
        # The query time. The value is a UNIX timestamp in milliseconds.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAacHeaders(DaraModel):
    def __init__(
        self,
        aac_headers: List[main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAacHeadersAacHeaders] = None,
    ):
        self.aac_headers = aac_headers

    def validate(self):
        if self.aac_headers:
            for v1 in self.aac_headers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AacHeaders'] = []
        if self.aac_headers is not None:
            for k1 in self.aac_headers:
                result['AacHeaders'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aac_headers = []
        if m.get('AacHeaders') is not None:
            for k1 in m.get('AacHeaders'):
                temp_model = main_models.DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAacHeadersAacHeaders()
                self.aac_headers.append(temp_model.from_map(k1))

        return self

class DescribeLiveUpVideoAudioInfoResponseBodyUpItemsPublishItemAacHeadersAacHeaders(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: int = None,
    ):
        # The number of AAC headers in the audio.
        self.time = time
        # The query time. The value is a UNIX timestamp in milliseconds.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

