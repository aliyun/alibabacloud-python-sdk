# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeQualityOverallDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_date: int = None,
        start_date: int = None,
        types: str = None,
    ):
        # APP ID
        # 
        # This parameter is required.
        self.app_id = app_id
        # The End Time of the query, represented as a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_date = end_date
        # The Start Time of the query, represented as a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.start_date = start_date
        # The Metric Types to query, separated by commas (,). Valid values:
        # - **JOIN_CHANNEL_SUC_RATE**: Channel Join Success Rate.
        # - **JOIN_CHANNEL_SUC_FIVE_SEC_RATE**: Five-second Channel Join Success Rate.
        # - **VIDEO_FIRST_PIC_DUR**: Time to First Video Frame.
        # - **AUDIO_STUCK_RATE**: Audio Lag Rate.
        # - **VIDEO_STUCK_RATE**: Video Lag Rate.
        # - **AUDIO_DELAY**: Audio Delay.
        # - **VIDEO_DELAY**: Video Delay.
        # - **AUDIO_HIGH_QUALITY_TRANSMISSION_RATE**: Audio High-quality Transmission Rate.
        # - **VIDEO_HIGH_QUALITY_TRANSMISSION_RATE**: Video High-quality Transmission Rate.
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

