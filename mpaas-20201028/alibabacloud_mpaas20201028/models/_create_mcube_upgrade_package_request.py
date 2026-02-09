# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMcubeUpgradePackageRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_version: str = None,
        appstore_url: str = None,
        bundle_id: str = None,
        custom_domain_name: str = None,
        desc: str = None,
        download_url: str = None,
        file_url: str = None,
        harmony_label: str = None,
        icon_file_url: str = None,
        install_amount: int = None,
        ios_symbolfile_url: str = None,
        is_enterprise: int = None,
        large_icon_url: str = None,
        need_check: int = None,
        onex_flag: bool = None,
        platform: str = None,
        tenant_id: str = None,
        valid_days: int = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.app_version = app_version
        self.appstore_url = appstore_url
        self.bundle_id = bundle_id
        self.custom_domain_name = custom_domain_name
        self.desc = desc
        self.download_url = download_url
        self.file_url = file_url
        self.harmony_label = harmony_label
        self.icon_file_url = icon_file_url
        self.install_amount = install_amount
        self.ios_symbolfile_url = ios_symbolfile_url
        self.is_enterprise = is_enterprise
        self.large_icon_url = large_icon_url
        self.need_check = need_check
        self.onex_flag = onex_flag
        self.platform = platform
        self.tenant_id = tenant_id
        self.valid_days = valid_days
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

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.appstore_url is not None:
            result['AppstoreUrl'] = self.appstore_url

        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        if self.custom_domain_name is not None:
            result['CustomDomainName'] = self.custom_domain_name

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.harmony_label is not None:
            result['HarmonyLabel'] = self.harmony_label

        if self.icon_file_url is not None:
            result['IconFileUrl'] = self.icon_file_url

        if self.install_amount is not None:
            result['InstallAmount'] = self.install_amount

        if self.ios_symbolfile_url is not None:
            result['IosSymbolfileUrl'] = self.ios_symbolfile_url

        if self.is_enterprise is not None:
            result['IsEnterprise'] = self.is_enterprise

        if self.large_icon_url is not None:
            result['LargeIconUrl'] = self.large_icon_url

        if self.need_check is not None:
            result['NeedCheck'] = self.need_check

        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.valid_days is not None:
            result['ValidDays'] = self.valid_days

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('AppstoreUrl') is not None:
            self.appstore_url = m.get('AppstoreUrl')

        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        if m.get('CustomDomainName') is not None:
            self.custom_domain_name = m.get('CustomDomainName')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('HarmonyLabel') is not None:
            self.harmony_label = m.get('HarmonyLabel')

        if m.get('IconFileUrl') is not None:
            self.icon_file_url = m.get('IconFileUrl')

        if m.get('InstallAmount') is not None:
            self.install_amount = m.get('InstallAmount')

        if m.get('IosSymbolfileUrl') is not None:
            self.ios_symbolfile_url = m.get('IosSymbolfileUrl')

        if m.get('IsEnterprise') is not None:
            self.is_enterprise = m.get('IsEnterprise')

        if m.get('LargeIconUrl') is not None:
            self.large_icon_url = m.get('LargeIconUrl')

        if m.get('NeedCheck') is not None:
            self.need_check = m.get('NeedCheck')

        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('ValidDays') is not None:
            self.valid_days = m.get('ValidDays')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

