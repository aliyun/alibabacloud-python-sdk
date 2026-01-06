# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetFullRequestSampleByInstanceIdResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.GetFullRequestSampleByInstanceIdResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message that contains information such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetFullRequestSampleByInstanceIdResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetFullRequestSampleByInstanceIdResponseBodyData(DaraModel):
    def __init__(
        self,
        database: str = None,
        frows: int = None,
        lock_wait_time: float = None,
        logical_read: float = None,
        origin_host: str = None,
        physical_async_read: float = None,
        physical_sync_read: float = None,
        rows: int = None,
        rows_examined: int = None,
        rows_returned: int = None,
        rt: float = None,
        scan_rows: int = None,
        scnt: int = None,
        sql: str = None,
        sql_id: str = None,
        sql_type: str = None,
        timestamp: int = None,
        update_rows: int = None,
        user: str = None,
    ):
        # The name of the database.
        self.database = database
        # The number of rows fetched by PolarDB-X 2.0 compute nodes.
        self.frows = frows
        # The lock wait duration. Unit: seconds.
        self.lock_wait_time = lock_wait_time
        # The number of logical reads.
        self.logical_read = logical_read
        # The source IP address.
        self.origin_host = origin_host
        # The number of physical asynchronous reads.
        self.physical_async_read = physical_async_read
        # The number of physical synchronous reads.
        self.physical_sync_read = physical_sync_read
        # The number of rows updated or returned on PolarDB-X 2.0 compute nodes.
        self.rows = rows
        # The total number of scanned rows.
        # 
        # > This parameter is returned only for ApsaraDB RDS for MySQL, ApsaraDB RDS for PostgreSQL, and PolarDB for MySQL databases.
        self.rows_examined = rows_examined
        # The number of rows returned by the SQL statement.
        self.rows_returned = rows_returned
        # The amount of time consumed to execute the SQL statement. Unit: seconds.
        self.rt = rt
        # The number of scanned rows.
        self.scan_rows = scan_rows
        # The number of requests sent from PolarDB-X 2.0 compute nodes to data nodes.
        self.scnt = scnt
        # The sample SQL statement.
        self.sql = sql
        # The SQL statement ID.
        self.sql_id = sql_id
        # The type of the SQL statement. Valid values: **SELECT**, **INSERT**, **UPDATE**, **DELETE**, **LOGIN**, **LOGOUT**, **MERGE**, **ALTER**, **CREATEINDEX**, **DROPINDEX**, **CREATE**, **DROP**, **SET**, **DESC**, **REPLACE**, **CALL**, **BEGIN**, **DESCRIBE**, **ROLLBACK**, **FLUSH**, **USE**, **SHOW**, **START**, **COMMIT**, and **RENAME**.
        self.sql_type = sql_type
        # The time when the SQL statement was executed. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp
        # The number of updated rows.
        self.update_rows = update_rows
        # The name of the user who executes the SQL statement.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database is not None:
            result['Database'] = self.database

        if self.frows is not None:
            result['Frows'] = self.frows

        if self.lock_wait_time is not None:
            result['LockWaitTime'] = self.lock_wait_time

        if self.logical_read is not None:
            result['LogicalRead'] = self.logical_read

        if self.origin_host is not None:
            result['OriginHost'] = self.origin_host

        if self.physical_async_read is not None:
            result['PhysicalAsyncRead'] = self.physical_async_read

        if self.physical_sync_read is not None:
            result['PhysicalSyncRead'] = self.physical_sync_read

        if self.rows is not None:
            result['Rows'] = self.rows

        if self.rows_examined is not None:
            result['RowsExamined'] = self.rows_examined

        if self.rows_returned is not None:
            result['RowsReturned'] = self.rows_returned

        if self.rt is not None:
            result['Rt'] = self.rt

        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows

        if self.scnt is not None:
            result['Scnt'] = self.scnt

        if self.sql is not None:
            result['Sql'] = self.sql

        if self.sql_id is not None:
            result['SqlId'] = self.sql_id

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.update_rows is not None:
            result['UpdateRows'] = self.update_rows

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Frows') is not None:
            self.frows = m.get('Frows')

        if m.get('LockWaitTime') is not None:
            self.lock_wait_time = m.get('LockWaitTime')

        if m.get('LogicalRead') is not None:
            self.logical_read = m.get('LogicalRead')

        if m.get('OriginHost') is not None:
            self.origin_host = m.get('OriginHost')

        if m.get('PhysicalAsyncRead') is not None:
            self.physical_async_read = m.get('PhysicalAsyncRead')

        if m.get('PhysicalSyncRead') is not None:
            self.physical_sync_read = m.get('PhysicalSyncRead')

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        if m.get('RowsExamined') is not None:
            self.rows_examined = m.get('RowsExamined')

        if m.get('RowsReturned') is not None:
            self.rows_returned = m.get('RowsReturned')

        if m.get('Rt') is not None:
            self.rt = m.get('Rt')

        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')

        if m.get('Scnt') is not None:
            self.scnt = m.get('Scnt')

        if m.get('Sql') is not None:
            self.sql = m.get('Sql')

        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('UpdateRows') is not None:
            self.update_rows = m.get('UpdateRows')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

