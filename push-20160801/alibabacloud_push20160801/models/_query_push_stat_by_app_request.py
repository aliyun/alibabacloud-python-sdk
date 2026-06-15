# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryPushStatByAppRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        end_time: str = None,
        granularity: str = None,
        start_time: str = None,
    ):
        # The AppKey value.
        # 
        # This parameter is required.
        self.app_key = app_key
        # The end time of the query. Specify the time in ISO 8601 format, YYYY-MM-DDThh:mm:ssZ.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The data granularity of the response. You can only query data for up to 31 days at daily granularity. Valid values:
        # 
        # - **DAY**: Query data at daily granularity.
        # 
        # This parameter is required.
        self.granularity = granularity
        # The start time of the query. Specify the time in ISO 8601 format, YYYY-MM-DDThh:mm:ssZ.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

