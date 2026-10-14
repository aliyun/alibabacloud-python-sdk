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
        isp: str = None,
        kubernetes_version: str = None,
        load_balancer_id: str = None,
        name: str = None,
        nat_gateway_id: str = None,
        pod_vswitch_ids_shrink: str = None,
        profile: str = None,
        public_access: bool = None,
        service_cidr: str = None,
        vpc_id: str = None,
        vswitch_ids_shrink: str = None,
    ):
        # Kubernetes or ManagedKubernetes. The former indicates an ECK cluster, and the latter indicates a serverless VC.
        # Must be used together with the profile parameter.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # The pod network CIDR block. The CIDR block must be a valid private CIDR block, which includes the following CIDR blocks and their subnets: 10.0.0.0/8, 172.16-31.0.0/12-16, and 192.168.0.0/16. The CIDR block cannot overlap with the CIDR blocks used by the VPC or existing Kubernetes clusters in the VPC. You cannot modify the CIDR block after the cluster is created.
        self.container_cidr = container_cidr
        # The control plane configuration.
        self.control_plane_config_shrink = control_plane_config_shrink
        # The ENS Region ID of the cluster.
        self.ens_region_id = ens_region_id
        self.isp = isp
        # The cluster version, which is consistent with the Kubernetes community baseline version. Select the latest version. If you do not specify this parameter, the latest version is used by default.
        self.kubernetes_version = kubernetes_version
        # The ID of the CLB instance used for API Server access. If you specify this parameter, automatic creation of a CLB instance for the API Server is skipped.
        self.load_balancer_id = load_balancer_id
        # The cluster name.
        self.name = name
        self.nat_gateway_id = nat_gateway_id
        # Each pod vSwitch corresponds to a worker node vSwitch. The zone of the pod vSwitch must be the same as that of the worker node vSwitch. If you do not specify this parameter, vswitch_ids is used by default.
        self.pod_vswitch_ids_shrink = pod_vswitch_ids_shrink
        # Default or Serverless. The former indicates an ECK cluster, and the latter indicates a serverless VC.
        # Must be used together with the cluster_type parameter.
        # 
        # This parameter is required.
        self.profile = profile
        # Specifies whether to enable public network access. The API Server is exposed through an EIP to enable public access to the cluster.
        # ● true: Enable public network access.
        # ● false: Disable public network access. If you select this option, you cannot access the cluster API Server from the Internet.
        # Default value: false.
        self.public_access = public_access
        # The service network CIDR block. Valid ranges: 10.0.0.0/16-24, 172.16-31.0.0/16-24, and 192.168.0.0/16-24. The CIDR block cannot overlap with the VPC CIDR block 10.1.0.0/21 or the CIDR blocks used by existing Kubernetes clusters in the VPC. You cannot modify the CIDR block after the cluster is created.
        self.service_cidr = service_cidr
        # The VPC used by the cluster.
        self.vpc_id = vpc_id
        # The IDs of the vSwitches for cluster nodes. The ENS Region of the vswitch_ids must be the same as the ens_region_id value.
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

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.kubernetes_version is not None:
            result['KubernetesVersion'] = self.kubernetes_version

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.name is not None:
            result['Name'] = self.name

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

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

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('KubernetesVersion') is not None:
            self.kubernetes_version = m.get('KubernetesVersion')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

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

