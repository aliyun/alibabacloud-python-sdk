# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRoleRequest(DaraModel):
    def __init__(
        self,
        assume_role_policy_document: str = None,
        description: str = None,
        max_session_duration: int = None,
        role_name: str = None,
    ):
        # The content of the access policy for assuming the role.
        # 
        # Specifies one or more entities that are allowed to assume the role. The trusted entity can be an Alibaba Cloud account, an Alibaba Cloud service, or an identity provider.
        # 
        # > A Resource Access Management (RAM) user cannot assume a RAM role whose trusted entity is an Alibaba Cloud service.
        # 
        # This parameter is required.
        self.assume_role_policy_document = assume_role_policy_document
        # The description of the role.
        # 
        # The description must be 1 to 1,024 characters in length.
        self.description = description
        # The maximum session duration of the role.
        # 
        # Valid values: 3600 to 43200. Unit: seconds. Default value: 3600.
        # 
        # If this parameter is left empty, the default value is used.
        self.max_session_duration = max_session_duration
        # The name of the role.
        # 
        # The name must be 1 to 64 characters in length and can contain letters, digits, periods (.), and hyphens (-).
        # 
        # This parameter is required.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document

        if self.description is not None:
            result['Description'] = self.description

        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

