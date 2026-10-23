# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClearAutoMemoryRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        owner_type: str = None,
        tenant_id: str = None,
        type: str = None,
    ):
        # The workspace ID. This parameter is required when ownerType is set to group.
        self.group_id = group_id
        # The owner type. Valid values:
        # - user: the personal memory of the authenticated user.
        # - group: the memory of a specified workspace.
        self.owner_type = owner_type
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The memory type. Valid values: user, feedback, reference, project, and all. A value of all does not clear manual memory.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.owner_type is not None:
            result['ownerType'] = self.owner_type

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('ownerType') is not None:
            self.owner_type = m.get('ownerType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

