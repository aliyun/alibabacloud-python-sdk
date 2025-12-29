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
        control_plane_config: main_models.ModifyClusterRequestControlPlaneConfig = None,
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
        # The network access control list (ACL) of the SLB instance associated with the API server if the cluster is a registered cluster.
        self.access_control_list = access_control_list
        # The custom subject alternative names (SANs) for the API server certificate to accept requests from specified IP addresses or domain names. This parameter is available only for ACK managed clusters.
        self.api_server_custom_cert_sans = api_server_custom_cert_sans
        # Specifies whether to associate an elastic IP address (EIP) with the cluster. This EIP is used to enable access to the API server over the Internet. Valid values:
        # 
        # *   `true`: associates an EIP with the cluster.
        # *   `false`: does not associate an EIP with the cluster.
        self.api_server_eip = api_server_eip
        # The ID of the EIP that you want to associate with the API server of the cluster. This parameter takes effect when `api_server_eip` is set to `true`.
        self.api_server_eip_id = api_server_eip_id
        # The cluster name.
        # 
        # The cluster name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). The cluster name cannot start with a hyphen (-).
        self.cluster_name = cluster_name
        # The control plane configurations of an ACK dedicated cluster.
        self.control_plane_config = control_plane_config
        # Specifies whether to enable cluster deletion protection. If you enable this option, the cluster cannot be deleted in the console or by calling API operations. Valid values:
        # 
        # *   `true`: enables cluster deletion protection.
        # *   `false`: disables cluster deletion protection.
        # 
        # Default value: `false`
        self.deletion_protection = deletion_protection
        # Specifies whether to enable the RAM Roles for Service Accounts (RRSA) feature. This parameter is available only for ACK managed clusters. Valid values:
        # 
        # *   `true`: enables the RRSA feature.
        # *   `false`: disables the RRSA feature.
        self.enable_rrsa = enable_rrsa
        # Specifies whether to remap the test domain name of the cluster. Valid values:
        # 
        # *   `true`: remaps the test domain name of the cluster.
        # *   `false`: does not remap the test domain name of the cluster.
        # 
        # Default value: `false`
        self.ingress_domain_rebinding = ingress_domain_rebinding
        # The ID of the Server Load Balancer (SLB) instance of the cluster to be modified.
        self.ingress_loadbalancer_id = ingress_loadbalancer_id
        # Specifies whether to enable instance deletion protection. If you enable this option, the instance cannot be deleted in the console or by calling API operations. Valid values:
        # 
        # *   `true`: enables instance deletion protection.
        # *   `false`: disables instance deletion protection.
        # 
        # Default value: `false`
        self.instance_deletion_protection = instance_deletion_protection
        # The cluster maintenance window. This feature takes effect only for ACK Pro clusters.
        self.maintenance_window = maintenance_window
        # The automatic O\\&M policy of the cluster.
        self.operation_policy = operation_policy
        # The resource group ID of the cluster.
        self.resource_group_id = resource_group_id
        # The ID of the security group for the control plane. 
        # 
        # - If block rules are configured in the security group, ensure the security group rules allow traffic for protocols and ports required by the cluster. For recommended security group rules, see [Configure and manage security groups for an ACK cluster](https://www.alibabacloud.com/help/en/ack/ack-managed-and-ack-dedicated/user-guide/configure-security-group-rules-to-enforce-access-control-on-ack-clusters?spm=a2c63.p38356.help-menu-85222.d_2_0_4_3.43e35d09s8oSlR).
        # 
        # - For non-ACK dedicated clusters: 
        #   - During security group updates, the cluster control plane and managed components (e.g., terway-controlplane) will restart briefly. Perform this operation during off-peak hours.
        #   - After updating the control plane security group, the Elastic Network Interfaces (ENIs) used by the control plane and managed components will automatically join the new security group.
        # 
        # - For ACK dedicated clusters:
        #    - After updating the control plane security group, newly scaled-out master nodes will automatically apply the new security group. Existing control plane nodes remain unaffected.
        self.security_group_id = security_group_id
        # The storage configurations of system events.
        self.system_events_logging = system_events_logging
        # The time zone configuration for the cluster.
        # 
        # - After modifying the time zone, cluster inspection configurations will adopt the new time zone.
        # 
        # - For ACK managed clusters:
        #    - During time zone updates, the cluster control plane and managed components (e.g., terway-controlplane) will restart briefly. Perform this operation during off-peak hours.
        #    - After updating the time zone:
        #       - Newly scaled-out nodes will automatically apply the new time zone.
        #       - Existing nodes remain unaffected. Reset the node to apply changes to existing nodes.
        # 
        # - For ACK dedicated clusters:
        #    - After updating the time zone:
        #       - Newly scaled-out nodes (including control plane nodes) automatically apply the new time zone.
        #       - Existing nodes (including control plane nodes) remain unaffected. Reset the node to apply changes to existing nodes.
        #       - For control plane nodes, perform a scale-out followed by a scale-in to apply the new time zone to all control plane nodes.
        self.timezone = timezone
        # The vSwitches of the control plane. This parameter can be used to change the vSwitches of the control plane in an ACK managed cluster. Take note of the following items:
        # 
        # *   This parameter overwrites the existing configuration. You must specify all vSwitches of the control plane.
        # *   The control plane components restarts during the change process. Exercise caution when you perform this operation.
        # *   Ensure that all security groups of the cluster, including the security groups of the control plane, all node pools, and container network, are allowed to access the CIDR blocks of the new vSwitches. This ensures that the nodes and containers can connect to the API server.
        # *   If the new vSwitches of the control plane are configured with an ACL, ensure that the ACL allows communication between the new vSwitches and CIDR blocks such as those of the cluster nodes and the container network.
        self.vswitch_ids = vswitch_ids

    def validate(self):
        if self.api_server_custom_cert_sans:
            self.api_server_custom_cert_sans.validate()
        if self.control_plane_config:
            self.control_plane_config.validate()
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

        if self.control_plane_config is not None:
            result['control_plane_config'] = self.control_plane_config.to_map()

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

        if m.get('control_plane_config') is not None:
            temp_model = main_models.ModifyClusterRequestControlPlaneConfig()
            self.control_plane_config = temp_model.from_map(m.get('control_plane_config'))

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
        # Specifies whether to enable system event storage.
        self.enabled = enabled
        # The name of the Simple Log Service project that stores system events.
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
        # The configurations of automatic update.
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
        # The frequency of auto cluster update. For more information, see [Update frequency](https://help.aliyun.com/document_detail/2712866.html).
        # 
        # Valid values:
        # 
        # *   patch: the latest patch version.
        # *   stables: the second-latest minor version.
        # *   rapid: the latest minor version.
        self.channel = channel
        # Specifies whether to enable automatic update.
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
        # Specifies whether to enable auto-renewal for control plane nodes. This parameter takes effect only when `charge_type` is set to `PrePaid`. Valid values:
        # 
        # *   `true`: enables auto-renewal.
        # *   `false`: disables auto-renewal.
        # 
        # Default value: `false`
        self.auto_renew = auto_renew
        # The auto-renewal period of control plane nodes. Valid values: 1, 2, 3, 6, and 12.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # The billing method of control plane nodes. Valid values:
        # 
        # *   `PrePaid`: subscription.
        # *   `PostPaid`: pay-as-you-go.
        # 
        # Default value: `PostPaid`.
        self.charge_type = charge_type
        # Specifies whether to install the CloudMonitor agent. Valid values:
        # 
        # *   `true`: installs the CloudMonitor agent.
        # *   `false`: does not install the CloudMonitor agent.
        self.cloud_monitor_flags = cloud_monitor_flags
        # The CPU management policy of nodes in the node pool. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later:
        # 
        # *   `static`: allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity.
        # *   `none`: specifies that the default CPU affinity is used.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # The ID of the deployment set.
        self.deploymentset_id = deploymentset_id
        # The custom image ID. You must configure this parameter if you use a custom image.
        self.image_id = image_id
        # The type of the OS image. Valid values:
        # 
        # *   `AliyunLinux3`: Alibaba Cloud Linux 3.
        # *   `Custom`: the custom image.
        self.image_type = image_type
        # The type of instance. For more information, see [Overview of ECS instance families](https://help.aliyun.com/document_detail/25378.html).
        self.instance_types = instance_types
        # The name of the key pair. You must configure either this parameter or the `login_password` parameter.
        self.key_pair = key_pair
        # The password for SSH logon. You must configure either this parameter or the `key_pair` parameter. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. To log on with a password, you must specify this parameter during the scale-out.
        self.login_password = login_password
        # The node port range.
        self.node_port_range = node_port_range
        # The subscription duration of the instance. This parameter takes effect and is required only when `charge_type` is set to `PrePaid`.
        # 
        # If `PeriodUnit=Month` is specified, the valid values are 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        self.period = period
        # The billing cycle of control plane nodes. This parameter takes effect only when `instance_charge_type` is set to `PrePaid`.
        # 
        # Set the value to `Month`.
        self.period_unit = period_unit
        # The type of the container runtime. Valid values:
        # 
        # *   `containerd`: supports all Kubernetes versions. We recommend that you set the parameter to this value.
        # 
        # Default value: containerd.
        self.runtime = runtime
        # Specifies whether to enable Alibaba Cloud Linux Security Hardening. Valid values:
        # 
        # *   `true`: enables Alibaba Cloud Linux Security Hardening.
        # *   `false`: disables Alibaba Cloud Linux Security Hardening.
        # 
        # Default value: `false`
        self.security_hardening_os = security_hardening_os
        # The number of control plane nodes. If you want to scale out the control plane in an ACK dedicated cluster, set this parameter to the desired number of nodes. This parameter must be greater than the current number of nodes.
        self.size = size
        # Specifies whether to enable Multi-Level Protection Scheme (MLPS) security hardening. For more information, see [ACK security hardening based on MLPS](https://help.aliyun.com/document_detail/196148.html).
        # 
        # Valid values:
        # 
        # *   `true`: enables MLPS security hardening.
        # *   `false`: disables MLPS security hardening.
        # 
        # Default value: `false`.
        self.soc_enabled = soc_enabled
        # Specifies whether to enable the burst feature for the system disk. Valid values:
        # 
        # *   `true`: enables the burst feature.
        # *   `false`: disables the burst feature.
        # 
        # This parameter is effective only when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The category of the system disk for nodes. Valid values:
        # 
        # *   `cloud`: basic disk.
        # *   `cloud_efficiency`: ultra disk.
        # *   `cloud_ssd`: standard SSD.
        # *   `cloud_essd`: Enterprise ESSD (ESSD).
        # *   `cloud_auto`: ESSD AutoPL disk.
        # *   `cloud_essd_entry`: ESSD Entry disk.
        self.system_disk_category = system_disk_category
        # The performance level (PL) of the system disk that you want to use for the node. This parameter is effective only for ESSDs. This parameter is related to the disk size. For more information, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        self.system_disk_performance_level = system_disk_performance_level
        # The preset read/write input/output operations per second (IOPS) of the system disk. Valid values: 0 to min{50,000, 1,000 × Capacity - Baseline IOPS}. Baseline IOPS = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # This parameter is effective only when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The type of the system disk. Valid values: [40,500]. Unit: GiB.
        self.system_disk_size = system_disk_size
        # The ID of the automatic snapshot policy applied to the node system disk.
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
        # Specifies whether to overwrite or add SANs. Valid values:
        # 
        # *   overwrite: overwrites SANs.
        # *   append: adds SANs.
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

