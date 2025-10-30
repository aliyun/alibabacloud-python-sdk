# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDiagnosisMonitorPerformanceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        end_time: str = None,
        query_condition: str = None,
        start_time: str = None,
        user: str = None,
    ):
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        # 
        # This parameter is required.
        self.database = database
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time
        # The filter condition on queries. Specify the value in the JSON format. Valid values:
        # 
        # *   `{"Type":"maxCost", "Value":"100"}`: filters the top 100 queries that are the most time-consuming.
        # 
        # *   `{"Type":"status","Value":"finished"}`: filters completed queries.
        # 
        # *   `{"Type":"status","Value":"running"}`: filters running queries.
        # 
        # *   `{"Type":"cost","Min":"30","Max":"50"}`: filters the queries that consume 30 milliseconds or more and less than 50 milliseconds. You can customize a filter condition by setting **Min** and **Max**.
        # 
        #     *   If only **Min** is specified, the queries that consume a period of time that is greater than or equal to the Min value are filtered.
        #     *   If only **Max** is specified, the queries that consume a period of time that is less than the Max value are filtered.
        #     *   If both **Min** and **Max** are specified, the queries that consume a period of time that is greater than or equal to the **Min** value and less than the **Max** value are filtered.
        self.query_condition = query_condition
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
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

        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition

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

        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

