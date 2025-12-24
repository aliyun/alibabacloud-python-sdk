# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreatePrefixListRequest(DaraModel):
    def __init__(
        self,
        address_family: str = None,
        client_token: str = None,
        description: str = None,
        entry: List[main_models.CreatePrefixListRequestEntry] = None,
        max_entries: int = None,
        owner_account: str = None,
        owner_id: int = None,
        prefix_list_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.CreatePrefixListRequestTag] = None,
    ):
        # The IP address family. Valid values:
        # 
        # *   IPv4
        # *   IPv6
        # 
        # This parameter is required.
        self.address_family = address_family
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The `token` can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the prefix list. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The details of entries in the prefix list.
        self.entry = entry
        # The maximum number of entries that the prefix list can contain. Valid values: 1 to 200.
        # 
        # This parameter is required.
        self.max_entries = max_entries
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the prefix list. The name must be 2 to 128 characters in length, and can contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-). It must start with a letter and cannot start with `http://`, `https://`, `com.aliyun`, or `com.alibabacloud`.
        # 
        # This parameter is required.
        self.prefix_list_name = prefix_list_name
        # The ID of the region in which to create the prefix list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which to assign the prefix list.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tags to add to the prefix list.
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
        if self.address_family is not None:
            result['AddressFamily'] = self.address_family

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

        if self.prefix_list_name is not None:
            result['PrefixListName'] = self.prefix_list_name

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
        if m.get('AddressFamily') is not None:
            self.address_family = m.get('AddressFamily')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.entry = []
        if m.get('Entry') is not None:
            for k1 in m.get('Entry'):
                temp_model = main_models.CreatePrefixListRequestEntry()
                self.entry.append(temp_model.from_map(k1))

        if m.get('MaxEntries') is not None:
            self.max_entries = m.get('MaxEntries')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrefixListName') is not None:
            self.prefix_list_name = m.get('PrefixListName')

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
                temp_model = main_models.CreatePrefixListRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreatePrefixListRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        self.key = key
        # The value of tag N. Valid values of N: 1 to 20. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain`  http:// or https:// `.
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

class CreatePrefixListRequestEntry(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        description: str = None,
    ):
        # The CIDR block in entry N. Valid values of N: 0 to 200. Notes:
        # 
        # *   The total number of entries cannot exceed the `MaxEntries` value.
        # *   CIDR block types are determined by the IP address family. You cannot combine IPv4 and IPv6 CIDR blocks in a single prefix list.
        # *   CIDR blocks must be unique across all entries in a prefix list. For example, you cannot specify 192.168.1.0/24 twice in the entries of the prefix list.
        # *   You can set a single IP address. The system automatically converts the IP address to a CIDR block. For example, if you set 192.168.1.100, the system automatically converts it to 192.168.1.100/32.
        # *   If you use an IPv6 CIDR block, the system automatically converts the CIDR block to zero and the letters to lowercase. For example, if you specify 2001:0DB8:0000:0000:0000:0000:0000:0000/32, the system converts it to 2001:db8::/32.
        # 
        # For more information about CIDR blocks, see [What is CIDR?](~~185311#598efe6ef1v00~~)
        # 
        # This parameter is left empty by default.
        # 
        # This parameter is required.
        self.cidr = cidr
        # The description in entry N. The description must be 2 to 32 characters in length and cannot start with `http://` or `https://`. Valid values of N: 0 to 200.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

