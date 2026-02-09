# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMpaasAppInfoRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        icon_file_url: str = None,
        identifier: str = None,
        onex_flag: bool = None,
        system_type: str = None,
        tenant_id: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.icon_file_url = icon_file_url
        self.identifier = identifier
        self.onex_flag = onex_flag
        self.system_type = system_type
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.icon_file_url is not None:
            result['IconFileUrl'] = self.icon_file_url

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag

        if self.system_type is not None:
            result['SystemType'] = self.system_type

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('IconFileUrl') is not None:
            self.icon_file_url = m.get('IconFileUrl')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')

        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

