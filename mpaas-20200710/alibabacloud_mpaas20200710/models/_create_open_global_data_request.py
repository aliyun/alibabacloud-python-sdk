# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOpenGlobalDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_max_version: str = None,
        app_min_version: str = None,
        biz_type: str = None,
        ext_attr_str: str = None,
        max_uid: int = None,
        min_uid: int = None,
        os_type: str = None,
        payload: str = None,
        tenant_id: str = None,
        third_msg_id: str = None,
        uids: str = None,
        valid_time_end: int = None,
        valid_time_start: int = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.app_max_version = app_max_version
        self.app_min_version = app_min_version
        # This parameter is required.
        self.biz_type = biz_type
        self.ext_attr_str = ext_attr_str
        self.max_uid = max_uid
        self.min_uid = min_uid
        self.os_type = os_type
        # This parameter is required.
        self.payload = payload
        self.tenant_id = tenant_id
        # This parameter is required.
        self.third_msg_id = third_msg_id
        self.uids = uids
        self.valid_time_end = valid_time_end
        self.valid_time_start = valid_time_start
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

        if self.app_max_version is not None:
            result['AppMaxVersion'] = self.app_max_version

        if self.app_min_version is not None:
            result['AppMinVersion'] = self.app_min_version

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.ext_attr_str is not None:
            result['ExtAttrStr'] = self.ext_attr_str

        if self.max_uid is not None:
            result['MaxUid'] = self.max_uid

        if self.min_uid is not None:
            result['MinUid'] = self.min_uid

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.payload is not None:
            result['Payload'] = self.payload

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.third_msg_id is not None:
            result['ThirdMsgId'] = self.third_msg_id

        if self.uids is not None:
            result['Uids'] = self.uids

        if self.valid_time_end is not None:
            result['ValidTimeEnd'] = self.valid_time_end

        if self.valid_time_start is not None:
            result['ValidTimeStart'] = self.valid_time_start

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppMaxVersion') is not None:
            self.app_max_version = m.get('AppMaxVersion')

        if m.get('AppMinVersion') is not None:
            self.app_min_version = m.get('AppMinVersion')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ExtAttrStr') is not None:
            self.ext_attr_str = m.get('ExtAttrStr')

        if m.get('MaxUid') is not None:
            self.max_uid = m.get('MaxUid')

        if m.get('MinUid') is not None:
            self.min_uid = m.get('MinUid')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('Payload') is not None:
            self.payload = m.get('Payload')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('ThirdMsgId') is not None:
            self.third_msg_id = m.get('ThirdMsgId')

        if m.get('Uids') is not None:
            self.uids = m.get('Uids')

        if m.get('ValidTimeEnd') is not None:
            self.valid_time_end = m.get('ValidTimeEnd')

        if m.get('ValidTimeStart') is not None:
            self.valid_time_start = m.get('ValidTimeStart')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

