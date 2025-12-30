# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SharedStorageTemplate(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        mount_directory: str = None,
        mount_options: str = None,
        mount_target_domain: str = None,
        nasdirectory: str = None,
        protocol_type: str = None,
    ):
        self.file_system_id = file_system_id
        self.mount_directory = mount_directory
        self.mount_options = mount_options
        self.mount_target_domain = mount_target_domain
        self.nasdirectory = nasdirectory
        self.protocol_type = protocol_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.mount_directory is not None:
            result['MountDirectory'] = self.mount_directory

        if self.mount_options is not None:
            result['MountOptions'] = self.mount_options

        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain

        if self.nasdirectory is not None:
            result['NASDirectory'] = self.nasdirectory

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MountDirectory') is not None:
            self.mount_directory = m.get('MountDirectory')

        if m.get('MountOptions') is not None:
            self.mount_options = m.get('MountOptions')

        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')

        if m.get('NASDirectory') is not None:
            self.nasdirectory = m.get('NASDirectory')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        return self

