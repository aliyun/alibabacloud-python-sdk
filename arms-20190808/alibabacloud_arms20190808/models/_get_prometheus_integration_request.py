# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPrometheusIntegrationRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance_id: int = None,
        integration_type: str = None,
        region_id: str = None,
    ):
        # The ID of the Prometheus instance. Valid values: aliyun-cs and ecs.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the exporter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The integration type. Valid values: kafka, mysql, redis, snmp, emr, nubela, and tidb.
        # 
        # This parameter is required.
        self.integration_type = integration_type
        # The region ID.
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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

