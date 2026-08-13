# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserResponseBody(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        code: str = None,
        display_name: str = None,
        is_new_user: bool = None,
        message: str = None,
        request_id: str = None,
        wn_user_id: str = None,
    ):
        # WINNEXO 登录账号
        self.account_id = account_id
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 用户显示名称
        self.display_name = display_name
        # 是否为新创建的用户（false 表示已有用户加入租户）
        self.is_new_user = is_new_user
        # 错误描述，成功时为空
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id
        # WINNEXO 平台用户ID
        self.wn_user_id = wn_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.code is not None:
            result['code'] = self.code

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.is_new_user is not None:
            result['isNewUser'] = self.is_new_user

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.wn_user_id is not None:
            result['wnUserId'] = self.wn_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('isNewUser') is not None:
            self.is_new_user = m.get('isNewUser')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('wnUserId') is not None:
            self.wn_user_id = m.get('wnUserId')

        return self

