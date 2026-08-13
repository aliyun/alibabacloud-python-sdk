# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListScheduledTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        has_more: bool = None,
        items: List[main_models.ListScheduledTasksResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码（ERR.* / InvalidParameter.*）
        self.code = code
        # 是否有更多数据
        self.has_more = has_more
        self.items = items
        # 本次实际生效的单页最大返回数量
        self.max_results = max_results
        # 错误描述，成功时为空
        self.message = message
        # 下一页翻页令牌，原样回传即可取下一页；无更多数据时为空字符串
        self.next_token = next_token
        # 当前页码（实际生效值）
        self.page = page
        # 每页条数（实际生效值）
        self.page_size = page_size
        # 请求追踪 ID
        self.request_id = request_id
        # 满足条件的总数
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.has_more is not None:
            result['hasMore'] = self.has_more

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

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

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListScheduledTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListScheduledTasksResponseBodyItems(DaraModel):
    def __init__(
        self,
        creator: str = None,
        cron_expression: str = None,
        description: str = None,
        execution_count: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        is_open: bool = None,
        name: str = None,
        task_id: str = None,
        trigger_type: str = None,
    ):
        # 创建人
        self.creator = creator
        # Cron 表达式
        self.cron_expression = cron_expression
        # 任务简述
        self.description = description
        # 累计执行次数
        self.execution_count = execution_count
        # 创建时间 ISO8601
        self.gmt_create = gmt_create
        # 修改时间 ISO8601
        self.gmt_modified = gmt_modified
        # 是否公开
        self.is_open = is_open
        # 文件名
        self.name = name
        # 任务 ID
        self.task_id = task_id
        # 触发类型（manual/cron/event）
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['creator'] = self.creator

        if self.cron_expression is not None:
            result['cronExpression'] = self.cron_expression

        if self.description is not None:
            result['description'] = self.description

        if self.execution_count is not None:
            result['executionCount'] = self.execution_count

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.is_open is not None:
            result['isOpen'] = self.is_open

        if self.name is not None:
            result['name'] = self.name

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('cronExpression') is not None:
            self.cron_expression = m.get('cronExpression')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('executionCount') is not None:
            self.execution_count = m.get('executionCount')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('isOpen') is not None:
            self.is_open = m.get('isOpen')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        return self

