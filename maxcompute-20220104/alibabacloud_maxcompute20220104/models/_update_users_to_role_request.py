# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateUsersToRoleRequest(DaraModel):
    def __init__(
        self,
        add: List[str] = None,
        remove: List[str] = None,
    ):
        # The action to add users to the project role.
        self.add = add
        # The action to remove users from the project role.
        self.remove = remove

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add is not None:
            result['add'] = self.add

        if self.remove is not None:
            result['remove'] = self.remove

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('add') is not None:
            self.add = m.get('add')

        if m.get('remove') is not None:
            self.remove = m.get('remove')

        return self

