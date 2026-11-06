# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RerunWorkflowNodeResponseBody(DaraModel):
    def __init__(
        self,
        affected_node_keys: List[str] = None,
        code: str = None,
        message: str = None,
        plan_id: str = None,
        request_id: str = None,
        revision: int = None,
        run_id: str = None,
        state_version: int = None,
    ):
        # 本次重跑影响的节点 key 列表，供调用方刷新；成功响应恒包含，错误响应可缺省
        self.affected_node_keys = affected_node_keys
        # 业务状态码；成功为200
        self.code = code
        # 错误描述
        self.message = message
        # 重跑后的当前物理计划ID；固定规划节点重跑可能生成新计划，后续查询应使用此值
        self.plan_id = plan_id
        # 请求追踪ID
        self.request_id = request_id
        # 重跑后的当前计划修订号
        self.revision = revision
        # 当前工作流运行ID，固定节点生成新 revision 时保持不变
        self.run_id = run_id
        # 重跑被接受后的工作流状态版本
        self.state_version = state_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affected_node_keys is not None:
            result['affectedNodeKeys'] = self.affected_node_keys

        if self.code is not None:
            result['code'] = self.code

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

        if self.state_version is not None:
            result['stateVersion'] = self.state_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('affectedNodeKeys') is not None:
            self.affected_node_keys = m.get('affectedNodeKeys')

        if m.get('code') is not None:
            self.code = m.get('code')

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

        if m.get('stateVersion') is not None:
            self.state_version = m.get('stateVersion')

        return self

