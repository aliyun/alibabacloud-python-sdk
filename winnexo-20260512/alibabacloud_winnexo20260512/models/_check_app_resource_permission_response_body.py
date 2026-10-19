# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckAppResourcePermissionResponseBody(DaraModel):
    def __init__(
        self,
        allowed: bool = None,
        code: str = None,
        message: str = None,
        permission: str = None,
        request_id: str = None,
        resource_key: str = None,
        resource_type: str = None,
    ):
        # 目标用户是否拥有该资源权限
        self.allowed = allowed
        # 业务状态码；成功为 200
        self.code = code
        # 错误描述；成功时为空
        self.message = message
        # 目标权限点
        self.permission = permission
        # 请求追踪 ID
        self.request_id = request_id
        # 首段为 APP 应用键的点分资源键
        self.resource_key = resource_key
        # 固定为 APP_RESOURCE
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed is not None:
            result['allowed'] = self.allowed

        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.permission is not None:
            result['permission'] = self.permission

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.resource_key is not None:
            result['resourceKey'] = self.resource_key

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowed') is not None:
            self.allowed = m.get('allowed')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('permission') is not None:
            self.permission = m.get('permission')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resourceKey') is not None:
            self.resource_key = m.get('resourceKey')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

