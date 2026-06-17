# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyConsumerRequest(DaraModel):
    def __init__(
        self,
        consumer_group_name: str = None,
        consumer_id: str = None,
        gw_cluster_id: str = None,
        is_default: str = None,
        name: str = None,
        region_id: str = None,
    ):
        # The name of the consumer group.
        self.consumer_group_name = consumer_group_name
        # The ID of the consumer.
        # 
        # This parameter is required.
        self.consumer_id = consumer_id
        # The ID of the gateway instance.
        # 
        # This parameter is required.
        self.gw_cluster_id = gw_cluster_id
        # Indicates if the consumer is in the default group. Valid values: 0 (No) and 1 (Yes).
        self.is_default = is_default
        # The new name for the consumer.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name

        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')

        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

