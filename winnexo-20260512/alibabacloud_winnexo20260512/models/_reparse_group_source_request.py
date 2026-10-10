# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReparseGroupSourceRequest(DaraModel):
    def __init__(
        self,
        force_sync: bool = None,
        group_id: str = None,
        source_id: str = None,
        tenant_id: str = None,
    ):
        # Specifies whether to synchronously wait for the re-parsing to complete. Default value: false, which indicates that the request is asynchronously queued.
        self.force_sync = force_sync
        # The project group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The unique identifier on the business system side, which is the business ID.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The tenant ID. This is a common parameter. In winnexo-cli, pass this parameter explicitly by using --tenant-id.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force_sync is not None:
            result['forceSync'] = self.force_sync

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('forceSync') is not None:
            self.force_sync = m.get('forceSync')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

