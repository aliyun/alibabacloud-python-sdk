# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ModifyVpcPrefixListRequest(DaraModel):
    def __init__(
        self,
        add_prefix_list_entry: List[main_models.ModifyVpcPrefixListRequestAddPrefixListEntry] = None,
        client_token: str = None,
        dry_run: bool = None,
        max_entries: int = None,
        owner_account: str = None,
        owner_id: int = None,
        prefix_list_description: str = None,
        prefix_list_id: str = None,
        prefix_list_name: str = None,
        region_id: str = None,
        remove_prefix_list_entry: List[main_models.ModifyVpcPrefixListRequestRemovePrefixListEntry] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The list of Classless Inter-Domain Routing blocks to add to the prefix list instance.
        self.add_prefix_list_entry = add_prefix_list_entry
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may differ for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # - **true**: performs a dry run without modifying the prefix list configuration. The system checks the required parameters, request format, and service limits. If the check fails, the corresponding error is returned. If the check succeeds, the `DryRunOperation` error code is returned.
        # - **false** (default): performs a dry run and sends the request. If the check succeeds, an HTTP 2xx status code is returned and the prefix list configuration is modified.
        self.dry_run = dry_run
        # The new maximum number of Classless Inter-Domain Routing block entries in the prefix list instance.
        self.max_entries = max_entries
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The new description of the prefix list.
        # 
        # The description must be 1 to 256 characters in length and cannot start with `http://` or `https://`.
        self.prefix_list_description = prefix_list_description
        # The instance ID of the prefix list that you want to modify.
        # 
        # This parameter is required.
        self.prefix_list_id = prefix_list_id
        # The new name of the prefix list.
        # 
        # The name must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
        self.prefix_list_name = prefix_list_name
        # The region ID of the prefix list that you want to modify.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of Classless Inter-Domain Routing blocks to delete from the prefix list instance.
        self.remove_prefix_list_entry = remove_prefix_list_entry
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.add_prefix_list_entry:
            for v1 in self.add_prefix_list_entry:
                 if v1:
                    v1.validate()
        if self.remove_prefix_list_entry:
            for v1 in self.remove_prefix_list_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddPrefixListEntry'] = []
        if self.add_prefix_list_entry is not None:
            for k1 in self.add_prefix_list_entry:
                result['AddPrefixListEntry'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.max_entries is not None:
            result['MaxEntries'] = self.max_entries

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prefix_list_description is not None:
            result['PrefixListDescription'] = self.prefix_list_description

        if self.prefix_list_id is not None:
            result['PrefixListId'] = self.prefix_list_id

        if self.prefix_list_name is not None:
            result['PrefixListName'] = self.prefix_list_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['RemovePrefixListEntry'] = []
        if self.remove_prefix_list_entry is not None:
            for k1 in self.remove_prefix_list_entry:
                result['RemovePrefixListEntry'].append(k1.to_map() if k1 else None)

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_prefix_list_entry = []
        if m.get('AddPrefixListEntry') is not None:
            for k1 in m.get('AddPrefixListEntry'):
                temp_model = main_models.ModifyVpcPrefixListRequestAddPrefixListEntry()
                self.add_prefix_list_entry.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('MaxEntries') is not None:
            self.max_entries = m.get('MaxEntries')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PrefixListDescription') is not None:
            self.prefix_list_description = m.get('PrefixListDescription')

        if m.get('PrefixListId') is not None:
            self.prefix_list_id = m.get('PrefixListId')

        if m.get('PrefixListName') is not None:
            self.prefix_list_name = m.get('PrefixListName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.remove_prefix_list_entry = []
        if m.get('RemovePrefixListEntry') is not None:
            for k1 in m.get('RemovePrefixListEntry'):
                temp_model = main_models.ModifyVpcPrefixListRequestRemovePrefixListEntry()
                self.remove_prefix_list_entry.append(temp_model.from_map(k1))

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class ModifyVpcPrefixListRequestRemovePrefixListEntry(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        description: str = None,
    ):
        # The Classless Inter-Domain Routing block to delete from the prefix list instance.
        self.cidr = cidr
        # The description of the Classless Inter-Domain Routing block to delete from the prefix list.
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

class ModifyVpcPrefixListRequestAddPrefixListEntry(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        description: str = None,
    ):
        # The Classless Inter-Domain Routing block to add to the prefix list instance.
        # 
        # > If the Classless Inter-Domain Routing block already exists in the prefix list, only the value of **AddPrefixListEntry.N.Description** is modified, which means only the description of the Classless Inter-Domain Routing block is updated.
        self.cidr = cidr
        # The description of the Classless Inter-Domain Routing block to add to the prefix list instance.
        # 
        # The description must be 1 to 128 characters in length and cannot start with `http://` or `https://`.
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

