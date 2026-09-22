# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAiAppDetailStatRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The ID of the AI application. This parameter is required.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The end time of the query. Format: YYYY-MM-DD HH:mm:ss.
        self.end_time = end_time
        # The ID of the region where the application resides.
        self.region_id = region_id
        # The start time of the query. Format: YYYY-MM-DD HH:mm:ss.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

