# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeActiveSQLRecordsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        end_time: str = None,
        keyword: str = None,
        max_duration: str = None,
        min_duration: str = None,
        order: str = None,
        start_time: str = None,
        user: str = None,
    ):
        # The instance ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.database = database
        # The end of the time range to query. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The end time must be later than the start time.
        self.end_time = end_time
        # The keyword used to filter queries.
        self.keyword = keyword
        # The maxmum amount of time consumed by traces. Unit: milliseconds.
        self.max_duration = max_duration
        # The minimum amount of time consumed by traces. Unit: milliseconds.
        self.min_duration = min_duration
        # The field used to sort lock diagnostics records and the sorting order.
        # 
        # Default value: `{"Field":"StartTime","Type":"Desc"}`, which indicates that lock diagnostics records are sorted by the start time in descending order. No other values are supported.
        self.order = order
        # The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        self.start_time = start_time
        # The name of the database account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.database is not None:
            result['Database'] = self.database

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.max_duration is not None:
            result['MaxDuration'] = self.max_duration

        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration

        if self.order is not None:
            result['Order'] = self.order

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MaxDuration') is not None:
            self.max_duration = m.get('MaxDuration')

        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

