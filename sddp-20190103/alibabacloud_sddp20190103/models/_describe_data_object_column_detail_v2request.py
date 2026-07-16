# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataObjectColumnDetailV2Request(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        feature_type: int = None,
        id: str = None,
        lang: str = None,
        page_size: int = None,
        product_id: int = None,
        template_id: int = None,
    ):
        # The page number. Default value: **1**.
        self.current_page = current_page
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The unique ID of the data object to query.
        # 
        # > You can call the [DescribeDataObjects](https://help.aliyun.com/document_detail/2399253.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.id = id
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # - **zh_cn**: Chinese.
        # 
        # - **en_us**: English.
        self.lang = lang
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size
        # The ID of the product to which the data object belongs. Valid values:
        # 
        # - **1**: MaxCompute
        # 
        # - **2**: OSS
        # 
        # - **3**: ADB-MYSQL
        # 
        # - **4**: Tablestore
        # 
        # - **5**: RDS
        # 
        # - **6**: SELF_DB
        # 
        # - **7**: PolarDB-X
        # 
        # - **8**: PolarDB
        # 
        # - **9**: ADB-PG
        # 
        # - **10**: OceanBase
        # 
        # - **11**: MongoDB
        # 
        # - **25**: Redis
        self.product_id = product_id
        # The ID of the industry-specific template.
        # 
        # > You can call the [DescribeDataObjects](https://help.aliyun.com/document_detail/2399253.html) operation to obtain the ID of the industry-specific template.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.id is not None:
            result['Id'] = self.id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

