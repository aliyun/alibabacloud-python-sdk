# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCrossAccountRequest(DaraModel):
    def __init__(
        self,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
    ):
        # This parameter is required.
        self.cross_account_role_name = cross_account_role_name
        self.cross_account_type = cross_account_type
        # This parameter is required.
        self.cross_account_user_id = cross_account_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        return self

