# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListInstanceNodesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        message: str = None,
        nodes: List[main_models.ListInstanceNodesResponseBodyNodes] = None,
        request_id: str = None,
        state_version: int = None,
    ):
        # 业务状态码；成功为200
        self.code = code
        # 物理实例ID
        self.instance_id = instance_id
        # 错误描述
        self.message = message
        # 按拓扑顺序排列的可见节点，数量由实际动态图决定
        self.nodes = nodes
        # 请求追踪ID
        self.request_id = request_id
        # 状态版本
        self.state_version = state_version

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

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

        result['nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['nodes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

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

        self.nodes = []
        if m.get('nodes') is not None:
            for k1 in m.get('nodes'):
                temp_model = main_models.ListInstanceNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('stateVersion') is not None:
            self.state_version = m.get('stateVersion')

        return self

class ListInstanceNodesResponseBodyNodes(DaraModel):
    def __init__(
        self,
        conclusion: str = None,
        duration: int = None,
        entered_at: str = None,
        finished_at: str = None,
        handler: str = None,
        lane: int = None,
        node_id: str = None,
        node_name: str = None,
        node_order: int = None,
        node_type: str = None,
        rank: int = None,
        status: str = None,
        wait_type: str = None,
    ):
        # 节点结果结论，无结论时为空
        self.conclusion = conclusion
        # 从首次运行到终态的整秒数，缺时间时为空
        self.duration = duration
        # 节点首次运行时间，历史或未运行节点为空
        self.entered_at = entered_at
        # 节点实际进入终态的时间，未结束时为空
        self.finished_at = finished_at
        # 节点负责人展示名称，未知时为空
        self.handler = handler
        # 节点在工作流图中的泳道位置
        self.lane = lane
        # 所属节点key（nodeKey），不是会话ID
        self.node_id = node_id
        # 节点展示名称
        self.node_name = node_name
        # 节点在返回拓扑列表中的展示序号，从1开始
        self.node_order = node_order
        # 实际节点类型，例如AGENT或HUMAN
        self.node_type = node_type
        # 节点在工作流图中的层级，从0开始
        self.rank = rank
        # 原始节点运行状态，例如READY、RUNNING、WAITING、SUCCEEDED或FAILED
        self.status = status
        # 等待原因：HUMAN_INPUT、HUMAN_STEP、REVIEW、MANUAL_PAUSE或UNBLOCK；未等待时为空
        self.wait_type = wait_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conclusion is not None:
            result['conclusion'] = self.conclusion

        if self.duration is not None:
            result['duration'] = self.duration

        if self.entered_at is not None:
            result['enteredAt'] = self.entered_at

        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        if self.handler is not None:
            result['handler'] = self.handler

        if self.lane is not None:
            result['lane'] = self.lane

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.node_name is not None:
            result['nodeName'] = self.node_name

        if self.node_order is not None:
            result['nodeOrder'] = self.node_order

        if self.node_type is not None:
            result['nodeType'] = self.node_type

        if self.rank is not None:
            result['rank'] = self.rank

        if self.status is not None:
            result['status'] = self.status

        if self.wait_type is not None:
            result['waitType'] = self.wait_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conclusion') is not None:
            self.conclusion = m.get('conclusion')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('enteredAt') is not None:
            self.entered_at = m.get('enteredAt')

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('handler') is not None:
            self.handler = m.get('handler')

        if m.get('lane') is not None:
            self.lane = m.get('lane')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')

        if m.get('nodeOrder') is not None:
            self.node_order = m.get('nodeOrder')

        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')

        if m.get('rank') is not None:
            self.rank = m.get('rank')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('waitType') is not None:
            self.wait_type = m.get('waitType')

        return self

