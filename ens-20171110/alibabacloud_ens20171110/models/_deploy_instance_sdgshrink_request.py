# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeployInstanceSDGShrinkRequest(DaraModel):
    def __init__(
        self,
        deployment_type: str = None,
        disk_access_protocol: str = None,
        disk_type: str = None,
        instance_ids_shrink: str = None,
        sdgid: str = None,
    ):
        # The deployment type of the SDG. shared: shared read/write splitting deployment. The content of the SDG is read-only, and data updates are written to the local storage of the instance.
        self.deployment_type = deployment_type
        self.disk_access_protocol = disk_access_protocol
        self.disk_type = disk_type
        # The IDs of the instances. The value is a JSON array that consists of up to 100 IDs.
        # 
        # This parameter is required.
        self.instance_ids_shrink = instance_ids_shrink
        # The ID of the SDG.
        # 
        # This parameter is required.
        self.sdgid = sdgid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_type is not None:
            result['DeploymentType'] = self.deployment_type

        if self.disk_access_protocol is not None:
            result['DiskAccessProtocol'] = self.disk_access_protocol

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink

        if self.sdgid is not None:
            result['SDGId'] = self.sdgid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentType') is not None:
            self.deployment_type = m.get('DeploymentType')

        if m.get('DiskAccessProtocol') is not None:
            self.disk_access_protocol = m.get('DiskAccessProtocol')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')

        if m.get('SDGId') is not None:
            self.sdgid = m.get('SDGId')

        return self

