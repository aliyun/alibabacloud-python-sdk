# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetServiceConfRequest(DaraModel):
    def __init__(
        self,
        by_default: bool = None,
        region_id: str = None,
        resource_type: str = None,
        scene: str = None,
        service_code: str = None,
    ):
        # Query default configuration
        self.by_default = by_default
        # Region ID.
        self.region_id = region_id
        # Resource type.
        self.resource_type = resource_type
        # Audit scenario.
        self.scene = scene
        # Service code.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.by_default is not None:
            result['ByDefault'] = self.by_default

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ByDefault') is not None:
            self.by_default = m.get('ByDefault')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        return self

