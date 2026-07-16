# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLifecyclePoliciesRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        file_system_id: str = None,
        lifecycle_policy_id: str = None,
        lifecycle_policy_name: str = None,
        lifecycle_policy_type: str = None,
        page_number: int = None,
        page_size: int = None,
        path: str = None,
        storage_type: str = None,
    ):
        # The description of the policy.
        # >Only CPFS for Lingjun supports this parameter.
        self.description = description
        # The file system ID.
        self.file_system_id = file_system_id
        # The ID of the lifecycle policy.
        self.lifecycle_policy_id = lifecycle_policy_id
        # The lifecycle policy name. Naming rules:
        # 
        # 
        # The name must be 3 to 64 characters in length, start with a letter, and can contain letters, digits, underscores (_), or hyphens (-).
        # 
        # >Optional for General-purpose NAS file systems. If specified, this parameter takes precedence. If not specified, LifecyclePolicyId is used instead.
        self.lifecycle_policy_name = lifecycle_policy_name
        # The policy type.
        # 
        # Valid values:
        # - Auto: automatic execution
        # - OnDemand: on-demand execution
        # >Only CPFS for Lingjun supports this parameter.
        self.lifecycle_policy_type = lifecycle_policy_type
        # The page number of the list.
        # 
        # Start value (default value): 1.
        self.page_number = page_number
        # The number of lifecycle management policies on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # Filters results by path.
        # >Only CPFS for Lingjun supports this parameter.
        self.path = path
        # The storage class type. Valid values:
        # - InfrequentAccess: IA storage class.
        # - Archive: Archive storage class.
        # > If StorageType is not specified, all lifecycle policies are returned.
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

        if self.lifecycle_policy_type is not None:
            result['LifecyclePolicyType'] = self.lifecycle_policy_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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

        if m.get('LifecyclePolicyType') is not None:
            self.lifecycle_policy_type = m.get('LifecyclePolicyType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

