# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyElasticBizBandWidthRequest(DaraModel):
    def __init__(
        self,
        elastic_biz_bandwidth: int = None,
        instance_id: str = None,
        mode: str = None,
    ):
        # The burstable clean bandwidth. Unit: Mbit/s. The burstable clean bandwidth cannot exceed nine times the clean bandwidth of your Anti-DDoS Pro or Anti-DDoS Premium instance, and the sum of the clean bandwidth and the burstable clean bandwidth cannot exceed the maximum clean bandwidth that is supported by your instance. The value 0 indicates that the burstable clean bandwidth feature is disabled. You can disable the burstable clean bandwidth feature once a month.
        # 
        # This parameter is required.
        self.elastic_biz_bandwidth = elastic_biz_bandwidth
        # The ID of the instance.
        # 
        # > You can call the [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) operation to query the IDs of all instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The metering method of the burstable clean bandwidth feature. Valid values:
        # 
        # *   **month**: the metering method of monthly 95th percentile
        # *   **day**: the metering method of daily 95th percentile
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_biz_bandwidth is not None:
            result['ElasticBizBandwidth'] = self.elastic_biz_bandwidth

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticBizBandwidth') is not None:
            self.elastic_biz_bandwidth = m.get('ElasticBizBandwidth')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

