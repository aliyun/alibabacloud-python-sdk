# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReplaceManualMemoryRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        group_id: str = None,
        owner_type: str = None,
        tenant_id: str = None,
    ):
        # The complete content of profile.md. An empty string indicates that the memory is cleared. This field is required, but an empty value is allowed.
        # 
        # This parameter is required.
        self.content = content
        # The workspace ID. This parameter is required when ownerType is set to group.
        self.group_id = group_id
        # The owner type. A value of user indicates the personal memory of the authenticated user. A value of group indicates the memory of a specified workspace.
        self.owner_type = owner_type
        # The tenant ID. This is a common parameter. If this parameter is not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.owner_type is not None:
            result['ownerType'] = self.owner_type

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('ownerType') is not None:
            self.owner_type = m.get('ownerType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

