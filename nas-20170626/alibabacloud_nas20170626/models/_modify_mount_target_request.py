# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyMountTargetRequest(DaraModel):
    def __init__(
        self,
        access_group_name: str = None,
        access_point_access_only: bool = None,
        dual_stack_mount_target_domain: str = None,
        file_system_id: str = None,
        mount_target_domain: str = None,
        status: str = None,
    ):
        # The name of the access group that is associated with the mount target.
        self.access_group_name = access_group_name
        self.access_point_access_only = access_point_access_only
        # The domain name of the dual-stack mount target.
        # 
        # > The IPv6 feature is available only for Extreme NAS file systems in the Chinese mainland.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain
        # The ID of the file system.
        # 
        # - For a General-purpose NAS file system, the ID is similar to `31a8e4****`.
        # 
        # - For an Extreme NAS file system, the ID must start with `extreme-`, for example, `extreme-0015****`.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The domain name of the IPv4 mount target.
        self.mount_target_domain = mount_target_domain
        # The status of the mount target.
        # 
        # Valid values:
        # 
        # - Active: The mount target is available.
        # 
        # - Inactive: The mount target is unavailable.
        # 
        # > You can change the status of a mount target only if the mount target is attached to a General-purpose NAS file system.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name

        if self.access_point_access_only is not None:
            result['AccessPointAccessOnly'] = self.access_point_access_only

        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')

        if m.get('AccessPointAccessOnly') is not None:
            self.access_point_access_only = m.get('AccessPointAccessOnly')

        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

