# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecommendNextActionsRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        custom_prompt: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        output_type: str = None,
        recent_message_count: int = None,
        session_id: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The extraction instruction.
        self.custom_prompt = custom_prompt
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The output type: `conversation/skill/task`.
        self.output_type = output_type
        # The number of recent messages used to assemble the contextual information.
        self.recent_message_count = recent_message_count
        # The session ID to filter by. If specified, returns all Active/Expired status information associated with this session.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The tenant ID. This is a common parameter. In winnexo-cli, pass this value explicitly by using --tenant-id.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.custom_prompt is not None:
            result['customPrompt'] = self.custom_prompt

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.output_type is not None:
            result['outputType'] = self.output_type

        if self.recent_message_count is not None:
            result['recentMessageCount'] = self.recent_message_count

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('customPrompt') is not None:
            self.custom_prompt = m.get('customPrompt')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('outputType') is not None:
            self.output_type = m.get('outputType')

        if m.get('recentMessageCount') is not None:
            self.recent_message_count = m.get('recentMessageCount')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

