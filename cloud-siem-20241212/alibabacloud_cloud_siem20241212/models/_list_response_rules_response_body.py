# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListResponseRulesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        response_rules: List[main_models.ListResponseRulesResponseBodyResponseRules] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        # This parameter is required.
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.response_rules = response_rules
        self.total_count = total_count

    def validate(self):
        if self.response_rules:
            for v1 in self.response_rules:
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResponseRules'] = []
        if self.response_rules is not None:
            for k1 in self.response_rules:
                result['ResponseRules'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.response_rules = []
        if m.get('ResponseRules') is not None:
            for k1 in m.get('ResponseRules'):
                temp_model = main_models.ListResponseRulesResponseBodyResponseRules()
                self.response_rules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListResponseRulesResponseBodyResponseRules(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        response_action_config: str = None,
        response_action_type: str = None,
        response_execution_condition: str = None,
        response_rule_id: str = None,
        response_rule_name: str = None,
        response_rule_priority: int = None,
        response_rule_status: int = None,
        response_rule_type: str = None,
        response_trigger_type: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.response_action_config = response_action_config
        self.response_action_type = response_action_type
        self.response_execution_condition = response_execution_condition
        self.response_rule_id = response_rule_id
        self.response_rule_name = response_rule_name
        self.response_rule_priority = response_rule_priority
        self.response_rule_status = response_rule_status
        self.response_rule_type = response_rule_type
        self.response_trigger_type = response_trigger_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.response_action_config is not None:
            result['ResponseActionConfig'] = self.response_action_config

        if self.response_action_type is not None:
            result['ResponseActionType'] = self.response_action_type

        if self.response_execution_condition is not None:
            result['ResponseExecutionCondition'] = self.response_execution_condition

        if self.response_rule_id is not None:
            result['ResponseRuleId'] = self.response_rule_id

        if self.response_rule_name is not None:
            result['ResponseRuleName'] = self.response_rule_name

        if self.response_rule_priority is not None:
            result['ResponseRulePriority'] = self.response_rule_priority

        if self.response_rule_status is not None:
            result['ResponseRuleStatus'] = self.response_rule_status

        if self.response_rule_type is not None:
            result['ResponseRuleType'] = self.response_rule_type

        if self.response_trigger_type is not None:
            result['ResponseTriggerType'] = self.response_trigger_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ResponseActionConfig') is not None:
            self.response_action_config = m.get('ResponseActionConfig')

        if m.get('ResponseActionType') is not None:
            self.response_action_type = m.get('ResponseActionType')

        if m.get('ResponseExecutionCondition') is not None:
            self.response_execution_condition = m.get('ResponseExecutionCondition')

        if m.get('ResponseRuleId') is not None:
            self.response_rule_id = m.get('ResponseRuleId')

        if m.get('ResponseRuleName') is not None:
            self.response_rule_name = m.get('ResponseRuleName')

        if m.get('ResponseRulePriority') is not None:
            self.response_rule_priority = m.get('ResponseRulePriority')

        if m.get('ResponseRuleStatus') is not None:
            self.response_rule_status = m.get('ResponseRuleStatus')

        if m.get('ResponseRuleType') is not None:
            self.response_rule_type = m.get('ResponseRuleType')

        if m.get('ResponseTriggerType') is not None:
            self.response_trigger_type = m.get('ResponseTriggerType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

