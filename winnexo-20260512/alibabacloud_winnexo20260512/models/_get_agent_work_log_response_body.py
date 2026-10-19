# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetAgentWorkLogResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        logs: List[main_models.GetAgentWorkLogResponseBodyLogs] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # 业务状态码；成功为200
        self.code = code
        # 按时间倒序的 Agent 工作记录，未保存记录时为空列表
        self.logs = logs
        # 错误描述
        self.message = message
        # 当前页码，从1开始
        self.page = page
        # 每页条数，取值1至100
        self.page_size = page_size
        # 请求追踪ID
        self.request_id = request_id
        # 筛选后的工作日志总条数
        self.total = total

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['logs'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.logs = []
        if m.get('logs') is not None:
            for k1 in m.get('logs'):
                temp_model = main_models.GetAgentWorkLogResponseBodyLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class GetAgentWorkLogResponseBodyLogs(DaraModel):
    def __init__(
        self,
        action: str = None,
        detail: str = None,
        duration: int = None,
        node_id: str = None,
        timestamp: str = None,
    ):
        # 记录类型：THINK、REPLY、TOOL_CALL、SKILL_CALL或ARTIFACT
        self.action = action
        # 已保存的原始记录内容；工具调用与产物元数据为JSON字符串
        self.detail = detail
        # 该条工作记录耗时，单位毫秒；产物记录为0
        self.duration = duration
        # 所属节点key（nodeKey），不是会话ID
        self.node_id = node_id
        # 记录事件时间，ISO-8601格式；源记录无时间时为空字符串
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.detail is not None:
            result['detail'] = self.detail

        if self.duration is not None:
            result['duration'] = self.duration

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('detail') is not None:
            self.detail = m.get('detail')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

