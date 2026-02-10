# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateJenkinsImageRegistryNameRequest(DaraModel):
    def __init__(
        self,
        registry_id: int = None,
        registry_name: str = None,
        source_ip: str = None,
    ):
        # The ID of the image repository.
        # 
        # > You can call the [PageImageRegistry](~~PageImageRegistry~~) operation to query the IDs of image repositories.
        self.registry_id = registry_id
        # The name of the image repository.
        self.registry_name = registry_name
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.registry_id is not None:
            result['RegistryId'] = self.registry_id

        if self.registry_name is not None:
            result['RegistryName'] = self.registry_name

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegistryId') is not None:
            self.registry_id = m.get('RegistryId')

        if m.get('RegistryName') is not None:
            self.registry_name = m.get('RegistryName')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

