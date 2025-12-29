# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterDetailResponseBody(DaraModel):
    def __init__(
        self,
        auto_mode: main_models.DescribeClusterDetailResponseBodyAutoMode = None,
        cluster_domain: str = None,
        cluster_id: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        container_cidr: str = None,
        control_plane_config: main_models.DescribeClusterDetailResponseBodyControlPlaneConfig = None,
        created: str = None,
        current_version: str = None,
        deletion_protection: bool = None,
        docker_version: str = None,
        external_loadbalancer_id: str = None,
        extra_sans: List[str] = None,
        init_version: str = None,
        ip_stack: str = None,
        maintenance_window: main_models.MaintenanceWindow = None,
        master_url: str = None,
        meta_data: str = None,
        name: str = None,
        network_mode: str = None,
        next_version: str = None,
        node_cidr_mask: str = None,
        operation_policy: main_models.DescribeClusterDetailResponseBodyOperationPolicy = None,
        parameters: Dict[str, str] = None,
        private_zone: bool = None,
        profile: str = None,
        proxy_mode: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        rrsa_config: main_models.DescribeClusterDetailResponseBodyRrsaConfig = None,
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
        self.auto_mode = auto_mode
        # The domain name of the cluster.
        self.cluster_domain = cluster_domain
        # The cluster ID.
        self.cluster_id = cluster_id
        # The edition of the cluster
        # 
        # *   `ack.pro.small`: the Pro edition.
        # *   `ack.standard`: the Basic edition.
        self.cluster_spec = cluster_spec
        # The type of the instance.
        # 
        # *   `Kubernetes`: ACK dedicated cluster.
        # *   `ManagedKubernetes`: ACK managed cluster. ACK managed clusters include ACK managed Basic clusters, ACK managed Pro clusters, ACK Serverless Pro clusters, ACK Serverless Basic clusters, ACK Edge Pro clusters, ACK Edge Basic clusters, and ACK Lingjun Pro clusters.
        # *   `ExternalKubernetes`: registered cluster.
        self.cluster_type = cluster_type
        # The pod CIDR block. The configuration of the Flannel network plug-in.
        self.container_cidr = container_cidr
        # The control plane configurations in an ACK dedicated cluster.
        self.control_plane_config = control_plane_config
        # The time when the cluster was created.
        self.created = created
        # The Kubernetes version of the cluster. For more information about the Kubernetes versions supported by ACK, see [Release notes for Kubernetes versions](https://help.aliyun.com/document_detail/185269.html).
        self.current_version = current_version
        # Indicates whether deletion protection is enabled for the cluster. If deletion protection is enabled, the cluster cannot be deleted in the Container Service console or by calling API operations. Valid values:
        # 
        # *   `true`: deletion protection is enabled for the cluster. This way, the cluster cannot be deleted in the Container Service console or by calling API operations.
        # *   `false`: deletion protection is disabled for the cluster. This way, the cluster can be deleted in the Container Service console or by calling API operations.
        self.deletion_protection = deletion_protection
        # The Docker version that is used by the cluster.
        self.docker_version = docker_version
        # The ID of the Server Load Balancer (SLB) instance that is created for the Ingress of the cluster.
        self.external_loadbalancer_id = external_loadbalancer_id
        self.extra_sans = extra_sans
        # The initial Kubernetes version of the cluster.
        self.init_version = init_version
        # The IP stack of the cluster. Valid values:
        # 
        # *   ipv4: The cluster is an IPv4 cluster.
        # *   dual: The cluster is an IPv4/IPv6 dual-stack cluster.
        self.ip_stack = ip_stack
        # The maintenance window of the cluster. This feature is available only in ACK Pro clusters.
        self.maintenance_window = maintenance_window
        # The endpoints of the cluster, including an internal endpoint and a public endpoint.
        self.master_url = master_url
        # The metadata of the cluster.
        self.meta_data = meta_data
        # The cluster name.
        self.name = name
        # The network type of the cluster. Example: Virtual Private Cloud (VPC).
        self.network_mode = network_mode
        # The Kubernetes version to which the cluster can be upgraded.
        self.next_version = next_version
        # This parameter is available only for Flannel.
        # 
        # The subnet mask length of the node CIDR block. This parameter indicates the maximum number of IP addresses that can be assigned to nodes.
        self.node_cidr_mask = node_cidr_mask
        # The automatic O\\&M policy of the cluster.
        self.operation_policy = operation_policy
        # The Resource Orchestration Service (ROS) parameters of the cluster.
        self.parameters = parameters
        # Indicates whether Alibaba Cloud DNS PrivateZone (PrivateZone) is enabled for the cluster. Valid values:
        # 
        # *   `true`: PrivateZone is enabled.
        # *   `false`: PrivateZone is dislabled.
        # 
        # Default value: false
        self.private_zone = private_zone
        # The subtype of the cluster.
        # 
        # *   `Default`. ACK managed cluster. ACK managed clusters include ACK Basic clusters and ACK Pro clusters.
        # *   `Edge`: ACK Edge cluster. ACK Edge clusters include ACK Edge Basic clusters and ACK Edge Pro clusters.
        # *   `Serverless`: ACK Serverless cluster. ACK Serverless clusters include ACK Serverless Basic clusters and ACK Serverless Pro clusters.
        # *   `Lingjun`: ACK Lingjun Pro cluster.
        self.profile = profile
        # The kube-proxy mode. Valid values:
        # 
        # *   `iptables`: a mature and stable kube-proxy mode that uses iptables rules to conduct Service discovery and load balancing. The performance of this mode is limited by the size of the cluster. This mode is suitable for clusters that run a small number of Services.
        # *   `ipvs`: provides high performance and uses IP Virtual Server (IPVS). This allows you to configure service discovery and load balancing. This mode is suitable for clusters that are required to run a large number of services. We recommend that you use this mode in scenarios that require high load balancing performance.
        self.proxy_mode = proxy_mode
        # The region ID of the cluster.
        self.region_id = region_id
        # The ID of the resource group to which the cluster belongs.
        self.resource_group_id = resource_group_id
        self.rrsa_config = rrsa_config
        # The ID of the security group to which the cluster belongs.
        self.security_group_id = security_group_id
        # The Service CIDR block.
        # 
        # This parameter is required.
        self.service_cidr = service_cidr
        # The number of nodes in the cluster. Master nodes and worker nodes are included.
        self.size = size
        # The status of the cluster. Valid values:
        # 
        # *   `initial`: The cluster is being created.
        # *   `failed`: The cluster failed to be created.
        # *   `running`: The cluster is running.
        # *   `updating`: The cluster is being updated.
        # *   `updating_failed`: The cluster failed to be updated.
        # *   `scaling`: The cluster is being scaled.
        # *   `waiting`: The cluster is waiting for connection requests.
        # *   `disconnected`: The cluster is disconnected.
        # *   `stopped`: The cluster is stopped.
        # *   `deleting`: The cluster is being deleted.
        # *   `deleted`: The cluster is deleted.
        # *   `delete_failed`: The cluster failed to be deleted.
        self.state = state
        # The pod CIDR block.
        self.subnet_cidr = subnet_cidr
        # The resource labels of the cluster.
        self.tags = tags
        # The time zone
        self.timezone = timezone
        # The time when the cluster was updated.
        self.updated = updated
        # The ID of the VPC where the cluster is deployed. This parameter is required when you create a cluster.
        self.vpc_id = vpc_id
        # The ID of the vSwitche. This field is deprecated. Use vswitch_ids to query the vSwitches on the control plane and vswitch_ids to query the vSwitches on the data plane.
        self.vswitch_id = vswitch_id
        # The vSwitch for the control plane of the cluster.
        self.vswitch_ids = vswitch_ids
        # The name of the worker Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes of the cluster to allow the worker nodes to manage Elastic Compute Service (ECS) instances.
        self.worker_ram_role_name = worker_ram_role_name
        # The ID of the zone within the region where the cluster is located.
        self.zone_id = zone_id

    def validate(self):
        if self.auto_mode:
            self.auto_mode.validate()
        if self.control_plane_config:
            self.control_plane_config.validate()
        if self.maintenance_window:
            self.maintenance_window.validate()
        if self.operation_policy:
            self.operation_policy.validate()
        if self.rrsa_config:
            self.rrsa_config.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_mode is not None:
            result['auto_mode'] = self.auto_mode.to_map()

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

        if self.control_plane_config is not None:
            result['control_plane_config'] = self.control_plane_config.to_map()

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

        if self.extra_sans is not None:
            result['extra_sans'] = self.extra_sans

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

        if self.node_cidr_mask is not None:
            result['node_cidr_mask'] = self.node_cidr_mask

        if self.operation_policy is not None:
            result['operation_policy'] = self.operation_policy.to_map()

        if self.parameters is not None:
            result['parameters'] = self.parameters

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

        if self.rrsa_config is not None:
            result['rrsa_config'] = self.rrsa_config.to_map()

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
        if m.get('auto_mode') is not None:
            temp_model = main_models.DescribeClusterDetailResponseBodyAutoMode()
            self.auto_mode = temp_model.from_map(m.get('auto_mode'))

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

        if m.get('control_plane_config') is not None:
            temp_model = main_models.DescribeClusterDetailResponseBodyControlPlaneConfig()
            self.control_plane_config = temp_model.from_map(m.get('control_plane_config'))

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

        if m.get('extra_sans') is not None:
            self.extra_sans = m.get('extra_sans')

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

        if m.get('node_cidr_mask') is not None:
            self.node_cidr_mask = m.get('node_cidr_mask')

        if m.get('operation_policy') is not None:
            temp_model = main_models.DescribeClusterDetailResponseBodyOperationPolicy()
            self.operation_policy = temp_model.from_map(m.get('operation_policy'))

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

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

        if m.get('rrsa_config') is not None:
            temp_model = main_models.DescribeClusterDetailResponseBodyRrsaConfig()
            self.rrsa_config = temp_model.from_map(m.get('rrsa_config'))

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

class DescribeClusterDetailResponseBodyRrsaConfig(DaraModel):
    def __init__(
        self,
        audience: str = None,
        enabled: bool = None,
        issuer: str = None,
        jwks_url: str = None,
        max_oidc_token_expiration: str = None,
        oidc_arn: str = None,
        oidc_name: str = None,
        open_api_configuration_url: str = None,
    ):
        self.audience = audience
        self.enabled = enabled
        self.issuer = issuer
        self.jwks_url = jwks_url
        self.max_oidc_token_expiration = max_oidc_token_expiration
        self.oidc_arn = oidc_arn
        self.oidc_name = oidc_name
        self.open_api_configuration_url = open_api_configuration_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audience is not None:
            result['audience'] = self.audience

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.issuer is not None:
            result['issuer'] = self.issuer

        if self.jwks_url is not None:
            result['jwks_url'] = self.jwks_url

        if self.max_oidc_token_expiration is not None:
            result['max_oidc_token_expiration'] = self.max_oidc_token_expiration

        if self.oidc_arn is not None:
            result['oidc_arn'] = self.oidc_arn

        if self.oidc_name is not None:
            result['oidc_name'] = self.oidc_name

        if self.open_api_configuration_url is not None:
            result['open_api_configuration_url'] = self.open_api_configuration_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audience') is not None:
            self.audience = m.get('audience')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('issuer') is not None:
            self.issuer = m.get('issuer')

        if m.get('jwks_url') is not None:
            self.jwks_url = m.get('jwks_url')

        if m.get('max_oidc_token_expiration') is not None:
            self.max_oidc_token_expiration = m.get('max_oidc_token_expiration')

        if m.get('oidc_arn') is not None:
            self.oidc_arn = m.get('oidc_arn')

        if m.get('oidc_name') is not None:
            self.oidc_name = m.get('oidc_name')

        if m.get('open_api_configuration_url') is not None:
            self.open_api_configuration_url = m.get('open_api_configuration_url')

        return self

class DescribeClusterDetailResponseBodyOperationPolicy(DaraModel):
    def __init__(
        self,
        cluster_auto_upgrade: main_models.DescribeClusterDetailResponseBodyOperationPolicyClusterAutoUpgrade = None,
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
            temp_model = main_models.DescribeClusterDetailResponseBodyOperationPolicyClusterAutoUpgrade()
            self.cluster_auto_upgrade = temp_model.from_map(m.get('cluster_auto_upgrade'))

        return self

class DescribeClusterDetailResponseBodyOperationPolicyClusterAutoUpgrade(DaraModel):
    def __init__(
        self,
        channel: str = None,
        enabled: bool = None,
    ):
        # The frequency of auto cluster updates. For more information, see [Update frequency](https://help.aliyun.com/document_detail/2712866.html).
        # 
        # Valid values:
        # 
        # *   patch: specifies the latest patch version.
        # *   stable: specifies the second-latest minor version.
        # *   rapid: specifies the latest minor version.
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

class DescribeClusterDetailResponseBodyControlPlaneConfig(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        charge_type: str = None,
        cloud_monitor_flags: bool = None,
        cpu_policy: str = None,
        deploymentset_id: str = None,
        image_id: str = None,
        image_type: str = None,
        instance_metadata_options: main_models.InstanceMetadataOptions = None,
        instance_types: List[str] = None,
        key_pair: str = None,
        node_port_range: str = None,
        period: int = None,
        period_unit: str = None,
        runtime: str = None,
        security_hardening_os: bool = None,
        size: int = None,
        soc_enabled: bool = None,
        system_disk_bursting_enabled: bool = None,
        system_disk_category: str = None,
        system_disk_performance_level: str = None,
        system_disk_provisioned_iops: int = None,
        system_disk_size: int = None,
        system_disk_snapshot_policy_id: str = None,
    ):
        # Indicates whether auto-renewal is enabled for the nodes.
        self.auto_renew = auto_renew
        # The auto-renewal duration for the nodes.
        self.auto_renew_period = auto_renew_period
        # The billing method of the control plane node.
        self.charge_type = charge_type
        # Indicates whether to install CloudMonitor for the node.
        self.cloud_monitor_flags = cloud_monitor_flags
        # The CPU management policy of nodes.
        self.cpu_policy = cpu_policy
        # The ID of the deployment set.
        self.deploymentset_id = deploymentset_id
        # The image ID.
        self.image_id = image_id
        # The type of the OS image.
        self.image_type = image_type
        self.instance_metadata_options = instance_metadata_options
        # The instance types of the nodes.
        self.instance_types = instance_types
        # The name of the key pair. You must set key_pair or login_password.
        self.key_pair = key_pair
        # The node port range.
        self.node_port_range = node_port_range
        # The subscription duration of nodes in the node pool.
        self.period = period
        # The unit of the subscription duration.
        self.period_unit = period_unit
        # The runtime.
        self.runtime = runtime
        # Indicates whether to enable Alibaba Cloud Linux Security Hardening.
        self.security_hardening_os = security_hardening_os
        # The number of control plane nodes.
        self.size = size
        # Indicates whether to enable Multi-Level Protection Scheme (MLPS) security hardening.
        self.soc_enabled = soc_enabled
        # Indicates whether to enable the burst feature for the system disk.
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The category of the system disk for nodes.
        self.system_disk_category = system_disk_category
        # The performance level (PL) of the system disk that you want to use for the node. This parameter takes effect only for ESSDs.
        self.system_disk_performance_level = system_disk_performance_level
        # The preset read/write IOPS of the system disk.
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The system disk size of the node. The value must be at least 40 GB.
        self.system_disk_size = system_disk_size
        # The automatic snapshot policy of the node.
        self.system_disk_snapshot_policy_id = system_disk_snapshot_policy_id

    def validate(self):
        if self.instance_metadata_options:
            self.instance_metadata_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['auto_renew_period'] = self.auto_renew_period

        if self.charge_type is not None:
            result['charge_type'] = self.charge_type

        if self.cloud_monitor_flags is not None:
            result['cloud_monitor_flags'] = self.cloud_monitor_flags

        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy

        if self.deploymentset_id is not None:
            result['deploymentset_id'] = self.deploymentset_id

        if self.image_id is not None:
            result['image_id'] = self.image_id

        if self.image_type is not None:
            result['image_type'] = self.image_type

        if self.instance_metadata_options is not None:
            result['instance_metadata_options'] = self.instance_metadata_options.to_map()

        if self.instance_types is not None:
            result['instance_types'] = self.instance_types

        if self.key_pair is not None:
            result['key_pair'] = self.key_pair

        if self.node_port_range is not None:
            result['node_port_range'] = self.node_port_range

        if self.period is not None:
            result['period'] = self.period

        if self.period_unit is not None:
            result['period_unit'] = self.period_unit

        if self.runtime is not None:
            result['runtime'] = self.runtime

        if self.security_hardening_os is not None:
            result['security_hardening_os'] = self.security_hardening_os

        if self.size is not None:
            result['size'] = self.size

        if self.soc_enabled is not None:
            result['soc_enabled'] = self.soc_enabled

        if self.system_disk_bursting_enabled is not None:
            result['system_disk_bursting_enabled'] = self.system_disk_bursting_enabled

        if self.system_disk_category is not None:
            result['system_disk_category'] = self.system_disk_category

        if self.system_disk_performance_level is not None:
            result['system_disk_performance_level'] = self.system_disk_performance_level

        if self.system_disk_provisioned_iops is not None:
            result['system_disk_provisioned_iops'] = self.system_disk_provisioned_iops

        if self.system_disk_size is not None:
            result['system_disk_size'] = self.system_disk_size

        if self.system_disk_snapshot_policy_id is not None:
            result['system_disk_snapshot_policy_id'] = self.system_disk_snapshot_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_renew') is not None:
            self.auto_renew = m.get('auto_renew')

        if m.get('auto_renew_period') is not None:
            self.auto_renew_period = m.get('auto_renew_period')

        if m.get('charge_type') is not None:
            self.charge_type = m.get('charge_type')

        if m.get('cloud_monitor_flags') is not None:
            self.cloud_monitor_flags = m.get('cloud_monitor_flags')

        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')

        if m.get('deploymentset_id') is not None:
            self.deploymentset_id = m.get('deploymentset_id')

        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')

        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')

        if m.get('instance_metadata_options') is not None:
            temp_model = main_models.InstanceMetadataOptions()
            self.instance_metadata_options = temp_model.from_map(m.get('instance_metadata_options'))

        if m.get('instance_types') is not None:
            self.instance_types = m.get('instance_types')

        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')

        if m.get('node_port_range') is not None:
            self.node_port_range = m.get('node_port_range')

        if m.get('period') is not None:
            self.period = m.get('period')

        if m.get('period_unit') is not None:
            self.period_unit = m.get('period_unit')

        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')

        if m.get('security_hardening_os') is not None:
            self.security_hardening_os = m.get('security_hardening_os')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('soc_enabled') is not None:
            self.soc_enabled = m.get('soc_enabled')

        if m.get('system_disk_bursting_enabled') is not None:
            self.system_disk_bursting_enabled = m.get('system_disk_bursting_enabled')

        if m.get('system_disk_category') is not None:
            self.system_disk_category = m.get('system_disk_category')

        if m.get('system_disk_performance_level') is not None:
            self.system_disk_performance_level = m.get('system_disk_performance_level')

        if m.get('system_disk_provisioned_iops') is not None:
            self.system_disk_provisioned_iops = m.get('system_disk_provisioned_iops')

        if m.get('system_disk_size') is not None:
            self.system_disk_size = m.get('system_disk_size')

        if m.get('system_disk_snapshot_policy_id') is not None:
            self.system_disk_snapshot_policy_id = m.get('system_disk_snapshot_policy_id')

        return self

class DescribeClusterDetailResponseBodyAutoMode(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        return self

