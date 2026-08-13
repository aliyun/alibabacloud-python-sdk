# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserVisibleKnowledgeBaseContentsRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
        sort_field: str = None,
        sort_order: str = None,
        source_types: str = None,
        tenant_id: str = None,
    ):
        # 目标知识库根目录或其子目录的唯一标识
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # 当前目录下的目录或资源名称关键词
        self.keyword = keyword
        # 页码，从 1 开始
        self.page = page
        # 每页数量，范围 1-200
        self.page_size = page_size
        # 排序字段，可选 name / gmt_create / gmt_modified
        self.sort_field = sort_field
        # 排序方向，可选 asc / desc
        self.sort_order = sort_order
        # 资源类型过滤，多个类型使用逗号分隔；传入后只返回资源
        self.source_types = source_types
        # 租户ID，公共参数，缺省时使用调用方默认租户
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

        if self.source_types is not None:
            result['sourceTypes'] = self.source_types

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
            self.source_types = m.get('sourceTypes')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

