# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeColumnsV2Request(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        engine_type: str = None,
        instance_id: int = None,
        instance_name: str = None,
        lang: str = None,
        name: str = None,
        page_size: int = None,
        product_code: str = None,
        risk_level_id: int = None,
        rule_id: int = None,
        rule_name: str = None,
        sens_level_name: str = None,
        table_id: str = None,
        table_name: str = None,
    ):
        # When performing a paginated query, sets the current page number. Default value: **1**.
        self.current_page = current_page
        # Engine type. Values:
        # - **MySQL**.
        # - **MariaDB**.
        # - **Oracle**.
        # - **PostgreSQL**.
        # - **SQLServer**.
        self.engine_type = engine_type
        # ID of the asset instance to which the column data in the data asset table belongs.
        # 
        # > Query the data in the columns of the data assets authorized by the Data Security Center based on the ID of the asset instance to which the column data in the data asset table belongs. The asset instance ID can be obtained by calling the [DescribeInstances](https://help.aliyun.com/document_detail/141708.html) interface.
        self.instance_id = instance_id
        # Name of the asset instance to which the column data in the data asset table belongs.
        self.instance_name = instance_name
        # Sets the language type for requests and received messages, default is **zh_cn**.
        # Values:
        # 
        # - **zh_cn**: Simplified Chinese
        # - **en_us**: English (United States)
        self.lang = lang
        # Search keyword, supports fuzzy matching.
        # 
        # For example, entering **test** will search for all data information containing **test** in the search items.
        self.name = name
        # When performing a paginated query, sets the maximum number of data asset instances displayed per page. Default value: **10**.
        self.page_size = page_size
        # Product name to which the column data in the data asset table belongs. Values: **MaxCompute, OSS, ADS, OTS, RDS**, etc.
        self.product_code = product_code
        # Risk level ID of the sensitive data recognition rule. Values:
        # - **1**: N/A.
        # - **2**: S1.
        # - **3**: S2.
        # - **4**: S3.
        # - **5**: S4.
        self.risk_level_id = risk_level_id
        # Unique identifier ID of the sensitive data recognition rule hit by the column data in the asset table.
        # 
        # > Query the data in the columns of the data assets authorized by the Data Security Center based on the ID of the sensitive data recognition rule hit by the column data in the asset table. The sensitive data recognition rule ID can be obtained by calling the [DescribeRules](https://help.aliyun.com/document_detail/141389.html) interface.
        self.rule_id = rule_id
        # Name of the sensitive data recognition rule hit by the column data in the data asset table.
        self.rule_name = rule_name
        # Sensitive level name. Values:
        # - **N/A**: No sensitive data detected.
        # - **S1**: Level 1 sensitive data.
        # - **S2**: Level 2 sensitive data.
        # - **S3**: Level 3 sensitive data.
        # - **S4**: Level 4 sensitive data.
        self.sens_level_name = sens_level_name
        # Unique identifier ID of the asset table to which the column in MaxCompute, RDS, etc., belongs.
        # 
        # > Query the data in the columns of the data assets authorized by the Data Security Center based on the ID of the asset table. The asset table ID can be obtained by calling the [DescribeTables](https://help.aliyun.com/document_detail/141709.html) interface.
        self.table_id = table_id
        # Name of the data asset table.
        self.table_name = table_name

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

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

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

        return self

