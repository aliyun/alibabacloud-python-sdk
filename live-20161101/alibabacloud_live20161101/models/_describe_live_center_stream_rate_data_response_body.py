# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveCenterStreamRateDataResponseBody(DaraModel):
    def __init__(
        self,
        rate_datas: List[main_models.DescribeLiveCenterStreamRateDataResponseBodyRateDatas] = None,
        request_id: str = None,
    ):
        # The list of frame rates and bitrates.
        self.rate_datas = rate_datas
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.rate_datas:
            for v1 in self.rate_datas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RateDatas'] = []
        if self.rate_datas is not None:
            for k1 in self.rate_datas:
                result['RateDatas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rate_datas = []
        if m.get('RateDatas') is not None:
            for k1 in m.get('RateDatas'):
                temp_model = main_models.DescribeLiveCenterStreamRateDataResponseBodyRateDatas()
                self.rate_datas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveCenterStreamRateDataResponseBodyRateDatas(DaraModel):
    def __init__(
        self,
        audio_fps: str = None,
        audio_rate: str = None,
        time: str = None,
        video_fps: str = None,
        video_rate: str = None,
    ):
        # The audio frame rate.
        self.audio_fps = audio_fps
        # The audio bitrate.
        self.audio_rate = audio_rate
        # The time when the data was collected. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.time = time
        # The video frame rate.
        self.video_fps = video_fps
        # The video bitrate.
        self.video_rate = video_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_fps is not None:
            result['AudioFps'] = self.audio_fps

        if self.audio_rate is not None:
            result['AudioRate'] = self.audio_rate

        if self.time is not None:
            result['Time'] = self.time

        if self.video_fps is not None:
            result['VideoFps'] = self.video_fps

        if self.video_rate is not None:
            result['VideoRate'] = self.video_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioFps') is not None:
            self.audio_fps = m.get('AudioFps')

        if m.get('AudioRate') is not None:
            self.audio_rate = m.get('AudioRate')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('VideoFps') is not None:
            self.video_fps = m.get('VideoFps')

        if m.get('VideoRate') is not None:
            self.video_rate = m.get('VideoRate')

        return self

