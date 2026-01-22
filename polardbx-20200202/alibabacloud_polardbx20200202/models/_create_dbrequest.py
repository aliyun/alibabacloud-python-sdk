# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDBRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_privilege: str = None,
        charset: str = None,
        dbinstance_name: str = None,
        db_description: str = None,
        db_name: str = None,
        mode: str = None,
        region_id: str = None,
        security_account_name: str = None,
        security_account_password: str = None,
        storage_pool_name: str = None,
    ):
        # This parameter is required.
        self.account_name = account_name
        self.account_privilege = account_privilege
        # This parameter is required.
        self.charset = charset
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.db_description = db_description
        # This parameter is required.
        self.db_name = db_name
        self.mode = mode
        # This parameter is required.
        self.region_id = region_id
        self.security_account_name = security_account_name
        self.security_account_password = security_account_password
        self.storage_pool_name = storage_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege

        if self.charset is not None:
            result['Charset'] = self.charset

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.db_description is not None:
            result['DbDescription'] = self.db_description

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_account_name is not None:
            result['SecurityAccountName'] = self.security_account_name

        if self.security_account_password is not None:
            result['SecurityAccountPassword'] = self.security_account_password

        if self.storage_pool_name is not None:
            result['StoragePoolName'] = self.storage_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')

        if m.get('Charset') is not None:
            self.charset = m.get('Charset')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DbDescription') is not None:
            self.db_description = m.get('DbDescription')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityAccountName') is not None:
            self.security_account_name = m.get('SecurityAccountName')

        if m.get('SecurityAccountPassword') is not None:
            self.security_account_password = m.get('SecurityAccountPassword')

        if m.get('StoragePoolName') is not None:
            self.storage_pool_name = m.get('StoragePoolName')

        return self

