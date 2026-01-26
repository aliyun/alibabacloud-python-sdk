# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPrometheusInstancesRequest(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        region_id: str = None,
        show_global_view: bool = None,
    ):
        # The cluster type. If you do not specify this parameter, all cluster types are queried. Valid values:
        # 
        # *   cloud-product-prometheus: Prometheus instance for cloud services
        # *   ManagedKubernetes: ACK managed cluster
        # *   satellite: Prometheus instance for ARMS OpenTelemetry
        # *   Ask: ACK Serverless cluster
        # *   remote-write-prometheus: general-purpose Prometheus instance
        # *   cloud-monitor-cmee: Hybrid Cloud Monitoring
        # *   ExternalKubernetes: external Kubernetes cluster registered in ACK
        # *   vpc-prometheus: Prometheus instance for ECS
        # *   cloud-monitor-direct: cloud service self-monitoring
        # *   Edge Kubernetes: ACK Edge cluster
        self.cluster_type = cluster_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to obtain global aggregation instances. Valid values:
        # 
        # *   true
        # *   false
        # 
        # This parameter is required.
        self.show_global_view = show_global_view

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.show_global_view is not None:
            result['ShowGlobalView'] = self.show_global_view

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShowGlobalView') is not None:
            self.show_global_view = m.get('ShowGlobalView')

        return self

