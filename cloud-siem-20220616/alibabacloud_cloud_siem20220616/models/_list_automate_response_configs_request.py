# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAutomateResponseConfigsRequest(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        auto_response_type: str = None,
        current_page: int = None,
        id: int = None,
        page_size: int = None,
        playbook_uuid: str = None,
        region_id: str = None,
        response_rule_type: str = None,
        role_for: int = None,
        role_type: int = None,
        rule_name: str = None,
        status: int = None,
        sub_user_id: int = None,
    ):
        # The type of the handling action. Valid values:
        # 
        # *   doPlaybook: runs a playbook.
        # *   changeEventStatus: changes the status of an event.
        # *   changeThreatLevel: changes the risk level of an event.
        self.action_type = action_type
        # The type of the automated response rule. Valid values:
        # 
        # *   event
        # *   alert
        self.auto_response_type = auto_response_type
        # The page number. Pages start from page 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The ID of the automated response rule.
        self.id = id
        # The number of entries per page. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The UUID of the playbook.
        self.playbook_uuid = playbook_uuid
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id
        self.response_rule_type = response_rule_type
        # The ID of the account that you switch from the management account.
        self.role_for = role_for
        # The type of the view. Valid values:
        # - 0: the current Alibaba Cloud account
        # - 1: the global account
        self.role_type = role_type
        # The name of the automated response rule.
        self.rule_name = rule_name
        # The status of the rule. Valid values:
        # 
        # *   0: disabled
        # *   100: enabled
        self.status = status
        # The ID of the user who created the rule.
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.auto_response_type is not None:
            result['AutoResponseType'] = self.auto_response_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.id is not None:
            result['Id'] = self.id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.response_rule_type is not None:
            result['ResponseRuleType'] = self.response_rule_type

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('AutoResponseType') is not None:
            self.auto_response_type = m.get('AutoResponseType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResponseRuleType') is not None:
            self.response_rule_type = m.get('ResponseRuleType')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        return self

