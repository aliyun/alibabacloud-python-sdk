# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        dbinstance_description: str = None,
        dbinstance_ids: str = None,
        dbinstance_status: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
        tag_shrink: str = None,
    ):
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The instance ID. Separate multiple instance IDs with commas (,).
        self.dbinstance_ids = dbinstance_ids
        # The state of the instance. Valid values:
        # 
        # *   **CREATING**: The instance is being created.
        # *   **ACTIVATION**: The instance is running.
        # *   **RESOURCE_CHANGING**: The resource configuration of the instance is being changed.
        # *   **ORDER_PREPARING**: The order is being confirmed.
        # *   **READONLY_RESOURCE_CHANGING**: The resource configuration of the instance is being changed and the instance is write-locked.
        # *   **DELETING**: The instance is being deleted.
        self.dbinstance_status = dbinstance_status
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**
        # *   **100**
        self.page_size = page_size
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids

        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')

        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

