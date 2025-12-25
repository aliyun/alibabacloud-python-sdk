# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyDatabaseRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dst_dbname: str = None,
        owner_id: int = None,
        reserve_account: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        src_dbname: str = None,
    ):
        # The instance name.
        self.dbinstance_name = dbinstance_name
        # The destination database name.
        self.dst_dbname = dst_dbname
        self.owner_id = owner_id
        # The reserved account.
        self.reserve_account = reserve_account
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The source database name.
        self.src_dbname = src_dbname

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dst_dbname is not None:
            result['DstDBName'] = self.dst_dbname

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.reserve_account is not None:
            result['ReserveAccount'] = self.reserve_account

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.src_dbname is not None:
            result['SrcDBName'] = self.src_dbname

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DstDBName') is not None:
            self.dst_dbname = m.get('DstDBName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ReserveAccount') is not None:
            self.reserve_account = m.get('ReserveAccount')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SrcDBName') is not None:
            self.src_dbname = m.get('SrcDBName')

        return self

