# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateResponseRuleRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        response_action_config: str = None,
        response_action_type: str = None,
        response_execution_condition: str = None,
        response_rule_name: str = None,
        response_rule_priority: str = None,
        response_trigger_type: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The maximum number of results to return.
        self.max_results = max_results
        # The token that specifies the position from which to start the query. If you do not specify this parameter, the query starts from the beginning.
        self.next_token = next_token
        # The deployment region of the data management center for threat analysis. You must select a region based on the location of your assets. Valid values:
        # 
        # - cn-hangzhou: Your assets are in the Chinese mainland or Hong Kong (China).
        # 
        # - ap-southeast-1: Your assets are in regions outside the Chinese mainland.
        self.region_id = region_id
        # The action configuration, specified as a JSON string.
        self.response_action_config = response_action_config
        # The action type for the automatic response rule. Valid values:
        # 
        # - doPlaybook: Runs a playbook.
        # 
        # - changeEventStatus: Changes the status of an event.
        # 
        # - changeThreatLevel: Changes the threat level of an event.
        # 
        # - addEventTag: Adds a tag to an event.
        # 
        # - deleteEventTag: Deletes a tag from an event.
        # 
        # - alertWhitelist: Adds an alert to the allowlist.
        self.response_action_type = response_action_type
        # The trigger conditions for the rule, specified as a JSON string.
        self.response_execution_condition = response_execution_condition
        # The name of the automatic response rule.
        self.response_rule_name = response_rule_name
        # The execution priority of the automatic response rule.
        self.response_rule_priority = response_rule_priority
        # The trigger type for the automatic response rule. Valid values:
        # 
        # - event: An event is generated.
        # 
        # - event_update: An event is updated.
        # 
        # - alert: An alert is generated.
        self.response_trigger_type = response_trigger_type
        # The ID of the member account. An administrator uses this parameter to operate on behalf of the specified member.
        self.role_for = role_for
        # The operational scope. Valid values:
        # 
        # - 0: Sets the scope to the current Alibaba Cloud account.
        # 
        # - 1: Sets the scope to all accounts in the enterprise.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.response_action_config is not None:
            result['ResponseActionConfig'] = self.response_action_config

        if self.response_action_type is not None:
            result['ResponseActionType'] = self.response_action_type

        if self.response_execution_condition is not None:
            result['ResponseExecutionCondition'] = self.response_execution_condition

        if self.response_rule_name is not None:
            result['ResponseRuleName'] = self.response_rule_name

        if self.response_rule_priority is not None:
            result['ResponseRulePriority'] = self.response_rule_priority

        if self.response_trigger_type is not None:
            result['ResponseTriggerType'] = self.response_trigger_type

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResponseActionConfig') is not None:
            self.response_action_config = m.get('ResponseActionConfig')

        if m.get('ResponseActionType') is not None:
            self.response_action_type = m.get('ResponseActionType')

        if m.get('ResponseExecutionCondition') is not None:
            self.response_execution_condition = m.get('ResponseExecutionCondition')

        if m.get('ResponseRuleName') is not None:
            self.response_rule_name = m.get('ResponseRuleName')

        if m.get('ResponseRulePriority') is not None:
            self.response_rule_priority = m.get('ResponseRulePriority')

        if m.get('ResponseTriggerType') is not None:
            self.response_trigger_type = m.get('ResponseTriggerType')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

