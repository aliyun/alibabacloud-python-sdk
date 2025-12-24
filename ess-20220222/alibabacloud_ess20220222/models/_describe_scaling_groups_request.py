# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeScalingGroupsRequest(DaraModel):
    def __init__(
        self,
        group_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_ids: List[str] = None,
        scaling_group_name: str = None,
        scaling_group_names: List[str] = None,
        tags: List[main_models.DescribeScalingGroupsRequestTags] = None,
    ):
        # The type of instances that are managed by the scaling group. Valid values:
        # 
        # *   ECS: Elastic Compute Service (ECS) instances.
        # *   ECI: elastic container instances.
        self.group_type = group_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Page starts from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the scaling group.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the scaling group that you want to query belongs.
        # 
        # >  If no scaling group belongs to the specified resource group, the query result is empty and no error is reported.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The IDs of the scaling groups that you want to query.
        # 
        # The IDs of inactive scaling groups are not included in the query results, and no error is returned.
        self.scaling_group_ids = scaling_group_ids
        # The name of the scaling group.
        self.scaling_group_name = scaling_group_name
        # The names of the scaling groups that you want to query.
        # 
        # The names of inactive scaling groups are not displayed in the query results, and no error is reported.
        self.scaling_group_names = scaling_group_names
        # The tags of the scaling group.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_type is not None:
            result['GroupType'] = self.group_type

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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scaling_group_ids is not None:
            result['ScalingGroupIds'] = self.scaling_group_ids

        if self.scaling_group_name is not None:
            result['ScalingGroupName'] = self.scaling_group_name

        if self.scaling_group_names is not None:
            result['ScalingGroupNames'] = self.scaling_group_names

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScalingGroupIds') is not None:
            self.scaling_group_ids = m.get('ScalingGroupIds')

        if m.get('ScalingGroupName') is not None:
            self.scaling_group_name = m.get('ScalingGroupName')

        if m.get('ScalingGroupNames') is not None:
            self.scaling_group_names = m.get('ScalingGroupNames')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeScalingGroupsRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeScalingGroupsRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the scaling group.
        self.key = key
        # The tag value of the scaling group.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

