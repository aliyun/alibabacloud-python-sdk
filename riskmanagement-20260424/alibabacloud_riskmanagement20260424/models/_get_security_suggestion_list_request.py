# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class GetSecuritySuggestionListRequest(DaraModel):
    def __init__(
        self,
        list_config_rules_request: main_models.GetSecuritySuggestionListRequestListConfigRulesRequest = None,
    ):
        self.list_config_rules_request = list_config_rules_request

    def validate(self):
        if self.list_config_rules_request:
            self.list_config_rules_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_config_rules_request is not None:
            result['ListConfigRulesRequest'] = self.list_config_rules_request.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListConfigRulesRequest') is not None:
            temp_model = main_models.GetSecuritySuggestionListRequestListConfigRulesRequest()
            self.list_config_rules_request = temp_model.from_map(m.get('ListConfigRulesRequest'))

        return self

class GetSecuritySuggestionListRequestListConfigRulesRequest(DaraModel):
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
    ):
        self.compliance_pack_id = compliance_pack_id
        self.compliance_type = compliance_type
        self.config_rule_name = config_rule_name
        self.config_rule_state = config_rule_state
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.resource_types = resource_types
        self.risk_level = risk_level

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

        return self

