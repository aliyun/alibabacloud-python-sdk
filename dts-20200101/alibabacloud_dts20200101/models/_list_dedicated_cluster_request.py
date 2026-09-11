# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDedicatedClusterRequest(DaraModel):
    def __init__(
        self,
        order_column: str = None,
        order_direction: str = None,
        owner_id: str = None,
        page_number: int = None,
        page_size: int = None,
        params: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        state: str = None,
        type: str = None,
    ):
        # The sort column when the response contains multiple DTS dedicated cluster instances. Valid values:
        # 
        # - **gmtCreated**: creation time.
        # - **orderCount**: number of nodes.
        self.order_column = order_column
        # The sort order. Valid values:
        # 
        # - **asc**: ascending order. This is the default value.
        # - **desc**: descending order.
        self.order_direction = order_direction
        self.owner_id = owner_id
        # The page number. The value must be a positive integer that does not exceed the maximum value of the Integer data type. Default value: **1**.
        self.page_number = page_number
        # The number of clusters to display per page.
        self.page_size = page_size
        # The specific content of the query condition.
        # 
        # > You must first specify the **Type** parameter to define the query key.
        self.params = params
        # The region ID. This parameter is used as a query condition.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The cluster status. Valid values:
        # 
        # - **init**: initializing.
        # - **schedule**: pending scheduling.
        # - **running**: running.
        # - **upgrade**: upgrading.
        # - **downgrade**: downgrading.
        # - **locked**: locked.
        # - **releasing**: being released.
        # - **released**: released.
        self.state = state
        # The query key. Valid values:
        # 
        # - **NAME**: cluster name.
        # - **INSTANCE**: cluster instance ID.
        # - **DEDICATEDCLUSTERID**: dedicated cluster ID.
        # 
        # > You must also specify the **Params** parameter to provide the specific content of the query condition.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_column is not None:
            result['OrderColumn'] = self.order_column

        if self.order_direction is not None:
            result['OrderDirection'] = self.order_direction

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.params is not None:
            result['Params'] = self.params

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.state is not None:
            result['State'] = self.state

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderColumn') is not None:
            self.order_column = m.get('OrderColumn')

        if m.get('OrderDirection') is not None:
            self.order_direction = m.get('OrderDirection')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

