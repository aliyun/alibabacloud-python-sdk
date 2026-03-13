# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddEmployeesToCustomRoleShrinkRequest(DaraModel):
    def __init__(
        self,
        role_id: str = None,
        user_id_list_shrink: str = None,
    ):
        # This parameter is required.
        self.role_id = role_id
        # This parameter is required.
        self.user_id_list_shrink = user_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_id is not None:
            result['role_id'] = self.role_id

        if self.user_id_list_shrink is not None:
            result['user_id_list'] = self.user_id_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')

        if m.get('user_id_list') is not None:
            self.user_id_list_shrink = m.get('user_id_list')

        return self

