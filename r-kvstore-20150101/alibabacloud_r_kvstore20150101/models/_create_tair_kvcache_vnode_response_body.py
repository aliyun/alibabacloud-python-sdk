# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTairKVCacheVNodeResponseBody(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        node_id: str = None,
        order_id: int = None,
        region_id: str = None,
        request_id: str = None,
        vcluster_id: str = None,
        vk_name: str = None,
        zone_id: str = None,
    ):
        # The ID of the Tair VNode instance.
        self.instance_id = instance_id
        # The ID of the VNode.
        self.node_id = node_id
        # The order ID.
        self.order_id = order_id
        # The ID of the region where the instance resides.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the VCluster.
        self.vcluster_id = vcluster_id
        # The ID of the VCluster instance.
        self.vk_name = vk_name
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.vcluster_id is not None:
            result['VClusterId'] = self.vcluster_id

        if self.vk_name is not None:
            result['VkName'] = self.vk_name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VClusterId') is not None:
            self.vcluster_id = m.get('VClusterId')

        if m.get('VkName') is not None:
            self.vk_name = m.get('VkName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

