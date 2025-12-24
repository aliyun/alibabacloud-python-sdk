# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNASFileSystemResponseBody(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        file_system_name: str = None,
        mount_target_domain: str = None,
        office_site_id: str = None,
        request_id: str = None,
    ):
        # ID of the NAS file system.
        self.file_system_id = file_system_id
        # Name of the NAS file system.
        self.file_system_name = file_system_name
        # Mount point domain.
        self.mount_target_domain = mount_target_domain
        # Workspace ID.
        self.office_site_id = office_site_id
        # Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name

        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')

        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

