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
        # The network access control list (ACL) rule of the SLB instance associated with the API server if the cluster is a registered cluster.
        self.access_control_list = access_control_list
        # The components that you want to install in the cluster. When you create a cluster, you can configure the `addons` parameter to specify the components that you want to install.
        # 
        # **Network plug-in**: required. The Flannel and Terway plug-ins are supported. Select one of the plug-ins for the cluster.
        # 
        # *   If you want to use the Terway component, specify the network plug-in in the [{"name":"flannel","config":""}] format.
        # *   If you want to use the Terway component, specify the value network plug-in in the [{"name": "terway-eniip","Config": ""}] format.
        # 
        # **Volume plug-in**: optional. Only the `Container Storage Interface (CSI)` plug-in is supported.
        # 
        # Specify the `CSI` plug-in in the following format: [{"name":"csi-plugin","config": ""},{"name": "csi-provisioner","config": ""}].
        # 
        # **Simple Log Service component**: optional. We recommend that you enable Simple Log Service. If Simple Log Service is disabled, you cannot use the cluster auditing feature.
        # 
        # *   Specify an existing `Simple Log Service project` in the following format: [{"name": "logtail-ds","config": "{"IngressDashboardEnabled":"true","sls_project_name":"your_sls_project_name"}"}].
        # *   To create a `Simple Log Service project`, specify the component in the following format: [{"name": "logtail-ds","config": "{"IngressDashboardEnabled":"true"}"}].
        # 
        # **Ingress controller**: optional. By default, the `nginx-ingress-controller` component is installed in ACK dedicated clusters.
        # 
        # *   To install nginx-ingress-controller and enable Internet access, specify the Ingress controller in the following format: [{"name":"nginx-ingress-controller","config":"{"IngressSlbNetworkType":"internet"}"}].
        # *   To disable the automatic installation of nginx-ingress-controller, specify the Ingress controller in the following format: [{"name": "nginx-ingress-controller","config": "","disabled": true}].
        # 
        # **Event center**: optional. By default, the event center feature is enabled.
        # 
        # You can use ACK event centers to store and query events and configure alerts. You can use the Logstores that are associated with ACK event centers free of charge within 90 days. For more information, see [Create and use an event center](https://help.aliyun.com/document_detail/150476.html).
        # 
        # To enable the event center feature, specify the event center component in the following format: [{"name":"ack-node-problem-detector","config":"{"sls_project_name":"your_sls_project_name"}"}].
        self.addons = addons
        # Service accounts provide identities for pods when pods communicate with the `API server` of the cluster. The `api-audiences` parameter validates `tokens` and is used by the `API server` to check whether the `tokens` of requests are valid. Separate multiple values with commas (,).``
        # 
        # For more information about `service accounts`, see [Enable service account token volume projection](https://help.aliyun.com/document_detail/160384.html).
        self.api_audiences = api_audiences
        self.audit_log_config = audit_log_config
        self.auto_mode = auto_mode
        # [**Deprecated**]
        # 
        # Specifies whether to enable auto-renewal. This parameter takes effect only when `charge_type` is set to `PrePaid`. Valid values:
        # 
        # *   `true`: enables auto-renewal.
        # *   `false`: disables auto-renewal.
        # 
        # Default value: `false`.
        # 
        # This parameter was changed on October 15, 2024. For more information, see [Announcement on changes to the parameter behavior of the CreateCluster operation](https://help.aliyun.com/document_detail/2849194.html).
        self.auto_renew = auto_renew
        # [**Deprecated**]
        # 
        # The auto-renewal duration. This parameter takes effect only if charge_type is set to PrePaid and auto_renew is set to true. If you set `period_unit` to Month, the valid values of auto_renew_period are 1, 2, 3, 6, and 12.
        # 
        # Default value: 1.
        # 
        # This parameter was changed on October 15, 2024. For more information, see [Announcement on changes to the parameter behavior of the CreateCluster operation](https://help.aliyun.com/document_detail/2849194.html).
        self.auto_renew_period = auto_renew_period
        # [**Deprecated**]
        # 
        # The billing method of the CLB instance that is used by the API server. Default value: PostPaid. Valid values:
        # 
        # *   PostPaid: pay-as-you-go.
        # *   PrePaid: subscription. This billing method is not supported by newly created CLB instances. Existing CLB instances are not affected.
        # 
        # > 
        # 
        # *   This parameter was changed on October 15, 2024. For more information, see [Announcement on changes to the parameter behavior of the CreateCluster operation](https://help.aliyun.com/document_detail/2849194.html).
        # 
        # *   Starting from December 1, 2024, newly created CLB instances no longer support the subscription billing method, and an instance fee will be charged for newly created CLB instances
        # 
        # For more information, see [CLB billing adjustments](https://help.aliyun.com/document_detail/2839797.html).
        self.charge_type = charge_type
        # [Deprecated] When you configure the control plane, use the `security_hardening_os` parameter in the `control_plane_config` section instead. When you configure a node pool, use the `security_hardening_os` parameter of the `scaling_group` field in the `nodepool` section instead.
        self.cis_enabled = cis_enabled
        # [**Deprecated**] When you configure the control plane, use the `cloud_monitor_flags` parameter in the `control_plane_config` section instead. When you configure a node pool, use the `cms_enabled` parameter of the `kubernetes_config` field in the nodepool section instead.
        # 
        # Specifies whether to install the CloudMonitor agent. Valid values:
        # 
        # *   `true`: installs the CloudMonitor agent.
        # *   `false`: does not install the CloudMonitor agent.
        # 
        # Default value: `false`.
        self.cloud_monitor_flags = cloud_monitor_flags
        # The domain name of the cluster.
        # 
        # The domain name can contain one or more parts that are separated by periods (.). Each part cannot exceed 63 characters in length, and can contain lowercase letters, digits, and hyphens (-). Each part must start and end with a lowercase letter or digit.
        self.cluster_domain = cluster_domain
        # If you set `cluster_type` to `ManagedKubernetes` and specify `profile`, you can further specify the edition of the cluster. Valid values:
        # 
        # *   `ack.pro.small`: Pro Edition.
        # *   `ack.standard`: Basic Edition. If you leave the parameter empty, an ACK Basic cluster is created.
        self.cluster_spec = cluster_spec
        # *   `Kubernetes`: ACK dedicated cluster.
        # *   `ManagedKubernetes`: ACK managed cluster. ACK managed clusters include ACK Basic clusters, ACK Pro clusters, ACK Serverless clusters (Basic Edition and Pro Edition), ACK Edge clusters (Basic Edition and Pro Edition), and ACK Lingjun clusters (Pro Edition).
        # *   `ExternalKubernetes`: registered cluster.
        self.cluster_type = cluster_type
        # The pod CIDR block. You can specify 10.0.0.0/8, 172.16-31.0.0/12-16, 192.168.0.0/16, or their subnets as the pod CIDR block. The pod CIDR block cannot overlap with the CIDR block of the VPC in which the cluster is deployed and the CIDR blocks of existing clusters in the VPC. You cannot modify the pod CIDR block after you create the cluster.
        # 
        # For more information about how to plan the network of an ACK cluster, see [Plan the network of an ACK cluster](https://help.aliyun.com/document_detail/86500.html).
        # 
        # >  This parameter is required if the cluster uses the Flannel plug-in.
        self.container_cidr = container_cidr
        # The control plane configurations of an ACK dedicated cluster.
        self.control_plane_config = control_plane_config
        # The control plane components for which you want to enable log collection.
        # 
        # By default, the logs of kube-apiserver, kube-controller-manager, and kube-scheduler are collected.
        self.controlplane_log_components = controlplane_log_components
        # The Simple Log Service project that is used to store the logs of control plane components. You can use an existing project or create one. If you choose to create a Simple Log Service project, the created project is named in the `k8s-log-{ClusterID}` format.
        self.controlplane_log_project = controlplane_log_project
        # The retention period of control plane logs in days.
        self.controlplane_log_ttl = controlplane_log_ttl
        # [**Deprecated**] When you configure the control plane, use the `cpu_policy` parameter in the `control_plane_config` section instead. When you configure a node pool, use the `cpu_policy` parameter of the `kubernetes_config` field in the `nodepool` section instead.
        # 
        # The CPU management policy of the node. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later:
        # 
        # *   `static`: allows pods with specific resource characteristics on the node to be granted enhanced CPU affinity and exclusivity.
        # *   `none`: specifies that the default CPU affinity is used.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # The custom subject alternative names (SANs) for the API server certificate to accept requests from specified IP addresses or domain names. Separate multiple IP addresses and domain names with commas (,).
        self.custom_san = custom_san
        # Specifies whether to enable cluster deletion protection. If you enable this option, the cluster cannot be deleted in the console or by calling API operations. Valid values:
        # 
        # *   `true`: enables cluster deletion protection.
        # *   `false`: disables cluster deletion protection.
        # 
        # Default value: `false`.
        self.deletion_protection = deletion_protection
        # [**Deprecated**] By default, the system does not perform a rollback when the cluster fails to be created. You must manually delete the cluster that fails to be created.
        # 
        # Specifies whether to perform a rollback when the cluster fails to be created. Valid values:
        # 
        # *   `true`: performs a rollback when the cluster fails to be created.
        # *   `false`: does not perform a rollback when the cluster fails to be created.
        # 
        # Default value: `true`.
        self.disable_rollback = disable_rollback
        # Specifies whether to enable the RAM Roles for Service Accounts (RRSA) feature.
        self.enable_rrsa = enable_rrsa
        # The ID of the Key Management Service (KMS) key that is used to encrypt the system disk. For more information, see [What is KMS?](https://help.aliyun.com/document_detail/28935.html)
        # 
        # >  The key can be used only in ACK Pro clusters.
        self.encryption_provider_key = encryption_provider_key
        # Specifies whether to enable Internet access for the cluster. You can use an elastic IP address (EIP) to expose the API server. This way, you can access the cluster over the Internet. Valid values:
        # 
        # *   `true`: enables Internet access for the cluster.
        # *   `false`: disables Internet access for the cluster. If you set the value to false, the API server cannot be accessed over the Internet.
        # 
        # Default value: `false`.
        self.endpoint_public_access = endpoint_public_access
        self.extra_sans = extra_sans
        # [**Deprecated**] When you configure a node pool, you cannot add existing nodes to the cluster. If you want to add existing nodes, you must first create a node pool and then call the [AttachInstancesToNodePool](https://help.aliyun.com/document_detail/2667920.html) operation.
        # 
        # Specifies whether to mount a data disk to a node that is created based on an existing ECS instance. Valid values:
        # 
        # *   `true`: stores the data of containers and images on a data disk. The existing data stored in the data disk is lost. Back up the existing data first.
        # *   `false`: does not store the data of containers and images on a data disk.
        # 
        # Default value: `false`.
        # 
        # How data disks are mounted:
        # 
        # *   If an ECS instance has data disks mounted and the file system of the last data disk is not initialized, the system automatically formats the data disk to ext4. Then, the system mounts the data disk to /var/lib/docker and /var/lib/kubelet.
        # *   If no data disk is mounted to the ECS instance, the system does not purchase a new data disk.
        self.format_disk = format_disk
        # [**Deprecated**] When you configure the control plane, use the `image_id` parameter in the `control_plane_config` section instead. When you configure a node pool, use the `image_id` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The custom image for nodes. By default, the image provided by ACK is used. You can select a custom image to replace the default image. For more information, see [Use a custom image to create an ACK cluster](https://help.aliyun.com/document_detail/146647.html).
        self.image_id = image_id
        # [**Deprecated**] When you configure the control plane, use the `image_type` parameter in the `control_plane_config` section instead. When you configure a node pool, use the `image_type` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The type of OS distribution that you want to use. To specify the node OS, we recommend that you use this parameter. Valid values:
        # 
        # *   CentOS
        # *   AliyunLinux
        # *   AliyunLinux Qboot
        # *   AliyunLinuxUEFI
        # *   AliyunLinux3
        # *   Windows
        # *   WindowsCore
        # *   AliyunLinux3Arm64
        # *   ContainerOS
        # 
        # Default value: `CentOS`.
        self.image_type = image_type
        # [**Deprecated**] When you configure a node pool, you cannot add existing nodes to the cluster. If you want to add existing nodes, you must first create a node pool and then call the [AttachInstancesToNodePool](https://help.aliyun.com/document_detail/2667920.html) operation.
        # 
        # The existing ECS instances that are specified as worker nodes for the cluster.
        # 
        # >  This parameter is required if you create worker nodes on existing ECS instances.
        self.instances = instances
        # The IP stack of the cluster.
        self.ip_stack = ip_stack
        # Specifies whether to create an advanced security group. This parameter takes effect only if `security_group_id` is left empty.
        # 
        # >  To use a basic security group, make sure that the sum of the number of nodes in the cluster and the number of pods that use Terway does not exceed 2,000. Therefore, we recommend that you specify an advanced security group for a cluster that uses Terway.
        # 
        # *   `true`: creates an advanced security group.
        # *   `false`: does not create an advanced security group.
        # 
        # Default value: `true`.
        self.is_enterprise_security_group = is_enterprise_security_group
        # [**Deprecated**] When you configure a node pool, you cannot add existing nodes to the cluster. If you want to add existing nodes, you must first create a node pool and then call the [AttachInstancesToNodePool](https://help.aliyun.com/document_detail/2667920.html) operation.
        # 
        # Specifies whether to retain the names of existing ECS instances that are used in the cluster. Valid values:
        # 
        # *   `true`: retains the names.
        # *   `false`: does not retain the names. The system assigns new names.
        # 
        # Default value: `true`.
        self.keep_instance_name = keep_instance_name
        # [**Deprecated**] When you configure the control plane, use the `key_pair` parameter in the `control_plane_config` section instead. When you configure a node pool, use the `key_pair` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The name of the key pair. You must configure this parameter or `login_password`.
        self.key_pair = key_pair
        # The Kubernetes version of the cluster. The Kubernetes versions supported by ACK are the same as the Kubernetes versions supported by open source Kubernetes. We recommend that you specify the latest Kubernetes version. If you do not specify this parameter, the latest Kubernetes version is used.
        # 
        # You can create ACK clusters of the latest three Kubernetes versions in the ACK console. If you want to create clusters that run earlier Kubernetes versions, use the ACK API. For more information about the Kubernetes versions supported by ACK, see [Support for Kubernetes versions](https://help.aliyun.com/document_detail/185269.html).
        self.kubernetes_version = kubernetes_version
        # Specifies the ID of the CLB instance for accessing the API server. If this parameter is specified, the system does not automatically create a CLB instance for the API server.
        # 
        # >  Make sure that the CLB instance does not have other dependencies, such as listeners and backend servers. You cannot specify shared-resource or Internet-facing CLB instances.
        self.load_balancer_id = load_balancer_id
        # [**Deprecated**] The pay-as-you-go billing method is used by Classic Load Balancer (CLB) instances. This parameter does not take effect.
        # 
        # The specification of the Server Load Balancer (SLB) instance. Valid values:
        # 
        # *   slb.s1.small
        # *   slb.s2.small
        # *   slb.s2.medium
        # *   slb.s3.small
        # *   slb.s3.medium
        # *   slb.s3.large
        # 
        # Default value: `slb.s2.small`.
        self.load_balancer_spec = load_balancer_spec
        # Enables Simple Log Service for the cluster. This parameter takes effect only for ACK Serverless clusters. Set the value to `SLS`.
        self.logging_type = logging_type
        # [**Deprecated**] When you configure the control plane, use the `login_password` parameter in the `control_plane_config` section instead. When you configure a node pool, use the `login_password` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The password for SSH logon. You must set this parameter or `key_pair`. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        self.login_password = login_password
        # The configurations of the cluster maintenance window.
        self.maintenance_window = maintenance_window
        # [**Deprecated**] When you configure the control plane, use the `auto-renew` parameter in the `control_plane_config` section instead.
        # 
        # Specifies whether to enable auto-renewal for master nodes. This parameter takes effect only when `master_instance_charge_type` is set to `PrePaid`. Valid values:
        # 
        # *   `true`: enables auto-renewal.
        # *   `false`: disables auto-renewal.
        # 
        # Default value: `true`.
        self.master_auto_renew = master_auto_renew
        # [**Deprecated**] When you configure the control plane, use the `auto-renew_period` parameter in the `control_plane_config` section instead.
        # 
        # The auto-renewal duration. This parameter takes effect and is required only when the subscription billing method is selected for master nodes.
        # 
        # Valid values: 1, 2, 3, 6, and 12.
        # 
        # Default value: 1.
        self.master_auto_renew_period = master_auto_renew_period
        # [**Deprecated**] When you configure the control plane, use the `size` parameter in the `control_plane_config` section instead.
        # 
        # The number of master nodes. Valid values: `3` and `5`.
        # 
        # Default value: `3`.
        self.master_count = master_count
        # [**Deprecated**] When you configure the control plane, use the `instance_charge_type` parameter in the `control_plane_config` section instead.
        # 
        # The billing method of master nodes. Valid values:
        # 
        # *   `PrePaid`: subscription.
        # *   `PostPaid`: pay-as-you-go.
        # 
        # Default value: `PostPaid`.
        self.master_instance_charge_type = master_instance_charge_type
        # [**Deprecated**] When you configure the control plane, use the `instance_types` parameter in the `control_plane_config` section instead.
        # 
        # The instance types of master nodes. For more information, see [Overview of instance families](https://help.aliyun.com/document_detail/25378.html).
        self.master_instance_types = master_instance_types
        # [**Deprecated**] When you configure the control plane, use the `unit` parameter in the `control_plane_config` section instead.
        # 
        # The subscription duration of master nodes. This parameter takes effect and is required only when `master_instance_charge_type` is set to `PrePaid`.
        # 
        # Valid values: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # Default value: 1.
        self.master_period = master_period
        # [**Deprecated**] When you configure the control plane, use the `period_unit` parameter in the `control_plane_config` section instead.
        # 
        # The billing cycle of the master nodes in the cluster. This parameter is required if master_instance_charge_type is set to `PrePaid`.
        # 
        # Valid value: `Month`, which indicates that master nodes are billed only on a monthly basis.
        self.master_period_unit = master_period_unit
        # [**Deprecated**] When you configure the control plane, use the `system_disk_category` parameter in the `control_plane_config` section instead.
        # 
        # The system disk category of master nodes. Valid values:
        # 
        # *   `cloud_efficiency`: ultra disk.
        # *   `cloud_ssd`: standard SSD.
        # *   `cloud_essd`: Enterprise SSD (ESSD).
        # 
        # Default value: `cloud_ssd`. The default value may vary in different zones.
        self.master_system_disk_category = master_system_disk_category
        # [**Deprecated**] When you configure the control plane, use the `system_disk_performance_level` parameter in the `control_plane_config` section instead.
        # 
        # The performance level (PL) of the system disk that you want to use for master nodes. This parameter takes effect only for ESSDs. For more information about the relationship between disk PLs and disk sizes, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        self.master_system_disk_performance_level = master_system_disk_performance_level
        # [**Deprecated**] When you configure the control plane, use the `system_disk_disk` parameter in the `control_plane_config` section instead.
        # 
        # The system disk size of master nodes. Valid values: 40 to 500. Unit: GiB.
        # 
        # Default value: `120`.
        self.master_system_disk_size = master_system_disk_size
        # [**Deprecated**] When you configure the control plane, use the `system_disk_snapshot_policy_id` parameter in the `control_plane_config` section instead.
        # 
        # The ID of the automatic snapshot policy that is used by the system disk specified for master nodes.
        self.master_system_disk_snapshot_policy_id = master_system_disk_snapshot_policy_id
        # [**Deprecated**] Use the `vswitch_ids` parameter instead.
        # 
        # The IDs of the vSwitches that are specified for master nodes. You can specify up to three vSwitches. We recommend that you specify three vSwitches in different zones to ensure high availability.
        # 
        # The number of vSwitches must be the same as the value of the `master_count` parameter and also the same as the number of vSwitches specified in the `master_vswitch_ids` parameter.
        self.master_vswitch_ids = master_vswitch_ids
        # The cluster name.
        # 
        # The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). The name cannot start with a hyphen (-).
        # 
        # This parameter is required.
        self.name = name
        # [Deprecated] Use the `snat_entry` parameter instead.
        self.nat_gateway = nat_gateway
        # The maximum number of IP addresses that can be assigned to each node. This number is determined by the subnet mask of the specified CIDR block. This parameter takes effect only if the cluster uses the Flannel plug-in.
        # 
        # Default value: `26`.
        self.node_cidr_mask = node_cidr_mask
        # [**Deprecated**] When you configure a node pool, use the `node_name_mode` parameter of the `kubernetes_config` field in the `nodepool` section instead.
        # 
        # The custom node name.
        # 
        # A custom node name consists of a prefix, a node IP address, and a suffix.
        # 
        # *   The prefix and suffix can contain multiple parts that are separated by periods (.). Each part can contain lowercase letters, digits, and hyphens (-), and must start and end with a lowercase letter or digit.
        # *   The IP substring length specifies the number of digits to be truncated from the end of the node IP address. The IP substring length ranges from 5 to 12.
        # 
        # For example, if the node IP address is 192.168.0.55, the prefix is aliyun.com, the IP substring length is 5, and the suffix is test, the node name will aliyun.com00055test.
        self.node_name_mode = node_name_mode
        # The node port range. Valid values: 30000 to 65535.
        # 
        # Default value: `30000-32767`.
        self.node_port_range = node_port_range
        # The list of node pools.
        self.nodepools = nodepools
        # [**Deprecated**] When you configure a node pool, use the `desired_size` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The number of worker nodes. Valid values: 0 to 100.
        self.num_of_nodes = num_of_nodes
        # The automatic O\\&M policy of the cluster.
        self.operation_policy = operation_policy
        # [**Deprecated**] When you configure the control plane, use the `image_type` parameter in the `control_plane_config` section instead. When you configure a node pool, use the `image_type` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The type of OS. Valid values:
        # 
        # *   Windows
        # *   Linux
        # 
        # Default value: `Linux`.
        self.os_type = os_type
        # [**Deprecated**]
        # 
        # The subscription duration. This parameter takes effect and is required only when you set charge_type to PrePaid.
        # 
        # Valid values: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # Default value: 1.
        # 
        # This parameter was changed on October 15, 2024. For more information, see [Announcement on changes to the parameter behavior of the CreateCluster operation](https://help.aliyun.com/document_detail/2849194.html).
        self.period = period
        # [**Deprecated**]
        # 
        # The billing cycle. This parameter is required if charge_type is set to PrePaid.
        # 
        # Valid value: Month, which indicates that resources are billed only on a monthly basis.
        # 
        # This parameter was changed on October 15, 2024. For more information, see [Announcement on changes to the parameter behavior of the CreateCluster operation](https://help.aliyun.com/document_detail/2849194.html).
        self.period_unit = period_unit
        # [**Deprecated**] When you configure a node pool, use the `platform` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The OS distribution that is used. Valid values:
        # 
        # *   CentOS
        # *   AliyunLinux
        # *   QbootAliyunLinux
        # *   Qboot
        # *   Windows
        # *   WindowsCore
        # 
        # Default value: `CentOS`.
        self.platform = platform
        # If you select Terway as the network plug-in, you must allocate vSwitches to pods. For each vSwitch that allocates IP addresses to worker nodes, you must select a vSwitch in the same zone to allocate IP addresses to pods.
        # 
        # >  We recommend that you select pod vSwitches whose subnet masks do not exceed 19 bits in length. The maximum subnet mask length of a pod vSwitch is 25 bits. If you select a pod vSwitch whose subnet mask exceeds 25 bits in length, the IP addresses that can be allocated to pods may be insufficient.
        self.pod_vswitch_ids = pod_vswitch_ids
        # If you set `cluster_type` to `ManagedKubernetes`, an ACK managed cluster is created. In this case, you can further specify the cluster edition. Valid values:
        # 
        # *   `Default`: ACK managed cluster. ACK managed clusters include ACK Basic clusters and ACK Pro clusters.
        # *   `Edge`: ACK Edge cluster. ACK Edge clusters include ACK Edge Basic clusters and ACK Edge Pro clusters.
        # *   `Serverless`: ACK Serverless cluster. ACK Serverless clusters include ACK Serverless Basic clusters and ACK Serverless Pro clusters.
        # *   `Lingjun`: ACK Lingjun Pro cluster.
        self.profile = profile
        # The kube-proxy mode. Valid values:
        # 
        # *   `iptables`: a mature and stable mode that uses iptables rules to conduct service discovery and load balancing. The performance of this mode is limited by the size of the cluster. This mode is suitable for clusters that run a small number of Services.
        # *   `ipvs`: a mode that provides high performance and uses IP Virtual Server (IPVS) to conduct service discovery and load balancing. This mode is suitable for clusters that run a large number of Services. We recommend that you use this mode in scenarios that require high-performance load balancing.
        # 
        # Default value: `ipvs`.
        self.proxy_mode = proxy_mode
        # [**Deprecated**] When you configure a node pool, use the `rds_instances` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The ApsaraDB RDS instances. The pod CIDR block and node CIDR block are added to the whitelists of the ApsaraDB RDS instances. We recommend that you add the pod CIDR block and node CIDR block to the whitelists of the ApsaraDB RDS instances in the ApsaraDB RDS console. If the RDS instances are not in the Running state, new nodes cannot be added to the cluster.
        self.rds_instances = rds_instances
        # The ID of the region in which the cluster is deployed. For more information about the regions supported by ACK, see [Regions supported by ACK](https://help.aliyun.com/document_detail/216938.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the cluster belongs. You can use resource groups to isolate clusters.
        self.resource_group_id = resource_group_id
        self.rrsa_config = rrsa_config
        # The container runtime. The default container runtime is Docker. containerd and Sandboxed-Container are also supported.
        # 
        # For more information about how to select a proper container runtime, see [Comparison among Docker, containerd, and Sandboxed-Container](https://help.aliyun.com/document_detail/160313.html).
        self.runtime = runtime
        # The ID of an existing security group. You must specify this parameter or `is_enterprise_security_group`. Cluster nodes are automatically added to the security group.
        self.security_group_id = security_group_id
        # [**Deprecated**] When you configure the control plane, use the `security_hardening_os` parameter in the `control_plane_config` section instead. When you configure a node pool, use the `security_hardening_os` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # Specifies whether to enable Alibaba Cloud Linux Security Hardening. Valid values:
        # 
        # *   `true`: enables Alibaba Cloud Linux Security Hardening.
        # *   `false`: disables Alibaba Cloud Linux Security Hardening.
        # 
        # Default value: `false`.
        self.security_hardening_os = security_hardening_os
        # Service accounts provide identities for pods when pods communicate with the `API server` of the cluster. `service-account-issuer` specifies the issuer of the `serviceaccount token`, which is specified by using the `iss` field in the `token payload`.
        # 
        # For more information about `ServiceAccount`, see [Enable service account token volume projection](https://help.aliyun.com/document_detail/160384.html).
        self.service_account_issuer = service_account_issuer
        # The Service CIDR block. Valid values: 10.0.0.0/16-24, 172.16-31.0.0/16-24, and 192.168.0.0/16-24. The Service CIDR block cannot overlap with the VPC CIDR block (10.1.0.0/21) or the CIDR blocks of existing clusters in the VPC. You cannot modify the Service CIDR block after the cluster is created.
        # 
        # By default, the Service CIDR block is set to 172.19.0.0/20.
        self.service_cidr = service_cidr
        # The methods for implementing service discovery in `ACK Serverless` clusters.
        # 
        # *   `CoreDNS`: a standard service discovery plug-in that is provided by open source Kubernetes. To use DNS resolution, you must provision pods. By default, two elastic container instances are used. The specification of each instance is 0.25 vCores and 512 MiB of memory.
        # *   `PrivateZone`: a DNS resolution service provided by Alibaba Cloud. You must activate Alibaba Cloud DNS PrivateZone before you can use it for service discovery.
        # 
        # By default, this parameter is not specified.
        self.service_discovery_types = service_discovery_types
        # Specifies whether to configure SNAT rules for the VPC in which your cluster is deployed. Valid values:
        # 
        # *   `true`: automatically creates a NAT gateway and configures SNAT rules. Set the value to `true` if nodes and applications in the cluster need to access the Internet.
        # *   `false`: does not create a NAT gateway or configure SNAT rules. In this case, nodes and applications in the cluster cannot access the Internet.
        # 
        # >  If this feature is disabled when you create the cluster, you can also manually enable this feature after you create the cluster. For more information, see [Enable an existing ACK cluster to access the Internet](https://help.aliyun.com/document_detail/178480.html).
        # 
        # Default value: `true`.
        self.snat_entry = snat_entry
        # [**Deprecated**] When you configure the control plane, use the `soc_enabled` parameter in the `control_plane_config` section instead. When you configure a node pool, use the `soc_enabled` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # Specifies whether to enable Multi-Level Protection Scheme (MLPS) security hardening. For more information, see [ACK security hardening based on MLPS](https://help.aliyun.com/document_detail/196148.html).
        # 
        # Valid values:
        # 
        # *   `true`: enables MLPS security hardening.
        # *   `false`: disables MLPS security hardening.
        # 
        # Default value: `false`.
        self.soc_enabled = soc_enabled
        # Specifies whether to enable SSH logon. If this parameter is set to true, you can log on to master nodes in an ACK dedicated cluster over the Internet. This parameter does not take effect for ACK managed clusters. Valid values:
        # 
        # *   `true`: enables SSH logon.
        # *   `false`: disables SSH logon.
        # 
        # Default value: `false`.
        self.ssh_flags = ssh_flags
        # The labels that you want to add to nodes. You must add labels based on the following rules:
        # 
        # *   A label is a case-sensitive key-value pair. You can add up to 20 labels.
        # *   When you add a label, you must specify a unique key, but you can leave the value empty. A key cannot exceed 64 characters in length, and a value cannot exceed 128 characters in length. Keys and values cannot start with aliyun, acs:, https://, or http://. For more information, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        self.tags = tags
        # [**Deprecated**] When you configure a node pool, use the `taints` parameter of the `kubernetes_config` field in the `nodepool` section instead.
        # 
        # The taints that you want to add to nodes. Taints can be used together with tolerations to avoid scheduling pods to specific nodes. For more information, see [taint-and-toleration](https://kubernetes.io/zh/docs/concepts/scheduling-eviction/taint-and-toleration/).
        self.taints = taints
        # [**Deprecated**] By default, the system does not perform a rollback when the cluster fails to be created. You must manually delete the cluster that fails to be created.
        # 
        # Specifies the timeout period of cluster creation. Unit: minutes.
        # 
        # Default value: `60`.
        self.timeout_mins = timeout_mins
        # The time zone of the cluster.
        self.timezone = timezone
        # The custom Certificate Authority (CA) certificate used by the cluster.
        self.user_ca = user_ca
        # The user data of nodes.
        self.user_data = user_data
        # The virtual private cloud (VPC) in which you want to deploy the cluster. This parameter is required.
        self.vpcid = vpcid
        # The vSwitches for nodes in the cluster. This parameter is required if you create an ACK managed cluster that does not contain nodes.
        self.vswitch_ids = vswitch_ids
        # [**Deprecated**] When you configure a node pool, use the `auto_renew` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # Specifies whether to enable auto-renewal for worker nodes. This parameter takes effect and is required only when `worker_instance_charge_type` is set to `PrePaid`. Valid values:
        # 
        # *   `true`: enables auto-renewal.
        # *   `false`: disables auto-renewal.
        # 
        # Default value: `true`.
        self.worker_auto_renew = worker_auto_renew
        # [**Deprecated**] When you configure a node pool, use the `auto_renew_period` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The auto-renewal duration of worker nodes. This parameter takes effect and is required only if the subscription billing method is selected for worker nodes.
        # 
        # Valid values: 1, 2, 3, 6, and 12.
        self.worker_auto_renew_period = worker_auto_renew_period
        # [**Deprecated**] When you configure a node pool, use the `data_disks` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The configurations of the data disks that you want to mount to worker nodes. The configurations include the disk category and disk size.
        self.worker_data_disks = worker_data_disks
        # [**Deprecated**] When you configure a node pool, use the `instance_charge_type` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The billing method of worker nodes. Valid values:
        # 
        # *   `PrePaid`: subscription.
        # *   `PostPaid`: pay-as-you-go.
        # 
        # Default value: PostPaid.
        self.worker_instance_charge_type = worker_instance_charge_type
        # [**Deprecated**] When you configure a node pool, use the `instance_types` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The instance configurations of worker nodes.
        self.worker_instance_types = worker_instance_types
        # [**Deprecated**] When you configure a node pool, use the `period` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The subscription duration of worker nodes. This parameter takes effect and is required only when `worker_instance_charge_type` is set to `PrePaid`.
        # 
        # Valid values: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # Default value: 1.
        self.worker_period = worker_period
        # [**Deprecated**] When you configure a node pool, use the `period_unit` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The billing cycle of worker nodes. This parameter is required if worker_instance_charge_type is set to `PrePaid`.
        # 
        # Valid value: `Month`, which indicates that worker nodes are billed only on a monthly basis.
        self.worker_period_unit = worker_period_unit
        # [**Deprecated**] When you configure a node pool, use the `system_disk_category` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The system disk category of worker nodes. For more information, see [Elastic Block Storage devices](https://help.aliyun.com/document_detail/63136.html).
        # 
        # Valid values:
        # 
        # *   `cloud_efficiency`: ultra disk.
        # *   `cloud_ssd`: standard SSD.
        # 
        # Default value: `cloud_ssd`.
        self.worker_system_disk_category = worker_system_disk_category
        # [**Deprecated**] When you configure a node pool, use the `system_disk_performance_level` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # If the system disk is an ESSD, you can specify the PL of the ESSD. For more information, see [Enterprise SSDs](https://help.aliyun.com/document_detail/122389.html).
        # 
        # Valid values:
        # 
        # *   PL0
        # *   PL1
        # *   PL2
        # *   PL3
        self.worker_system_disk_performance_level = worker_system_disk_performance_level
        # [**Deprecated**] When you configure a node pool, use the `system_disk_size` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The system disk size of worker nodes. Unit: GiB.
        # 
        # Valid values: 40 to 500.
        # 
        # The value of this parameter must be at least 40 and greater than or equal to the image size.
        # 
        # Default value: `120`.
        self.worker_system_disk_size = worker_system_disk_size
        # [**Deprecated**] When you configure a node pool, use the `system_disk_snapshot_policy_id` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The ID of the automatic snapshot policy that is used by the system disk specified for worker nodes.
        self.worker_system_disk_snapshot_policy_id = worker_system_disk_snapshot_policy_id
        # [**Deprecated**] When you configure a node pool, use the `vswitch_ids` parameter of the `scaling_group` field in the `nodepool` section instead.
        # 
        # The vSwitches for worker nodes. Each worker node is allocated a vSwitch.
        # 
        # `worker_vswitch_ids` is optional, but `vswitch_ids` is required if you create an ACK managed cluster that does not contain nodes.
        self.worker_vswitch_ids = worker_vswitch_ids
        # [Deprecated] Use the `zone_ids` parameter instead.
        # 
        # The ID of the zone to which the cluster belongs. This parameter is specific to ACK Serverless clusters.
        # 
        # When you create an ACK managed cluster, you must set the `zone_id` parameter if `vpc_id` and `vswitch_ids` are not specified. This way, the system automatically creates a VPC in the specified zone. This parameter is invalid if you specify the `vpc_id` and `vswitch_ids` parameters.
        self.zone_id = zone_id
        # The IDs of the zone in which the cluster is deployed. This parameter is specific to ACK managed clusters.
        # 
        # When you create an ACK managed cluster, you must set the `zone_id` parameter if `vpc_id` and `vswitch_ids` are not specified. This way, the system automatically creates a VPC in the specified zone. This parameter is invalid if you specify the `vpc_id` and `vswitch_ids` parameters.
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
        # The data disk category.
        # 
        # This parameter is required.
        self.category = category
        # Specifies whether to encrypt the data disk. Valid values:
        # 
        # *   `true`: encrypts the data disk.
        # *   `false`: does not encrypt the data disk.
        # 
        # Default value: `false`.
        self.encrypted = encrypted
        # The PL of the data disk. This parameter takes effect only for ESSDs. You can specify a higher PL if you increase the size of a data disk. For more information, see [Enterprise SSDs](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The data disk size. Valid values: 40 to 32767. Unit: GiB.
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
        # The configurations of auto cluster upgrade.
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
        # The automatic update frequency. Valid values:
        # 
        # *   patch
        # *   stable
        # *   rapid
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
        # Specifies whether to enable auto-renewal for the node.
        self.auto_renew = auto_renew
        # The auto-renewal duration for the node.
        self.auto_renew_period = auto_renew_period
        # The billing method of the node.
        self.charge_type = charge_type
        # Specifies whether to install CloudMonitor on the node.
        self.cloud_monitor_flags = cloud_monitor_flags
        # The CPU management policy of the node.
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
        # The name of the key pair. You must set this parameter or login_password.
        self.key_pair = key_pair
        # The SSH logon password. The password must be 8 to 30 characters in length and contain a minimum of three of the following character types: uppercase letters, lowercase letters, digits, and special characters. You must set this parameter or key_pair.
        self.login_password = login_password
        # The node port range.
        self.node_port_range = node_port_range
        # The subscription duration of the node.
        self.period = period
        # The unit of the subscription duration of the node.
        self.period_unit = period_unit
        # The container runtime.
        self.runtime = runtime
        # Specifies whether to enable Alibaba Cloud Linux Security Hardening.
        self.security_hardening_os = security_hardening_os
        # The number of control plane nodes.
        self.size = size
        # Specifies whether to enable MLPS security hardening.
        self.soc_enabled = soc_enabled
        # Specifies whether to enable the burst feature for the system disk.
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The system disk category for the node.
        self.system_disk_category = system_disk_category
        # The PL of the system disk that you want to use for the node. This parameter takes effect only for ESSDs.
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
        self.enabled = enabled
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

