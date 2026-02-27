# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListControlPoliciesRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        policy_type: str = None,
    ):
        # The language in which you want to return the descriptions of the access control policies. Valid values:
        # 
        # - zh-CN (default value): Chinese
        # - en: English
        # - ja: Japanese
        # 
        # >  This parameter is valid only for system access control policies.
        self.language = language
        # The number of the page to return. 
        # 
        # Page start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. 
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The type of the access control policy. Valid values:
        # 
        # - System: system access control policy
        # - Custom: custom access control policy
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

