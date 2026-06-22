# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class SceneElement(DaraModel):
    def __init__(
        self,
        frame_times: List[int] = None,
        labels: List[main_models.Label] = None,
        time_range: List[int] = None,
        video_stream_index: int = None,
    ):
        # The timestamps of the frames within the current video element that match the search content. The unit is milliseconds.
        self.frame_times = frame_times
        # The label information.
        self.labels = labels
        # The time range of the video element. The array has a fixed length of 2. The two values represent the start time and end time in milliseconds.
        self.time_range = time_range
        # The index of the video stream to which the current video scene element belongs. This corresponds to the index in the [VideoStreams](https://help.aliyun.com/zh/imm/developer-reference/api-imm-2020-09-30-detectmediameta?spm=a2c4g.11186623.0.0.463e600fIDdM8r#api-detail-40) array.
        self.video_stream_index = video_stream_index

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frame_times is not None:
            result['FrameTimes'] = self.frame_times

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.time_range is not None:
            result['TimeRange'] = self.time_range

        if self.video_stream_index is not None:
            result['VideoStreamIndex'] = self.video_stream_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameTimes') is not None:
            self.frame_times = m.get('FrameTimes')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.Label()
                self.labels.append(temp_model.from_map(k1))

        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')

        if m.get('VideoStreamIndex') is not None:
            self.video_stream_index = m.get('VideoStreamIndex')

        return self

