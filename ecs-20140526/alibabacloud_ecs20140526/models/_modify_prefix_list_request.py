# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyPrefixListRequest(DaraModel):
    def __init__(
        self,
        add_entry: List[main_models.ModifyPrefixListRequestAddEntry] = None,
        description: str = None,
        owner_account: str = None,
        owner_id: int = None,
        prefix_list_id: str = None,
        prefix_list_name: str = None,
        region_id: str = None,
        remove_entry: List[main_models.ModifyPrefixListRequestRemoveEntry] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The prefix list entries to add.
        self.add_entry = add_entry
        # The description of the prefix list. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The prefix list ID.
        # 
        # This parameter is required.
        self.prefix_list_id = prefix_list_id
        # The name of the prefix list. The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. It cannot start with `http://`, `https://`, `com.aliyun`, or `com.alibabacloud`. It can contain letters, Chinese characters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        self.prefix_list_name = prefix_list_name
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The prefix list entries to delete.
        self.remove_entry = remove_entry
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.add_entry:
            for v1 in self.add_entry:
                 if v1:
                    v1.validate()
        if self.remove_entry:
            for v1 in self.remove_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddEntry'] = []
        if self.add_entry is not None:
            for k1 in self.add_entry:
                result['AddEntry'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id

        if self.prefix_list_name is not None:
            result['PrefixListName'] = self.prefix_list_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['RemoveEntry'] = []
        if self.remove_entry is not None:
            for k1 in self.remove_entry:
                result['RemoveEntry'].append(k1.to_map() if k1 else None)

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_entry = []
        if m.get('AddEntry') is not None:
            for k1 in m.get('AddEntry'):
                temp_model = main_models.ModifyPrefixListRequestAddEntry()
                self.add_entry.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')

        if m.get('PrefixListName') is not None:
            self.prefix_list_name = m.get('PrefixListName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.remove_entry = []
        if m.get('RemoveEntry') is not None:
            for k1 in m.get('RemoveEntry'):
                temp_model = main_models.ModifyPrefixListRequestRemoveEntry()
                self.remove_entry.append(temp_model.from_map(k1))

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class ModifyPrefixListRequestRemoveEntry(DaraModel):
    def __init__(
        self,
        cidr: str = None,
    ):
        # The Classless Inter-Domain Routing (CIDR) block of the prefix list entry to delete. Valid values of N: 0 to 200.
        # 
        # Take note of the following items:
        # - Duplicate CIDR blocks are not allowed in Settings.
        # - The value cannot be the same as the value of the `AddEntry.N.Cidr` parameter.
        # 
        # This parameter is required.
        self.cidr = cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        return self

class ModifyPrefixListRequestAddEntry(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        description: str = None,
    ):
        # The Classless Inter-Domain Routing (CIDR) block of the prefix list entry to add. Valid values of N: 0 to 200.
        # 
        # Take note of the following items:
        # - The total number of entries in the prefix list cannot exceed the maximum number of entries supported by the prefix list. You can invoke [DescribePrefixListAttributes](https://help.aliyun.com/document_detail/205872.html) to query the maximum number of entries supported by a specified prefix list.
        # - Duplicate CIDR blocks are not allowed in Settings.
        # - The value cannot be the same as the value of the `RemoveEntry.N.Cidr` parameter.
        # 
        # This parameter is required.
        self.cidr = cidr
        # The description of the prefix list entry. The description must be 2 to 32 characters in length and cannot start with `http://` or `https://`. Valid values of N: 0 to 200.
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

