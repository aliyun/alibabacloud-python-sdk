# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeQoeMetricDataResponseBody(DaraModel):
    def __init__(
        self,
        audio_data: List[main_models.DescribeQoeMetricDataResponseBodyAudioData] = None,
        request_id: str = None,
        video_data: List[main_models.DescribeQoeMetricDataResponseBodyVideoData] = None,
    ):
        # Audio data.
        self.audio_data = audio_data
        # Request ID.
        self.request_id = request_id
        # Video data.
        self.video_data = video_data

    def validate(self):
        if self.audio_data:
            for v1 in self.audio_data:
                 if v1:
                    v1.validate()
        if self.video_data:
            for v1 in self.video_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioData'] = []
        if self.audio_data is not None:
            for k1 in self.audio_data:
                result['AudioData'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['VideoData'] = []
        if self.video_data is not None:
            for k1 in self.video_data:
                result['VideoData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_data = []
        if m.get('AudioData') is not None:
            for k1 in m.get('AudioData'):
                temp_model = main_models.DescribeQoeMetricDataResponseBodyAudioData()
                self.audio_data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.video_data = []
        if m.get('VideoData') is not None:
            for k1 in m.get('VideoData'):
                temp_model = main_models.DescribeQoeMetricDataResponseBodyVideoData()
                self.video_data.append(temp_model.from_map(k1))

        return self

class DescribeQoeMetricDataResponseBodyVideoData(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeQoeMetricDataResponseBodyVideoDataNodes] = None,
        type: str = None,
        user_id: str = None,
    ):
        # List of coordinate points for the video metric trend graph.
        self.nodes = nodes
        # The type of metric that impacts communication experience. Valid values:
        # - **VIDEO_CAMERA**: Camera bitrate.
        # - **VIDEO_SCREEN_SHARE**: Screen sharing stream bitrate.
        # - **VIDEO_STUCK_CAMERA**: Camera stuttering.
        # - **VIDEO_STUCK_SCREEN_SHARE**: Screen sharing stuttering.
        # - **VIDEO_VAGUE_CAMERA**: Camera blur.
        # - **VIDEO_VAGUE_SCREEN_SHARE**: Screen sharing blur.
        self.type = type
        # User ID
        self.user_id = user_id

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeQoeMetricDataResponseBodyVideoDataNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeQoeMetricDataResponseBodyVideoDataNodes(DaraModel):
    def __init__(
        self,
        x: str = None,
        y: str = None,
    ):
        # The x-axis coordinate in the video metric trend graph.
        self.x = x
        # The y-axis coordinate in the Video Trend Indicator.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class DescribeQoeMetricDataResponseBodyAudioData(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeQoeMetricDataResponseBodyAudioDataNodes] = None,
        type: str = None,
        user_id: str = None,
    ):
        # List of coordinate points for the audio trend indicator.
        self.nodes = nodes
        # Communication experience. Valid values:  
        # - **AUDIO**: Audio bitrate.  
        # - **AUDIO_STUCK**: Audio downlink stuttering.
        self.type = type
        # User ID.
        self.user_id = user_id

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeQoeMetricDataResponseBodyAudioDataNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeQoeMetricDataResponseBodyAudioDataNodes(DaraModel):
    def __init__(
        self,
        x: str = None,
        y: str = None,
    ):
        # X-axis coordinate in the audio trend indicator.
        self.x = x
        # Y-axis coordinate in the audio trend indicator.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

