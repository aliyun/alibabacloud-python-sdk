# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBVersionInfosRequest(DaraModel):
    def __init__(
        self,
        dbinstance_mode: str = None,
        dbversion: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The resource type of the instance. Valid values:
        # 
        # *   **StorageElastic**: elastic storage mode.
        # *   **Serverless**: Serverless mode.
        self.dbinstance_mode = dbinstance_mode
        # The minor version number that does not include the prefix.
        self.dbversion = dbversion
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs. For information about how to obtain the ID of a resource group, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_mode is not None:
            result['DBInstanceMode'] = self.dbinstance_mode

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceMode') is not None:
            self.dbinstance_mode = m.get('DBInstanceMode')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

