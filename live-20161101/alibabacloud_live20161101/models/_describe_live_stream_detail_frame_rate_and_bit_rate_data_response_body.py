# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamDetailFrameRateAndBitRateDataResponseBody(DaraModel):
    def __init__(
        self,
        frame_rate_and_bit_rate_infos: List[main_models.DescribeLiveStreamDetailFrameRateAndBitRateDataResponseBodyFrameRateAndBitRateInfos] = None,
        request_id: str = None,
    ):
        # The audio and video frame rates and bitrates at each time granularity.
        self.frame_rate_and_bit_rate_infos = frame_rate_and_bit_rate_infos
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.frame_rate_and_bit_rate_infos:
            for v1 in self.frame_rate_and_bit_rate_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FrameRateAndBitRateInfos'] = []
        if self.frame_rate_and_bit_rate_infos is not None:
            for k1 in self.frame_rate_and_bit_rate_infos:
                result['FrameRateAndBitRateInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.frame_rate_and_bit_rate_infos = []
        if m.get('FrameRateAndBitRateInfos') is not None:
            for k1 in m.get('FrameRateAndBitRateInfos'):
                temp_model = main_models.DescribeLiveStreamDetailFrameRateAndBitRateDataResponseBodyFrameRateAndBitRateInfos()
                self.frame_rate_and_bit_rate_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveStreamDetailFrameRateAndBitRateDataResponseBodyFrameRateAndBitRateInfos(DaraModel):
    def __init__(
        self,
        audio_bit_rate: float = None,
        audio_frame_rate: float = None,
        bit_rate: float = None,
        stream_url: str = None,
        time: str = None,
        video_bit_rate: float = None,
        video_frame_rate: float = None,
    ):
        # The audio bitrate of the live stream. Unit: bit/s.
        self.audio_bit_rate = audio_bit_rate
        # The audio frame rate of the live stream. Unit: FPS.
        self.audio_frame_rate = audio_frame_rate
        # The bitrate of the live stream. Unit: bit/s.
        self.bit_rate = bit_rate
        # The URL of the live stream.
        self.stream_url = stream_url
        # The time when the data was collected. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.time = time
        # The video bitrate of the live stream. Unit: bit/s.
        self.video_bit_rate = video_bit_rate
        # The video frame rate of the live stream. Unit: frames per second (FPS).
        self.video_frame_rate = video_frame_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_bit_rate is not None:
            result['AudioBitRate'] = self.audio_bit_rate

        if self.audio_frame_rate is not None:
            result['AudioFrameRate'] = self.audio_frame_rate

        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate

        if self.stream_url is not None:
            result['StreamUrl'] = self.stream_url

        if self.time is not None:
            result['Time'] = self.time

        if self.video_bit_rate is not None:
            result['VideoBitRate'] = self.video_bit_rate

        if self.video_frame_rate is not None:
            result['VideoFrameRate'] = self.video_frame_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioBitRate') is not None:
            self.audio_bit_rate = m.get('AudioBitRate')

        if m.get('AudioFrameRate') is not None:
            self.audio_frame_rate = m.get('AudioFrameRate')

        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')

        if m.get('StreamUrl') is not None:
            self.stream_url = m.get('StreamUrl')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('VideoBitRate') is not None:
            self.video_bit_rate = m.get('VideoBitRate')

        if m.get('VideoFrameRate') is not None:
            self.video_frame_rate = m.get('VideoFrameRate')

        return self

