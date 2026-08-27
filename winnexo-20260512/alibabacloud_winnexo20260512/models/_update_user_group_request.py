# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserGroupRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        move_to_root: bool = None,
        parent_id: str = None,
        tenant_id: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        # The new description of the user group. If not specified, the description is not modified.
        self.description = description
        # Specifies whether to move the user group to the root node. This parameter cannot be set together with parentId.
        self.move_to_root = move_to_root
        # The ID of the new parent user group. If not specified, the user group is not moved.
        self.parent_id = parent_id
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The ID of the target user group.
        # 
        # This parameter is required.
        self.user_group_id = user_group_id
        # The new name of the user group. If not specified, the name is not modified.
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.move_to_root is not None:
            result['moveToRoot'] = self.move_to_root

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_group_id is not None:
            result['userGroupId'] = self.user_group_id

        if self.user_group_name is not None:
            result['userGroupName'] = self.user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('moveToRoot') is not None:
            self.move_to_root = m.get('moveToRoot')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userGroupId') is not None:
            self.user_group_id = m.get('userGroupId')

        if m.get('userGroupName') is not None:
            self.user_group_name = m.get('userGroupName')

        return self

