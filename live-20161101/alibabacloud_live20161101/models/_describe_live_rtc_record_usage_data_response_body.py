# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveRtcRecordUsageDataResponseBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        audio_summary_duration: float = None,
        data: List[main_models.DescribeLiveRtcRecordUsageDataResponseBodyData] = None,
        record_mode: str = None,
        request_id: str = None,
        total_summary_duration: float = None,
        v_1080summary_duration: float = None,
        v_480summary_duration: float = None,
        v_720summary_duration: float = None,
    ):
        self.app_id = app_id
        self.audio_summary_duration = audio_summary_duration
        self.data = data
        self.record_mode = record_mode
        # Id of the request
        self.request_id = request_id
        self.total_summary_duration = total_summary_duration
        self.v_1080summary_duration = v_1080summary_duration
        self.v_480summary_duration = v_480summary_duration
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
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.audio_summary_duration is not None:
            result['AudioSummaryDuration'] = self.audio_summary_duration

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.record_mode is not None:
            result['RecordMode'] = self.record_mode

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AudioSummaryDuration') is not None:
            self.audio_summary_duration = m.get('AudioSummaryDuration')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeLiveRtcRecordUsageDataResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RecordMode') is not None:
            self.record_mode = m.get('RecordMode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalSummaryDuration') is not None:
            self.total_summary_duration = m.get('TotalSummaryDuration')

        if m.get('V1080SummaryDuration') is not None:
            self.v_1080summary_duration = m.get('V1080SummaryDuration')

        if m.get('V480SummaryDuration') is not None:
            self.v_480summary_duration = m.get('V480SummaryDuration')

        if m.get('V720SummaryDuration') is not None:
            self.v_720summary_duration = m.get('V720SummaryDuration')

        return self

class DescribeLiveRtcRecordUsageDataResponseBodyData(DaraModel):
    def __init__(
        self,
        audio_duration: float = None,
        timestamp: str = None,
        total_duration: float = None,
        v_1080duration: float = None,
        v_480duration: float = None,
        v_720duration: float = None,
    ):
        self.audio_duration = audio_duration
        self.timestamp = timestamp
        self.total_duration = total_duration
        self.v_1080duration = v_1080duration
        self.v_480duration = v_480duration
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

