# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListRegistrationPoliciesRequest(DaraModel):
    def __init__(
        self,
        company_limit_type: str = None,
        current_page: int = None,
        match_mode: str = None,
        name: str = None,
        page_size: int = None,
        personal_limit_type: str = None,
        policy_ids: List[str] = None,
        status: str = None,
        user_group_id: str = None,
    ):
        self.company_limit_type = company_limit_type
        # This parameter is required.
        self.current_page = current_page
        self.match_mode = match_mode
        self.name = name
        # This parameter is required.
        self.page_size = page_size
        self.personal_limit_type = personal_limit_type
        self.policy_ids = policy_ids
        self.status = status
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_limit_type is not None:
            result['CompanyLimitType'] = self.company_limit_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.personal_limit_type is not None:
            result['PersonalLimitType'] = self.personal_limit_type

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.status is not None:
            result['Status'] = self.status

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyLimitType') is not None:
            self.company_limit_type = m.get('CompanyLimitType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PersonalLimitType') is not None:
            self.personal_limit_type = m.get('PersonalLimitType')

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

