# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeColumnsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        engine_type: str = None,
        instance_id: int = None,
        instance_name: str = None,
        lang: str = None,
        model_tag_id: str = None,
        name: str = None,
        page_size: int = None,
        product_code: str = None,
        product_id: str = None,
        risk_level_id: int = None,
        rule_id: int = None,
        rule_name: str = None,
        sens_level_name: str = None,
        service_region_id: str = None,
        table_id: int = None,
        table_name: str = None,
        template_id: str = None,
        template_rule_id: str = None,
    ):
        # The page number for a paged query.
        self.current_page = current_page
        # The database engine type. Valid values:
        # - **MySQL**
        # - **MariaDB**
        # - **Oracle**
        # - **PostgreSQL**
        # - **SQLServer**
        self.engine_type = engine_type
        # The ID of the asset instance to which the column data in the data asset table belongs.
        # 
        # > Queries column data in data asset tables authorized for connection by Data Security Center based on the asset instance ID. You can call the [DescribeInstances](~~DescribeRules~~) operation to obtain the instance ID.
        self.instance_id = instance_id
        # The name of the asset instance to which the column data in the data asset table belongs.
        self.instance_name = instance_name
        # The language of the request and response. Default value: **zh_cn**. Valid values:
        # - **zh_cn**: Chinese.
        # - **en_us**: English.
        self.lang = lang
        # The data tag.
        # 
        # - 101: personal sensitive information
        # 
        # - 102: personal information
        self.model_tag_id = model_tag_id
        # The keyword to search for. Fuzzy match is supported.
        # 
        # For example, if you enter **test**, all data entries that contain **test** in the search fields are returned.
        self.name = name
        # The maximum number of entries per page.
        self.page_size = page_size
        # The name of the product to which the column data in the data asset table belongs. Valid values: **MaxCompute, OSS, ADS, OTS, RDS**, and others.
        self.product_code = product_code
        # The ID that corresponds to the product name to which the data object belongs. Valid values:
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
        self.product_id = product_id
        # The risk level ID of the sensitive data detection rule. Valid values:
        # - **1**: N/A.
        # - **2**: S1.
        # - **3**: S2.
        # - **4**: S3.
        # - **5**: S4.
        self.risk_level_id = risk_level_id
        # The unique ID of the sensitive data detection rule that the column data matches.
        # 
        # > Queries column data in data asset tables authorized for connection by Data Security Center based on the ID of the sensitive data detection rule that the column data matches. You can call the [DescribeRules](~~DescribeRules~~) operation to obtain the rule ID.
        self.rule_id = rule_id
        # The name of the sensitive data detection rule that the column data in the data asset table matches.
        self.rule_name = rule_name
        # The sensitivity level name. Valid values:
        # - **N/A**: No sensitive data is detected.
        # - **S1**: Level-1 sensitive data.
        # - **S2**: Level-2 sensitive data.
        # - **S3**: Level-3 sensitive data.
        # - **S4**: Level-4 sensitive data.
        self.sens_level_name = sens_level_name
        self.service_region_id = service_region_id
        # The unique ID of the data asset table to which the columns belong in MaxCompute, ApsaraDB RDS, or other assets.
        # 
        # > Queries column data in data asset tables authorized for connection by Data Security Center based on the table ID. You can call the [DescribeTables](~~DescribeTables~~) operation to obtain the table ID.
        self.table_id = table_id
        # The name of the data asset table.
        self.table_name = table_name
        # The industry template ID.
        # > You can call the [DescribeCategoryTemplateList](https://help.aliyun.com/document_detail/2399296.html) operation to obtain the industry template ID.
        self.template_id = template_id
        # The ID of the matched template rule.
        # > You can call the [DescribeCategoryTemplateRuleList](https://help.aliyun.com/document_detail/410143.html) operation to obtain the matched template rule ID.
        self.template_rule_id = template_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.model_tag_id is not None:
            result['ModelTagId'] = self.model_tag_id

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sens_level_name is not None:
            result['SensLevelName'] = self.sens_level_name

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_rule_id is not None:
            result['TemplateRuleId'] = self.template_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ModelTagId') is not None:
            self.model_tag_id = m.get('ModelTagId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SensLevelName') is not None:
            self.sens_level_name = m.get('SensLevelName')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateRuleId') is not None:
            self.template_rule_id = m.get('TemplateRuleId')

        return self

