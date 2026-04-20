# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddWorksAuthorizationRequest(DaraModel):
    def __init__(
        self,
        auth_points: int = None,
        authorize_scope: int = None,
        authorized_id: str = None,
        expire_day: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # This parameter is required.
        self.auth_points = auth_points
        # This parameter is required.
        self.authorize_scope = authorize_scope
        # This parameter is required.
        self.authorized_id = authorized_id
        self.expire_day = expire_day
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_points is not None:
            result['AuthPoints'] = self.auth_points

        if self.authorize_scope is not None:
            result['AuthorizeScope'] = self.authorize_scope

        if self.authorized_id is not None:
            result['AuthorizedId'] = self.authorized_id

        if self.expire_day is not None:
            result['ExpireDay'] = self.expire_day

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthPoints') is not None:
            self.auth_points = m.get('AuthPoints')

        if m.get('AuthorizeScope') is not None:
            self.authorize_scope = m.get('AuthorizeScope')

        if m.get('AuthorizedId') is not None:
            self.authorized_id = m.get('AuthorizedId')

        if m.get('ExpireDay') is not None:
            self.expire_day = m.get('ExpireDay')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

