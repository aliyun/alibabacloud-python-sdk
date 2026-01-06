# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class EventCenterQueryEventsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.EventCenterQueryEventsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.EventCenterQueryEventsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class EventCenterQueryEventsResponseBodyData(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        table: List[main_models.EventCenterQueryEventsResponseBodyDataTable] = None,
        time_series: List[main_models.EventCenterQueryEventsResponseBodyDataTimeSeries] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.table = table
        self.time_series = time_series
        self.total_count = total_count

    def validate(self):
        if self.table:
            for v1 in self.table:
                 if v1:
                    v1.validate()
        if self.time_series:
            for v1 in self.time_series:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Table'] = []
        if self.table is not None:
            for k1 in self.table:
                result['Table'].append(k1.to_map() if k1 else None)

        result['TimeSeries'] = []
        if self.time_series is not None:
            for k1 in self.time_series:
                result['TimeSeries'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.table = []
        if m.get('Table') is not None:
            for k1 in m.get('Table'):
                temp_model = main_models.EventCenterQueryEventsResponseBodyDataTable()
                self.table.append(temp_model.from_map(k1))

        self.time_series = []
        if m.get('TimeSeries') is not None:
            for k1 in m.get('TimeSeries'):
                temp_model = main_models.EventCenterQueryEventsResponseBodyDataTimeSeries()
                self.time_series.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class EventCenterQueryEventsResponseBodyDataTimeSeries(DaraModel):
    def __init__(
        self,
        row_data: Dict[str, Any] = None,
        time: str = None,
    ):
        self.row_data = row_data
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.row_data is not None:
            result['RowData'] = self.row_data

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RowData') is not None:
            self.row_data = m.get('RowData')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

class EventCenterQueryEventsResponseBodyDataTable(DaraModel):
    def __init__(
        self,
        row_data: Dict[str, Any] = None,
    ):
        self.row_data = row_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.row_data is not None:
            result['RowData'] = self.row_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RowData') is not None:
            self.row_data = m.get('RowData')

        return self

