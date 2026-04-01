# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceMetricsResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        items: List[main_models.DescribeDBInstanceMetricsResponseBodyItems] = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The instance ID.
        self.dbinstance_name = dbinstance_name
        # An array consisting of the Enhanced Monitoring metrics that are enabled for the instance.
        self.items = items
        # The ID of the request.
        self.request_id = request_id
        # The total number of enhanced monitoring metrics that are enabled for the instance.
        self.total_record_count = total_record_count

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
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDBInstanceMetricsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeDBInstanceMetricsResponseBodyItems(DaraModel):
    def __init__(
        self,
        description: str = None,
        dimension: str = None,
        group_key: str = None,
        group_key_type: str = None,
        method: str = None,
        metrics_key: str = None,
        metrics_key_alias: str = None,
        sort_rule: int = None,
        unit: str = None,
    ):
        # The description of the enhanced monitoring metric.
        self.description = description
        # The category of the enhanced monitoring metric. Valid values:
        # 
        # *   **os**: OS metric
        # *   **db**: database metric
        self.dimension = dimension
        # The key of the group to which the enhanced monitoring metric belongs.
        self.group_key = group_key
        # The name of the group to which the enhanced monitoring metric belongs.
        self.group_key_type = group_key_type
        # The method that is used to aggregate the monitoring data of the enhanced monitoring metric. Valid values:
        # 
        # *   **avg**: The system calculates the average value of the enhanced monitoring metric.
        # *   **min**: The system calculates the minimum value of the enhanced monitoring metric.
        # *   **max**: The system calculates the maximum value of the enhanced monitoring metric.
        self.method = method
        # The key of the enhanced monitoring metric.
        self.metrics_key = metrics_key
        # The alias of the enhanced monitoring metric.
        self.metrics_key_alias = metrics_key_alias
        # The serial number of the enhanced monitoring metric.
        self.sort_rule = sort_rule
        # The unit of the enhanced monitoring metric.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.group_key is not None:
            result['GroupKey'] = self.group_key

        if self.group_key_type is not None:
            result['GroupKeyType'] = self.group_key_type

        if self.method is not None:
            result['Method'] = self.method

        if self.metrics_key is not None:
            result['MetricsKey'] = self.metrics_key

        if self.metrics_key_alias is not None:
            result['MetricsKeyAlias'] = self.metrics_key_alias

        if self.sort_rule is not None:
            result['SortRule'] = self.sort_rule

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('GroupKey') is not None:
            self.group_key = m.get('GroupKey')

        if m.get('GroupKeyType') is not None:
            self.group_key_type = m.get('GroupKeyType')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('MetricsKey') is not None:
            self.metrics_key = m.get('MetricsKey')

        if m.get('MetricsKeyAlias') is not None:
            self.metrics_key_alias = m.get('MetricsKeyAlias')

        if m.get('SortRule') is not None:
            self.sort_rule = m.get('SortRule')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

