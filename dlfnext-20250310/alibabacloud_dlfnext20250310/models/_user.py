# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class User(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        display_name: str = None,
        type: str = None,
        updated_at: int = None,
        updated_by: str = None,
        user_id: str = None,
        user_name: str = None,
        user_principal: str = None,
    ):
        self.created_at = created_at
        self.created_by = created_by
        self.display_name = display_name
        self.type = type
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.user_id = user_id
        self.user_name = user_name
        self.user_principal = user_principal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.type is not None:
            result['type'] = self.type

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.user_name is not None:
            result['userName'] = self.user_name

        if self.user_principal is not None:
            result['userPrincipal'] = self.user_principal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        if m.get('userPrincipal') is not None:
            self.user_principal = m.get('userPrincipal')

        return self

