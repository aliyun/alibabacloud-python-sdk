# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListAggregateConfigRulesRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
        compliance_type: str = None,
        config_rule_name: str = None,
        config_rule_state: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_types: str = None,
        risk_level: int = None,
        sort_by: str = None,
        tag: List[main_models.ListAggregateConfigRulesRequestTag] = None,
    ):
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The compliance package ID.
        self.compliance_pack_id = compliance_pack_id
        # The compliance evaluation result. Valid values:
        # 
        # *   COMPLIANT: The resources are evaluated as compliant.
        # *   NON_COMPLIANT: The resources are evaluated as non-compliant.
        # *   NOT_APPLICABLE: The rule does not apply to the resources.
        # *   INSUFFICIENT_DATA: No data is available.
        self.compliance_type = compliance_type
        # The name of the rule.
        self.config_rule_name = config_rule_name
        # The status of the rule. Valid values:
        # 
        # *   ACTIVE: The rule is being used to monitor resource configurations.
        # *   DELETING: The rule is being deleted.
        # *   EVALUATING: The rule is triggered and is being used to monitor resource configurations.
        # *   INACTIVE: The rule is disabled.
        self.config_rule_state = config_rule_state
        # The keyword that is used for queries.
        # 
        # You can perform a fuzzy search by rule ID, rule name, rule description, or managed rule ID.
        self.keyword = keyword
        # The page number.
        # 
        # Pages start from page 1. Default value: 1
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100. Minimum value: 1. Default value: 10
        self.page_size = page_size
        # Resource type for the rule to evaluate.
        self.resource_types = resource_types
        # The risk level of the resources that do not comply with the rule. Valid values:
        # 
        # *   1: high
        # *   2: medium
        # *   3: low
        self.risk_level = risk_level
        self.sort_by = sort_by
        # The tags of the resource.
        # 
        # You can add up to 20 tags to a resource.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type

        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name

        if self.config_rule_state is not None:
            result['ConfigRuleState'] = self.config_rule_state

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')

        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')

        if m.get('ConfigRuleState') is not None:
            self.config_rule_state = m.get('ConfigRuleState')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListAggregateConfigRulesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListAggregateConfigRulesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # The tag key cannot be an empty string. The tag key can be up to 64 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can specify at most 20 tag keys.
        self.key = key
        # The value of the tag. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. The tag value cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

