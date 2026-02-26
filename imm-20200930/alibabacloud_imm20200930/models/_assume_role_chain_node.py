# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssumeRoleChainNode(DaraModel):
    def __init__(
        self,
        owner_id: str = None,
        role: str = None,
        type: str = None,
    ):
        # The UID of the account.
        # 
        # This parameter is required.
        self.owner_id = owner_id
        # The role.
        # 
        # This parameter is required.
        self.role = role
        # The type of the account. Valid values:
        # 
        # *   user: Alibaba Cloud account.
        # *   service: Alibaba Cloud service.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.role is not None:
            result['Role'] = self.role

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

