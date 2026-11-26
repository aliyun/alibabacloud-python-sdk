# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitTodoShrinkRequest(DaraModel):
    def __init__(
        self,
        answers_shrink: str = None,
        app_token: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        tenant_id: str = None,
        todo_id: str = None,
    ):
        # The answer array. The original text of the question must align with the to-do question.
        # 
        # This parameter is required.
        self.answers_shrink = answers_shrink
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The to-do task ID.
        self.tenant_id = tenant_id
        # The answer array. The original text of the question must align with the to-do question.
        # 
        # This parameter is required.
        self.todo_id = todo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answers_shrink is not None:
            result['answers'] = self.answers_shrink

        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.todo_id is not None:
            result['todoId'] = self.todo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answers') is not None:
            self.answers_shrink = m.get('answers')

        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('todoId') is not None:
            self.todo_id = m.get('todoId')

        return self

