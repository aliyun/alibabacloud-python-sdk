# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckRoleRequest(DaraModel):
    def __init__(
        self,
        check_role_type: str = None,
        cross_account_role_name: str = None,
        cross_account_user_id: int = None,
    ):
        # The role type. Valid values:
        # - EcsRole: access permissions for ECS resources
        # - CsgRole: permissions to back up Cloud Storage Gateway resources
        # - NasRole: permissions to back up NAS resources
        # - OssRole: permissions to back up OSS resources
        # - UdmRole: permissions to back up entire ECS instances
        # - VMwareLocalRole: permissions to back up on-premises VMware virtual machines
        # - VMwareCloudRole: permissions to back up cloud-based VMware virtual machines
        # - EcsBackupRole: permissions for ECS backup
        # - OtsRole: permissions to back up OTS resources
        # - CrossAccountRole: permissions for cross-account backup
        self.check_role_type = check_role_type
        # The name of the RAM role created in the source account for cross-account backup managed by the current account.
        self.cross_account_role_name = cross_account_role_name
        # The ID of the source account for cross-account backup managed by the current account.
        self.cross_account_user_id = cross_account_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_role_type is not None:
            result['CheckRoleType'] = self.check_role_type

        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckRoleType') is not None:
            self.check_role_type = m.get('CheckRoleType')

        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        return self

