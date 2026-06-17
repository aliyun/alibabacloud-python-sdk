# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeConsumersRequest(DaraModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        consumer_id: str = None,
        gw_cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The consumer group ID.
        self.consumer_group_id = consumer_group_id
        # The consumer ID.
        self.consumer_id = consumer_id
        # The gateway instance ID.
        # 
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        # The page number. The default value is 1.
        self.page_number = page_number
        # The number of entries to return on each page. Valid values are:
        # 
        # - **30**
        # 
        # - **50**
        # 
        # - **100**. The default is **30**.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_group_id is not None:
            result['ConsumerGroupId'] = self.consumer_group_id

        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroupId') is not None:
            self.consumer_group_id = m.get('ConsumerGroupId')

        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

