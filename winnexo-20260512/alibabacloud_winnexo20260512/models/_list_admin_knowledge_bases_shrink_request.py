# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAdminKnowledgeBasesShrinkRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
        sort_field: str = None,
        sort_order: str = None,
        source_types_shrink: str = None,
        tenant_id: str = None,
    ):
        # 目录 ID；为空或 \"root\" 时返回 KB 顶层列表，传具体值时下钻返回该目录的子目录 + 资源（混合分页，由 itemType 区分）
        self.directory_id = directory_id
        # 搜索关键词，仅在 directoryId 为空/root 时生效，模糊匹配 KB 名称或描述（忽略大小写）
        self.keyword = keyword
        # 页码，从 1 开始
        self.page = page
        # 每页数量，范围 1-100
        self.page_size = page_size
        # 排序字段：name / gmtCreate / gmtModified；非法值回退为 name
        self.sort_field = sort_field
        # 排序方向：asc / desc；非法值回退为 asc
        self.sort_order = sort_order
        # 资源类型过滤，仅在下钻（directoryId 非空）时生效；命中时仅返回匹配类型的资源，不含子目录
        self.source_types_shrink = source_types_shrink
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.sort_field is not None:
            result['sortField'] = self.sort_field

        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order

        if self.source_types_shrink is not None:
            result['sourceTypes'] = self.source_types_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('sortField') is not None:
            self.sort_field = m.get('sortField')

        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')

        if m.get('sourceTypes') is not None:
            self.source_types_shrink = m.get('sourceTypes')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

