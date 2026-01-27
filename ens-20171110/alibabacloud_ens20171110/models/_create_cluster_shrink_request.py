# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateClusterShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        container_cidr: str = None,
        control_plane_config_shrink: str = None,
        ens_region_id: str = None,
        kubernetes_version: str = None,
        load_balancer_id: str = None,
        name: str = None,
        pod_vswitch_ids_shrink: str = None,
        profile: str = None,
        public_access: bool = None,
        service_cidr: str = None,
        vpc_id: str = None,
        vswitch_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.cluster_type = cluster_type
        self.container_cidr = container_cidr
        self.control_plane_config_shrink = control_plane_config_shrink
        self.ens_region_id = ens_region_id
        self.kubernetes_version = kubernetes_version
        self.load_balancer_id = load_balancer_id
        # The name of the cluster.
        self.name = name
        self.pod_vswitch_ids_shrink = pod_vswitch_ids_shrink
        # This parameter is required.
        self.profile = profile
        self.public_access = public_access
        self.service_cidr = service_cidr
        self.vpc_id = vpc_id
        self.vswitch_ids_shrink = vswitch_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.container_cidr is not None:
            result['ContainerCidr'] = self.container_cidr

        if self.control_plane_config_shrink is not None:
            result['ControlPlaneConfig'] = self.control_plane_config_shrink

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.kubernetes_version is not None:
            result['KubernetesVersion'] = self.kubernetes_version

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.name is not None:
            result['Name'] = self.name

        if self.pod_vswitch_ids_shrink is not None:
            result['PodVswitchIds'] = self.pod_vswitch_ids_shrink

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.public_access is not None:
            result['PublicAccess'] = self.public_access

        if self.service_cidr is not None:
            result['ServiceCidr'] = self.service_cidr

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_ids_shrink is not None:
            result['VswitchIds'] = self.vswitch_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('ContainerCidr') is not None:
            self.container_cidr = m.get('ContainerCidr')

        if m.get('ControlPlaneConfig') is not None:
            self.control_plane_config_shrink = m.get('ControlPlaneConfig')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('KubernetesVersion') is not None:
            self.kubernetes_version = m.get('KubernetesVersion')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PodVswitchIds') is not None:
            self.pod_vswitch_ids_shrink = m.get('PodVswitchIds')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('PublicAccess') is not None:
            self.public_access = m.get('PublicAccess')

        if m.get('ServiceCidr') is not None:
            self.service_cidr = m.get('ServiceCidr')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchIds') is not None:
            self.vswitch_ids_shrink = m.get('VswitchIds')

        return self

