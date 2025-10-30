# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeSQLLogCountResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        items: List[main_models.DescribeSQLLogCountResponseBodyItems] = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The instance ID.
        self.dbcluster_id = dbcluster_id
        # The end time of the query.
        self.end_time = end_time
        # The name of the instance.
        self.items = items
        # The request ID.
        self.request_id = request_id
        # The start time of the query.
        self.start_time = start_time

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

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeSQLLogCountResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeSQLLogCountResponseBodyItems(DaraModel):
    def __init__(
        self,
        name: str = None,
        series: List[main_models.DescribeSQLLogCountResponseBodyItemsSeries] = None,
    ):
        # The name of the table.
        self.name = name
        # Details of the audit logs.
        self.series = series

    def validate(self):
        if self.series:
            for v1 in self.series:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        result['Series'] = []
        if self.series is not None:
            for k1 in self.series:
                result['Series'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.series = []
        if m.get('Series') is not None:
            for k1 in m.get('Series'):
                temp_model = main_models.DescribeSQLLogCountResponseBodyItemsSeries()
                self.series.append(temp_model.from_map(k1))

        return self

class DescribeSQLLogCountResponseBodyItemsSeries(DaraModel):
    def __init__(
        self,
        values: List[main_models.DescribeSQLLogCountResponseBodyItemsSeriesValues] = None,
    ):
        # Details of the audit logs.
        self.values = values

    def validate(self):
        if self.values:
            for v1 in self.values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['Values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.values = []
        if m.get('Values') is not None:
            for k1 in m.get('Values'):
                temp_model = main_models.DescribeSQLLogCountResponseBodyItemsSeriesValues()
                self.values.append(temp_model.from_map(k1))

        return self

class DescribeSQLLogCountResponseBodyItemsSeriesValues(DaraModel):
    def __init__(
        self,
        point: List[str] = None,
    ):
        # The time when the audit logs were generated and the number of the audit logs.
        self.point = point

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.point is not None:
            result['Point'] = self.point

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Point') is not None:
            self.point = m.get('Point')

        return self

