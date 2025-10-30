# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceSupportMaxPerformanceResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        performances: main_models.DescribeDBInstanceSupportMaxPerformanceResponseBodyPerformances = None,
        request_id: str = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The queried performance metric.
        self.performances = performances
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.performances:
            self.performances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.performances is not None:
            result['Performances'] = self.performances.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Performances') is not None:
            temp_model = main_models.DescribeDBInstanceSupportMaxPerformanceResponseBodyPerformances()
            self.performances = temp_model.from_map(m.get('Performances'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceSupportMaxPerformanceResponseBodyPerformances(DaraModel):
    def __init__(
        self,
        performance: List[main_models.DescribeDBInstanceSupportMaxPerformanceResponseBodyPerformancesPerformance] = None,
    ):
        self.performance = performance

    def validate(self):
        if self.performance:
            for v1 in self.performance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Performance'] = []
        if self.performance is not None:
            for k1 in self.performance:
                result['Performance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.performance = []
        if m.get('Performance') is not None:
            for k1 in m.get('Performance'):
                temp_model = main_models.DescribeDBInstanceSupportMaxPerformanceResponseBodyPerformancesPerformance()
                self.performance.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceSupportMaxPerformanceResponseBodyPerformancesPerformance(DaraModel):
    def __init__(
        self,
        bottleneck: str = None,
        key: str = None,
        unit: str = None,
        value: str = None,
    ):
        # The performance bottleneck type.
        self.bottleneck = bottleneck
        # The name of the performance metric.
        self.key = key
        # The unit of the performance metric.
        self.unit = unit
        # The value of the performance metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bottleneck is not None:
            result['Bottleneck'] = self.bottleneck

        if self.key is not None:
            result['Key'] = self.key

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bottleneck') is not None:
            self.bottleneck = m.get('Bottleneck')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

