# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DissociateIpAddressRequest(DaraModel):
    def __init__(
        self,
        eip_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.eip_id = eip_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_id is not None:
            result['EipId'] = self.eip_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipId') is not None:
            self.eip_id = m.get('EipId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

