# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMcubeHotpatchResourceRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        file_url: str = None,
        fix_desc: str = None,
        onex_flag: bool = None,
        platform: str = None,
        product_version: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.file_url = file_url
        self.fix_desc = fix_desc
        # This parameter is required.
        self.onex_flag = onex_flag
        # This parameter is required.
        self.platform = platform
        # This parameter is required.
        self.product_version = product_version
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

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.fix_desc is not None:
            result['FixDesc'] = self.fix_desc

        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.product_version is not None:
            result['ProductVersion'] = self.product_version

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('FixDesc') is not None:
            self.fix_desc = m.get('FixDesc')

        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProductVersion') is not None:
            self.product_version = m.get('ProductVersion')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

