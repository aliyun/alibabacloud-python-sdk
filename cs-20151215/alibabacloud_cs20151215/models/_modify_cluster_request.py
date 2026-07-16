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
        # Access control list for the registered cluster API Server SLB.
        self.access_control_list = access_control_list
        # Custom API Server certificate SAN (Subject Alternative Name).
        # Used to add custom IPs or domain names to the SAN field of the cluster API Server server certificate for client access control.
        # 
        # Only managed clusters support this parameter.
        self.api_server_custom_cert_sans = api_server_custom_cert_sans
        # Whether to associate an EIP with the cluster for public access to API Server. Valid values:
        # 
        # - `true`: Associate an EIP with the cluster.
        # - `false`: Do not associate an EIP with the cluster.
        self.api_server_eip = api_server_eip
        # The ID of the EIP instance associated with the cluster API Server. This parameter takes effect only when `api_server_eip` is set to `true`.
        self.api_server_eip_id = api_server_eip_id
        # Custom cluster name. The name can contain digits, Chinese characters, English characters, or hyphens (-), must be 1 to 63 characters in length, and cannot start with a hyphen (-).
        self.cluster_name = cluster_name
        # When `cluster_type` is set to `ManagedKubernetes` and `profile` is configured, specifies the cluster specification. Valid values:
        # 
        # - `ack.pro.small`: Pro Edition
        # - `ack.pro.xlarge`: Pro XL
        # - `ack.pro.2xlarge`: Pro 2XL
        # - `ack.pro.4xlarge`: Pro 4XL (requires contacting customer service to enable allowlisting)
        # 
        # Pro XL, Pro 2XL, and Pro 4XL are three tiers provided by <props="china">[ACK Pro Provisioned Control Plane](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane)<props="intl">[ACK Pro Provisioned Control Plane](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane). By pre-allocating and fixing control plane resources, it ensures that API concurrency and Pod scheduling capabilities are always at a determined high level, suitable for AI training and inference, ultra-large-scale clusters, and mission-critical workloads.
        # 
        # For cluster management fees for Pro Edition and Provisioned Control Plane editions, see <props="china">[Cluster Management Fees](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee)<props="intl">[Cluster Management Fees](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee).
        self.cluster_spec = cluster_spec
        # Dedicated cluster control plane configuration.
        self.control_plane_config = control_plane_config
        # Cluster connection configuration.
        self.control_plane_endpoints_config = control_plane_endpoints_config
        # Cluster deletion protection, which prevents accidental deletion of the cluster through the console or API. Valid values:
        # 
        # - `true`: Enable cluster deletion protection. The cluster cannot be deleted through the console or API.
        # - `false`: Disable cluster deletion protection. The cluster can be deleted through the console or API.
        # 
        # Default value: `false`.
        self.deletion_protection = deletion_protection
        # Enable or disable the RRSA feature (only managed clusters support this parameter). Valid values:
        # 
        # - `true`: Enable.
        # - `false`: Disable.
        self.enable_rrsa = enable_rrsa
        # Rebind the cluster test domain. Valid values:
        # 
        # - `true`: Rebind the cluster test domain.
        # - `false`: Do not rebind the cluster test domain.
        # 
        # Default value: `false`.
        self.ingress_domain_rebinding = ingress_domain_rebinding
        # SLB instance ID of the cluster to be modified.
        self.ingress_loadbalancer_id = ingress_loadbalancer_id
        # Instance deletion protection to prevent accidental deletion and release of nodes through the console or API. Valid values:
        # 
        # - `true`: Nodes cannot be accidentally deleted through the console or API.
        # - `false`: Nodes can be deleted through the console or API.
        # 
        # Default value: `false`.
        self.instance_deletion_protection = instance_deletion_protection
        # Cluster maintenance window. This feature only takes effect for ACK Pro managed clusters.
        self.maintenance_window = maintenance_window
        # Cluster automatic O&M policy.
        self.operation_policy = operation_policy
        # Cluster resource group ID.
        self.resource_group_id = resource_group_id
        # Control plane security group ID.
        # 
        # - If you have configured blocking rules in the security group, ensure that the security group rules allow the protocols and ports required by the cluster. For recommended security group rules, see [Configure and Manage Cluster Security Groups](https://help.aliyun.com/document_detail/353191.html).
        # - For non-ACK dedicated clusters, during the change process, the cluster control plane and installed managed components (such as terway-controlplane) will briefly restart. We recommend performing this operation during off-peak hours. After the control plane security group is changed, the ENIs used by the cluster control plane and installed managed components will be automatically added to the new security group.
        # - For ACK dedicated clusters, after the control plane security group is changed, newly scaled-out Master nodes will automatically use the new control plane security group. Existing control plane nodes are not affected.
        self.security_group_id = security_group_id
        # System event storage configuration.
        self.system_events_logging = system_events_logging
        # Cluster timezone. See [Supported Timezones](https://help.aliyun.com/document_detail/354879.html).
        # - After changing the timezone, cluster inspection configurations will use the new timezone settings.
        # 
        # - For managed clusters, during the change process, the cluster control plane and installed managed components (such as terway-controlplane) will briefly restart. We recommend performing this operation during off-peak hours. After changing the timezone, newly scaled-out nodes will automatically use the new timezone settings. Existing nodes are not affected. You can use the node pool node reset feature to apply the new settings to existing nodes.
        # 
        # - For dedicated clusters, after changing the timezone, newly scaled-out nodes (including control plane nodes) will automatically use the new timezone settings. Existing nodes (including control plane nodes) are not affected. You can use the node pool node reset feature to apply the new settings to existing nodes. For control plane nodes, you need to scale out first and then scale in to apply the settings to all control plane nodes.
        self.timezone = timezone
        # Cluster control plane vSwitches. For dedicated clusters, this takes effect on newly scaled-out control plane nodes. When modifying control plane vSwitches for managed clusters, note the following:
        # - This parameter performs a full overwrite update. You must specify the complete list of target vSwitches.
        # - During the change, control plane components will briefly restart. Proceed with caution.
        # - Ensure that all security groups of the cluster (including the control plane security group, all node pool security groups, and container network security groups) allow inbound and outbound traffic for the IP ranges of the new vSwitches to prevent nodes and containers from being unable to connect to the API Server.
        # - If the new control plane vSwitches have ACL rules configured, ensure that the ACL rules allow communication with the cluster nodes, container network, and other IP ranges.
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
        # Whether to enable system event storage.
        # 
        # 
        # - true: Enable system event storage.
        # 
        # - false: Disable system event storage.
        self.enabled = enabled
        # LogProject name for system event storage.
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
        # Cluster automatic upgrade.
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
        # Cluster automatic upgrade frequency. For more information, see [Upgrade Frequency](https://help.aliyun.com/document_detail/2712866.html).
        # 
        # Valid values:
        # - patch: Latest patch version.
        # - stable: Second latest minor version.
        # - rapid: Latest minor version.
        self.channel = channel
        # Whether to enable cluster automatic upgrade.
        # 
        # - true: Enable automatic upgrade.
        # 
        # - false: Disable automatic upgrade.
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
        # Cluster internal domain name configuration. Applicable to ACK managed clusters. The cluster internal domain name is used by node-side system components such as kubelet and kube-proxy to access the API Server. When the cluster internal domain name access is not enabled, node-side system components access via the CLB IP.
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
        # VPCs where the cluster internal domain name record resolution takes effect.
        self.bind_vpcs = bind_vpcs
        # Whether to enable cluster internal domain name access. Valid values:
        # - true: Enable cluster internal domain name access. Node-side components (kubelet, kube-proxy) will access the API Server through the cluster internal domain name.
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
        # Whether to enable automatic renewal for control plane node instances. This parameter takes effect only when `charge_type` is set to `PrePaid`. Valid values:
        # 
        # - `true`: Enable automatic renewal.
        # - `false`: Disable automatic renewal.
        # 
        # Default value: `false`.
        self.auto_renew = auto_renew
        # Duration for each automatic renewal of control plane node instances.
        # 
        # Valid values: {1, 2, 3, 6, 12}. Unit: months.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # Control plane node instance billing method. Valid values:
        # 
        # - `PrePaid`: Subscription.
        # - `PostPaid`: Pay-as-you-go.
        # 
        # Default value: `PostPaid`.
        self.charge_type = charge_type
        # Whether to install the Cloud Monitor agent on control plane nodes. Valid values:
        # 
        # - `true`: Install the Cloud Monitor agent.
        # - `false`: Do not install the Cloud Monitor agent.
        self.cloud_monitor_flags = cloud_monitor_flags
        # Node CPU management policy. When the cluster version is 1.12.6 or later, the following two policies are supported:
        # 
        # - `static`: Allows enhanced CPU affinity and exclusivity for Pods with certain resource characteristics on the node.
        # - `none`: Uses the existing default CPU affinity scheme.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # Deployment set ID.
        self.deploymentset_id = deploymentset_id
        # Custom image ID. Specified when using a custom image.
        self.image_id = image_id
        # Operating system image type. Valid values:
        # 
        # - `AliyunLinux3`: Alinux3 image.
        # - `Custom`: Custom image.
        self.image_type = image_type
        # Instance types. For more information, see [Instance Family](https://help.aliyun.com/document_detail/25378.html).
        self.instance_types = instance_types
        # Key pair name. Mutually exclusive with `login_password`.
        self.key_pair = key_pair
        # SSH login password. Mutually exclusive with `key_pair`. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. If you want to use password login, specify this parameter during scale-out.
        self.login_password = login_password
        # Node service port range.
        # Available port range: [30000, 65535].
        # 
        # Default value: 30000-32767.
        self.node_port_range = node_port_range
        # Control plane node instance subscription duration. This parameter takes effect and is required only when `charge_type` is set to `PrePaid`.
        # 
        # When `period_unit=Month`, valid values: {1, 2, 3, 6, 12, 24, 36, 48, 60}.
        self.period = period
        # Control plane node instance billing period. This parameter takes effect only when `charge_type` is set to `PrePaid`.
        # 
        # `Month`: Billed on a monthly basis. Currently, only monthly billing is supported.
        self.period_unit = period_unit
        # Container runtime name. Valid values:
        # 
        # - `containerd`: Recommended. Supported by all cluster versions.
        # 
        # Default value: containerd.
        self.runtime = runtime
        # Alibaba Cloud OS security hardening. Valid values:
        # 
        # - `true`: Enable Alibaba Cloud OS security hardening.
        # - `false`: Disable Alibaba Cloud OS security hardening.
        # 
        # Default value: `false`.
        self.security_hardening_os = security_hardening_os
        # Number of control plane nodes. To scale out the dedicated cluster control plane, this parameter specifies the target number of control plane nodes and must be greater than the current number of control plane nodes.
        self.size = size
        # Security hardening for compliance. For more information, see [ACK Security Hardening for Compliance](https://help.aliyun.com/document_detail/196148.html).
        # 
        # Valid values:
        # - `true`: Enable security hardening for compliance.
        # - `false`: Disable security hardening for compliance.
        # 
        # Default value: `false`.
        self.soc_enabled = soc_enabled
        # Whether to enable burst (performance bursting) for the node system disk. Valid values:
        # - `true`: Enable.
        # - `false`: Disable.
        # 
        # This parameter is supported only when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # Node system disk type. Valid values:
        # - `cloud_efficiency`: Ultra disk.
        # - `cloud_ssd`: SSD disk.
        # - `cloud_essd`: ESSD disk.
        # - `cloud_auto`: ESSD AutoPL disk.
        # - `cloud_essd_entry`: ESSD Entry disk.
        self.system_disk_category = system_disk_category
        # Node system disk performance level. Only applicable to ESSD disks. The performance level is related to the disk size. For more information, see [ESSD](https://help.aliyun.com/document_detail/122389.html).
        self.system_disk_performance_level = system_disk_performance_level
        # Provisioned read/write IOPS for the node system disk. Valid values: 0 to min{50,000, 1000*capacity - baseline performance}. Baseline performance = min{1,800 + 50*capacity, 50,000}.
        # 
        # This parameter is supported only when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # Node system disk size. Valid values: [40, 500]. Unit: GiB.
        self.system_disk_size = system_disk_size
        # Automatic snapshot policy ID for the node system disk.
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
        # Overwrite or append SAN configuration. Valid values:
        # - overwrite: Overwrite.
        # - append: Append.
        self.action = action
        # SAN list.
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

