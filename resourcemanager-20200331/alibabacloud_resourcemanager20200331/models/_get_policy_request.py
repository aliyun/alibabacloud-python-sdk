# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPolicyRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        policy_name: str = None,
        policy_type: str = None,
    ):
        # The language in which you want to return the description of the system permission policy. Valid values:
        # 
        # *   en: English
        # *   zh-CN: Chinese
        # *   ja: Japanese
        self.language = language
        # The name of the permission policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # The type of the permission policy. Valid values:
        # 
        # *   Custom
        # *   System
        # 
        # This parameter is required.
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

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

