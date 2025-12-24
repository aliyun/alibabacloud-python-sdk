# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class CreateAccessControlListRequest(DaraModel):
    def __init__(
        self,
        acl_name: str = None,
        address_ipversion: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreateAccessControlListRequestTag] = None,
    ):
        # The name of the ACL. The name must be 1 to 80 characters in length, and can contain letters, digits, periods (.), hyphens (-), forward slashes (/), and underscores (_). The name of the ACL that you create must be unique within each region.
        # 
        # This parameter is required.
        self.acl_name = acl_name
        # The IP version. Valid values: **ipv4** and **ipv6**.
        self.address_ipversion = address_ipversion
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the ACL.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags.
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
        if self.acl_name is not None:
            result['AclName'] = self.acl_name

        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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
        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')

        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

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
                temp_model = main_models.CreateAccessControlListRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateAccessControlListRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N. Valid values of N: **1** to **20**. The tag key cannot be an empty string. The tag key can be up to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `acs:` or `aliyun`.
        self.key = key
        # The value of tag N. Valid values of N: **1** to **20**. The tag value can be an empty string. The tag value must be 0 to 128 characters in length, and cannot start with `acs:`. It cannot contain `http://` or `https://`.
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

