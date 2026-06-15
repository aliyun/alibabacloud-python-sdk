# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoProvisioningGroupsRequest(DaraModel):
    def __init__(
        self,
        auto_provisioning_group_id: List[str] = None,
        auto_provisioning_group_name: str = None,
        auto_provisioning_group_status: List[str] = None,
        auto_provisioning_group_types: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.DescribeAutoProvisioningGroupsRequestTag] = None,
    ):
        # The IDs of the auto provisioning groups. You can specify up to 20 IDs.
        self.auto_provisioning_group_id = auto_provisioning_group_id
        # The name of the auto provisioning group.
        self.auto_provisioning_group_name = auto_provisioning_group_name
        # The statuses of the auto provisioning groups.
        self.auto_provisioning_group_status = auto_provisioning_group_status
        self.auto_provisioning_group_types = auto_provisioning_group_types
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number to return.
        # 
        # Start value: 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return per page.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The ID of the region where the auto provisioning group is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the auto provisioning group belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags used to filter auto provisioning groups. You can specify up to 20 tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_provisioning_group_id is not None:
            result['AutoProvisioningGroupId'] = self.auto_provisioning_group_id

        if self.auto_provisioning_group_name is not None:
            result['AutoProvisioningGroupName'] = self.auto_provisioning_group_name

        if self.auto_provisioning_group_status is not None:
            result['AutoProvisioningGroupStatus'] = self.auto_provisioning_group_status

        if self.auto_provisioning_group_types is not None:
            result['AutoProvisioningGroupTypes'] = self.auto_provisioning_group_types

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

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoProvisioningGroupId') is not None:
            self.auto_provisioning_group_id = m.get('AutoProvisioningGroupId')

        if m.get('AutoProvisioningGroupName') is not None:
            self.auto_provisioning_group_name = m.get('AutoProvisioningGroupName')

        if m.get('AutoProvisioningGroupStatus') is not None:
            self.auto_provisioning_group_status = m.get('AutoProvisioningGroupStatus')

        if m.get('AutoProvisioningGroupTypes') is not None:
            self.auto_provisioning_group_types = m.get('AutoProvisioningGroupTypes')

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

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeAutoProvisioningGroupsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeAutoProvisioningGroupsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. The key can be up to 128 characters in length and cannot be an empty string. It cannot start with `aliyun` or `acs:` or contain http\\:// or https\\://.
        self.key = key
        # The value of the tag. The value can be up to 128 characters in length and can be an empty string. It cannot contain `http://` or `https://`.
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

