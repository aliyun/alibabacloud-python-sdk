# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFaultDiagnosisOverallDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_ts: int = None,
        start_ts: int = None,
        stat_dim: str = None,
    ):
        # The app ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The end time of the query. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_ts = end_ts
        # The start time of the query. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.start_ts = start_ts
        # The statistical dimension. Valid values:
        # - **JOIN_SLOW_USER**: the number of users who joined the channel slowly
        # - **AUDIO_STUCK_USER**: the number of users who experienced audio stuttering
        # - **VIDEO_STUCK_USER**: the number of users who experienced video stuttering
        # - **VIDEO_VAGUE_USER**: the number of users who experienced blurry video
        # - **HIGH_DELAY_USER**: the number of users who experienced high call latency
        # - **FIRST_FRAME_SLOW_USER**: the number of users who experienced slow first screen rendering
        # 
        # This parameter is required.
        self.stat_dim = stat_dim

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.end_ts is not None:
            result['EndTs'] = self.end_ts

        if self.start_ts is not None:
            result['StartTs'] = self.start_ts

        if self.stat_dim is not None:
            result['StatDim'] = self.stat_dim

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')

        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')

        if m.get('StatDim') is not None:
            self.stat_dim = m.get('StatDim')

        return self

