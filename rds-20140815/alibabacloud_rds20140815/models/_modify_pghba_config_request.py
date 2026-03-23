# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class ModifyPGHbaConfigRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstance_id: str = None,
        hba_item: List[main_models.ModifyPGHbaConfigRequestHbaItem] = None,
        ops_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.hba_item = hba_item
        # This parameter is required.
        self.ops_type = ops_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.hba_item:
            for v1 in self.hba_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        result['HbaItem'] = []
        if self.hba_item is not None:
            for k1 in self.hba_item:
                result['HbaItem'].append(k1.to_map() if k1 else None)

        if self.ops_type is not None:
            result['OpsType'] = self.ops_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        self.hba_item = []
        if m.get('HbaItem') is not None:
            for k1 in m.get('HbaItem'):
                temp_model = main_models.ModifyPGHbaConfigRequestHbaItem()
                self.hba_item.append(temp_model.from_map(k1))

        if m.get('OpsType') is not None:
            self.ops_type = m.get('OpsType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class ModifyPGHbaConfigRequestHbaItem(DaraModel):
    def __init__(
        self,
        address: str = None,
        database: str = None,
        mask: str = None,
        method: str = None,
        option: str = None,
        priority_id: int = None,
        type: str = None,
        user: str = None,
    ):
        # This parameter is required.
        self.address = address
        # This parameter is required.
        self.database = database
        self.mask = mask
        # This parameter is required.
        self.method = method
        self.option = option
        # This parameter is required.
        self.priority_id = priority_id
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.database is not None:
            result['Database'] = self.database

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.method is not None:
            result['Method'] = self.method

        if self.option is not None:
            result['Option'] = self.option

        if self.priority_id is not None:
            result['PriorityId'] = self.priority_id

        if self.type is not None:
            result['Type'] = self.type

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        if m.get('PriorityId') is not None:
            self.priority_id = m.get('PriorityId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

