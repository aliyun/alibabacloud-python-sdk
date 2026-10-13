# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLifecyclePolicyRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        lifecycle_policy_id: str = None,
        lifecycle_policy_name: str = None,
    ):
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the lifecycle policy.
        # This parameter is required for CPFS for Lingjun file systems.
        self.lifecycle_policy_id = lifecycle_policy_id
        # The Policy Name of the lifecycle management policy. The name must be 3 to 64 characters in epoch, must start with an uppercase letter or lowercase letter, and can contain letters, digits, underscores (_), or hyphens (-).
        # 
        # >This parameter is optional for General-purpose NAS file systems. If this parameter is specified, the value of this parameter is used. If this parameter is not specified, the value of LifecyclePolicyId is used.
        self.lifecycle_policy_name = lifecycle_policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.lifecycle_policy_id is not None:
            result['LifecyclePolicyId'] = self.lifecycle_policy_id

        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('LifecyclePolicyId') is not None:
            self.lifecycle_policy_id = m.get('LifecyclePolicyId')

        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')

        return self

