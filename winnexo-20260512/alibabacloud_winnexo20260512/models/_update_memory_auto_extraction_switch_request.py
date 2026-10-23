# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMemoryAutoExtractionSwitchRequest(DaraModel):
    def __init__(
        self,
        clear_existing: bool = None,
        enabled: bool = None,
        group_id: str = None,
        owner_type: str = None,
        tenant_id: str = None,
    ):
        # Specifies whether to synchronously clear the automatically collected memories. This parameter can be used regardless of whether the feature is enabled or disabled.
        self.clear_existing = clear_existing
        # Specifies whether to enable automatic memory collection.
        # 
        # This parameter is required.
        self.enabled = enabled
        # The collaborative workspace ID. This parameter is required when ownerType is set to group.
        self.group_id = group_id
        # The owner type. A value of user indicates personal memories of the authenticated user. A value of group indicates memories of a specified collaborative workspace.
        self.owner_type = owner_type
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clear_existing is not None:
            result['clearExisting'] = self.clear_existing

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.owner_type is not None:
            result['ownerType'] = self.owner_type

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clearExisting') is not None:
            self.clear_existing = m.get('clearExisting')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('ownerType') is not None:
            self.owner_type = m.get('ownerType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

