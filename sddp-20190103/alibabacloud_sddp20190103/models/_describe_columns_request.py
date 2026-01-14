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
        table_id: int = None,
        table_name: str = None,
        template_id: str = None,
        template_rule_id: str = None,
    ):
        # The page number of the page to return.
        self.current_page = current_page
        # The engine type. Valid values:
        # 
        # *   **MySQL**
        # *   **MariaDB**
        # *   **Oracle**
        # *   **PostgreSQL**
        # *   **SQLServer**
        self.engine_type = engine_type
        # The ID of the instance to which data in the column of the table belongs.
        # 
        # > You can call the [DescribeInstances](~~DescribeRules~~) operation to query the IDs of instances.
        self.instance_id = instance_id
        # The name of the instance to which data in the column of the table belongs.
        self.instance_name = instance_name
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Chinese
        # *   **en_us**: English
        self.lang = lang
        # The data tag.
        # 
        # *   101: personal sensitive information
        # *   102: personal information
        self.model_tag_id = model_tag_id
        # The search keyword. Fuzzy match is supported.
        # 
        # For example, if you enter **test**, all columns whose names contain **test** are retrieved.
        self.name = name
        # The number of entries to return on each page.
        self.page_size = page_size
        # The name of the service to which data in the column of the table belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.product_code = product_code
        # The ID of the service to which the data object belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: Object Storage Service (OSS)
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore (OTS)
        # *   **5**: ApsaraDB RDS
        # *   **6**: self-managed database
        # *   **7**: PolarDB for Xscale (PolarDB-X)
        # *   **8**: PolarDB
        # *   **9**: AnalyticDB for PostgreSQL
        # *   **10**: ApsaraDB for OceanBase
        # *   **11**: ApsaraDB for MongoDB
        # *   **25**: ApsaraDB for Redis
        self.product_id = product_id
        # The sensitivity level of the sensitive data that hits the sensitive data detection rule. Valid values:
        # 
        # *   **1**: N/A
        # *   **2**: S1
        # *   **3**: S2
        # *   **4**: S3
        # *   **5**: S4
        self.risk_level_id = risk_level_id
        # The ID of the sensitive data detection rule that data in the column of the table hits.
        # 
        # > You can call the [DescribeRules](~~DescribeRules~~) operation to query the IDs of sensitive data detection rules.
        self.rule_id = rule_id
        # The name of the sensitive data detection rule that data in the column of the table hits.
        self.rule_name = rule_name
        # The name of the sensitivity level of the data that hits the sensitive data detection rule. Valid values:
        # 
        # *   **N/A**: No sensitive data is detected.
        # *   **S1**: indicates the low sensitivity level.
        # *   **S2**: indicates the medium sensitivity level.
        # *   **S3**: indicates the high sensitivity level.
        # *   **S4**: indicates the highest sensitivity level.
        self.sens_level_name = sens_level_name
        # The ID of the table to which the column belongs.
        # 
        # > You can call the [DescribeTables](~~DescribeTables~~) operation to query the IDs of tables.
        self.table_id = table_id
        # The name of the table.
        self.table_name = table_name
        # The ID of the industry-specific classification template.
        # 
        # >  You can call the [DescribeCategoryTemplateList](https://help.aliyun.com/document_detail/2399296.html) operation to obtain the IDs of industry-specific classification templates.
        self.template_id = template_id
        # The ID of the template rule that is hit.
        # 
        # >  You can call the [DescribeCategoryTemplateRuleList](https://help.aliyun.com/document_detail/410143.html) operation to obtain the IDs of hit template rules.
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

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateRuleId') is not None:
            self.template_rule_id = m.get('TemplateRuleId')

        return self

