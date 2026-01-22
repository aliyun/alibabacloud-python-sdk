# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCustomEndpointRequest(DaraModel):
    def __init__(
        self,
        custom_endpoint_id: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
    ):
        self.custom_endpoint_id = custom_endpoint_id
        self.dbinstance_name = dbinstance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_endpoint_id is not None:
            result['CustomEndpointId'] = self.custom_endpoint_id

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomEndpointId') is not None:
            self.custom_endpoint_id = m.get('CustomEndpointId')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

