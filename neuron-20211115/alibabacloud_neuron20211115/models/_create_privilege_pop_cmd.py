# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePrivilegePopCmd(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        actions: str = None,
        resource: str = None,
        role_id: int = None,
    ):
        self.account_id = account_id
        self.actions = actions
        self.resource = resource
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.actions is not None:
            result['actions'] = self.actions

        if self.resource is not None:
            result['resource'] = self.resource

        if self.role_id is not None:
            result['roleId'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('resource') is not None:
            self.resource = m.get('resource')

        if m.get('roleId') is not None:
            self.role_id = m.get('roleId')

        return self

