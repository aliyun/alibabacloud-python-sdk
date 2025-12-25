# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAbacAuthorizationRequest(DaraModel):
    def __init__(
        self,
        identity_type: str = None,
        policy_id: int = None,
        role_id: int = None,
        tid: int = None,
        user_id: int = None,
    ):
        # Principal Type. Valid values:**user**or**custom role**.
        # 
        # Valid values:
        # 
        # *   USER
        # *   ROLE
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # The ID of the policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The ID of the role.
        # 
        # > If IdentityType is set to ROLE, this parameter is required.
        self.role_id = role_id
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid
        # The ID of the user. You can call the [GetUser](https://help.aliyun.com/document_detail/465816.html) operation to query the user ID.
        # 
        # > If IdentityType is set to USER, this parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

