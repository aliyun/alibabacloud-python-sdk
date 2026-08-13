# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomOrgResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        corp_id: str = None,
        corp_name: str = None,
        message: str = None,
        platform_type: str = None,
        request_id: str = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 注册成功的组织标识
        self.corp_id = corp_id
        # 组织展示名称
        self.corp_name = corp_name
        # 错误描述，成功时为空
        self.message = message
        # 平台类型，固定为 custom
        self.platform_type = platform_type
        # 请求追踪 ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.corp_id is not None:
            result['corpId'] = self.corp_id

        if self.corp_name is not None:
            result['corpName'] = self.corp_name

        if self.message is not None:
            result['message'] = self.message

        if self.platform_type is not None:
            result['platformType'] = self.platform_type

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')

        if m.get('corpName') is not None:
            self.corp_name = m.get('corpName')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('platformType') is not None:
            self.platform_type = m.get('platformType')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

