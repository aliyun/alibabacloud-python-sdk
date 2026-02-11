# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDashboardsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        product: str = None,
        recreate_switch: bool = None,
        region_id: str = None,
        title: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.product = product
        self.recreate_switch = recreate_switch
        self.region_id = region_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.product is not None:
            result['Product'] = self.product

        if self.recreate_switch is not None:
            result['RecreateSwitch'] = self.recreate_switch

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RecreateSwitch') is not None:
            self.recreate_switch = m.get('RecreateSwitch')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

