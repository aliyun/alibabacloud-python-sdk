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
        ens_region_id: str = None,
        join_token: str = None,
        kubernetes_version: str = None,
        load_balancer_id: str = None,
        name: str = None,
        pod_vswitch_ids: List[str] = None,
        public_access: bool = None,
        service_cidr: str = None,
        vpc_id: str = None,
        vswitch_ids: List[str] = None,
    ):
        self.ali_uid = ali_uid
        self.cluster_id = cluster_id
        self.config = config
        self.container_cidr = container_cidr
        self.control_plane_config = control_plane_config
        self.ens_region_id = ens_region_id
        self.join_token = join_token
        self.kubernetes_version = kubernetes_version
        self.load_balancer_id = load_balancer_id
        self.name = name
        self.pod_vswitch_ids = pod_vswitch_ids
        self.public_access = public_access
        self.service_cidr = service_cidr
        self.vpc_id = vpc_id
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

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

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

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

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
        self.container_runtime = container_runtime
        self.image_id = image_id
        self.instance_spec = instance_spec
        self.node_port_range = node_port_range
        self.size = size
        self.system_disk_category = system_disk_category
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

