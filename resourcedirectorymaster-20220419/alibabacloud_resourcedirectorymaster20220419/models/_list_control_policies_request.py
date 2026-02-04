# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class ListControlPoliciesRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        page_number: int = None,
        page_size: int = None,
        policy_type: str = None,
        tag: List[main_models.ListControlPoliciesRequestTag] = None,
    ):
        # The language in which you want to return the descriptions of the access control policies. Valid values:
        # 
        # *   zh-CN (default value): Chinese
        # *   en: English
        # *   ja: Japanese
        # 
        # > This parameter is available only for system access control policies.
        self.language = language
        # The page number.
        # 
        # Page starts from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The type of the access control policies. Valid values:
        # 
        # *   System: system access control policy
        # *   Custom: custom access control policy
        self.policy_type = policy_type
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

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

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

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

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListControlPoliciesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListControlPoliciesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

