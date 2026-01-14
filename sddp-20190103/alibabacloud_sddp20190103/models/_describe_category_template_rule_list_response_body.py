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
        # The page number of the returned page.
        self.current_page = current_page
        # The list of rules.
        self.items = items
        # The number of entries returned per page.
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
        # The unique ID of the rule.
        self.id = id
        # The IDs of sensitive data types. Multiple IDs are separated by commas (,).
        self.identification_rule_ids = identification_rule_ids
        # The scan scope of the rule. The value is a JSON array of the STRING type. Each element in a JSON array indicates a scan scope that contains the following fields:
        # 
        # *   **Asset**: the data asset type. Valid values: RDS, DRDS, PolarDB, OTS, ADB, and OceanBase. The value is of the STRING type.
        # 
        # *   **Content**: the scan scope. The value is of the STRING type. Each element in a JSON array indicates a scan scope that contains the following fields:
        # 
        #     *   **Range**: the matching condition. Valid values: Instance, database, table, column, project, bucket, and object. The value project is valid only for data assets in MaxCompute. The values bucket and object are valid only for data assets in Object Storage Service (OSS). The value of this parameter is of the STRING type.
        #     *   **Operator**: the operator. Valid values: equals, regex, prefix, and suffix. The operator equals indicates a full match. The operator regex indicates a match by regular expression. The operator prefix indicates a match by prefix. The operator suffix indicates a match by suffix.
        #     *   **Value**: the matching content. The value is of the STRING type.
        self.identification_scope = identification_scope
        # The name of the rule.
        self.name = name
        # The sensitivity level of the data that is not compliant with the rule. Valid values: **1** to **11**.
        # 
        # *   **1**: No sensitive data is detected.
        # *   **2**: indicates the S1 sensitivity level.
        # *   **3**: indicates the S2 sensitivity level.
        # *   **4**: indicates the S3 sensitivity level.
        # *   **5**: indicates the S4 sensitivity level.
        # *   **6**: indicates the S5 sensitivity level.
        # *   **7**: indicates the S6 sensitivity level.
        # *   **8**: indicates the S7 sensitivity level.
        # *   **9**: indicates the S8 sensitivity level.
        # *   **10**: indicates the S9 sensitivity level.
        # *   **11**: indicates the S10 sensitivity level.
        # *   **null**: indicates all preceding sensitivity levels.
        self.risk_level_id = risk_level_id
        # The status of the rule. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        # *   **null**: all states
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

