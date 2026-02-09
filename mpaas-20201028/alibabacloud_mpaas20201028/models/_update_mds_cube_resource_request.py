# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMdsCubeResourceRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        mock_data_url: str = None,
        onex_flag: bool = None,
        template_resource_id: int = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.mock_data_url = mock_data_url
        # This parameter is required.
        self.onex_flag = onex_flag
        # This parameter is required.
        self.template_resource_id = template_resource_id
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

        if self.mock_data_url is not None:
            result['MockDataUrl'] = self.mock_data_url

        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag

        if self.template_resource_id is not None:
            result['TemplateResourceId'] = self.template_resource_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('MockDataUrl') is not None:
            self.mock_data_url = m.get('MockDataUrl')

        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')

        if m.get('TemplateResourceId') is not None:
            self.template_resource_id = m.get('TemplateResourceId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

