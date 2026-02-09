# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadUserAppToMsaRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        file_name: str = None,
        file_url: str = None,
        tenant_id: str = None,
        use_yshield: bool = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.file_name = file_name
        self.file_url = file_url
        # This parameter is required.
        self.tenant_id = tenant_id
        self.use_yshield = use_yshield
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

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.use_yshield is not None:
            result['UseYShield'] = self.use_yshield

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UseYShield') is not None:
            self.use_yshield = m.get('UseYShield')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

