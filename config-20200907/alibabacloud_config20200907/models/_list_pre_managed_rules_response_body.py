# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListPreManagedRulesResponseBody(DaraModel):
    def __init__(
        self,
        managed_rules: List[main_models.ListPreManagedRulesResponseBodyManagedRules] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        # The evaluation rules.
        self.managed_rules = managed_rules
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.managed_rules:
            for v1 in self.managed_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ManagedRules'] = []
        if self.managed_rules is not None:
            for k1 in self.managed_rules:
                result['ManagedRules'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.managed_rules = []
        if m.get('ManagedRules') is not None:
            for k1 in m.get('ManagedRules'):
                temp_model = main_models.ListPreManagedRulesResponseBodyManagedRules()
                self.managed_rules.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPreManagedRulesResponseBodyManagedRules(DaraModel):
    def __init__(
        self,
        compulsory_input_parameter_details: Dict[str, Any] = None,
        config_rule_name: str = None,
        description: str = None,
        help_urls: str = None,
        identifier: str = None,
        optional_input_parameter_details: Dict[str, Any] = None,
        resource_type: str = None,
    ):
        # The details of the required input parameters of the rule.
        self.compulsory_input_parameter_details = compulsory_input_parameter_details
        # The name of the rule.
        self.config_rule_name = config_rule_name
        # The description of the rule.
        self.description = description
        # The URL of the topic that describes how the evaluation rule remediates the incompliant configurations.
        self.help_urls = help_urls
        # The identifier of the rule.
        self.identifier = identifier
        # The details of the optional input parameters of the rule.
        self.optional_input_parameter_details = optional_input_parameter_details
        # The type of resource.
        self.resource_type = resource_type

    def validate(self):
        pass

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

        if self.optional_input_parameter_details is not None:
            result['OptionalInputParameterDetails'] = self.optional_input_parameter_details

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

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

        if m.get('OptionalInputParameterDetails') is not None:
            self.optional_input_parameter_details = m.get('OptionalInputParameterDetails')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

