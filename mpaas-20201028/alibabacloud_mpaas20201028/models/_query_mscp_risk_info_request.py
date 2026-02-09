# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMscpRiskInfoRequest(DaraModel):
    def __init__(
        self,
        apdid_token: str = None,
        app_id: str = None,
        tenant_id: str = None,
        terminal_type: str = None,
        workspace_id: str = None,
    ):
        # ApdidToken
        self.apdid_token = apdid_token
        # AppId
        self.app_id = app_id
        # TenantId
        self.tenant_id = tenant_id
        # TerminalType
        self.terminal_type = terminal_type
        # WorkspaceId
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apdid_token is not None:
            result['ApdidToken'] = self.apdid_token

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.terminal_type is not None:
            result['TerminalType'] = self.terminal_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApdidToken') is not None:
            self.apdid_token = m.get('ApdidToken')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TerminalType') is not None:
            self.terminal_type = m.get('TerminalType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

