# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSQLLogCountRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        database: str = None,
        end_time: str = None,
        execute_cost: str = None,
        execute_state: str = None,
        max_execute_cost: str = None,
        min_execute_cost: str = None,
        operation_class: str = None,
        operation_type: str = None,
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
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        # 
        # > The end time must be later than the start time. The maximum time range that can be specified is seven days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The execution duration of the SQL statement. Unit: seconds.
        self.execute_cost = execute_cost
        # The execution status of the query. Valid values:
        # 
        # *   1: successful.
        # *   0: failed.
        # *   0,1 or 1,0: all.
        self.execute_state = execute_state
        # The maximum amount of time consumed by a slow query. Unit: seconds. Minimum value: 0.
        self.max_execute_cost = max_execute_cost
        # The minimum amount of time consumed by a slow query. Unit: seconds. Minimum value: 0.
        self.min_execute_cost = min_execute_cost
        # The type of the query language. Valid values:
        # 
        # *   **DQL**
        # *   **DML**
        # *   **DDL**
        # *   **DCL**
        # *   **TCL**
        self.operation_class = operation_class
        # The type of the SQL statement.
        # 
        # > 
        # 
        # *   If you specify **OperationClass**, the value of **OperationType** must be of the corresponding query language. For example, if you set **OperationClass** to **DQL**, the value of **OperationType** must be a **DQL** statement such as **SELECT**.
        # 
        # *   If you leave **OperationClass** empty, the value of **OperationType** can be an SQL statement of any query language.
        # 
        # *   If you leave **OperationClass** and **OperationType** empty, all types of SQL statements are returned.
        self.operation_type = operation_type
        # The keywords that are used to query audit logs.
        self.query_keywords = query_keywords
        # The source IP address.
        self.source_ip = source_ip
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The name of the database account that is used to connect to the database.
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

        if self.max_execute_cost is not None:
            result['MaxExecuteCost'] = self.max_execute_cost

        if self.min_execute_cost is not None:
            result['MinExecuteCost'] = self.min_execute_cost

        if self.operation_class is not None:
            result['OperationClass'] = self.operation_class

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

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

        if m.get('MaxExecuteCost') is not None:
            self.max_execute_cost = m.get('MaxExecuteCost')

        if m.get('MinExecuteCost') is not None:
            self.min_execute_cost = m.get('MinExecuteCost')

        if m.get('OperationClass') is not None:
            self.operation_class = m.get('OperationClass')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('QueryKeywords') is not None:
            self.query_keywords = m.get('QueryKeywords')

        if m.get('SourceIP') is not None:
            self.source_ip = m.get('SourceIP')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

