# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetBlockingDetailListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetBlockingDetailListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        # 
        # >  If the request is successful, **Successful** is returned. Otherwise, an error message such as an error code is returned.
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
            temp_model = main_models.GetBlockingDetailListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetBlockingDetailListResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.GetBlockingDetailListResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The details of the data returned.
        self.list = list
        # The page number of the page returned.
        self.page_no = page_no
        # The number of entries returned on each page.
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
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetBlockingDetailListResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetBlockingDetailListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        batch_id: int = None,
        client_app_name: str = None,
        current_collection_time: int = None,
        data_base: str = None,
        host_name: str = None,
        login_id: str = None,
        query_hash: str = None,
        spid: str = None,
        sql_text: str = None,
        start_time: str = None,
        wait_time_ms: int = None,
        wait_type: str = None,
    ):
        # The batch ID.
        self.batch_id = batch_id
        # The client name.
        self.client_app_name = client_app_name
        # The time when the blocking data was collected. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.current_collection_time = current_collection_time
        # The name of the database.
        self.data_base = data_base
        # The client hostname.
        self.host_name = host_name
        # The username that is used for the logon.
        self.login_id = login_id
        # The hash value of the SQL statement.
        self.query_hash = query_hash
        # The session ID.
        self.spid = spid
        # The SQL statement.
        self.sql_text = sql_text
        # The time when the execution started. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The duration of the blocking. Unit: milliseconds.
        self.wait_time_ms = wait_time_ms
        # The wait type. For more information about wait types, see [sys.dm_os_wait_stats (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-os-wait-stats-transact-sql?view=sql-server-ver15).
        self.wait_type = wait_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.client_app_name is not None:
            result['ClientAppName'] = self.client_app_name

        if self.current_collection_time is not None:
            result['CurrentCollectionTime'] = self.current_collection_time

        if self.data_base is not None:
            result['DataBase'] = self.data_base

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.login_id is not None:
            result['LoginId'] = self.login_id

        if self.query_hash is not None:
            result['QueryHash'] = self.query_hash

        if self.spid is not None:
            result['Spid'] = self.spid

        if self.sql_text is not None:
            result['SqlText'] = self.sql_text

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.wait_time_ms is not None:
            result['WaitTimeMs'] = self.wait_time_ms

        if self.wait_type is not None:
            result['WaitType'] = self.wait_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('ClientAppName') is not None:
            self.client_app_name = m.get('ClientAppName')

        if m.get('CurrentCollectionTime') is not None:
            self.current_collection_time = m.get('CurrentCollectionTime')

        if m.get('DataBase') is not None:
            self.data_base = m.get('DataBase')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('LoginId') is not None:
            self.login_id = m.get('LoginId')

        if m.get('QueryHash') is not None:
            self.query_hash = m.get('QueryHash')

        if m.get('Spid') is not None:
            self.spid = m.get('Spid')

        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WaitTimeMs') is not None:
            self.wait_time_ms = m.get('WaitTimeMs')

        if m.get('WaitType') is not None:
            self.wait_type = m.get('WaitType')

        return self

