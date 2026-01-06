# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMeetingRoomGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        parent_group_id: int = None,
        tenant_context_shrink: str = None,
    ):
        self.group_name = group_name
        # This parameter is required.
        self.parent_group_id = parent_group_id
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.parent_group_id is not None:
            result['ParentGroupId'] = self.parent_group_id

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ParentGroupId') is not None:
            self.parent_group_id = m.get('ParentGroupId')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

