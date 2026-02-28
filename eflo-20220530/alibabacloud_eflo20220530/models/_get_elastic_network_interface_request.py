# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetElasticNetworkInterfaceRequest(DaraModel):
    def __init__(
        self,
        elastic_network_interface_id: str = None,
        region_id: str = None,
    ):
        # Lingjun Elastic Network Interface ID
        # 
        # This parameter is required.
        self.elastic_network_interface_id = elastic_network_interface_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_network_interface_id is not None:
            result['ElasticNetworkInterfaceId'] = self.elastic_network_interface_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticNetworkInterfaceId') is not None:
            self.elastic_network_interface_id = m.get('ElasticNetworkInterfaceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

