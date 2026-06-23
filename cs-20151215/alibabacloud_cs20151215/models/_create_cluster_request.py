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
        # [**This field is deprecated**] Registered cluster API Server SLB access control list.
        self.access_control_list = access_control_list
        # List of cluster components. Specify the components to install when creating a cluster through `addons`.
        # 
        # **Network component**: Required. Choose between Flannel and Terway network types when creating a cluster:
        # 
        # - Flannel network: [{"name":"flannel","config":""}].
        # - Terway network: [{"name": "terway-eniip","config": ""}] .
        # 
        # **Storage component**: Optional. Only the `csi` type is supported:
        # 
        # `csi`: [{"name":"csi-plugin","config": ""},{"name": "csi-provisioner","config": ""}].
        # 
        # **Log component**: Optional. Recommended to enable. If Log Service is not enabled, the cluster audit feature will be unavailable.
        # 
        # - Use an existing `SLS Project`: [{"name": "loongcollector","config": "{\\"IngressDashboardEnabled\\":\\"true\\",\\"sls_project_name\\":\\"your_sls_project_name\\"}"}] .
        # - Create a new `SLS Project`: [{"name": "loongcollector","config": "{\\"IngressDashboardEnabled\\":\\"true\\"}"}] .
        # 
        # **Ingress component**: Optional. ACK dedicated clusters install the Ingress component `nginx-ingress-controller` by default.
        # 
        # - Install Ingress with public network access: [{"name":"nginx-ingress-controller","config":"{\\"IngressSlbNetworkType\\":\\"internet\\"}"}] .
        # - Disable default Ingress installation: [{"name": "nginx-ingress-controller","config": "","disabled": true}] .
        # 
        # **Event center**: Optional. Enabled by default.
        # 
        # The event center provides capabilities for storing, querying, and alerting on Kubernetes events. The Logstore associated with the Kubernetes event center is free for 90 days. For more information about the free policy, see [Create and use the Kubernetes event center](https://help.aliyun.com/document_detail/150476.html).
        # 
        # Example of enabling the event center: [{"name":"ack-node-problem-detector","config":"{\\"sls_project_name\\":\\"your_sls_project_name\\"}"}].
        self.addons = addons
        # ServiceAccount is the access credential for communication between Pods and the cluster API Server. `api-audiences` defines the valid request `token` identities used by the `apiserver` to verify whether the request `token` is legitimate. Multiple `audience` values can be configured, separated by commas (,).
        # 
        # For more details about `ServiceAccount`, see [Deploy service account token volume projection](https://help.aliyun.com/document_detail/160384.html).
        self.api_audiences = api_audiences
        # Cluster audit log configuration.
        self.audit_log_config = audit_log_config
        # [Intelligent managed mode](https://help.aliyun.com/document_detail/2938898.html) configuration.
        self.auto_mode = auto_mode
        # [**This field is deprecated**]
        # 
        # Whether to enable auto-renewal. Only takes effect when `charge_type` is set to `PrePaid`. Valid values:
        # 
        # - `true`: Enable auto-renewal.
        # - `false`: Disable auto-renewal.
        # 
        # Default value: `false`.
        # 
        # This field was changed on October 15, 2024. For more information, see [Announcement on CreateCluster API parameter behavior changes](https://help.aliyun.com/document_detail/2849194.html).
        self.auto_renew = auto_renew
        # [**This field is deprecated**]
        # 
        # Auto-renewal period. Only takes effect when subscription and auto-renewal are selected. When `PeriodUnit=Month`, valid values: {1, 2, 3, 6, 12}.
        # 
        # Default value: 1.
        # 
        # This field was changed on October 15, 2024. For more information, see [Announcement on CreateCluster API parameter behavior changes](https://help.aliyun.com/document_detail/2849194.html).
        self.auto_renew_period = auto_renew_period
        # [**This field is deprecated**]
        # 
        # Billing type of the CLB instance used by the API Server. Default value: PostPaid. Valid values:
        # - PostPaid: Pay-as-you-go.
        # - PrePaid: Subscription. This billing type is no longer supported for newly created CLB instances. Existing instances are not affected.
        # 
        # >Notice: 
        # 
        # - This field was changed on October 15, 2024. For more information, see [Announcement on CreateCluster API parameter behavior changes](https://help.aliyun.com/document_detail/2849194.html).
        # - Starting from December 1, 2024, newly created CLB instances no longer support the subscription billing type, and instance fees will be charged.
        # </notice>
        # <props="china">For details, see [Product announcement on canceling subscription billing for cluster API Server CLB](https://help.aliyun.com/document_detail/2851191.html) and [CLB billing adjustment announcement](https://help.aliyun.com/document_detail/2839797.html).
        # <props="intl">For details, see [CLB billing adjustment announcement](https://help.aliyun.com/document_detail/2839797.html).
        self.charge_type = charge_type
        # [**This field is deprecated**] For cluster control plane configuration, use the `security_hardening_os` parameter under `control_plane_config` instead. For node pool configuration, use the `security_hardening_os` parameter under `scaling_group` in `nodepool` instead.
        self.cis_enabled = cis_enabled
        # [**This field is deprecated**] For cluster control plane node configuration, use the `cloud_monitor_flags` parameter under `control_plane_config` instead. For node pool configuration, use the `cms_enabled` parameter under `kubernetes_config` in `nodepool` instead.
        # 
        # Whether to install the CloudMonitor agent in the cluster. Valid values:
        # 
        # - `true`: Install the CloudMonitor agent.
        # - `false`: Do not install the CloudMonitor agent.
        # 
        # Default value: `false`.
        self.cloud_monitor_flags = cloud_monitor_flags
        # Cluster local domain name.
        # 
        # Naming rules: The domain name consists of one or more parts separated by periods (.). Each part can be up to 63 characters long and can contain lowercase letters, digits, and hyphens (-). Each part must start and end with a lowercase letter or digit.
        self.cluster_domain = cluster_domain
        # After selecting `cluster_type` as `ManagedKubernetes` and configuring `profile`, you can further specify the cluster specification. Valid values:
        # 
        # - `ack.standard`: Basic edition (selected by default when the value is empty)
        # - `ack.pro.small`: Pro edition
        # - `ack.pro.xlarge`: Pro XL
        # - `ack.pro.2xlarge`: Pro 2XL
        # - `ack.pro.4xlarge`: Pro 4XL (requires contacting customer service to enable allowlisting)
        # 
        # Pro XL, Pro 2XL, and Pro 4XL are three tiers provided by <props="china">[ACK Pro Provisioned Control Plane](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane)<props="intl">[ACK Pro Provisioned Control Plane](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane). They pre-allocate and fix control plane resources to ensure that API concurrency and Pod scheduling capabilities always remain at a determined high level, suitable for AI training and inference, ultra-large-scale clusters, and mission-critical workloads.
        # 
        # For the cluster management fees of Pro edition and provisioned control plane editions, see <props="china">[Cluster management fees](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee)<props="intl">[Cluster management fees](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee).
        self.cluster_spec = cluster_spec
        # - `Kubernetes`: ACK dedicated cluster.
        # - `ManagedKubernetes`: ACK managed cluster types, including ACK managed cluster (Pro and Basic editions), ACK Serverless cluster (Pro and Basic editions), ACK Edge cluster (Pro and Basic editions), and ACK Lingjun cluster (Pro edition).
        # - `ExternalKubernetes`: Registered cluster.
        self.cluster_type = cluster_type
        # Pod network CIDR block. Must be a valid private CIDR block, specifically the following CIDR blocks and their subnets: 10.0.0.0/8, 172.16-31.0.0/12-16, 192.168.0.0/16. Cannot overlap with the VPC or CIDR blocks used by existing Kubernetes clusters in the VPC. Cannot be modified after creation.
        # 
        # For cluster network planning, see [ACK managed cluster network planning](https://help.aliyun.com/document_detail/86500.html).
        # 
        # > This field is required for Flannel clusters.
        self.container_cidr = container_cidr
        # ACK dedicated cluster control plane configuration.
        self.control_plane_config = control_plane_config
        # Cluster connection configuration.
        self.control_plane_endpoints_config = control_plane_endpoints_config
        # List of component names, specifying which control plane components\\" logs to collect.
        # 
        # By default, logs are collected from kube-apiserver, kube-controller-manager, kube-scheduler, and cloud-controller-manager.
        self.controlplane_log_components = controlplane_log_components
        # Log Service project for control plane component logs. You can use an existing project for log storage or let the system automatically create a project. If you choose to auto-create a Log Service project, a project named `k8s-log-{ClusterID}` will be automatically created.
        self.controlplane_log_project = controlplane_log_project
        # Number of days to retain control plane component logs.
        self.controlplane_log_ttl = controlplane_log_ttl
        # [**This field is deprecated**] For cluster control plane configuration, use the `cpu_policy` parameter under `control_plane_config` instead. For node pool configuration, use the `cpu_policy` parameter under `kubernetes_config` in `nodepool` instead.
        # 
        # Node CPU management policy. The following two policies are supported when the cluster version is 1.12.6 or later:
        # 
        # - `static`: Allows enhancing CPU affinity and exclusivity for Pods with certain resource characteristics on the node.
        # - `none`: Enables the existing default CPU affinity scheme.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # [**This field is deprecated**] Use the `extra_sans` parameter instead.
        # 
        # Custom certificate SAN. Multiple IPs or domain names are separated by commas (,).
        self.custom_san = custom_san
        # Cluster deletion protection, which prevents accidental cluster deletion through the console or API. Valid values:
        # 
        # - `true`: Enable cluster deletion protection. The cluster cannot be deleted through the console or API.
        # - `false`: Disable cluster deletion protection. The cluster can be deleted through the console or API.
        # 
        # Default value: `false`.
        self.deletion_protection = deletion_protection
        # [**This field is deprecated**] By default, no rollback is performed when cluster creation fails. You need to clean up the failed cluster yourself.
        # 
        # Whether to roll back when cluster creation fails. Valid values:
        # 
        # - `true`: Roll back when cluster creation fails.
        # - `false`: Do not roll back when cluster creation fails.
        # 
        # 
        # Default value: `true`.
        self.disable_rollback = disable_rollback
        # [**This field is deprecated**] Use the `rrsa_config` parameter instead.
        # 
        # Whether to enable the RRSA feature.
        # 
        # - true: Enable.
        # 
        # - false: Disable.
        self.enable_rrsa = enable_rrsa
        # KMS key ID. This key is used to encrypt data disks. For more details, see [Key Management Service](https://help.aliyun.com/document_detail/28935.html).
        # 
        # > This feature only takes effect in professional managed clusters (ACK Pro clusters).
        self.encryption_provider_key = encryption_provider_key
        # Whether to enable public access. Expose the API Server through an EIP to enable public access to the cluster.
        # 
        # - `true`: Enable public access.
        # - `false`: Disable public access. When disabled, the cluster API Server cannot be accessed from the Internet.
        # 
        # Default value: `false`.
        self.endpoint_public_access = endpoint_public_access
        # Custom API Server certificate SAN (Subject Alternative Name).
        self.extra_sans = extra_sans
        # [**This field is deprecated**] Selecting existing nodes when creating a cluster is no longer supported. To add existing nodes to a cluster, create a node pool first and call the [AttachInstancesToNodePool](https://help.aliyun.com/document_detail/2667920.html) API.
        # 
        # Whether to mount data disks on instances when creating a cluster with existing instances. Valid values:
        # 
        # - `true`: Store containers and images on the data disk. Existing data on the data disk will be lost. Please back up your data.
        # 
        # - `false`: Do not store containers and images on the data disk.
        # 
        # Default value: `false`.
        # 
        # Data disk mounting rules:
        # 
        # - If the ECS instance already has data disks mounted and the file system of the last data disk is not initialized, the system will automatically format the data disk as ext4 to store /var/lib/docker and /var/lib/kubelet.
        # - If the ECS instance has no data disks mounted, no new data disk will be mounted.
        self.format_disk = format_disk
        # [**This field is deprecated**] For cluster control plane configuration, use the `image_id` parameter under `control_plane_config` instead. For node pool configuration, use the `image_id` parameter under `scaling_group` in `nodepool` instead.
        # 
        # Custom node image. The system image is used by default. When a custom image is selected, it replaces the default system image. See [Custom images](https://help.aliyun.com/document_detail/146647.html).
        self.image_id = image_id
        # [**This field is deprecated**] For cluster control plane configuration, use the `image_type` parameter under `control_plane_config` instead. For node pool configuration, use the `image_type` parameter under `scaling_group` in `nodepool` instead.
        # 
        # OS distribution type. It is recommended to use this field to specify the node OS. Valid values:
        # 
        # - CentOS
        # - AliyunLinux
        # - AliyunLinux Qboot
        # - AliyunLinuxUEFI
        # - AliyunLinux3
        # - Windows
        # - WindowsCore
        # - AliyunLinux3Arm64
        # - ContainerOS
        # 
        # Default value: `CentOS`.
        self.image_type = image_type
        # [**This field is deprecated**] Selecting existing nodes when creating a cluster is no longer supported. To add existing nodes to a cluster, create a node pool first and call the [AttachInstancesToNodePool](https://help.aliyun.com/document_detail/2667920.html) API.
        # 
        # 
        # When creating a cluster with existing nodes, you need to specify a list of ECS instances. These instances will join the cluster as Worker nodes.
        # 
        # > This field is required when creating a cluster with existing instances.
        self.instances = instances
        # Cluster IP stack.
        self.ip_stack = ip_stack
        # Automatically create an enterprise security group. Takes effect when `security_group_id` is empty.
        # 
        # > When using a basic security group, the total number of nodes and Terway Pods in the cluster cannot exceed 2000. Therefore, when creating a Terway network type cluster, it is recommended to use an enterprise security group.
        # 
        # - `true`: Create and use an enterprise security group.
        # - `false`: Use a basic security group.
        # 
        # Default value: `true`.
        self.is_enterprise_security_group = is_enterprise_security_group
        # [**This field is deprecated**] Selecting existing nodes when creating a cluster is no longer supported. To add existing nodes to a cluster, create a node pool first and call the [AttachInstancesToNodePool](https://help.aliyun.com/document_detail/2667920.html) API.
        # 
        # Whether to retain instance names when creating a cluster with existing instances.
        # 
        # - `true`: Retain.
        # - `false`: Do not retain. Names will be replaced using system rules.
        # 
        # Default value: `true`.
        self.keep_instance_name = keep_instance_name
        # [**This field is deprecated**] For cluster control plane configuration, use the `key_pair` parameter under `control_plane_config` instead. For node pool configuration, use the `key_pair` parameter under `scaling_group` in `nodepool` instead.
        # 
        # Key pair name. Mutually exclusive with `login_password`.
        self.key_pair = key_pair
        # Cluster version, consistent with the Kubernetes community baseline version. We recommend selecting the latest version. If not specified, the latest version is used by default.
        # 
        # You can create clusters of the three most recent versions. You can query supported cluster versions through the [DescribeKubernetesVersionMetadata](https://help.aliyun.com/document_detail/2667899.html) API.
        # 
        # For Kubernetes versions supported by ACK, see [Kubernetes version release overview](https://help.aliyun.com/document_detail/185269.html).
        self.kubernetes_version = kubernetes_version
        # Specify the CLB instance ID for API Server access. When this parameter is specified, an API Server CLB will not be automatically created.
        # > Ensure that the CLB instance has no other dependencies (such as listeners or backend servers). Shared and public-network CLB instances are not supported.
        self.load_balancer_id = load_balancer_id
        # [**This parameter is deprecated**] CLB is billed by usage. This parameter does not take effect.
        # 
        # Load balancer specification. Valid values:
        # - slb.s1.small
        # - slb.s2.small
        # - slb.s2.medium
        # - slb.s3.small
        # - slb.s3.medium
        # - slb.s3.large
        # 
        # Default value: `slb.s2.small`.
        self.load_balancer_spec = load_balancer_spec
        # [**This field is deprecated**] Enable Log Service for the cluster. Only takes effect for ACK Serverless clusters, and the value must be `SLS`.
        self.logging_type = logging_type
        # [**This field is deprecated**] For cluster control plane configuration, use the `login_password` parameter under `control_plane_config` instead. For node pool configuration, use the `login_password` parameter under `scaling_group` in `nodepool` instead.
        # 
        # SSH login password. Mutually exclusive with `key_pair`. The password must be 8 to 30 characters in length and contain at least three of the following: uppercase letters, lowercase letters, digits, and special characters.
        self.login_password = login_password
        # Cluster maintenance window.
        self.maintenance_window = maintenance_window
        # [**This field is deprecated**] For cluster control plane configuration, use the `auto_renew` parameter under `control_plane_config` instead.
        # 
        # Whether to enable auto-renewal for Master nodes. Only takes effect when `master_instance_charge_type` is set to `PrePaid`. Valid values:
        # 
        # - `true`: Enable auto-renewal.
        # - `false`: Disable auto-renewal.
        # 
        # Default value: `true`.
        self.master_auto_renew = master_auto_renew
        # [**This field is deprecated**] For cluster control plane configuration, use the `auto_renew_period` parameter under `control_plane_config` instead.
        # 
        # Master node auto-renewal period. Only takes effect when subscription billing type is selected, and is a required value.
        # 
        # Valid values: {1, 2, 3, 6, 12}.
        # 
        # Default value: 1.
        self.master_auto_renew_period = master_auto_renew_period
        # [**This field is deprecated**] For cluster control plane configuration, use the `size` parameter under `control_plane_config` instead.
        # 
        # Number of Master nodes. Valid values: `3` or `5`.
        # 
        # Default value: `3`.
        self.master_count = master_count
        # [**This field is deprecated**] For cluster control plane configuration, use the `instance_charge_type` parameter under `control_plane_config` instead.
        # 
        # Master node billing type. Valid values:
        # 
        # - `PrePaid`: Subscription.
        # - `PostPaid`: Pay-as-you-go.
        # 
        # Default value: `PostPaid`.
        self.master_instance_charge_type = master_instance_charge_type
        # [**This field is deprecated**] For cluster control plane configuration, use the `instance_types` parameter under `control_plane_config` instead.
        # 
        # Master node instance types. For more information, see [Instance family](https://help.aliyun.com/document_detail/25378.html).
        self.master_instance_types = master_instance_types
        # [**This field is deprecated**] For cluster control plane configuration, use the `unit` parameter under `control_plane_config` instead.
        # 
        # Master node subscription duration. Valid and required when `master_instance_charge_type` is set to `PrePaid`.
        # 
        # Valid values: {1, 2, 3, 6, 12, 24, 36, 48, 60}.
        # 
        # Default value: 1.
        self.master_period = master_period
        # [**This field is deprecated**] For cluster control plane configuration, use the `period_unit` parameter under `control_plane_config` instead.
        # 
        # Master node billing period. Must be specified when the billing type is `PrePaid`.
        # 
        # Valid value: `Month`. Currently, only month-based periods are supported.
        self.master_period_unit = master_period_unit
        # [**This field is deprecated**] For cluster control plane configuration, use the `system_disk_category` parameter under `control_plane_config` instead.
        # 
        # Master node system disk type. Valid values:
        # 
        # - `cloud_efficiency`: Ultra disk.
        # - `cloud_ssd`: SSD disk.
        # - `cloud_essd`: ESSD disk.
        # 
        # Default value: `cloud_ssd`. The default value may vary across availability zones.
        self.master_system_disk_category = master_system_disk_category
        # [**This field is deprecated**] For cluster control plane configuration, use the `system_disk_performance_level` parameter under `control_plane_config` instead.
        # 
        # Cluster Master node system disk performance level. Only takes effect for ESSD disks. The performance level is related to the disk size. For more information, see [ESSD disk](https://help.aliyun.com/document_detail/122389.html).
        self.master_system_disk_performance_level = master_system_disk_performance_level
        # [**This field is deprecated**] For cluster control plane configuration, use the `system_disk_size` parameter under `control_plane_config` instead.
        # 
        # Master node system disk size. Valid values: [40, 500\\]. Unit: GiB.
        # 
        # Default value: `120`.
        self.master_system_disk_size = master_system_disk_size
        # [**This field is deprecated**] For cluster control plane configuration, use the `system_disk_snapshot_policy_id` parameter under `control_plane_config` instead.
        # 
        # Automatic snapshot policy ID for the Master node system disk.
        self.master_system_disk_snapshot_policy_id = master_system_disk_snapshot_policy_id
        # [**This field is deprecated**] Use the `vswitch_ids` parameter instead.
        # 
        # List of Master node vSwitch IDs. The number of vSwitches ranges from [1, 3\\]. To ensure high availability of the cluster, it is recommended to select 3 vSwitches distributed in different availability zones.
        # 
        # The number of specified instance types must be consistent with `master_count` and correspond one-to-one with the elements in `master_vswitch_ids`.
        self.master_vswitch_ids = master_vswitch_ids
        # Custom cluster name. Consists of digits, Chinese characters, English characters, or hyphens (-), with a length of 1 to 63 characters, and cannot start with a hyphen (-).
        # 
        # This parameter is required.
        self.name = name
        # [**This field is deprecated**] Use the `snat_entry` parameter instead.
        self.nat_gateway = nat_gateway
        # Number of node IPs, determined by specifying the network CIDR. Only takes effect for Flannel network type clusters.
        # 
        # Default value: `26`.
        self.node_cidr_mask = node_cidr_mask
        # [**This field is deprecated**] For node pool configuration, use the `node_name_mode` parameter under `kubernetes_config` in `nodepool` instead.
        self.node_name_mode = node_name_mode
        # Node service ports. Valid port range: [30000, 65535\\].
        # 
        # Default value: `30000-32767`.
        self.node_port_range = node_port_range
        # Node pool list.
        self.nodepools = nodepools
        # [**This field is deprecated**] For node pool configuration, use the `desired_size` parameter under `scaling_group` in `nodepool` instead.
        # 
        # Number of Worker nodes. Range: [0, 100\\].
        self.num_of_nodes = num_of_nodes
        # Cluster automatic O&M policy.
        self.operation_policy = operation_policy
        # [**This field is deprecated**] For cluster control plane node configuration, use the `image_type` parameter under `control_plane_config` instead. For node pool configuration, use the `image_type` parameter under `scaling_group` in `nodepool` instead.
        # 
        # OS platform type. Valid values:
        # - Windows
        # - Linux
        # 
        # Default value: `Linux`.
        self.os_type = os_type
        # [**This field is deprecated**]
        # 
        # Purchase duration. Subscription duration. Valid and required when charge_type is set to PrePaid.
        # 
        # Valid values: {1, 2, 3, 6, 12, 24, 36, 48, 60}.
        # 
        # Default value: 1.
        # 
        # This field was changed on October 15, 2024. For more information, see [Announcement on CreateCluster API parameter behavior changes](https://help.aliyun.com/document_detail/2849194.html).
        self.period = period
        # [**This field is deprecated**]
        # 
        # Billing period. Must be specified when the billing type is PrePaid.
        # 
        # Valid value: Month. Currently, only month-based periods are supported.
        # 
        # This field was changed on October 15, 2024. For more information, see [Announcement on CreateCluster API parameter behavior changes](https://help.aliyun.com/document_detail/2849194.html).
        self.period_unit = period_unit
        # [**This field is deprecated**] For node pool configuration, use the `platform` parameter under `scaling_group` in `nodepool` instead.
        # 
        # OS distribution. Valid values:
        # 
        # - CentOS
        # - AliyunLinux
        # - QbootAliyunLinux
        # - Qboot
        # - Windows
        # - WindowsCore
        # 
        # Default value: `CentOS`.
        self.platform = platform
        # [**This field is deprecated**] When using the Terway network plugin, you need to specify vSwitches for Pod IP allocation. Each Pod vSwitch corresponds to a Worker node vSwitch, and the availability zones of Pod vSwitches and Worker node vSwitches must be consistent.
        # > The CIDR mask of Pod vSwitches should not exceed 19 and must not exceed 25; otherwise, the available Pod IP addresses in the cluster network will be very limited, affecting normal cluster usage.
        self.pod_vswitch_ids = pod_vswitch_ids
        # When `cluster_type` is set to `ManagedKubernetes`, you can further specify the cluster subtype.
        # - `Default`: ACK managed cluster, including ACK cluster (Pro and Basic editions).
        # - `Edge`: ACK Edge cluster, including ACK Edge cluster (Pro and Basic editions).
        # - `Serverless`: ACK Serverless cluster, including ACK Serverless cluster (Pro and Basic editions).
        # - `Lingjun`: ACK Lingjun cluster, available in Pro edition.
        self.profile = profile
        # kube-proxy mode
        # 
        # - `iptables`: A mature and stable kube-proxy mode. Kubernetes Service discovery and load balancing are configured using iptables rules. Performance is average and significantly affected by scale, suitable for clusters with a small number of Services.
        # - `ipvs`: A high-performance kube-proxy mode. Kubernetes Service discovery and load balancing are configured using the Linux IPVS module, suitable for clusters with a large number of Services that require high-performance load balancing.
        # - `nftables`: Next-generation kube-proxy mode based on Linux nftables for Service discovery and load balancing. It is a modern replacement for iptables. Compared to iptables, nftables performs better in network performance, rule update efficiency, and large-scale Service scenarios.  
        # Only supported for clusters of version 1.35 and above. The Kubernetes community deprecated IPVS starting from version 1.35. It is recommended to use nftables for new clusters for longer-term community support.
        # 
        # Default value: `ipvs`.
        self.proxy_mode = proxy_mode
        # [**This field is deprecated**] For node pool configuration, use the `rds_instances` parameter under `scaling_group` in `nodepool` instead.
        # 
        # List of RDS instances. Select the RDS instances you want to add to the whitelist. It is recommended to add the container Pod CIDR block and Node CIDR block in RDS. Setting RDS instances may fail to pop up due to non-running instance status.
        self.rds_instances = rds_instances
        # The region ID where the cluster is located. For details, see [Regions supported by Container Service](https://help.aliyun.com/document_detail/216938.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID to which the cluster belongs, used for isolating different resources.
        self.resource_group_id = resource_group_id
        # RRSA feature configuration.
        self.rrsa_config = rrsa_config
        # Container runtime in the cluster. Supports containerd, sandboxed containers, and Docker.
        # > Kubernetes 1.24 no longer supports Docker as a built-in container runtime.
        # 
        # For more information, see [Comparison of Docker, containerd, and sandboxed container runtimes](https://help.aliyun.com/document_detail/160313.html).
        self.runtime = runtime
        # Specify the security group ID when creating a cluster with an existing security group. Mutually exclusive with `is_enterprise_security_group`. Cluster nodes are automatically added to this security group.
        self.security_group_id = security_group_id
        # [**This field is deprecated**] For cluster control plane configuration, use the `security_hardening_os` parameter under `control_plane_config` instead. For node pool configuration, use the `security_hardening_os` parameter under `scaling_group` in `nodepool` instead.
        # 
        # Alibaba Cloud OS security hardening. Valid values:
        # 
        # - `true`: Enable Alibaba Cloud OS security hardening.
        # - `false`: Disable Alibaba Cloud OS security hardening.
        # 
        # Default value: `false`.
        self.security_hardening_os = security_hardening_os
        # ServiceAccount is the access credential for communication between Pods and the cluster API Server. `service-account-issuer` is the issuer identity in the `serviceaccount token`, i.e., the `iss` field in the `token payload`.
        # 
        # For more details about `ServiceAccount`, see [Deploy service account token volume projection](https://help.aliyun.com/document_detail/160384.html).
        self.service_account_issuer = service_account_issuer
        # Service network CIDR block. Valid ranges: 10.0.0.0/16-24, 172.16-31.0.0/16-24, 192.168.0.0/16-24. Cannot overlap with VPC CIDR block 10.1.0.0/21 or CIDR blocks used by existing Kubernetes clusters in the VPC. Cannot be modified after creation.
        # 
        # Default value: 172.19.0.0/20.
        self.service_cidr = service_cidr
        # [**This field is deprecated**] Service discovery type within the cluster, used to specify the service discovery method in `ACK Serverless` clusters.
        # 
        # - `CoreDNS`: Uses the Kubernetes native standard service discovery component CoreDNS. A set of containers needs to be deployed in the cluster for DNS resolution. By default, two ECI instances with 0.25 Core 512 MiB specifications are used.
        # - `PrivateZone`: Uses the Alibaba Cloud PrivateZone product for service discovery capabilities. The PrivateZone service needs to be enabled.
        # 
        # Default value: Not enabled.
        self.service_discovery_types = service_discovery_types
        # Configure SNAT for the VPC. Valid values:
        # 
        # - `true`: Automatically create a NAT gateway and configure SNAT rules. Set to `true` if nodes and applications in the cluster need to access the Internet.
        # - `false`: Do not create a NAT gateway or SNAT rules. Nodes and applications in the cluster will not be able to access the Internet.
        # 
        # > If not enabled during cluster creation and the business later requires Internet access, you can [manually enable it](https://help.aliyun.com/document_detail/178480.html).
        # 
        # Default value: `false`.
        self.snat_entry = snat_entry
        # [**This field is deprecated**] For cluster control plane node configuration, use the `soc_enabled` parameter under `control_plane_config` instead. For node pool configuration, use the `soc_enabled` parameter under `scaling_group` in `nodepool` instead.
        # 
        # Classified protection hardening. For more information, see [ACK classified protection hardening user guide](https://help.aliyun.com/document_detail/196148.html).
        # 
        # Valid values:
        # - `true`: Enable classified protection hardening.
        # - `false`: Disable classified protection hardening.
        # 
        # Default value: `false`.
        self.soc_enabled = soc_enabled
        # Whether to enable public SSH login. Used for logging in to Master nodes of ACK dedicated clusters. This parameter does not take effect in managed clusters.
        # - `true`: Enable.
        # - `false`: Disable.
        # 
        # Default value: `false`.
        self.ssh_flags = ssh_flags
        # Node tags. Tag definition rules:
        # 
        # - Tags consist of case-sensitive key-value pairs. You can set up to 20 tags.
        # - Tag keys cannot be duplicated, with a maximum length of 64 characters; tag values can be empty, with a maximum length of 128 characters. Neither tag keys nor tag values can start with “aliyun”, “acs:”, “https://”, or “http://”. For details, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        self.tags = tags
        # [**This field is deprecated**] For node pool configuration, use the `taints` parameter under `kubernetes_config` in `nodepool` instead.
        # 
        # Node taint information. Taints and tolerations work together to prevent Pods from being scheduled on inappropriate nodes. For more information, see [taint-and-toleration](https://kubernetes.io/zh/docs/concepts/scheduling-eviction/taint-and-toleration/).
        self.taints = taints
        # [**This field is deprecated**] By default, no rollback is performed when cluster creation fails. You need to clean up the failed cluster yourself.
        # 
        # Cluster creation timeout. Unit: minutes.
        # 
        # Default value: `60`.
        self.timeout_mins = timeout_mins
        # The timezone used by the cluster. See [Supported timezones](https://help.aliyun.com/document_detail/354879.html).
        self.timezone = timezone
        # Custom cluster CA.
        self.user_ca = user_ca
        # [**This field is deprecated**] Custom node data.
        self.user_data = user_data
        # The VPC used by the cluster. Must be provided when creating a cluster.
        self.vpcid = vpcid
        # vSwitches for cluster nodes. This field is required when creating a zero-node managed cluster.
        self.vswitch_ids = vswitch_ids
        # [**This field is deprecated**] For node pool configuration, use the `auto_renew` parameter under `scaling_group` in `nodepool` instead.
        # 
        # Whether to enable auto-renewal for Worker nodes. Only takes effect when `worker_instance_charge_type` is set to `PrePaid`. Valid values:
        # 
        # - `true`: Enable auto-renewal.
        # - `false`: Disable auto-renewal.
        # 
        # Default value: `true`.
        self.worker_auto_renew = worker_auto_renew
        # [**This field is deprecated**] For node pool configuration, use the `auto_renew_period` parameter under `scaling_group` in `nodepool` instead.
        # 
        # 
        # Worker node auto-renewal period. Only takes effect when subscription billing type is selected, and is a required value.
        # 
        # Valid values: {1, 2, 3, 6, 12}.
        self.worker_auto_renew_period = worker_auto_renew_period
        # [**This field is deprecated**] For node pool configuration, use the `data_disks` parameter under `scaling_group` in `nodepool` instead.
        # 
        # Combination of Worker node data disk type, size, and other configurations.
        self.worker_data_disks = worker_data_disks
        # [**This field is deprecated**] For node pool configuration, use the `instance_charge_type` parameter under `scaling_group` in `nodepool` instead.
        # 
        # Worker node billing type. Valid values:
        # 
        # - `PrePaid`: Subscription.
        # - `PostPaid`: Pay-as-you-go.
        # 
        # Default value: Pay-as-you-go.
        self.worker_instance_charge_type = worker_instance_charge_type
        # [**This field is deprecated**] For node pool configuration, use the `instance_types` parameter under `scaling_group` in `nodepool` instead.
        # 
        # Worker node instance configuration.
        self.worker_instance_types = worker_instance_types
        # [**This field is deprecated**] For node pool configuration, use the `period` parameter under `scaling_group` in `nodepool` instead.
        # 
        # Worker node subscription duration. Valid and required when `worker_instance_charge_type` is set to `PrePaid`.
        # 
        # Valid values: {1, 2, 3, 6, 12, 24, 36, 48, 60}.
        # 
        # Default value: 1.
        self.worker_period = worker_period
        # [**This field is deprecated**] For node pool configuration, use the `period_unit` parameter under `scaling_group` in `nodepool` instead.
        # 
        # Worker node billing period. Must be specified when the billing type is `PrePaid`.
        # 
        # Valid value: `Month`. Currently, only month-based periods are supported.
        self.worker_period_unit = worker_period_unit
        # [**This field is deprecated**] For node pool configuration, use the `system_disk_category` parameter under `scaling_group` in `nodepool` instead.
        # 
        # Worker node system disk type. For more information, see [Block storage overview](https://help.aliyun.com/document_detail/63136.html).
        # 
        # Valid values:
        # 
        # - `cloud_efficiency`: Ultra disk.
        # - `cloud_ssd`: SSD disk.
        # 
        # 
        # Default value: `cloud_ssd`.
        self.worker_system_disk_category = worker_system_disk_category
        # [**This field is deprecated**] For node pool configuration, use the `system_disk_performance_level` parameter under `scaling_group` in `nodepool` instead.
        # 
        # When the system disk is an ESSD disk, you can set the Performance Level (PL) of the ESSD disk. For more information, see [ESSD disk](https://help.aliyun.com/document_detail/122389.html).
        # 
        # Valid values:
        # 
        # - PL0
        # - PL1
        # - PL2
        # - PL3
        self.worker_system_disk_performance_level = worker_system_disk_performance_level
        # [**This field is deprecated**] For node pool configuration, use the `system_disk_size` parameter under `scaling_group` in `nodepool` instead.
        # 
        # Worker node system disk size. Unit: GiB.
        # 
        # Valid values: [40, 500\\].
        # 
        # The value must be greater than or equal to max{40, ImageSize}.
        # 
        # Default value: `120`.
        self.worker_system_disk_size = worker_system_disk_size
        # [**This field is deprecated**] For node pool configuration, use the `system_disk_snapshot_policy_id` parameter under `scaling_group` in `nodepool` instead.
        # 
        # Automatic snapshot policy ID for the Worker node system disk.
        self.worker_system_disk_snapshot_policy_id = worker_system_disk_snapshot_policy_id
        # [**This field is deprecated**] For node pool configuration, use the `vswitch_ids` parameter under `scaling_group` in `nodepool` instead.
        # 
        # List of vSwitches used by cluster nodes. One node corresponds to one value.
        # 
        # When creating a zero-node managed cluster, the `worker_vswitch_ids` field is not required, but `vswitch_ids` must be provided.
        self.worker_vswitch_ids = worker_vswitch_ids
        # [**This field is deprecated**] Use the `zone_ids` parameter instead.
        # 
        # Availability zone ID of the region where the cluster is located. This parameter is specific to ACK managed cluster types.
        # 
        # When creating an ACK managed cluster, if `vpc_id` and `vswitch_ids` are not specified, `zone_id` must be specified for the cluster to automatically create VPC network resources in this availability zone. This parameter is ignored when `vpc_id` and `vswitch_ids` are specified.
        self.zone_id = zone_id
        # Multiple availability zone IDs of the region where the cluster is located. This parameter is specific to ACK managed cluster types.
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
        # Data disk type.
        # 
        # This parameter is required.
        self.category = category
        # Whether to encrypt the data disk. Valid values:
        # 
        # - `true`: Encrypt the data disk.
        # - `false`: Do not encrypt the data disk.
        # 
        # Default value: `false`.
        self.encrypted = encrypted
        # Node data disk performance level. Only takes effect for [ESSD disks](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # Data disk size. Valid values: 40 to 32767. Unit: GiB.
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
        # Whether to enable the RRSA feature.
        # 
        # - true: Enable.
        # 
        # - false: Disable.
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
            temp_model = main_models.CreateClusterRequestOperationPolicyClusterAutoUpgrade()
            self.cluster_auto_upgrade = temp_model.from_map(m.get('cluster_auto_upgrade'))

        return self

class CreateClusterRequestOperationPolicyClusterAutoUpgrade(DaraModel):
    def __init__(
        self,
        channel: str = None,
        enabled: bool = None,
    ):
        # Cluster automatic upgrade frequency. Valid values:
        # - patch: Automatically upgrade to an available patch version of the current minor version. The new Kubernetes version will not contain breaking changes.
        # - stable: Automatically upgrade to the latest patch version of the second-newest minor version. The new Kubernetes version may involve API and feature changes, but its stability has been widely verified.
        # - rapid: Automatically upgrade to the latest patch version of the latest minor version to get new features from the Kubernetes community faster.
        self.channel = channel
        # Whether to enable cluster automatic upgrade.
        # 
        # - true: Enable.
        # 
        # - false: Disable.
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
    ):
        # Internal DNS configuration for the cluster, applicable to ACK managed clusters. The internal DNS is used by node-side system components such as kubelet and kube-proxy to access the API Server. When internal DNS access is not enabled, node-side system components will access via CLB IP.
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
            temp_model = main_models.CreateClusterRequestControlPlaneEndpointsConfigInternalDnsConfig()
            self.internal_dns_config = temp_model.from_map(m.get('internal_dns_config'))

        return self

class CreateClusterRequestControlPlaneEndpointsConfigInternalDnsConfig(DaraModel):
    def __init__(
        self,
        bind_vpcs: List[str] = None,
    ):
        # VPCs where the internal DNS record resolution takes effect.
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
        # Whether to enable auto-renewal for control plane nodes. Valid when the billing type is `PrePaid`.
        # - true: Enable auto-renewal.
        # - false: Disable auto-renewal.
        # 
        # Default value: true.
        self.auto_renew = auto_renew
        # Auto-renewal duration for control plane nodes.
        # 
        # Valid values: {1, 2, 3, 6, 12}. Unit: months.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # Control plane node billing type.
        # 
        # - `PrePaid`: Subscription.
        # - `PostPaid`: Pay-as-you-go.
        # 
        # Default value: `PostPaid`.
        self.charge_type = charge_type
        # Whether to install CloudMonitor on nodes.
        # 
        # - true: Install the CloudMonitor agent.
        # 
        # - false: Do not install the CloudMonitor agent.
        # 
        # Default value: false.
        self.cloud_monitor_flags = cloud_monitor_flags
        # Node CPU management policy.
        # 
        # - static: Allows enhancing CPU affinity and exclusivity for Pods with certain resource characteristics on the node.
        # 
        # - none: Enables the existing default CPU affinity scheme.
        # 
        # Default value: none.
        self.cpu_policy = cpu_policy
        # Deployment set ID.
        self.deploymentset_id = deploymentset_id
        # Image ID.
        self.image_id = image_id
        # OS image type.
        self.image_type = image_type
        # ECS instance metadata access configuration.
        self.instance_metadata_options = instance_metadata_options
        # Node instance types.
        self.instance_types = instance_types
        # Key pair name. Mutually exclusive with login_password.
        self.key_pair = key_pair
        # SSH login password. The password must be 8 to 30 characters in length and contain at least three of the following: uppercase letters, lowercase letters, digits, and special characters. Mutually exclusive with key_pair.
        self.login_password = login_password
        # [**This field is deprecated**] Node service port range.
        self.node_port_range = node_port_range
        # Subscription duration for control plane nodes. Valid and required when the billing type is `PrePaid`.
        # 
        # Valid values: {1, 2, 3, 6, 12, 24, 36, 48, 60}. Unit: months.
        # 
        # Default value: 1.
        self.period = period
        # Subscription period unit for control plane nodes. Valid and required when the billing type is `PrePaid`.
        # 
        # Valid value: `Month`. Currently, only month-based periods are supported.
        self.period_unit = period_unit
        # [**This field is deprecated**] Control plane node runtime name. Valid value:
        # 
        # containerd: Containerd runtime, supported by all cluster versions.
        self.runtime = runtime
        # Whether to enable Alibaba Cloud OS security hardening.
        # 
        # - true: Enable Alibaba Cloud OS security hardening.
        # 
        # - false: Disable Alibaba Cloud OS security hardening.
        # 
        # Default value: false.
        self.security_hardening_os = security_hardening_os
        # Number of control plane nodes.
        # 
        # Valid values: `3` or `5`.
        self.size = size
        # Whether to enable classified protection security hardening.
        # 
        # - true: Enable classified protection hardening.
        # 
        # - false: Disable classified protection hardening.
        # 
        # Default value: false.
        self.soc_enabled = soc_enabled
        # Whether to enable burst (performance burst) for the node system disk.
        # 
        # - true: Enable.
        # 
        # - false: Disable.
        # 
        # This parameter is only supported when `system_disk_category` is set to `cloud_auto`.
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # Node system disk type.
        # 
        # - `cloud_efficiency`: Ultra disk.
        # - `cloud_ssd`: SSD disk.
        # - `cloud_essd`: ESSD disk.
        # - `cloud_auto`: ESSD AutoPL disk.
        # - `cloud_essd_entry`: ESSD Entry disk.
        # 
        # Default value: `cloud_ssd`. The default value may vary across availability zones.
        self.system_disk_category = system_disk_category
        # Node system disk performance level. Only takes effect for ESSD disks.
        # 
        # The performance level is related to the disk size. For more information, see [ESSD disk](https://help.aliyun.com/document_detail/122389.html).
        self.system_disk_performance_level = system_disk_performance_level
        # Pre-provisioned read/write IOPS for the node system disk.
        # 
        # Valid values: 0 to min{50,000, 1000*capacity - baseline performance}. Baseline performance = min{1,800 + 50*capacity, 50000}.
        # 
        # This parameter is only supported when `system_disk_category` is set to `cloud_auto`.
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # Node system disk size.
        # 
        # Valid values: [40, 500\\]. Unit: GiB.
        # 
        # Default value: `120`.
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
        # Whether to enable intelligent managed mode.
        # 
        # - true: Enable.
        # 
        # - false: Disable.
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
        # Whether to enable the cluster audit log feature.
        # 
        # - true: Enable.
        # 
        # - false: Disable.
        self.enabled = enabled
        # The [SLS Project](https://help.aliyun.com/document_detail/48873.html) where the cluster audit log [Logstore](https://help.aliyun.com/document_detail/48873.html) is located.
        # 
        # - Default value: `k8s-log-{clusterid}`.
        # 
        # - After enabling the cluster audit log feature, a corresponding Logstore will be created under the specified SLS Project.
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

