# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetServiceIdentityRoleResponseBody(DaraModel):
    def __init__(
        self,
        policy: str = None,
        request_id: str = None,
        role_name: str = None,
    ):
        self.policy = policy
        self.request_id = request_id
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy is not None:
            result['Policy'] = self.policy

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

