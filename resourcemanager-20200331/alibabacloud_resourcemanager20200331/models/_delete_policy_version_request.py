# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePolicyVersionRequest(DaraModel):
    def __init__(
        self,
        policy_name: str = None,
        version_id: str = None,
    ):
        # The name of the permission policy.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, and hyphen (-).
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # The ID of the policy version.
        # 
        # You can call the [ListPolicyVersions](https://help.aliyun.com/document_detail/159982.html) operation to query the ID.
        # 
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

