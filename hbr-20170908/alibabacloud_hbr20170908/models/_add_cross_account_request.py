# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCrossAccountRequest(DaraModel):
    def __init__(
        self,
        alias: str = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
    ):
        # The alias. The maximum length is 32 characters. This parameter is not required for cross-account backups that are configured based on a resource directory.
        self.alias = alias
        # The name of the RAM role for the account to back up. This parameter is used when you configure a cross-account backup by assuming a RAM role.
        self.cross_account_role_name = cross_account_role_name
        # The type of cross-account backup. Valid values:
        # 
        # - **CROSS_ACCOUNT**: Configures a cross-account backup by assuming a RAM role.
        # 
        # - **CROSS_ACCOUNT_BY_RD**: Configures a cross-account backup based on a resource directory.
        self.cross_account_type = cross_account_type
        # The UID of the account to back up.
        self.cross_account_user_id = cross_account_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        return self

