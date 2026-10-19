# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTodosShrinkRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        priorities_shrink: str = None,
        read_status_shrink: str = None,
        sort_by: str = None,
        source_types_shrink: str = None,
        statuses_shrink: str = None,
        tenant_id: str = None,
    ):
        # 协作空间 ID（可选过滤；不传 = 全部空间）
        self.collaboration_group_id = collaboration_group_id
        # 标题/摘要模糊搜索关键词
        self.keyword = keyword
        # 单页最大返回数量（1~100）；传入时优先于 pageSize
        self.max_results = max_results
        # 翻页令牌，取上次响应返回的 nextToken；传入时优先于 page
        self.next_token = next_token
        # 页码；传入 nextToken 时忽略
        self.page = page
        # 每页条数（1~100）
        self.page_size = page_size
        # 优先级筛选（HIGH/MEDIUM/LOW）
        self.priorities_shrink = priorities_shrink
        # 读取状态筛选（UNREAD/READ，按处理人 readAt 判定）
        self.read_status_shrink = read_status_shrink
        # 排序方式
        self.sort_by = sort_by
        # 待办类型筛选（WORKFLOW/OPEN_API）
        self.source_types_shrink = source_types_shrink
        # 待办状态筛选（PENDING/COMPLETED/CANCELLED）
        self.statuses_shrink = statuses_shrink
        # 租户ID，公共参数；缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.priorities_shrink is not None:
            result['priorities'] = self.priorities_shrink

        if self.read_status_shrink is not None:
            result['readStatus'] = self.read_status_shrink

        if self.sort_by is not None:
            result['sortBy'] = self.sort_by

        if self.source_types_shrink is not None:
            result['sourceTypes'] = self.source_types_shrink

        if self.statuses_shrink is not None:
            result['statuses'] = self.statuses_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('priorities') is not None:
            self.priorities_shrink = m.get('priorities')

        if m.get('readStatus') is not None:
            self.read_status_shrink = m.get('readStatus')

        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')

        if m.get('sourceTypes') is not None:
            self.source_types_shrink = m.get('sourceTypes')

        if m.get('statuses') is not None:
            self.statuses_shrink = m.get('statuses')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

