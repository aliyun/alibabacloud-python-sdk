# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckHealthResponseBody(DaraModel):
    def __init__(
        self,
        auth_source: str = None,
        caller_type: str = None,
        code: str = None,
        digital_employee_name: str = None,
        message: str = None,
        request_id: str = None,
        tenant_id: int = None,
        user_id: int = None,
    ):
        # 认证来源: bearer / aliyun_gateway
        self.auth_source = auth_source
        self.caller_type = caller_type
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 当前请求生效的数字员工名（运营对象）；未传且租户下无数字员工时为空
        self.digital_employee_name = digital_employee_name
        # 错误描述，成功时为空
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id
        # 生效租户ID
        self.tenant_id = tenant_id
        # 平台用户ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_source is not None:
            result['authSource'] = self.auth_source

        if self.caller_type is not None:
            result['callerType'] = self.caller_type

        if self.code is not None:
            result['code'] = self.code

        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authSource') is not None:
            self.auth_source = m.get('authSource')

        if m.get('callerType') is not None:
            self.caller_type = m.get('callerType')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

