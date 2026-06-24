# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNodePoolAttributeShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        node_capacity: int = None,
        node_pool_strategy_shrink: str = None,
        pool_id: str = None,
        product_type: str = None,
    ):
        # The region ID of the delivery group. For more information about supported regions, see [Limits](https://help.aliyun.com/document_detail/426036.html).
        self.biz_region_id = biz_region_id
        # The number of concurrent sessions, which is the number of sessions that can be simultaneously connected to a single resource. If too many sessions are connected simultaneously, the application experience may degrade. The valid values vary depending on the resource specification. The valid values for each resource specification are as follows:
        # 
        # - appstreaming.general.4c8g: 1 to 2.
        # - appstreaming.general.8c16g: 1 to 4.
        # - appstreaming.vgpu.8c16g.4g: 1 to 4.
        # - appstreaming.vgpu.8c31g.16g: 1 to 4.
        # - appstreaming.vgpu.14c93g.12g: 1 to 6.
        self.node_capacity = node_capacity
        # The automatic scaling policy of the delivery group.
        self.node_pool_strategy_shrink = node_pool_strategy_shrink
        # The resource group ID.
        self.pool_id = pool_id
        # The product type.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity

        if self.node_pool_strategy_shrink is not None:
            result['NodePoolStrategy'] = self.node_pool_strategy_shrink

        if self.pool_id is not None:
            result['PoolId'] = self.pool_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')

        if m.get('NodePoolStrategy') is not None:
            self.node_pool_strategy_shrink = m.get('NodePoolStrategy')

        if m.get('PoolId') is not None:
            self.pool_id = m.get('PoolId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

