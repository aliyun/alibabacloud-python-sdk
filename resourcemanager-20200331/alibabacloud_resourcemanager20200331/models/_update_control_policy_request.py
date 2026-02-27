# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateControlPolicyRequest(DaraModel):
    def __init__(
        self,
        new_description: str = None,
        new_policy_document: str = None,
        new_policy_name: str = None,
        policy_id: str = None,
    ):
        # The new description of the access control policy.
        # 
        # The description must be 1 to 1,024 characters in length. The description can contain letters, digits, underscores (_), and hyphens (-) and must start with a letter.
        self.new_description = new_description
        # The new document of the access control policy.
        # 
        # The document can be a maximum of 4,096 characters in length.
        # 
        # For more information about the languages of access control policies, see [Languages of access control policies](https://help.aliyun.com/document_detail/179096.html).
        # 
        # For more information about the examples of access control policies, see [Examples of custom access control policies](https://help.aliyun.com/document_detail/181474.html).
        self.new_policy_document = new_policy_document
        # The new name of the access control policy.
        # 
        # The name must be 1 to 128 characters in length. The name can contain letters, digits, and hyphens (-) and must start with a letter.
        self.new_policy_name = new_policy_name
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
        if self.new_description is not None:
            result['NewDescription'] = self.new_description

        if self.new_policy_document is not None:
            result['NewPolicyDocument'] = self.new_policy_document

        if self.new_policy_name is not None:
            result['NewPolicyName'] = self.new_policy_name

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')

        if m.get('NewPolicyDocument') is not None:
            self.new_policy_document = m.get('NewPolicyDocument')

        if m.get('NewPolicyName') is not None:
            self.new_policy_name = m.get('NewPolicyName')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        return self

