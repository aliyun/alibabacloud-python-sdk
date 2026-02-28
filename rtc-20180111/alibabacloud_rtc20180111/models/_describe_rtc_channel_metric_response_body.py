# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeRtcChannelMetricResponseBody(DaraModel):
    def __init__(
        self,
        channel_metric_info: main_models.DescribeRtcChannelMetricResponseBodyChannelMetricInfo = None,
        request_id: str = None,
    ):
        self.channel_metric_info = channel_metric_info
        self.request_id = request_id

    def validate(self):
        if self.channel_metric_info:
            self.channel_metric_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_metric_info is not None:
            result['ChannelMetricInfo'] = self.channel_metric_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelMetricInfo') is not None:
            temp_model = main_models.DescribeRtcChannelMetricResponseBodyChannelMetricInfo()
            self.channel_metric_info = temp_model.from_map(m.get('ChannelMetricInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRtcChannelMetricResponseBodyChannelMetricInfo(DaraModel):
    def __init__(
        self,
        channel_metric: main_models.DescribeRtcChannelMetricResponseBodyChannelMetricInfoChannelMetric = None,
        duration: main_models.DescribeRtcChannelMetricResponseBodyChannelMetricInfoDuration = None,
    ):
        self.channel_metric = channel_metric
        self.duration = duration

    def validate(self):
        if self.channel_metric:
            self.channel_metric.validate()
        if self.duration:
            self.duration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_metric is not None:
            result['ChannelMetric'] = self.channel_metric.to_map()

        if self.duration is not None:
            result['Duration'] = self.duration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelMetric') is not None:
            temp_model = main_models.DescribeRtcChannelMetricResponseBodyChannelMetricInfoChannelMetric()
            self.channel_metric = temp_model.from_map(m.get('ChannelMetric'))

        if m.get('Duration') is not None:
            temp_model = main_models.DescribeRtcChannelMetricResponseBodyChannelMetricInfoDuration()
            self.duration = temp_model.from_map(m.get('Duration'))

        return self

class DescribeRtcChannelMetricResponseBodyChannelMetricInfoDuration(DaraModel):
    def __init__(
        self,
        pub_duration: main_models.DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationPubDuration = None,
        sub_duration: main_models.DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationSubDuration = None,
    ):
        self.pub_duration = pub_duration
        self.sub_duration = sub_duration

    def validate(self):
        if self.pub_duration:
            self.pub_duration.validate()
        if self.sub_duration:
            self.sub_duration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pub_duration is not None:
            result['PubDuration'] = self.pub_duration.to_map()

        if self.sub_duration is not None:
            result['SubDuration'] = self.sub_duration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PubDuration') is not None:
            temp_model = main_models.DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationPubDuration()
            self.pub_duration = temp_model.from_map(m.get('PubDuration'))

        if m.get('SubDuration') is not None:
            temp_model = main_models.DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationSubDuration()
            self.sub_duration = temp_model.from_map(m.get('SubDuration'))

        return self

class DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationSubDuration(DaraModel):
    def __init__(
        self,
        audio: int = None,
        content: int = None,
        video_1080: int = None,
        video_360: int = None,
        video_720: int = None,
    ):
        self.audio = audio
        self.content = content
        self.video_1080 = video_1080
        self.video_360 = video_360
        self.video_720 = video_720

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio is not None:
            result['Audio'] = self.audio

        if self.content is not None:
            result['Content'] = self.content

        if self.video_1080 is not None:
            result['Video1080'] = self.video_1080

        if self.video_360 is not None:
            result['Video360'] = self.video_360

        if self.video_720 is not None:
            result['Video720'] = self.video_720

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audio') is not None:
            self.audio = m.get('Audio')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Video1080') is not None:
            self.video_1080 = m.get('Video1080')

        if m.get('Video360') is not None:
            self.video_360 = m.get('Video360')

        if m.get('Video720') is not None:
            self.video_720 = m.get('Video720')

        return self

class DescribeRtcChannelMetricResponseBodyChannelMetricInfoDurationPubDuration(DaraModel):
    def __init__(
        self,
        audio: int = None,
        content: int = None,
        video_1080: int = None,
        video_360: int = None,
        video_720: int = None,
    ):
        self.audio = audio
        self.content = content
        self.video_1080 = video_1080
        self.video_360 = video_360
        self.video_720 = video_720

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio is not None:
            result['Audio'] = self.audio

        if self.content is not None:
            result['Content'] = self.content

        if self.video_1080 is not None:
            result['Video1080'] = self.video_1080

        if self.video_360 is not None:
            result['Video360'] = self.video_360

        if self.video_720 is not None:
            result['Video720'] = self.video_720

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audio') is not None:
            self.audio = m.get('Audio')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Video1080') is not None:
            self.video_1080 = m.get('Video1080')

        if m.get('Video360') is not None:
            self.video_360 = m.get('Video360')

        if m.get('Video720') is not None:
            self.video_720 = m.get('Video720')

        return self

class DescribeRtcChannelMetricResponseBodyChannelMetricInfoChannelMetric(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        end_time: str = None,
        pub_user_count: int = None,
        start_time: str = None,
        sub_user_count: int = None,
        user_count: int = None,
    ):
        self.channel_id = channel_id
        self.end_time = end_time
        self.pub_user_count = pub_user_count
        self.start_time = start_time
        self.sub_user_count = sub_user_count
        self.user_count = user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.pub_user_count is not None:
            result['PubUserCount'] = self.pub_user_count

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.sub_user_count is not None:
            result['SubUserCount'] = self.sub_user_count

        if self.user_count is not None:
            result['UserCount'] = self.user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PubUserCount') is not None:
            self.pub_user_count = m.get('PubUserCount')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SubUserCount') is not None:
            self.sub_user_count = m.get('SubUserCount')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        return self

