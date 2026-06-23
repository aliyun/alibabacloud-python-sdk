# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMcubeNebulaResourceRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        auto_install: int = None,
        client_version_max: str = None,
        client_version_min: str = None,
        custom_domain_name: str = None,
        extend_info: str = None,
        file_url: str = None,
        h_5id: str = None,
        h_5name: str = None,
        h_5version: str = None,
        install_type: int = None,
        main_url: str = None,
        onex_flag: bool = None,
        platform: str = None,
        repeat_nebula: int = None,
        resource_type: int = None,
        sub_url: str = None,
        tenant_id: str = None,
        vhost: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.auto_install = auto_install
        self.client_version_max = client_version_max
        self.client_version_min = client_version_min
        self.custom_domain_name = custom_domain_name
        self.extend_info = extend_info
        self.file_url = file_url
        self.h_5id = h_5id
        self.h_5name = h_5name
        self.h_5version = h_5version
        self.install_type = install_type
        self.main_url = main_url
        self.onex_flag = onex_flag
        self.platform = platform
        self.repeat_nebula = repeat_nebula
        self.resource_type = resource_type
        self.sub_url = sub_url
        self.tenant_id = tenant_id
        self.vhost = vhost
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

        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install

        if self.client_version_max is not None:
            result['ClientVersionMax'] = self.client_version_max

        if self.client_version_min is not None:
            result['ClientVersionMin'] = self.client_version_min

        if self.custom_domain_name is not None:
            result['CustomDomainName'] = self.custom_domain_name

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.h_5id is not None:
            result['H5Id'] = self.h_5id

        if self.h_5name is not None:
            result['H5Name'] = self.h_5name

        if self.h_5version is not None:
            result['H5Version'] = self.h_5version

        if self.install_type is not None:
            result['InstallType'] = self.install_type

        if self.main_url is not None:
            result['MainUrl'] = self.main_url

        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.repeat_nebula is not None:
            result['RepeatNebula'] = self.repeat_nebula

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.sub_url is not None:
            result['SubUrl'] = self.sub_url

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.vhost is not None:
            result['Vhost'] = self.vhost

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AutoInstall') is not None:
            self.auto_install = m.get('AutoInstall')

        if m.get('ClientVersionMax') is not None:
            self.client_version_max = m.get('ClientVersionMax')

        if m.get('ClientVersionMin') is not None:
            self.client_version_min = m.get('ClientVersionMin')

        if m.get('CustomDomainName') is not None:
            self.custom_domain_name = m.get('CustomDomainName')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')

        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')

        if m.get('H5Version') is not None:
            self.h_5version = m.get('H5Version')

        if m.get('InstallType') is not None:
            self.install_type = m.get('InstallType')

        if m.get('MainUrl') is not None:
            self.main_url = m.get('MainUrl')

        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RepeatNebula') is not None:
            self.repeat_nebula = m.get('RepeatNebula')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SubUrl') is not None:
            self.sub_url = m.get('SubUrl')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Vhost') is not None:
            self.vhost = m.get('Vhost')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

