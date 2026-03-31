# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolicyVersionRequest(DaraModel):
    def __init__(
        self,
        policy_document: str = None,
        policy_name: str = None,
        rotate_strategy: str = None,
        set_as_default: bool = None,
    ):
        # The document of the policy. The document can be up to 6,144 bytes in length.
        self.policy_document = policy_document
        # The name of the policy.
        self.policy_name = policy_name
        # The rotation strategy of the policy. The rotation strategy can be used to delete an early policy version.
        # 
        # Valid values:
        # 
        # *   `None`: disables the rotation strategy.
        # *   `DeleteOldestNonDefaultVersionWhenLimitExceeded`: deletes the earliest non-active version if the number of versions exceeds the limit.
        # 
        # Default value: `None`.
        self.rotate_strategy = rotate_strategy
        # Specifies whether to set this policy as the default policy. Default value: `false`.
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

        if self.rotate_strategy is not None:
            result['RotateStrategy'] = self.rotate_strategy

        if self.set_as_default is not None:
            result['SetAsDefault'] = self.set_as_default

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('RotateStrategy') is not None:
            self.rotate_strategy = m.get('RotateStrategy')

        if m.get('SetAsDefault') is not None:
            self.set_as_default = m.get('SetAsDefault')

        return self

