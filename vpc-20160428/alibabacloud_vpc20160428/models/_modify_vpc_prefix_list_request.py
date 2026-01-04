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
        # The information about CIDR blocks to be added to the prefix list.
        self.add_prefix_list_entry = add_prefix_list_entry
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system uses **RequestId** as **ClientToken**. **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to only precheck the request. Valid values:
        # 
        # *   **true**: checks the request without performing the operation. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the check, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The maximum number of CIDR blocks supported by the prefix list after the configuration of the prefix list is modified.
        self.max_entries = max_entries
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The new description of the prefix list.
        # 
        # The description must be 1 to 256 characters in length, and cannot start with `http://` or `https://`.
        self.prefix_list_description = prefix_list_description
        # The ID of the prefix list.
        # 
        # This parameter is required.
        self.prefix_list_id = prefix_list_id
        # The new name of the prefix list.
        # 
        # The name must be 1 to 128 characters in length, and cannot start with `http://` or `https://`.
        self.prefix_list_name = prefix_list_name
        # The region ID of the prefix list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The information about CIDR blocks to be deleted to the prefix list.
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
        # The CIDR block that you want to delete from the prefix list.
        self.cidr = cidr
        # The description of the CIDR block that you want to delete.
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
        # The CIDR block to be added to the prefix list.
        # 
        # >  If the CIDR block already exists in the prefix list, you can only modify the description of the CIDR block by setting the **AddPrefixListEntry.N.Description** parameter.
        self.cidr = cidr
        # The description of the CIDR block to be added to the prefix list.
        # 
        # The description must be 1 to 128 characters in length, and cannot start with `http://` or `https://`.
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

