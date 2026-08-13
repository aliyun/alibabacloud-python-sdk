# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryPrimaryObjectDataRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        only_favorites: bool = None,
        operating_object_name: str = None,
        page: int = None,
        page_size: int = None,
        tenant_id: str = None,
    ):
        # 关键字搜索（固定匹配 name；若 schema 定义 description，则同时匹配 description）
        self.keyword = keyword
        # 仅返回关注的主对象；false 或不传则返回全部对象（包含 isFavorited 标识）
        self.only_favorites = only_favorites
        # 运营对象名称（如 customer_1）
        # 
        # This parameter is required.
        self.operating_object_name = operating_object_name
        # 页码（从 1 开始）
        self.page = page
        # 每页数量，范围 1-100
        self.page_size = page_size
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.only_favorites is not None:
            result['onlyFavorites'] = self.only_favorites

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('onlyFavorites') is not None:
            self.only_favorites = m.get('onlyFavorites')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

