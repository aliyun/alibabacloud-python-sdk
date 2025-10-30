# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceConfigRequest(DaraModel):
    def __init__(
        self,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        idle_time: int = None,
        resource_group_id: str = None,
        serverless_resource: int = None,
    ):
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The ID of the instance.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the instance IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The wait period for the instance that has no traffic to become idle. Minimum value: 60. Default value: 600. Unit: seconds.
        self.idle_time = idle_time
        # The ID of the resource group to which the instance belongs. For more information about how to obtain the ID of a resource group, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        # The threshold of computing resources. Valid values: 8 to 32. Unit: AnalyticDB Compute Units (ACUs).
        self.serverless_resource = serverless_resource

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.idle_time is not None:
            result['IdleTime'] = self.idle_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.serverless_resource is not None:
            result['ServerlessResource'] = self.serverless_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('IdleTime') is not None:
            self.idle_time = m.get('IdleTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ServerlessResource') is not None:
            self.serverless_resource = m.get('ServerlessResource')

        return self

