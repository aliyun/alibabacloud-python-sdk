# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyFeatureConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        description: str = None,
        field: str = None,
        region_id: str = None,
        resource_type: str = None,
        service_code: str = None,
        type: str = None,
    ):
        # query
        self.config = config
        # query
        self.description = description
        # query
        self.field = field
        # query
        self.region_id = region_id
        # query
        self.resource_type = resource_type
        # System-defined parameter. Value: **ModifyFeatureConfig**.
        self.service_code = service_code
        # query
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.description is not None:
            result['Description'] = self.description

        if self.field is not None:
            result['Field'] = self.field

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

