# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeCategoryTemplateRuleListResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeCategoryTemplateRuleListResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # A list of template rules.
        self.items = items
        # The number of template rules returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of rules in the template.
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
                temp_model = main_models.DescribeCategoryTemplateRuleListResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCategoryTemplateRuleListResponseBodyItems(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        identification_rule_ids: str = None,
        identification_scope: str = None,
        name: str = None,
        risk_level_id: int = None,
        status: int = None,
    ):
        # The description of the rule.
        self.description = description
        # The unique ID of the template rule.
        self.id = id
        # A comma-separated list of IDs of the associated atomic models.
        self.identification_rule_ids = identification_rule_ids
        # The scope of data that the template rule scans. This parameter is a string converted from a JSON array. Each element in the JSON array represents a data scanning scope and contains the following fields:
        # 
        # - **Asset**: A string that indicates the asset type. Valid values include RDS, DRDS, PolarDB, OTS, ADB, OceanBase, and ODPS.
        # 
        # - **Content**: The specific scope of the asset to scan. This is an array of objects, where each object contains the following fields:
        # 
        #   - **Range**: A string that indicates the matching range. Valid values include instance, database, table, column, project (for MaxCompute assets only), bucket (for OSS assets only), and object (for OSS assets only).
        # 
        #   - **Operator**: A string that indicates the matching condition. Valid values include equals, regex (regular expression), prefix, and suffix.
        # 
        #   - **Value**: A string that indicates the content to match.
        self.identification_scope = identification_scope
        # The name of the template rule.
        self.name = name
        # The risk level of the template rule. The value ranges from **1** to **11**. Valid values:
        # 
        # - **1**: No risk.
        # 
        # - **2**: S1.
        # 
        # - **3**: S2.
        # 
        # - **4**: S3.
        # 
        # - **5**: S4.
        # 
        # - **6**: S5.
        # 
        # - **7**: S6.
        # 
        # - **8**: S7.
        # 
        # - **9**: S8.
        # 
        # - **10**: S9.
        # 
        # - **11**: S10.
        # 
        # - **null**: Indicates all risk levels, including No risk, S1, S2, S3, S4, S5, S6, S7, S8, S9, and S10.
        self.risk_level_id = risk_level_id
        # The status of the template rule. Valid values:
        # 
        # - **0**: disabled.
        # 
        # - **1**: enabled.
        # 
        # - **null**: Represents all statuses, including enabled and disabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.identification_rule_ids is not None:
            result['IdentificationRuleIds'] = self.identification_rule_ids

        if self.identification_scope is not None:
            result['IdentificationScope'] = self.identification_scope

        if self.name is not None:
            result['Name'] = self.name

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdentificationRuleIds') is not None:
            self.identification_rule_ids = m.get('IdentificationRuleIds')

        if m.get('IdentificationScope') is not None:
            self.identification_scope = m.get('IdentificationScope')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

