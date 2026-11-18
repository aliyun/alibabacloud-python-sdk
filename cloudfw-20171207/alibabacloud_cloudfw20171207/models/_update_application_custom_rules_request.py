# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class UpdateApplicationCustomRulesRequest(DaraModel):
    def __init__(
        self,
        rules: List[main_models.UpdateApplicationCustomRulesRequestRules] = None,
    ):
        # The list of custom application rules to be modified. You can specify up to 20 rules at a time. Rule IDs in the list must be unique.
        # 
        # This parameter is required.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.UpdateApplicationCustomRulesRequestRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class UpdateApplicationCustomRulesRequestRules(DaraModel):
    def __init__(
        self,
        add_application_ids: List[int] = None,
        application_custom_rule_id: str = None,
        application_custom_rule_name: str = None,
        priority: int = None,
        remove_application_ids: List[int] = None,
        rule_action: str = None,
    ):
        # The list of application IDs to be associated. You can specify up to 200 IDs. The IDs cannot be 0 and must exist in the built-in application signature library. The IDs must not overlap with those in RemoveApplicationIds. The combined list cannot be empty and can contain up to 200 IDs.
        self.add_application_ids = add_application_ids
        # The ID of the custom application rule to be modified. The rule must exist within the current Alibaba Cloud account.
        self.application_custom_rule_id = application_custom_rule_id
        # The name of the custom rule. The name can be up to 64 characters in length and can contain Chinese characters, letters, digits, hyphens (-), underscores (_), and periods (.). If this parameter is not specified or is left empty, the original value is retained.
        self.application_custom_rule_name = application_custom_rule_name
        # The priority of the rule. This parameter is required. Valid values: integers from 1 to 200. A smaller value indicates a higher priority. Priorities must be unique within the same template. You can swap priorities by deleting and then re-inserting rules.
        self.priority = priority
        # The list of application IDs to be disassociated. You can specify up to 200 IDs. The IDs must not overlap with those in AddApplicationIds. The combined list cannot be empty and can contain up to 200 IDs.
        self.remove_application_ids = remove_application_ids
        # The action to perform when the rule is matched. This parameter is required. Valid values:
        # - **Allow**: allows the traffic.
        # - **Alert**: monitors the traffic.
        # - **Deny**: blocks the traffic.
        self.rule_action = rule_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_application_ids is not None:
            result['AddApplicationIds'] = self.add_application_ids

        if self.application_custom_rule_id is not None:
            result['ApplicationCustomRuleId'] = self.application_custom_rule_id

        if self.application_custom_rule_name is not None:
            result['ApplicationCustomRuleName'] = self.application_custom_rule_name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.remove_application_ids is not None:
            result['RemoveApplicationIds'] = self.remove_application_ids

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddApplicationIds') is not None:
            self.add_application_ids = m.get('AddApplicationIds')

        if m.get('ApplicationCustomRuleId') is not None:
            self.application_custom_rule_id = m.get('ApplicationCustomRuleId')

        if m.get('ApplicationCustomRuleName') is not None:
            self.application_custom_rule_name = m.get('ApplicationCustomRuleName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RemoveApplicationIds') is not None:
            self.remove_application_ids = m.get('RemoveApplicationIds')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        return self

