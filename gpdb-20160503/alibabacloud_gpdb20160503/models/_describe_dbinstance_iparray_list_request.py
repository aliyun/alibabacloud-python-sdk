# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceIPArrayListRequest(DaraModel):
    def __init__(
        self,
        dbinstance_iparray_name: str = None,
        dbinstance_id: str = None,
        resource_group_id: str = None,
    ):
        # The name of the IP address whitelist. If you do not specify this parameter, the default whitelist is queried.
        # 
        # >  Each instance supports up to 50 IP address whitelists.
        self.dbinstance_iparray_name = dbinstance_iparray_name
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query details about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The ID of the resource group to which the instance belongs. For information about how to obtain the ID of a resource group, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_iparray_name is not None:
            result['DBInstanceIPArrayName'] = self.dbinstance_iparray_name

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceIPArrayName') is not None:
            self.dbinstance_iparray_name = m.get('DBInstanceIPArrayName')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

