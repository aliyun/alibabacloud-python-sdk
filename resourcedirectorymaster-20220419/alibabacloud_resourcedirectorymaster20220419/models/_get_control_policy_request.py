# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetControlPolicyRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        policy_id: str = None,
    ):
        # The language in which you want to return the description of the access control policy. Valid values:
        # 
        # *   zh-CN (default value): Chinese
        # *   en: English
        # *   ja: Japanese
        # 
        # > This parameter is valid only for system access control policies.
        self.language = language
        # The ID of the access control policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        return self

