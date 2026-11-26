# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTodoRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        message_id: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        tenant_id: str = None,
        todo_id: str = None,
        work_item_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The ID of the assistant message. This parameter is used to query multiple to-do items by message.
        self.message_id = message_id
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The tenant ID. This is a common parameter. If this parameter is not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The ID of the to-do item (get).
        self.todo_id = todo_id
        # The ID of the work item. This parameter is used to query multiple to-do items by source.
        self.work_item_id = work_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.todo_id is not None:
            result['todoId'] = self.todo_id

        if self.work_item_id is not None:
            result['workItemId'] = self.work_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('todoId') is not None:
            self.todo_id = m.get('todoId')

        if m.get('workItemId') is not None:
            self.work_item_id = m.get('workItemId')

        return self

