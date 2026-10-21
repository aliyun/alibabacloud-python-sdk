# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateResponseRuleRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        response_action_config: str = None,
        response_action_type: str = None,
        response_execution_condition: str = None,
        response_rule_id: str = None,
        response_rule_name: str = None,
        response_rule_priority: int = None,
        response_rule_remark: str = None,
        response_rule_status: int = None,
        response_trigger_type: str = None,
    ):
        # The language of the response messages. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The maximum number of data records to read in this request.
        self.max_results = max_results
        # The token that marks the start position of the current read. Leave this parameter empty to start from the beginning.
        self.next_token = next_token
        # The region where the data management center of Cloud Threat Detection and Response (CTDR) is located. Select the management center region based on the region where your assets reside. Valid values:
        # - cn-hangzhou: Your assets reside in the Chinese mainland.
        # - ap-southeast-1: Your assets reside outside China.
        self.region_id = region_id
        # The action configuration of the automated response rule.
        self.response_action_config = response_action_config
        # The action type of the automated response rule. Valid values:
        # - doPlaybook: runs a playbook.
        # - changeEventStatus: updates the event status.
        # - changeThreatLevel: updates the threat level of an event.
        # - addEventTag: adds a label to an event.
        # - deleteEventTag: deletes a label from an event.
        # - alertWhitelist: adds an alert to the whitelist.
        self.response_action_type = response_action_type
        # The trigger condition configuration of the rule.
        self.response_execution_condition = response_execution_condition
        # The ID of the automated response rule.
        self.response_rule_id = response_rule_id
        # The name of the automated response rule.
        self.response_rule_name = response_rule_name
        # The execution priority of the automated response rule.
        self.response_rule_priority = response_rule_priority
        # The remarks for the response rule.
        self.response_rule_remark = response_rule_remark
        # The status of the automated response rule. Valid values:
        # - 0: disabled.
        # - 100: enabled.
        self.response_rule_status = response_rule_status
        # The trigger type of the automated response rule. Valid values:
        # - event: an event occurs.
        # - event_update: an event is updated.
        # - alert: an alert occurs.
        self.response_trigger_type = response_trigger_type

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

        if self.response_rule_id is not None:
            result['ResponseRuleId'] = self.response_rule_id

        if self.response_rule_name is not None:
            result['ResponseRuleName'] = self.response_rule_name

        if self.response_rule_priority is not None:
            result['ResponseRulePriority'] = self.response_rule_priority

        if self.response_rule_remark is not None:
            result['ResponseRuleRemark'] = self.response_rule_remark

        if self.response_rule_status is not None:
            result['ResponseRuleStatus'] = self.response_rule_status

        if self.response_trigger_type is not None:
            result['ResponseTriggerType'] = self.response_trigger_type

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

        if m.get('ResponseRuleId') is not None:
            self.response_rule_id = m.get('ResponseRuleId')

        if m.get('ResponseRuleName') is not None:
            self.response_rule_name = m.get('ResponseRuleName')

        if m.get('ResponseRulePriority') is not None:
            self.response_rule_priority = m.get('ResponseRulePriority')

        if m.get('ResponseRuleRemark') is not None:
            self.response_rule_remark = m.get('ResponseRuleRemark')

        if m.get('ResponseRuleStatus') is not None:
            self.response_rule_status = m.get('ResponseRuleStatus')

        if m.get('ResponseTriggerType') is not None:
            self.response_trigger_type = m.get('ResponseTriggerType')

        return self

