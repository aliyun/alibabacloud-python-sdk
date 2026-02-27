# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRoleRequest(DaraModel):
    def __init__(
        self,
        new_assume_role_policy_document: str = None,
        new_description: str = None,
        new_max_session_duration: int = None,
        role_name: str = None,
    ):
        # The trust policy of the RAM role.
        self.new_assume_role_policy_document = new_assume_role_policy_document
        # The description of the RAM role.
        # 
        # The description must be 1 to 1,024 characters in length.
        self.new_description = new_description
        # The maximum session time of the RAM role.
        # 
        # Valid values: 3600 to 43200. Unit: seconds. Default value: 3600.
        # 
        # If you do not specify this parameter, the default value is used.
        self.new_max_session_duration = new_max_session_duration
        # The name of the RAM role.
        # 
        # The name must be 1 to 64 characters in length, and can contain letters, digits, periods (.), and hyphens (-).
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
        if self.new_assume_role_policy_document is not None:
            result['NewAssumeRolePolicyDocument'] = self.new_assume_role_policy_document

        if self.new_description is not None:
            result['NewDescription'] = self.new_description

        if self.new_max_session_duration is not None:
            result['NewMaxSessionDuration'] = self.new_max_session_duration

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewAssumeRolePolicyDocument') is not None:
            self.new_assume_role_policy_document = m.get('NewAssumeRolePolicyDocument')

        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')

        if m.get('NewMaxSessionDuration') is not None:
            self.new_max_session_duration = m.get('NewMaxSessionDuration')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

