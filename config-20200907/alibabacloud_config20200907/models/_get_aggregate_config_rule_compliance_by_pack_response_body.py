# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetAggregateConfigRuleComplianceByPackResponseBody(DaraModel):
    def __init__(
        self,
        config_rule_compliance_result: main_models.GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResult = None,
        request_id: str = None,
    ):
        # The compliance results of the rules in the compliance pack.
        self.config_rule_compliance_result = config_rule_compliance_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.config_rule_compliance_result:
            self.config_rule_compliance_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_rule_compliance_result is not None:
            result['ConfigRuleComplianceResult'] = self.config_rule_compliance_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleComplianceResult') is not None:
            temp_model = main_models.GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResult()
            self.config_rule_compliance_result = temp_model.from_map(m.get('ConfigRuleComplianceResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResult(DaraModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        compliant_count: int = None,
        config_rule_compliances: List[main_models.GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResultConfigRuleCompliances] = None,
        ignored_count: int = None,
        insufficient_data_count: int = None,
        non_compliant_count: int = None,
        not_applicable_count: int = None,
        total_count: int = None,
    ):
        # The ID of the compliance pack.
        self.compliance_pack_id = compliance_pack_id
        # The total number of rules for which all evaluation results are **Compliant**.
        self.compliant_count = compliant_count
        # A list of rule compliance results.
        self.config_rule_compliances = config_rule_compliances
        # The total number of rules whose evaluation results include **Ignored**.
        self.ignored_count = ignored_count
        # The total number of rules whose evaluation results include **Insufficient Data**.
        self.insufficient_data_count = insufficient_data_count
        # The number of non-compliant rules.
        self.non_compliant_count = non_compliant_count
        # The total number of rules whose evaluation results include **Not Applicable**.
        self.not_applicable_count = not_applicable_count
        # The total number of rules.
        self.total_count = total_count

    def validate(self):
        if self.config_rule_compliances:
            for v1 in self.config_rule_compliances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.compliant_count is not None:
            result['CompliantCount'] = self.compliant_count

        result['ConfigRuleCompliances'] = []
        if self.config_rule_compliances is not None:
            for k1 in self.config_rule_compliances:
                result['ConfigRuleCompliances'].append(k1.to_map() if k1 else None)

        if self.ignored_count is not None:
            result['IgnoredCount'] = self.ignored_count

        if self.insufficient_data_count is not None:
            result['InsufficientDataCount'] = self.insufficient_data_count

        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count

        if self.not_applicable_count is not None:
            result['NotApplicableCount'] = self.not_applicable_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('CompliantCount') is not None:
            self.compliant_count = m.get('CompliantCount')

        self.config_rule_compliances = []
        if m.get('ConfigRuleCompliances') is not None:
            for k1 in m.get('ConfigRuleCompliances'):
                temp_model = main_models.GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResultConfigRuleCompliances()
                self.config_rule_compliances.append(temp_model.from_map(k1))

        if m.get('IgnoredCount') is not None:
            self.ignored_count = m.get('IgnoredCount')

        if m.get('InsufficientDataCount') is not None:
            self.insufficient_data_count = m.get('InsufficientDataCount')

        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')

        if m.get('NotApplicableCount') is not None:
            self.not_applicable_count = m.get('NotApplicableCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetAggregateConfigRuleComplianceByPackResponseBodyConfigRuleComplianceResultConfigRuleCompliances(DaraModel):
    def __init__(
        self,
        compliance_type: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
    ):
        # The compliance result. Valid values:
        # 
        # - COMPLIANT: The rule is compliant.
        # 
        # - NON_COMPLIANT: The rule is non-compliant.
        # 
        # - NOT_APPLICABLE: The rule is not applicable.
        # 
        # - INSUFFICIENT_DATA: No data is available.
        self.compliance_type = compliance_type
        # The ID of the rule in the compliance pack.
        self.config_rule_id = config_rule_id
        # The name of the rule in the compliance pack.
        self.config_rule_name = config_rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type

        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')

        return self

