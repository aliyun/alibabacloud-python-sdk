# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceMetricsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        metrics_config: str = None,
        resource_owner_id: int = None,
        scope: str = None,
    ):
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The keys of the Enhanced Monitoring metrics that you want to display for the instance. You can enter a maximum of 30 metric keys. If you enter multiple metric keys, you must separate the metric keys with commas (,).
        # 
        # You can call the DescribeAvailableMetrics operation to query the keys of metrics.
        # 
        # This parameter is required.
        self.metrics_config = metrics_config
        self.resource_owner_id = resource_owner_id
        # The application scope of this modification. Valid values:
        # 
        # *   **instance**: This modification is applied only to the current instance.
        # *   **region**: This modification is applied to all ApsaraDB RDS for PostgreSQL instances that are equipped with the same type of storage media as the current instance in the region to which the current instance belongs. For example, if the current instance is equipped with cloud disks, this modification is applied to all ApsaraDB RDS for PostgreSQL instances that are equipped with cloud disks in the region to which the current instance belongs.
        # 
        # This parameter is required.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.metrics_config is not None:
            result['MetricsConfig'] = self.metrics_config

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('MetricsConfig') is not None:
            self.metrics_config = m.get('MetricsConfig')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

