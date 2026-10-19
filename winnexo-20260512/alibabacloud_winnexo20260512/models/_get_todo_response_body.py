# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class GetTodoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        todo: Dict[str, Any] = None,
        todos: List[main_models.GetTodoResponseBodyTodos] = None,
    ):
        # 业务状态码；成功为200
        self.code = code
        # 错误描述
        self.message = message
        # 请求追踪ID
        self.request_id = request_id
        # todoId 查询时的单条结果（其余查询为空）；字段集同 getTodoDetail 平铺结构
        self.todo = todo
        # workItemId/messageId 查询时的多条结果（todoId 查询为空）
        self.todos = todos

    def validate(self):
        if self.todos:
            for v1 in self.todos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.todo is not None:
            result['todo'] = self.todo

        result['todos'] = []
        if self.todos is not None:
            for k1 in self.todos:
                result['todos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('todo') is not None:
            self.todo = m.get('todo')

        self.todos = []
        if m.get('todos') is not None:
            for k1 in m.get('todos'):
                temp_model = main_models.GetTodoResponseBodyTodos()
                self.todos.append(temp_model.from_map(k1))

        return self

class GetTodoResponseBodyTodos(DaraModel):
    def __init__(
        self,
        assignees: List[main_models.GetTodoResponseBodyTodosAssignees] = None,
        completed_at: str = None,
        completed_by_user_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        message_id: str = None,
        priority: str = None,
        questions: Dict[str, Any] = None,
        result_payload: Dict[str, Any] = None,
        source_context: Dict[str, Any] = None,
        status: str = None,
        summary: str = None,
        title: str = None,
        todo_id: str = None,
    ):
        # 全部处理人
        self.assignees = assignees
        # 完成时间（北京时间）
        self.completed_at = completed_at
        # 完成人用户ID
        self.completed_by_user_id = completed_by_user_id
        # 创建时间（北京时间）
        self.gmt_create = gmt_create
        # 最后修改时间（北京时间）
        self.gmt_modified = gmt_modified
        # assistant 消息ID；无会话来源为空
        self.message_id = message_id
        # 优先级
        self.priority = priority
        # 问题清单（JSONB 原样）
        self.questions = questions
        # 作答内容（JSONB 原样）
        self.result_payload = result_payload
        # 来源上下文（原样透传）
        self.source_context = source_context
        # 待办主状态
        self.status = status
        # 待办摘要
        self.summary = summary
        # 待办标题
        self.title = title
        # 待办ID
        self.todo_id = todo_id

    def validate(self):
        if self.assignees:
            for v1 in self.assignees:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['assignees'] = []
        if self.assignees is not None:
            for k1 in self.assignees:
                result['assignees'].append(k1.to_map() if k1 else None)

        if self.completed_at is not None:
            result['completedAt'] = self.completed_at

        if self.completed_by_user_id is not None:
            result['completedByUserId'] = self.completed_by_user_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.priority is not None:
            result['priority'] = self.priority

        if self.questions is not None:
            result['questions'] = self.questions

        if self.result_payload is not None:
            result['resultPayload'] = self.result_payload

        if self.source_context is not None:
            result['sourceContext'] = self.source_context

        if self.status is not None:
            result['status'] = self.status

        if self.summary is not None:
            result['summary'] = self.summary

        if self.title is not None:
            result['title'] = self.title

        if self.todo_id is not None:
            result['todoId'] = self.todo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assignees = []
        if m.get('assignees') is not None:
            for k1 in m.get('assignees'):
                temp_model = main_models.GetTodoResponseBodyTodosAssignees()
                self.assignees.append(temp_model.from_map(k1))

        if m.get('completedAt') is not None:
            self.completed_at = m.get('completedAt')

        if m.get('completedByUserId') is not None:
            self.completed_by_user_id = m.get('completedByUserId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('questions') is not None:
            self.questions = m.get('questions')

        if m.get('resultPayload') is not None:
            self.result_payload = m.get('resultPayload')

        if m.get('sourceContext') is not None:
            self.source_context = m.get('sourceContext')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('todoId') is not None:
            self.todo_id = m.get('todoId')

        return self

class GetTodoResponseBodyTodosAssignees(DaraModel):
    def __init__(
        self,
        acted_at: str = None,
        assignee_source: str = None,
        assignee_user_id: str = None,
        read_at: str = None,
        status: str = None,
        transferred_from_user_id: str = None,
    ):
        # 处理时间（北京时间）；未处理为空
        self.acted_at = acted_at
        # 处理人来源：ORIGINAL/TRANSFERRED
        self.assignee_source = assignee_source
        # 处理人用户ID
        self.assignee_user_id = assignee_user_id
        # 已读时间（北京时间）；未读为空
        self.read_at = read_at
        # 处理人行状态
        self.status = status
        # 转出人用户ID；仅转办产生
        self.transferred_from_user_id = transferred_from_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acted_at is not None:
            result['actedAt'] = self.acted_at

        if self.assignee_source is not None:
            result['assigneeSource'] = self.assignee_source

        if self.assignee_user_id is not None:
            result['assigneeUserId'] = self.assignee_user_id

        if self.read_at is not None:
            result['readAt'] = self.read_at

        if self.status is not None:
            result['status'] = self.status

        if self.transferred_from_user_id is not None:
            result['transferredFromUserId'] = self.transferred_from_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actedAt') is not None:
            self.acted_at = m.get('actedAt')

        if m.get('assigneeSource') is not None:
            self.assignee_source = m.get('assigneeSource')

        if m.get('assigneeUserId') is not None:
            self.assignee_user_id = m.get('assigneeUserId')

        if m.get('readAt') is not None:
            self.read_at = m.get('readAt')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('transferredFromUserId') is not None:
            self.transferred_from_user_id = m.get('transferredFromUserId')

        return self

