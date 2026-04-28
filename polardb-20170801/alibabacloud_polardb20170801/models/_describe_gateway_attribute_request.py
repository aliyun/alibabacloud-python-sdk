# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGatewayAttributeRequest(DaraModel):
    def __init__(
        self,
        gw_cluster_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

