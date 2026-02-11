# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PostAutomateResponseConfigRequest(DaraModel):
    def __init__(
        self,
        action_config: str = None,
        action_type: str = None,
        auto_response_type: str = None,
        execution_condition: str = None,
        id: int = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        rule_name: str = None,
        sub_user_id: int = None,
    ):
        # The action configuration of the automated response rule. The value is in the JSON format.
        self.action_config = action_config
        # The type of the handling action. Multiple types are separated by commas (,). Valid values:
        # 
        # *   **doPlaybook**: runs the playbook.
        # *   **changeEventStatus**: changes the event status.
        # *   **changeThreatLevel**: changes the threat level of the event.
        self.action_type = action_type
        # The type of the automated response rule. Valid values:
        # 
        # *   **event**
        # *   **alert**
        self.auto_response_type = auto_response_type
        # The trigger condition of the automated response rule. The value is in the JSON format.
        self.execution_condition = execution_condition
        # The rule ID.
        self.id = id
        # The data management center of the threat analysis feature. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   **cn-hangzhou**: Your assets reside in regions in China.
        # *   **ap-southeast-1**: Your assets reside in regions outside China.
        self.region_id = region_id
        # The ID of the account that you switch from the management account.
        self.role_for = role_for
        # The type of the view. Valid values:
        # - 0: the current Alibaba Cloud account
        # - 1: the global account
        self.role_type = role_type
        # The rule name.
        self.rule_name = rule_name
        # The ID of the user who created the rule.
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_config is not None:
            result['ActionConfig'] = self.action_config

        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type

        if self.execution_condition is not None:
            result['ExecutionCondition'] = self.execution_condition

        if self.id is not None:
            result['Id'] = self.id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionConfig') is not None:
            self.action_config = m.get('ActionConfig')

        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')

        if m.get('ExecutionCondition') is not None:
            self.execution_condition = m.get('ExecutionCondition')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        return self

