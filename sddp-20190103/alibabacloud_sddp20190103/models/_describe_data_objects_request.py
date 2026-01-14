# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataObjectsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        domain_id: int = None,
        feature_type: int = None,
        file_category_code: int = None,
        file_type: int = None,
        instance_id: str = None,
        lang: str = None,
        member_account: int = None,
        model_ids: str = None,
        model_tag_ids: str = None,
        page_size: int = None,
        parent_category_ids: str = None,
        product_ids: str = None,
        query_name: str = None,
        risk_levels: str = None,
        service_region_id: str = None,
        template_id: int = None,
    ):
        # Page number for the paginated query. Default value: 1.
        self.current_page = current_page
        # ID of the data domain to which the data asset belongs.
        self.domain_id = domain_id
        # This parameter is deprecated.
        self.feature_type = feature_type
        # File category code.
        self.file_category_code = file_category_code
        # OSS file types that are supported for recognition.
        # 
        # > You can obtain the supported OSS file types by calling [DescribeDocTypes](https://help.aliyun.com/document_detail/2536492.html), using the Code field value from the response. This parameter is only valid for querying OSS-type assets.
        self.file_type = file_type
        # Keyword for the asset instance ID.
        self.instance_id = instance_id
        # The language type for request and response messages, default is **zh_cn**. Values:
        # - **zh_cn**: Chinese.
        # - **en_us**: English.
        self.lang = lang
        # Member account ID.
        self.member_account = member_account
        # Model IDs of the industry template, separated by commas.
        # > You can obtain the industry template model identifier ID by calling [DescribeTemplateAllRules](https://help.aliyun.com/document_detail/2536491.html).
        self.model_ids = model_ids
        # Data labels to be queried, separated by commas. Values:
        # - **101**: Personal Sensitive Information.
        # - **102**: Personal Information.
        # - **107**: General Information.
        self.model_tag_ids = model_tag_ids
        # When performing a paginated query, set the maximum number of data asset instances to display per page. Default value: **10**.
        self.page_size = page_size
        # List of parent category IDs for the template to be queried, separated by commas.
        self.parent_category_ids = parent_category_ids
        # It is recommended to fill in the list of product IDs to be queried, separated by commas. Values:
        # - **1**: MaxCompute
        # - **2**: OSS
        # - **3**: ADB-MYSQL
        # - **4**: TableStore
        # - **5**: RDS
        # - **6**: SELF_DB
        # - **7**: PolarDB-X
        # - **8**: PolarDB
        # - **9**: ADB-PG
        # - **10**: OceanBase
        # - **11**: MongoDB
        # - **25**: Redis
        # 
        # > OSS is mutually exclusive with other products, meaning if OSS is included in the query, no other products can be listed; by default, non-OSS products are queried.
        self.product_ids = product_ids
        # Keyword for the data object to be queried.
        self.query_name = query_name
        # Specify the risk levels of the data assets to be queried, separated by commas if multiple.
        # - **2**: S1, low risk level.
        # - **3**: S2, medium risk level.
        # - **4**: S3, high risk level.
        # - **5**: S4, highest risk level.
        self.risk_levels = risk_levels
        # Region where the asset is located. Values:
        # - **cn-beijing**: North China 2 (Beijing).
        # - **cn-zhangjiakou**: North China 3 (Zhangjiakou).
        # - **cn-huhehaote**: North China 5 (Hohhot).
        # - **cn-hangzhou**: East China 1 (Hangzhou).
        # - **cn-shanghai**: East China 2 (Shanghai).
        # - **cn-shenzhen**: South China 1 (Shenzhen).
        # - **cn-hongkong**: Hong Kong, China.
        self.service_region_id = service_region_id
        # Industry template ID.
        # 
        # > You can obtain the industry template identifier ID by calling [DescribeCategoryTemplateList](https://help.aliyun.com/document_detail/2399296.html).
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

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.file_category_code is not None:
            result['FileCategoryCode'] = self.file_category_code

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_account is not None:
            result['MemberAccount'] = self.member_account

        if self.model_ids is not None:
            result['ModelIds'] = self.model_ids

        if self.model_tag_ids is not None:
            result['ModelTagIds'] = self.model_tag_ids

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_category_ids is not None:
            result['ParentCategoryIds'] = self.parent_category_ids

        if self.product_ids is not None:
            result['ProductIds'] = self.product_ids

        if self.query_name is not None:
            result['QueryName'] = self.query_name

        if self.risk_levels is not None:
            result['RiskLevels'] = self.risk_levels

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('FileCategoryCode') is not None:
            self.file_category_code = m.get('FileCategoryCode')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberAccount') is not None:
            self.member_account = m.get('MemberAccount')

        if m.get('ModelIds') is not None:
            self.model_ids = m.get('ModelIds')

        if m.get('ModelTagIds') is not None:
            self.model_tag_ids = m.get('ModelTagIds')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentCategoryIds') is not None:
            self.parent_category_ids = m.get('ParentCategoryIds')

        if m.get('ProductIds') is not None:
            self.product_ids = m.get('ProductIds')

        if m.get('QueryName') is not None:
            self.query_name = m.get('QueryName')

        if m.get('RiskLevels') is not None:
            self.risk_levels = m.get('RiskLevels')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

