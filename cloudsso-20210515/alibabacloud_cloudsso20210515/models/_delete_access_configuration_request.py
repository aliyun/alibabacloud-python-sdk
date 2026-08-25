# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAccessConfigurationRequest(DaraModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        force_remove_permission_policies: bool = None,
    ):
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # Specifies whether to forcibly remove system policies and inline policies. Valid values:
        # 
        # - true: When you delete the access configuration, the associated system policies and inline policies are forcibly removed.
        # 
        # - false: When you delete the access configuration, the associated system policies and inline policies are not forcibly removed. This is the default value. If these policies exist in the access configuration, the deletion fails. Before you delete the access configuration, you must remove the system policies and inline policies. For more information, see [RemovePermissionPolicyFromAccessConfiguration](https://help.aliyun.com/document_detail/336904.html).
        self.force_remove_permission_policies = force_remove_permission_policies

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

        if self.force_remove_permission_policies is not None:
            result['ForceRemovePermissionPolicies'] = self.force_remove_permission_policies

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('ForceRemovePermissionPolicies') is not None:
            self.force_remove_permission_policies = m.get('ForceRemovePermissionPolicies')

        return self

