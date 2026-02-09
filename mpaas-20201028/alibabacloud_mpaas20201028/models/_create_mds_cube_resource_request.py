# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMdsCubeResourceRequest(DaraModel):
    def __init__(
        self,
        android_max_version: str = None,
        android_min_version: str = None,
        app_id: str = None,
        extend_info: str = None,
        file_url: str = None,
        ios_max_version: str = None,
        ios_min_version: str = None,
        mock_data_url: str = None,
        onex_flag: bool = None,
        platform: str = None,
        preview_picture_url: str = None,
        template_id: str = None,
        template_resource_desc: str = None,
        template_resource_version: str = None,
        tenant_id: str = None,
        workspace_id: str = None,
    ):
        self.android_max_version = android_max_version
        self.android_min_version = android_min_version
        self.app_id = app_id
        self.extend_info = extend_info
        self.file_url = file_url
        self.ios_max_version = ios_max_version
        self.ios_min_version = ios_min_version
        self.mock_data_url = mock_data_url
        self.onex_flag = onex_flag
        self.platform = platform
        self.preview_picture_url = preview_picture_url
        self.template_id = template_id
        self.template_resource_desc = template_resource_desc
        self.template_resource_version = template_resource_version
        self.tenant_id = tenant_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_max_version is not None:
            result['AndroidMaxVersion'] = self.android_max_version

        if self.android_min_version is not None:
            result['AndroidMinVersion'] = self.android_min_version

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.ios_max_version is not None:
            result['IosMaxVersion'] = self.ios_max_version

        if self.ios_min_version is not None:
            result['IosMinVersion'] = self.ios_min_version

        if self.mock_data_url is not None:
            result['MockDataUrl'] = self.mock_data_url

        if self.onex_flag is not None:
            result['OnexFlag'] = self.onex_flag

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.preview_picture_url is not None:
            result['PreviewPictureUrl'] = self.preview_picture_url

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_resource_desc is not None:
            result['TemplateResourceDesc'] = self.template_resource_desc

        if self.template_resource_version is not None:
            result['TemplateResourceVersion'] = self.template_resource_version

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidMaxVersion') is not None:
            self.android_max_version = m.get('AndroidMaxVersion')

        if m.get('AndroidMinVersion') is not None:
            self.android_min_version = m.get('AndroidMinVersion')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('IosMaxVersion') is not None:
            self.ios_max_version = m.get('IosMaxVersion')

        if m.get('IosMinVersion') is not None:
            self.ios_min_version = m.get('IosMinVersion')

        if m.get('MockDataUrl') is not None:
            self.mock_data_url = m.get('MockDataUrl')

        if m.get('OnexFlag') is not None:
            self.onex_flag = m.get('OnexFlag')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('PreviewPictureUrl') is not None:
            self.preview_picture_url = m.get('PreviewPictureUrl')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateResourceDesc') is not None:
            self.template_resource_desc = m.get('TemplateResourceDesc')

        if m.get('TemplateResourceVersion') is not None:
            self.template_resource_version = m.get('TemplateResourceVersion')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

