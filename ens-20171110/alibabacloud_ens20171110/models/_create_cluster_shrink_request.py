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
        # Kubernetes or ManagedKubernetes. The former indicates an ECK cluster, and the latter indicates a serverless VC. This parameter must be used together with the Profile parameter.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # The CIDR block for pods. It must be a valid private CIDR block, such as 10.0.0.0/8, 172.16.0.0/12 to 172.31.0.0/16, or 192.168.0.0/16, and their subnets. The CIDR block cannot overlap with the CIDR block of the VPC or the CIDR blocks used by existing Kubernetes clusters in the VPC. The CIDR block cannot be modified after the cluster is created.
        self.container_cidr = container_cidr
        # The control plane configuration.
        self.control_plane_config_shrink = control_plane_config_shrink
        # The ID of the Edge Node Service (ENS) region where the cluster is deployed.
        self.ens_region_id = ens_region_id
        # The Internet service provider (ISP) information. Valid values:
        # 
        # - **cmcc**: China Mobile.
        # - **unicom**: China Unicom.
        # - **telecom**: China Telecom.
        self.isp = isp
        # The Kubernetes version of the cluster. The version aligns with the Kubernetes community baseline version. We recommend that you select the latest version. If you do not specify this parameter, the latest version is used by default.
        self.kubernetes_version = kubernetes_version
        # The ID of the Classic Load Balancer (CLB) instance used for API server access. If you specify this parameter, automatic creation of a CLB instance for the API server is skipped.
        self.load_balancer_id = load_balancer_id
        # The name of the cluster.
        self.name = name
        # The ID of the NAT gateway used by the cluster. If you specify this parameter, automatic creation of a NAT gateway is skipped.
        self.nat_gateway_id = nat_gateway_id
        # The IDs of the pod vSwitches. Each pod vSwitch corresponds to a worker node vSwitch. The pod vSwitch and the worker node vSwitch must be in the same zone. If you do not specify this parameter, the vSwitches specified by the VswitchIds parameter are used by default.
        self.pod_vswitch_ids_shrink = pod_vswitch_ids_shrink
        # Default or Serverless. The former indicates an ECK cluster, and the latter indicates a serverless VC. This parameter must be used together with the ClusterType parameter.
        # 
        # This parameter is required.
        self.profile = profile
        # Specifies whether to enable public network access. You can expose the API server by using an elastic IP address (EIP) to enable public network access to the cluster. Valid values:
        # - true: enables public network access.
        # - false: disables public network access. If you select false, you cannot access the API server of the cluster over the Internet.
        # Default value: false.
        self.public_access = public_access
        # The CIDR block for Services. Valid ranges include 10.0.0.0/16 to 10.0.0.0/24, 172.16.0.0/16 to 172.31.0.0/24, and 192.168.0.0/16 to 192.168.0.0/24. The CIDR block cannot overlap with the VPC CIDR block 10.1.0.0/21 or the CIDR blocks used by existing Kubernetes clusters in the VPC. The CIDR block cannot be modified after the cluster is created.
        self.service_cidr = service_cidr
        # The ID of the virtual private cloud (VPC) used by the cluster.
        self.vpc_id = vpc_id
        # The IDs of the vSwitches where the cluster nodes are deployed. The ENS region of the vSwitches must be the same as the ENS region specified by the EnsRegionId parameter.
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

