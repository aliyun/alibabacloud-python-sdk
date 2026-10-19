# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class CreateWorkflowInstanceResponseBody(DaraModel):
    def __init__(
        self,
        business_id: str = None,
        code: str = None,
        collaboration_group_id: str = None,
        created_at: str = None,
        current_node: main_models.CreateWorkflowInstanceResponseBodyCurrentNode = None,
        current_nodes: List[main_models.CreateWorkflowInstanceResponseBodyCurrentNodes] = None,
        ended_at: str = None,
        initiator: str = None,
        instance_id: str = None,
        message: str = None,
        pause_scope: str = None,
        plan_id: str = None,
        progress: main_models.CreateWorkflowInstanceResponseBodyProgress = None,
        request_id: str = None,
        review_status: str = None,
        revision: int = None,
        run_id: str = None,
        runtime_status: str = None,
        started_at: str = None,
        state_version: int = None,
        status: str = None,
        template_id: str = None,
        title: str = None,
        work_item_id: str = None,
    ):
        # 空间内唯一外部需求编号
        self.business_id = business_id
        # 业务状态码，来自统一 POP 响应包装
        self.code = code
        # 协作空间 ID
        self.collaboration_group_id = collaboration_group_id
        # 逻辑实例创建时间，ISO8601
        self.created_at = created_at
        # 首个活动节点，终态为 null
        self.current_node = current_node
        # 全部活动节点，支持并行 DAG
        self.current_nodes = current_nodes
        # 当前计划终态时间，未结束为 null
        self.ended_at = ended_at
        # 外部发起人标签，不参与鉴权
        self.initiator = initiator
        # 稳定逻辑实例 ID，工作项重启不改变
        self.instance_id = instance_id
        # 用户可见错误描述，来自统一 POP 响应包装
        self.message = message
        # 原始计划暂停范围
        self.pause_scope = pause_scope
        # 当前物理计划修订 ID
        self.plan_id = plan_id
        # 可见图进度
        self.progress = progress
        # 请求追踪 ID
        self.request_id = request_id
        # 原始计划审核状态
        self.review_status = review_status
        # 当前物理计划修订号
        self.revision = revision
        # 当前运行 ID，重启后会改变
        self.run_id = run_id
        # 原始 BUILDING/RUNNING/SUCCEEDED/FAILED/CANCELLED
        self.runtime_status = runtime_status
        # 当前计划节点首次开始时间，未执行为 null
        self.started_at = started_at
        # 运行状态版本
        self.state_version = state_version
        # Running/Completed/Failed/Terminated
        self.status = status
        # 创建时绑定的工作流模板 ID
        self.template_id = template_id
        # 当前需求标题
        self.title = title
        # 关联工作项 ID
        self.work_item_id = work_item_id

    def validate(self):
        if self.current_node:
            self.current_node.validate()
        if self.current_nodes:
            for v1 in self.current_nodes:
                 if v1:
                    v1.validate()
        if self.progress:
            self.progress.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_id is not None:
            result['businessId'] = self.business_id

        if self.code is not None:
            result['code'] = self.code

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.current_node is not None:
            result['currentNode'] = self.current_node.to_map()

        result['currentNodes'] = []
        if self.current_nodes is not None:
            for k1 in self.current_nodes:
                result['currentNodes'].append(k1.to_map() if k1 else None)

        if self.ended_at is not None:
            result['endedAt'] = self.ended_at

        if self.initiator is not None:
            result['initiator'] = self.initiator

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.message is not None:
            result['message'] = self.message

        if self.pause_scope is not None:
            result['pauseScope'] = self.pause_scope

        if self.plan_id is not None:
            result['planId'] = self.plan_id

        if self.progress is not None:
            result['progress'] = self.progress.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.review_status is not None:
            result['reviewStatus'] = self.review_status

        if self.revision is not None:
            result['revision'] = self.revision

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.runtime_status is not None:
            result['runtimeStatus'] = self.runtime_status

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.state_version is not None:
            result['stateVersion'] = self.state_version

        if self.status is not None:
            result['status'] = self.status

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.title is not None:
            result['title'] = self.title

        if self.work_item_id is not None:
            result['workItemId'] = self.work_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessId') is not None:
            self.business_id = m.get('businessId')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('currentNode') is not None:
            temp_model = main_models.CreateWorkflowInstanceResponseBodyCurrentNode()
            self.current_node = temp_model.from_map(m.get('currentNode'))

        self.current_nodes = []
        if m.get('currentNodes') is not None:
            for k1 in m.get('currentNodes'):
                temp_model = main_models.CreateWorkflowInstanceResponseBodyCurrentNodes()
                self.current_nodes.append(temp_model.from_map(k1))

        if m.get('endedAt') is not None:
            self.ended_at = m.get('endedAt')

        if m.get('initiator') is not None:
            self.initiator = m.get('initiator')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('pauseScope') is not None:
            self.pause_scope = m.get('pauseScope')

        if m.get('planId') is not None:
            self.plan_id = m.get('planId')

        if m.get('progress') is not None:
            temp_model = main_models.CreateWorkflowInstanceResponseBodyProgress()
            self.progress = temp_model.from_map(m.get('progress'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('reviewStatus') is not None:
            self.review_status = m.get('reviewStatus')

        if m.get('revision') is not None:
            self.revision = m.get('revision')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('runtimeStatus') is not None:
            self.runtime_status = m.get('runtimeStatus')

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('stateVersion') is not None:
            self.state_version = m.get('stateVersion')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('workItemId') is not None:
            self.work_item_id = m.get('workItemId')

        return self

class CreateWorkflowInstanceResponseBodyProgress(DaraModel):
    def __init__(
        self,
        completed_count: int = None,
        total_count: int = None,
    ):
        # 已成功或跳过的可见节点数
        self.completed_count = completed_count
        # 当前图可见节点总数，非固定六节点
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_count is not None:
            result['completedCount'] = self.completed_count

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completedCount') is not None:
            self.completed_count = m.get('completedCount')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class CreateWorkflowInstanceResponseBodyCurrentNodes(DaraModel):
    def __init__(
        self,
        handler: str = None,
        handler_id: str = None,
        node_id: str = None,
        node_name: str = None,
        node_type: str = None,
        status: str = None,
    ):
        # 当前处理人展示名
        self.handler = handler
        # 处理人或数字员工标识
        self.handler_id = handler_id
        # 真实运行节点 nodeKey
        self.node_id = node_id
        # 节点展示名
        self.node_name = node_name
        # 真实节点类型 AGENT/HUMAN/CONDITION
        self.node_type = node_type
        # 节点运行状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.handler is not None:
            result['handler'] = self.handler

        if self.handler_id is not None:
            result['handlerId'] = self.handler_id

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.node_name is not None:
            result['nodeName'] = self.node_name

        if self.node_type is not None:
            result['nodeType'] = self.node_type

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('handler') is not None:
            self.handler = m.get('handler')

        if m.get('handlerId') is not None:
            self.handler_id = m.get('handlerId')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')

        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class CreateWorkflowInstanceResponseBodyCurrentNode(DaraModel):
    def __init__(
        self,
        handler: str = None,
        handler_id: str = None,
        node_id: str = None,
        node_name: str = None,
        node_type: str = None,
        status: str = None,
    ):
        # 当前处理人展示名
        self.handler = handler
        # 处理人或数字员工标识
        self.handler_id = handler_id
        # 真实运行节点 nodeKey
        self.node_id = node_id
        # 节点展示名
        self.node_name = node_name
        # 真实节点类型 AGENT/HUMAN/CONDITION
        self.node_type = node_type
        # 节点运行状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.handler is not None:
            result['handler'] = self.handler

        if self.handler_id is not None:
            result['handlerId'] = self.handler_id

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.node_name is not None:
            result['nodeName'] = self.node_name

        if self.node_type is not None:
            result['nodeType'] = self.node_type

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('handler') is not None:
            self.handler = m.get('handler')

        if m.get('handlerId') is not None:
            self.handler_id = m.get('handlerId')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')

        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

