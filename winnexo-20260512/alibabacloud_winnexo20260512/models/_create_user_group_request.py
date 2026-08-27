# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserGroupRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        parent_id: str = None,
        tenant_id: str = None,
        user_group_name: str = None,
    ):
        # The description of the user group.
        self.description = description
        # The ID of the parent user group. If this parameter is not specified, a root node is created.
        self.parent_id = parent_id
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The name of the user group. The name must be unique under the same parent node.
        # 
        # This parameter is required.
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

        if self.parent_id is not None:
            result['parentId'] = self.parent_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_group_name is not None:
            result['userGroupName'] = self.user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userGroupName') is not None:
            self.user_group_name = m.get('userGroupName')

        return self

