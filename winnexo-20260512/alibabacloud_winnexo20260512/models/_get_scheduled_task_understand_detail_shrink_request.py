# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScheduledTaskUnderstandDetailShrinkRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        collaboration_group_id: str = None,
        digital_employee_name_shrink: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        segments_shrink: str = None,
        tenant_id: str = None,
        user_input: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The ID of the collaboration group to which the task belongs, such as cg_101. If this parameter is specified, a group space task is created and the caller must be a valid group member. If this parameter is left empty, a personal task is created.
        self.collaboration_group_id = collaboration_group_id
        # The name of the current effective digital employee. This parameter is empty if not configured.
        # 
        # This parameter is required.
        self.digital_employee_name_shrink = digital_employee_name_shrink
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The segments.
        self.segments_shrink = segments_shrink
        # The ID of the effective tenant.
        self.tenant_id = tenant_id
        # The natural language task description.
        self.user_input = user_input

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.digital_employee_name_shrink is not None:
            result['digitalEmployeeName'] = self.digital_employee_name_shrink

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.segments_shrink is not None:
            result['segments'] = self.segments_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_input is not None:
            result['userInput'] = self.user_input

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name_shrink = m.get('digitalEmployeeName')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('segments') is not None:
            self.segments_shrink = m.get('segments')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userInput') is not None:
            self.user_input = m.get('userInput')

        return self

