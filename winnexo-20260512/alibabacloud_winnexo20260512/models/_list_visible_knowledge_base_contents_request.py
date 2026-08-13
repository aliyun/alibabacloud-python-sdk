# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListVisibleKnowledgeBaseContentsRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        operating_object_name: str = None,
        page: int = None,
        page_size: int = None,
        sort_field: str = None,
        sort_order: str = None,
        source_types: List[str] = None,
        tenant_id: str = None,
    ):
        # 目录 ID（必传非空，必须在数字员工 linked_directories 及其子目录范围内）
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # 数字员工名称（运营对象 name）
        # 
        # This parameter is required.
        self.operating_object_name = operating_object_name
        # 页码（从 1 开始）
        self.page = page
        # 每页数量，范围 1-100
        self.page_size = page_size
        # 排序字段，可选 name / gmt_create / gmt_modified
        self.sort_field = sort_field
        # 排序方向，可选 asc / desc
        self.sort_order = sort_order
        # 资源类型筛选列表（有值时仅返回资源，不包含子目录）
        self.source_types = source_types
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

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

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

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

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

