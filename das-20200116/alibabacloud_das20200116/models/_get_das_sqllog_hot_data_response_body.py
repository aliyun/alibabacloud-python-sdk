# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetDasSQLLogHotDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDasSQLLogHotDataResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        # 
        # > If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
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
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.GetDasSQLLogHotDataResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDasSQLLogHotDataResponseBodyData(DaraModel):
    def __init__(
        self,
        extra: Any = None,
        list: List[main_models.GetDasSQLLogHotDataResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The reserved parameter.
        self.extra = extra
        # The details of the data returned.
        self.list = list
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['Extra'] = self.extra

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetDasSQLLogHotDataResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetDasSQLLogHotDataResponseBodyDataList(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        dbname: str = None,
        execute_time: str = None,
        ext: str = None,
        host_address: str = None,
        latancy: int = None,
        lock_time: int = None,
        logic_read: int = None,
        node_id: str = None,
        origin_time: str = None,
        physic_async_read: int = None,
        physic_sync_read: int = None,
        return_rows: int = None,
        sqltext: str = None,
        scan_rows: int = None,
        sql_type: str = None,
        state: str = None,
        thread_id: int = None,
        transaction_id: str = None,
        update_rows: int = None,
    ):
        # The account of the database.
        self.account_name = account_name
        # The name of the database.
        self.dbname = dbname
        # The execution time. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.execute_time = execute_time
        # The extended information. This parameter is a reserved parameter.
        self.ext = ext
        # The IP address of the client.
        self.host_address = host_address
        # The execution duration. Unit: microseconds.
        self.latancy = latancy
        # The lock wait duration. Unit: microseconds.
        self.lock_time = lock_time
        # The number of logical reads.
        self.logic_read = logic_read
        self.node_id = node_id
        # The execution time. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.origin_time = origin_time
        # The number of physical asynchronous reads.
        self.physic_async_read = physic_async_read
        # The number of physical synchronous reads.
        self.physic_sync_read = physic_sync_read
        # The number of rows returned.
        self.return_rows = return_rows
        # The content of the SQL statement.
        self.sqltext = sqltext
        # The number of rows scanned by the SQL statement.
        self.scan_rows = scan_rows
        # The type of the SQL statement. Valid values:
        # 
        # * **SELECT**
        # * **UPDATE**
        # * **DELETE**
        self.sql_type = sql_type
        # The execution result. If a **0** is returned, the SQL statement was successfully executed. If an error code is returned, the SQL statement failed to be executed.
        self.state = state
        # The thread ID.
        self.thread_id = thread_id
        # The transaction ID.
        self.transaction_id = transaction_id
        # The number of updated rows.
        self.update_rows = update_rows

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time

        if self.ext is not None:
            result['Ext'] = self.ext

        if self.host_address is not None:
            result['HostAddress'] = self.host_address

        if self.latancy is not None:
            result['Latancy'] = self.latancy

        if self.lock_time is not None:
            result['LockTime'] = self.lock_time

        if self.logic_read is not None:
            result['LogicRead'] = self.logic_read

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.origin_time is not None:
            result['OriginTime'] = self.origin_time

        if self.physic_async_read is not None:
            result['PhysicAsyncRead'] = self.physic_async_read

        if self.physic_sync_read is not None:
            result['PhysicSyncRead'] = self.physic_sync_read

        if self.return_rows is not None:
            result['ReturnRows'] = self.return_rows

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.state is not None:
            result['State'] = self.state

        if self.thread_id is not None:
            result['ThreadID'] = self.thread_id

        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id

        if self.update_rows is not None:
            result['UpdateRows'] = self.update_rows

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')

        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')

        if m.get('Latancy') is not None:
            self.latancy = m.get('Latancy')

        if m.get('LockTime') is not None:
            self.lock_time = m.get('LockTime')

        if m.get('LogicRead') is not None:
            self.logic_read = m.get('LogicRead')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OriginTime') is not None:
            self.origin_time = m.get('OriginTime')

        if m.get('PhysicAsyncRead') is not None:
            self.physic_async_read = m.get('PhysicAsyncRead')

        if m.get('PhysicSyncRead') is not None:
            self.physic_sync_read = m.get('PhysicSyncRead')

        if m.get('ReturnRows') is not None:
            self.return_rows = m.get('ReturnRows')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('ThreadID') is not None:
            self.thread_id = m.get('ThreadID')

        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')

        if m.get('UpdateRows') is not None:
            self.update_rows = m.get('UpdateRows')

        return self

