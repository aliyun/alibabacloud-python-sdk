# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMountTargetsRequest(DaraModel):
    def __init__(
        self,
        dual_stack_mount_target_domain: str = None,
        file_system_id: str = None,
        mount_target_domain: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The dual-stack (IPv4 and IPv6) domain name of the mount target.
        # 
        # > Currently, only Extreme NAS file systems in Chinese mainland regions support IPv6.
        self.dual_stack_mount_target_domain = dual_stack_mount_target_domain
        # The ID of the file system.
        # 
        # - general-purpose NAS: 31a8e4\\*\\*\\*\\*.
        # 
        # - Extreme NAS: The ID must start with `extreme-`. Example: extreme-0015\\*\\*\\*\\*.
        # 
        # - CPFS: The ID must start with `cpfs-`. Example: cpfs-125487\\*\\*\\*\\*.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The domain name of the mount target.
        self.mount_target_domain = mount_target_domain
        # The page number to return.
        # 
        # The value must be 1 or greater. Default value: 1.
        self.page_number = page_number
        # The number of mount targets to return per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dual_stack_mount_target_domain is not None:
            result['DualStackMountTargetDomain'] = self.dual_stack_mount_target_domain

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DualStackMountTargetDomain') is not None:
            self.dual_stack_mount_target_domain = m.get('DualStackMountTargetDomain')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

