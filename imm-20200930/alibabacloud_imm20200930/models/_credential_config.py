# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CredentialConfig(DaraModel):
    def __init__(
        self,
        chain: List[main_models.CredentialConfigChain] = None,
        policy: str = None,
        service_role: str = None,
    ):
        # The authorization chains. All roles in the array must have the `sts:AssumeRole` permission. You need to only grant other permissions, such as read and write permissions on OSS, to the last role in the array. You can grant permissions in the RAM console.
        self.chain = chain
        # The policy that is attached to the role specified by the ServiceRole parameter. For example, the policy allows access to OSS. This parameter is optional.
        self.policy = policy
        # The service role in the account that is used to call an IMM API operation. The role must have the `sts:AssumeRole` permission. You can configure permissions for the role in the Resource Access Management (RAM) console.
        self.service_role = service_role

    def validate(self):
        if self.chain:
            for v1 in self.chain:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Chain'] = []
        if self.chain is not None:
            for k1 in self.chain:
                result['Chain'].append(k1.to_map() if k1 else None)

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.service_role is not None:
            result['ServiceRole'] = self.service_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chain = []
        if m.get('Chain') is not None:
            for k1 in m.get('Chain'):
                temp_model = main_models.CredentialConfigChain()
                self.chain.append(temp_model.from_map(k1))

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')

        return self

class CredentialConfigChain(DaraModel):
    def __init__(
        self,
        assume_role_for: str = None,
        role: str = None,
        role_type: str = None,
    ):
        # The ID of the account that you use to grant permissions.
        self.assume_role_for = assume_role_for
        # The RAM role that can be assumed.
        self.role = role
        # The role type. Valid values:
        # 
        # *   user: Alibaba Cloud account.
        # *   service: Alibaba Cloud service.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for

        if self.role is not None:
            result['Role'] = self.role

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

