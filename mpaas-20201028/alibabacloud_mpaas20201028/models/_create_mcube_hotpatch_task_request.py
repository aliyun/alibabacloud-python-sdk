# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMcubeHotpatchTaskRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        grey_config_info: str = None,
        grey_endtime_data: str = None,
        grey_num: int = None,
        memo: str = None,
        package_id: int = None,
        platform: str = None,
        publish_mode: int = None,
        publish_type: int = None,
        sync_mode: str = None,
        tenant_id: str = None,
        whitelist_ids: str = None,
        workspace_id: str = None,
    ):
        self.app_id = app_id
        self.grey_config_info = grey_config_info
        self.grey_endtime_data = grey_endtime_data
        self.grey_num = grey_num
        self.memo = memo
        # This parameter is required.
        self.package_id = package_id
        self.platform = platform
        self.publish_mode = publish_mode
        self.publish_type = publish_type
        self.sync_mode = sync_mode
        self.tenant_id = tenant_id
        self.whitelist_ids = whitelist_ids
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

        if self.grey_config_info is not None:
            result['GreyConfigInfo'] = self.grey_config_info

        if self.grey_endtime_data is not None:
            result['GreyEndtimeData'] = self.grey_endtime_data

        if self.grey_num is not None:
            result['GreyNum'] = self.grey_num

        if self.memo is not None:
            result['Memo'] = self.memo

        if self.package_id is not None:
            result['PackageId'] = self.package_id

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.publish_mode is not None:
            result['PublishMode'] = self.publish_mode

        if self.publish_type is not None:
            result['PublishType'] = self.publish_type

        if self.sync_mode is not None:
            result['SyncMode'] = self.sync_mode

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.whitelist_ids is not None:
            result['WhitelistIds'] = self.whitelist_ids

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('GreyConfigInfo') is not None:
            self.grey_config_info = m.get('GreyConfigInfo')

        if m.get('GreyEndtimeData') is not None:
            self.grey_endtime_data = m.get('GreyEndtimeData')

        if m.get('GreyNum') is not None:
            self.grey_num = m.get('GreyNum')

        if m.get('Memo') is not None:
            self.memo = m.get('Memo')

        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('PublishMode') is not None:
            self.publish_mode = m.get('PublishMode')

        if m.get('PublishType') is not None:
            self.publish_type = m.get('PublishType')

        if m.get('SyncMode') is not None:
            self.sync_mode = m.get('SyncMode')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('WhitelistIds') is not None:
            self.whitelist_ids = m.get('WhitelistIds')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

