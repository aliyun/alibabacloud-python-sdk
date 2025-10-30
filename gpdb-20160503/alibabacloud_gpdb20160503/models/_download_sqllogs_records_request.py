# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DownloadSQLLogsRecordsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        end_time: str = None,
        execute_cost: str = None,
        execute_state: str = None,
        lang: str = None,
        max_execute_cost: str = None,
        min_execute_cost: str = None,
        operation_class: str = None,
        operation_type: str = None,
        page_number: int = None,
        page_size: int = None,
        query_keywords: str = None,
        source_ip: str = None,
        start_time: str = None,
        user: str = None,
    ):
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        self.database = database
        # The end of the time range to query. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format. The end time must be later than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The execution duration of the SQL statement. Unit: seconds.
        self.execute_cost = execute_cost
        # The execution status of the SQL statement.
        # 
        # *   **1**: successful.
        # *   **0**: failed.
        self.execute_state = execute_state
        # The language of the file that contains the query diagnostic information. Valid values:
        # 
        # *   **zh**: simplified Chinese.
        # *   **en**: English.
        # *   **ja**: Japanese.
        # *   **zh-tw**: traditional Chinese.
        self.lang = lang
        # The maximum amount of time consumed by a slow query. Unit: seconds. Minimum value: 0.
        self.max_execute_cost = max_execute_cost
        # The minimum amount of time consumed by a slow query. Unit: seconds. Minimum value: 0.
        self.min_execute_cost = min_execute_cost
        # The type of the query language. Example: DQL, DML, or DDL.
        self.operation_class = operation_class
        # The type of the SQL statement. Example: SELECT.
        self.operation_type = operation_type
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30**
        # *   **50**
        # *   **100**
        # 
        # Default value: **30**.
        self.page_size = page_size
        # The keywords that are used for query.
        self.query_keywords = query_keywords
        # The source IP address.
        self.source_ip = source_ip
        # The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        # 
        # This parameter is required.
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

        if self.execute_cost is not None:
            result['ExecuteCost'] = self.execute_cost

        if self.execute_state is not None:
            result['ExecuteState'] = self.execute_state

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_execute_cost is not None:
            result['MaxExecuteCost'] = self.max_execute_cost

        if self.min_execute_cost is not None:
            result['MinExecuteCost'] = self.min_execute_cost

        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_keywords is not None:
            result['QueryKeywords'] = self.query_keywords

        if self.source_ip is not None:
            result['SourceIP'] = self.source_ip

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

        if m.get('ExecuteCost') is not None:
            self.execute_cost = m.get('ExecuteCost')

        if m.get('ExecuteState') is not None:
            self.execute_state = m.get('ExecuteState')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxExecuteCost') is not None:
            self.max_execute_cost = m.get('MaxExecuteCost')

        if m.get('MinExecuteCost') is not None:
            self.min_execute_cost = m.get('MinExecuteCost')

        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')

        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

