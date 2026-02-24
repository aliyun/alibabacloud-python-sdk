# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetComplianceSummaryResponseBody(DaraModel):
    def __init__(
        self,
        compliance_summary: main_models.GetComplianceSummaryResponseBodyComplianceSummary = None,
        request_id: str = None,
    ):
        # The compliance summary.
        self.compliance_summary = compliance_summary
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.compliance_summary:
            self.compliance_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_summary is not None:
            result['ComplianceSummary'] = self.compliance_summary.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceSummary') is not None:
            temp_model = main_models.GetComplianceSummaryResponseBodyComplianceSummary()
            self.compliance_summary = temp_model.from_map(m.get('ComplianceSummary'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetComplianceSummaryResponseBodyComplianceSummary(DaraModel):
    def __init__(
        self,
        compliance_summary_by_config_rule: main_models.GetComplianceSummaryResponseBodyComplianceSummaryComplianceSummaryByConfigRule = None,
        compliance_summary_by_resource: main_models.GetComplianceSummaryResponseBodyComplianceSummaryComplianceSummaryByResource = None,
    ):
        # The compliance summary by rule.
        self.compliance_summary_by_config_rule = compliance_summary_by_config_rule
        # The compliance summary by resource.
        self.compliance_summary_by_resource = compliance_summary_by_resource

    def validate(self):
        if self.compliance_summary_by_config_rule:
            self.compliance_summary_by_config_rule.validate()
        if self.compliance_summary_by_resource:
            self.compliance_summary_by_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_summary_by_config_rule is not None:
            result['ComplianceSummaryByConfigRule'] = self.compliance_summary_by_config_rule.to_map()

        if self.compliance_summary_by_resource is not None:
            result['ComplianceSummaryByResource'] = self.compliance_summary_by_resource.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceSummaryByConfigRule') is not None:
            temp_model = main_models.GetComplianceSummaryResponseBodyComplianceSummaryComplianceSummaryByConfigRule()
            self.compliance_summary_by_config_rule = temp_model.from_map(m.get('ComplianceSummaryByConfigRule'))

        if m.get('ComplianceSummaryByResource') is not None:
            temp_model = main_models.GetComplianceSummaryResponseBodyComplianceSummaryComplianceSummaryByResource()
            self.compliance_summary_by_resource = temp_model.from_map(m.get('ComplianceSummaryByResource'))

        return self

class GetComplianceSummaryResponseBodyComplianceSummaryComplianceSummaryByResource(DaraModel):
    def __init__(
        self,
        compliance_summary_timestamp: int = None,
        compliant_count: int = None,
        high_risk_rule_non_compliant_resource_count: int = None,
        low_risk_rule_non_compliant_resource_count: int = None,
        medium_risk_rule_non_compliant_resource_count: int = None,
        non_compliant_count: int = None,
        total_count: int = None,
    ):
        # The timestamp when the compliance summary was generated. Unit: milliseconds.
        self.compliance_summary_timestamp = compliance_summary_timestamp
        # The number of compliant resources.
        self.compliant_count = compliant_count
        # The number of non-compliant resources detected by high-risk rules.
        # 
        # > Note: This value can be greater than the total number of resources in your account. Resources are counted based on each rule. For example, if a resource is evaluated as non-compliant by two rules, the value of this parameter increases by 2.
        self.high_risk_rule_non_compliant_resource_count = high_risk_rule_non_compliant_resource_count
        # The number of non-compliant resources detected by low-risk rules.
        # 
        # > Note: This value can be greater than the total number of resources in your account. Resources are counted based on each rule. For example, if a resource is evaluated as non-compliant by two low-risk rules, the value of this parameter increases by 2.
        self.low_risk_rule_non_compliant_resource_count = low_risk_rule_non_compliant_resource_count
        # The number of non-compliant resources detected by medium-risk rules.
        # 
        # > Note: This value can be greater than the total number of resources in your account. Resources are counted based on each rule. For example, if a resource is evaluated as non-compliant by two rules, the value of this parameter increases by 2.
        self.medium_risk_rule_non_compliant_resource_count = medium_risk_rule_non_compliant_resource_count
        # The number of non-compliant resources.
        self.non_compliant_count = non_compliant_count
        # The total number of resources.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_summary_timestamp is not None:
            result['ComplianceSummaryTimestamp'] = self.compliance_summary_timestamp

        if self.compliant_count is not None:
            result['CompliantCount'] = self.compliant_count

        if self.high_risk_rule_non_compliant_resource_count is not None:
            result['HighRiskRuleNonCompliantResourceCount'] = self.high_risk_rule_non_compliant_resource_count

        if self.low_risk_rule_non_compliant_resource_count is not None:
            result['LowRiskRuleNonCompliantResourceCount'] = self.low_risk_rule_non_compliant_resource_count

        if self.medium_risk_rule_non_compliant_resource_count is not None:
            result['MediumRiskRuleNonCompliantResourceCount'] = self.medium_risk_rule_non_compliant_resource_count

        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceSummaryTimestamp') is not None:
            self.compliance_summary_timestamp = m.get('ComplianceSummaryTimestamp')

        if m.get('CompliantCount') is not None:
            self.compliant_count = m.get('CompliantCount')

        if m.get('HighRiskRuleNonCompliantResourceCount') is not None:
            self.high_risk_rule_non_compliant_resource_count = m.get('HighRiskRuleNonCompliantResourceCount')

        if m.get('LowRiskRuleNonCompliantResourceCount') is not None:
            self.low_risk_rule_non_compliant_resource_count = m.get('LowRiskRuleNonCompliantResourceCount')

        if m.get('MediumRiskRuleNonCompliantResourceCount') is not None:
            self.medium_risk_rule_non_compliant_resource_count = m.get('MediumRiskRuleNonCompliantResourceCount')

        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetComplianceSummaryResponseBodyComplianceSummaryComplianceSummaryByConfigRule(DaraModel):
    def __init__(
        self,
        compliance_summary_timestamp: int = None,
        compliant_count: int = None,
        non_compliant_count: int = None,
        total_count: int = None,
    ):
        # The timestamp when the compliance summary was generated. Unit: milliseconds.
        self.compliance_summary_timestamp = compliance_summary_timestamp
        # The number of compliant rules.
        self.compliant_count = compliant_count
        # The number of non-compliant rules.
        self.non_compliant_count = non_compliant_count
        # The total number of rules.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_summary_timestamp is not None:
            result['ComplianceSummaryTimestamp'] = self.compliance_summary_timestamp

        if self.compliant_count is not None:
            result['CompliantCount'] = self.compliant_count

        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceSummaryTimestamp') is not None:
            self.compliance_summary_timestamp = m.get('ComplianceSummaryTimestamp')

        if m.get('CompliantCount') is not None:
            self.compliant_count = m.get('CompliantCount')

        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

