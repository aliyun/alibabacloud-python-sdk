# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddPrometheusIntegrationRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        integration_type: str = None,
        param: str = None,
        region_id: str = None,
    ):
        # The ID of the Prometheus instance. Only a Prometheus instance for Container Service or a Prometheus instance for ECS is supported.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The type of the integration.
        # 
        # This parameter is required.
        self.integration_type = integration_type
        # The configurations of the exporter. The value is a JSON string.
        # 
        # This parameter is required.
        self.param = param
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

        if self.integration_type is not None:
            result['IntegrationType'] = self.integration_type

        if self.param is not None:
            result['Param'] = self.param

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('IntegrationType') is not None:
            self.integration_type = m.get('IntegrationType')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

