# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryEventHouseWithTimeRangeRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        limit: int = None,
        query: str = None,
    ):
        # The start time for querying internal EventHouse data. Specify a UNIX timestamp in seconds. The time range includes this point in time.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The end time for querying internal EventHouse data. Specify a UNIX timestamp in seconds. The time range excludes this point in time. The value must be greater than BeginTime.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The maximum number of result rows that can be returned for this query.
        self.limit = limit
        # The single read-only SQL statement to execute. You can query internal EventHouse data or perform federated queries with mounted external data sources.
        # 
        # This parameter is required.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

