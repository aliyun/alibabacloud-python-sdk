# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPermissionPoliciesInAccessConfigurationRequest(DaraModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        permission_policy_type: str = None,
    ):
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The type of the policy. The type can be used to filter policies. Valid values:
        # 
        # *   System: system policy.
        # *   Inline: inline policy.
        # 
        # If you do not specify this parameter, all types of policies are queried.
        self.permission_policy_type = permission_policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.permission_policy_type is not None:
            result['PermissionPolicyType'] = self.permission_policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('PermissionPolicyType') is not None:
            self.permission_policy_type = m.get('PermissionPolicyType')

        return self

