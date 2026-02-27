# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolicyRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        policy_document: str = None,
        policy_name: str = None,
    ):
        # The description of the permission policy.
        # 
        # The description must be 1 to 1,024 characters in length.
        self.description = description
        # The document of the policy.
        # 
        # The document must be 1 to 6,144 characters in length.
        # 
        # This parameter is required.
        self.policy_document = policy_document
        # The name of the permission policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        return self

