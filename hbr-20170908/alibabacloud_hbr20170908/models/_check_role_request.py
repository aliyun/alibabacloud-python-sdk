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
        # The type of the role. Valid values:
        # 
        # *   EcsRole: a role with the permissions to access Elastic Compute Service (ECS) resources
        # *   CsgRole: a role with the permissions to perform Cloud Storage Gateway (CSG) backup
        # *   NasRole: a role with the permissions to perform NAS backup
        # *   OssRole: a role with the permissions to perform Object Storage Service (OSS) backup
        # *   UdmRole: a role with the permissions to perform ECS instance backup
        # *   VMwareLocalRole: a role with the permissions to back up on-premises VMware virtual machines (VMs)
        # *   VMwareCloudRole: a role with the permissions to back up VMs deployed on Alibaba Cloud VMware Service (ACVS)
        # *   EcsBackupRole: a role with the permissions to perform ECS backup
        # *   OtsRole: a role with the permissions to perform Tablestore backup
        # *   CrossAccountRole: a role with the permissions to perform cross-account backup
        self.check_role_type = check_role_type
        # The name of the Resource Access Management (RAM) role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
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

