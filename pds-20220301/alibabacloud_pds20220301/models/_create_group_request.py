# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGroupRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        group_name: str = None,
        is_root: bool = None,
        parent_group_id: str = None,
    ):
        # The description of the group. The description can be up to 1,024 characters in length.
        self.description = description
        # The name of the group. The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.group_name = group_name
        # Specifies whether the group is a root group. A root group cannot be added to any other group. In most cases, a root group is the top-level organization in the organizational structure.
        self.is_root = is_root
        # The ID of the parent group to which the group is added. If this parameter is specified, the system automatically adds the group to the specified parent group after the group is created.
        self.parent_group_id = parent_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.group_name is not None:
            result['group_name'] = self.group_name

        if self.is_root is not None:
            result['is_root'] = self.is_root

        if self.parent_group_id is not None:
            result['parent_group_id'] = self.parent_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')

        if m.get('is_root') is not None:
            self.is_root = m.get('is_root')

        if m.get('parent_group_id') is not None:
            self.parent_group_id = m.get('parent_group_id')

        return self

