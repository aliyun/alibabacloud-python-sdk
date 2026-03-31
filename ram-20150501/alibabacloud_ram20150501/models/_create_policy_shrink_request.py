# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        policy_document: str = None,
        policy_name: str = None,
        tag_shrink: str = None,
    ):
        # The description of the policy.
        # 
        # The description must be 1 to 1,024 characters in length.
        self.description = description
        # The document of the policy.
        # 
        # The document must be 1 to 6,144 characters in length.
        # 
        # For more information about policy elements and sample policies, see [Policy elements](https://help.aliyun.com/document_detail/93738.html) and [Overview of sample policies](https://help.aliyun.com/document_detail/210969.html).
        self.policy_document = policy_document
        # The name of the policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        self.policy_name = policy_name
        # The tags.
        self.tag_shrink = tag_shrink

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

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

