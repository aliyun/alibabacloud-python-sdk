# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResponseRulesRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        response_action_type: str = None,
        response_rule_name: str = None,
        response_rule_status: int = None,
        response_rule_type: str = None,
        response_trigger_type: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The language of the response message. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        # 
        # Note: This parameter is required in actual API calls. If it is not provided, the service returns a 400 error "The specified Lang can not be empty.". Explicitly pass the language code.
        self.lang = lang
        # The maximum number of data records to return for the current request.
        self.max_results = max_results
        # The position from which to start reading. If you leave this parameter empty, the reading starts from the beginning.
        self.next_token = next_token
        # The page number of the current page.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region where the data management center for threat analysis is located. You must select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: Assets are located outside the Chinese mainland.
        self.region_id = region_id
        # The action type of the automatic response rule. Valid values:
        # - doPlaybook: Execute a playbook.
        # - changeEventStatus: Update the event status.
        # - changeThreatLevel: Update the event threat level.
        # - addEventTag: Add an event tag.
        # - deleteEventTag: Delete an event tag.
        # - alertWhitelist: Add an alert to the whitelist.
        self.response_action_type = response_action_type
        # The name of the automatic response rule.
        self.response_rule_name = response_rule_name
        # The status of the automatic response rule. Valid values:
        # - 0: Disabled.
        # - 100: Enabled.
        self.response_rule_status = response_rule_status
        # The type of the response rule. Valid values:
        # - preset: Preset.
        # - custom: Custom.
        self.response_rule_type = response_rule_type
        # The trigger type of the automatic response rule. Valid values:
        # - event: Event occurrence.
        # - event_update: Event update.
        # - alert: Alert occurrence.
        self.response_trigger_type = response_trigger_type
        # The ID of the user whose perspective the administrator switches to.
        self.role_for = role_for
        # The view type. Valid values:
        # - 0: The view of the current Alibaba Cloud account.
        # - 1: The view of all accounts in the enterprise.
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.response_action_type is not None:
            result['ResponseActionType'] = self.response_action_type

        if self.response_rule_name is not None:
            result['ResponseRuleName'] = self.response_rule_name

        if self.response_rule_status is not None:
            result['ResponseRuleStatus'] = self.response_rule_status

        if self.response_rule_type is not None:
            result['ResponseRuleType'] = self.response_rule_type

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

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResponseActionType') is not None:
            self.response_action_type = m.get('ResponseActionType')

        if m.get('ResponseRuleName') is not None:
            self.response_rule_name = m.get('ResponseRuleName')

        if m.get('ResponseRuleStatus') is not None:
            self.response_rule_status = m.get('ResponseRuleStatus')

        if m.get('ResponseRuleType') is not None:
            self.response_rule_type = m.get('ResponseRuleType')

        if m.get('ResponseTriggerType') is not None:
            self.response_trigger_type = m.get('ResponseTriggerType')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

