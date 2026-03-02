# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RoleRevokeCmd(DaraModel):
    def __init__(
        self,
        authorizer_id: str = None,
        authorizer_type: str = None,
        role_id: int = None,
    ):
        # This parameter is required.
        self.authorizer_id = authorizer_id
        # This parameter is required.
        self.authorizer_type = authorizer_type
        # This parameter is required.
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorizer_id is not None:
            result['authorizerId'] = self.authorizer_id

        if self.authorizer_type is not None:
            result['authorizerType'] = self.authorizer_type

        if self.role_id is not None:
            result['roleId'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizerId') is not None:
            self.authorizer_id = m.get('authorizerId')

        if m.get('authorizerType') is not None:
            self.authorizer_type = m.get('authorizerType')

        if m.get('roleId') is not None:
            self.role_id = m.get('roleId')

        return self

