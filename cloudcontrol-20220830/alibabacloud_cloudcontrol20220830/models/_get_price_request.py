# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetPriceRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_attributes: Dict[str, Any] = None,
    ):
        # The region ID. This parameter is required if the cloud product is deployed in a region.
        self.region_id = region_id
        # The attributes based on which the price is queried (in JSON format).
        self.resource_attributes = resource_attributes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_attributes is not None:
            result['resourceAttributes'] = self.resource_attributes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceAttributes') is not None:
            self.resource_attributes = m.get('resourceAttributes')

        return self

