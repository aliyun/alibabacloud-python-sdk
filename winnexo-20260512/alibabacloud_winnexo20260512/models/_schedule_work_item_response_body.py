# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ScheduleWorkItemResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        created: bool = None,
        message: str = None,
        plan_id: str = None,
        request_id: str = None,
        revision: int = None,
        run_id: str = None,
        run_seq: int = None,
        work_item_id: str = None,
    ):
        # 业务状态码；成功为200
        self.code = code
        # 本次是否新创建 Plan
        self.created = created
        # 错误描述
        self.message = message
        # 物理计划ID
        self.plan_id = plan_id
        # 请求追踪ID
        self.request_id = request_id
        # 修订号
        self.revision = revision
        # 运行ID
        self.run_id = run_id
        # 运行序号
        self.run_seq = run_seq
        # 工作项ID
        self.work_item_id = work_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.created is not None:
            result['created'] = self.created

        if self.message is not None:
            result['message'] = self.message

        if self.plan_id is not None:
            result['planId'] = self.plan_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.revision is not None:
            result['revision'] = self.revision

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.run_seq is not None:
            result['runSeq'] = self.run_seq

        if self.work_item_id is not None:
            result['workItemId'] = self.work_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('planId') is not None:
            self.plan_id = m.get('planId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('revision') is not None:
            self.revision = m.get('revision')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('runSeq') is not None:
            self.run_seq = m.get('runSeq')

        if m.get('workItemId') is not None:
            self.work_item_id = m.get('workItemId')

        return self

