# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApplicationAssignmentRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        principal_name: str = None,
        principal_type: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The principal name of the RAM user or the role name.
        # 
        # + User principal name: The format is `<username>@<account-id>.onaliyun.com`. You can query it by calling the `GetUser` or `ListUsers` API.
        # + Role name: You can query it by calling the RAM `ListRoles` API.
        # 
        # This parameter is required.
        self.principal_name = principal_name
        # The type of the target principal for the application assignment. Valid values:
        # 
        # + user: The principal is a RAM user. In this case, PrincipalName must be the user principal name.
        # + role: The principal is a RAM role. In this case, PrincipalName must be the role name.
        # 
        # This parameter is required.
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        return self

