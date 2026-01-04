# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNetworkAccessEndpointAvailableZonesRequest(DaraModel):
    def __init__(
        self,
        nae_region_id: str = None,
    ):
        # 专属网络端点支持的地域
        # 
        # This parameter is required.
        self.nae_region_id = nae_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nae_region_id is not None:
            result['NaeRegionId'] = self.nae_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NaeRegionId') is not None:
            self.nae_region_id = m.get('NaeRegionId')

        return self

