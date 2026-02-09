# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMgsApirestRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        format: str = None,
        id: int = None,
        tenant_id: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.format = format
        self.id = id
        self.tenant_id = tenant_id
        self.type = type
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

        if self.format is not None:
            result['Format'] = self.format

        if self.id is not None:
            result['Id'] = self.id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.type is not None:
            result['Type'] = self.type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

