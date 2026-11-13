# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeScalingActivitiesRequest(DaraModel):
    def __init__(
        self,
        instance_refresh_task_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_activity_ids: List[str] = None,
        scaling_group_id: str = None,
        status_code: str = None,
    ):
        # The ID of the instance refresh task node. You can configure the Settings of this parameter to perform a parameter query for the scaling activity list related to the instance refresh task.
        self.instance_refresh_task_id = instance_refresh_task_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the scaling activity list. Pages start from 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The paging Settings for the number of entries per page in a paged query. Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the scaling group to which the scaling activity belongs.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the scaling activity to be queried.
        # 
        # > When you invoke this API, you must specify either the ScalingGroupId or ScalingActivityIds parameter. If neither parameter is specified, an error occurs.
        self.scaling_activity_ids = scaling_activity_ids
        # The ID of the scaling group.
        # 
        # > When you call this operation, you must specify either ScalingGroupId or ScalingActivityIds. If neither is specified, an error occurs.
        self.scaling_group_id = scaling_group_id
        # The status of the scaling activity. Valid values:
        #  
        # - Successful: The scaling activity is successful. 
        # - Warning: The scaling activity is partially successful. 
        # - Failed: The scaling activity failed. 
        # - InProgress: The scaling activity is in progress. 
        # - Rejected: The request to execute the scaling activity is rejected.
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_refresh_task_id is not None:
            result['InstanceRefreshTaskId'] = self.instance_refresh_task_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scaling_activity_ids is not None:
            result['ScalingActivityIds'] = self.scaling_activity_ids

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceRefreshTaskId') is not None:
            self.instance_refresh_task_id = m.get('InstanceRefreshTaskId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScalingActivityIds') is not None:
            self.scaling_activity_ids = m.get('ScalingActivityIds')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

