# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListManagedRulesResponseBody(DaraModel):
    def __init__(
        self,
        managed_rules: main_models.ListManagedRulesResponseBodyManagedRules = None,
        request_id: str = None,
    ):
        # The managed rules.
        self.managed_rules = managed_rules
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.managed_rules:
            self.managed_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.managed_rules is not None:
            result['ManagedRules'] = self.managed_rules.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedRules') is not None:
            temp_model = main_models.ListManagedRulesResponseBodyManagedRules()
            self.managed_rules = temp_model.from_map(m.get('ManagedRules'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListManagedRulesResponseBodyManagedRules(DaraModel):
    def __init__(
        self,
        managed_rule_list: List[main_models.ListManagedRulesResponseBodyManagedRulesManagedRuleList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The details of the managed rule.
        self.managed_rule_list = managed_rule_list
        # The page number.
        # 
        # Page start from page 1.
        self.page_number = page_number
        # The number of entries returned per page. Valid values: 1 to 500.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.managed_rule_list:
            for v1 in self.managed_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ManagedRuleList'] = []
        if self.managed_rule_list is not None:
            for k1 in self.managed_rule_list:
                result['ManagedRuleList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.managed_rule_list = []
        if m.get('ManagedRuleList') is not None:
            for k1 in m.get('ManagedRuleList'):
                temp_model = main_models.ListManagedRulesResponseBodyManagedRulesManagedRuleList()
                self.managed_rule_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListManagedRulesResponseBodyManagedRulesManagedRuleList(DaraModel):
    def __init__(
        self,
        config_rule_name: str = None,
        description: str = None,
        help_urls: str = None,
        identifier: str = None,
        labels: List[str] = None,
        remediation_template_identifier: str = None,
        remediation_template_name: str = None,
        risk_level: int = None,
        scope: main_models.ListManagedRulesResponseBodyManagedRulesManagedRuleListScope = None,
        support_preview_managed_rule: bool = None,
    ):
        # The name of the managed rule.
        self.config_rule_name = config_rule_name
        # The description of the managed rule.
        self.description = description
        # The URL of the topic that describes how the managed rule remediates the incompliant configurations.
        self.help_urls = help_urls
        # The unique identifier of the managed rule.
        self.identifier = identifier
        # The classification description of the managed rule.
        self.labels = labels
        # The ID of the remediation template.
        self.remediation_template_identifier = remediation_template_identifier
        # The name of the remediation template.
        self.remediation_template_name = remediation_template_name
        # The risk level of the resources that do not comply with the rule. Valid values:
        # 
        # *   1: high
        # *   2: medium
        # *   3: low
        self.risk_level = risk_level
        # The effective scope of the managed rule.
        self.scope = scope
        # Indicates whether precheck is supported. Valid values:
        # 
        # *   true
        # *   false
        self.support_preview_managed_rule = support_preview_managed_rule

    def validate(self):
        if self.scope:
            self.scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name

        if self.description is not None:
            result['Description'] = self.description

        if self.help_urls is not None:
            result['HelpUrls'] = self.help_urls

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.remediation_template_identifier is not None:
            result['RemediationTemplateIdentifier'] = self.remediation_template_identifier

        if self.remediation_template_name is not None:
            result['RemediationTemplateName'] = self.remediation_template_name

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.scope is not None:
            result['Scope'] = self.scope.to_map()

        if self.support_preview_managed_rule is not None:
            result['SupportPreviewManagedRule'] = self.support_preview_managed_rule

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HelpUrls') is not None:
            self.help_urls = m.get('HelpUrls')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('RemediationTemplateIdentifier') is not None:
            self.remediation_template_identifier = m.get('RemediationTemplateIdentifier')

        if m.get('RemediationTemplateName') is not None:
            self.remediation_template_name = m.get('RemediationTemplateName')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Scope') is not None:
            temp_model = main_models.ListManagedRulesResponseBodyManagedRulesManagedRuleListScope()
            self.scope = temp_model.from_map(m.get('Scope'))

        if m.get('SupportPreviewManagedRule') is not None:
            self.support_preview_managed_rule = m.get('SupportPreviewManagedRule')

        return self

class ListManagedRulesResponseBodyManagedRulesManagedRuleListScope(DaraModel):
    def __init__(
        self,
        compliance_resource_types: List[str] = None,
    ):
        # The types of resources to which the managed rule applies.
        self.compliance_resource_types = compliance_resource_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_resource_types is not None:
            result['ComplianceResourceTypes'] = self.compliance_resource_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceResourceTypes') is not None:
            self.compliance_resource_types = m.get('ComplianceResourceTypes')

        return self

