# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class CreateClusterRequest(DaraModel):
    def __init__(
        self,
        access_control_list: List[str] = None,
        addons: List[main_models.Addon] = None,
        api_audiences: str = None,
        audit_log_config: main_models.CreateClusterRequestAuditLogConfig = None,
        auto_mode: main_models.CreateClusterRequestAutoMode = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        charge_type: str = None,
        cis_enabled: bool = None,
        cloud_monitor_flags: bool = None,
        cluster_domain: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        container_cidr: str = None,
        control_plane_config: main_models.CreateClusterRequestControlPlaneConfig = None,
        control_plane_endpoints_config: main_models.CreateClusterRequestControlPlaneEndpointsConfig = None,
        controlplane_log_components: List[str] = None,
        controlplane_log_project: str = None,
        controlplane_log_ttl: str = None,
        cpu_policy: str = None,
        custom_san: str = None,
        deletion_protection: bool = None,
        disable_rollback: bool = None,
        enable_rrsa: bool = None,
        encryption_provider_key: str = None,
        endpoint_public_access: bool = None,
        extra_sans: List[str] = None,
        format_disk: bool = None,
        image_id: str = None,
        image_type: str = None,
        instances: List[str] = None,
        ip_stack: str = None,
        is_enterprise_security_group: bool = None,
        keep_instance_name: bool = None,
        key_pair: str = None,
        kubernetes_version: str = None,
        load_balancer_id: str = None,
        load_balancer_spec: str = None,
        logging_type: str = None,
        login_password: str = None,
        maintenance_window: main_models.MaintenanceWindow = None,
        master_auto_renew: bool = None,
        master_auto_renew_period: int = None,
        master_count: int = None,
        master_instance_charge_type: str = None,
        master_instance_types: List[str] = None,
        master_period: int = None,
        master_period_unit: str = None,
        master_system_disk_category: str = None,
        master_system_disk_performance_level: str = None,
        master_system_disk_size: int = None,
        master_system_disk_snapshot_policy_id: str = None,
        master_vswitch_ids: List[str] = None,
        name: str = None,
        nat_gateway: bool = None,
        node_cidr_mask: str = None,
        node_name_mode: str = None,
        node_port_range: str = None,
        nodepools: List[main_models.Nodepool] = None,
        num_of_nodes: int = None,
        operation_policy: main_models.CreateClusterRequestOperationPolicy = None,
        os_type: str = None,
        period: int = None,
        period_unit: str = None,
        platform: str = None,
        pod_vswitch_ids: List[str] = None,
        profile: str = None,
        proxy_mode: str = None,
        rds_instances: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        rrsa_config: main_models.CreateClusterRequestRrsaConfig = None,
        runtime: main_models.Runtime = None,
        security_group_id: str = None,
        security_hardening_os: bool = None,
        service_account_issuer: str = None,
        service_cidr: str = None,
        service_discovery_types: List[str] = None,
        snat_entry: bool = None,
        soc_enabled: bool = None,
        ssh_flags: bool = None,
        tags: List[main_models.Tag] = None,
        taints: List[main_models.Taint] = None,
        timeout_mins: int = None,
        timezone: str = None,
        user_ca: str = None,
        user_data: str = None,
        vpcid: str = None,
        vswitch_ids: List[str] = None,
        worker_auto_renew: bool = None,
        worker_auto_renew_period: int = None,
        worker_data_disks: List[main_models.CreateClusterRequestWorkerDataDisks] = None,
        worker_instance_charge_type: str = None,
        worker_instance_types: List[str] = None,
        worker_period: int = None,
        worker_period_unit: str = None,
        worker_system_disk_category: str = None,
        worker_system_disk_performance_level: str = None,
        worker_system_disk_size: int = None,
        worker_system_disk_snapshot_policy_id: str = None,
        worker_vswitch_ids: List[str] = None,
        zone_id: str = None,
        zone_ids: List[str] = None,
    ):
        # **[Deprecated]** The access control list for the API Server SLB of the registered cluster.
        self.access_control_list = access_control_list
        # The list of cluster components. Use `addons` to specify the components to install when creating a cluster.
        self.addons = addons
        # A ServiceAccount is the access credential for communication between a pod and the cluster API server. The `api-audiences` parameter specifies the valid request `token` identities used by the `apiserver` to authenticate whether a request `token` is valid. You can specify multiple `audience` values separated by commas (,).
        self.api_audiences = api_audiences
        # The cluster audit log configuration.
        self.audit_log_config = audit_log_config
        # The [intelligent managed mode](https://help.aliyun.com/document_detail/2938898.html) configuration.
        self.auto_mode = auto_mode
        # **[Deprecated]**
        self.auto_renew = auto_renew
        # **[Deprecated]**
        self.auto_renew_period = auto_renew_period
        # **[Deprecated]**
        self.charge_type = charge_type
        # **[Deprecated]** For cluster control plane configuration, use the `security_hardening_os` parameter under `control_plane_config` instead. For node pool configuration, use the `security_hardening_os` parameter under `scaling_group` in `nodepool` instead.
        self.cis_enabled = cis_enabled
        # **[Deprecated]** For cluster control plane node configuration, use the `cloud_monitor_flags` parameter under `control_plane_config` instead. For node pool configuration, use the `cms_enabled` parameter under `kubernetes_config` in `nodepool` instead.
        self.cloud_monitor_flags = cloud_monitor_flags
        # The cluster local domain name.
        self.cluster_domain = cluster_domain
        # If you set `cluster_type` to `ManagedKubernetes` and configure `profile`, you can further specify the cluster specifications. Valid values:
        self.cluster_spec = cluster_spec
        # - `Kubernetes`: ACK dedicated cluster.
        self.cluster_type = cluster_type
        # The pod network CIDR block. It must be a valid private CIDR block, which includes the following CIDR blocks and their subnets: 10.0.0.0/8, 172.16-31.0.0/12-16, and 192.168.0.0/16. It cannot overlap with the CIDR blocks used by the VPC or existing Kubernetes clusters in the VPC. It cannot be modified after the cluster is created.
        self.container_cidr = container_cidr
        # The control plane configuration for ACK dedicated clusters.
        self.control_plane_config = control_plane_config
        # The cluster connection configuration.
        self.control_plane_endpoints_config = control_plane_endpoints_config
        # The list of component names that specifies which control plane components to collect logs from.
        self.controlplane_log_components = controlplane_log_components
        # The Simple Log Service project for control plane component logs. You can use an existing project for log storage or allow the system to automatically create a project. If you choose automatic creation, a Simple Log Service project named `k8s-log-{ClusterID}` is automatically created.
        self.controlplane_log_project = controlplane_log_project
        # The number of days for control plane component log retention.
        self.controlplane_log_ttl = controlplane_log_ttl
        # **[Deprecated]** For cluster control plane configuration, use the cpu_policy parameter under `control_plane_config` instead. For node pool configuration, use the cpu_policy parameter under `kubernetes_config` in `nodepool` instead.
        self.cpu_policy = cpu_policy
        # **[Deprecated]** Use the `extra_sans` parameter instead.
        self.custom_san = custom_san
        # Specifies whether to enable deletion protection for the cluster to prevent accidental deletion through the console or API. Valid values:
        self.deletion_protection = deletion_protection
        # **[Deprecated]** When cluster creation fails, rollback is not performed by default. You must manually clean up the failed cluster.
        self.disable_rollback = disable_rollback
        # **[Deprecated]** Use the `rrsa_config` parameter instead.
        self.enable_rrsa = enable_rrsa
        # The KMS key ID used to encrypt data cloud disks. For more information, see [Key Management Service](https://help.aliyun.com/document_detail/28935.html).
        self.encryption_provider_key = encryption_provider_key
        # Specifies whether to public network access. The API Server is exposed through an EIP to public network access to the cluster.
        self.endpoint_public_access = endpoint_public_access
        # The custom API Server certificate SAN (Subject Alternative Name).
        self.extra_sans = extra_sans
        # **[Deprecated]** Selecting existing nodes during cluster creation is not supported. To add existing nodes to a cluster, create a node pool first and call the [AttachInstancesToNodePool](https://help.aliyun.com/document_detail/2667920.html) operation.
        self.format_disk = format_disk
        # **[Deprecated]** For cluster control plane configuration, use the `image_id` parameter under `control_plane_config` instead. For node pool configuration, use the `image_id` parameter under `scaling_group` in `nodepool` instead.
        self.image_id = image_id
        # **[Deprecated]** For cluster control plane configuration, use the `image_type` parameter under `control_plane_config` instead. For node pool configuration, use the `image_type` parameter under `scaling_group` in `nodepool` instead.
        self.image_type = image_type
        # **[Deprecated]** Selecting existing nodes during cluster creation is not supported. To add existing nodes to a cluster, create a node pool first and call the [AttachInstancesToNodePool](https://help.aliyun.com/document_detail/2667920.html) operation.
        self.instances = instances
        # The IP stack of the cluster.
        self.ip_stack = ip_stack
        # Specifies whether to enable automatic creation of an advanced security group. This parameter takes effect only when `security_group_id` is empty.
        self.is_enterprise_security_group = is_enterprise_security_group
        # **[Deprecated]** Selecting existing nodes during cluster creation is not supported. To add existing nodes to a cluster, create a node pool first and call the [AttachInstancesToNodePool](https://help.aliyun.com/document_detail/2667920.html) operation.
        self.keep_instance_name = keep_instance_name
        # **[Deprecated]** For cluster control plane configuration, use the key_pair parameter under `control_plane_config` instead. For node pool configuration, use the key_pair parameter under `scaling_group` in `nodepool` instead.
        self.key_pair = key_pair
        # The cluster version, which is consistent with the Kubernetes community baseline version. Use the latest version. If you do not specify this parameter, the latest version is used by default.
        self.kubernetes_version = kubernetes_version
        # The CLB instance ID used for API Server access. When this parameter is specified, automatic creation of the API Server CLB is skipped.
        self.load_balancer_id = load_balancer_id
        # **[Deprecated]** CLB is billed on a pay-by-usage basis. This parameter does not take effect.
        self.load_balancer_spec = load_balancer_spec
        # **[Deprecated]** Enables the log service for the cluster. This parameter takes effect only for ACK Serverless clusters, and the value must be `SLS`.
        self.logging_type = logging_type
        # **[Deprecated]** For cluster control plane configuration, use the login_password parameter under `control_plane_config` instead. For node pool configuration, use the login_password parameter under `scaling_group` in `nodepool` instead.
        self.login_password = login_password
        # The cluster maintenance window.
        self.maintenance_window = maintenance_window
        # **[Deprecated]** For cluster control plane configuration, use the auto_renew parameter under `control_plane_config` instead.
        self.master_auto_renew = master_auto_renew
        # **[Deprecated]** For cluster control plane configuration, use the auto_renew_period parameter under `control_plane_config` instead.
        self.master_auto_renew_period = master_auto_renew_period
        # **[Deprecated]** For cluster control plane configuration, use the size parameter under `control_plane_config` instead.
        self.master_count = master_count
        # **[Deprecated]** For cluster control plane configuration, use the instance_charge_type parameter under `control_plane_config` instead.
        self.master_instance_charge_type = master_instance_charge_type
        # **[Deprecated]** For cluster control plane configuration, use the instance_types parameter under `control_plane_config` instead.
        self.master_instance_types = master_instance_types
        # **[Deprecated]** For cluster control plane configuration, use the `unit` parameter under `control_plane_config` instead.
        self.master_period = master_period
        # **[Deprecated]** For cluster control plane configuration, use the period_unit parameter under `control_plane_config` instead.
        self.master_period_unit = master_period_unit
        # **[Deprecated]** For cluster control plane configuration, use the system_disk_category parameter under `control_plane_config` instead.
        self.master_system_disk_category = master_system_disk_category
        # **[Deprecated]** For cluster control plane configuration, use the system_disk_performance_level parameter under `control_plane_config` instead.
        self.master_system_disk_performance_level = master_system_disk_performance_level
        # **[Deprecated]** For cluster control plane configuration, use the system_disk_size parameter under `control_plane_config` instead.
        self.master_system_disk_size = master_system_disk_size
        # **[Deprecated]** For cluster control plane configuration, use the system_disk_snapshot_policy_id parameter under `control_plane_config` instead.
        self.master_system_disk_snapshot_policy_id = master_system_disk_snapshot_policy_id
        # **[Deprecated]** Use the `vswitch_ids` parameter instead.
        self.master_vswitch_ids = master_vswitch_ids
        # The custom cluster name. The name must be 1 to 63 characters in length and can contain digits, Chinese characters, letters, and hyphens (-). It cannot start with a hyphen (-).
        # 
        # This parameter is required.
        self.name = name
        # **[Deprecated]** Use the `snat_entry` parameter instead.
        self.nat_gateway = nat_gateway
        # The number of node IP addresses, determined by specifying the network CIDR block. This parameter takes effect only for Flannel network type clusters.
        self.node_cidr_mask = node_cidr_mask
        # **[Deprecated]** For node pool configuration, use the `node_name_mode` parameter under `kubernetes_config` in `nodepool` instead.
        self.node_name_mode = node_name_mode
        # The node service port. Valid port range: [30000,65535\\].
        self.node_port_range = node_port_range
        # The list of node pools.
        self.nodepools = nodepools
        # **[Deprecated]** For node pool configuration, use the desired_size parameter under `scaling_group` in `nodepool` instead.
        self.num_of_nodes = num_of_nodes
        # The cluster automatic O&M policy.
        self.operation_policy = operation_policy
        # **[Deprecated]** For cluster control plane node configuration, use the `image_type` parameter under `control_plane_config` instead. For node pool configuration, use the `image_type` parameter under `scaling_group` in `nodepool` instead.
        self.os_type = os_type
        # **[Deprecated]**
        self.period = period
        # **[Deprecated]**
        self.period_unit = period_unit
        # **[Deprecated]** For node pool configuration, use the `platform` parameter under `scaling_group` in `nodepool` instead.
        self.platform = platform
        # **[Deprecated]** When you select Terway as the network plugin, you must specify vSwitches for pod IP address allocation. Each pod vSwitch corresponds to a worker node vSwitch, and the pod vSwitch and the worker node vSwitch must be in the same zone.
        self.pod_vswitch_ids = pod_vswitch_ids
        # If you set `cluster_type` to `ManagedKubernetes`, which indicates an ACK managed cluster, you can further specify the cluster subtype.
        self.profile = profile
        # The kube-proxy proxy mode.
        self.proxy_mode = proxy_mode
        # **[Deprecated]** For node pool configuration, use the `rds_instances` parameter under `scaling_group` in `nodepool` instead.
        self.rds_instances = rds_instances
        # The region ID of the cluster. For details, see [Regions supported by container service](https://help.aliyun.com/document_detail/216938.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID of the cluster, which is used to isolate different resources.
        self.resource_group_id = resource_group_id
        # The RRSA feature configuration.
        self.rrsa_config = rrsa_config
        # The container runtime in the cluster. Supported runtimes include containerd, sandboxed containers, and Docker.
        self.runtime = runtime
        # The security group ID. Specify this parameter when you use an existing security group to create a cluster. This parameter and `is_enterprise_security_group` are mutually exclusive. Cluster nodes are automatically added to this security group.
        self.security_group_id = security_group_id
        # **[Deprecated]** For cluster control plane configuration, use the `security_hardening_os` parameter under `control_plane_config` instead. For node pool configuration, use the `security_hardening_os` parameter under `scaling_group` in `nodepool` instead.
        self.security_hardening_os = security_hardening_os
        # A ServiceAccount is the access credential for communication between a pod and the cluster API server. The `service-account-issuer` is the issuer identity in the `serviceaccount token`, which is the `iss` field in the `token payload`.
        self.service_account_issuer = service_account_issuer
        # The Service network CIDR block. Valid ranges: 10.0.0.0/16-24, 172.16-31.0.0/16-24, and 192.168.0.0/16-24.
        self.service_cidr = service_cidr
        # **[Deprecated]** The service discovery types within the cluster, used to specify the service discovery method in `ACK Serverless` clusters.
        self.service_discovery_types = service_discovery_types
        # Specifies whether to configure SNAT for the VPC. Valid values:
        self.snat_entry = snat_entry
        # **[Deprecated]** For cluster control plane node configuration, use the `soc_enabled` parameter under `control_plane_config` instead. For node pool configuration, use the `soc_enabled` parameter under `scaling_group` in `nodepool` instead.
        self.soc_enabled = soc_enabled
        # Specifies whether to enable public SSH logon. This is used to log on to the master nodes of ACK dedicated clusters. This parameter does not take effect for managed clusters.
        self.ssh_flags = ssh_flags
        # The node tags. Tag definition rules:
        self.tags = tags
        # **[Deprecated]** For node pool configuration, use the `taints` parameter under `kubernetes_config` in `nodepool` instead.
        self.taints = taints
        # **[Deprecated]** When cluster creation fails, rollback is not performed by default. You must manually clean up the failed cluster.
        self.timeout_mins = timeout_mins
        # The time zone used by the cluster. For more information, see [Supported time zones](https://help.aliyun.com/document_detail/354879.html).
        self.timezone = timezone
        # The custom cluster CA.
        self.user_ca = user_ca
        # **[Deprecated]** The custom node data.
        self.user_data = user_data
        # The VPC used by the cluster. You must provide a VPC when you create a cluster.
        self.vpcid = vpcid
        # The vSwitches for cluster nodes. This field is required when you create a zero-node managed cluster.
        self.vswitch_ids = vswitch_ids
        # **[Deprecated]** For node pool configuration, use the auto_renew parameter under `scaling_group` in `nodepool` instead.
        self.worker_auto_renew = worker_auto_renew
        # **[Deprecated]** For node pool configuration, use the auto_renew_period parameter under `scaling_group` in `nodepool` instead.
        self.worker_auto_renew_period = worker_auto_renew_period
        # **[Deprecated]** For node pool configuration, use the data_disks parameter under `scaling_group` in `nodepool` instead.
        self.worker_data_disks = worker_data_disks
        # **[Deprecated]** For node pool configuration, use the instance_charge_type parameter under `scaling_group` in `nodepool` instead.
        self.worker_instance_charge_type = worker_instance_charge_type
        # **[Deprecated]** For node pool configuration, use the instance_types parameter under `scaling_group` in `nodepool` instead.
        self.worker_instance_types = worker_instance_types
        # **[Deprecated]** For node pool configuration, use the period parameter under `scaling_group` in `nodepool` instead.
        self.worker_period = worker_period
        # **[Deprecated]** For node pool configuration, use the period_unit parameter under `scaling_group` in `nodepool` instead.
        self.worker_period_unit = worker_period_unit
        # **[Deprecated]** For node pool configuration, use the system_disk_category parameter under `scaling_group` in `nodepool` instead.
        self.worker_system_disk_category = worker_system_disk_category
        # **[Deprecated]** For node pool configuration, use the system_disk_performance_level parameter under `scaling_group` in `nodepool` instead.
        self.worker_system_disk_performance_level = worker_system_disk_performance_level
        # **[Deprecated]** For node pool configuration, use the system_disk_size parameter under `scaling_group` in `nodepool` instead.
        self.worker_system_disk_size = worker_system_disk_size
        # **[Deprecated]** For node pool configuration, use the system_disk_snapshot_policy_id parameter under `scaling_group` in `nodepool` instead.
        self.worker_system_disk_snapshot_policy_id = worker_system_disk_snapshot_policy_id
        # **[Deprecated]** For node pool configuration, use the vswitch_ids parameter under `scaling_group` in `nodepool` instead.
        self.worker_vswitch_ids = worker_vswitch_ids
        # **[Deprecated]** Use the `zone_ids` parameter instead.
        self.zone_id = zone_id
        # The zone IDs of the cluster region. This parameter is specific to ACK managed clusters.
        self.zone_ids = zone_ids

    def validate(self):
        if self.addons:
            for v1 in self.addons:
                 if v1:
                    v1.validate()
        if self.audit_log_config:
            self.audit_log_config.validate()
        if self.auto_mode:
            self.auto_mode.validate()
        if self.control_plane_config:
            self.control_plane_config.validate()
        if self.control_plane_endpoints_config:
            self.control_plane_endpoints_config.validate()
        if self.maintenance_window:
            self.maintenance_window.validate()
        if self.nodepools:
            for v1 in self.nodepools:
                 if v1:
                    v1.validate()
        if self.operation_policy:
            self.operation_policy.validate()
        if self.rrsa_config:
            self.rrsa_config.validate()
        if self.runtime:
            self.runtime.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.taints:
            for v1 in self.taints:
                 if v1:
                    v1.validate()
        if self.worker_data_disks:
            for v1 in self.worker_data_disks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_control_list is not None:
            result['access_control_list'] = self.access_control_list

        result['addons'] = []
        if self.addons is not None:
            for k1 in self.addons:
                result['addons'].append(k1.to_map() if k1 else None)

        if self.api_audiences is not None:
            result['api_audiences'] = self.api_audiences

        if self.audit_log_config is not None:
            result['audit_log_config'] = self.audit_log_config.to_map()

        if self.auto_mode is not None:
            result['auto_mode'] = self.auto_mode.to_map()

        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['auto_renew_period'] = self.auto_renew_period

        if self.charge_type is not None:
            result['charge_type'] = self.charge_type

        if self.cis_enabled is not None:
            result['cis_enabled'] = self.cis_enabled

        if self.cloud_monitor_flags is not None:
            result['cloud_monitor_flags'] = self.cloud_monitor_flags

        if self.cluster_domain is not None:
            result['cluster_domain'] = self.cluster_domain

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

        if self.controlplane_log_components is not None:
            result['controlplane_log_components'] = self.controlplane_log_components

        if self.controlplane_log_project is not None:
            result['controlplane_log_project'] = self.controlplane_log_project

        if self.controlplane_log_ttl is not None:
            result['controlplane_log_ttl'] = self.controlplane_log_ttl

        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy

        if self.custom_san is not None:
            result['custom_san'] = self.custom_san

        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection

        if self.disable_rollback is not None:
            result['disable_rollback'] = self.disable_rollback

        if self.enable_rrsa is not None:
            result['enable_rrsa'] = self.enable_rrsa

        if self.encryption_provider_key is not None:
            result['encryption_provider_key'] = self.encryption_provider_key

        if self.endpoint_public_access is not None:
            result['endpoint_public_access'] = self.endpoint_public_access

        if self.extra_sans is not None:
            result['extra_sans'] = self.extra_sans

        if self.format_disk is not None:
            result['format_disk'] = self.format_disk

        if self.image_id is not None:
            result['image_id'] = self.image_id

        if self.image_type is not None:
            result['image_type'] = self.image_type

        if self.instances is not None:
            result['instances'] = self.instances

        if self.ip_stack is not None:
            result['ip_stack'] = self.ip_stack

        if self.is_enterprise_security_group is not None:
            result['is_enterprise_security_group'] = self.is_enterprise_security_group

        if self.keep_instance_name is not None:
            result['keep_instance_name'] = self.keep_instance_name

        if self.key_pair is not None:
            result['key_pair'] = self.key_pair

        if self.kubernetes_version is not None:
            result['kubernetes_version'] = self.kubernetes_version

        if self.load_balancer_id is not None:
            result['load_balancer_id'] = self.load_balancer_id

        if self.load_balancer_spec is not None:
            result['load_balancer_spec'] = self.load_balancer_spec

        if self.logging_type is not None:
            result['logging_type'] = self.logging_type

        if self.login_password is not None:
            result['login_password'] = self.login_password

        if self.maintenance_window is not None:
            result['maintenance_window'] = self.maintenance_window.to_map()

        if self.master_auto_renew is not None:
            result['master_auto_renew'] = self.master_auto_renew

        if self.master_auto_renew_period is not None:
            result['master_auto_renew_period'] = self.master_auto_renew_period

        if self.master_count is not None:
            result['master_count'] = self.master_count

        if self.master_instance_charge_type is not None:
            result['master_instance_charge_type'] = self.master_instance_charge_type

        if self.master_instance_types is not None:
            result['master_instance_types'] = self.master_instance_types

        if self.master_period is not None:
            result['master_period'] = self.master_period

        if self.master_period_unit is not None:
            result['master_period_unit'] = self.master_period_unit

        if self.master_system_disk_category is not None:
            result['master_system_disk_category'] = self.master_system_disk_category

        if self.master_system_disk_performance_level is not None:
            result['master_system_disk_performance_level'] = self.master_system_disk_performance_level

        if self.master_system_disk_size is not None:
            result['master_system_disk_size'] = self.master_system_disk_size

        if self.master_system_disk_snapshot_policy_id is not None:
            result['master_system_disk_snapshot_policy_id'] = self.master_system_disk_snapshot_policy_id

        if self.master_vswitch_ids is not None:
            result['master_vswitch_ids'] = self.master_vswitch_ids

        if self.name is not None:
            result['name'] = self.name

        if self.nat_gateway is not None:
            result['nat_gateway'] = self.nat_gateway

        if self.node_cidr_mask is not None:
            result['node_cidr_mask'] = self.node_cidr_mask

        if self.node_name_mode is not None:
            result['node_name_mode'] = self.node_name_mode

        if self.node_port_range is not None:
            result['node_port_range'] = self.node_port_range

        result['nodepools'] = []
        if self.nodepools is not None:
            for k1 in self.nodepools:
                result['nodepools'].append(k1.to_map() if k1 else None)

        if self.num_of_nodes is not None:
            result['num_of_nodes'] = self.num_of_nodes

        if self.operation_policy is not None:
            result['operation_policy'] = self.operation_policy.to_map()

        if self.os_type is not None:
            result['os_type'] = self.os_type

        if self.period is not None:
            result['period'] = self.period

        if self.period_unit is not None:
            result['period_unit'] = self.period_unit

        if self.platform is not None:
            result['platform'] = self.platform

        if self.pod_vswitch_ids is not None:
            result['pod_vswitch_ids'] = self.pod_vswitch_ids

        if self.profile is not None:
            result['profile'] = self.profile

        if self.proxy_mode is not None:
            result['proxy_mode'] = self.proxy_mode

        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances

        if self.region_id is not None:
            result['region_id'] = self.region_id

        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id

        if self.rrsa_config is not None:
            result['rrsa_config'] = self.rrsa_config.to_map()

        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()

        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id

        if self.security_hardening_os is not None:
            result['security_hardening_os'] = self.security_hardening_os

        if self.service_account_issuer is not None:
            result['service_account_issuer'] = self.service_account_issuer

        if self.service_cidr is not None:
            result['service_cidr'] = self.service_cidr

        if self.service_discovery_types is not None:
            result['service_discovery_types'] = self.service_discovery_types

        if self.snat_entry is not None:
            result['snat_entry'] = self.snat_entry

        if self.soc_enabled is not None:
            result['soc_enabled'] = self.soc_enabled

        if self.ssh_flags is not None:
            result['ssh_flags'] = self.ssh_flags

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        result['taints'] = []
        if self.taints is not None:
            for k1 in self.taints:
                result['taints'].append(k1.to_map() if k1 else None)

        if self.timeout_mins is not None:
            result['timeout_mins'] = self.timeout_mins

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.user_ca is not None:
            result['user_ca'] = self.user_ca

        if self.user_data is not None:
            result['user_data'] = self.user_data

        if self.vpcid is not None:
            result['vpcid'] = self.vpcid

        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids

        if self.worker_auto_renew is not None:
            result['worker_auto_renew'] = self.worker_auto_renew

        if self.worker_auto_renew_period is not None:
            result['worker_auto_renew_period'] = self.worker_auto_renew_period

        result['worker_data_disks'] = []
        if self.worker_data_disks is not None:
            for k1 in self.worker_data_disks:
                result['worker_data_disks'].append(k1.to_map() if k1 else None)

        if self.worker_instance_charge_type is not None:
            result['worker_instance_charge_type'] = self.worker_instance_charge_type

        if self.worker_instance_types is not None:
            result['worker_instance_types'] = self.worker_instance_types

        if self.worker_period is not None:
            result['worker_period'] = self.worker_period

        if self.worker_period_unit is not None:
            result['worker_period_unit'] = self.worker_period_unit

        if self.worker_system_disk_category is not None:
            result['worker_system_disk_category'] = self.worker_system_disk_category

        if self.worker_system_disk_performance_level is not None:
            result['worker_system_disk_performance_level'] = self.worker_system_disk_performance_level

        if self.worker_system_disk_size is not None:
            result['worker_system_disk_size'] = self.worker_system_disk_size

        if self.worker_system_disk_snapshot_policy_id is not None:
            result['worker_system_disk_snapshot_policy_id'] = self.worker_system_disk_snapshot_policy_id

        if self.worker_vswitch_ids is not None:
            result['worker_vswitch_ids'] = self.worker_vswitch_ids

        if self.zone_id is not None:
            result['zone_id'] = self.zone_id

        if self.zone_ids is not None:
            result['zone_ids'] = self.zone_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_control_list') is not None:
            self.access_control_list = m.get('access_control_list')

        self.addons = []
        if m.get('addons') is not None:
            for k1 in m.get('addons'):
                temp_model = main_models.Addon()
                self.addons.append(temp_model.from_map(k1))

        if m.get('api_audiences') is not None:
            self.api_audiences = m.get('api_audiences')

        if m.get('audit_log_config') is not None:
            temp_model = main_models.CreateClusterRequestAuditLogConfig()
            self.audit_log_config = temp_model.from_map(m.get('audit_log_config'))

        if m.get('auto_mode') is not None:
            temp_model = main_models.CreateClusterRequestAutoMode()
            self.auto_mode = temp_model.from_map(m.get('auto_mode'))

        if m.get('auto_renew') is not None:
            self.auto_renew = m.get('auto_renew')

        if m.get('auto_renew_period') is not None:
            self.auto_renew_period = m.get('auto_renew_period')

        if m.get('charge_type') is not None:
            self.charge_type = m.get('charge_type')

        if m.get('cis_enabled') is not None:
            self.cis_enabled = m.get('cis_enabled')

        if m.get('cloud_monitor_flags') is not None:
            self.cloud_monitor_flags = m.get('cloud_monitor_flags')

        if m.get('cluster_domain') is not None:
            self.cluster_domain = m.get('cluster_domain')

        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')

        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')

        if m.get('container_cidr') is not None:
            self.container_cidr = m.get('container_cidr')

        if m.get('control_plane_config') is not None:
            temp_model = main_models.CreateClusterRequestControlPlaneConfig()
            self.control_plane_config = temp_model.from_map(m.get('control_plane_config'))

        if m.get('control_plane_endpoints_config') is not None:
            temp_model = main_models.CreateClusterRequestControlPlaneEndpointsConfig()
            self.control_plane_endpoints_config = temp_model.from_map(m.get('control_plane_endpoints_config'))

        if m.get('controlplane_log_components') is not None:
            self.controlplane_log_components = m.get('controlplane_log_components')

        if m.get('controlplane_log_project') is not None:
            self.controlplane_log_project = m.get('controlplane_log_project')

        if m.get('controlplane_log_ttl') is not None:
            self.controlplane_log_ttl = m.get('controlplane_log_ttl')

        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')

        if m.get('custom_san') is not None:
            self.custom_san = m.get('custom_san')

        if m.get('deletion_protection') is not None:
            self.deletion_protection = m.get('deletion_protection')

        if m.get('disable_rollback') is not None:
            self.disable_rollback = m.get('disable_rollback')

        if m.get('enable_rrsa') is not None:
            self.enable_rrsa = m.get('enable_rrsa')

        if m.get('encryption_provider_key') is not None:
            self.encryption_provider_key = m.get('encryption_provider_key')

        if m.get('endpoint_public_access') is not None:
            self.endpoint_public_access = m.get('endpoint_public_access')

        if m.get('extra_sans') is not None:
            self.extra_sans = m.get('extra_sans')

        if m.get('format_disk') is not None:
            self.format_disk = m.get('format_disk')

        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')

        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')

        if m.get('instances') is not None:
            self.instances = m.get('instances')

        if m.get('ip_stack') is not None:
            self.ip_stack = m.get('ip_stack')

        if m.get('is_enterprise_security_group') is not None:
            self.is_enterprise_security_group = m.get('is_enterprise_security_group')

        if m.get('keep_instance_name') is not None:
            self.keep_instance_name = m.get('keep_instance_name')

        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')

        if m.get('kubernetes_version') is not None:
            self.kubernetes_version = m.get('kubernetes_version')

        if m.get('load_balancer_id') is not None:
            self.load_balancer_id = m.get('load_balancer_id')

        if m.get('load_balancer_spec') is not None:
            self.load_balancer_spec = m.get('load_balancer_spec')

        if m.get('logging_type') is not None:
            self.logging_type = m.get('logging_type')

        if m.get('login_password') is not None:
            self.login_password = m.get('login_password')

        if m.get('maintenance_window') is not None:
            temp_model = main_models.MaintenanceWindow()
            self.maintenance_window = temp_model.from_map(m.get('maintenance_window'))

        if m.get('master_auto_renew') is not None:
            self.master_auto_renew = m.get('master_auto_renew')

        if m.get('master_auto_renew_period') is not None:
            self.master_auto_renew_period = m.get('master_auto_renew_period')

        if m.get('master_count') is not None:
            self.master_count = m.get('master_count')

        if m.get('master_instance_charge_type') is not None:
            self.master_instance_charge_type = m.get('master_instance_charge_type')

        if m.get('master_instance_types') is not None:
            self.master_instance_types = m.get('master_instance_types')

        if m.get('master_period') is not None:
            self.master_period = m.get('master_period')

        if m.get('master_period_unit') is not None:
            self.master_period_unit = m.get('master_period_unit')

        if m.get('master_system_disk_category') is not None:
            self.master_system_disk_category = m.get('master_system_disk_category')

        if m.get('master_system_disk_performance_level') is not None:
            self.master_system_disk_performance_level = m.get('master_system_disk_performance_level')

        if m.get('master_system_disk_size') is not None:
            self.master_system_disk_size = m.get('master_system_disk_size')

        if m.get('master_system_disk_snapshot_policy_id') is not None:
            self.master_system_disk_snapshot_policy_id = m.get('master_system_disk_snapshot_policy_id')

        if m.get('master_vswitch_ids') is not None:
            self.master_vswitch_ids = m.get('master_vswitch_ids')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nat_gateway') is not None:
            self.nat_gateway = m.get('nat_gateway')

        if m.get('node_cidr_mask') is not None:
            self.node_cidr_mask = m.get('node_cidr_mask')

        if m.get('node_name_mode') is not None:
            self.node_name_mode = m.get('node_name_mode')

        if m.get('node_port_range') is not None:
            self.node_port_range = m.get('node_port_range')

        self.nodepools = []
        if m.get('nodepools') is not None:
            for k1 in m.get('nodepools'):
                temp_model = main_models.Nodepool()
                self.nodepools.append(temp_model.from_map(k1))

        if m.get('num_of_nodes') is not None:
            self.num_of_nodes = m.get('num_of_nodes')

        if m.get('operation_policy') is not None:
            temp_model = main_models.CreateClusterRequestOperationPolicy()
            self.operation_policy = temp_model.from_map(m.get('operation_policy'))

        if m.get('os_type') is not None:
            self.os_type = m.get('os_type')

        if m.get('period') is not None:
            self.period = m.get('period')

        if m.get('period_unit') is not None:
            self.period_unit = m.get('period_unit')

        if m.get('platform') is not None:
            self.platform = m.get('platform')

        if m.get('pod_vswitch_ids') is not None:
            self.pod_vswitch_ids = m.get('pod_vswitch_ids')

        if m.get('profile') is not None:
            self.profile = m.get('profile')

        if m.get('proxy_mode') is not None:
            self.proxy_mode = m.get('proxy_mode')

        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')

        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')

        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')

        if m.get('rrsa_config') is not None:
            temp_model = main_models.CreateClusterRequestRrsaConfig()
            self.rrsa_config = temp_model.from_map(m.get('rrsa_config'))

        if m.get('runtime') is not None:
            temp_model = main_models.Runtime()
            self.runtime = temp_model.from_map(m.get('runtime'))

        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')

        if m.get('security_hardening_os') is not None:
            self.security_hardening_os = m.get('security_hardening_os')

        if m.get('service_account_issuer') is not None:
            self.service_account_issuer = m.get('service_account_issuer')

        if m.get('service_cidr') is not None:
            self.service_cidr = m.get('service_cidr')

        if m.get('service_discovery_types') is not None:
            self.service_discovery_types = m.get('service_discovery_types')

        if m.get('snat_entry') is not None:
            self.snat_entry = m.get('snat_entry')

        if m.get('soc_enabled') is not None:
            self.soc_enabled = m.get('soc_enabled')

        if m.get('ssh_flags') is not None:
            self.ssh_flags = m.get('ssh_flags')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        self.taints = []
        if m.get('taints') is not None:
            for k1 in m.get('taints'):
                temp_model = main_models.Taint()
                self.taints.append(temp_model.from_map(k1))

        if m.get('timeout_mins') is not None:
            self.timeout_mins = m.get('timeout_mins')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('user_ca') is not None:
            self.user_ca = m.get('user_ca')

        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')

        if m.get('vpcid') is not None:
            self.vpcid = m.get('vpcid')

        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')

        if m.get('worker_auto_renew') is not None:
            self.worker_auto_renew = m.get('worker_auto_renew')

        if m.get('worker_auto_renew_period') is not None:
            self.worker_auto_renew_period = m.get('worker_auto_renew_period')

        self.worker_data_disks = []
        if m.get('worker_data_disks') is not None:
            for k1 in m.get('worker_data_disks'):
                temp_model = main_models.CreateClusterRequestWorkerDataDisks()
                self.worker_data_disks.append(temp_model.from_map(k1))

        if m.get('worker_instance_charge_type') is not None:
            self.worker_instance_charge_type = m.get('worker_instance_charge_type')

        if m.get('worker_instance_types') is not None:
            self.worker_instance_types = m.get('worker_instance_types')

        if m.get('worker_period') is not None:
            self.worker_period = m.get('worker_period')

        if m.get('worker_period_unit') is not None:
            self.worker_period_unit = m.get('worker_period_unit')

        if m.get('worker_system_disk_category') is not None:
            self.worker_system_disk_category = m.get('worker_system_disk_category')

        if m.get('worker_system_disk_performance_level') is not None:
            self.worker_system_disk_performance_level = m.get('worker_system_disk_performance_level')

        if m.get('worker_system_disk_size') is not None:
            self.worker_system_disk_size = m.get('worker_system_disk_size')

        if m.get('worker_system_disk_snapshot_policy_id') is not None:
            self.worker_system_disk_snapshot_policy_id = m.get('worker_system_disk_snapshot_policy_id')

        if m.get('worker_vswitch_ids') is not None:
            self.worker_vswitch_ids = m.get('worker_vswitch_ids')

        if m.get('zone_id') is not None:
            self.zone_id = m.get('zone_id')

        if m.get('zone_ids') is not None:
            self.zone_ids = m.get('zone_ids')

        return self

class CreateClusterRequestWorkerDataDisks(DaraModel):
    def __init__(
        self,
        category: str = None,
        encrypted: str = None,
        performance_level: str = None,
        size: str = None,
    ):
        # The type of the data disk.
        # 
        # This parameter is required.
        self.category = category
        # Specifies whether to encrypt the data disk. Valid values:
        self.encrypted = encrypted
        # The performance level of the data cloud disk for nodes. This parameter takes effect only for [standard SSDs](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The size of the data disk. Valid values: 40 to 32767. Unit: GiB.
        # 
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.encrypted is not None:
            result['encrypted'] = self.encrypted

        if self.performance_level is not None:
            result['performance_level'] = self.performance_level

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')

        if m.get('performance_level') is not None:
            self.performance_level = m.get('performance_level')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

class CreateClusterRequestRrsaConfig(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        # Specifies whether to enable the RRSA feature.
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        return self

class CreateClusterRequestOperationPolicy(DaraModel):
    def __init__(
        self,
        cluster_auto_upgrade: main_models.CreateClusterRequestOperationPolicyClusterAutoUpgrade = None,
    ):
        # The cluster auto-upgrade configuration.
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
            temp_model = main_models.CreateClusterRequestOperationPolicyClusterAutoUpgrade()
            self.cluster_auto_upgrade = temp_model.from_map(m.get('cluster_auto_upgrade'))

        return self

class CreateClusterRequestOperationPolicyClusterAutoUpgrade(DaraModel):
    def __init__(
        self,
        channel: str = None,
        enabled: bool = None,
    ):
        # The cluster auto-upgrade frequency. Valid values:
        self.channel = channel
        # Specifies whether to enable cluster auto-upgrade.
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

class CreateClusterRequestControlPlaneEndpointsConfig(DaraModel):
    def __init__(
        self,
        internal_dns_config: main_models.CreateClusterRequestControlPlaneEndpointsConfigInternalDnsConfig = None,
        load_balancers_config: List[main_models.CreateClusterRequestControlPlaneEndpointsConfigLoadBalancersConfig] = None,
    ):
        # The internal DNS configuration of the cluster. This applies to ACK managed clusters. The internal domain name is used by node-side system components such as kubelet and kube-proxy to access the API Server. If the internal domain name access is not enabled, node-side system components access the API Server through the CLB IP address.
        self.internal_dns_config = internal_dns_config
        # The cluster connection configuration. When this field is specified, the endpoint_public_access and load_balancer_id parameters do not take effect.
        self.load_balancers_config = load_balancers_config

    def validate(self):
        if self.internal_dns_config:
            self.internal_dns_config.validate()
        if self.load_balancers_config:
            for v1 in self.load_balancers_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internal_dns_config is not None:
            result['internal_dns_config'] = self.internal_dns_config.to_map()

        result['load_balancers_config'] = []
        if self.load_balancers_config is not None:
            for k1 in self.load_balancers_config:
                result['load_balancers_config'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('internal_dns_config') is not None:
            temp_model = main_models.CreateClusterRequestControlPlaneEndpointsConfigInternalDnsConfig()
            self.internal_dns_config = temp_model.from_map(m.get('internal_dns_config'))

        self.load_balancers_config = []
        if m.get('load_balancers_config') is not None:
            for k1 in m.get('load_balancers_config'):
                temp_model = main_models.CreateClusterRequestControlPlaneEndpointsConfigLoadBalancersConfig()
                self.load_balancers_config.append(temp_model.from_map(k1))

        return self

class CreateClusterRequestControlPlaneEndpointsConfigLoadBalancersConfig(DaraModel):
    def __init__(
        self,
        endpoint_type: str = None,
        load_balancer_id: str = None,
    ):
        # The endpoint type.
        self.endpoint_type = endpoint_type
        # The NLB instance ID.
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_type is not None:
            result['endpoint_type'] = self.endpoint_type

        if self.load_balancer_id is not None:
            result['load_balancer_id'] = self.load_balancer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint_type') is not None:
            self.endpoint_type = m.get('endpoint_type')

        if m.get('load_balancer_id') is not None:
            self.load_balancer_id = m.get('load_balancer_id')

        return self

class CreateClusterRequestControlPlaneEndpointsConfigInternalDnsConfig(DaraModel):
    def __init__(
        self,
        bind_vpcs: List[str] = None,
    ):
        # The VPCs in which the internal domain name DNS resolution takes effect.
        self.bind_vpcs = bind_vpcs

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_vpcs is not None:
            result['bind_vpcs'] = self.bind_vpcs

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bind_vpcs') is not None:
            self.bind_vpcs = m.get('bind_vpcs')

        return self

class CreateClusterRequestControlPlaneConfig(DaraModel):
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
        # Specifies whether to enable auto-renewal for control plane nodes. This parameter is valid only when charge_type is set to `PrePaid`.
        self.auto_renew = auto_renew
        # The auto-renewal duration of control plane nodes.
        self.auto_renew_period = auto_renew_period
        # The billing method of control plane nodes.
        self.charge_type = charge_type
        # Specifies whether to install CloudMonitor on nodes.
        self.cloud_monitor_flags = cloud_monitor_flags
        # The CPU management policy for nodes.
        self.cpu_policy = cpu_policy
        # The deployment set ID.
        self.deploymentset_id = deploymentset_id
        # The image ID.
        self.image_id = image_id
        # The operating system image type.
        self.image_type = image_type
        # The instance metadata access configuration for ECS instances.
        self.instance_metadata_options = instance_metadata_options
        # The instance types of nodes.
        self.instance_types = instance_types
        # The name of the key pair. Specify either this parameter or login_password.
        self.key_pair = key_pair
        # The SSH logon password. The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Specify either this parameter or key_pair.
        self.login_password = login_password
        # **[Deprecated]** The node service port range.
        self.node_port_range = node_port_range
        # The subscription duration of control plane nodes. This parameter is valid and required only when charge_type is set to `PrePaid`.
        self.period = period
        # The unit of the subscription duration of control plane nodes. This parameter is valid and required only when charge_type is set to `PrePaid`.
        self.period_unit = period_unit
        # **[Deprecated]** The runtime name of control plane nodes. Valid values:
        self.runtime = runtime
        # Specifies whether to enable Alibaba Cloud OS security hardening.
        self.security_hardening_os = security_hardening_os
        # The number of control plane nodes.
        self.size = size
        # Specifies whether to enable MLPS security hardening.
        self.soc_enabled = soc_enabled
        # Specifies whether to enable burst (performance burst) for the system cloud disk of nodes.
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The type of the system cloud disk for nodes.
        self.system_disk_category = system_disk_category
        # The performance level of the system cloud disk. This parameter takes effect only for ESSD disks.
        self.system_disk_performance_level = system_disk_performance_level
        # The provisioned read/write IOPS of the system cloud disk for nodes.
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The size of the system cloud disk for nodes.
        self.system_disk_size = system_disk_size
        # The automatic snapshot policy for nodes.
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

        if m.get('instance_metadata_options') is not None:
            temp_model = main_models.InstanceMetadataOptions()
            self.instance_metadata_options = temp_model.from_map(m.get('instance_metadata_options'))

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

class CreateClusterRequestAutoMode(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        # Specifies whether to enable intelligent managed mode.
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

class CreateClusterRequestAuditLogConfig(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        sls_project_name: str = None,
    ):
        # Specifies whether to enable the cluster audit log feature.
        self.enabled = enabled
        # The [Simple Log Service project](https://help.aliyun.com/document_detail/48873.html) that contains the [Logstore](https://help.aliyun.com/document_detail/48873.html) for cluster audit logs.
        self.sls_project_name = sls_project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.sls_project_name is not None:
            result['sls_project_name'] = self.sls_project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('sls_project_name') is not None:
            self.sls_project_name = m.get('sls_project_name')

        return self

