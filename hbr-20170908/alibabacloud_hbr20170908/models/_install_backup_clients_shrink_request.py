# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstallBackupClientsShrinkRequest(DaraModel):
    def __init__(
        self,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        instance_ids_shrink: str = None,
    ):
        # The name of the RAM role that is created in the source account for cross-account backup.
        self.cross_account_role_name = cross_account_role_name
        # The type of cross-account backup. Valid values:
        # 
        # - SELF_ACCOUNT: Backs up data within the current account.
        # 
        # - CROSS_ACCOUNT: Backs up data across accounts.
        self.cross_account_type = cross_account_type
        # The ID of the source account that is used for cross-account backup.
        self.cross_account_user_id = cross_account_user_id
        # The IDs of the ECS instances. You can specify a maximum of 20 instance IDs.
        # 
        # This parameter is required.
        self.instance_ids_shrink = instance_ids_shrink

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

        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        return self

