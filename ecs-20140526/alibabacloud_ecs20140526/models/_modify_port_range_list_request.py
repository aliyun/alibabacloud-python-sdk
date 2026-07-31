# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyPortRangeListRequest(DaraModel):
    def __init__(
        self,
        add_entry: List[main_models.ModifyPortRangeListRequestAddEntry] = None,
        client_token: str = None,
        description: str = None,
        owner_account: str = None,
        owner_id: int = None,
        port_range_list_id: str = None,
        port_range_list_name: str = None,
        region_id: str = None,
        remove_entry: List[main_models.ModifyPortRangeListRequestRemoveEntry] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The entries to add or modify in the port range list.
        self.add_entry = add_entry
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The description of the port range list. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the port range list to modify.
        # 
        # This parameter is required.
        self.port_range_list_id = port_range_list_id
        # The name of the port range list. The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. It cannot start with http://, https://, com.aliyun, or com.alibabacloud. It can contain letters, Chinese characters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        self.port_range_list_name = port_range_list_name
        # The region ID of the port range list. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The entries to delete from the port range list.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.port_range_list_id is not None:
            result['PortRangeListId'] = self.port_range_list_id

        if self.port_range_list_name is not None:
            result['PortRangeListName'] = self.port_range_list_name

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
                temp_model = main_models.ModifyPortRangeListRequestAddEntry()
                self.add_entry.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PortRangeListId') is not None:
            self.port_range_list_id = m.get('PortRangeListId')

        if m.get('PortRangeListName') is not None:
            self.port_range_list_name = m.get('PortRangeListName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.remove_entry = []
        if m.get('RemoveEntry') is not None:
            for k1 in m.get('RemoveEntry'):
                temp_model = main_models.ModifyPortRangeListRequestRemoveEntry()
                self.remove_entry.append(temp_model.from_map(k1))

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class ModifyPortRangeListRequestRemoveEntry(DaraModel):
    def __init__(
        self,
        port_range: str = None,
    ):
        # The port range. Valid values of N: 0 to 200. Settings:
        # 
        # - You cannot specify duplicate values for `PortRange`.
        # 
        # - The value cannot be the same as the value of the `AddEntry.N.PortRange` parameter.
        self.port_range = port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port_range is not None:
            result['PortRange'] = self.port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        return self

class ModifyPortRangeListRequestAddEntry(DaraModel):
    def __init__(
        self,
        description: str = None,
        port_range: str = None,
    ):
        # The description of the port range. The description must be 2 to 32 characters in length and cannot start with http:// or https://. Valid values of N: 0 to 200.
        self.description = description
        # The port range. Valid values of N: 0 to 200. Settings:
        # 
        # - The number of entries cannot exceed the maximum entry capacity (`MaxEntries`).
        # 
        # - You cannot specify duplicate values for `PortRange`.
        # 
        # - The value cannot be the same as the value of the `RemoveEntry.N.PortRange` parameter.
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

