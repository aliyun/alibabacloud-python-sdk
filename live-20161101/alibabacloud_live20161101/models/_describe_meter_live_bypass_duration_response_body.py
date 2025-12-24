# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeMeterLiveBypassDurationResponseBody(DaraModel):
    def __init__(
        self,
        audio_summary_duration: int = None,
        data: List[main_models.DescribeMeterLiveBypassDurationResponseBodyData] = None,
        request_id: str = None,
        single_audio_summary_duration: int = None,
        single_video_summary_duration: int = None,
        total_summary_duration: int = None,
        v_1080summary_duration: int = None,
        v_480summary_duration: int = None,
        v_720summary_duration: int = None,
    ):
        # The total audio-only duration. Audio-only is a basic specification. Unit: minutes.
        self.audio_summary_duration = audio_summary_duration
        # The usage statistics for each time granularity.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The total single-stream relay duration for audio. Unit: minutes.
        self.single_audio_summary_duration = single_audio_summary_duration
        # The total single-stream relay duration for video. Unit: minutes.
        self.single_video_summary_duration = single_video_summary_duration
        # The total duration. Unit: minutes.
        self.total_summary_duration = total_summary_duration
        # The total Full HD duration. The video resolution is 1920 × 1080 or lower. Unit: minutes.
        self.v_1080summary_duration = v_1080summary_duration
        # The total standard definition (SD) duration. The video resolution is 640 × 480 or lower. Unit: minutes.
        self.v_480summary_duration = v_480summary_duration
        # The total high definition (HD) duration. The video resolution is 1280 × 720 or lower. Unit: minutes.
        self.v_720summary_duration = v_720summary_duration

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_summary_duration is not None:
            result['AudioSummaryDuration'] = self.audio_summary_duration

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.single_audio_summary_duration is not None:
            result['SingleAudioSummaryDuration'] = self.single_audio_summary_duration

        if self.single_video_summary_duration is not None:
            result['SingleVideoSummaryDuration'] = self.single_video_summary_duration

        if self.total_summary_duration is not None:
            result['TotalSummaryDuration'] = self.total_summary_duration

        if self.v_1080summary_duration is not None:
            result['V1080SummaryDuration'] = self.v_1080summary_duration

        if self.v_480summary_duration is not None:
            result['V480SummaryDuration'] = self.v_480summary_duration

        if self.v_720summary_duration is not None:
            result['V720SummaryDuration'] = self.v_720summary_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioSummaryDuration') is not None:
            self.audio_summary_duration = m.get('AudioSummaryDuration')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeMeterLiveBypassDurationResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SingleAudioSummaryDuration') is not None:
            self.single_audio_summary_duration = m.get('SingleAudioSummaryDuration')

        if m.get('SingleVideoSummaryDuration') is not None:
            self.single_video_summary_duration = m.get('SingleVideoSummaryDuration')

        if m.get('TotalSummaryDuration') is not None:
            self.total_summary_duration = m.get('TotalSummaryDuration')

        if m.get('V1080SummaryDuration') is not None:
            self.v_1080summary_duration = m.get('V1080SummaryDuration')

        if m.get('V480SummaryDuration') is not None:
            self.v_480summary_duration = m.get('V480SummaryDuration')

        if m.get('V720SummaryDuration') is not None:
            self.v_720summary_duration = m.get('V720SummaryDuration')

        return self

class DescribeMeterLiveBypassDurationResponseBodyData(DaraModel):
    def __init__(
        self,
        audio_duration: int = None,
        single_audio: int = None,
        single_video: int = None,
        timestamp: str = None,
        total_duration: int = None,
        v_1080duration: int = None,
        v_480duration: int = None,
        v_720duration: int = None,
    ):
        # The audio-only duration. Audio-only is a basic specification. Unit: minutes.
        self.audio_duration = audio_duration
        # The single-stream relay duration for audio. Unit: minutes.
        self.single_audio = single_audio
        # The single-stream relay duration for video. Unit: minutes.
        self.single_video = single_video
        # The timestamp of the data returned.
        self.timestamp = timestamp
        # The duration. Unit: minutes.
        self.total_duration = total_duration
        # The Full HD duration. The video resolution is 1920 × 1080 or lower. Unit: minutes.
        self.v_1080duration = v_1080duration
        # The SD duration. The video resolution is 640 × 480 or lower. Unit: minutes.
        self.v_480duration = v_480duration
        # The HD duration. The video resolution is 1280 × 720 or lower. Unit: minutes.
        self.v_720duration = v_720duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_duration is not None:
            result['AudioDuration'] = self.audio_duration

        if self.single_audio is not None:
            result['Single_Audio'] = self.single_audio

        if self.single_video is not None:
            result['Single_Video'] = self.single_video

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration

        if self.v_1080duration is not None:
            result['V1080Duration'] = self.v_1080duration

        if self.v_480duration is not None:
            result['V480Duration'] = self.v_480duration

        if self.v_720duration is not None:
            result['V720Duration'] = self.v_720duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioDuration') is not None:
            self.audio_duration = m.get('AudioDuration')

        if m.get('Single_Audio') is not None:
            self.single_audio = m.get('Single_Audio')

        if m.get('Single_Video') is not None:
            self.single_video = m.get('Single_Video')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')

        if m.get('V1080Duration') is not None:
            self.v_1080duration = m.get('V1080Duration')

        if m.get('V480Duration') is not None:
            self.v_480duration = m.get('V480Duration')

        if m.get('V720Duration') is not None:
            self.v_720duration = m.get('V720Duration')

        return self

