# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RerunNodeAIResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        message: str = None,
        node_id: str = None,
        request_id: str = None,
        rerun_accepted: bool = None,
        state_version: int = None,
    ):
        # 业务状态码；成功为200
        self.code = code
        # 物理实例ID
        self.instance_id = instance_id
        # 错误描述
        self.message = message
        # 已安排重跑的节点 key
        self.node_id = node_id
        # 请求追踪ID
        self.request_id = request_id
        # 重跑事实接受为 true，不表示 AI 已完成；失败通过 Code 和 Message 返回
        self.rerun_accepted = rerun_accepted
        # 状态版本
        self.state_version = state_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.message is not None:
            result['message'] = self.message

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.rerun_accepted is not None:
            result['rerunAccepted'] = self.rerun_accepted

        if self.state_version is not None:
            result['stateVersion'] = self.state_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('rerunAccepted') is not None:
            self.rerun_accepted = m.get('rerunAccepted')

        if m.get('stateVersion') is not None:
            self.state_version = m.get('stateVersion')

        return self

