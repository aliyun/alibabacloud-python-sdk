# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceExpireTimeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        found: bool = None,
        instance_expire_time: str = None,
        instance_id: str = None,
        instance_status: str = None,
        message: str = None,
        request_id: str = None,
        tenant_id: int = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 是否找到标准包实例
        self.found = found
        # 实例过期时间（ISO格式）
        self.instance_expire_time = instance_expire_time
        # 实例ID
        self.instance_id = instance_id
        # 实例状态
        self.instance_status = instance_status
        # 错误描述，成功时为空
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id
        # 系统租户ID
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.found is not None:
            result['found'] = self.found

        if self.instance_expire_time is not None:
            result['instanceExpireTime'] = self.instance_expire_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_status is not None:
            result['instanceStatus'] = self.instance_status

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('found') is not None:
            self.found = m.get('found')

        if m.get('instanceExpireTime') is not None:
            self.instance_expire_time = m.get('instanceExpireTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceStatus') is not None:
            self.instance_status = m.get('instanceStatus')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

