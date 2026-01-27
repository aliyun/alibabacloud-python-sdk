# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateRegistrationPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        company_limit_count_shrink: str = None,
        company_limit_type: str = None,
        description: str = None,
        match_mode: str = None,
        name: str = None,
        personal_limit_count_shrink: str = None,
        personal_limit_type: str = None,
        policy_id: str = None,
        priority: int = None,
        status: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        self.company_limit_count_shrink = company_limit_count_shrink
        self.company_limit_type = company_limit_type
        self.description = description
        self.match_mode = match_mode
        self.name = name
        self.personal_limit_count_shrink = personal_limit_count_shrink
        self.personal_limit_type = personal_limit_type
        # This parameter is required.
        self.policy_id = policy_id
        self.priority = priority
        self.status = status
        self.user_group_ids = user_group_ids
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_limit_count_shrink is not None:
            result['CompanyLimitCount'] = self.company_limit_count_shrink

        if self.company_limit_type is not None:
            result['CompanyLimitType'] = self.company_limit_type

        if self.description is not None:
            result['Description'] = self.description

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.name is not None:
            result['Name'] = self.name

        if self.personal_limit_count_shrink is not None:
            result['PersonalLimitCount'] = self.personal_limit_count_shrink

        if self.personal_limit_type is not None:
            result['PersonalLimitType'] = self.personal_limit_type

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.status is not None:
            result['Status'] = self.status

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyLimitCount') is not None:
            self.company_limit_count_shrink = m.get('CompanyLimitCount')

        if m.get('CompanyLimitType') is not None:
            self.company_limit_type = m.get('CompanyLimitType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PersonalLimitCount') is not None:
            self.personal_limit_count_shrink = m.get('PersonalLimitCount')

        if m.get('PersonalLimitType') is not None:
            self.personal_limit_type = m.get('PersonalLimitType')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

