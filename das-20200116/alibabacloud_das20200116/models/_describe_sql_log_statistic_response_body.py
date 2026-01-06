# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeSqlLogStatisticResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeSqlLogStatisticResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The response code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.DescribeSqlLogStatisticResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSqlLogStatisticResponseBodyData(DaraModel):
    def __init__(
        self,
        cold_sql_size: int = None,
        free_cold_sql_size: int = None,
        free_hot_sql_size: int = None,
        hot_sql_size: int = None,
        import_sql_size: int = None,
        timestamp: int = None,
        total_sql_size: int = None,
    ):
        # The size of the SQL Explorer and Audit data that is stored in cold storage. Unit: bytes.
        self.cold_sql_size = cold_sql_size
        # The free quota for cold data storage. Unit: bytes.
        self.free_cold_sql_size = free_cold_sql_size
        # The free quota for hot data storage. Unit: bytes.
        self.free_hot_sql_size = free_hot_sql_size
        # The size of the SQL Explorer and Audit data that is stored in hot storage. Unit: bytes.
        self.hot_sql_size = hot_sql_size
        # The size of the SQL Explorer and Audit data that was generated in the most recent day. Unit: bytes.
        self.import_sql_size = import_sql_size
        # The timestamp. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp
        self.total_sql_size = total_sql_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cold_sql_size is not None:
            result['ColdSqlSize'] = self.cold_sql_size

        if self.free_cold_sql_size is not None:
            result['FreeColdSqlSize'] = self.free_cold_sql_size

        if self.free_hot_sql_size is not None:
            result['FreeHotSqlSize'] = self.free_hot_sql_size

        if self.hot_sql_size is not None:
            result['HotSqlSize'] = self.hot_sql_size

        if self.import_sql_size is not None:
            result['ImportSqlSize'] = self.import_sql_size

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.total_sql_size is not None:
            result['TotalSqlSize'] = self.total_sql_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColdSqlSize') is not None:
            self.cold_sql_size = m.get('ColdSqlSize')

        if m.get('FreeColdSqlSize') is not None:
            self.free_cold_sql_size = m.get('FreeColdSqlSize')

        if m.get('FreeHotSqlSize') is not None:
            self.free_hot_sql_size = m.get('FreeHotSqlSize')

        if m.get('HotSqlSize') is not None:
            self.hot_sql_size = m.get('HotSqlSize')

        if m.get('ImportSqlSize') is not None:
            self.import_sql_size = m.get('ImportSqlSize')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('TotalSqlSize') is not None:
            self.total_sql_size = m.get('TotalSqlSize')

        return self

