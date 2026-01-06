# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeAuditLogRecordsResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        items: List[main_models.DescribeAuditLogRecordsResponseBodyItems] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        self.dbcluster_id = dbcluster_id
        # The queried SQL audit logs.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeAuditLogRecordsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAuditLogRecordsResponseBodyItems(DaraModel):
    def __init__(
        self,
        conn_id: str = None,
        dbname: str = None,
        execute_time: str = None,
        execute_timestamp: int = None,
        has_diagnostic_info: bool = None,
        host_address: str = None,
        process_id: str = None,
        sqltext: str = None,
        sqltype: str = None,
        succeed: str = None,
        total_time: str = None,
        user: str = None,
    ):
        # The connection ID.
        self.conn_id = conn_id
        # The name of the database on which the SQL statement was executed.
        self.dbname = dbname
        # The start time of the execution of the SQL statement. The time is displayed in the ISO 8601 standard in the yyyy-MM-dd HH:mm:ss format. The time must be in UTC.
        self.execute_time = execute_time
        self.execute_timestamp = execute_timestamp
        self.has_diagnostic_info = has_diagnostic_info
        # The IP address and port number of the client that is used to execute the SQL statement.
        self.host_address = host_address
        # The task ID.
        self.process_id = process_id
        # The SQL statement.
        self.sqltext = sqltext
        # The type of the SQL statement.
        self.sqltype = sqltype
        # Indicates whether the SQL statement was successfully executed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.succeed = succeed
        # The amount of time that is consumed to execute the SQL statement. Unit: milliseconds.
        self.total_time = total_time
        # The username that is used to execute the SQL statement.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conn_id is not None:
            result['ConnId'] = self.conn_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time

        if self.execute_timestamp is not None:
            result['ExecuteTimestamp'] = self.execute_timestamp

        if self.has_diagnostic_info is not None:
            result['HasDiagnosticInfo'] = self.has_diagnostic_info

        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.process_id is not None:
            result['ProcessID'] = self.process_id

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        if self.sqltype is not None:
            result['SQLType'] = self.sqltype

        if self.succeed is not None:
            result['Succeed'] = self.succeed

        if self.total_time is not None:
            result['TotalTime'] = self.total_time

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnId') is not None:
            self.conn_id = m.get('ConnId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')

        if m.get('ExecuteTimestamp') is not None:
            self.execute_timestamp = m.get('ExecuteTimestamp')

        if m.get('HasDiagnosticInfo') is not None:
            self.has_diagnostic_info = m.get('HasDiagnosticInfo')

        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('ProcessID') is not None:
            self.process_id = m.get('ProcessID')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')

        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')

        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

