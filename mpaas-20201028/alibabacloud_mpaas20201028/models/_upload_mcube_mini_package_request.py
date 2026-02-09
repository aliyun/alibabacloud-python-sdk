# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadMcubeMiniPackageRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        auto_install: int = None,
        client_version_max: str = None,
        client_version_min: str = None,
        enable_keep_alive: str = None,
        enable_option_menu: str = None,
        enable_tab_bar: int = None,
        extend_info: str = None,
        h_5id: str = None,
        h_5name: str = None,
        h_5version: str = None,
        icon_file_url: str = None,
        icon_url: str = None,
        install_type: int = None,
        main_url: str = None,
        onex_flag: bool = None,
        package_type: int = None,
        platform: str = None,
        resource_file_url: str = None,
        resource_type: int = None,
        tenant_id: str = None,
        user_id: str = None,
        uuid: str = None,
        vhost: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.auto_install = auto_install
        self.client_version_max = client_version_max
        # This parameter is required.
        self.client_version_min = client_version_min
        # This parameter is required.
        self.enable_keep_alive = enable_keep_alive
        # This parameter is required.
        self.enable_option_menu = enable_option_menu
        # This parameter is required.
        self.enable_tab_bar = enable_tab_bar
        self.extend_info = extend_info
        # This parameter is required.
        self.h_5id = h_5id
        # This parameter is required.
        self.h_5name = h_5name
        # This parameter is required.
        self.h_5version = h_5version
        self.icon_file_url = icon_file_url
        self.icon_url = icon_url
        # This parameter is required.
        self.install_type = install_type
        # This parameter is required.
        self.main_url = main_url
        # This parameter is required.
        self.onex_flag = onex_flag
        # This parameter is required.
        self.package_type = package_type
        # This parameter is required.
        self.platform = platform
        # This parameter is required.
        self.resource_file_url = resource_file_url
        # This parameter is required.
        self.resource_type = resource_type
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
        self.user_id = user_id
        self.uuid = uuid
        # This parameter is required.
        self.vhost = vhost
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

        if self.auto_install is not None:
            result['AutoInstall'] = self.auto_install

        if self.client_version_max is not None:
            result['ClientVersionMax'] = self.client_version_max

        if self.client_version_min is not None:
            result['ClientVersionMin'] = self.client_version_min

        if self.enable_keep_alive is not None:
            result['EnableKeepAlive'] = self.enable_keep_alive

        if self.enable_option_menu is not None:
            result['EnableOptionMenu'] = self.enable_option_menu

        if self.enable_tab_bar is not None:
            result['EnableTabBar'] = self.enable_tab_bar

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.h_5id is not None:
            result['H5Id'] = self.h_5id

        if self.h_5name is not None:
            result['H5Name'] = self.h_5name

        if self.h_5version is not None:
            result['H5Version'] = self.h_5version

        if self.icon_file_url is not None:
            result['IconFileUrl'] = self.icon_file_url

        if self.icon_url is not None:
            result['IconUrl'] = self.icon_url

        if self.install_type is not None:
            result['InstallType'] = self.install_type

        if self.main_url is not None:
            result['MainUrl'] = self.main_url

        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.resource_file_url is not None:
            result['ResourceFileUrl'] = self.resource_file_url

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

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

        if m.get('EnableKeepAlive') is not None:
            self.enable_keep_alive = m.get('EnableKeepAlive')

        if m.get('EnableOptionMenu') is not None:
            self.enable_option_menu = m.get('EnableOptionMenu')

        if m.get('EnableTabBar') is not None:
            self.enable_tab_bar = m.get('EnableTabBar')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('H5Id') is not None:
            self.h_5id = m.get('H5Id')

        if m.get('H5Name') is not None:
            self.h_5name = m.get('H5Name')

        if m.get('H5Version') is not None:
            self.h_5version = m.get('H5Version')

        if m.get('IconFileUrl') is not None:
            self.icon_file_url = m.get('IconFileUrl')

        if m.get('IconUrl') is not None:
            self.icon_url = m.get('IconUrl')

        if m.get('InstallType') is not None:
            self.install_type = m.get('InstallType')

        if m.get('MainUrl') is not None:
            self.main_url = m.get('MainUrl')

        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ResourceFileUrl') is not None:
            self.resource_file_url = m.get('ResourceFileUrl')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('Vhost') is not None:
            self.vhost = m.get('Vhost')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

