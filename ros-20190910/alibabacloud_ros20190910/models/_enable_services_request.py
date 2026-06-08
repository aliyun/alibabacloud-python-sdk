# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class EnableServicesRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        service_names: List[str] = None,
    ):
        # This parameter is required.
        self.region_id = region_id
        self.service_names = service_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_names is not None:
            result['ServiceNames'] = self.service_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceNames') is not None:
            self.service_names = m.get('ServiceNames')

        return self

