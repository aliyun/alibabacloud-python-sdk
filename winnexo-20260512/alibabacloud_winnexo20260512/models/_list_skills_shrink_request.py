# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSkillsShrinkRequest(DaraModel):
    def __init__(
        self,
        bind_status: str = None,
        filter_type: str = None,
        keyword: str = None,
        operating_object_name: str = None,
        page: int = None,
        page_size: int = None,
        tags_shrink: str = None,
        tenant_id: str = None,
    ):
        # 绑定状态：BOUND(已绑定) / UNBOUND(未绑定的全局技能)；必须与 operatingObjectName 同时传入
        self.bind_status = bind_status
        # 技能筛选维度：ALL/BUILTIN/CUSTOM/DRAFT/ALL_WITH_DRAFTS
        self.filter_type = filter_type
        # 按技能名称或描述模糊匹配
        self.keyword = keyword
        # 数字员工名称；必须与 bindStatus 同时传入
        self.operating_object_name = operating_object_name
        # 页码，从 1 开始
        self.page = page
        # 每页数量，范围 1-100
        self.page_size = page_size
        # 按标签过滤，数组任一命中即匹配
        self.tags_shrink = tags_shrink
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_status is not None:
            result['bindStatus'] = self.bind_status

        if self.filter_type is not None:
            result['filterType'] = self.filter_type

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bindStatus') is not None:
            self.bind_status = m.get('bindStatus')

        if m.get('filterType') is not None:
            self.filter_type = m.get('filterType')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

