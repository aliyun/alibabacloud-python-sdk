# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConfigRulesShrinkRequest(DaraModel):
    def __init__(
        self,
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
        tag_shrink: str = None,
    ):
        # The compliance package ID.
        # 
        # For more information about how to obtain the ID of a compliance package, see [ListCompliancePacks](https://help.aliyun.com/document_detail/606968.html).
        # 
        # >  You must configure either the `CompliancePackId` or `ConfigRuleId` parameter.
        self.compliance_pack_id = compliance_pack_id
        # The compliance evaluation result of the rule. Valid values:
        # 
        # *   COMPLIANT: The resources are evaluated as compliant.
        # *   NON_COMPLIANT: The resources are evaluated as non-compliant.
        # *   NOT_APPLICABLE: The rule does not apply to the resources.
        # *   INSUFFICIENT_DATA: No resource data is available.
        self.compliance_type = compliance_type
        # The name of the rule.
        self.config_rule_name = config_rule_name
        # The status of the rule. Valid values:
        # 
        # *   ACTIVE: The rule is enabled.
        # *   DELETING: The rule is being deleted.
        # *   EVALUATING: The rule is being used to evaluate resource configurations.
        # *   INACTIVE: The rule is disabled.
        self.config_rule_state = config_rule_state
        # The query keyword.
        # 
        # You can perform a fuzzy search by rule ID, rule name, rule description, or managed rule ID.
        self.keyword = keyword
        # The page number.
        # 
        # Page numbers start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100. A minimum of 1 entry can be returned per page. Default value: 10.
        self.page_size = page_size
        # The type of the resources to be evaluated based on the rule.
        self.resource_types = resource_types
        # The risk level of the resources that are not compliant with the rule. Valid values:
        # 
        # *   1: high
        # *   2: medium
        # *   3: low
        self.risk_level = risk_level
        self.sort_by = sort_by
        # The tags of the resource.
        # 
        # You can add up to 20 tags to a resource.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

