# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBProxyPerformanceResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbproxy_engine_type: str = None,
        end_time: str = None,
        performance_keys: main_models.DescribeDBProxyPerformanceResponseBodyPerformanceKeys = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # An internal parameter. You do not need to specify this parameter.
        self.dbproxy_engine_type = dbproxy_engine_type
        # The end time of the query.
        self.end_time = end_time
        # The performance list.
        self.performance_keys = performance_keys
        # The request ID.
        self.request_id = request_id
        # The start time of the query.
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

        if self.dbproxy_engine_type is not None:
            result['DBProxyEngineType'] = self.dbproxy_engine_type

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
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBProxyEngineType') is not None:
            self.dbproxy_engine_type = m.get('DBProxyEngineType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PerformanceKeys') is not None:
            temp_model = main_models.DescribeDBProxyPerformanceResponseBodyPerformanceKeys()
            self.performance_keys = temp_model.from_map(m.get('PerformanceKeys'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDBProxyPerformanceResponseBodyPerformanceKeys(DaraModel):
    def __init__(
        self,
        performance_key: List[main_models.DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceKey] = None,
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
                temp_model = main_models.DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceKey()
                self.performance_key.append(temp_model.from_map(k1))

        return self

class DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceKey(DaraModel):
    def __init__(
        self,
        key: str = None,
        node: str = None,
        server: str = None,
        service: str = None,
        value_format: str = None,
        values: main_models.DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceKeyValues = None,
    ):
        # The performance parameter.
        self.key = key
        self.node = node
        self.server = server
        # The service dimension.
        self.service = service
        # The format in which the value of the performance metric is returned.
        self.value_format = value_format
        # The performance metrics.
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

        if self.node is not None:
            result['Node'] = self.node

        if self.server is not None:
            result['Server'] = self.server

        if self.service is not None:
            result['Service'] = self.service

        if self.value_format is not None:
            result['ValueFormat'] = self.value_format

        if self.values is not None:
            result['Values'] = self.values.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Node') is not None:
            self.node = m.get('Node')

        if m.get('Server') is not None:
            self.server = m.get('Server')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('ValueFormat') is not None:
            self.value_format = m.get('ValueFormat')

        if m.get('Values') is not None:
            temp_model = main_models.DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceKeyValues()
            self.values = temp_model.from_map(m.get('Values'))

        return self

class DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceKeyValues(DaraModel):
    def __init__(
        self,
        performance_value: List[main_models.DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceKeyValuesPerformanceValue] = None,
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
                temp_model = main_models.DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceKeyValuesPerformanceValue()
                self.performance_value.append(temp_model.from_map(k1))

        return self

class DescribeDBProxyPerformanceResponseBodyPerformanceKeysPerformanceKeyValuesPerformanceValue(DaraModel):
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

