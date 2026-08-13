# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunSkillResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        created_at: str = None,
        message: str = None,
        request_id: str = None,
        run_id: str = None,
        skill_code: str = None,
        skill_name: str = None,
        status: str = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 任务创建时间，ISO8601 UTC 格式
        self.created_at = created_at
        # 错误描述，成功时为空
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id
        # 异步任务 ID，用于 getSkillRun 查询
        self.run_id = run_id
        # 实际执行的技能编码
        self.skill_code = skill_code
        # 技能名称
        self.skill_name = skill_name
        # 任务状态：提交即返回 Running
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

