# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAccessPointRequest(DaraModel):
    def __init__(
        self,
        access_group: str = None,
        access_point_id: str = None,
        access_point_name: str = None,
        enabled_ram: bool = None,
        file_system_id: str = None,
    ):
        # The permission group name.
        # 
        # This parameter is required when the file system is a General-purpose NAS file system.
        # 
        # Default permission group: DEFAULT_VPC_GROUP_NAME (the default VPC permission group).
        # > Agentic file systems do not support this parameter.
        self.access_group = access_group
        # The access point ID.
        # 
        # This parameter is required.
        self.access_point_id = access_point_id
        # The access point name.
        self.access_point_name = access_point_name
        # Specifies whether to enable the RAM policy. Valid values:
        # 
        # - true: Enabled.
        # - false (default): Not enabled.
        # 
        # > After you enable the access point RAM policy, all Resource Access Management (RAM) users are denied access to mount and access data through the access point by default. You must grant the corresponding access permissions through authorization and mount and access data through the access point. After you disable the RAM policy, the access point allows anonymity mounting.
        # 
        # > Agentic file systems do not support this parameter.
        self.enabled_ram = enabled_ram
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group

        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.access_point_name is not None:
            result['AccessPointName'] = self.access_point_name

        if self.enabled_ram is not None:
            result['EnabledRam'] = self.enabled_ram

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')

        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('AccessPointName') is not None:
            self.access_point_name = m.get('AccessPointName')

        if m.get('EnabledRam') is not None:
            self.enabled_ram = m.get('EnabledRam')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        return self

