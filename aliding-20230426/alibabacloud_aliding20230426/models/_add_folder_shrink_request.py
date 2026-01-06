# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddFolderShrinkRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        option_shrink: str = None,
        parent_id: str = None,
        space_id: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.name = name
        self.option_shrink = option_shrink
        # This parameter is required.
        self.parent_id = parent_id
        # This parameter is required.
        self.space_id = space_id
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.option_shrink is not None:
            result['Option'] = self.option_shrink

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Option') is not None:
            self.option_shrink = m.get('Option')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

