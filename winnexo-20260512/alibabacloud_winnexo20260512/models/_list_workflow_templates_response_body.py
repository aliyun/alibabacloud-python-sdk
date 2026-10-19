# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListWorkflowTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        has_more: bool = None,
        items: List[main_models.ListWorkflowTemplatesResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # 业务状态码；成功为200
        self.code = code
        # 是否还有更多数据
        self.has_more = has_more
        # 当前页模板摘要列表
        self.items = items
        # 本次生效的单页最大返回数量
        self.max_results = max_results
        # 错误描述
        self.message = message
        # 下一页翻页令牌；无更多数据时为空字符串
        self.next_token = next_token
        # 当前页码
        self.page = page
        # 生效单页条数
        self.page_size = page_size
        # 请求追踪ID
        self.request_id = request_id
        # 筛选条件下可见总数
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
                temp_model = main_models.ListWorkflowTemplatesResponseBodyItems()
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

class ListWorkflowTemplatesResponseBodyItems(DaraModel):
    def __init__(
        self,
        description: str = None,
        gmt_modified: str = None,
        name: str = None,
        owner_count: int = None,
        review_step_count: int = None,
        step_count: int = None,
        template_id: str = None,
    ):
        # 模板描述
        self.description = description
        # 最近修改时间(ISO8601)
        self.gmt_modified = gmt_modified
        # 模板名称
        self.name = name
        # 去重后的负责人数量
        self.owner_count = owner_count
        # 配置了审核人的步骤数
        self.review_step_count = review_step_count
        # 步骤数
        self.step_count = step_count
        # 模板ID
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.name is not None:
            result['name'] = self.name

        if self.owner_count is not None:
            result['ownerCount'] = self.owner_count

        if self.review_step_count is not None:
            result['reviewStepCount'] = self.review_step_count

        if self.step_count is not None:
            result['stepCount'] = self.step_count

        if self.template_id is not None:
            result['templateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ownerCount') is not None:
            self.owner_count = m.get('ownerCount')

        if m.get('reviewStepCount') is not None:
            self.review_step_count = m.get('reviewStepCount')

        if m.get('stepCount') is not None:
            self.step_count = m.get('stepCount')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        return self

