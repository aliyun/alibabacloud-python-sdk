# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataObjectsRequest(DaraModel):
    def __init__(
        self,
        apiversion: int = None,
        bucket: str = None,
        current_page: int = None,
        cursor: str = None,
        cursor_direction: str = None,
        db_name: str = None,
        domain_id: int = None,
        engine_type: str = None,
        facet_type: str = None,
        feature_type: int = None,
        file_category_code: int = None,
        file_type: int = None,
        instance_id: str = None,
        is_revision: int = None,
        lang: str = None,
        log_store: str = None,
        log_store_flag: int = None,
        member_account: int = None,
        model_ids: str = None,
        model_tag_ids: str = None,
        page_size: int = None,
        parent_category_ids: str = None,
        path: str = None,
        product_id: int = None,
        product_ids: str = None,
        project: str = None,
        query_name: str = None,
        region_id: str = None,
        risk_level_id_list: str = None,
        risk_levels: str = None,
        rule_ids: str = None,
        service_region_id: str = None,
        table_name: str = None,
        task_id: int = None,
        template_id: int = None,
    ):
        # The identifier used for canary release evaluation.
        self.apiversion = apiversion
        # The OSS bucket filter.
        self.bucket = bucket
        # The page number in a paged query. Default value: 1.
        self.current_page = current_page
        self.cursor = cursor
        self.cursor_direction = cursor_direction
        # The database name filter.
        self.db_name = db_name
        # The data domain ID to which the data asset belongs.
        self.domain_id = domain_id
        self.engine_type = engine_type
        # The facet dimension for associated filtering in the data catalog. Valid values: rule (category), task (task), instance (instance), and db (database). If this parameter is not specified or is empty, the original list and count query is performed (behavior unchanged). If a valid value is specified, the list query is skipped and only content.hitValues is returned. If an invalid value is specified, a parameter error is returned.
        self.facet_type = facet_type
        # **[Deprecated]** This parameter is deprecated.
        self.feature_type = feature_type
        # The file category code.
        self.file_category_code = file_category_code
        # The OSS file type supported for detection.
        # 
        # > You can call [DescribeDocTypes](https://help.aliyun.com/document_detail/2536492.html) to obtain the supported OSS file types. Use the Code field value from the response. This parameter is valid only for OSS asset queries.
        self.file_type = file_type
        # The keyword of the asset instance ID.
        self.instance_id = instance_id
        # Specifies whether to filter revision items.
        self.is_revision = is_revision
        # The language of the request and response. Default value: **zh_cn**. Valid values:
        # - **zh_cn**: Chinese.
        # - **en_us**: English.
        self.lang = lang
        # The SLS Logstore filter.
        self.log_store = log_store
        # The data catalog SLS page has two layers. This parameter indicates whether the query is at the Logstore dimension.
        self.log_store_flag = log_store_flag
        # The member accounts ID.
        self.member_account = member_account
        # The model IDs of the industry template, separated by commas.
        # > You can call [DescribeTemplateAllRules](https://help.aliyun.com/document_detail/2536491.html) to obtain the industry template model IDs.
        self.model_ids = model_ids
        # The data tags to query, separated by commas. Valid values:
        # - **101**: personal sensitive information.
        # - **102**: personal information.
        # - **107**: general information.
        self.model_tag_ids = model_tag_ids
        # The maximum number of data asset instances to return per page in a paged query. Default value: **10**.
        self.page_size = page_size
        # The list of parent category IDs of the templates to query, separated by commas.
        self.parent_category_ids = parent_category_ids
        # The file path filter.
        self.path = path
        # The product of the data catalog.
        self.product_id = product_id
        # We recommend that you specify this parameter. The list of product IDs to query, separated by commas. Valid values:
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
        # > OSS is mutually exclusive with other products. If OSS is included in the query, no other products can be specified. By default, non-OSS products are queried.
        self.product_ids = product_ids
        # The SLS project filter.
        self.project = project
        # The keyword of the data object to query.
        self.query_name = query_name
        # The region of the data catalog display page.
        self.region_id = region_id
        # The risk level filter.
        self.risk_level_id_list = risk_level_id_list
        # The risk levels of the data assets to query. Separate multiple values with commas (,).
        # - **2**: S1, low risk level.
        # - **3**: S2, medium risk level.
        # - **4**: S3, high risk level.
        # - **5**: S4, highest risk level.
        self.risk_levels = risk_levels
        # The rule filter.
        self.rule_ids = rule_ids
        # The region where the asset resides. Valid values:
        # - **cn-beijing**: China (Beijing).
        # - **cn-zhangjiakou**: China (Zhangjiakou).
        # - **cn-huhehaote**: China (Hohhot).
        # - **cn-hangzhou**: China (Hangzhou).
        # - **cn-shanghai**: China (Shanghai).
        # - **cn-shenzhen**: China (Shenzhen).
        # - **cn-hongkong**: Hong Kong (China).
        self.service_region_id = service_region_id
        # The task name filter.
        self.table_name = table_name
        # The task ID filter.
        self.task_id = task_id
        # The industry template ID.
        # 
        # > You can call [DescribeCategoryTemplateList](https://help.aliyun.com/document_detail/2399296.html) to obtain the industry template ID.
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
        if self.apiversion is not None:
            result['APIVersion'] = self.apiversion

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.cursor is not None:
            result['Cursor'] = self.cursor

        if self.cursor_direction is not None:
            result['CursorDirection'] = self.cursor_direction

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.facet_type is not None:
            result['FacetType'] = self.facet_type

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.file_category_code is not None:
            result['FileCategoryCode'] = self.file_category_code

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_revision is not None:
            result['IsRevision'] = self.is_revision

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.log_store_flag is not None:
            result['LogStoreFlag'] = self.log_store_flag

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

        if self.path is not None:
            result['Path'] = self.path

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_ids is not None:
            result['ProductIds'] = self.product_ids

        if self.project is not None:
            result['Project'] = self.project

        if self.query_name is not None:
            result['QueryName'] = self.query_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.risk_level_id_list is not None:
            result['RiskLevelIdList'] = self.risk_level_id_list

        if self.risk_levels is not None:
            result['RiskLevels'] = self.risk_levels

        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APIVersion') is not None:
            self.apiversion = m.get('APIVersion')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')

        if m.get('CursorDirection') is not None:
            self.cursor_direction = m.get('CursorDirection')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('FacetType') is not None:
            self.facet_type = m.get('FacetType')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('FileCategoryCode') is not None:
            self.file_category_code = m.get('FileCategoryCode')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsRevision') is not None:
            self.is_revision = m.get('IsRevision')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('LogStoreFlag') is not None:
            self.log_store_flag = m.get('LogStoreFlag')

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

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductIds') is not None:
            self.product_ids = m.get('ProductIds')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('QueryName') is not None:
            self.query_name = m.get('QueryName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RiskLevelIdList') is not None:
            self.risk_level_id_list = m.get('RiskLevelIdList')

        if m.get('RiskLevels') is not None:
            self.risk_levels = m.get('RiskLevels')

        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

