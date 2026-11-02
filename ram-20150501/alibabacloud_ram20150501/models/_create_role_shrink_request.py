# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRoleShrinkRequest(DaraModel):
    def __init__(
        self,
        allow_console_login: bool = None,
        assume_role_policy_document: str = None,
        description: str = None,
        max_session_duration: int = None,
        role_name: str = None,
        tag_shrink: str = None,
    ):
        # Specifies whether the RAM role is allowed to log on to the console. Valid values:
        # - true: allowed
        # - false: not allowed
        self.allow_console_login = allow_console_login
        # The trust policy. Specifies one or more principals that are allowed to assume the RAM role. The principals can be Alibaba Cloud accounts, Alibaba Cloud services, or identity providers.
        # >Resource Access Management (RAM) users cannot assume RAM roles whose trusted entity is an Alibaba Cloud service.
        self.assume_role_policy_document = assume_role_policy_document
        # The description of the RAM role.
        # 
        # The description must be 1 to 1,024 characters in length.
        self.description = description
        # The maximum session duration of the RAM role.
        # 
        # Valid values: 3600 to 43200. Unit: seconds. Default value: 3600.
        # 
        # If this parameter is left empty, the default value is used.
        self.max_session_duration = max_session_duration
        # The name of the RAM role.
        # 
        # The name must be 1 to 64 characters in length and can contain letters, digits, periods (.), and hyphens (-).
        self.role_name = role_name
        # The tags.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_console_login is not None:
            result['AllowConsoleLogin'] = self.allow_console_login

        if self.assume_role_policy_document is not None:
            result['AssumeRolePolicyDocument'] = self.assume_role_policy_document

        if self.description is not None:
            result['Description'] = self.description

        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowConsoleLogin') is not None:
            self.allow_console_login = m.get('AllowConsoleLogin')

        if m.get('AssumeRolePolicyDocument') is not None:
            self.assume_role_policy_document = m.get('AssumeRolePolicyDocument')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

