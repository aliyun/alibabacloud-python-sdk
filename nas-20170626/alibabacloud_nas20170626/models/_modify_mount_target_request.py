# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyMountTargetRequest(DaraModel):
    def __init__(
        self,
        access_group_name: str = None,
        dual_stack_mount_target_domain: str = None,
        file_system_id: str = None,
        mount_target_domain: str = None,
        status: str = None,
    ):
        # The name of the permission group that is attached to the mount target.
        self.access_group_name = access_group_name
        # The dual-stack (IPv4 and IPv6) domain name of the mount target.
        # 
        # >  Only Extreme NAS file systems that reside in the Chinese mainland support IPv6.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain
        # The ID of the file system.
        # 
        # *   Sample ID of a General-purpose NAS file system: `31a8e4****`.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`, for example, `extreme-0015****`.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The IPv4 domain name of the mount target.
        self.mount_target_domain = mount_target_domain
        # The status of the mount target.
        # 
        # Valid values:
        # 
        # *   Active: The mount target is available.
        # *   Inactive: The mount target is unavailable.
        # 
        # >  Only General-purpose File Storage NAS (NAS) file systems support changing the mount target status.
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

        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

