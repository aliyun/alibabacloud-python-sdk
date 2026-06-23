# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMcubeWhitelistRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        tenant_id: str = None,
        white_list_name: str = None,
        whitelist_type: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.white_list_name = white_list_name
        # This parameter is required.
        self.whitelist_type = whitelist_type
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

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.white_list_name is not None:
            result['WhiteListName'] = self.white_list_name

        if self.whitelist_type is not None:
            result['WhitelistType'] = self.whitelist_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('WhiteListName') is not None:
            self.white_list_name = m.get('WhiteListName')

        if m.get('WhitelistType') is not None:
            self.whitelist_type = m.get('WhitelistType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

