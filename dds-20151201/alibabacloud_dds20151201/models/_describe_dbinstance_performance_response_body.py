# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancePerformanceResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        performance_keys: main_models.DescribeDBInstancePerformanceResponseBodyPerformanceKeys = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The end of the queried time range. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # The details of performance metrics.
        self.performance_keys = performance_keys
        # The request ID.
        self.request_id = request_id
        # The beginning of the queried time range. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        if self.performance_keys:
            self.performance_keys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.performance_keys is not None:
            result['PerformanceKeys'] = self.performance_keys.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PerformanceKeys') is not None:
            temp_model = main_models.DescribeDBInstancePerformanceResponseBodyPerformanceKeys()
            self.performance_keys = temp_model.from_map(m.get('PerformanceKeys'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDBInstancePerformanceResponseBodyPerformanceKeys(DaraModel):
    def __init__(
        self,
        performance_key: List[main_models.DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKey] = None,
    ):
        self.performance_key = performance_key

    def validate(self):
        if self.performance_key:
            for v1 in self.performance_key:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PerformanceKey'] = []
        if self.performance_key is not None:
            for k1 in self.performance_key:
                result['PerformanceKey'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.performance_key = []
        if m.get('PerformanceKey') is not None:
            for k1 in m.get('PerformanceKey'):
                temp_model = main_models.DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKey()
                self.performance_key.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKey(DaraModel):
    def __init__(
        self,
        key: str = None,
        performance_values: main_models.DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValues = None,
        unit: str = None,
        value_format: str = None,
    ):
        # The performance metrics that are returned.
        self.key = key
        # The details of the performance metric values.
        self.performance_values = performance_values
        # The unit of the performance metric.
        self.unit = unit
        # The format of the performance metric value. If the performance metric contains multiple fields, the fields are separated with ampersands ( &).
        # 
        # For example, if you query disk space usage, the returned value of the **ValueFormat** parameter is **ins_size\\&data_size\\&log_size**.
        self.value_format = value_format

    def validate(self):
        if self.performance_values:
            self.performance_values.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.performance_values is not None:
            result['PerformanceValues'] = self.performance_values.to_map()

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value_format is not None:
            result['ValueFormat'] = self.value_format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('PerformanceValues') is not None:
            temp_model = main_models.DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValues()
            self.performance_values = temp_model.from_map(m.get('PerformanceValues'))

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('ValueFormat') is not None:
            self.value_format = m.get('ValueFormat')

        return self

class DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValues(DaraModel):
    def __init__(
        self,
        performance_value: List[main_models.DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValuesPerformanceValue] = None,
    ):
        self.performance_value = performance_value

    def validate(self):
        if self.performance_value:
            for v1 in self.performance_value:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PerformanceValue'] = []
        if self.performance_value is not None:
            for k1 in self.performance_value:
                result['PerformanceValue'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.performance_value = []
        if m.get('PerformanceValue') is not None:
            for k1 in m.get('PerformanceValue'):
                temp_model = main_models.DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValuesPerformanceValue()
                self.performance_value.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyPerformanceValuesPerformanceValue(DaraModel):
    def __init__(
        self,
        date: str = None,
        value: str = None,
    ):
        # The date and time when the metric value was generated.
        self.date = date
        # The value of the performance metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

