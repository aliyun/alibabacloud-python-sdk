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
        # The returned status code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        # 
        # > If the request is successful, **Successful** is returned. If the request fails, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # * true: The request is successful.
        # * false: The request fails.
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
        # The total cold storage data. Unit: bytes.
        self.cold_sql_size = cold_sql_size
        # The free cold storage data. Unit: bytes.
        self.free_cold_sql_size = free_cold_sql_size
        # The free hot storage data. Unit: bytes.
        self.free_hot_sql_size = free_hot_sql_size
        # The total hot storage data. Unit: bytes.
        self.hot_sql_size = hot_sql_size
        # The amount of data imported in the last day. Unit: bytes.
        self.import_sql_size = import_sql_size
        # The timestamp in UNIX timestamp format. Unit: milliseconds.
        self.timestamp = timestamp
        # The total storage data (cold data + hot data).
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

