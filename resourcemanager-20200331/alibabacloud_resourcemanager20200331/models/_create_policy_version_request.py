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
        # The content of the access policy.
        # 
        # The content must be 1 to 6,144 characters in length.
        # 
        # This parameter is required.
        self.policy_document = policy_document
        # Policy Name of the access policy.
        # 
        # Policy Name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # Specifies whether to set the version as the default access policy version.
        # 
        # Valid values:
        # 
        # - false (default): The version is not set as the default access policy version.
        # - true: The version is set as the default access policy version.
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

