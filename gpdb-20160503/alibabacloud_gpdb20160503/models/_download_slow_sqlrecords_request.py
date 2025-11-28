# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DownloadSlowSQLRecordsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbname: str = None,
        end_time: str = None,
        keyword: str = None,
        max_duration: str = None,
        min_duration: str = None,
        order_by: str = None,
        region_id: str = None,
        start_time: str = None,
        user_name: str = None,
    ):
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The database name.
        self.dbname = dbname
        # The end of the time range to query. The time must be in UTC and formatted as *yyyy-MM-dd*T*HH:mm*Z. The time must be in UTC. The end time must be later than the start time.
        # 
        # Defaults to the current time
        self.end_time = end_time
        # The search keyword.
        self.keyword = keyword
        # The longest execution duration. Unit: seconds.
        self.max_duration = max_duration
        # The minimum execution duration. Unit: seconds.
        self.min_duration = min_duration
        # Sort criteria.
        self.order_by = order_by
        # The region ID of the instance.
        self.region_id = region_id
        # The beginning of the time range to query. The time must be in UTC and formatted as *yyyy-MM-dd*T*HH:mm*Z.
        # 
        # Defaults to the current time minus 5 minutes.
        self.start_time = start_time
        # The database account.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.max_duration is not None:
            result['MaxDuration'] = self.max_duration

        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('MaxDuration') is not None:
            self.max_duration = m.get('MaxDuration')

        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

