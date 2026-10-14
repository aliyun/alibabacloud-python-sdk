# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterDetailResponseBody(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        cluster_id: str = None,
        config: Any = None,
        container_cidr: str = None,
        control_plane_config: main_models.DescribeClusterDetailResponseBodyControlPlaneConfig = None,
        control_plane_meta: main_models.DescribeClusterDetailResponseBodyControlPlaneMeta = None,
        created: str = None,
        ens_region_id: str = None,
        isp: str = None,
        join_token: str = None,
        kubernetes_version: str = None,
        load_balancer_id: str = None,
        name: str = None,
        nat_gateway_id: str = None,
        node_count: main_models.DescribeClusterDetailResponseBodyNodeCount = None,
        pod_status: main_models.DescribeClusterDetailResponseBodyPodStatus = None,
        pod_vswitch_ids: List[str] = None,
        public_access: bool = None,
        request_id: str = None,
        service_cidr: str = None,
        state: str = None,
        vpc_id: str = None,
        vswitch_ids: List[str] = None,
    ):
        # The user ID.
        self.ali_uid = ali_uid
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster kubeconfig.
        self.config = config
        # The CIDR block for pods.
        self.container_cidr = container_cidr
        # The control plane configuration.
        self.control_plane_config = control_plane_config
        self.control_plane_meta = control_plane_meta
        self.created = created
        # The ENS edge zone ID.
        self.ens_region_id = ens_region_id
        self.isp = isp
        # The authentication token for cluster access.
        self.join_token = join_token
        # The cluster version, which is consistent with the Kubernetes community baseline version. We recommend that you select the latest version. If you do not specify this parameter, the latest version is used by default.
        self.kubernetes_version = kubernetes_version
        # The CLB instance ID of the API server.
        self.load_balancer_id = load_balancer_id
        # The cluster name.
        self.name = name
        self.nat_gateway_id = nat_gateway_id
        self.node_count = node_count
        self.pod_status = pod_status
        # The vSwitch IDs for pods.
        self.pod_vswitch_ids = pod_vswitch_ids
        # Indicates whether public network access is enabled.
        self.public_access = public_access
        # Id of the request。
        self.request_id = request_id
        # The CIDR block for services.
        self.service_cidr = service_cidr
        # The cluster status. Valid values:
        # - **initial**: Being created.
        # - **failed**: Creation failed.
        # - **running**: Running.
        # - **deleting**: Being released.
        self.state = state
        # The VPC used by the cluster.
        self.vpc_id = vpc_id
        # The vSwitch IDs of the cluster nodes.
        self.vswitch_ids = vswitch_ids

    def validate(self):
        if self.control_plane_config:
            self.control_plane_config.validate()
        if self.control_plane_meta:
            self.control_plane_meta.validate()
        if self.node_count:
            self.node_count.validate()
        if self.pod_status:
            self.pod_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.config is not None:
            result['Config'] = self.config

        if self.container_cidr is not None:
            result['ContainerCidr'] = self.container_cidr

        if self.control_plane_config is not None:
            result['ControlPlaneConfig'] = self.control_plane_config.to_map()

        if self.control_plane_meta is not None:
            result['ControlPlaneMeta'] = self.control_plane_meta.to_map()

        if self.created is not None:
            result['Created'] = self.created

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.join_token is not None:
            result['JoinToken'] = self.join_token

        if self.kubernetes_version is not None:
            result['KubernetesVersion'] = self.kubernetes_version

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.name is not None:
            result['Name'] = self.name

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.node_count is not None:
            result['NodeCount'] = self.node_count.to_map()

        if self.pod_status is not None:
            result['PodStatus'] = self.pod_status.to_map()

        if self.pod_vswitch_ids is not None:
            result['PodVswitchIds'] = self.pod_vswitch_ids

        if self.public_access is not None:
            result['PublicAccess'] = self.public_access

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_cidr is not None:
            result['ServiceCidr'] = self.service_cidr

        if self.state is not None:
            result['State'] = self.state

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_ids is not None:
            result['VswitchIds'] = self.vswitch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ContainerCidr') is not None:
            self.container_cidr = m.get('ContainerCidr')

        if m.get('ControlPlaneConfig') is not None:
            temp_model = main_models.DescribeClusterDetailResponseBodyControlPlaneConfig()
            self.control_plane_config = temp_model.from_map(m.get('ControlPlaneConfig'))

        if m.get('ControlPlaneMeta') is not None:
            temp_model = main_models.DescribeClusterDetailResponseBodyControlPlaneMeta()
            self.control_plane_meta = temp_model.from_map(m.get('ControlPlaneMeta'))

        if m.get('Created') is not None:
            self.created = m.get('Created')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('JoinToken') is not None:
            self.join_token = m.get('JoinToken')

        if m.get('KubernetesVersion') is not None:
            self.kubernetes_version = m.get('KubernetesVersion')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NodeCount') is not None:
            temp_model = main_models.DescribeClusterDetailResponseBodyNodeCount()
            self.node_count = temp_model.from_map(m.get('NodeCount'))

        if m.get('PodStatus') is not None:
            temp_model = main_models.DescribeClusterDetailResponseBodyPodStatus()
            self.pod_status = temp_model.from_map(m.get('PodStatus'))

        if m.get('PodVswitchIds') is not None:
            self.pod_vswitch_ids = m.get('PodVswitchIds')

        if m.get('PublicAccess') is not None:
            self.public_access = m.get('PublicAccess')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceCidr') is not None:
            self.service_cidr = m.get('ServiceCidr')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchIds') is not None:
            self.vswitch_ids = m.get('VswitchIds')

        return self

class DescribeClusterDetailResponseBodyPodStatus(DaraModel):
    def __init__(
        self,
        running: int = None,
        total: int = None,
    ):
        self.running = running
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.running is not None:
            result['Running'] = self.running

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Running') is not None:
            self.running = m.get('Running')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeClusterDetailResponseBodyNodeCount(DaraModel):
    def __init__(
        self,
        ready: int = None,
        total: int = None,
    ):
        self.ready = ready
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ready is not None:
            result['Ready'] = self.ready

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ready') is not None:
            self.ready = m.get('Ready')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeClusterDetailResponseBodyControlPlaneMeta(DaraModel):
    def __init__(
        self,
        master_instances: List[main_models.DescribeClusterDetailResponseBodyControlPlaneMetaMasterInstances] = None,
        master_url: main_models.DescribeClusterDetailResponseBodyControlPlaneMetaMasterUrl = None,
    ):
        self.master_instances = master_instances
        self.master_url = master_url

    def validate(self):
        if self.master_instances:
            for v1 in self.master_instances:
                 if v1:
                    v1.validate()
        if self.master_url:
            self.master_url.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MasterInstances'] = []
        if self.master_instances is not None:
            for k1 in self.master_instances:
                result['MasterInstances'].append(k1.to_map() if k1 else None)

        if self.master_url is not None:
            result['MasterUrl'] = self.master_url.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.master_instances = []
        if m.get('MasterInstances') is not None:
            for k1 in m.get('MasterInstances'):
                temp_model = main_models.DescribeClusterDetailResponseBodyControlPlaneMetaMasterInstances()
                self.master_instances.append(temp_model.from_map(k1))

        if m.get('MasterUrl') is not None:
            temp_model = main_models.DescribeClusterDetailResponseBodyControlPlaneMetaMasterUrl()
            self.master_url = temp_model.from_map(m.get('MasterUrl'))

        return self

class DescribeClusterDetailResponseBodyControlPlaneMetaMasterUrl(DaraModel):
    def __init__(
        self,
        private_url: str = None,
        public_url: str = None,
    ):
        self.private_url = private_url
        self.public_url = public_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_url is not None:
            result['PrivateUrl'] = self.private_url

        if self.public_url is not None:
            result['PublicUrl'] = self.public_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateUrl') is not None:
            self.private_url = m.get('PrivateUrl')

        if m.get('PublicUrl') is not None:
            self.public_url = m.get('PublicUrl')

        return self

class DescribeClusterDetailResponseBodyControlPlaneMetaMasterInstances(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        ip: str = None,
        name: str = None,
    ):
        self.instance_id = instance_id
        self.ip = ip
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeClusterDetailResponseBodyControlPlaneConfig(DaraModel):
    def __init__(
        self,
        container_runtime: str = None,
        image_id: str = None,
        instance_spec: str = None,
        node_port_range: str = None,
        size: int = None,
        system_disk_category: str = None,
        system_disk_size: int = None,
    ):
        # The container runtime type.
        self.container_runtime = container_runtime
        # The image ID of the control plane virtual machine.
        self.image_id = image_id
        # The node instance type.
        self.instance_spec = instance_spec
        # The node service port range.
        self.node_port_range = node_port_range
        # The number of control plane nodes.
        self.size = size
        # The system cloud disk type of the node.
        self.system_disk_category = system_disk_category
        # The system cloud disk size of the node.
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_runtime is not None:
            result['ContainerRuntime'] = self.container_runtime

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.node_port_range is not None:
            result['NodePortRange'] = self.node_port_range

        if self.size is not None:
            result['Size'] = self.size

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerRuntime') is not None:
            self.container_runtime = m.get('ContainerRuntime')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('NodePortRange') is not None:
            self.node_port_range = m.get('NodePortRange')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

