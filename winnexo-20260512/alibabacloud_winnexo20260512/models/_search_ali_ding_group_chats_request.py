# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchAliDingGroupChatsRequest(DaraModel):
    def __init__(
        self,
        cursor: str = None,
        exclude_muted: bool = None,
        keyword: str = None,
        page_size: int = None,
        tenant_id: str = None,
    ):
        # 分页游标，首页传 0
        self.cursor = cursor
        # 是否排除免打扰群聊
        self.exclude_muted = exclude_muted
        # 群聊搜索关键词
        # 
        # This parameter is required.
        self.keyword = keyword
        # 每页条数，范围 1-100
        self.page_size = page_size
        # 租户 ID，公共参数；缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cursor is not None:
            result['cursor'] = self.cursor

        if self.exclude_muted is not None:
            result['excludeMuted'] = self.exclude_muted

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')

        if m.get('excludeMuted') is not None:
            self.exclude_muted = m.get('excludeMuted')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

