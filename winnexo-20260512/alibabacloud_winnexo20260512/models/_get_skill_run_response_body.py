# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class GetSkillRunResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        created_at: str = None,
        error_code: str = None,
        error_message: str = None,
        finished_at: str = None,
        logs: List[Dict[str, Any]] = None,
        message: str = None,
        progress: int = None,
        progress_message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
        run_id: str = None,
        skill_code: str = None,
        skill_name: str = None,
        started_at: str = None,
        status: str = None,
        usage: Dict[str, Any] = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 任务创建时间，ISO8601
        self.created_at = created_at
        # 错误码，仅 Failed 时返回
        self.error_code = error_code
        # 错误描述，仅 Failed 时返回
        self.error_message = error_message
        # 任务结束时间，ISO8601；仅终态（Succeeded/Failed/Cancelled）有值
        self.finished_at = finished_at
        self.logs = logs
        # 错误描述，成功时为空
        self.message = message
        # 进度百分比（仅 Running 时有意义）
        self.progress = progress
        # 进度描述
        self.progress_message = progress_message
        # 请求追踪 ID
        self.request_id = request_id
        self.result = result
        # 异步任务 ID
        self.run_id = run_id
        # 技能编码
        self.skill_code = skill_code
        # 技能名称
        self.skill_name = skill_name
        # 任务开始执行时间，ISO8601
        self.started_at = started_at
        # 执行状态：Running / Succeeded / Failed / Cancelled
        self.status = status
        self.usage = usage

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

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        if self.logs is not None:
            result['logs'] = self.logs

        if self.message is not None:
            result['message'] = self.message

        if self.progress is not None:
            result['progress'] = self.progress

        if self.progress_message is not None:
            result['progressMessage'] = self.progress_message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.skill_name is not None:
            result['skillName'] = self.skill_name

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.status is not None:
            result['status'] = self.status

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('logs') is not None:
            self.logs = m.get('logs')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('progressMessage') is not None:
            self.progress_message = m.get('progressMessage')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('skillName') is not None:
            self.skill_name = m.get('skillName')

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

