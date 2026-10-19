# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryWorkItemFeedShrinkRequest(DaraModel):
    def __init__(
        self,
        business_statuses_shrink: str = None,
        collaboration_group_id: str = None,
        cursor: str = None,
        item_types_shrink: str = None,
        keyword: str = None,
        page_size: int = None,
        priorities_shrink: str = None,
        scope: str = None,
        source_task_id: str = None,
        tenant_id: str = None,
        view: str = None,
    ):
        # 业务状态筛选（七态）
        self.business_statuses_shrink = business_statuses_shrink
        # 协作空间 ID
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # 翻页游标，取上次响应的 nextCursor
        self.cursor = cursor
        # 工作项类型筛选
        self.item_types_shrink = item_types_shrink
        # 标题/描述模糊搜索关键词
        self.keyword = keyword
        # 单页条数（1~100）
        self.page_size = page_size
        # 优先级筛选
        self.priorities_shrink = priorities_shrink
        # 个人范围筛选
        self.scope = scope
        # 来源任务ID；指定时返回该任务平铺子项
        self.source_task_id = source_task_id
        # 租户ID，公共参数；缺省时使用调用方默认租户
        self.tenant_id = tenant_id
        # 视图：FLAT 平铺 / TREE 任务分组
        self.view = view

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_statuses_shrink is not None:
            result['businessStatuses'] = self.business_statuses_shrink

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.cursor is not None:
            result['cursor'] = self.cursor

        if self.item_types_shrink is not None:
            result['itemTypes'] = self.item_types_shrink

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.priorities_shrink is not None:
            result['priorities'] = self.priorities_shrink

        if self.scope is not None:
            result['scope'] = self.scope

        if self.source_task_id is not None:
            result['sourceTaskId'] = self.source_task_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.view is not None:
            result['view'] = self.view

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessStatuses') is not None:
            self.business_statuses_shrink = m.get('businessStatuses')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')

        if m.get('itemTypes') is not None:
            self.item_types_shrink = m.get('itemTypes')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('priorities') is not None:
            self.priorities_shrink = m.get('priorities')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('sourceTaskId') is not None:
            self.source_task_id = m.get('sourceTaskId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('view') is not None:
            self.view = m.get('view')

        return self

