# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListCompliancePackTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        compliance_pack_templates_result: main_models.ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResult = None,
        request_id: str = None,
    ):
        # The information about the compliance package templates returned.
        self.compliance_pack_templates_result = compliance_pack_templates_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.compliance_pack_templates_result:
            self.compliance_pack_templates_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_pack_templates_result is not None:
            result['CompliancePackTemplatesResult'] = self.compliance_pack_templates_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackTemplatesResult') is not None:
            temp_model = main_models.ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResult()
            self.compliance_pack_templates_result = temp_model.from_map(m.get('CompliancePackTemplatesResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResult(DaraModel):
    def __init__(
        self,
        compliance_pack_templates: List[main_models.ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplates] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The compliance package templates.
        self.compliance_pack_templates = compliance_pack_templates
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of the compliance package templates returned.
        self.total_count = total_count

    def validate(self):
        if self.compliance_pack_templates:
            for v1 in self.compliance_pack_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CompliancePackTemplates'] = []
        if self.compliance_pack_templates is not None:
            for k1 in self.compliance_pack_templates:
                result['CompliancePackTemplates'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliance_pack_templates = []
        if m.get('CompliancePackTemplates') is not None:
            for k1 in m.get('CompliancePackTemplates'):
                temp_model = main_models.ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplates()
                self.compliance_pack_templates.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplates(DaraModel):
    def __init__(
        self,
        compliance_pack_template_id: str = None,
        compliance_pack_template_name: str = None,
        config_rules: List[main_models.ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRules] = None,
        description: str = None,
        labels: str = None,
        last_update: int = None,
        risk_level: int = None,
    ):
        # The ID of the compliance package template.
        self.compliance_pack_template_id = compliance_pack_template_id
        # The name of the compliance package template.
        self.compliance_pack_template_name = compliance_pack_template_name
        # The default rules in the compliance package.
        self.config_rules = config_rules
        # The description of the compliance package.
        self.description = description
        # The tag of the compliance package.
        self.labels = labels
        # The time when the compliance package was last updated.
        self.last_update = last_update
        # The risk level of the managed rule in the compliance package. Valid values:
        # 
        # *   1: high
        # *   2: medium
        # *   3: low
        self.risk_level = risk_level

    def validate(self):
        if self.config_rules:
            for v1 in self.config_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id

        if self.compliance_pack_template_name is not None:
            result['CompliancePackTemplateName'] = self.compliance_pack_template_name

        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k1 in self.config_rules:
                result['ConfigRules'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.last_update is not None:
            result['LastUpdate'] = self.last_update

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')

        if m.get('CompliancePackTemplateName') is not None:
            self.compliance_pack_template_name = m.get('CompliancePackTemplateName')

        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k1 in m.get('ConfigRules'):
                temp_model = main_models.ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRules()
                self.config_rules.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('LastUpdate') is not None:
            self.last_update = m.get('LastUpdate')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRules(DaraModel):
    def __init__(
        self,
        config_rule_parameters: List[main_models.ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRulesConfigRuleParameters] = None,
        control_description: str = None,
        control_id: str = None,
        default_enable: bool = None,
        description: str = None,
        managed_rule_identifier: str = None,
        managed_rule_name: str = None,
        resource_types_scope: str = None,
        risk_level: int = None,
    ):
        # The input parameter of the managed rule.
        self.config_rule_parameters = config_rule_parameters
        # The description of the regulation. This parameter is available only for regulation compliance packages.
        self.control_description = control_description
        # The regulation ID.
        # 
        # >  This parameter is available only for regulation compliance packages.
        self.control_id = control_id
        # Indicates whether the rules are enabled together with the compliance package. Valid values:
        # 
        # *   true
        # *   false
        self.default_enable = default_enable
        # The description of the rule.
        self.description = description
        # The identifier of the managed rule.
        self.managed_rule_identifier = managed_rule_identifier
        # The name of the managed rule.
        self.managed_rule_name = managed_rule_name
        # The types of the resources evaluated based on the rule.
        self.resource_types_scope = resource_types_scope
        # The risk level of the managed rule. Valid values:
        # 
        # *   1: high
        # *   2: medium
        # *   3: low
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for v1 in self.config_rule_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k1 in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k1.to_map() if k1 else None)

        if self.control_description is not None:
            result['ControlDescription'] = self.control_description

        if self.control_id is not None:
            result['ControlId'] = self.control_id

        if self.default_enable is not None:
            result['DefaultEnable'] = self.default_enable

        if self.description is not None:
            result['Description'] = self.description

        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier

        if self.managed_rule_name is not None:
            result['ManagedRuleName'] = self.managed_rule_name

        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k1 in m.get('ConfigRuleParameters'):
                temp_model = main_models.ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k1))

        if m.get('ControlDescription') is not None:
            self.control_description = m.get('ControlDescription')

        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')

        if m.get('DefaultEnable') is not None:
            self.default_enable = m.get('DefaultEnable')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')

        if m.get('ManagedRuleName') is not None:
            self.managed_rule_name = m.get('ManagedRuleName')

        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class ListCompliancePackTemplatesResponseBodyCompliancePackTemplatesResultCompliancePackTemplatesConfigRulesConfigRuleParameters(DaraModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
        required: bool = None,
    ):
        # The name of the input parameter of the managed rule.
        self.parameter_name = parameter_name
        # The value of the input parameter of the managed rule.
        self.parameter_value = parameter_value
        # Indicates whether the parameter is required in the managed rule. Valid values:
        # 
        # *   true: required
        # *   false: optional
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        if self.required is not None:
            result['Required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        return self

