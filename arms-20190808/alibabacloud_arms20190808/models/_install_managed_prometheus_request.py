# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstallManagedPrometheusRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        grafana_instance_id: str = None,
        kube_config: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vc_extra_info: str = None,
        vpc_id: str = None,
    ):
        # The ID of the ASK cluster.
        self.cluster_id = cluster_id
        # The name of the cluster. This parameter is required if the ClusterType parameter is set to ecs.
        self.cluster_name = cluster_name
        # The cluster type.
        # 
        # Valid values:
        # 
        # *   ecs: ECS
        # *   one: ACK One
        # *   ask: ASK
        # *   pro: Container Monitoring Pro
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # The ID of the managed Grafana workspace that is associated with the cluster. If you set this parameter to free or leave this parameter empty, the cluster is associated with a shared Grafana workspace.
        self.grafana_instance_id = grafana_instance_id
        # This parameter is not supported.
        self.kube_config = kube_config
        # The region ID.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        # The ID of the security group to which the cluster belongs.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The ID of the vSwitch that is used by the cluster.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        self.vc_extra_info = vc_extra_info
        # The virtual private cloud (VPC) where the cluster resides.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.grafana_instance_id is not None:
            result['GrafanaInstanceId'] = self.grafana_instance_id

        if self.kube_config is not None:
            result['KubeConfig'] = self.kube_config

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vc_extra_info is not None:
            result['VcExtraInfo'] = self.vc_extra_info

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('GrafanaInstanceId') is not None:
            self.grafana_instance_id = m.get('GrafanaInstanceId')

        if m.get('KubeConfig') is not None:
            self.kube_config = m.get('KubeConfig')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VcExtraInfo') is not None:
            self.vc_extra_info = m.get('VcExtraInfo')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

