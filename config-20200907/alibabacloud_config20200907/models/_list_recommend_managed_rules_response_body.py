# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListRecommendManagedRulesResponseBody(DaraModel):
    def __init__(
        self,
        recommended_managed_rules: main_models.ListRecommendManagedRulesResponseBodyRecommendedManagedRules = None,
        request_id: str = None,
    ):
        self.recommended_managed_rules = recommended_managed_rules
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.recommended_managed_rules:
            self.recommended_managed_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.recommended_managed_rules is not None:
            result['RecommendedManagedRules'] = self.recommended_managed_rules.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecommendedManagedRules') is not None:
            temp_model = main_models.ListRecommendManagedRulesResponseBodyRecommendedManagedRules()
            self.recommended_managed_rules = temp_model.from_map(m.get('RecommendedManagedRules'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListRecommendManagedRulesResponseBodyRecommendedManagedRules(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        recommended_managed_rule_list: List[main_models.ListRecommendManagedRulesResponseBodyRecommendedManagedRulesRecommendedManagedRuleList] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.recommended_managed_rule_list = recommended_managed_rule_list
        self.total_count = total_count

    def validate(self):
        if self.recommended_managed_rule_list:
            for v1 in self.recommended_managed_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['RecommendedManagedRuleList'] = []
        if self.recommended_managed_rule_list is not None:
            for k1 in self.recommended_managed_rule_list:
                result['RecommendedManagedRuleList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.recommended_managed_rule_list = []
        if m.get('RecommendedManagedRuleList') is not None:
            for k1 in m.get('RecommendedManagedRuleList'):
                temp_model = main_models.ListRecommendManagedRulesResponseBodyRecommendedManagedRulesRecommendedManagedRuleList()
                self.recommended_managed_rule_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRecommendManagedRulesResponseBodyRecommendedManagedRulesRecommendedManagedRuleList(DaraModel):
    def __init__(
        self,
        config_rule_name: str = None,
        description: str = None,
        identifier: str = None,
        resource_type_scope: str = None,
    ):
        self.config_rule_name = config_rule_name
        self.description = description
        self.identifier = identifier
        self.resource_type_scope = resource_type_scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name

        if self.description is not None:
            result['Description'] = self.description

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.resource_type_scope is not None:
            result['ResourceTypeScope'] = self.resource_type_scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('ResourceTypeScope') is not None:
            self.resource_type_scope = m.get('ResourceTypeScope')

        return self

