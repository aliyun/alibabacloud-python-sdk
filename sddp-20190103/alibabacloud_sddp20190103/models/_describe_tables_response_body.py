# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeTablesResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeTablesResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # An array that consists of tables.
        self.items = items
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeTablesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTablesResponseBodyItems(DaraModel):
    def __init__(
        self,
        creation_time: int = None,
        id: int = None,
        instance_description: str = None,
        instance_id: int = None,
        instance_name: str = None,
        name: str = None,
        owner: str = None,
        product_code: str = None,
        product_id: str = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        rule_list: List[main_models.DescribeTablesResponseBodyItemsRuleList] = None,
        sensitive: bool = None,
        sensitive_count: int = None,
        sensitive_ratio: str = None,
        tenant_name: str = None,
        total_count: int = None,
    ):
        # The point in time when the table was created. Unit: milliseconds.
        self.creation_time = creation_time
        # The ID of the table.
        self.id = id
        # The description of the data asset.
        self.instance_description = instance_description
        # The ID of the data asset to which the table belongs.
        self.instance_id = instance_id
        # The name of the data asset to which the table belongs.
        self.instance_name = instance_name
        # The name of the table.
        self.name = name
        # The Alibaba Cloud account to which the table belongs.
        self.owner = owner
        # The name of the service to which the table belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**. For more information about the types of data assets from which DSC can scan for sensitive data, see [Supported data assets](https://help.aliyun.com/document_detail/212906.html).
        self.product_code = product_code
        # The ID of the service to which the table belongs.
        self.product_id = product_id
        # The sensitivity level of the table. Each sensitivity level ID corresponds to a sensitivity level name. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id
        # The name of the sensitivity level for the table. Valid values:
        # 
        # *   **N/A**: indicates that no sensitive data is detected.
        # *   **S1**: indicates the low sensitivity level.
        # *   **S2**: indicates the medium sensitivity level.
        # *   **S3**: indicates the high sensitivity level.
        # *   **S4**: indicates the highest sensitivity level.
        self.risk_level_name = risk_level_name
        # The information about the sensitive data detection rules that are hit.
        self.rule_list = rule_list
        # Indicates whether the table contains sensitive fields. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.sensitive = sensitive
        # The total number of sensitive fields in the table.
        self.sensitive_count = sensitive_count
        # The percentage of sensitive fields in the table.
        self.sensitive_ratio = sensitive_ratio
        # The name of the tenant.
        self.tenant_name = tenant_name
        # The total number of fields in the table.
        self.total_count = total_count

    def validate(self):
        if self.rule_list:
            for v1 in self.rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name

        result['RuleList'] = []
        if self.rule_list is not None:
            for k1 in self.rule_list:
                result['RuleList'].append(k1.to_map() if k1 else None)

        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive

        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count

        if self.sensitive_ratio is not None:
            result['SensitiveRatio'] = self.sensitive_ratio

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')

        self.rule_list = []
        if m.get('RuleList') is not None:
            for k1 in m.get('RuleList'):
                temp_model = main_models.DescribeTablesResponseBodyItemsRuleList()
                self.rule_list.append(temp_model.from_map(k1))

        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')

        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')

        if m.get('SensitiveRatio') is not None:
            self.sensitive_ratio = m.get('SensitiveRatio')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTablesResponseBodyItemsRuleList(DaraModel):
    def __init__(
        self,
        count: int = None,
        name: str = None,
        risk_level_id: int = None,
    ):
        # The total number of rules.
        self.count = count
        # The name of the rule.
        self.name = name
        # The sensitivity level of the sensitive data that hits the sensitive data detection rule. Valid values:
        # 
        # *   **1**: N/A, which indicates that no sensitive data is detected.
        # *   **2**: S1, which indicates the low sensitivity level.
        # *   **3**: S2, which indicates the medium sensitivity level.
        # *   **4**: S3, which indicates the high sensitivity level.
        # *   **5**: S4, which indicates the highest sensitivity level.
        self.risk_level_id = risk_level_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.name is not None:
            result['Name'] = self.name

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        return self

