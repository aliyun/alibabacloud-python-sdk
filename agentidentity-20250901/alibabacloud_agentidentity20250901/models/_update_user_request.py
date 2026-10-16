# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        email: str = None,
        status: str = None,
        user_name: str = None,
        user_pool_name: str = None,
    ):
        # The description of the user. The description must be 0 to 256 characters in length.
        self.description = description
        # The display name of the user. The display name must be 0 to 128 characters in length.
        self.display_name = display_name
        # The email address of the user.
        self.email = email
        # The status of the user. Valid values:
        # - Enabled: The user is enabled.
        # - Disabled: The user is disabled.
        self.status = status
        # The username of the user to be updated. The username can contain letters, digits, underscores (_), periods (.), and hyphens (-), and must be 3 to 128 characters in length.
        self.user_name = user_name
        # The name of the user pool.
        self.user_pool_name = user_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.status is not None:
            result['Status'] = self.status

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

