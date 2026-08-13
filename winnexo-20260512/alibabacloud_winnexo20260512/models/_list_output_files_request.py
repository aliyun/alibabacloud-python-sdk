# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOutputFilesRequest(DaraModel):
    def __init__(
        self,
        item_type: str = None,
        keyword: str = None,
        operating_object_name: str = None,
        page: int = None,
        page_size: int = None,
        shared_only: bool = None,
        tenant_id: str = None,
    ):
        # 产出明细类型: ppt/html/document/picture/slides/video/audio/email/others
        self.item_type = item_type
        # 关键词搜索，匹配产出标题或明细名称
        self.keyword = keyword
        # 数字员工（运营对象）名称，按名称过滤
        self.operating_object_name = operating_object_name
        # 页码，从 1 开始
        self.page = page
        # 每页数量，范围 1-100
        self.page_size = page_size
        # 是否仅展示开启分享的产出和产出明细
        self.shared_only = shared_only
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_type is not None:
            result['itemType'] = self.item_type

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.shared_only is not None:
            result['sharedOnly'] = self.shared_only

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('sharedOnly') is not None:
            self.shared_only = m.get('sharedOnly')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

