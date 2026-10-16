# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateControlPolicyRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        effect_scope: str = None,
        policy_document: str = None,
        policy_name: str = None,
    ):
        # The description of the control policy.
        # 
        # The description must be 1 to 1024 characters in length, must start with a letter, and can contain letters, digits, underscores (_), and hyphens (-).
        self.description = description
        # The effective scope of the control policy.
        # 
        # Valid values: RAM, which indicates that the control policy takes effect only for Resource Access Management (RAM) users or RAM roles.
        # 
        # This parameter is required.
        self.effect_scope = effect_scope
        # The content of the control policy.
        # 
        # The maximum length is 4096 characters.
        # 
        # For information about the control policy language, see [Control policy language](https://help.aliyun.com/document_detail/179096.html).
        # 
        # For examples of control policies, see [Examples of custom control policies](https://help.aliyun.com/document_detail/181474.html).
        # 
        # This parameter is required.
        self.policy_document = policy_document
        # Policy Name of the control policy.
        # 
        # Policy Name must be 1 to 128 characters in length, must start with a letter, and can contain letters, digits, and hyphens (-).
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

        if self.effect_scope is not None:
            result['EffectScope'] = self.effect_scope

        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EffectScope') is not None:
            self.effect_scope = m.get('EffectScope')

        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        return self

