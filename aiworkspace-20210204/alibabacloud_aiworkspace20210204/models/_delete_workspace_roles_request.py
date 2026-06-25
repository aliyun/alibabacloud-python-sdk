# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteWorkspaceRolesRequest(DaraModel):
    def __init__(
        self,
        role_ids: List[str] = None,
    ):
        # The IDs of the roles to delete.
        self.role_ids = role_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_ids is not None:
            result['RoleIds'] = self.role_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleIds') is not None:
            self.role_ids = m.get('RoleIds')

        return self

