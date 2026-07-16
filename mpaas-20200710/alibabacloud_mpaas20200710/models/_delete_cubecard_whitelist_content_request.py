# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCubecardWhitelistContentRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        tenant_id: str = None,
        whitelist_id: str = None,
        whitelist_value: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.tenant_id = tenant_id
        self.whitelist_id = whitelist_id
        self.whitelist_value = whitelist_value
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

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.whitelist_id is not None:
            result['WhitelistId'] = self.whitelist_id

        if self.whitelist_value is not None:
            result['WhitelistValue'] = self.whitelist_value

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('WhitelistId') is not None:
            self.whitelist_id = m.get('WhitelistId')

        if m.get('WhitelistValue') is not None:
            self.whitelist_value = m.get('WhitelistValue')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

