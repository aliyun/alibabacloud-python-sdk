# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAccountMaskingPrivilegeRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dbname: str = None,
        expire_time: str = None,
        owner_id: str = None,
        privilege: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.dbname = dbname
        self.expire_time = expire_time
        self.owner_id = owner_id
        # This parameter is required.
        self.privilege = privilege
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.privilege is not None:
            result['Privilege'] = self.privilege

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Privilege') is not None:
            self.privilege = m.get('Privilege')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

