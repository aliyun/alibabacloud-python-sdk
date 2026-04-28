# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGroupRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
    ):
        # The description of the group after modification.
        self.description = description
        # The ID of the group that you want to modify.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The name of the group after modification.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.group_id is not None:
            result['group_id'] = self.group_id

        if self.group_name is not None:
            result['group_name'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')

        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')

        return self

