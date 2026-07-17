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
        # 【**该字段已废弃**】注册集群 API Server SLB 访问控制列表。
        self.access_control_list = access_control_list
        # The list of cluster components. Specify the components to install when creating a cluster using `addons`.
        # 
        # **Network component**: Required. Choose between Flannel and Terway network types:
        # 
        # - Flannel network: [{"name":"flannel","config":""}\\].
        # - Terway network: [{"name": "terway-eniip","config": ""}\\].
        # 
        # **Storage component**: Optional. Only the `csi` type is supported:
        # 
        # `csi`: [{"name":"csi-plugin","config": ""},{"name": "csi-provisioner","config": ""}\\].
        # 
        # **Log component**: Optional. We recommend that you enable this component. If the log service is not enabled, the cluster audit feature is unavailable.
        # 
        # - Use an existing `SLS Project`: [{"name": "loongcollector","config": "{\\"IngressDashboardEnabled\\":\\"true\\",\\"sls_project_name\\":\\"your_sls_project_name\\"}"}\\].
        # - Create a new `SLS Project`: [{"name": "loongcollector","config": "{\\"IngressDashboardEnabled\\":\\"true\\"}"}\\].
        # 
        # **Ingress component**: Optional. ACK dedicated clusters install the Ingress component `nginx-ingress-controller` by default.
        # 
        # - Install Ingress with public network access: [{"name":"nginx-ingress-controller","config":"{\\"IngressSlbNetworkType\\":\\"internet\\"}"}\\].
        # - Disable default Ingress installation: [{"name": "nginx-ingress-controller","config": "","disabled": true}\\].
        # 
        # **Event Center**: Optional. Enabled by default.
        # 
        # The Event Center provides storage, query, and alerting capabilities for Kubernetes events. The Logstore associated with the Kubernetes Event Center is free for 90 days. For more information about the free policy, see [Create and use the Kubernetes event center](https://help.aliyun.com/document_detail/150476.html).
        # 
        # Example of enabling the Event Center: [{"name":"ack-node-problem-detector","config":"{\\"sls_project_name\\":\\"your_sls_project_name\\"}"}\\].
        self.addons = addons
        # A ServiceAccount is the access credential for communication between a Pod and the cluster API Server. The `api-audiences` is the valid request `token` identity, used by the `apiserver` to authenticate whether a request `token` is valid. Multiple `audiences` are supported, separated by commas (,).
        # 
        # For more information about `ServiceAccount`, see [Deploy service account token volume projection](https://help.aliyun.com/document_detail/160384.html).
        self.api_audiences = api_audiences
        # The cluster audit log configuration.
        self.audit_log_config = audit_log_config
        # The [intelligent managed mode](https://help.aliyun.com/document_detail/2938898.html) configuration.
        self.auto_mode = auto_mode
        # 【**该字段已废弃**】
        # 
        # 是否开启自动续费，当`charge_type`取值为`PrePaid`时才生效。取值：
        # 
        # - `true`：自动续费。
        # - `false`：不自动续费。
        # 
        # 默认值：`false`。
        # 
        # 该字段于2024年10月15日存在变更，更多信息，请参见[关于集群创建接口CreateCluster参数行为变更的公告](https://help.aliyun.com/document_detail/2849194.html)。
        self.auto_renew = auto_renew
        # 【**该字段已废弃**】
        # 
        # 自动续费周期，当选择预付费和自动续费时才生效。当`PeriodUnit=Month`时，取值范围：{1, 2, 3, 6, 12}。
        # 
        # 默认值：1。
        # 
        # 该字段于2024年10月15日存在变更，更多信息，请参见[关于集群创建接口CreateCluster参数行为变更的公告](https://help.aliyun.com/document_detail/2849194.html)。
        self.auto_renew_period = auto_renew_period
        # 【**该字段已废弃**】
        # 
        # API Server所使用的CLB实例的付费类型，默认值为PostPaid。取值：
        # - PostPaid：按量付费。
        # - PrePaid：包年包月，新建CLB付费类型已不支持，存量不影响。
        # 
        # >Notice: 
        # 
        # - 该字段于2024年10月15日存在变更，更多信息，请参见[关于集群创建接口CreateCluster参数行为变更的公告](https://help.aliyun.com/document_detail/2849194.html)。
        # - 自2024年12月01日起，新创建的CLB实例不再支持包年包月付费类型，同时将新增收取实例费。
        # </notice>
        # <props="china">详细信息请参见[【产品公告】关于取消新增集群API Server负载均衡CLB包年包月付费的公告](https://help.aliyun.com/document_detail/2851191.html)、[传统型负载均衡CLB计费项调整公告](https://help.aliyun.com/document_detail/2839797.html)。
        # <props="intl">详细信息请参见[传统型负载均衡CLB计费项调整公告](https://help.aliyun.com/document_detail/2839797.html)。
        self.charge_type = charge_type
        # **This field is deprecated.** For control plane configurations, use the `security_hardening_os` parameter under `control_plane_config` instead. For node pool configurations, use the `security_hardening_os` parameter under `scaling_group` in `nodepool` instead.
        self.cis_enabled = cis_enabled
        # **This field is deprecated.** For control plane node configurations, use the `cloud_monitor_flags` parameter under `control_plane_config` instead. For node pool configurations, use the `cms_enabled` parameter under `kubernetes_config` in `nodepool` instead.
        # 
        # Specifies whether to install the CloudMonitor agent on the cluster. Valid values:
        # 
        # - `true`: Installs the CloudMonitor agent.
        # - `false`: Does not install the CloudMonitor agent.
        # 
        # Default value: `false`.
        self.cloud_monitor_flags = cloud_monitor_flags
        # The cluster local domain.
        # 
        # Naming rules: The domain consists of one or more parts separated by periods (.). Each part can be up to 63 characters in length and can contain lowercase letters, digits, and hyphens (-). Each part must start and end with a lowercase letter or digit.
        self.cluster_domain = cluster_domain
        # After you set `cluster_type` to `ManagedKubernetes` and configure `profile`, you can further specify the cluster specification. Valid values:
        # 
        # - `ack.standard`: Basic (selected by default when the value is empty)
        # - `ack.pro.small`: Pro
        # - `ack.pro.xlarge`: Pro XL
        # - `ack.pro.2xlarge`: Pro 2XL
        # - `ack.pro.4xlarge`: Pro 4XL (requires contacting customer service to enable the whitelist)
        # 
        # Pro XL, Pro 2XL, and Pro 4XL are three tiers provided by <props="china">[ACK Pro Provisioned Control Plane](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane)<props="intl">[ACK Pro Provisioned Control Plane](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/user-guide/ack-pro-provisioned-control-plane). By pre-allocating and fixing control plane resources, they ensure that API concurrency and Pod scheduling capabilities remain at a deterministic high level, suitable for AI training and inference, ultra-large-scale clusters, and mission-critical workloads.
        # 
        # For information about the management fees for Pro and Provisioned Control Plane clusters, see <props="china">[Cluster management fee](https://help.aliyun.com/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee)<props="intl">[Cluster management fee](https://www.alibabacloud.com/help/ack/ack-managed-and-ack-dedicated/product-overview/cluster-management-fee).
        self.cluster_spec = cluster_spec
        # - `Kubernetes`: ACK dedicated cluster.
        # - `ManagedKubernetes`: ACK managed cluster types, including ACK managed clusters (Pro and Basic), ACK Serverless clusters (Pro and Basic), ACK Edge clusters (Pro and Basic), and ACK Lingjun clusters (Pro).
        # - `ExternalKubernetes`: registered cluster.
        self.cluster_type = cluster_type
        # The Pod network CIDR block. It must be a valid private CIDR block, specifically the following CIDR blocks and their subnets: 10.0.0.0/8, 172.16-31.0.0/12-16, 192.168.0.0/16. It cannot overlap with the VPC CIDR block or CIDR blocks used by existing Kubernetes clusters in the VPC. It cannot be modified after creation.
        # 
        # For information about cluster network planning, see [ACK managed cluster network planning](https://help.aliyun.com/document_detail/86500.html).
        # 
        # > This field is required for Flannel clusters.
        self.container_cidr = container_cidr
        # The ACK dedicated cluster control plane configuration.
        self.control_plane_config = control_plane_config
        # The cluster endpoint configuration.
        self.control_plane_endpoints_config = control_plane_endpoints_config
        # The list of component names that specifies which control plane components to collect logs from.
        # 
        # By default, logs are collected from kube-apiserver, kube-controller-manager, kube-scheduler, and cloud-controller-manager.
        self.controlplane_log_components = controlplane_log_components
        # The Simple Log Service project for control plane component logs. You can use an existing project for log storage or have the system automatically create a project. If you choose automatic creation, a Simple Log Service project named `k8s-log-{ClusterID}` is created.
        self.controlplane_log_project = controlplane_log_project
        # The number of days for log retention of control plane component logs.
        self.controlplane_log_ttl = controlplane_log_ttl
        # **This field is deprecated.** For control plane configurations, use the `cpu_policy` parameter under `control_plane_config` instead. For node pool configurations, use the `cpu_policy` parameter under `kubernetes_config` in `nodepool` instead.
        # 
        # The node CPU management policy. The following policies are supported for cluster versions 1.12.6 and later:
        # 
        # - `static`: Allows pods with certain resource characteristics on the node to be granted enhanced CPU affinity and exclusivity.
        # - `none`: Uses the existing default CPU affinity scheme.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # **This field is deprecated.** Use the `extra_sans` parameter instead.
        # 
        # The custom certificate Subject Alternative Name (SAN). Separate multiple IP addresses or domain names with commas (,).
        self.custom_san = custom_san
        # Specifies whether to enable cluster deletion protection, which prevents the cluster from being accidentally deleted through the console or API. Valid values:
        # 
        # - `true`: Enable cluster deletion protection. The cluster cannot be deleted through the console or API.
        # - `false`: Do not enable cluster deletion protection. The cluster can be deleted through the console or API.
        # 
        # Default value: `false`.
        self.deletion_protection = deletion_protection
        # 【**该字段已废弃**】集群创建失败时默认不会进行回滚，您需要自行清理创建失败的集群。
        # 
        # 集群创建失败是否回滚。取值：
        # 
        # - `true`：当集群创建失败时，进行回滚操作。
        # - `false`：当集群创建失败时，不进行回滚操作。
        # 
        # 
        # 默认值：`true`。
        self.disable_rollback = disable_rollback
        # 【**该字段已废弃**】请使用参数`rrsa_config`代替。
        # 
        # 是否启用RRSA功能。
        # 
        # - true：开启。
        # 
        # - false：不开启。
        self.enable_rrsa = enable_rrsa
        # The KMS key ID used to encrypt data disks. For more information, see [Key Management Service](https://help.aliyun.com/document_detail/28935.html).
        # 
        # > This feature only takes effect in ACK Pro managed clusters.
        self.encryption_provider_key = encryption_provider_key
        # Specifies whether to public network access. Exposes the API Server through an EIP to public network access to the cluster.
        # 
        # - `true`: Public network access.
        # - `false`: Do not public network access. If not enabled, the cluster API Server cannot be accessed from the Internet.
        # 
        # Default value: `false`.
        self.endpoint_public_access = endpoint_public_access
        # The custom API Server certificate SAN (Subject Alternative Name).
        self.extra_sans = extra_sans
        # 【**该字段已废弃**】创建集群时不支持选择已有节点，如需添加已有节点到集群，请先创建节点池，并调用[AttachInstancesToNodePool](https://help.aliyun.com/document_detail/2667920.html)接口操作。
        # 
        # 使用已有实例创建集群时，是否对实例进行数据盘挂载，取值：
        # 
        # - `true`：将容器和镜像存储在数据盘，数据盘内原有数据将丢失，请注意备份数据。
        # 
        # - `false`：不将容器和镜像存储在数据盘。
        # 
        # 默认值：`false`。
        # 
        # 数据盘挂载规则：
        # 
        # - 如果ECS已挂载数据盘，且最后一块数据盘的文件系统未初始化，系统会自动将该数据盘格式化为ext4，用来存放内容/var/lib/docker、/var/lib/kubelet。
        # - 如果ECS未挂载数据盘，则不会挂载新的数据盘。
        self.format_disk = format_disk
        # **This field is deprecated.** For control plane configurations, use the `image_id` parameter under `control_plane_config` instead. For node pool configurations, use the `image_id` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The custom node image. The system image is used by default. When a custom image is selected, it replaces the default system image. For more information, see [Custom images](https://help.aliyun.com/document_detail/146647.html).
        self.image_id = image_id
        # 【**该字段已废弃**】集群控制面配置请使用`control_plane_config`下的`image_type`参数代替；节点池配置请使用`nodepool`中`scaling_group`下的`image_type`参数代替。
        # 
        # 操作系统发行版类型，推荐使用该字段指定节点操作系统。取值：
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
        # 默认值：`CentOS`。
        self.image_type = image_type
        # 【**该字段已废弃**】创建集群时不支持选择已有节点，如需添加已有节点到集群，请先创建节点池，并调用[AttachInstancesToNodePool](https://help.aliyun.com/document_detail/2667920.html)接口操作。
        # 
        # 
        # 使用已有节点创建集群时，需要指定ECS实例列表，该实例会作为Worker节点加入集群。
        # 
        # > 使用已有实例创建集群时，该字段必填。
        self.instances = instances
        # The IP protocol stack of the cluster.
        self.ip_stack = ip_stack
        # Specifies whether to use automatic creation of an advanced security group. Takes effect when `security_group_id` is empty.
        # 
        # > When using a basic security group, the total number of nodes and Terway Pods in the cluster cannot exceed 2000. Therefore, when creating a Terway network type cluster, we recommend using an advanced security group.
        # 
        # - `true`: Create and use an advanced security group.
        # - `false`: Use a basic security group.
        # 
        # Default value: `true`.
        self.is_enterprise_security_group = is_enterprise_security_group
        # 【**该字段已废弃**】创建集群时不支持选择已有节点，如需添加已有节点到集群，请先创建节点池，并调用[AttachInstancesToNodePool](https://help.aliyun.com/document_detail/2667920.html)接口操作。
        # 
        # 使用已有实例创建集群时，是否保留实例名称。
        # 
        # - `true`：保留。
        # - `false`：不保留，会用系统规则进行替换。
        # 
        # 默认值：`true`。
        self.keep_instance_name = keep_instance_name
        # **This field is deprecated.** For control plane configurations, use the `key_pair` parameter under `control_plane_config` instead. For node pool configurations, use the `key_pair` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The key pair name. Mutually exclusive with `login_password`.
        self.key_pair = key_pair
        # The cluster version, which is consistent with the Kubernetes community baseline version. We recommend that you select the latest version. If you do not specify this parameter, the latest version is used by default.
        # 
        # You can create clusters of the latest three versions. Call the [DescribeKubernetesVersionMetadata](https://help.aliyun.com/document_detail/2667899.html) operation to query supported cluster versions.
        # 
        # For more information about Kubernetes versions supported by ACK, see [Kubernetes version release overview](https://help.aliyun.com/document_detail/185269.html).
        self.kubernetes_version = kubernetes_version
        # The CLB instance ID for API Server access. When this parameter is specified, automatic creation of the API Server CLB is not performed.
        # > Ensure that the CLB instance has no other dependencies (such as listeners or backend servers). Shared and Internet-facing CLB instances are not supported.
        self.load_balancer_id = load_balancer_id
        # 【**该参数已废弃**】CLB按使用量计费，该参数不生效。
        # 
        # 负载均衡规格，取值：
        # - slb.s1.small
        # - slb.s2.small
        # - slb.s2.medium
        # - slb.s3.small
        # - slb.s3.medium
        # - slb.s3.large
        # 
        # 默认值：`slb.s2.small`。
        self.load_balancer_spec = load_balancer_spec
        # 【**该字段已废弃**】集群开启日志服务，只针对ACK Serverless集群生效，且取值必须是`SLS`。
        self.logging_type = logging_type
        # **This field is deprecated.** For control plane configurations, use the `login_password` parameter under `control_plane_config` instead. For node pool configurations, use the `login_password` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The SSH logon password. Mutually exclusive with `key_pair`. The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        self.login_password = login_password
        # The cluster maintenance window.
        self.maintenance_window = maintenance_window
        # **This field is deprecated.** For control plane configurations, use the `auto_renew` parameter under `control_plane_config` instead.
        # 
        # Specifies whether to enable auto-renewal for master nodes. This parameter takes effect only when `master_instance_charge_type` is set to `PrePaid`. Valid values:
        # 
        # - `true`: Enables auto-renewal.
        # - `false`: Disables auto-renewal.
        # 
        # Default value: `true`.
        self.master_auto_renew = master_auto_renew
        # **This field is deprecated.** For control plane configurations, use the `auto_renew_period` parameter under `control_plane_config` instead.
        # 
        # The auto-renewal period for master nodes. This parameter takes effect and is required when the subscription billing method is selected.
        # 
        # Valid values: {1, 2, 3, 6, 12}.
        # 
        # Default value: 1.
        self.master_auto_renew_period = master_auto_renew_period
        # **This field is deprecated.** For control plane configurations, use the `size` parameter under `control_plane_config` instead.
        # 
        # The number of master nodes. Valid values: `3` or `5`.
        # 
        # Default value: `3`.
        self.master_count = master_count
        # **This field is deprecated.** For control plane configurations, use the `instance_charge_type` parameter under `control_plane_config` instead.
        # 
        # The billing method for master nodes. Valid values:
        # 
        # - `PrePaid`: subscription.
        # - `PostPaid`: pay-as-you-go.
        # 
        # Default value: `PostPaid`.
        self.master_instance_charge_type = master_instance_charge_type
        # **This field is deprecated.** For control plane configurations, use the `instance_types` parameter under `control_plane_config` instead.
        # 
        # The instance types for master nodes. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.master_instance_types = master_instance_types
        # **This field is deprecated.** For control plane configurations, use the `unit` parameter under `control_plane_config` instead.
        # 
        # The subscription duration for master nodes. This parameter takes effect and is required only when `master_instance_charge_type` is set to `PrePaid`.
        # 
        # Valid values: {1, 2, 3, 6, 12, 24, 36, 48, 60}.
        # 
        # Default value: 1.
        self.master_period = master_period
        # **This field is deprecated.** For control plane configurations, use the `period_unit` parameter under `control_plane_config` instead.
        # 
        # The billing period unit for master nodes. This parameter is required when the billing method is `PrePaid`.
        # 
        # Valid values: `Month`. Only monthly billing is supported.
        self.master_period_unit = master_period_unit
        # **This field is deprecated.** For control plane configurations, use the `system_disk_category` parameter under `control_plane_config` instead.
        # 
        # The system cloud disk type for master nodes. Valid values:
        # 
        # - `cloud_efficiency`: ultra cloud disk.
        # - `cloud_ssd`: standard SSD.
        # - `cloud_essd`: ESSD.
        # 
        # Default value: `cloud_ssd`. The default value may vary by zone.
        self.master_system_disk_category = master_system_disk_category
        # **This field is deprecated.** For control plane configurations, use the `system_disk_performance_level` parameter under `control_plane_config` instead.
        # 
        # The performance level of the system cloud disk for cluster master nodes. This parameter takes effect only for ESSD cloud disks. The performance level varies based on the cloud disk size. For more information, see [ESSD cloud disks](https://help.aliyun.com/document_detail/122389.html).
        self.master_system_disk_performance_level = master_system_disk_performance_level
        # **This field is deprecated.** For control plane configurations, use the `system_disk_size` parameter under `control_plane_config` instead.
        # 
        # The system cloud disk size for master nodes. Valid values: [40,500\\]. Unit: GiB.
        # 
        # Default value: `120`.
        self.master_system_disk_size = master_system_disk_size
        # **This field is deprecated.** For control plane configurations, use the `system_disk_snapshot_policy_id` parameter under `control_plane_config` instead.
        # 
        # The automatic snapshot policy ID for the master node system cloud disk.
        self.master_system_disk_snapshot_policy_id = master_system_disk_snapshot_policy_id
        # **This field is deprecated.** Use the `vswitch_ids` parameter instead.
        # 
        # The list of vSwitch IDs for master nodes. The number of vSwitches ranges from [1,3\\]. To ensure high availability, select three vSwitches distributed across different zones.
        # 
        # The number of specified instance types must match the value of `master_count` and correspond one-to-one with the elements in `master_vswitch_ids`.
        self.master_vswitch_ids = master_vswitch_ids
        # The custom cluster name. The name must be 1 to 63 characters in length and can contain digits, Chinese characters, letters, and hyphens (-). It cannot start with a hyphen (-).
        # 
        # This parameter is required.
        self.name = name
        # 【**该字段已废弃**】请使用参数`snat_entry`代替。
        self.nat_gateway = nat_gateway
        # The number of IP addresses per node, determined by specifying the network CIDR mask. Only takes effect for Flannel network type clusters.
        # 
        # Default value: `26`.
        self.node_cidr_mask = node_cidr_mask
        # **This field is deprecated.** For node pool configurations, use the `node_name_mode` parameter under `kubernetes_config` in `nodepool` instead.
        self.node_name_mode = node_name_mode
        # The node service port range. Valid values: [30000,65535\\].
        # 
        # Default value: `30000-32767`.
        self.node_port_range = node_port_range
        # The list of node pools.
        self.nodepools = nodepools
        # **This field is deprecated.** For node pool configurations, use the `desired_size` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The number of worker nodes. Valid values: [0, 100\\].
        self.num_of_nodes = num_of_nodes
        # The cluster automatic O&M policy.
        self.operation_policy = operation_policy
        # **This field is deprecated.** For control plane node configurations, use the `image_type` parameter under `control_plane_config` instead. For node pool configurations, use the `image_type` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The operating system platform type. Valid values:
        # - Windows
        # - Linux
        # 
        # Default value: `Linux`.
        self.os_type = os_type
        # 【**该字段已废弃**】
        # 
        # 购买时长。包年包月时长，当charge_type取值为PrePaid时才生效，且为必选值。
        # 
        # 取值范围：{1, 2, 3, 6, 12, 24, 36, 48, 60}。
        # 
        # 默认值：1。
        # 
        # 该字段于2024年10月15日存在变更，更多信息，请参见[关于集群创建接口CreateCluster参数行为变更的公告](https://help.aliyun.com/document_detail/2849194.html)。
        self.period = period
        # 【**该字段已废弃**】
        # 
        # 付费周期，当付费类型为PrePaid的时候，需要指定周期。
        # 
        # 取值：Month，当前仅支持以月为周期。
        # 
        # 该字段于2024年10月15日存在变更，更多信息，请参见[关于集群创建接口CreateCluster参数行为变更的公告](https://help.aliyun.com/document_detail/2849194.html)。
        self.period_unit = period_unit
        # **This field is deprecated.** For node pool configurations, use the `platform` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The operating system distribution. Valid values:
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
        # **This field is deprecated.** When you select Terway as the network plugin, you must assign vSwitches for Pod IP allocation. Each Pod vSwitch corresponds to a worker node vSwitch, and the Pod vSwitch and the worker node vSwitch must be in the same zone.
        # > The CIDR block mask of the Pod vSwitch should not exceed 19 and must not exceed 25. Otherwise, the number of Pod IP addresses available in the cluster network is very limited, which affects normal cluster usage.
        self.pod_vswitch_ids = pod_vswitch_ids
        # When you set `cluster_type` to `ManagedKubernetes` (ACK managed cluster types), you can further specify the cluster subtype.
        # - `Default`: ACK managed cluster, including ACK clusters (Pro and Basic).
        # - `Edge`: ACK Edge cluster, including ACK Edge clusters (Pro and Basic).
        # - `Serverless`: ACK Serverless cluster, including ACK Serverless clusters (Pro and Basic).
        # - `Lingjun`: ACK Lingjun cluster, available in Pro.
        self.profile = profile
        # The kube-proxy mode.
        # 
        # - `iptables`: A mature and stable kube-proxy mode. Service discovery and load balancing for Kubernetes Services are configured using iptables rules. However, performance is average and significantly affected by scale. Suitable for clusters with a small number of Services.
        # - `ipvs`: A high-performance kube-proxy mode. Service discovery and load balancing for Kubernetes Services are configured using the Linux IPVS module. Suitable for clusters with a large number of Services that require high-performance load balancing.
        # - `nftables`: A next-generation kube-proxy mode that implements Service discovery and load balancing based on Linux nftables, serving as a modern replacement for iptables. Compared to iptables, nftables offers better network performance, more efficient rule updates, and improved behavior in large-scale Service scenarios.  
        # Only supported for clusters running version 1.35 or later. The Kubernetes community deprecated IPVS starting from version 1.35. For new clusters, use nftables for longer-term community support.
        # 
        # Default value: `ipvs`.
        self.proxy_mode = proxy_mode
        # **This field is deprecated.** For node pool configurations, use the `rds_instances` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The list of RDS instances. Select the RDS instances that you want to add to the whitelist. Go to the RDS console to add the container pod CIDR block and node CIDR block. Configuring RDS instances may fail if the instances are not in the running state.
        self.rds_instances = rds_instances
        # The region ID of the cluster. For more information, see [Regions supported by Container Service](https://help.aliyun.com/document_detail/216938.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID of the cluster, used to isolate different resources.
        self.resource_group_id = resource_group_id
        # The RRSA configuration.
        self.rrsa_config = rrsa_config
        # The container runtime of the cluster. Supported runtimes include containerd, sandboxed containers, and Docker.
        # > Kubernetes 1.24 no longer supports Docker as a built-in container runtime.
        # 
        # For more information, see [Comparison among Docker, containerd, and sandboxed container runtimes](https://help.aliyun.com/document_detail/160313.html).
        self.runtime = runtime
        # The security group ID. Specify this parameter when creating a cluster with an existing security group. Mutually exclusive with `is_enterprise_security_group`. Cluster nodes are automatically added to this security group.
        self.security_group_id = security_group_id
        # **This field is deprecated.** For control plane configurations, use the `security_hardening_os` parameter under `control_plane_config` instead. For node pool configurations, use the `security_hardening_os` parameter under `scaling_group` in `nodepool` instead.
        # 
        # Alibaba Cloud OS security hardening. Valid values:
        # 
        # - `true`: Enables Alibaba Cloud OS security hardening.
        # - `false`: Does not enable Alibaba Cloud OS security hardening.
        # 
        # Default value: `false`.
        self.security_hardening_os = security_hardening_os
        # A ServiceAccount is the access credential for communication between a Pod and the cluster API Server. The `service-account-issuer` is the issuer identity in the `serviceaccount token`, which is the `iss` field in the `token payload`.
        # 
        # For more information about `ServiceAccount`, see [Deploy service account token volume projection](https://help.aliyun.com/document_detail/160384.html).
        self.service_account_issuer = service_account_issuer
        # The Service network CIDR block. Valid ranges: 10.0.0.0/16-24, 172.16-31.0.0/16-24, 192.168.0.0/16-24. It cannot overlap with the VPC CIDR block 10.1.0.0/21 or CIDR blocks used by existing Kubernetes clusters in the VPC. It cannot be modified after creation.
        # 
        # Default value: 172.19.0.0/20.
        self.service_cidr = service_cidr
        # 【**该字段已废弃**】集群内服务发现类型，用于在`ACK Serverless`集群中指定服务发现方式。
        # 
        # - `CoreDNS`：使用Kubernetes原生标准服务发现组件CoreDNS，需要在集群部署一组容器用于DNS解析。默认采用两个0.25 Core 512 MiB规格的ECI实例。
        # - `PrivateZone`：使用阿里云PrivateZone产品提供服务发现能力，需要开启PrivateZone服务。
        # 
        # 默认值：不开启。
        self.service_discovery_types = service_discovery_types
        # Settings for configuring SNAT for the VPC. Valid values:
        # 
        # - `true`: Use automatic creation of a NAT gateway and configure SNAT rules. Set this to `true` if nodes and applications in the cluster need to access the Internet.
        # - `false`: Do not create a NAT gateway or SNAT rules. Nodes and applications in the cluster cannot access the Internet.
        # 
        # > If this is not enabled during cluster creation and Internet access is needed later, you can [manually enable it](https://help.aliyun.com/document_detail/178480.html).
        # 
        # Default value: `false`.
        self.snat_entry = snat_entry
        # **This field is deprecated.** For control plane node configurations, use the `soc_enabled` parameter under `control_plane_config` instead. For node pool configurations, use the `soc_enabled` parameter under `scaling_group` in `nodepool` instead.
        # 
        # MLPS 2.0 security hardening. For more information, see [ACK MLPS 2.0 security hardening usage instructions](https://help.aliyun.com/document_detail/196148.html).
        # 
        # Valid values:
        # - `true`: Enables MLPS 2.0 security hardening.
        # - `false`: Does not enable MLPS 2.0 security hardening.
        # 
        # Default value: `false`.
        self.soc_enabled = soc_enabled
        # Specifies whether to enable public SSH logon. Used to log on to the master nodes of ACK dedicated clusters. This parameter does not take effect for managed clusters.
        # - `true`: Enable.
        # - `false`: Do not enable.
        # 
        # Default value: `false`.
        self.ssh_flags = ssh_flags
        # The node tags. Tag definition rules:
        # 
        # - Tags are composed of case-sensitive key-value pairs. You can set up to 20 tags.
        # - Tag keys cannot be duplicated and can be up to 64 characters in length. Tag values can be empty and can be up to 128 characters in length. Tag keys and tag values cannot start with "aliyun", "acs:", "https://", or "http://". For more information, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        self.tags = tags
        # **This field is deprecated.** For node pool configurations, use the `taints` parameter under `kubernetes_config` in `nodepool` instead.
        # 
        # The node taint information. Taints and tolerations work together to prevent pods from being scheduled to inappropriate nodes. For more information, see [taint-and-toleration](https://kubernetes.io/zh/docs/concepts/scheduling-eviction/taint-and-toleration/).
        self.taints = taints
        # 【**该字段已废弃**】集群创建失败时默认不会进行回滚，您需要自行清理创建失败的集群。
        # 
        # 集群创建超时时间，单位分钟。
        # 
        # 默认值：`60`。
        self.timeout_mins = timeout_mins
        # The time zone used by the cluster. See [Supported time zones](https://help.aliyun.com/document_detail/354879.html).
        self.timezone = timezone
        # The custom cluster CA.
        self.user_ca = user_ca
        # **This field is deprecated.** The custom node data.
        self.user_data = user_data
        # The VPC used by the cluster. You must provide a VPC when creating a cluster.
        self.vpcid = vpcid
        # The vSwitches for cluster nodes. This field is required when creating a zero-node managed cluster.
        self.vswitch_ids = vswitch_ids
        # 【**该字段已废弃**】节点池配置请使用`nodepool`中`scaling_group`下的`auto_renew`参数代替。
        # 
        # Worker节点是否开启自动续费，当`worker_instance_charge_type`取值为`PrePaid`时才生效，取值：
        # 
        # - `true`：自动续费。
        # - `false`：不自动续费。
        # 
        # 默认值：`true`。
        self.worker_auto_renew = worker_auto_renew
        # 【**该字段已废弃**】节点池配置请使用`nodepool`中`scaling_group`下的`auto_renew_period`参数代替。
        # 
        # 
        # Worker节点自动续费周期，当选择包年包月付费类型时才生效，且为必选值。
        # 
        # 取值范围：{1, 2, 3, 6, 12}。
        self.worker_auto_renew_period = worker_auto_renew_period
        # **This field is deprecated.** For node pool configurations, use the `data_disks` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The data cloud disk type, size, and other configurations for worker nodes.
        self.worker_data_disks = worker_data_disks
        # **This field is deprecated.** For node pool configurations, use the `instance_charge_type` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The billing method for worker nodes. Valid values:
        # 
        # - `PrePaid`: subscription.
        # - `PostPaid`: pay-as-you-go.
        # 
        # Default value: pay-as-you-go.
        self.worker_instance_charge_type = worker_instance_charge_type
        # **This field is deprecated.** For node pool configurations, use the `instance_types` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The instance configuration for worker nodes.
        self.worker_instance_types = worker_instance_types
        # **This field is deprecated.** For node pool configurations, use the `period` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The subscription duration for worker nodes. This parameter takes effect and is required only when `worker_
        self.worker_period = worker_period
        # **This field is deprecated.** For node pool configurations, use the `period_unit` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The billing period unit for worker nodes. This parameter is required when the billing method is `PrePaid`.
        # 
        # Valid values: `Month`. Only monthly billing is supported.
        self.worker_period_unit = worker_period_unit
        # **This field is deprecated.** For node pool configurations, use the `system_disk_category` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The system cloud disk type for worker nodes. For more information, see [Block storage overview](https://help.aliyun.com/document_detail/63136.html).
        # 
        # Valid values:
        # 
        # - `cloud_efficiency`: ultra cloud disk.
        # - `cloud_ssd`: standard SSD.
        # 
        # 
        # Default value: `cloud_ssd`.
        self.worker_system_disk_category = worker_system_disk_category
        # **This field is deprecated.** For node pool configurations, use the `system_disk_performance_level` parameter under `scaling_group` in `nodepool` instead.
        # 
        # When the system cloud disk is an ESSD, you can set the performance level (PL) of the ESSD. For more information, see [ESSD cloud disks](https://help.aliyun.com/document_detail/122389.html).
        # 
        # Valid values:
        # 
        # - PL0
        # - PL1
        # - PL2
        # - PL3
        self.worker_system_disk_performance_level = worker_system_disk_performance_level
        # **This field is deprecated.** For node pool configurations, use the `system_disk_size` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The system cloud disk size for worker nodes. Unit: GiB.
        # 
        # Valid values: [40,500\\].
        # 
        # The value must be greater than or equal to max{40, ImageSize}.
        # 
        # Default value: `120`.
        self.worker_system_disk_size = worker_system_disk_size
        # **This field is deprecated.** For node pool configurations, use the `system_disk_snapshot_policy_id` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The automatic snapshot policy ID for the worker node system cloud disk.
        self.worker_system_disk_snapshot_policy_id = worker_system_disk_snapshot_policy_id
        # **This field is deprecated.** For node pool configurations, use the `vswitch_ids` parameter under `scaling_group` in `nodepool` instead.
        # 
        # The list of vSwitches used by cluster nodes. Each node corresponds to one value.
        # 
        # When creating a zero-node managed cluster, the `worker_vswitch_ids` field is not required, but you must provide `vswitch_ids`.
        self.worker_vswitch_ids = worker_vswitch_ids
        # 【**该字段已废弃**】请使用`zone_ids`参数代替。
        # 
        # 集群所属地域的可用区ID。此参数为ACK托管类的集群特有参数。
        # 
        # 当创建ACK托管类的集群时，如果未指定`vpc_id`和`vswitch_ids`，必须为集群指定`zone_id`，用于自动在该可用区创建VPC网络资源；指定`vpc_id`和`vswitch_ids`时，该参数无效。
        self.zone_id = zone_id
        # The zone IDs of the region where the cluster resides. This parameter is specific to ACK managed cluster types.
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
        # The data cloud disk type.
        # 
        # This parameter is required.
        self.category = category
        # Specifies whether to encrypt the data cloud disk. Valid values:
        # 
        # - `true`: Encrypts the data cloud disk.
        # - `false`: Does not encrypt the data cloud disk.
        # 
        # Default value: `false`.
        self.encrypted = encrypted
        # The performance level of the node data cloud disk. This parameter takes effect only for [ESSD cloud disks](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The data cloud disk size. Valid values: 40 to 32767. Unit: GiB.
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
        # Specifies whether to enable RRSA.
        # 
        # - true: Enable.
        # 
        # - false: Do not enable.
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
        # - patch: Automatically upgrades to the available patch version of the current minor version. The new Kubernetes version does not contain breaking changes.
        # - stable: Automatically upgrades to the latest patch version of the second-latest minor version. The new Kubernetes version may involve API and feature changes, but its stability has been widely validated.
        # - rapid: Automatically upgrades to the latest patch version of the latest minor version to gain access to new Kubernetes community features faster.
        self.channel = channel
        # Specifies whether to enable cluster auto-upgrade.
        # 
        # - true: Enable.
        # 
        # - false: Do not enable.
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
        # The internal DNS configuration for the cluster. Applicable to ACK managed clusters. The internal domain name is used by node-side system components such as kubelet and kube-proxy to access the API Server. When internal domain name access is not enabled, node-side system components access the API Server through the CLB IP address.
        self.internal_dns_config = internal_dns_config
        # The cluster endpoint configuration. When this field is specified, the endpoint_public_access and load_balancer_id parameters do not take effect. ACK only supports automatic creation of NLB instances. To specify a CLB/NLB, use load_balancers_config to specify the instance ID.
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
        # The VPCs where the internal domain name record resolution takes effect.
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
        # Specifies whether to enable auto-renewal for control plane nodes. Takes effect when the billing method is `PrePaid`.
        # - true: Enable auto-renewal.
        # - false: Do not enable auto-renewal.
        # 
        # Default value: true.
        self.auto_renew = auto_renew
        # The auto-renewal period of control plane nodes.
        # 
        # Valid values: {1, 2, 3, 6, 12}. Unit: months.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # The billing method of control plane nodes.
        # 
        # - `PrePaid`: Subscription.
        # - `PostPaid`: Pay-as-you-go.
        # 
        # Default value: `PostPaid`.
        self.charge_type = charge_type
        # Specifies whether to install CloudMonitor on nodes.
        # 
        # - true: Installs the CloudMonitor agent.
        # 
        # - false: Does not install the CloudMonitor agent.
        # 
        # Default value: false.
        self.cloud_monitor_flags = cloud_monitor_flags
        # The node CPU management policy.
        # 
        # - static: Allows pods with certain resource characteristics on the node to be granted enhanced CPU affinity and exclusivity.
        # 
        # - none: Uses the existing default CPU affinity scheme.
        # 
        # Default value: none.
        self.cpu_policy = cpu_policy
        # The deployment set ID.
        self.deploymentset_id = deploymentset_id
        # The image ID.
        self.image_id = image_id
        # The operating system image type.
        self.image_type = image_type
        # The instance metadata access configuration for ECS instances.
        self.instance_metadata_options = instance_metadata_options
        # The node instance types.
        self.instance_types = instance_types
        # The key pair name. Mutually exclusive with login_password.
        self.key_pair = key_pair
        # The SSH logon password. Must be 8 to 30 characters in length and contain at least three of the following: uppercase letters, lowercase letters, digits, and special characters. Mutually exclusive with key_pair.
        self.login_password = login_password
        # **This field is deprecated.** The node service port range.
        self.node_port_range = node_port_range
        # The subscription duration of control plane nodes. Valid and required when the billing method is `PrePaid`.
        # 
        # Valid values: {1, 2, 3, 6, 12, 24, 36, 48, 60}. Unit: months.
        # 
        # Default value: 1.
        self.period = period
        # The subscription period unit of control plane nodes. Valid and required when the billing method is `PrePaid`.
        # 
        # Valid value: `Month`. Currently, only monthly periods are supported.
        self.period_unit = period_unit
        # **This field is deprecated.** The container runtime for control plane nodes. Valid values:
        # 
        # containerd: The Containerd runtime, which supports all cluster versions.
        self.runtime = runtime
        # Specifies whether to enable Alibaba Cloud OS security hardening.
        # 
        # - true: Enables Alibaba Cloud OS security hardening.
        # 
        # - false: Does not enable Alibaba Cloud OS security hardening.
        # 
        # Default value: false.
        self.security_hardening_os = security_hardening_os
        # The number of control plane nodes.
        # 
        # Valid values: `3` or `5`.
        self.size = size
        # Specifies whether to enable MLPS 2.0 security hardening.
        # 
        # - true: Enables MLPS 2.0 security hardening.
        # 
        # - false: Does not enable MLPS 2.0 security hardening.
        # 
        # Default value: false.
        self.soc_enabled = soc_enabled
        # Specifies whether to enable burst (performance burst) for the node system cloud disk.
        # 
        # - true: Enabled.
        # 
        # - false: Not enabled.
        # 
        # This parameter is supported only when `system_disk_category` is set to `cloud_auto`.
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The node system disk type.
        # 
        # - `cloud_efficiency`: Ultra disk.
        # - `cloud_ssd`: Standard SSD.
        # - `cloud_essd`: ESSD.
        # - `cloud_auto`: ESSD AutoPL.
        # - `cloud_essd
        self.system_disk_category = system_disk_category
        # The performance level of the node system cloud disk. This parameter takes effect only for ESSD cloud disks.
        # 
        # The performance level varies based on the cloud disk size. For more information, see [ESSD cloud disks](https://help.aliyun.com/document_detail/122389.html).
        self.system_disk_performance_level = system_disk_performance_level
        # The provisioned read/write IOPS for the node system cloud disk.
        # 
        # Valid values: 0 to min{50,000, 1000 × capacity - baseline performance}. Baseline performance = min{1,800 + 50 × capacity, 50000}.
        # 
        # This parameter is supported only when `system_disk_category` is set to `cloud_auto`.
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The size of the node system cloud disk.
        # 
        # Valid values: [40,500\\]. Unit: GiB.
        # 
        # Default value: `120`.
        self.system_disk_size = system_disk_size
        # The automatic snapshot backup policy for nodes.
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
        # 
        # - true: Enable.
        # 
        # - false: Do not enable.
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
        # 
        # - true: Enable.
        # 
        # - false: Do not enable.
        self.enabled = enabled
        # The [SLS Project](https://help.aliyun.com/document_detail/48873.html) that contains the cluster audit log [Logstore](https://help.aliyun.com/document_detail/48873.html).
        # 
        # - Default value: `k8s-log-{clusterid}`.
        # 
        # - After the cluster audit log feature is enabled, a Logstore for cluster audit logs is created in the specified SLS Project.
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

