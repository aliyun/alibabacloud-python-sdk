# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeClustersV1ResponseBody(DaraModel):
    def __init__(
        self,
        clusters: List[main_models.DescribeClustersV1ResponseBodyClusters] = None,
        page_info: main_models.DescribeClustersV1ResponseBodyPageInfo = None,
    ):
        # The queried cluster details.
        self.clusters = clusters
        # The pagination information.
        self.page_info = page_info

    def validate(self):
        if self.clusters:
            for v1 in self.clusters:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['clusters'] = []
        if self.clusters is not None:
            for k1 in self.clusters:
                result['clusters'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('clusters') is not None:
            for k1 in m.get('clusters'):
                temp_model = main_models.DescribeClustersV1ResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k1))

        if m.get('page_info') is not None:
            temp_model = main_models.DescribeClustersV1ResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('page_info'))

        return self

class DescribeClustersV1ResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.total_count is not None:
            result['total_count'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')

        return self

class DescribeClustersV1ResponseBodyClusters(DaraModel):
    def __init__(
        self,
        cluster_domain: str = None,
        cluster_id: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        container_cidr: str = None,
        created: str = None,
        current_version: str = None,
        deletion_protection: bool = None,
        docker_version: str = None,
        external_loadbalancer_id: str = None,
        init_version: str = None,
        ip_stack: str = None,
        maintenance_window: main_models.MaintenanceWindow = None,
        master_url: str = None,
        meta_data: str = None,
        name: str = None,
        network_mode: str = None,
        next_version: str = None,
        operation_policy: main_models.DescribeClustersV1ResponseBodyClustersOperationPolicy = None,
        private_zone: bool = None,
        profile: str = None,
        proxy_mode: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        service_cidr: str = None,
        size: int = None,
        state: str = None,
        subnet_cidr: str = None,
        tags: List[main_models.Tag] = None,
        timezone: str = None,
        updated: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        vswitch_ids: List[str] = None,
        worker_ram_role_name: str = None,
        zone_id: str = None,
    ):
        # The domain name of the cluster.
        self.cluster_domain = cluster_domain
        # The cluster ID.
        self.cluster_id = cluster_id
        # The specification of the cluster.
        self.cluster_spec = cluster_spec
        # The type of the instance.
        self.cluster_type = cluster_type
        # The pod CIDR block and the configuration of the Flannel network plug-in.
        self.container_cidr = container_cidr
        # The time at which the instance is created.
        self.created = created
        # The Kubernetes version of the cluster.
        self.current_version = current_version
        # Specifies whether to enable cluster deletion protection. If you enable this option, the cluster cannot be deleted in the console or by calling API operations. Valid values:
        # 
        # *   `true`: enables deletion protection for the cluster. This way, the cluster cannot be deleted in the ACK console or by calling API operations.
        # *   `false`: disables deletion protection for the cluster. This way, the cluster can be deleted in the ACK console or by calling API operations.
        self.deletion_protection = deletion_protection
        # The Docker version that is used by the cluster.
        self.docker_version = docker_version
        # The ID of the Server Load Balancer (SLB) instance that is used by the Ingresses of the cluster.
        # 
        # The default SLB specification is slb.s1.small, which belongs to the high-performance instance type.
        self.external_loadbalancer_id = external_loadbalancer_id
        # The version of the cluster. For more information about the Kubernetes versions supported by ACK, see [Release notes for Kubernetes versions](https://help.aliyun.com/document_detail/185269.html).
        self.init_version = init_version
        # The IP stack of the cluster. Valid values:
        # 
        # *   ipv4: creates a cluster that supports only the IPv4 protocol stack.
        # *   dual: creates a cluster that supports IPv4/IPv6 dual-stack.
        self.ip_stack = ip_stack
        # The maintenance window of the cluster. This feature is available only for ACK managed clusters and ACK Serverless clusters.
        self.maintenance_window = maintenance_window
        # The address of the cluster API server. It includes an internal endpoint and a public endpoint.
        self.master_url = master_url
        # The metadata of the cluster.
        self.meta_data = meta_data
        # The cluster name.
        self.name = name
        # The network mode of the cluster. Valid values:
        # 
        # *   `classic`: classic network.
        # *   `vpc`: virtual private cloud (VPC).
        # *   `overlay`: overlay network.
        # *   `calico`: network powered by Calico.
        self.network_mode = network_mode
        # The Kubernetes version to which the cluster can be updated.
        self.next_version = next_version
        # The automatic O\\&M policy of the cluster.
        self.operation_policy = operation_policy
        # Indicates whether Alibaba Cloud DNS PrivateZone is enabled. Valid values:
        # 
        # *   `true`: Alibaba Cloud DNS PrivateZone is enabled.
        # *   `false`: Alibaba Cloud DNS PrivateZone is disabled.
        self.private_zone = private_zone
        # The subtype of the cluster.
        self.profile = profile
        # The kube-proxy mode.
        # 
        # *   `iptables`: a mature and stable mode that uses iptables rules to conduct service discovery and load balancing. The performance of this mode is limited by the size of the cluster. This mode is suitable for clusters that run a small number of Services.
        # *   `ipvs`: provides high performance and uses IP Virtual Server (IPVS). This allows you to configure service discovery and load balancing. This mode is suitable for clusters that are required to run a large number of services. We recommend that you use this mode in scenarios that require high load balancing performance.
        self.proxy_mode = proxy_mode
        # The region ID of the cluster.
        self.region_id = region_id
        # The ID of the resource group to which the cluster belongs.
        self.resource_group_id = resource_group_id
        # The ID of the security group of the cluster.
        self.security_group_id = security_group_id
        # The Service CIDR block.
        # 
        # This parameter is required.
        self.service_cidr = service_cidr
        # The number of nodes in the cluster, including control planes and worker nodes.
        self.size = size
        # The status of the cluster. Valid values:
        # 
        # *   `initial`: The cluster is being created.
        # *   `failed`: The cluster failed to be created.
        # *   `running`: The cluster is running.
        # *   `upgrading`: The cluster is undergoing an upgrade.
        # *   `updating`: Cluster specification changes are being applied.
        # *   `removing`: Nodes are being removed from the node pool.
        # *   `draining`: Node draining is in progress.
        # *   `scaling`: Auto-scaling operation is in progress for the cluster.
        # *   `stopped`: The cluster has stopped running.
        # *   `deleting`: The cluster is being deleted.
        # *   `deleted`: The cluster has been deleted.
        # *   `delete_failed`: The cluster failed to be deleted.
        self.state = state
        # This parameter is deprecated. Use the container_cidr parameter to obtain the pod CIDR block.
        self.subnet_cidr = subnet_cidr
        # The label of the cluster.
        self.tags = tags
        # The time zone
        self.timezone = timezone
        # The time when the cluster was updated.
        self.updated = updated
        # The ID of the virtual private cloud (VPC) that is used by the cluster.
        self.vpc_id = vpc_id
        # The ID of the vSwitch in the cluster.
        self.vswitch_id = vswitch_id
        # The vSwitches of the control planes.
        self.vswitch_ids = vswitch_ids
        # The name of the worker Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes of the cluster to allow the worker nodes to manage ECS instances.
        self.worker_ram_role_name = worker_ram_role_name
        # The ID of the zone where the cluster is deployed.
        self.zone_id = zone_id

    def validate(self):
        if self.maintenance_window:
            self.maintenance_window.validate()
        if self.operation_policy:
            self.operation_policy.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_domain is not None:
            result['cluster_domain'] = self.cluster_domain

        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec

        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type

        if self.container_cidr is not None:
            result['container_cidr'] = self.container_cidr

        if self.created is not None:
            result['created'] = self.created

        if self.current_version is not None:
            result['current_version'] = self.current_version

        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection

        if self.docker_version is not None:
            result['docker_version'] = self.docker_version

        if self.external_loadbalancer_id is not None:
            result['external_loadbalancer_id'] = self.external_loadbalancer_id

        if self.init_version is not None:
            result['init_version'] = self.init_version

        if self.ip_stack is not None:
            result['ip_stack'] = self.ip_stack

        if self.maintenance_window is not None:
            result['maintenance_window'] = self.maintenance_window.to_map()

        if self.master_url is not None:
            result['master_url'] = self.master_url

        if self.meta_data is not None:
            result['meta_data'] = self.meta_data

        if self.name is not None:
            result['name'] = self.name

        if self.network_mode is not None:
            result['network_mode'] = self.network_mode

        if self.next_version is not None:
            result['next_version'] = self.next_version

        if self.operation_policy is not None:
            result['operation_policy'] = self.operation_policy.to_map()

        if self.private_zone is not None:
            result['private_zone'] = self.private_zone

        if self.profile is not None:
            result['profile'] = self.profile

        if self.proxy_mode is not None:
            result['proxy_mode'] = self.proxy_mode

        if self.region_id is not None:
            result['region_id'] = self.region_id

        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id

        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id

        if self.service_cidr is not None:
            result['service_cidr'] = self.service_cidr

        if self.size is not None:
            result['size'] = self.size

        if self.state is not None:
            result['state'] = self.state

        if self.subnet_cidr is not None:
            result['subnet_cidr'] = self.subnet_cidr

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.updated is not None:
            result['updated'] = self.updated

        if self.vpc_id is not None:
            result['vpc_id'] = self.vpc_id

        if self.vswitch_id is not None:
            result['vswitch_id'] = self.vswitch_id

        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids

        if self.worker_ram_role_name is not None:
            result['worker_ram_role_name'] = self.worker_ram_role_name

        if self.zone_id is not None:
            result['zone_id'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_domain') is not None:
            self.cluster_domain = m.get('cluster_domain')

        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')

        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')

        if m.get('container_cidr') is not None:
            self.container_cidr = m.get('container_cidr')

        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('current_version') is not None:
            self.current_version = m.get('current_version')

        if m.get('deletion_protection') is not None:
            self.deletion_protection = m.get('deletion_protection')

        if m.get('docker_version') is not None:
            self.docker_version = m.get('docker_version')

        if m.get('external_loadbalancer_id') is not None:
            self.external_loadbalancer_id = m.get('external_loadbalancer_id')

        if m.get('init_version') is not None:
            self.init_version = m.get('init_version')

        if m.get('ip_stack') is not None:
            self.ip_stack = m.get('ip_stack')

        if m.get('maintenance_window') is not None:
            temp_model = main_models.MaintenanceWindow()
            self.maintenance_window = temp_model.from_map(m.get('maintenance_window'))

        if m.get('master_url') is not None:
            self.master_url = m.get('master_url')

        if m.get('meta_data') is not None:
            self.meta_data = m.get('meta_data')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('network_mode') is not None:
            self.network_mode = m.get('network_mode')

        if m.get('next_version') is not None:
            self.next_version = m.get('next_version')

        if m.get('operation_policy') is not None:
            temp_model = main_models.DescribeClustersV1ResponseBodyClustersOperationPolicy()
            self.operation_policy = temp_model.from_map(m.get('operation_policy'))

        if m.get('private_zone') is not None:
            self.private_zone = m.get('private_zone')

        if m.get('profile') is not None:
            self.profile = m.get('profile')

        if m.get('proxy_mode') is not None:
            self.proxy_mode = m.get('proxy_mode')

        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')

        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')

        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')

        if m.get('service_cidr') is not None:
            self.service_cidr = m.get('service_cidr')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('subnet_cidr') is not None:
            self.subnet_cidr = m.get('subnet_cidr')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        if m.get('vpc_id') is not None:
            self.vpc_id = m.get('vpc_id')

        if m.get('vswitch_id') is not None:
            self.vswitch_id = m.get('vswitch_id')

        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')

        if m.get('worker_ram_role_name') is not None:
            self.worker_ram_role_name = m.get('worker_ram_role_name')

        if m.get('zone_id') is not None:
            self.zone_id = m.get('zone_id')

        return self

class DescribeClustersV1ResponseBodyClustersOperationPolicy(DaraModel):
    def __init__(
        self,
        cluster_auto_upgrade: main_models.DescribeClustersV1ResponseBodyClustersOperationPolicyClusterAutoUpgrade = None,
    ):
        # The configurations of auto cluster update.
        self.cluster_auto_upgrade = cluster_auto_upgrade

    def validate(self):
        if self.cluster_auto_upgrade:
            self.cluster_auto_upgrade.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_auto_upgrade is not None:
            result['cluster_auto_upgrade'] = self.cluster_auto_upgrade.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_auto_upgrade') is not None:
            temp_model = main_models.DescribeClustersV1ResponseBodyClustersOperationPolicyClusterAutoUpgrade()
            self.cluster_auto_upgrade = temp_model.from_map(m.get('cluster_auto_upgrade'))

        return self

class DescribeClustersV1ResponseBodyClustersOperationPolicyClusterAutoUpgrade(DaraModel):
    def __init__(
        self,
        channel: str = None,
        enabled: bool = None,
    ):
        # The frequency of auto cluster updates. For more information, see [Update frequency](https://help.aliyun.com/document_detail/2712866.html).
        # 
        # Valid values:
        # 
        # *   patch: the latest patch version.
        # *   stables: the second-latest minor version.
        # *   rapid: the latest minor version.
        self.channel = channel
        # Specifies whether to enable auto cluster update.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['channel'] = self.channel

        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

