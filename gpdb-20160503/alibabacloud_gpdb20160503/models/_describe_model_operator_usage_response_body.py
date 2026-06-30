# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeModelOperatorUsageResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        keys: List[main_models.DescribeModelOperatorUsageResponseBodyKeys] = None,
        period: int = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.keys = keys
        self.period = period
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.keys:
            for v1 in self.keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Keys'] = []
        if self.keys is not None:
            for k1 in self.keys:
                result['Keys'].append(k1.to_map() if k1 else None)

        if self.period is not None:
            result['Period'] = self.period

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.keys = []
        if m.get('Keys') is not None:
            for k1 in m.get('Keys'):
                temp_model = main_models.DescribeModelOperatorUsageResponseBodyKeys()
                self.keys.append(temp_model.from_map(k1))

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeModelOperatorUsageResponseBodyKeys(DaraModel):
    def __init__(
        self,
        name: str = None,
        series: List[main_models.DescribeModelOperatorUsageResponseBodyKeysSeries] = None,
        unit: str = None,
    ):
        self.name = name
        self.series = series
        self.unit = unit

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

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.series = []
        if m.get('Series') is not None:
            for k1 in m.get('Series'):
                temp_model = main_models.DescribeModelOperatorUsageResponseBodyKeysSeries()
                self.series.append(temp_model.from_map(k1))

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

class DescribeModelOperatorUsageResponseBodyKeysSeries(DaraModel):
    def __init__(
        self,
        api_key_id: int = None,
        name: str = None,
        role: str = None,
        values: List[main_models.DescribeModelOperatorUsageResponseBodyKeysSeriesValues] = None,
    ):
        self.api_key_id = api_key_id
        self.name = name
        self.role = role
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
        if self.api_key_id is not None:
            result['ApiKeyId'] = self.api_key_id

        if self.name is not None:
            result['Name'] = self.name

        if self.role is not None:
            result['Role'] = self.role

        result['Values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['Values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeyId') is not None:
            self.api_key_id = m.get('ApiKeyId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        self.values = []
        if m.get('Values') is not None:
            for k1 in m.get('Values'):
                temp_model = main_models.DescribeModelOperatorUsageResponseBodyKeysSeriesValues()
                self.values.append(temp_model.from_map(k1))

        return self

class DescribeModelOperatorUsageResponseBodyKeysSeriesValues(DaraModel):
    def __init__(
        self,
        point: List[str] = None,
    ):
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

