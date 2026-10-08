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
        # The instance ID. You can call DescribeDBInstances to obtain the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The monitoring metrics to configure for the instance. You can specify multiple metric keys separated by commas (,). A maximum of 30 metric keys can be specified.
        # 
        # You can call the DescribeAvailableMetrics operation to obtain the enhanced monitoring metric keys.
        # 
        # This parameter is required.
        self.metrics_config = metrics_config
        self.resource_owner_id = resource_owner_id
        # The scope of the modification. Valid values:
        # * **instance**: instance level. The modification is applied only to cloud disk instance.
        # * **region**: region level. The modification is applied to all ApsaraDB RDS for PostgreSQL instances that use the same storage type as cloud disk instance in the current region. For example, if cloud disk instance uses cloud disks, the modification is applied to all ApsaraDB RDS for PostgreSQL instances with cloud disks in the current region.
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

