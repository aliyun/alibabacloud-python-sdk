# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyElasticBizQpsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        mode: str = None,
        ops_elastic_qps: int = None,
    ):
        # The ID of the Anti-DDoS Proxy instance.
        # 
        # >  You can call the [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) operation to query the IDs of all instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The metering method for the burstable QPS. Valid values:
        # 
        # *   **month**: monthly 95th percentile
        # *   **day**: daily 95th percentile QPS
        # 
        # This parameter is required.
        self.mode = mode
        # The burstable QPS value.
        # 
        # >  The default value is 300,000 for the Chinese mainland and 150,000 for regions outside the Chinese mainland.
        self.ops_elastic_qps = ops_elastic_qps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.ops_elastic_qps is not None:
            result['OpsElasticQps'] = self.ops_elastic_qps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('OpsElasticQps') is not None:
            self.ops_elastic_qps = m.get('OpsElasticQps')

        return self

