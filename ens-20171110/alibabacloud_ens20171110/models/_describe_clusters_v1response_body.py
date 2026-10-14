# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeClustersV1ResponseBody(DaraModel):
    def __init__(
        self,
        clusters: List[main_models.DescribeClustersV1ResponseBodyClusters] = None,
        request_id: str = None,
    ):
        # The list of clusters.
        self.clusters = clusters
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.clusters:
            for v1 in self.clusters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Clusters'] = []
        if self.clusters is not None:
            for k1 in self.clusters:
                result['Clusters'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k1 in m.get('Clusters'):
                temp_model = main_models.DescribeClustersV1ResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClustersV1ResponseBodyClusters(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        cluster_id: str = None,
        config: Any = None,
        container_cidr: str = None,
        control_plane_config: main_models.DescribeClustersV1ResponseBodyClustersControlPlaneConfig = None,
        created: str = None,
        ens_region_id: str = None,
        isp: str = None,
        join_token: str = None,
        kubernetes_version: str = None,
        load_balancer_id: str = None,
        name: str = None,
        pod_vswitch_ids: List[str] = None,
        public_access: bool = None,
        service_cidr: str = None,
        state: str = None,
        vpc_id: str = None,
        vswitch_ids: List[str] = None,
    ):
        # The user ID.
        self.ali_uid = ali_uid
        # The cluster instance ID.
        self.cluster_id = cluster_id
        # The cluster kubeconfig.
        self.config = config
        # The pod network CIDR block. The value must be a valid private CIDR block, which includes the following CIDR blocks and their subnets: 10.0.0.0/8, 172.16-31.0.0/12-16, and 192.168.0.0/16. The CIDR block cannot overlap with the VPC CIDR block or the CIDR blocks used by existing Kubernetes clusters in the VPC. You cannot modify this value after the cluster is created.
        self.container_cidr = container_cidr
        # The control plane configuration.
        self.control_plane_config = control_plane_config
        self.created = created
        # The ENS node ID.
        self.ens_region_id = ens_region_id
        self.isp = isp
        # The authentication token for cluster access.
        self.join_token = join_token
        # The cluster version, which is consistent with the Kubernetes community baseline version. Use the latest version. If you do not specify this parameter, the latest version is used by default.
        self.kubernetes_version = kubernetes_version
        # The load balancing instance ID.
        self.load_balancer_id = load_balancer_id
        # The cluster name.
        self.name = name
        # The vSwitch IDs for pods. Each pod vSwitch corresponds to a worker node vSwitch, and the zones of the pod vSwitch and the worker node vSwitch must be the same. If you leave this parameter empty, the value of vswitch_ids is used by default.
        self.pod_vswitch_ids = pod_vswitch_ids
        # Indicates whether public network access is enabled. The API Server is exposed through an EIP to enable public access to the cluster. Valid values:
        # 
        # - true: Public network access is enabled.
        # - false: Public network access is disabled. If you select this option, the cluster API Server cannot be accessed from the Internet.
        self.public_access = public_access
        # The service network CIDR block. Valid ranges: 10.0.0.0/16-24, 172.16-31.0.0/16-24, and 192.168.0.0/16-24. The CIDR block cannot overlap with the VPC CIDR block 10.1.0.0/21 or the CIDR blocks used by existing Kubernetes clusters in the VPC. You cannot modify this value after the cluster is created.
        self.service_cidr = service_cidr
        # The cluster status.
        self.state = state
        # The VPC used by the cluster.
        self.vpc_id = vpc_id
        # The vSwitch IDs of the cluster nodes. The ENS region of the vSwitch IDs must be the same as the value of ens_region_id.
        self.vswitch_ids = vswitch_ids

    def validate(self):
        if self.control_plane_config:
            self.control_plane_config.validate()

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

        if self.pod_vswitch_ids is not None:
            result['PodVswitchIds'] = self.pod_vswitch_ids

        if self.public_access is not None:
            result['PublicAccess'] = self.public_access

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
            temp_model = main_models.DescribeClustersV1ResponseBodyClustersControlPlaneConfig()
            self.control_plane_config = temp_model.from_map(m.get('ControlPlaneConfig'))

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

        if m.get('PodVswitchIds') is not None:
            self.pod_vswitch_ids = m.get('PodVswitchIds')

        if m.get('PublicAccess') is not None:
            self.public_access = m.get('PublicAccess')

        if m.get('ServiceCidr') is not None:
            self.service_cidr = m.get('ServiceCidr')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchIds') is not None:
            self.vswitch_ids = m.get('VswitchIds')

        return self

class DescribeClustersV1ResponseBodyClustersControlPlaneConfig(DaraModel):
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
        # The image ID.
        self.image_id = image_id
        # The instance type.
        self.instance_spec = instance_spec
        # The node service port range.
        self.node_port_range = node_port_range
        # The number of control plane nodes.
        self.size = size
        # The system cloud disk type of the node. Valid values: local_ssd, cloud_ssd, cloud_efficiency, and local_hdd.
        self.system_disk_category = system_disk_category
        # The system cloud disk size. Unit: GB.
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

