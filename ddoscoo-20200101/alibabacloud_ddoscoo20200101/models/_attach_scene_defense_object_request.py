# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachSceneDefenseObjectRequest(DaraModel):
    def __init__(
        self,
        object_type: str = None,
        objects: str = None,
        policy_id: str = None,
    ):
        # The type of the object. Set the value to **Domain**, which indicates a domain name.
        # 
        # This parameter is required.
        self.object_type = object_type
        # The object that you want to add to the policy. Separate multiple objects with commas (,).
        # 
        # This parameter is required.
        self.objects = objects
        # The ID of the policy.
        # 
        # > You can call the [DescribeSceneDefensePolicies](https://help.aliyun.com/document_detail/159382.html) operation to query the IDs of all policies.
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
        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.objects is not None:
            result['Objects'] = self.objects

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('Objects') is not None:
            self.objects = m.get('Objects')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        return self

