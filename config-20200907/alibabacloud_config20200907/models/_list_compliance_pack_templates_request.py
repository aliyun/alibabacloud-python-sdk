# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCompliancePackTemplatesRequest(DaraModel):
    def __init__(
        self,
        compliance_pack_template_id: str = None,
        filter_type: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_types: str = None,
        rule_risk_level: int = None,
    ):
        # The ID of the compliance package template.
        self.compliance_pack_template_id = compliance_pack_template_id
        self.filter_type = filter_type
        # The page number.
        # 
        # Pages start from page 1. Default value: 1
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100. Minimum value: 1. Default value: 10.
        self.page_size = page_size
        # The types of the resources evaluated based on the rule. If you configure this parameter, only the rules that include the resource types in the compliance package template are returned.
        self.resource_types = resource_types
        self.rule_risk_level = rule_risk_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id

        if self.filter_type is not None:
            result['FilterType'] = self.filter_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        if self.rule_risk_level is not None:
            result['RuleRiskLevel'] = self.rule_risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')

        if m.get('FilterType') is not None:
            self.filter_type = m.get('FilterType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        if m.get('RuleRiskLevel') is not None:
            self.rule_risk_level = m.get('RuleRiskLevel')

        return self

