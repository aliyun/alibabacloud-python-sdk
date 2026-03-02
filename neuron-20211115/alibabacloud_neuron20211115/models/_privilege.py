# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Privilege(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        actions: str = None,
        gmt_create: str = None,
        id: int = None,
        request_id: str = None,
        resource: str = None,
        role_id: int = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        # This parameter is required.
        self.actions = actions
        self.gmt_create = gmt_create
        self.id = id
        self.request_id = request_id
        # This parameter is required.
        self.resource = resource
        # This parameter is required.
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

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.id is not None:
            result['id'] = self.id

        if self.request_id is not None:
            result['requestId'] = self.request_id

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

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resource') is not None:
            self.resource = m.get('resource')

        if m.get('roleId') is not None:
            self.role_id = m.get('roleId')

        return self

