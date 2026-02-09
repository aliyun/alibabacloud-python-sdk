# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMcubeWhitelistRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        id: str = None,
        key_ids: str = None,
        onex_flag: bool = None,
        oss_url: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.id = id
        self.key_ids = key_ids
        # This parameter is required.
        self.onex_flag = onex_flag
        self.oss_url = oss_url
        # This parameter is required.
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

        if self.id is not None:
            result['Id'] = self.id

        if self.key_ids is not None:
            result['KeyIds'] = self.key_ids

        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag

        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('KeyIds') is not None:
            self.key_ids = m.get('KeyIds')

        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')

        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

