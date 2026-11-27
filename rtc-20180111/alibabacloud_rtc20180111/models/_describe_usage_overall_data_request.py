# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUsageOverallDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        start_date: int = None,
        types: str = None,
    ):
        # The app ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The end time of the query. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_date = end_date
        # The start time of the query. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.start_date = start_date
        # The metric types to query. Separate multiple values with commas (,). Valid values:
        # - **TOTAL_CALL_DURATION**: total duration.
        # - **VIDEO_CALL_DURATION**: video communication duration.
        # - **AUDIO_CALL_DURATION**: audio communication duration.
        # - **CALL_CHANNEL_COUNT**: communication channel count.
        # - **HIGHLY_CONCURRENT_CHANNEL_COUNT**: highly concurrent communication channel count.
        # - **CHANNEL_CONCURRENT_PEAK**: peak concurrent channel count.
        # - **ONLINE_USER_PEAK**: peak online user count.
        # - **TOTAL_CALL_USER**: total call users.
        # - **TOTAL_INOUT_NUM**: total inbound and outbound visits.
        # 
        # This parameter is required.
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.types is not None:
            result['Types'] = self.types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Types') is not None:
            self.types = m.get('Types')

        return self

