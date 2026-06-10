# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ModifyClusterRequest(DaraModel):
    def __init__(
        self,
        access_control_list: List[str] = None,
        api_server_custom_cert_sans: main_models.ModifyClusterRequestApiServerCustomCertSans = None,
        api_server_eip: bool = None,
        api_server_eip_id: str = None,
        cluster_name: str = None,
        cluster_spec: str = None,
        control_plane_config: main_models.ModifyClusterRequestControlPlaneConfig = None,
        control_plane_endpoints_config: main_models.ModifyClusterRequestControlPlaneEndpointsConfig = None,
        deletion_protection: bool = None,
        enable_rrsa: bool = None,
        ingress_domain_rebinding: bool = None,
        ingress_loadbalancer_id: str = None,
        instance_deletion_protection: bool = None,
        maintenance_window: main_models.MaintenanceWindow = None,
        operation_policy: main_models.ModifyClusterRequestOperationPolicy = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        system_events_logging: main_models.ModifyClusterRequestSystemEventsLogging = None,
        timezone: str = None,
        vswitch_ids: List[str] = None,
    ):
        # The access control list for the API server SLB of registered clusters.
        self.access_control_list = access_control_list
        # This parameter adds custom IP addresses or domain names to the SAN field of the API server certificate to control client access.
        # 
        # Only managed clusters support this parameter.
        self.api_server_custom_cert_sans = api_server_custom_cert_sans
        # Specifies whether to bind an EIP to the cluster for public network access to the API server. Valid values:
        # 
        # - `true`: Binds an EIP to the cluster.
        # 
        # - `false`: Does not bind an EIP to the cluster.
        self.api_server_eip = api_server_eip
        # The EIP instance ID bound to the cluster API server. This parameter takes effect only when `api_server_eip` is set to `true`.
        self.api_server_eip_id = api_server_eip_id
        # The custom cluster name. The name can contain digits, letters, Chinese characters, and hyphens (-). It must be 1 to 63 characters in length and cannot start with a hyphen (-).
        self.cluster_name = cluster_name
        # The cluster specification when you set `cluster_type` to `ManagedKubernetes` and configure `profile`. Valid values:
        # 
        # - `ack.pro.small`: Pro
        # 
        # - `ack.pro.xlarge`: Pro XL
        # 
        # - `ack.pro.2xlarge`: Pro 2XL
        # 
        # - `ack.pro.4xlarge`: Pro 4XL (requires approval from customer service to enable)
        # 
        # Pro XL, Pro 2XL, and Pro 4XL are three tiers provided by <props="china">[ACK Pro provisioned control plane](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane)<props="intl">[ACK Pro provisioned control plane](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane). These tiers pre-allocate and dedicate control plane resources to ensure consistent high performance for API concurrency and pod scheduling. They are suitable for AI training and inference, ultra-large-scale clusters, and mission-critical workloads.
        # 
        # For cluster management fees for Pro and provisioned control plane clusters, see <props="china">[Cluster management fees](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee)<props="intl">[Cluster management fees](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee).
        self.cluster_spec = cluster_spec
        # Control plane configuration for dedicated clusters.
        self.control_plane_config = control_plane_config
        # Cluster connection configuration.
        self.control_plane_endpoints_config = control_plane_endpoints_config
        # Enables or disables cluster deletion protection to prevent accidental cluster deletion from the console or using APIs. Valid values:
        # 
        # - `true`: Enables cluster deletion protection. You cannot delete the cluster from the console or using APIs.
        # 
        # - `false`: Disables cluster deletion protection. You can delete the cluster from the console or using APIs.
        # 
        # Default value: `false`.
        self.deletion_protection = deletion_protection
        # Enables or disables the RRSA feature. Only managed clusters support this parameter. Valid values:
        # 
        # - `true`: Enables RRSA.
        # 
        # - `false`: Disables RRSA.
        self.enable_rrsa = enable_rrsa
        # Specifies whether to rebind the cluster test domain name. Valid values:
        # 
        # - `true`: Rebinds the cluster test domain name.
        # 
        # - `false`: Does not rebind the cluster test domain name.
        # 
        # Default value: `false`.
        self.ingress_domain_rebinding = ingress_domain_rebinding
        # The SLB instance ID of the cluster to be modified.
        self.ingress_loadbalancer_id = ingress_loadbalancer_id
        # Enables or disables instance deletion protection to prevent accidental release of nodes from the console or using APIs. Valid values:
        # 
        # - `true`: Prevents accidental node deletion from the console or using APIs.
        # 
        # - `false`: Allows accidental node deletion from the console or using APIs.
        # 
        # Default value: `false`.
        self.instance_deletion_protection = instance_deletion_protection
        # The maintenance window of the cluster. This feature is available only for ACK managed clusters Pro.
        self.maintenance_window = maintenance_window
        # Automatic O\\&M policy for the cluster.
        self.operation_policy = operation_policy
        # The resource group ID of the cluster.
        self.resource_group_id = resource_group_id
        # The security group ID for the control plane.
        # 
        # - If you configure blocking rules in the security group, ensure that the security group rules allow the protocols and ports required by the cluster. For recommended security group rules, see [Configure and manage cluster security groups](https://help.aliyun.com/document_detail/353191.html).
        # 
        # - For non-dedicated ACK clusters, the control plane and installed managed components (such as terway-controlplane) restart briefly during the update. Perform this operation during off-peak hours. After you change the control plane security group, the ENIs used by the control plane and managed components are automatically added to the new security group.
        # 
        # - For ACK dedicated clusters, newly scaled-out master nodes automatically apply the new control plane security group. Existing control plane nodes are unaffected.
        self.security_group_id = security_group_id
        # System event logging configuration.
        self.system_events_logging = system_events_logging
        # The cluster time zone. For more information, see [Supported time zones](https://help.aliyun.com/document_detail/354879.html).
        # 
        # - After you change the time zone, cluster inspection configurations use the new time zone.
        # 
        # - For managed clusters, the control plane and installed managed components (such as terway-controlplane) restart briefly during the update. Perform this operation during off-peak hours. Newly scaled-out nodes automatically apply the new time zone. Existing nodes are unaffected. You can reset nodes in node pools to apply the new time zone to existing nodes.
        # 
        # - For dedicated clusters, newly scaled-out nodes (including control plane nodes) automatically apply the new time zone. Existing nodes (including control plane nodes) are unaffected. You can reset nodes in node pools to apply the new time zone to existing nodes. For control plane nodes, scale out and then scale in to apply the new time zone to all control plane nodes.
        self.timezone = timezone
        # The vSwitches for the cluster control plane. For dedicated clusters, the change applies only to newly scaled-out control plane nodes. When you change the control plane vSwitches for managed clusters, note the following:
        # 
        # - This parameter performs an overwrite update. You must specify the complete target vSwitch list.
        # 
        # - Control plane components restart briefly during the update. Proceed with caution.
        # 
        # - Ensure that all security groups (including those for the control plane, all node pools, and container networking) allow inbound and outbound traffic for the IP CIDR blocks of the new vSwitches. Otherwise, nodes and containers cannot connect to the API server.
        # 
        # - If the new control plane vSwitches have ACL rules configured, ensure that these rules allow communication between the vSwitches and the IP CIDR blocks of cluster nodes and container networks.
        self.vswitch_ids = vswitch_ids

    def validate(self):
        if self.api_server_custom_cert_sans:
            self.api_server_custom_cert_sans.validate()
        if self.control_plane_config:
            self.control_plane_config.validate()
        if self.control_plane_endpoints_config:
            self.control_plane_endpoints_config.validate()
        if self.maintenance_window:
            self.maintenance_window.validate()
        if self.operation_policy:
            self.operation_policy.validate()
        if self.system_events_logging:
            self.system_events_logging.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_control_list is not None:
            result['access_control_list'] = self.access_control_list

        if self.api_server_custom_cert_sans is not None:
            result['api_server_custom_cert_sans'] = self.api_server_custom_cert_sans.to_map()

        if self.api_server_eip is not None:
            result['api_server_eip'] = self.api_server_eip

        if self.api_server_eip_id is not None:
            result['api_server_eip_id'] = self.api_server_eip_id

        if self.cluster_name is not None:
            result['cluster_name'] = self.cluster_name

        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec

        if self.control_plane_config is not None:
            result['control_plane_config'] = self.control_plane_config.to_map()

        if self.control_plane_endpoints_config is not None:
            result['control_plane_endpoints_config'] = self.control_plane_endpoints_config.to_map()

        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection

        if self.enable_rrsa is not None:
            result['enable_rrsa'] = self.enable_rrsa

        if self.ingress_domain_rebinding is not None:
            result['ingress_domain_rebinding'] = self.ingress_domain_rebinding

        if self.ingress_loadbalancer_id is not None:
            result['ingress_loadbalancer_id'] = self.ingress_loadbalancer_id

        if self.instance_deletion_protection is not None:
            result['instance_deletion_protection'] = self.instance_deletion_protection

        if self.maintenance_window is not None:
            result['maintenance_window'] = self.maintenance_window.to_map()

        if self.operation_policy is not None:
            result['operation_policy'] = self.operation_policy.to_map()

        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id

        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id

        if self.system_events_logging is not None:
            result['system_events_logging'] = self.system_events_logging.to_map()

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_control_list') is not None:
            self.access_control_list = m.get('access_control_list')

        if m.get('api_server_custom_cert_sans') is not None:
            temp_model = main_models.ModifyClusterRequestApiServerCustomCertSans()
            self.api_server_custom_cert_sans = temp_model.from_map(m.get('api_server_custom_cert_sans'))

        if m.get('api_server_eip') is not None:
            self.api_server_eip = m.get('api_server_eip')

        if m.get('api_server_eip_id') is not None:
            self.api_server_eip_id = m.get('api_server_eip_id')

        if m.get('cluster_name') is not None:
            self.cluster_name = m.get('cluster_name')

        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')

        if m.get('control_plane_config') is not None:
            temp_model = main_models.ModifyClusterRequestControlPlaneConfig()
            self.control_plane_config = temp_model.from_map(m.get('control_plane_config'))

        if m.get('control_plane_endpoints_config') is not None:
            temp_model = main_models.ModifyClusterRequestControlPlaneEndpointsConfig()
            self.control_plane_endpoints_config = temp_model.from_map(m.get('control_plane_endpoints_config'))

        if m.get('deletion_protection') is not None:
            self.deletion_protection = m.get('deletion_protection')

        if m.get('enable_rrsa') is not None:
            self.enable_rrsa = m.get('enable_rrsa')

        if m.get('ingress_domain_rebinding') is not None:
            self.ingress_domain_rebinding = m.get('ingress_domain_rebinding')

        if m.get('ingress_loadbalancer_id') is not None:
            self.ingress_loadbalancer_id = m.get('ingress_loadbalancer_id')

        if m.get('instance_deletion_protection') is not None:
            self.instance_deletion_protection = m.get('instance_deletion_protection')

        if m.get('maintenance_window') is not None:
            temp_model = main_models.MaintenanceWindow()
            self.maintenance_window = temp_model.from_map(m.get('maintenance_window'))

        if m.get('operation_policy') is not None:
            temp_model = main_models.ModifyClusterRequestOperationPolicy()
            self.operation_policy = temp_model.from_map(m.get('operation_policy'))

        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')

        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')

        if m.get('system_events_logging') is not None:
            temp_model = main_models.ModifyClusterRequestSystemEventsLogging()
            self.system_events_logging = temp_model.from_map(m.get('system_events_logging'))

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')

        return self

class ModifyClusterRequestSystemEventsLogging(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        logging_project: str = None,
    ):
        # Specifies whether to enable system event logging.
        # 
        # - true: Enables system event logging.
        # 
        # - false: Disables system event logging.
        self.enabled = enabled
        # The LogProject name for system event logging.
        self.logging_project = logging_project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.logging_project is not None:
            result['logging_project'] = self.logging_project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('logging_project') is not None:
            self.logging_project = m.get('logging_project')

        return self

class ModifyClusterRequestOperationPolicy(DaraModel):
    def __init__(
        self,
        cluster_auto_upgrade: main_models.ModifyClusterRequestOperationPolicyClusterAutoUpgrade = None,
    ):
        # Automatic cluster upgrade.
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
            temp_model = main_models.ModifyClusterRequestOperationPolicyClusterAutoUpgrade()
            self.cluster_auto_upgrade = temp_model.from_map(m.get('cluster_auto_upgrade'))

        return self

class ModifyClusterRequestOperationPolicyClusterAutoUpgrade(DaraModel):
    def __init__(
        self,
        channel: str = None,
        enabled: bool = None,
    ):
        # The frequency of automatic cluster upgrades. For more information, see [Upgrade frequency](https://help.aliyun.com/document_detail/2712866.html).
        # 
        # Valid values:
        # 
        # - patch: Latest patch version.
        # 
        # - stable: Second latest minor version.
        # 
        # - rapid: Latest minor version.
        self.channel = channel
        # Specifies whether to enable automatic cluster upgrades.
        # 
        # - true: Enables automatic upgrades.
        # 
        # - false: Disables automatic upgrades.
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

class ModifyClusterRequestControlPlaneEndpointsConfig(DaraModel):
    def __init__(
        self,
        internal_dns_config: main_models.ModifyClusterRequestControlPlaneEndpointsConfigInternalDnsConfig = None,
    ):
        # Internal domain name configuration for the cluster. This feature is available for ACK managed clusters. Cluster internal domain names allow node-side system components such as kubelet and kube-proxy to access the API server. If this feature is disabled, node-side system components access the API server through the CLB IP address.
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
            temp_model = main_models.ModifyClusterRequestControlPlaneEndpointsConfigInternalDnsConfig()
            self.internal_dns_config = temp_model.from_map(m.get('internal_dns_config'))

        return self

class ModifyClusterRequestControlPlaneEndpointsConfigInternalDnsConfig(DaraModel):
    def __init__(
        self,
        bind_vpcs: List[str] = None,
        enabled: bool = None,
    ):
        # The VPCs where cluster internal domain name resolution takes effect.
        self.bind_vpcs = bind_vpcs
        # Specifies whether to enable cluster internal domain name access. Valid values:
        # 
        # - true: Enables cluster internal domain name access. Node-side components (kubelet, kube-proxy) access the API server through the cluster internal domain name.
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

class ModifyClusterRequestControlPlaneConfig(DaraModel):
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
        instance_types: List[str] = None,
        key_pair: str = None,
        login_password: str = None,
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
        # Specifies whether to enable auto-renewal for control plane node instances. This parameter takes effect only when `charge_type` is set to `PrePaid`. Valid values:
        # 
        # - `true`: Enables auto-renewal.
        # 
        # - `false`: Disables auto-renewal.
        # 
        # Default value: `false`.
        self.auto_renew = auto_renew
        # The auto-renewal duration for each renewal of control plane node instances.
        # 
        # Valid values: {1, 2, 3, 6, 12}. Unit: months.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # The billing method for control plane node instances. Valid values:
        # 
        # - `PrePaid`: Subscription.
        # 
        # - `PostPaid`: Pay-as-you-go.
        # 
        # Default value: `PostPaid`.
        self.charge_type = charge_type
        # Specifies whether to install the CloudMonitor agent on control plane nodes. Valid values:
        # 
        # - `true`: Installs the CloudMonitor agent.
        # 
        # - `false`: Does not install the CloudMonitor agent.
        self.cloud_monitor_flags = cloud_monitor_flags
        # The CPU management policy for nodes. Clusters of version 1.12.6 or later support the following policies:
        # 
        # - `static`: Enhances CPU affinity and exclusivity for pods with specific resource characteristics on nodes.
        # 
        # - `none`: Uses the default CPU affinity scheme.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # The deployment set ID.
        self.deploymentset_id = deploymentset_id
        # The custom image ID. Specify this parameter when you use a custom image.
        self.image_id = image_id
        # The operating system image type. Valid values:
        # 
        # - `AliyunLinux3`: Alinux3 image.
        # 
        # - `Custom`: Custom image.
        self.image_type = image_type
        # The instance types. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.instance_types = instance_types
        # The key pair name. Specify either this parameter or `login_password`.
        self.key_pair = key_pair
        # The SSH logon password. Specify either this parameter or `key_pair`. The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. To use password-based logon, specify this parameter during scale-out.
        self.login_password = login_password
        # Valid port range: [30000,65535].
        # 
        # Default value: 30000-32767.
        self.node_port_range = node_port_range
        # The subscription duration for control plane node instances. This parameter is required and takes effect only when `charge_type` is set to `PrePaid`.
        # 
        # When `period_unit=Month`, valid values are {1, 2, 3, 6, 12, 24, 36, 48, 60}.
        self.period = period
        # The billing cycle for control plane node instances. This parameter takes effect only when `charge_type` is set to `PrePaid`.
        # 
        # `Month`: Billing by month. Only monthly billing is supported.
        self.period_unit = period_unit
        # The container runtime. Valid values:
        # 
        # - `containerd`: Recommended. Supported by all cluster versions.
        # 
        # Default value: containerd.
        self.runtime = runtime
        # Alibaba Cloud OS security hardening. Valid values:
        # 
        # - `true`: Enables Alibaba Cloud OS security hardening.
        # 
        # - `false`: Disables Alibaba Cloud OS security hardening.
        # 
        # Default value: `false`.
        self.security_hardening_os = security_hardening_os
        # The number of control plane nodes. To scale out the control plane of a dedicated cluster, set this parameter to the target number of control plane nodes, which must be greater than the current number.
        self.size = size
        # MLPS 2.0 security hardening. For more information, see [Use MLPS 2.0 security hardening for ACK](https://help.aliyun.com/document_detail/196148.html).
        # 
        # Valid values:
        # 
        # - `true`: Enables MLPS 2.0 security hardening.
        # 
        # - `false`: Disables MLPS 2.0 security hardening.
        # 
        # Default value: `false`.
        self.soc_enabled = soc_enabled
        # Specifies whether to enable performance burst for node system disks. Valid values:
        # 
        # - `true`: Enables performance burst.
        # 
        # - `false`: Disables performance burst.
        # 
        # You can set this parameter only when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The system disk category for nodes. Valid values:
        # 
        # - `cloud_efficiency`: Ultra disk.
        # 
        # - `cloud_ssd`: Standard SSD.
        # 
        # - `cloud_essd`: ESSD.
        # 
        # - `cloud_auto`: ESSD AutoPL.
        # 
        # - `cloud_essd_entry`: ESSD Entry.
        self.system_disk_category = system_disk_category
        # The performance level of node system disks. This parameter applies only to ESSDs. The performance level depends on the disk size. For more information, see [ESSD](https://help.aliyun.com/document_detail/122389.html).
        self.system_disk_performance_level = system_disk_performance_level
        # The provisioned read/write IOPS for node system disks. Valid values: 0 to min{50,000, 1000 × capacity - baseline performance}. Baseline performance = min{1,800 + 50 × capacity, 50,000}.
        # 
        # You can set this parameter only when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The system disk size for nodes. Valid values: [40,500]. Unit: GiB.
        self.system_disk_size = system_disk_size
        # The automatic snapshot policy ID for node system disks.
        self.system_disk_snapshot_policy_id = system_disk_snapshot_policy_id

    def validate(self):
        pass

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

        if self.instance_types is not None:
            result['instance_types'] = self.instance_types

        if self.key_pair is not None:
            result['key_pair'] = self.key_pair

        if self.login_password is not None:
            result['login_password'] = self.login_password

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

        if m.get('instance_types') is not None:
            self.instance_types = m.get('instance_types')

        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')

        if m.get('login_password') is not None:
            self.login_password = m.get('login_password')

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

class ModifyClusterRequestApiServerCustomCertSans(DaraModel):
    def __init__(
        self,
        action: str = None,
        subject_alternative_names: List[str] = None,
    ):
        # Specifies whether to overwrite or append the SAN configuration. Valid values:
        # 
        # - overwrite: Overwrites the existing configuration.
        # 
        # - append: Appends to the existing configuration.
        self.action = action
        # The list of SANs.
        self.subject_alternative_names = subject_alternative_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.subject_alternative_names is not None:
            result['subject_alternative_names'] = self.subject_alternative_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('subject_alternative_names') is not None:
            self.subject_alternative_names = m.get('subject_alternative_names')

        return self

