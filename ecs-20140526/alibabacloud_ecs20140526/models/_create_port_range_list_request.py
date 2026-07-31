# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreatePortRangeListRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        entry: List[main_models.CreatePortRangeListRequestEntry] = None,
        max_entries: int = None,
        owner_account: str = None,
        owner_id: int = None,
        port_range_list_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreatePortRangeListRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the port list. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The array of port list entries.
        self.entry = entry
        # The maximum number of entries that the port list supports. This value cannot be changed after the port list is created. Valid values: 1 to 2000.
        # 
        # >Notice: When calculating rule quotas for resources associated with the port list (such as security groups), the maximum number of entries is used instead of the actual number of entries. Set this value appropriately.
        # 
        # This parameter is required.
        self.max_entries = max_entries
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the port list. The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. The name cannot start with http://, https://, com.aliyun, or com.alibabacloud. The name can contain letters, digits, Chinese characters, colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # This parameter is required.
        self.port_range_list_name = port_range_list_name
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the port list belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The array of tags bound to the port list. Array length: 0 to 20.
        self.tag = tag

    def validate(self):
        if self.entry:
            for v1 in self.entry:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        result['Entry'] = []
        if self.entry is not None:
            for k1 in self.entry:
                result['Entry'].append(k1.to_map() if k1 else None)

        if self.max_entries is not None:
            result['MaxEntries'] = self.max_entries

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.port_range_list_name is not None:
            result['PortRangeListName'] = self.port_range_list_name

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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.entry = []
        if m.get('Entry') is not None:
            for k1 in m.get('Entry'):
                temp_model = main_models.CreatePortRangeListRequestEntry()
                self.entry.append(temp_model.from_map(k1))

        if m.get('MaxEntries') is not None:
            self.max_entries = m.get('MaxEntries')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PortRangeListName') is not None:
            self.port_range_list_name = m.get('PortRangeListName')

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
                temp_model = main_models.CreatePortRangeListRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreatePortRangeListRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the port list.
        # 
        # This parameter cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        self.key = key
        # The tag value of the port list.
        # 
        # This parameter cannot be null but can be an empty string. The tag value can be up to 128 characters in length and cannot contain http:// or https://.
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

class CreatePortRangeListRequestEntry(DaraModel):
    def __init__(
        self,
        description: str = None,
        port_range: str = None,
    ):
        # The description of the port range. The description must be 2 to 32 characters in length and cannot start with http:// or https://. Valid values of N: 0 to 200.
        self.description = description
        # The port range. Valid values of N: 0 to 200.
        # 
        # - The number of entries cannot exceed the maximum number of entries (MaxEntries).
        # 
        # - The PortRange values in multiple entries cannot be duplicated.
        self.port_range = port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        return self

