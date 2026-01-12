# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyServiceInfoRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        service_code: str = None,
        service_desc: str = None,
        service_name: str = None,
    ):
        # Region ID.
        self.region_id = region_id
        # Resource type.
        self.resource_type = resource_type
        # Service code.
        self.service_code = service_code
        # Service description.
        self.service_desc = service_desc
        # Service name.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        if self.service_desc is not None:
            result['ServiceDesc'] = self.service_desc

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        if m.get('ServiceDesc') is not None:
            self.service_desc = m.get('ServiceDesc')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

