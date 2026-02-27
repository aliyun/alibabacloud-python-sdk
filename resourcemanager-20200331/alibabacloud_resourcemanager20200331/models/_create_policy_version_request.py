# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolicyVersionRequest(DaraModel):
    def __init__(
        self,
        policy_document: str = None,
        policy_name: str = None,
        set_as_default: bool = None,
    ):
        # The document of the permission policy.
        # 
        # The document must be 1 to 6,144 characters in length.
        # 
        # This parameter is required.
        self.policy_document = policy_document
        # The name of the permission policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphen (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # Specifies whether to set the policy version as the default version.
        # 
        # *   false (default)
        # *   true
        self.set_as_default = set_as_default

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.set_as_default is not None:
            result['SetAsDefault'] = self.set_as_default

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('SetAsDefault') is not None:
            self.set_as_default = m.get('SetAsDefault')

        return self

