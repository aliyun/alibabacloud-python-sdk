# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyElasticBandWidthRequest(DaraModel):
    def __init__(
        self,
        elastic_bandwidth: int = None,
        instance_id: str = None,
    ):
        # The new burstable protection bandwidth that you want to use. Unit: Gbit/s.
        # 
        # > You can call the [DescribeElasticBandwidthSpec](https://help.aliyun.com/document_detail/91502.html) operation to query the available burstable protection bandwidth of the instance.
        # 
        # This parameter is required.
        self.elastic_bandwidth = elastic_bandwidth
        # The ID of the instance.
        # 
        # >  The instance must be in a normal state. You can call the [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) operation to query the IDs of all instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

