# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class DescribeMeterImsSummaryResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeMeterImsSummaryResponseBodyData] = None,
        request_id: str = None,
    ):
        # The usage statistics of IMS.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeMeterImsSummaryResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMeterImsSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        editing_duration: str = None,
        live_edit_duration: str = None,
        live_record_duration: str = None,
        live_snapshot_count: str = None,
        live_transcode_duration: int = None,
        mps_ai_duration: int = None,
        mps_transcode_duration: int = None,
        mps_transcode_uhdduration: int = None,
    ):
        # The duration of video editing.
        self.editing_duration = editing_duration
        # The duration of live editing.
        self.live_edit_duration = live_edit_duration
        # The duration of live stream recording.
        self.live_record_duration = live_record_duration
        # The number of live stream snapshots.
        self.live_snapshot_count = live_snapshot_count
        # The duration of live stream transcoding.
        self.live_transcode_duration = live_transcode_duration
        # The duration of AI processing.
        self.mps_ai_duration = mps_ai_duration
        # The duration of video-on-demand (VOD) transcoding.
        self.mps_transcode_duration = mps_transcode_duration
        # The duration of audio and video enhancement.
        self.mps_transcode_uhdduration = mps_transcode_uhdduration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.editing_duration is not None:
            result['EditingDuration'] = self.editing_duration

        if self.live_edit_duration is not None:
            result['LiveEditDuration'] = self.live_edit_duration

        if self.live_record_duration is not None:
            result['LiveRecordDuration'] = self.live_record_duration

        if self.live_snapshot_count is not None:
            result['LiveSnapshotCount'] = self.live_snapshot_count

        if self.live_transcode_duration is not None:
            result['LiveTranscodeDuration'] = self.live_transcode_duration

        if self.mps_ai_duration is not None:
            result['MpsAiDuration'] = self.mps_ai_duration

        if self.mps_transcode_duration is not None:
            result['MpsTranscodeDuration'] = self.mps_transcode_duration

        if self.mps_transcode_uhdduration is not None:
            result['MpsTranscodeUHDDuration'] = self.mps_transcode_uhdduration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EditingDuration') is not None:
            self.editing_duration = m.get('EditingDuration')

        if m.get('LiveEditDuration') is not None:
            self.live_edit_duration = m.get('LiveEditDuration')

        if m.get('LiveRecordDuration') is not None:
            self.live_record_duration = m.get('LiveRecordDuration')

        if m.get('LiveSnapshotCount') is not None:
            self.live_snapshot_count = m.get('LiveSnapshotCount')

        if m.get('LiveTranscodeDuration') is not None:
            self.live_transcode_duration = m.get('LiveTranscodeDuration')

        if m.get('MpsAiDuration') is not None:
            self.mps_ai_duration = m.get('MpsAiDuration')

        if m.get('MpsTranscodeDuration') is not None:
            self.mps_transcode_duration = m.get('MpsTranscodeDuration')

        if m.get('MpsTranscodeUHDDuration') is not None:
            self.mps_transcode_uhdduration = m.get('MpsTranscodeUHDDuration')

        return self

