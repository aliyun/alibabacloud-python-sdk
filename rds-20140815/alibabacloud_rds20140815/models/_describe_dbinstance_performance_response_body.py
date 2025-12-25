# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancePerformanceResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        engine: str = None,
        performance_keys: main_models.DescribeDBInstancePerformanceResponseBodyPerformanceKeys = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The end time of the query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.end_time = end_time
        # The database engine of the instance.
        self.engine = engine
        # Details of the performance metrics.
        self.performance_keys = performance_keys
        # The request ID.
        self.request_id = request_id
        # The start time of the query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        if self.performance_keys:
            self.performance_keys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.performance_keys is not None:
            result['PerformanceKeys'] = self.performance_keys.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

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
        unit: str = None,
        value_format: str = None,
        values: main_models.DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyValues = None,
    ):
        # The name of the performance metric.
        self.key = key
        # The unit of the performance metrics.
        self.unit = unit
        # The format in which the value of the performance metric is returned.
        # 
        # >  If a performance metric value consists of multiple fields, the values are separated with ampersands (&). Example: com_delete\\&com_insert\\&com_insert_select\\&com_replace.
        self.value_format = value_format
        # The performance metric values.
        self.values = values

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value_format is not None:
            result['ValueFormat'] = self.value_format

        if self.values is not None:
            result['Values'] = self.values.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('ValueFormat') is not None:
            self.value_format = m.get('ValueFormat')

        if m.get('Values') is not None:
            temp_model = main_models.DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyValues()
            self.values = temp_model.from_map(m.get('Values'))

        return self

class DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyValues(DaraModel):
    def __init__(
        self,
        performance_value: List[main_models.DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyValuesPerformanceValue] = None,
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
                temp_model = main_models.DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyValuesPerformanceValue()
                self.performance_value.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancePerformanceResponseBodyPerformanceKeysPerformanceKeyValuesPerformanceValue(DaraModel):
    def __init__(
        self,
        date: str = None,
        value: str = None,
    ):
        # The date and time when the value of the performance metric was recorded. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
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

