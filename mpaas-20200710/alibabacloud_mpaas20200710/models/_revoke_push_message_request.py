# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokePushMessageRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        message_id: str = None,
        target_id: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.message_id = message_id
        # This parameter is required.
        self.target_id = target_id
        self.tenant_id = tenant_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

