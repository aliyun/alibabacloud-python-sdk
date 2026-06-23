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
        control_plane_endpoints_config: main_models.DescribeClusterDetailResponseBodyControlPlaneEndpointsConfig = None,
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
        # Intelligent managed mode configuration.
        self.auto_mode = auto_mode
        # Cluster local domain.
        self.cluster_domain = cluster_domain
        # Cluster ID.
        self.cluster_id = cluster_id
        # The cluster specifications when `cluster_type` is set to `ManagedKubernetes` and `profile` is configured. Valid values:
        # 
        # - `ack.standard`: Basic edition (selected by default when the value is empty)
        # - `ack.pro.small`: Pro edition
        # - `ack.pro.xlarge`: Pro XL
        # - `ack.pro.2xlarge`: Pro 2XL
        # - `ack.pro.4xlarge`: Pro 4XL (requires contacting customer service for allowlisting)
        # 
        # Pro XL, Pro 2XL, and Pro 4XL are three tiers provided by <props="china">[ACK Pro Provisioned Control Plane](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane)<props="intl">[ACK Pro Provisioned Control Plane](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane). By pre-allocating and pinning control plane resources, they ensure that API concurrency and Pod scheduling capabilities remain at a consistently high level, suitable for AI training and inference, ultra-large-scale clusters, and mission-critical workloads.
        # 
        # For cluster management fees for Pro edition and Provisioned Control Plane editions, see <props="china">[Cluster management fees](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee)<props="intl">[Cluster management fees](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee).
        self.cluster_spec = cluster_spec
        # Cluster type.
        # 
        # - `Kubernetes`: ACK dedicated cluster.
        #  
        # - `ManagedKubernetes`: ACK managed clusters, including ACK managed clusters (ACK Pro and ACK Basic), ACK Serverless clusters (Pro and Basic), ACK Edge clusters (Pro and Basic), and ACK Lingjun clusters (Pro).
        #  
        # - `ExternalKubernetes`: Registered cluster.
        self.cluster_type = cluster_type
        # Pod network CIDR block, configured for Flannel networking.
        self.container_cidr = container_cidr
        # Dedicated cluster control plane configuration.
        self.control_plane_config = control_plane_config
        # Cluster connection configuration.
        self.control_plane_endpoints_config = control_plane_endpoints_config
        # Cluster creation time.
        self.created = created
        # The current version of the cluster. For Kubernetes versions supported by ACK, see [Kubernetes release overview](https://help.aliyun.com/document_detail/185269.html).
        self.current_version = current_version
        # Cluster deletion protection, which prevents accidental deletion of the cluster through the console or API. Valid values:
        # 
        # - `true`: Enable cluster deletion protection. The cluster cannot be deleted through the console or API.
        # - `false`: Disable cluster deletion protection. The cluster can be deleted through the console or API.
        self.deletion_protection = deletion_protection
        # The Docker version in the cluster.
        self.docker_version = docker_version
        # Cluster Ingress SLB instance ID.
        self.external_loadbalancer_id = external_loadbalancer_id
        # Custom API Server certificate SAN (Subject Alternative Name).
        self.extra_sans = extra_sans
        # Cluster initial version.
        self.init_version = init_version
        # The IP protocol stack of the cluster. Valid values:
        # - ipv4: Creates a cluster that supports only the IPv4 protocol stack.
        # - dual: Creates a cluster that supports the IPv4/IPv6 dual stack.
        self.ip_stack = ip_stack
        # Cluster maintenance window configuration. Only takes effect in managed editions (i.e., ACK Pro clusters).
        self.maintenance_window = maintenance_window
        # The access endpoint of the cluster, including the internal and public access endpoints.
        self.master_url = master_url
        # Cluster metadata information.
        self.meta_data = meta_data
        # Cluster name.
        self.name = name
        # The network type used by the cluster, for example: VPC network.
        self.network_mode = network_mode
        # Cluster upgradeable version.
        self.next_version = next_version
        # Only applicable to the Flannel network plugin.
        # 
        # The subnet mask size allocated to each node, which controls the number of IP addresses that can be allocated to the node.
        self.node_cidr_mask = node_cidr_mask
        # Cluster automatic O&M policy.
        self.operation_policy = operation_policy
        # Cluster ROS parameter collection.
        self.parameters = parameters
        # Whether PrivateZone is enabled for the cluster.
        # 
        # - `true`: Enabled.
        # - `false`: Not enabled.
        # 
        # Default value: false.
        self.private_zone = private_zone
        # Cluster subtype.
        # 
        # - `Default`: ACK managed cluster, including ACK Pro and ACK Basic.
        #  
        # - `Edge`: ACK Edge cluster, including ACK Edge Pro and ACK Edge Basic.
        #  
        # - `Serverless`: ACK Serverless cluster, including ACK Serverless Pro and ACK Serverless Basic.
        #  
        # - `Lingjun`: ACK Lingjun cluster, available in Pro edition.
        self.profile = profile
        # kube-proxy proxy mode.
        # 
        # - `iptables`: A mature and stable kube-proxy proxy mode. Service discovery and load balancing for Kubernetes Services are configured using iptables rules. However, the performance is average and significantly affected by scale. This mode is suitable for clusters with a small number of Services.
        # - `ipvs`: A high-performance kube-proxy proxy mode. Service discovery and load balancing for Kubernetes Services are configured using the Linux IPVS module. This mode is suitable for clusters with a large number of Services and scenarios that require high-performance load balancing.
        self.proxy_mode = proxy_mode
        # The region ID where the cluster is located.
        self.region_id = region_id
        # Cluster resource group ID.
        self.resource_group_id = resource_group_id
        # RRSA configuration.
        self.rrsa_config = rrsa_config
        # Cluster security group ID.
        self.security_group_id = security_group_id
        # Service network CIDR block.
        # 
        # This parameter is required.
        self.service_cidr = service_cidr
        # The number of nodes in the cluster, including both Master and Worker nodes.
        self.size = size
        # Cluster running status. Valid values:
        # 
        # - `initial`: The cluster is being created.
        # - `failed`: The cluster failed to be created.
        # - `running`: The cluster is running.
        # - `updating`: The cluster is being updated.
        # - `upgrading`: The cluster is being upgraded.
        # - `removing`: Nodes are being removed.
        # - `draining`: Nodes are being drained.
        # - `scaling`: The cluster is being scaled.
        # - `inactive`: The cluster is inactive.
        # - `unavailable`: The cluster is unavailable.
        # - `deleting`: The cluster is being deleted.
        # - `deleted`: The cluster has been deleted.
        # - `delete_failed`: The cluster failed to be deleted.
        # - `waiting`: Waiting for connection.
        # - `disconnected`: Disconnected.
        self.state = state
        # Pod network CIDR block.
        self.subnet_cidr = subnet_cidr
        # Cluster resource tags.
        self.tags = tags
        # Timezone.
        self.timezone = timezone
        # Cluster update time.
        self.updated = updated
        # The VPC ID of the cluster. This is a required parameter when creating a cluster.
        self.vpc_id = vpc_id
        # vSwitch ID. This field is deprecated. For control plane vSwitches, use the vswitch_ids field. For data plane vSwitches, query through the vswitch_ids field in node pools.
        self.vswitch_id = vswitch_id
        # Cluster control plane vSwitches.
        self.vswitch_ids = vswitch_ids
        # The name of the Worker RAM role, which authorizes ECS instances as Worker nodes of the cluster.
        self.worker_ram_role_name = worker_ram_role_name
        # The availability zone ID within the region where the cluster is located.
        self.zone_id = zone_id

    def validate(self):
        if self.auto_mode:
            self.auto_mode.validate()
        if self.control_plane_config:
            self.control_plane_config.validate()
        if self.control_plane_endpoints_config:
            self.control_plane_endpoints_config.validate()
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

        if self.control_plane_endpoints_config is not None:
            result['control_plane_endpoints_config'] = self.control_plane_endpoints_config.to_map()

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

        if m.get('control_plane_endpoints_config') is not None:
            temp_model = main_models.DescribeClusterDetailResponseBodyControlPlaneEndpointsConfig()
            self.control_plane_endpoints_config = temp_model.from_map(m.get('control_plane_endpoints_config'))

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
        # The default audience information of the OIDC token. Multiple values are separated by commas (,). The values will be set as an array in the aud field of the OIDC token.
        self.audience = audience
        # Whether RRSA is enabled.
        self.enabled = enabled
        # The issuer information of the OIDC token. Multiple values are separated by commas (,). The first value will be set as the iss field of the OIDC token and the issuer URL of the OIDC identity provider.
        self.issuer = issuer
        # OIDC public key information URL.
        self.jwks_url = jwks_url
        # The maximum configurable validity period of an OIDC token.
        self.max_oidc_token_expiration = max_oidc_token_expiration
        # OIDC identity provider ARN.
        self.oidc_arn = oidc_arn
        # OIDC identity provider name.
        self.oidc_name = oidc_name
        # OIDC configuration document URL.
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
        # Cluster auto-upgrade.
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
        # Cluster auto-upgrade frequency. For more information, see [Upgrade frequency](https://help.aliyun.com/document_detail/2712866.html).
        # 
        # Valid values:
        # - patch: Latest patch version.
        # - stable: Second latest minor version.
        # - rapid: Latest minor version.
        self.channel = channel
        # Whether cluster auto-upgrade is enabled.
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

class DescribeClusterDetailResponseBodyControlPlaneEndpointsConfig(DaraModel):
    def __init__(
        self,
        internal_dns_config: main_models.DescribeClusterDetailResponseBodyControlPlaneEndpointsConfigInternalDnsConfig = None,
    ):
        # Internal DNS configuration for the cluster, applicable to ACK managed clusters. The internal DNS is used by node-side system components such as kubelet and kube-proxy to access the API Server. When internal DNS access is not enabled, node-side system components access the API Server through the CLB IP.
        self.internal_dns_config = internal_dns_config

    def validate(self):
        if self.internal_dns_config:
            self.internal_dns_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internal_dns_config is not None:
            result['internal_dns_config'] = self.internal_dns_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('internal_dns_config') is not None:
            temp_model = main_models.DescribeClusterDetailResponseBodyControlPlaneEndpointsConfigInternalDnsConfig()
            self.internal_dns_config = temp_model.from_map(m.get('internal_dns_config'))

        return self

class DescribeClusterDetailResponseBodyControlPlaneEndpointsConfigInternalDnsConfig(DaraModel):
    def __init__(
        self,
        bind_vpcs: List[str] = None,
        enabled: bool = None,
    ):
        # The VPC scope within which the internal DNS record resolution takes effect. The VPC where the cluster is located is included by default.
        self.bind_vpcs = bind_vpcs
        # Whether to enable internal DNS access for the cluster.
        # - true: Enable internal DNS access. Node-side components (kubelet, kube-proxy) will access the API Server through the internal DNS.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_vpcs is not None:
            result['bind_vpcs'] = self.bind_vpcs

        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bind_vpcs') is not None:
            self.bind_vpcs = m.get('bind_vpcs')

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
        # Whether auto-renewal is enabled for the node.
        self.auto_renew = auto_renew
        # Auto-renewal duration of the node.
        self.auto_renew_period = auto_renew_period
        # Billing type of control plane nodes.
        self.charge_type = charge_type
        # Whether to install CloudMonitor on the node.
        self.cloud_monitor_flags = cloud_monitor_flags
        # Node CPU management policy.
        self.cpu_policy = cpu_policy
        # Deployment set ID.
        self.deploymentset_id = deploymentset_id
        # Image ID.
        self.image_id = image_id
        # OS image type.
        self.image_type = image_type
        # Metadata access configuration for ECS instances.
        self.instance_metadata_options = instance_metadata_options
        # Node instance specification types.
        self.instance_types = instance_types
        # Key pair name. You can specify either this parameter or login_password.
        self.key_pair = key_pair
        # Node service port range.
        self.node_port_range = node_port_range
        # Subscription duration of the node.
        self.period = period
        # Unit of the subscription duration.
        self.period_unit = period_unit
        # Container runtime name.
        self.runtime = runtime
        # Whether to enable Alibaba Cloud OS security hardening.
        self.security_hardening_os = security_hardening_os
        # Number of control plane nodes.
        self.size = size
        # Whether to enable classified protection security hardening.
        self.soc_enabled = soc_enabled
        # Whether burst (performance burst) is enabled for the node system disk.
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # Node system disk type.
        self.system_disk_category = system_disk_category
        # Performance level of the node system disk. Only applicable to ESSD disks.
        self.system_disk_performance_level = system_disk_performance_level
        # Provisioned read/write IOPS for the node system disk.
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # Node system disk size, minimum 40.
        self.system_disk_size = system_disk_size
        # Node automatic snapshot backup policy.
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
        # Whether to enable intelligent managed mode.
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

