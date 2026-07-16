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
        db_name: str = None,
        domain_id: int = None,
        feature_type: int = None,
        file_category_code: int = None,
        file_type: int = None,
        instance_id: str = None,
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
        # The version of the API.
        self.apiversion = apiversion
        # The name of the OSS bucket.
        self.bucket = bucket
        # The page number of the returned page. Default value: 1.
        self.current_page = current_page
        # The name of the database.
        self.db_name = db_name
        # The ID of the data domain to which the data asset belongs.
        self.domain_id = domain_id
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The code of the file category.
        self.file_category_code = file_category_code
        # The type of the OSS file.
        # 
        # > This parameter is valid only for querying data assets of the OSS type. You can call the [DescribeDocTypes](https://help.aliyun.com/document_detail/2536492.html) operation to obtain the supported OSS file types. Use the value of the `Code` parameter in the response.
        self.file_type = file_type
        # The keyword of the instance ID.
        self.instance_id = instance_id
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # - **zh_cn**: Chinese.
        # 
        # - **en_us**: English.
        self.lang = lang
        # The name of the Logstore.
        self.log_store = log_store
        # Specifies whether to query data at the Logstore level. The Simple Log Service data catalog has two layers. Set this parameter to 1 to query data at the Logstore level.
        self.log_store_flag = log_store_flag
        # The ID of the member.
        self.member_account = member_account
        # The model ID of the industry-specific rule template. You can specify multiple IDs. Separate them with commas (,).
        # 
        # > You can call the [DescribeTemplateAllRules](https://help.aliyun.com/document_detail/2536491.html) operation to obtain the model ID of the industry-specific rule template.
        self.model_ids = model_ids
        # The data labels to be queried. You can specify multiple data labels. Separate them with commas (,). Valid values:
        # 
        # - **101**: personal sensitive information
        # 
        # - **102**: personal information
        # 
        # - **107**: general information
        self.model_tag_ids = model_tag_ids
        # The number of data assets to return on each page. Default value: **10**.
        self.page_size = page_size
        # The IDs of the parent asset categories to be queried. You can specify multiple IDs. Separate them with commas (,).
        self.parent_category_ids = parent_category_ids
        # The path of the file.
        self.path = path
        # The ID of the product.
        self.product_id = product_id
        # The IDs of the products to which the data assets to be queried belong. You can specify multiple product IDs. Separate them with commas (,). We recommend that you specify this parameter. Valid values:
        # 
        # - **1**: MaxCompute
        # 
        # - **2**: OSS
        # 
        # - **3**: ADB-MYSQL
        # 
        # - **4**: TableStore
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
        # 
        # > If you want to query data assets that belong to OSS, you cannot query data assets of other products. By default, data assets of products other than OSS are queried.
        self.product_ids = product_ids
        # The name of the Simple Log Service project.
        self.project = project
        # The keyword of the data asset to be queried.
        self.query_name = query_name
        # The region in which the data asset catalog resides.
        self.region_id = region_id
        # The IDs of the sensitivity levels. You can specify multiple sensitivity level IDs. Separate them with commas (,).
        self.risk_level_id_list = risk_level_id_list
        # The sensitivity level of the data asset. You can specify multiple sensitivity levels. Separate them with commas (,).
        # 
        # - **2**: S1, low sensitivity level
        # 
        # - **3**: S2, medium sensitivity level
        # 
        # - **4**: S3, high sensitivity level
        # 
        # - **5**: S4, highest sensitivity level
        self.risk_levels = risk_levels
        # The IDs of the rules. You can specify multiple rule IDs. Separate them with commas (,).
        self.rule_ids = rule_ids
        # The region where the data asset resides. Valid values:
        # 
        # - **cn-beijing**: China (Beijing)
        # 
        # - **cn-zhangjiakou**: China (Zhangjiakou)
        # 
        # - **cn-huhehaote**: China (Hohhot)
        # 
        # - **cn-hangzhou**: China (Hangzhou)
        # 
        # - **cn-shanghai**: China (Shanghai)
        # 
        # - **cn-shenzhen**: China (Shenzhen)
        # 
        # - **cn-hongkong**: China (Hong Kong)
        self.service_region_id = service_region_id
        # The name of the table.
        self.table_name = table_name
        # The ID of the task.
        self.task_id = task_id
        # The ID of the industry-specific rule template.
        # 
        # > You can call the [DescribeCategoryTemplateList](https://help.aliyun.com/document_detail/2399296.html) operation to obtain the ID of the industry-specific rule template.
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

        if self.db_name is not None:
            result['DbName'] = self.db_name

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

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

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

