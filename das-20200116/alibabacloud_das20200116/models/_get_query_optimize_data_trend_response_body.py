# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetQueryOptimizeDataTrendResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetQueryOptimizeDataTrendResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The detailed information.
        self.data = data
        # The returned message.
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
            temp_model = main_models.GetQueryOptimizeDataTrendResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQueryOptimizeDataTrendResponseBodyData(DaraModel):
    def __init__(
        self,
        extra: str = None,
        list: List[main_models.GetQueryOptimizeDataTrendResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The reserved parameter.
        self.extra = extra
        # The details of the trend data.
        self.list = list
        # The reserved parameter.
        self.page_no = page_no
        # The reserved parameter.
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
                temp_model = main_models.GetQueryOptimizeDataTrendResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetQueryOptimizeDataTrendResponseBodyDataList(DaraModel):
    def __init__(
        self,
        kpi: str = None,
        timestamp: int = None,
        value: float = None,
    ):
        # The name of the metric. Valid values:
        # 
        # * **sqlExecuteCount**: the number of executions of slow SQL queries.
        # * **sqlExecuteCountDiff**: the difference in the number of executions of slow SQL queries compared to the previous day.
        # * **sqlCount**: the number of slow SQL templates.
        # * **sqlCountDiff**: the difference in the number of slow SQL templates compared to the previous day.
        # * **optimizedSqlExecuteCount**: the number of optimizable executions of slow SQL queries.
        # * **optimizedSqlExecuteCountDiff**: the difference in the number of optimizable executions of slow SQL queries compared to the previous day.
        # * **optimizedSqlCount**: the number of optimizable slow SQL templates.
        # * **optimizedSqlCountDiff**: the difference in the number of optimizable slow SQL templates compared to the previous day.
        self.kpi = kpi
        # The data timestamp. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.timestamp = timestamp
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kpi is not None:
            result['Kpi'] = self.kpi

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Kpi') is not None:
            self.kpi = m.get('Kpi')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

