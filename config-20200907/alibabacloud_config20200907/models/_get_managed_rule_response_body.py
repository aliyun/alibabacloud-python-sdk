# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetManagedRuleResponseBody(DaraModel):
    def __init__(
        self,
        managed_rule: main_models.GetManagedRuleResponseBodyManagedRule = None,
        request_id: str = None,
    ):
        # The details of the managed rule.
        self.managed_rule = managed_rule
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.managed_rule:
            self.managed_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.managed_rule is not None:
            result['ManagedRule'] = self.managed_rule.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedRule') is not None:
            temp_model = main_models.GetManagedRuleResponseBodyManagedRule()
            self.managed_rule = temp_model.from_map(m.get('ManagedRule'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetManagedRuleResponseBodyManagedRule(DaraModel):
    def __init__(
        self,
        compulsory_input_parameter_details: Dict[str, Any] = None,
        config_rule_name: str = None,
        description: str = None,
        help_urls: str = None,
        identifier: str = None,
        labels: List[str] = None,
        optional_input_parameter_details: Dict[str, Any] = None,
        risk_level: int = None,
        scope: main_models.GetManagedRuleResponseBodyManagedRuleScope = None,
        source_details: List[main_models.GetManagedRuleResponseBodyManagedRuleSourceDetails] = None,
    ):
        # The details of the required input parameters for the managed rule.
        self.compulsory_input_parameter_details = compulsory_input_parameter_details
        # The name of the managed rule.
        self.config_rule_name = config_rule_name
        # The description of the managed rule.
        self.description = description
        # The URL of the topic that provides guidance on remediation for the managed rule.
        self.help_urls = help_urls
        # The identifier of the managed rule.
        self.identifier = identifier
        # The tags of the managed rule.
        self.labels = labels
        # The details of the optional input parameters for the managed rule.
        self.optional_input_parameter_details = optional_input_parameter_details
        # The risk level of the managed rule. Valid values:
        # 
        # *   1: high
        # *   2: medium
        # *   3: low
        self.risk_level = risk_level
        # The effective scope of the managed rule.
        self.scope = scope
        # The information about the trigger type of the managed rule.
        self.source_details = source_details

    def validate(self):
        if self.scope:
            self.scope.validate()
        if self.source_details:
            for v1 in self.source_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compulsory_input_parameter_details is not None:
            result['CompulsoryInputParameterDetails'] = self.compulsory_input_parameter_details

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

        if self.optional_input_parameter_details is not None:
            result['OptionalInputParameterDetails'] = self.optional_input_parameter_details

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.scope is not None:
            result['Scope'] = self.scope.to_map()

        result['SourceDetails'] = []
        if self.source_details is not None:
            for k1 in self.source_details:
                result['SourceDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompulsoryInputParameterDetails') is not None:
            self.compulsory_input_parameter_details = m.get('CompulsoryInputParameterDetails')

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

        if m.get('OptionalInputParameterDetails') is not None:
            self.optional_input_parameter_details = m.get('OptionalInputParameterDetails')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Scope') is not None:
            temp_model = main_models.GetManagedRuleResponseBodyManagedRuleScope()
            self.scope = temp_model.from_map(m.get('Scope'))

        self.source_details = []
        if m.get('SourceDetails') is not None:
            for k1 in m.get('SourceDetails'):
                temp_model = main_models.GetManagedRuleResponseBodyManagedRuleSourceDetails()
                self.source_details.append(temp_model.from_map(k1))

        return self

class GetManagedRuleResponseBodyManagedRuleSourceDetails(DaraModel):
    def __init__(
        self,
        maximum_execution_frequency: str = None,
        message_type: str = None,
    ):
        # The interval at which the rule is triggered. Valid values: Valid values:
        # 
        # *   One_Hour
        # *   Three_Hours
        # *   Six_Hours
        # *   Twelve_Hours
        # *   TwentyFour_Hours
        self.maximum_execution_frequency = maximum_execution_frequency
        # The trigger type of the rule. Valid values:
        # 
        # *   ConfigurationItemChangeNotification: The rule is triggered by configuration changes.
        # *   ScheduledNotification: The rule is periodically triggered.
        self.message_type = message_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        return self

class GetManagedRuleResponseBodyManagedRuleScope(DaraModel):
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

