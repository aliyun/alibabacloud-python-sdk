# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCheckPoliciesRequest(DaraModel):
    def __init__(
        self,
        check_types: List[str] = None,
        current_page: int = None,
        dependent_policy_id: int = None,
        lang: str = None,
        page_size: int = None,
        policy_id: int = None,
        policy_show_name: str = None,
        policy_type: str = None,
        type: str = None,
    ):
        # The types of policies to be queried (default queries both custom and system predefined policies).
        self.check_types = check_types
        # Specifies the page number from which to start displaying the query results. The starting value is **1**. The default value is **1**, indicating that the display starts from the **1st** page.
        self.current_page = current_page
        # ID of the associated parent policy.
        # 
        # (The specific dependency relationship from low to high is: Section -> Requirement -> Standard)
        self.dependent_policy_id = dependent_policy_id
        # Language type for request and response messages, with a default value of **zh**. Possible values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Number of check item information entries displayed per page during pagination. The default value is **50**, indicating 50 entries per page.
        self.page_size = page_size
        # ID of the newly added classification setting.
        self.policy_id = policy_id
        # Name of the newly added classification setting.
        self.policy_show_name = policy_show_name
        # Policy type of the custom check item rule:
        # - **STANDARD**: New standard
        # - **REQUIREMENT**: New requirement
        # - **SECTION**: New section
        # 
        # This parameter is required.
        self.policy_type = policy_type
        # Name of the associated major policy category (required when PolicyType is STANDARD):
        # - **AISPM**: AI Configuration Management (AI-SPM)
        # - **IDENTITY_PERMISSION**: Identity and Permission Management (CIEM)
        # - **RISK**: Security Risk
        # - **COMPLIANCE**: Compliance Risk
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_types is not None:
            result['CheckTypes'] = self.check_types

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dependent_policy_id is not None:
            result['DependentPolicyId'] = self.dependent_policy_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_show_name is not None:
            result['PolicyShowName'] = self.policy_show_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckTypes') is not None:
            self.check_types = m.get('CheckTypes')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DependentPolicyId') is not None:
            self.dependent_policy_id = m.get('DependentPolicyId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyShowName') is not None:
            self.policy_show_name = m.get('PolicyShowName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

