# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadBitcodeToMsaRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        bitcode: str = None,
        code_version: str = None,
        license: str = None,
        tenant_id: str = None,
        type: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.bitcode = bitcode
        self.code_version = code_version
        self.license = license
        # This parameter is required.
        self.tenant_id = tenant_id
        self.type = type
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

        if self.bitcode is not None:
            result['Bitcode'] = self.bitcode

        if self.code_version is not None:
            result['CodeVersion'] = self.code_version

        if self.license is not None:
            result['License'] = self.license

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

        if m.get('Bitcode') is not None:
            self.bitcode = m.get('Bitcode')

        if m.get('CodeVersion') is not None:
            self.code_version = m.get('CodeVersion')

        if m.get('License') is not None:
            self.license = m.get('License')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

