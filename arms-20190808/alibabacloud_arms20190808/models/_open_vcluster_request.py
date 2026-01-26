# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenVClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        length: int = None,
        product: str = None,
        recreate_switch: bool = None,
        region_id: str = None,
    ):
        # The type of the cluster. For cloud services, set this parameter to `cloud-product-prometheus`.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # The length of the cluster ID. Default value: 10.
        self.length = length
        # The name of the cloud service. This parameter must be specified when ClusterType is set to `cloud-product-prometheus`. Valid values: influxdb, mongodb, and DLA. You cannot specify multiple service names.
        self.product = product
        # Specifies whether to create or query a virtual cluster. This parameter provides backward compatibility.
        self.recreate_switch = recreate_switch
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
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.length is not None:
            result['Length'] = self.length

        if self.product is not None:
            result['Product'] = self.product

        if self.recreate_switch is not None:
            result['RecreateSwitch'] = self.recreate_switch

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RecreateSwitch') is not None:
            self.recreate_switch = m.get('RecreateSwitch')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

