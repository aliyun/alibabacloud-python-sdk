# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConsumerProgressRequest(DaraModel):
    def __init__(
        self,
        consumer_id: str = None,
        hide_last_timestamp: bool = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The name of the consumer group.
        # 
        # This parameter is required.
        self.consumer_id = consumer_id
        # Specifies whether to hide LastTimestamp. Default value: false. We recommend that you set this parameter to true.
        # 
        # > 
        # 
        # *   If you set this parameter to true, -1 is returned for LastTimestamp. If you set this parameter to false, a specific value is returned for LastTimestamp. This parameter is supported only by topics that use cloud storage on reserved instances.
        # 
        # *   A large amount of data is processed by this operation, which causes performance loss. We recommend that you set this parameter to true to accelerate processing.
        self.hide_last_timestamp = hide_last_timestamp
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
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
        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id

        if self.hide_last_timestamp is not None:
            result['HideLastTimestamp'] = self.hide_last_timestamp

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('HideLastTimestamp') is not None:
            self.hide_last_timestamp = m.get('HideLastTimestamp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

