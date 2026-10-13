# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLifecyclePolicyRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        file_system_id: str = None,
        lifecycle_policy_id: str = None,
        lifecycle_policy_name: str = None,
        lifecycle_rule_name: str = None,
        path: str = None,
        storage_type: str = None,
    ):
        # The description.
        self.description = description
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the lifecycle policy.
        self.lifecycle_policy_id = lifecycle_policy_id
        # The lifecycle management Policy Name.
        # 
        # The name must be 3 to 64 characters in length. It must start with an uppercase letter or a lowercase letter, and can contain letters, digits, underscores (_), and hyphens (-).
        self.lifecycle_policy_name = lifecycle_policy_name
        # The management rule associated with the lifecycle management policy.
        # 
        # Valid values:
        # 
        # - DEFAULT_ATIME_14: Files that have not been accessed for 14 days.
        # - DEFAULT_ATIME_30: Files that have not been accessed for 30 days.
        # - DEFAULT_ATIME_60: Files that have not been accessed for 60 days.
        # - DEFAULT_ATIME_90: Files that have not been accessed for 90 days.
        # - DEFAULT_ATIME_180: Files that have not been accessed for 180 days. DEFAULT_ATIME_180 is supported only when StorageType is set to Archive.
        # > If an IA storage class policy is already configured for the directory, the time threshold for the Archive storage class policy must be longer than that of the IA storage class policy.
        self.lifecycle_rule_name = lifecycle_rule_name
        # The absolute path of a single directory configured for the lifecycle management policy.
        # 
        # The path must start with a forward slash (/) and must be a valid path in the mount target.
        self.path = path
        # The tiered storage class.
        # 
        # Valid values:
        # 
        # - InfrequentAccess: IA storage class.
        # - Archive: Archive storage class.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.lifecycle_policy_id is not None:
            result['LifecyclePolicyId'] = self.lifecycle_policy_id

        if self.lifecycle_policy_name is not None:
            result['LifecyclePolicyName'] = self.lifecycle_policy_name

        if self.lifecycle_rule_name is not None:
            result['LifecycleRuleName'] = self.lifecycle_rule_name

        if self.path is not None:
            result['Path'] = self.path

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('LifecyclePolicyId') is not None:
            self.lifecycle_policy_id = m.get('LifecyclePolicyId')

        if m.get('LifecyclePolicyName') is not None:
            self.lifecycle_policy_name = m.get('LifecyclePolicyName')

        if m.get('LifecycleRuleName') is not None:
            self.lifecycle_rule_name = m.get('LifecycleRuleName')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

