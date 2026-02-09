# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportMappCenterAppConfigRequest(DaraModel):
    def __init__(
        self,
        apk_file_url: str = None,
        app_id: str = None,
        cert_rsa_base_64: str = None,
        identifier: str = None,
        onex_flag: bool = None,
        system_type: str = None,
        workspace_id: str = None,
    ):
        self.apk_file_url = apk_file_url
        self.app_id = app_id
        self.cert_rsa_base_64 = cert_rsa_base_64
        # This parameter is required.
        self.identifier = identifier
        # This parameter is required.
        self.onex_flag = onex_flag
        # This parameter is required.
        self.system_type = system_type
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apk_file_url is not None:
            result['ApkFileUrl'] = self.apk_file_url

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cert_rsa_base_64 is not None:
            result['CertRsaBase64'] = self.cert_rsa_base_64

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag

        if self.system_type is not None:
            result['SystemType'] = self.system_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApkFileUrl') is not None:
            self.apk_file_url = m.get('ApkFileUrl')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CertRsaBase64') is not None:
            self.cert_rsa_base_64 = m.get('CertRsaBase64')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')

        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

