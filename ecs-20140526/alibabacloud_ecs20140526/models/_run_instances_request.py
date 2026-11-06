# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class RunInstancesRequest(DaraModel):
    def __init__(
        self,
        cpu_options: main_models.RunInstancesRequestCpuOptions = None,
        hibernation_options: main_models.RunInstancesRequestHibernationOptions = None,
        private_pool_options: main_models.RunInstancesRequestPrivatePoolOptions = None,
        scheduler_options: main_models.RunInstancesRequestSchedulerOptions = None,
        security_options: main_models.RunInstancesRequestSecurityOptions = None,
        system_disk: main_models.RunInstancesRequestSystemDisk = None,
        affinity: str = None,
        amount: int = None,
        arn: List[main_models.RunInstancesRequestArn] = None,
        auto_pay: bool = None,
        auto_release_time: str = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        client_token: str = None,
        clock_options: main_models.RunInstancesRequestClockOptions = None,
        credit_specification: str = None,
        data_disk: List[main_models.RunInstancesRequestDataDisk] = None,
        dedicated_host_id: str = None,
        deletion_protection: bool = None,
        deployment_set_group_no: int = None,
        deployment_set_id: str = None,
        description: str = None,
        dry_run: bool = None,
        host_name: str = None,
        host_names: List[str] = None,
        hpc_cluster_id: str = None,
        http_endpoint: str = None,
        http_put_response_hop_limit: int = None,
        http_tokens: str = None,
        image_family: str = None,
        image_id: str = None,
        image_options: main_models.RunInstancesRequestImageOptions = None,
        instance_charge_type: str = None,
        instance_name: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        ipv_6address: List[str] = None,
        ipv_6address_count: int = None,
        isp: str = None,
        key_pair_name: str = None,
        launch_template_id: str = None,
        launch_template_name: str = None,
        launch_template_version: int = None,
        managed_host_id: str = None,
        min_amount: int = None,
        network_interface: List[main_models.RunInstancesRequestNetworkInterface] = None,
        network_interface_queue_number: int = None,
        network_options: main_models.RunInstancesRequestNetworkOptions = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        password_inherit: bool = None,
        period: int = None,
        period_unit: str = None,
        private_dns_name_options: main_models.RunInstancesRequestPrivateDnsNameOptions = None,
        private_ip_address: str = None,
        ram_role_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_enhancement_strategy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        spot_duration: int = None,
        spot_interruption_behavior: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        storage_set_id: str = None,
        storage_set_partition_number: int = None,
        tag: List[main_models.RunInstancesRequestTag] = None,
        tenancy: str = None,
        unique_suffix: bool = None,
        user_data: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.cpu_options = cpu_options
        self.hibernation_options = hibernation_options
        self.private_pool_options = private_pool_options
        self.scheduler_options = scheduler_options
        self.security_options = security_options
        self.system_disk = system_disk
        # Specifies whether to associate the instance on a dedicated host with the dedicated host. Valid values:
        # - default: Does not associate the instance with the dedicated host. If an instance for which the economical mode is enabled is stopped and then started, and the available resources of the original dedicated host are insufficient, the instance is deployed on another dedicated host in the automatic deployment resource pool.
        # - host: Associates the instance with the dedicated host. If an instance for which the economical mode is enabled is stopped and then started, the instance is still deployed on the original dedicated host. If the available resources of the original dedicated host are insufficient, the instance fails to be restarted.
        # Default value: default.
        self.affinity = affinity
        # The number of ECS instances to create. Valid values: 1 to 100.
        # 
        # The number of successfully created ECS instances depends on the specified Amount and minAmount:
        # 
        # - When minAmount is not specified: Instances are created based on the Amount value. If the inventory is insufficient, the API returns a creation failure, and no instances are created.
        # 
        # - When minAmount is specified:
        #   - If the ECS inventory < minAmount: No ECS instances are created, and the API returns a creation failure.
        #   - If minAmount ≤ ECS inventory < Amount: Instances are created based on the inventory, and the API returns a creation success.
        #   - If the ECS inventory ≥ Amount: Instances are created based on the specified Amount, and the API returns a creation success.
        # 
        # Default value: 1.
        self.amount = amount
        # >This parameter is not available.
        self.arn = arn
        # Specifies whether to automatically pay for the instance when you create it. Valid values:
        # 
        # - true: Automatically pays for the instance.
        # 
        #     > If you enable automatic payment, make sure that your payment method has sufficient balance. Otherwise, an abnormal order is generated and can only be canceled. If your payment method has insufficient balance, you can set AutoPay to false. In this case, an unpaid order is generated, and you can log on to the ECS console to complete the payment.
        # 
        # - false: Generates an order without deducting fees.
        # 
        #     > If InstanceChargeType is set to PostPaid, you cannot set AutoPay to false.
        # 
        # Default value: true.
        self.auto_pay = auto_pay
        # The automatic release time of the pay-as-you-go instance. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # - If the seconds (`ss`) value is not `00`, it is automatically set to the start of the current minute (`mm`).
        # 
        # - The shortest release time is half an hour after the current time.
        # 
        # - The longest release time cannot exceed three years from the current time.
        self.auto_release_time = auto_release_time
        # Specifies whether to enable auto-renewal. This parameter takes effect only when `InstanceChargeType` is set to `PrePaid`. Valid values:
        # 
        # - true: Enables auto-renewal.
        # - false: Disables auto-renewal.
        # 
        # Default value: false.
        self.auto_renew = auto_renew
        # The auto-renewal period. Valid values: 
        #          
        # <props="china">
        # - When PeriodUnit is set to Week: 1, 2, and 3.
        # - When PeriodUnit is set to Month: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # 
        # 
        # <props="intl">When PeriodUnit is set to Month: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The clock attribute configurations of the instance.
        self.clock_options = clock_options
        # The running mode of the burstable instance. Valid values:
        # 
        # - Standard: standard mode. For more information about the instance performance, see the "Standard mode" section in [What are burstable instances?](https://help.aliyun.com/document_detail/59977.html).
        # - Unlimited: unlimited mode. For more information about the instance performance, see the "Unlimited mode" section in [What are burstable instances?](https://help.aliyun.com/document_detail/59977.html).
        self.credit_specification = credit_specification
        # The data disk configurations.
        self.data_disk = data_disk
        # The dedicated host ID.
        # <props="china">You can call [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/134242.html) to query the dedicated host ID list.
        # 
        # <props="intl">You can call [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/134242.html) to query the dedicated host ID list.
        # 
        # >Notice: Dedicated hosts do not support the creation of spot instances. After you specify the `DedicatedHostId` parameter, the `SpotStrategy` and `SpotPriceLimit` settings in the request are automatically ignored.</notice>
        self.dedicated_host_id = dedicated_host_id
        # The release protection attribute of the instance. Specifies whether the instance can be released by using the console or by calling the [DeleteInstance](https://help.aliyun.com/document_detail/25507.html) operation. Valid values:
        # - true: Enables release protection for the instance.
        # - false: Disables release protection for the instance.
        # Default value: false.
        # > This attribute applies only to pay-as-you-go instances and restricts only manual release operations. It does not take effect on system release operations.
        self.deletion_protection = deletion_protection
        # The group number of the instance in the deployment set. If the policy of the deployment set is AvailabilityGroup, you can use this parameter to specify the group number. Valid values: 1 to 7.
        self.deployment_set_group_no = deployment_set_group_no
        # The ID of the deployment set.
        self.deployment_set_id = deployment_set_id
        # The instance description. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to pre-check this request. Valid values:
        # 
        # -  true: Sends a check request. No instances are created. Check items include whether required parameters are filled in, request format, business limits, and ECS inventory. If the check fails, the corresponding error is returned. If the check succeeds, the `DryRunOperation` error code is returned.
        # -  false (default): Sends a regular request. Instances are created directly after the check succeeds.
        self.dry_run = dry_run
        # The hostname of the instance. Limits:
        # 
        # - Periods (.) and hyphens (-) cannot be used as the first or last character and cannot be used consecutively.
        # - Windows instances: The hostname must be 2 to 15 characters in length. It cannot contain periods (.) or contain only digits. It can contain uppercase and lowercase letters, digits, and hyphens (-).
        # - Other instances (such as Linux instances):
        #     - The hostname must be 2 to 64 characters in length. It can contain multiple periods (.). The string between two consecutive periods is a segment, which can contain uppercase and lowercase letters, digits, and hyphens (-).
        #     - You can use the `${instance_id}` placeholder to write the instance ID into the `HostName` parameter. For example, if `HostName=k8s-${instance_id}` and the created ECS instance ID is `i-123abc****`, the hostname of the instance is `k8s-i-123abc****`.
        # 
        # When you create multiple ECS instances, you can:
        # 
        # - Batch configure sequential hostnames. For more information, see [Batch configure sequential names or hostnames for instances](https://help.aliyun.com/document_detail/196048.html).
        # - Use the `HostNames.N` parameter to set hostnames for multiple instances separately. Note that you cannot set both `HostName` and `HostNames.N`.
        self.host_name = host_name
        # Specifies different hostnames for each instance when you create multiple instances.
        self.host_names = host_names
        # The ID of the HPC cluster to which the instance belongs. 
        # 
        # This parameter is required when you create an SCC instance. You can refer to [CreateHpcCluster](https://help.aliyun.com/document_detail/109138.html) to create an HPC cluster.
        self.hpc_cluster_id = hpc_cluster_id
        # Specifies whether to enable the access channel for instance metadata. Valid values:
        # - enabled: Enables the access channel.
        # - disabled: Disables the access channel.
        # 
        # Default value: enabled.
        # > For more information about instance metadata, see [Overview of instance metadata](https://help.aliyun.com/document_detail/49122.html).
        self.http_endpoint = http_endpoint
        # > This parameter is not available.
        self.http_put_response_hop_limit = http_put_response_hop_limit
        # Specifies whether to forcibly use the hardened mode (IMDSv2) when you access instance metadata. Valid values:
        # - optional: Does not forcibly use the hardened mode.
        # - required: Forcibly uses the hardened mode. After you set this value, you cannot access instance metadata in normal mode.
        # 
        # Default value: optional.
        # > For more information about the modes for accessing instance metadata, see [Instance metadata access modes](https://help.aliyun.com/document_detail/150575.html).
        self.http_tokens = http_tokens
        # The image family name. Set this parameter to use the latest available image in the specified image family to create the instance.
        # 
        # The name must be 2 to 128 characters in length. It cannot start with a special character, digit, http://, or https://. It can contain periods (.), underscores (_), hyphens (-), and colons (:).
        # 
        # Take note of the following items:
        # 
        # - If `ImageId` is specified, you cannot set this parameter.
        # - If `ImageId` is not specified but `ImageId` is set in the launch template specified by `LaunchTemplateId` or `LaunchTemplateName`, you cannot set this parameter.
        # - If `ImageId` is not specified and `ImageId` is not set in the launch template specified by `LaunchTemplateId` or `LaunchTemplateName`, you can set this parameter.
        # - If neither `ImageId` nor `LaunchTemplateId` and `LaunchTemplateName` are specified, you can set this parameter.
        # > For information about the image families associated with Alibaba Cloud public images, see [Public image overview](https://help.aliyun.com/document_detail/108393.html).
        self.image_family = image_family
        # The image ID. The image used to start the instance. You can call [DescribeImages](https://help.aliyun.com/document_detail/25534.html) to query available images. If you do not specify `LaunchTemplateId` or `LaunchTemplateName` to determine a launch template, and do not specify `ImageFamily` to use the latest available image in an image family, `ImageId` is required.
        self.image_id = image_id
        # The image attribute configurations.
        self.image_options = image_options
        # The billing method of the instance. Valid values:
        # 
        # -  PrePaid: subscription.
        # -  PostPaid: pay-as-you-go.
        # 
        # Default value: PostPaid.
        # 
        # <props="china">When you select subscription, you must ensure that your account supports balance payment or credit payment. Otherwise, an `InvalidPayMethod` error is returned.
        # 
        # <props="intl">When you select subscription, you must ensure that your account supports credit payment. Otherwise, an `InvalidPayMethod` error is returned.
        self.instance_charge_type = instance_charge_type
        # The instance name. The name must be 2 to 128 characters in length. It can contain letters (including English and Chinese letters) and digits in the Unicode letter category. It can also contain colons (:), underscores (_), periods (.), and hyphens (-). Default value: the `InstanceId` of the instance.
        # 
        # When you create multiple ECS instances, you can batch configure sequential instance names, which can include brackets ([]) and commas (,). For more information, see [Batch configure sequential names or hostnames for instances](https://help.aliyun.com/document_detail/196048.html).
        self.instance_name = instance_name
        # The instance type. If you do not specify `LaunchTemplateId` or `LaunchTemplateName` to determine a launch template, `InstanceType` is a required parameter.  
        # 
        # - Instance type selection: See [instance family](https://help.aliyun.com/document_detail/25378.html) or invoke [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) to view the performance data of the target instance type. You can also see [Best practices for instance type selection](https://help.aliyun.com/document_detail/58291.html) to learn how to select an instance type.
        # - Inventory query: invoke [DescribeAvailableResource](https://help.aliyun.com/document_detail/66186.html) to check the resource availability in a specific region or zone.
        self.instance_type = instance_type
        # The network billing method. Valid values:
        # 
        # - PayByBandwidth: pay-by-bandwidth.
        # - PayByTraffic: pay-by-traffic.
        # 
        # Default value: PayByTraffic.
        # 
        # > In the **pay-by-traffic** mode, the peak inbound and outbound bandwidths are upper limits and are not guaranteed service level indicators. When resource contention occurs, the peak bandwidths may be limited. If your business requires guaranteed bandwidth, use the **pay-by-bandwidth** mode.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth. Unit: Mbit/s. Valid values:
        # 
        # - When the purchased outbound public bandwidth is less than or equal to 10 Mbit/s: 1 to 10. Default value: 10.
        # - When the purchased outbound public bandwidth is greater than 10 Mbit/s: 1 to the value of `InternetMaxBandwidthOut`. Default value: the value of `InternetMaxBandwidthOut`.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s. Valid values: 0 to 100.
        # 
        # Default value: 0.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether the instance is an I/O optimized instance. For [retired instance types](https://help.aliyun.com/document_detail/55263.html), the default value is none. For other instance types, the default value is optimized. Valid values:
        # 
        # - none: The instance is not I/O optimized.
        # - optimized: The instance is I/O optimized.
        self.io_optimized = io_optimized
        # Specifies one or more IPv6 addresses for the primary ENI. You can specify up to 10 IPv6 addresses. Valid values of N: 1 to 10.
        # 
        # Example: Ipv6Address.1=2001:db8:1234:1a00::***.
        # 
        # Take note of the following items:
        # 
        # - If you specify Ipv6Address.N, Amount can only be set to 1, and you cannot specify Ipv6AddressCount.
        # 
        # - If NetworkInterface.N.InstanceType is set to Primary, you cannot specify Ipv6Addresses.N or Ipv6AddressCount. Instead, you must specify NetworkInterface.N.Ipv6Addresses.N or NetworkInterface.N.Ipv6AddressCount.
        self.ipv_6address = ipv_6address
        # The number of IPv6 addresses to be randomly generated for the primary ENI. Valid values: 1 to 10.
        #          
        # Take note of the following items:
        # 
        # - You cannot set both `Ipv6Address.N` and `Ipv6AddressCount`.
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Primary`, you cannot set `Ipv6Address.N` or `Ipv6AddressCount`. You can only set `NetworkInterface.N.Ipv6Address.N` or `NetworkInterface.N.Ipv6AddressCount`.
        self.ipv_6address_count = ipv_6address_count
        # > This parameter is in invitational preview and is not available.
        self.isp = isp
        # The key pair name.
        # > For Windows instances, this parameter is ignored. The default value is empty. Even if this parameter is specified, only the `Password` parameter takes effect.
        self.key_pair_name = key_pair_name
        # The launch template ID. For more information, call [DescribeLaunchTemplates](https://help.aliyun.com/document_detail/73759.html).
        # 
        # When you use a launch template to create an instance, you must specify `LaunchTemplateId` or `LaunchTemplateName` to determine the launch template.
        self.launch_template_id = launch_template_id
        # The launch template name.
        # 
        # When you use a launch template to create an instance, you must specify `LaunchTemplateId` or `LaunchTemplateName` to determine the launch template.
        self.launch_template_name = launch_template_name
        # The launch template version. If you specify `LaunchTemplateId` or `LaunchTemplateName` but do not specify the launch template version, the default version is used.
        self.launch_template_version = launch_template_version
        # The unique identifier of the managed host, such as mh-f2d3647ca21****.
        self.managed_host_id = managed_host_id
        # The minimum quantity of ECS instances to purchase. Valid values: 1 to 100.
        # 
        # The number of successfully created ECS instances depends on the specified Amount and minAmount:
        # 
        # - When minAmount is not specified: Instances are created based on the Amount value. If the inventory is insufficient, the API returns a creation failure, and no instances are created.
        # 
        # - When minAmount is specified:
        #   - If the ECS inventory < minAmount: No ECS instances are created, and the API returns a creation failure.
        #   - If minAmount ≤ ECS inventory < Amount: Instances are created based on the inventory, and the API returns a creation success.
        #   - If the ECS inventory ≥ Amount: Instances are created based on the specified Amount, and the API returns a creation success.
        self.min_amount = min_amount
        # The ENI information.
        self.network_interface = network_interface
        # The number of queues for the primary ENI. Note the following:
        # 
        # - The value cannot exceed the maximum number of queues per ENI allowed by the instance type.
        # 
        # - The total number of queues for all ENIs attached to the instance cannot exceed the total queue quota allowed by the instance type. To obtain the maximum number of queues per ENI and the total queue quota for the instance type, query the `MaximumQueueNumberPerEni` and `TotalEniQueueQuantity` fields by calling the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation.
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Primary`, you cannot specify `NetworkInterfaceQueueNumber`. You can specify only `NetworkInterface.N.QueueNumber`.
        self.network_interface_queue_number = network_interface_queue_number
        # The network attribute configurations.
        self.network_options = network_options
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The instance password. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include:
        # 
        # ```
        # ()`~!@#$%^&*-_+=|{}[]:;\\"<>,.?/
        # ```
        # 
        # For Windows instances, the password cannot start with a forward slash (/).
        # 
        # > If you pass in the `Password` parameter, we recommend that you use HTTPS to send the request to prevent password leaks.
        self.password = password
        # Specifies whether to use the password preset in the image. Valid values:
        # 
        # - true: Uses the preset password.
        # - false: Does not use the preset password.
        # 
        # Default value: false.
        # 
        # > When you use this parameter, the Password parameter must be left empty. Make sure that the image you use has a password configured.
        self.password_inherit = password_inherit
        # The subscription period of the resource. The unit is specified by `PeriodUnit`. This parameter takes effect and is required only when `InstanceChargeType` is set to `PrePaid`. If `DedicatedHostId` is specified, the subscription period cannot exceed the subscription period of the dedicated host. Valid values:
        # 
        # <props="china">
        # - When PeriodUnit is set to Week, valid values of Period are 1, 2, 3, and 4.
        # - When PeriodUnit is set to Month, valid values of Period are 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        # 
        # 
        # 
        # <props="intl">When PeriodUnit is set to Month, valid values of Period are 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        self.period = period
        # The time unit of the subscription billing method. Valid values: 
        # 
        # <props="china">
        # - Week.
        # - Month (default).
        # 
        # 
        # 
        # <props="intl">Month (default).
        self.period_unit = period_unit
        # The private domain name configurations of the instance.
        # 
        # 
        # For more information about private private domain resolution, see [Private private domain resolution for ECS](https://help.aliyun.com/document_detail/2844797.html).
        self.private_dns_name_options = private_dns_name_options
        # The private IP address of the instance. When you specify a private IP address for an ECS instance in a VPC, the IP address must be an available IP address within the CIDR block of the vSwitch specified by `VSwitchId`.
        # 
        # Note:
        # 
        # - After you specify `PrivateIpAddress`:
        #     - If `Amount` is set to 1, the specified private IP address is assigned to the created ECS instance.
        #     - If `Amount` is set to a value greater than 1, the specified private IP address is used as the starting IP address to assign consecutive private IP addresses to the ECS instances that you create in a batch. In this case, you cannot bind secondary ENIs to the instances. That is, you cannot specify parameters such as `NetworkInterface.N.*`.
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Primary`, you cannot specify `PrivateIpAddress`. You can only specify `NetworkInterface.N.PrimaryIpAddress`.
        # 
        # > The first and last three IP addresses of each vSwitch are reserved by the system and cannot be specified.
        # For example, if the CIDR block of a vSwitch is 192.168.1.0/24, the following four IP addresses are reserved by the system: 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255.
        self.private_ip_address = private_ip_address
        # The instance RAM role name. You can use the RAM API [ListRoles](https://help.aliyun.com/document_detail/28713.html) to query the instance RAM roles you have created.
        self.ram_role_name = ram_role_name
        # The region ID of the instance. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the enterprise resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable security hardening. Valid values:
        # 
        # - Active: Enables security hardening. This value takes effect only for public images.
        # - Deactive: Disables security hardening. This value takes effect for all image types.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The ID of the security group to which the new instance belongs. Instances in the same security group can access each other. The maximum number of instances that a security group can contain depends on the security group type. For more information, see the "Security group limits" section in [Limits](~~25412#SecurityGroupQuota~~).
        # 
        # > `SecurityGroupId` determines the network type of the instance. For example, if the network type of the security group is VPC, the instance is of the VPC type, and you must also specify `VSwitchId`.
        # 
        # If you do not specify `LaunchTemplateId` or `LaunchTemplateName` to determine a launch template, the security group ID is required. Take note of the following items:
        # 
        # - You can set `SecurityGroupId` to specify one security group, or set `SecurityGroupIds.N` to specify one or more security groups. However, you cannot set both `SecurityGroupId` and `SecurityGroupIds.N`.
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Primary`, you cannot set `SecurityGroupId` or `SecurityGroupIds.N`. You can only set `NetworkInterface.N.SecurityGroupId` or `NetworkInterface.N.SecurityGroupIds.N`.
        self.security_group_id = security_group_id
        # Adds the instance to multiple security groups. The valid values of N depend on the quota of security groups to which the instance can be added. For more information, see [Security group limits](https://help.aliyun.com/document_detail/101348.html).
        # 
        # Take note of the following items:
        # 
        # - You cannot specify both SecurityGroupId and SecurityGroupIds.N.
        # - If NetworkInterface.N.InstanceType is set to Primary, you cannot specify SecurityGroupId or SecurityGroupIds.N. You can only specify NetworkInterface.N.SecurityGroupId or NetworkInterface.N.SecurityGroupIds.N.
        self.security_group_ids = security_group_ids
        # The protection period of the spot instance. Unit: hours. Valid values:
        # - 1: After the spot instance is created, Alibaba Cloud guarantees that the spot instance will not be automatically released within 1 hour. After 1 hour, the system compares the bid price with the marketplace price and checks the resource inventory in real time to determine whether to retain or reclaim the spot instance.
        # - 0: After the spot instance is created, Alibaba Cloud does not guarantee the runtime duration of the spot instance. The system compares the bid price with the marketplace price and checks the resource inventory in real time to determine whether to retain or reclaim the spot instance.
        # 
        # Default value: 1.
        # > 
        # > - Currently, this parameter can only be set to 0 or 1.
        # > - Spot instances are billed by the second. We recommend that you select an appropriate protection period based on the execution duration of your specific task.
        # > - Alibaba Cloud sends a notification through an ECS system event 5 minutes before the spot instance is reclaimed.
        self.spot_duration = spot_duration
        # The break mode for the spot instance. Valid values:
        # 
        # - Terminate: Releases the instance.
        # - Stop: Puts the instance into economical mode.
        # 
        #   For more information about economical mode, see [Economical mode for pay-as-you-go instances](https://help.aliyun.com/document_detail/63353.html).
        # 
        # Default value: Terminate.
        self.spot_interruption_behavior = spot_interruption_behavior
        # The maximum hourly price of the instance. It supports up to three decimal places. This parameter takes effect when `SpotStrategy` is set to `SpotWithPriceLimit`.
        self.spot_price_limit = spot_price_limit
        # The bidding policy for the pay-as-you-go instance. This parameter takes effect when `InstanceChargeType` is set to `PostPaid`. Valid values:
        # 
        # - NoSpot: regular pay-as-you-go instance.
        # - SpotWithPriceLimit: spot instance with a maximum price.
        # - SpotAsPriceGo: spot instance for which the system automatically places bids based on the market price.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy
        # The ID of the storage set.
        self.storage_set_id = storage_set_id
        # The maximum number of partitions in the storage set. Valid values: integers greater than or equal to 1.
        self.storage_set_partition_number = storage_set_partition_number
        # The tag information of the instance, cloud disks, and primary ENI.
        self.tag = tag
        # Specifies whether to create the instance on a dedicated host. Valid values:
        # - default: Creates a non-dedicated host instance.
        # - host: Creates an instance on a dedicated host. If you do not specify DedicatedHostId, Alibaba Cloud automatically selects a dedicated host to deploy the instance.
        # Default value: default.
        self.tenancy = tenancy
        # Specifies whether to automatically append sequential suffixes to `HostName` and `InstanceName` when you create multiple instances. The sequential suffix starts from 001 and increments up to 999. Valid values:
        # - true: Appends sequential suffixes.
        # - false: Does not append sequential suffixes.
        # 
        # Default value: false.
        # 
        # If `HostName` or `InstanceName` is set in a specified sorting format without the `name_suffix` naming suffix, meaning the naming format is `name_prefix[begin_number,bits]`, `UniqueSuffix` does not take effect, and the names are sorted only in the specified order.
        # 
        # For more information, see [Batch configure sequential names or hostnames for instances](https://help.aliyun.com/document_detail/196048.html).
        self.unique_suffix = unique_suffix
        # The user data of the instance. The data must be Base64-encoded. The size of the user data cannot exceed 32 KB before Base64 encoding.
        # 
        # For more information about the limits, format, and execution frequency of user data, see [Instance user data](https://help.aliyun.com/document_detail/49121.html).
        # 
        # > To ensure the security of UserData during transmission, avoid transmitting sensitive data such as passwords and private keys in plaintext. If you need to transmit such information, encrypt it first, encode it in Base64, and then decrypt it inside the instance to ensure information security.
        self.user_data = user_data
        # The vSwitch ID. If you create a VPC-type ECS instance, you must specify a vSwitch ID. The security group and the vSwitch must belong to the same VPC. You can call [DescribeVSwitches](https://help.aliyun.com/document_detail/35748.html) to query created vSwitches.
        # 
        # Take note of the following items:
        # 
        # - If you set `VSwitchId`, the `ZoneId` parameter must be set to the zone where the vSwitch resides. You can also leave `ZoneId` unspecified, and the system automatically selects the zone where the specified vSwitch resides.
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Primary`, you cannot set `VSwitchId`. You can only set `NetworkInterface.N.VSwitchId`.
        self.v_switch_id = v_switch_id
        # The zone ID of the instance. You can call [DescribeZones](https://help.aliyun.com/document_detail/25610.html) to obtain the zone list.
        # 
        # > If you specify the `VSwitchId` parameter, the `ZoneId` parameter must be set to the zone where the vSwitch resides. You can also leave the `ZoneId` parameter unspecified, and the system automatically selects the zone where the specified vSwitch resides.
        # 
        # Default value: automatically selected by the system.
        self.zone_id = zone_id

    def validate(self):
        if self.cpu_options:
            self.cpu_options.validate()
        if self.hibernation_options:
            self.hibernation_options.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.scheduler_options:
            self.scheduler_options.validate()
        if self.security_options:
            self.security_options.validate()
        if self.system_disk:
            self.system_disk.validate()
        if self.arn:
            for v1 in self.arn:
                 if v1:
                    v1.validate()
        if self.clock_options:
            self.clock_options.validate()
        if self.data_disk:
            for v1 in self.data_disk:
                 if v1:
                    v1.validate()
        if self.image_options:
            self.image_options.validate()
        if self.network_interface:
            for v1 in self.network_interface:
                 if v1:
                    v1.validate()
        if self.network_options:
            self.network_options.validate()
        if self.private_dns_name_options:
            self.private_dns_name_options.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_options is not None:
            result['CpuOptions'] = self.cpu_options.to_map()

        if self.hibernation_options is not None:
            result['HibernationOptions'] = self.hibernation_options.to_map()

        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()

        if self.scheduler_options is not None:
            result['SchedulerOptions'] = self.scheduler_options.to_map()

        if self.security_options is not None:
            result['SecurityOptions'] = self.security_options.to_map()

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.affinity is not None:
            result['Affinity'] = self.affinity

        if self.amount is not None:
            result['Amount'] = self.amount

        result['Arn'] = []
        if self.arn is not None:
            for k1 in self.arn:
                result['Arn'].append(k1.to_map() if k1 else None)

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_release_time is not None:
            result['AutoReleaseTime'] = self.auto_release_time

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.clock_options is not None:
            result['ClockOptions'] = self.clock_options.to_map()

        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification

        result['DataDisk'] = []
        if self.data_disk is not None:
            for k1 in self.data_disk:
                result['DataDisk'].append(k1.to_map() if k1 else None)

        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.deployment_set_group_no is not None:
            result['DeploymentSetGroupNo'] = self.deployment_set_group_no

        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.host_names is not None:
            result['HostNames'] = self.host_names

        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id

        if self.http_endpoint is not None:
            result['HttpEndpoint'] = self.http_endpoint

        if self.http_put_response_hop_limit is not None:
            result['HttpPutResponseHopLimit'] = self.http_put_response_hop_limit

        if self.http_tokens is not None:
            result['HttpTokens'] = self.http_tokens

        if self.image_family is not None:
            result['ImageFamily'] = self.image_family

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_options is not None:
            result['ImageOptions'] = self.image_options.to_map()

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized

        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        if self.launch_template_name is not None:
            result['LaunchTemplateName'] = self.launch_template_name

        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version

        if self.managed_host_id is not None:
            result['ManagedHostId'] = self.managed_host_id

        if self.min_amount is not None:
            result['MinAmount'] = self.min_amount

        result['NetworkInterface'] = []
        if self.network_interface is not None:
            for k1 in self.network_interface:
                result['NetworkInterface'].append(k1.to_map() if k1 else None)

        if self.network_interface_queue_number is not None:
            result['NetworkInterfaceQueueNumber'] = self.network_interface_queue_number

        if self.network_options is not None:
            result['NetworkOptions'] = self.network_options.to_map()

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.private_dns_name_options is not None:
            result['PrivateDnsNameOptions'] = self.private_dns_name_options.to_map()

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration

        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior

        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.storage_set_id is not None:
            result['StorageSetId'] = self.storage_set_id

        if self.storage_set_partition_number is not None:
            result['StorageSetPartitionNumber'] = self.storage_set_partition_number

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy

        if self.unique_suffix is not None:
            result['UniqueSuffix'] = self.unique_suffix

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuOptions') is not None:
            temp_model = main_models.RunInstancesRequestCpuOptions()
            self.cpu_options = temp_model.from_map(m.get('CpuOptions'))

        if m.get('HibernationOptions') is not None:
            temp_model = main_models.RunInstancesRequestHibernationOptions()
            self.hibernation_options = temp_model.from_map(m.get('HibernationOptions'))

        if m.get('PrivatePoolOptions') is not None:
            temp_model = main_models.RunInstancesRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

        if m.get('SchedulerOptions') is not None:
            temp_model = main_models.RunInstancesRequestSchedulerOptions()
            self.scheduler_options = temp_model.from_map(m.get('SchedulerOptions'))

        if m.get('SecurityOptions') is not None:
            temp_model = main_models.RunInstancesRequestSecurityOptions()
            self.security_options = temp_model.from_map(m.get('SecurityOptions'))

        if m.get('SystemDisk') is not None:
            temp_model = main_models.RunInstancesRequestSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')

        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        self.arn = []
        if m.get('Arn') is not None:
            for k1 in m.get('Arn'):
                temp_model = main_models.RunInstancesRequestArn()
                self.arn.append(temp_model.from_map(k1))

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoReleaseTime') is not None:
            self.auto_release_time = m.get('AutoReleaseTime')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClockOptions') is not None:
            temp_model = main_models.RunInstancesRequestClockOptions()
            self.clock_options = temp_model.from_map(m.get('ClockOptions'))

        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')

        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.RunInstancesRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DeploymentSetGroupNo') is not None:
            self.deployment_set_group_no = m.get('DeploymentSetGroupNo')

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('HostNames') is not None:
            self.host_names = m.get('HostNames')

        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')

        if m.get('HttpEndpoint') is not None:
            self.http_endpoint = m.get('HttpEndpoint')

        if m.get('HttpPutResponseHopLimit') is not None:
            self.http_put_response_hop_limit = m.get('HttpPutResponseHopLimit')

        if m.get('HttpTokens') is not None:
            self.http_tokens = m.get('HttpTokens')

        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageOptions') is not None:
            temp_model = main_models.RunInstancesRequestImageOptions()
            self.image_options = temp_model.from_map(m.get('ImageOptions'))

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')

        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        if m.get('LaunchTemplateName') is not None:
            self.launch_template_name = m.get('LaunchTemplateName')

        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')

        if m.get('ManagedHostId') is not None:
            self.managed_host_id = m.get('ManagedHostId')

        if m.get('MinAmount') is not None:
            self.min_amount = m.get('MinAmount')

        self.network_interface = []
        if m.get('NetworkInterface') is not None:
            for k1 in m.get('NetworkInterface'):
                temp_model = main_models.RunInstancesRequestNetworkInterface()
                self.network_interface.append(temp_model.from_map(k1))

        if m.get('NetworkInterfaceQueueNumber') is not None:
            self.network_interface_queue_number = m.get('NetworkInterfaceQueueNumber')

        if m.get('NetworkOptions') is not None:
            temp_model = main_models.RunInstancesRequestNetworkOptions()
            self.network_options = temp_model.from_map(m.get('NetworkOptions'))

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PrivateDnsNameOptions') is not None:
            temp_model = main_models.RunInstancesRequestPrivateDnsNameOptions()
            self.private_dns_name_options = temp_model.from_map(m.get('PrivateDnsNameOptions'))

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')

        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')

        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('StorageSetId') is not None:
            self.storage_set_id = m.get('StorageSetId')

        if m.get('StorageSetPartitionNumber') is not None:
            self.storage_set_partition_number = m.get('StorageSetPartitionNumber')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.RunInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')

        if m.get('UniqueSuffix') is not None:
            self.unique_suffix = m.get('UniqueSuffix')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class RunInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instance, cloud disks, and primary ENI. Valid values of N: 1 to 20. If you specify this parameter, it cannot be an empty string. The tag key can be up to 128 characters in length. It cannot start with aliyun or acs:, and cannot contain http:// or https://.
        self.key = key
        # The tag value of the instance, cloud disks, and primary ENI. Valid values of N: 1 to 20. If you specify this parameter, it can be an empty string. The tag value can be up to 128 characters in length and cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class RunInstancesRequestPrivateDnsNameOptions(DaraModel):
    def __init__(
        self,
        enable_instance_id_dns_aaaarecord: bool = None,
        enable_instance_id_dns_arecord: bool = None,
        enable_ip_dns_arecord: bool = None,
        enable_ip_dns_ptr_record: bool = None,
        hostname_type: str = None,
    ):
        # Specifies whether to enable or disable the resolution of instance ID-based domain names to IPv6 addresses. Valid values:
        # 
        # - true: Enables the resolution.
        # 
        # - false: Disables the resolution.
        # 
        # Default value: false.
        self.enable_instance_id_dns_aaaarecord = enable_instance_id_dns_aaaarecord
        # Specifies whether to enable or disable the resolution of instance ID-based domain names to IPv4 addresses. Valid values:
        # 
        # - true: Enables the resolution.
        # 
        # - false: Disables the resolution.
        # 
        # Default value: false.
        self.enable_instance_id_dns_arecord = enable_instance_id_dns_arecord
        # Specifies whether to enable or disable the resolution of IP-based domain names to IPv4 addresses. Valid values:
        # 
        # - true: Enables the resolution.
        # - false: Disables the resolution.
        # 
        # Default value: false.
        self.enable_ip_dns_arecord = enable_ip_dns_arecord
        # Specifies whether to enable or disable the reverse resolution of IPv4 addresses to IP-based domain names. Valid values:
        # 
        # - true: Enables the resolution.
        # - false: Disables the resolution.
        # 
        # Default value: false.
        self.enable_ip_dns_ptr_record = enable_ip_dns_ptr_record
        # The hostname type. Valid values:
        # 
        # - Custom: Custom hostname.
        # - IpBased: IP-based hostname.
        # - InstanceIdBased: Instance ID-based hostname.
        # 
        # Default value: Custom.
        self.hostname_type = hostname_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_instance_id_dns_aaaarecord is not None:
            result['EnableInstanceIdDnsAAAARecord'] = self.enable_instance_id_dns_aaaarecord

        if self.enable_instance_id_dns_arecord is not None:
            result['EnableInstanceIdDnsARecord'] = self.enable_instance_id_dns_arecord

        if self.enable_ip_dns_arecord is not None:
            result['EnableIpDnsARecord'] = self.enable_ip_dns_arecord

        if self.enable_ip_dns_ptr_record is not None:
            result['EnableIpDnsPtrRecord'] = self.enable_ip_dns_ptr_record

        if self.hostname_type is not None:
            result['HostnameType'] = self.hostname_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableInstanceIdDnsAAAARecord') is not None:
            self.enable_instance_id_dns_aaaarecord = m.get('EnableInstanceIdDnsAAAARecord')

        if m.get('EnableInstanceIdDnsARecord') is not None:
            self.enable_instance_id_dns_arecord = m.get('EnableInstanceIdDnsARecord')

        if m.get('EnableIpDnsARecord') is not None:
            self.enable_ip_dns_arecord = m.get('EnableIpDnsARecord')

        if m.get('EnableIpDnsPtrRecord') is not None:
            self.enable_ip_dns_ptr_record = m.get('EnableIpDnsPtrRecord')

        if m.get('HostnameType') is not None:
            self.hostname_type = m.get('HostnameType')

        return self

class RunInstancesRequestNetworkOptions(DaraModel):
    def __init__(
        self,
        bandwidth_weighting: str = None,
        enable_jumbo_frame: bool = None,
        enable_network_encryption: bool = None,
    ):
        # The bandwidth weight of the instance. The valid values vary based on the instance type. You can call the DescribeInstanceTypes operation to query the valid values for a specific instance type. The BandwidthWeighting field in the response indicates the bandwidth weight levels supported by the instance type. You can use the name field in the response as the dictionary value, such as Vpc-L1 and Ebs-L1.
        self.bandwidth_weighting = bandwidth_weighting
        # Specifies whether to enable the Jumbo Frame feature for the instance. Valid values:
        # 
        # - false: Disables the Jumbo Frame feature. The maximum transmission unit (MTU) of all ENIs (including the primary ENI and secondary ENIs) of the instance is set to 1500.
        # 
        # - true: Enables the Jumbo Frame feature. The MTU of all ENIs (including the primary ENI and secondary ENIs) of the instance is set to 8500.
        # 
        # Default value: true.
        # 
        # >Only specific eighth-generation and later instance types support the Jumbo Frame feature. For more information, see [MTU of ECS instances](https://help.aliyun.com/document_detail/200512.html).
        self.enable_jumbo_frame = enable_jumbo_frame
        # > This parameter is in invitational preview and is not available.
        self.enable_network_encryption = enable_network_encryption

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_weighting is not None:
            result['BandwidthWeighting'] = self.bandwidth_weighting

        if self.enable_jumbo_frame is not None:
            result['EnableJumboFrame'] = self.enable_jumbo_frame

        if self.enable_network_encryption is not None:
            result['EnableNetworkEncryption'] = self.enable_network_encryption

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthWeighting') is not None:
            self.bandwidth_weighting = m.get('BandwidthWeighting')

        if m.get('EnableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('EnableJumboFrame')

        if m.get('EnableNetworkEncryption') is not None:
            self.enable_network_encryption = m.get('EnableNetworkEncryption')

        return self

class RunInstancesRequestNetworkInterface(DaraModel):
    def __init__(
        self,
        delete_on_release: bool = None,
        description: str = None,
        instance_type: str = None,
        ipv_6address: List[str] = None,
        ipv_6address_count: int = None,
        network_card_index: int = None,
        network_interface_id: str = None,
        network_interface_name: str = None,
        network_interface_traffic_mode: str = None,
        primary_ip_address: str = None,
        queue_number: int = None,
        queue_pair_number: int = None,
        rx_queue_size: int = None,
        secondary_private_ip_address_count: int = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        source_dest_check: bool = None,
        tx_queue_size: int = None,
        v_switch_id: str = None,
    ):
        # Specifies whether to retain the ENI when the instance is released. Valid values:
        # 
        # - true: Does not retain the ENI.
        # 
        # - false: Retains the ENI.
        # 
        # Default value: true.
        # 
        # >This parameter takes effect only for secondary ENIs.
        self.delete_on_release = delete_on_release
        # The description of the ENI.
        # 
        # Take note of the following items:
        # 
        # - The valid values of N cannot exceed the maximum number of network interface controllers (NICs) supported by the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controllers (NICs) supported by the instance type.
        # - The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        # - If NetworkInterface.N.InstanceType is set to Primary, you do not need to specify this parameter.
        self.description = description
        # The type of the ENI. The valid values of N cannot exceed the maximum number of network interface controllers (NICs) supported by the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controllers (NICs) supported by the instance type.
        # 
        # Valid values of the parameter:
        # 
        # - Primary: primary ENI.
        # - Secondary: secondary ENI.
        # 
        # Default value: Secondary.
        self.instance_type = instance_type
        # Specifies one or more IPv6 addresses for the primary ENI. You can specify up to 10 IPv6 addresses. Valid values of the second N: 1 to 10.
        # 
        # Example: Ipv6Address.1=2001:db8:1234:1a00::***.
        # 
        # Take note of the following items:
        # 
        # - This parameter takes effect only when NetworkInterface.N.InstanceType is set to Primary. If NetworkInterface.N.InstanceType is set to Secondary or left empty, you cannot specify this parameter.
        # 
        # - After you specify this parameter, Amount can only be set to 1, and you cannot specify Ipv6AddressCount, Ipv6Address.N, or NetworkInterface.N.Ipv6AddressCount.
        self.ipv_6address = ipv_6address
        # The number of IPv6 addresses to be randomly generated for the primary ENI. Valid values: 1 to 10.
        # 
        # Take note of the following items:
        # 
        # - This parameter takes effect only when NetworkInterface.N.InstanceType is set to Primary. If NetworkInterface.N.InstanceType is set to Secondary or left empty, you cannot specify this parameter.
        # 
        # - After you specify this parameter, you cannot specify Ipv6AddressCount, Ipv6Address.N, or NetworkInterface.N.Ipv6Address.N.
        self.ipv_6address_count = ipv_6address_count
        # The index of the network card specified for the ENI.
        # 
        # Take note of the following items:
        # - Only specific instance types support specifying the network card index.
        # - When NetworkInterface.N.InstanceType is set to Primary, if the instance type supports network cards and you specify this parameter, you can only set it to 0.
        # - When NetworkInterface.N.InstanceType is set to Secondary or left empty, if the instance type supports network cards, you can specify this parameter based on the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.network_card_index = network_card_index
        # The ID of the ENI attached to the instance.
        # 
        # After you specify this parameter, Amount can only be set to 1.
        # 
        # >This parameter takes effect only for secondary ENIs. After you specify an existing secondary ENI, you cannot configure other ENI creation parameters.
        self.network_interface_id = network_interface_id
        # The name of the ENI. The name must be 2 to 128 characters in length. It can contain letters and digits in the Unicode letter category. It can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # Take note of the following items:
        # 
        # - The valid values of N cannot exceed the maximum number of network interface controllers (NICs) supported by the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controllers (NICs) supported by the instance type.
        # 
        # - If NetworkInterface.N.InstanceType is set to Primary, you do not need to specify this parameter.
        self.network_interface_name = network_interface_name
        # The communication mode of the network interface controller (NIC). Valid values of the parameter:
        # 
        # - Standard: Uses the TCP communication mode.
        # - HighPerformance: Enables the Elastic RDMA Interface (ERI) and uses the RDMA communication mode.
        # 
        # Default value: Standard.
        # 
        # >The number of Elastic Network Interfaces (ENIs) in RDMA mode cannot exceed the limit of the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # Adds an ENI and specifies a primary IP address.
        # 
        # Take note of the following items:
        # 
        # - The valid values of N cannot exceed the maximum number of network interface controllers (NICs) supported by the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controllers (NICs) supported by the instance type.
        #     - When you configure one ENI, you can configure one primary ENI or one secondary ENI. If the Amount parameter is set to a value greater than 1, and you configure a primary ENI and specify this parameter, consecutive primary IP addresses are allocated to multiple ECS instances starting from the specified primary IP address when you create instances in batches. Note that you cannot attach secondary ENIs to instances in this case.
        #     - Note that if the Amount parameter is set to a value greater than 1 and you specify this parameter for the primary ENI, you cannot configure secondary ENIs. This means you cannot set NetworkInterface.2.InstanceType to Secondary.
        # 
        # - If NetworkInterface.N.InstanceType is set to Primary, this parameter serves the same purpose as PrivateIpAddress, but you cannot specify both PrivateIpAddress and this parameter.
        # 
        # - If NetworkInterface.N.InstanceType is set to Secondary or left empty, this parameter specifies the primary IP address for the secondary ENI. By default, an IP address is randomly selected from the vSwitch CIDR block of the vSwitch to which the ENI belongs.
        # 
        # >- The first and last three IP addresses of each vSwitch are system reserved IP addresses and cannot be specified.
        # For example, if the vSwitch CIDR block is 192.168.1.0/24, the following four IP addresses are system reserved IP addresses: 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255.
        self.primary_ip_address = primary_ip_address
        # The number of ENI queues.
        # 
        # Take note of the following items:
        # 
        # - The valid values of N cannot exceed the maximum number of network interface controllers (NICs) supported by the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controllers (NICs) supported by the instance type.
        # 
        # - The value cannot exceed the maximum number of queues per ENI allowed by the instance type.
        # 
        # - The total number of queues for all ENIs of the instance cannot exceed the total queue quota allowed by the instance type. You can invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation and query the MaximumQueueNumberPerEni and TotalEniQueueQuantity fields to obtain the maximum number of queues per ENI and the total queue quota for the instance type.
        # 
        # - If NetworkInterface.N.InstanceType is set to Primary and you specify this parameter, you cannot specify the NetworkInterfaceQueueNumber parameter.
        self.queue_number = queue_number
        # The number of RDMA ENI queues.
        # 
        # If you want to attach multiple RDMA ENIs to the instance, we recommend that you manually specify QueuePairNumber for each ENI based on the maximum QueuePairNumber supported by the instance type and the planned number of ENIs. Make sure that the total QueuePairNumber of all ENIs does not exceed the maximum value allowed by the instance type. You can call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum value for the instance type.
        # 
        # >Notice: If QueuePairNumber is not specified for an RDMA ENI, the maximum QueuePairNumber supported by all RDMA ENIs for the instance type is used by default. Therefore, after you attach an RDMA ENI for which QueuePairNumber is not specified, you cannot attach more RDMA ENIs. Regular ENIs are not subject to this limit.</notice>
        self.queue_pair_number = queue_pair_number
        # The inbound queue depth of the ENI.
        # 
        # 
        # <props="china">
        # 
        # >This parameter is in invitational preview and is not available. If you want to use this parameter, [submit a ticket](https://selfservice.console.aliyun.com/ticket/createIndex) to apply for the whitelist.
        # 
        # 
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is in invitational preview and is not available. If you want to use this parameter, [submit a ticket](https://smartservice.console.aliyun.com/service/create-ticket-intl) to apply for the whitelist.
        # 
        # 
        # 
        # Take note of the following items when you use this parameter:
        # 
        # - This parameter is applicable only to seventh-generation and later ECS instance types.
        # 
        # - This parameter is applicable only to Linux images.
        # 
        # - A larger inbound queue depth can improve inbound throughput and reduce the packet loss rate, but it consumes more memory.
        self.rx_queue_size = rx_queue_size
        # The number of secondary private IPv4 addresses to be allocated to the ENI. Valid values: 1 to 49.
        # 
        # - The value cannot exceed the limit on the number of IP addresses for the instance type. For more information, see [Instance families](~~~25378~~).
        # - NetworkInterface.N.SecondaryPrivateIpAddressCount specifies the number of secondary private IPv4 addresses to be allocated to the ENI, excluding the primary private IP address of the ENI. The system randomly allocates the addresses from the active CIDR block of the vSwitch (NetworkInterface.N.VSwitchId) to which the ENI belongs.
        self.secondary_private_ip_address_count = secondary_private_ip_address_count
        # The ID of the security group to which the ENI belongs.
        # 
        # Take note of the following items:
        # 
        # - The valid values of N cannot exceed the maximum number of network interface controllers (NICs) supported by the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controllers (NICs) supported by the instance type.
        # 
        # - If NetworkInterface.N.InstanceType is set to Primary, you must specify this parameter. In this case, this parameter serves the same purpose as SecurityGroupId, but you cannot specify SecurityGroupId, SecurityGroupIds.N, or NetworkInterface.N.SecurityGroupIds.N.
        # 
        # - If NetworkInterface.N.InstanceType is set to Secondary or left empty, this parameter is optional. The default value is the security group to which the ECS instance belongs.
        self.security_group_id = security_group_id
        # The IDs of one or more security groups to which the ENI belongs.
        # 
        # - The valid values of N cannot exceed the maximum number of network interface controllers (NICs) supported by the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controllers (NICs) supported by the instance type.
        # - The second N indicates that you can specify one or more security group IDs. The valid values of N depend on the quota of security groups to which the instance can be added. For more information, see [Security group limits](~~25412#SecurityGroupQuota1~~).
        # 
        # Take note of the following items:
        # 
        # - If NetworkInterface.N.InstanceType is set to Primary, you must specify this parameter or NetworkInterface.N.SecurityGroupId. In this case, this parameter serves the same purpose as SecurityGroupIds.N, but you cannot specify SecurityGroupId, SecurityGroupIds.N, or NetworkInterface.N.SecurityGroupId.
        # 
        # - If NetworkInterface.N.InstanceType is set to Secondary or left empty, this parameter is optional. The default value is the security group to which the ECS instance belongs.
        self.security_group_ids = security_group_ids
        # Specifies whether to enable the source/destination checking feature. We recommend that you enable this feature to improve network security. Valid values:
        # 
        # - true: Enables the feature.
        # 
        # - false: Disables the feature.
        # 
        # Default value: false.
        # 
        # > This feature is supported only in specific regions. Before you use this feature, read [Source/destination checking](https://help.aliyun.com/document_detail/2863210.html).
        self.source_dest_check = source_dest_check
        # The outbound queue depth of the ENI.
        # 
        # 
        # <props="china">
        # 
        # >This parameter is in invitational preview and is not available. If you want to use this parameter, [submit a ticket](https://selfservice.console.aliyun.com/ticket/createIndex) to apply for the whitelist.
        # 
        # 
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # > This parameter is in invitational preview and is not available. If you want to use this parameter, [submit a ticket](https://smartservice.console.aliyun.com/service/create-ticket-intl) to apply for the whitelist.
        # 
        # 
        # 
        # Take note of the following items when you use this parameter:
        # 
        # - This parameter is applicable only to seventh-generation and later ECS instance types.
        # 
        # - This parameter is applicable only to Linux images.
        # 
        # - A larger outbound queue depth can improve outbound throughput and reduce the packet loss rate, but it consumes more memory.
        self.tx_queue_size = tx_queue_size
        # The ID of the vSwitch to which the ENI belongs.
        # 
        # Take note of the following items:
        # 
        # - The valid values of N cannot exceed the maximum number of network interface controllers (NICs) supported by the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controllers (NICs) supported by the instance type.  
        # - If NetworkInterface.N.InstanceType is set to Primary, you must specify this parameter. In this case, this parameter serves the same purpose as VSwitchId, but you cannot specify both VSwitchId and this parameter.
        # 
        # - If NetworkInterface.N.InstanceType is set to Secondary or left empty, this parameter is optional. The default value is the vSwitch to which the ECS instance belongs.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_on_release is not None:
            result['DeleteOnRelease'] = self.delete_on_release

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address

        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count

        if self.network_card_index is not None:
            result['NetworkCardIndex'] = self.network_card_index

        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name

        if self.network_interface_traffic_mode is not None:
            result['NetworkInterfaceTrafficMode'] = self.network_interface_traffic_mode

        if self.primary_ip_address is not None:
            result['PrimaryIpAddress'] = self.primary_ip_address

        if self.queue_number is not None:
            result['QueueNumber'] = self.queue_number

        if self.queue_pair_number is not None:
            result['QueuePairNumber'] = self.queue_pair_number

        if self.rx_queue_size is not None:
            result['RxQueueSize'] = self.rx_queue_size

        if self.secondary_private_ip_address_count is not None:
            result['SecondaryPrivateIpAddressCount'] = self.secondary_private_ip_address_count

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.source_dest_check is not None:
            result['SourceDestCheck'] = self.source_dest_check

        if self.tx_queue_size is not None:
            result['TxQueueSize'] = self.tx_queue_size

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteOnRelease') is not None:
            self.delete_on_release = m.get('DeleteOnRelease')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')

        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')

        if m.get('NetworkCardIndex') is not None:
            self.network_card_index = m.get('NetworkCardIndex')

        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')

        if m.get('NetworkInterfaceTrafficMode') is not None:
            self.network_interface_traffic_mode = m.get('NetworkInterfaceTrafficMode')

        if m.get('PrimaryIpAddress') is not None:
            self.primary_ip_address = m.get('PrimaryIpAddress')

        if m.get('QueueNumber') is not None:
            self.queue_number = m.get('QueueNumber')

        if m.get('QueuePairNumber') is not None:
            self.queue_pair_number = m.get('QueuePairNumber')

        if m.get('RxQueueSize') is not None:
            self.rx_queue_size = m.get('RxQueueSize')

        if m.get('SecondaryPrivateIpAddressCount') is not None:
            self.secondary_private_ip_address_count = m.get('SecondaryPrivateIpAddressCount')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('SourceDestCheck') is not None:
            self.source_dest_check = m.get('SourceDestCheck')

        if m.get('TxQueueSize') is not None:
            self.tx_queue_size = m.get('TxQueueSize')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class RunInstancesRequestImageOptions(DaraModel):
    def __init__(
        self,
        login_as_non_root: bool = None,
    ):
        # Specifies whether the instance that uses the image supports logon as the ecs-user user. Valid values:
        # 
        # - true: Supports logon as the ecs-user user.
        # 
        # - false: Does not support logon as the ecs-user user.
        self.login_as_non_root = login_as_non_root

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_as_non_root is not None:
            result['LoginAsNonRoot'] = self.login_as_non_root

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginAsNonRoot') is not None:
            self.login_as_non_root = m.get('LoginAsNonRoot')

        return self

class RunInstancesRequestDataDisk(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        delete_with_instance: bool = None,
        description: str = None,
        device: str = None,
        disk_name: str = None,
        encrypt_algorithm: str = None,
        encrypted: str = None,
        kmskey_id: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
        snapshot_id: str = None,
        storage_cluster_id: str = None,
    ):
        # The ID of the automatic snapshot policy applied to the data disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable the performance burst feature. Valid values:
        # 
        # - true: Enables the feature.
        # - false: Disables the feature.
        # 
        # >This parameter is supported only when DiskCategory is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The category of data disk N. Valid values:
        # 
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: enterprise SSD.
        # - cloud: basic disk.
        # - cloud_auto: ESSD AutoPL disk.
        # - cloud_regional_disk_auto: regional enterprise SSD.
        # - cloud_essd_entry: ESSD Entry disk.
        #   >This parameter supports cloud_essd_entry only when InstanceType is set to an instance type in the ecs.u1 or ecs.e instance family.
        # - elastic_ephemeral_disk_standard: standard elastic ephemeral disk.
        # - elastic_ephemeral_disk_premium: elastic ephemeral disk - Premium Edition.
        # 
        # For I/O optimized instances, the default value is cloud_efficiency. For non-I/O optimized instances, the default value is cloud.
        # Default value description:
        # 
        # - If InstanceType is set to a retired and non-I/O optimized instance type, the default value is cloud.
        # - In other cases, the default value is cloud_efficiency. <props="china">After January 30, 2026, if the I/O optimized instance type does not support cloud_auto, the default value is cloud_efficiency. Otherwise, the default value is cloud_auto, and the performance burst feature is enabled by default (which incurs additional fees. For more information, see [Billing examples](~~368372#p_75k_2hp_7gp~~)). For more details, see [Announcement](https://www.aliyun.com/notice/117844).
        self.category = category
        # Specifies whether to release the data disk when the instance is released. Valid values:
        # - true: Releases the data disk when the instance is released.
        # - false: Retains the data disk when the instance is released.
        # 
        # Default value: true.
        self.delete_with_instance = delete_with_instance
        # The description of the data disk. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The mount point of the data disk. The naming convention for mount points varies based on the number of attached data disks:
        # 
        # - 1 to 25 data disks: /dev/xvd[b-z]
        # 
        # - More than 25 data disks: /dev/xvd[aa-zz]. For example, the 26th data disk is named /dev/xvdaa, the 27th data disk is named /dev/xvdab, and so on.
        # 
        # > - This parameter is applicable only to full images (instance images). You can set this parameter to the mount point of the data disk in the full image, and modify the DataDisk.N.Size and DataDisk.N.Category parameters to change the category and size of the data disk in the full image.
        # > - When you use a full image to create an instance, the data disks in the full image are created as the first n data disks of the ECS instance.
        self.device = device
        # The name of the data disk. The name must be 2 to 128 characters in length. It can contain letters and digits in the Unicode letter category. It can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        self.disk_name = disk_name
        # >This parameter is not available.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt data disk N. Valid values:
        # - true: Encrypts the data disk.
        # - false: Does not encrypt the data disk.
        # 
        # Default value: false.
        # 
        # 
        # >Notice: When you use a shared encrypted image to create a cloud disk based on an encrypted snapshot, you must set the Encrypted request parameter of the cloud disk to true. This ensures that the created cloud disk uses the key of the shared image recipient.</notice>
        self.encrypted = encrypted
        # The ID of the KMS key used to encrypt the data disk.
        # 
        # > If Encrypted is set to true and KMSKeyId is not specified, the default key is used for encryption, and the KMSKeyId value is returned after the instance is created.
        # > - - If the cloud disk is created from a non-shared encrypted snapshot, the encryption key used by the snapshot is used by default.
        # > - - If the cloud disk is created from a shared encrypted snapshot, the service key is used by default.
        # > - - If the cloud disk is created in a region where account-level default encryption for Block Storage is enabled, the specified account-level key is used by default.
        # > - - In other cases, the service key is used by default.
        self.kmskey_id = kmskey_id
        # Specifies the performance level of the ESSD used as a data disk. The value of N must be the same as the value of N in DataDisk.N.Category=cloud_essd. Valid values:
        # 
        # - PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # - PL1 (default): A single ESSD can deliver up to 50,000 random read/write IOPS.
        # - PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # - PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        # 
        # For more information about how to select the performance level of an ESSD, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values: 0 to min{50,000, 1000 × Capacity - Baseline performance}.
        # 
        # Baseline performance = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # >This parameter is supported only when DiskCategory is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.provisioned_iops = provisioned_iops
        # The size of data disk N. Valid values of N: 1 to 16. Unit: GiB. Valid values:
        # 
        # - cloud_efficiency: 20 to 32768.
        # - cloud_ssd: 20 to 32768.
        # - cloud_essd: The valid values depend on the value of DataDisk.N.PerformanceLevel. 
        #     - PL0: 1 to 65,536.
        #     - PL1: 20 to 65,536.
        #     - PL2: 461 to 65,536.
        #     - PL3: 1261 to 65,536.
        # - cloud: 5 to 2000.
        # - cloud_auto: 1 to 65,536.
        # - cloud_essd_entry: 10 to 32768.
        # 
        # >The value of this parameter must be greater than or equal to the size of the snapshot specified by the SnapshotId parameter.
        self.size = size
        # The ID of the snapshot used to create data disk N. Valid values of N: 1 to 16.
        # 
        # After you specify the DataDisk.N.SnapshotId parameter, the DataDisk.N.Size parameter is ignored. The actual size of the created cloud disk is the same as the size of the specified snapshot. You cannot use snapshots created on or before July 15, 2013. Otherwise, the request is rejected and an error is reported.
        self.snapshot_id = snapshot_id
        # The ID of the dedicated block storage cluster. If you want to use cloud disk resources in a dedicated block storage cluster as data disks when you create an ECS instance, specify this parameter.
        self.storage_cluster_id = storage_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.category is not None:
            result['Category'] = self.category

        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance

        if self.description is not None:
            result['Description'] = self.description

        if self.device is not None:
            result['Device'] = self.device

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.storage_cluster_id is not None:
            result['StorageClusterId'] = self.storage_cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('StorageClusterId') is not None:
            self.storage_cluster_id = m.get('StorageClusterId')

        return self

class RunInstancesRequestClockOptions(DaraModel):
    def __init__(
        self,
        ptp_status: str = None,
    ):
        # The Precision Time Protocol (PTP) status. Valid values:
        # 
        # - enabled: Enables PTP.
        # 
        # - disabled: Disables PTP.
        # 
        # Default value: disabled.
        self.ptp_status = ptp_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ptp_status is not None:
            result['PtpStatus'] = self.ptp_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PtpStatus') is not None:
            self.ptp_status = m.get('PtpStatus')

        return self

class RunInstancesRequestArn(DaraModel):
    def __init__(
        self,
        assume_role_for: int = None,
        role_type: str = None,
        rolearn: str = None,
    ):
        # >This parameter is not available.
        self.assume_role_for = assume_role_for
        # >This parameter is not available.
        self.role_type = role_type
        # >This parameter is not available.
        self.rolearn = rolearn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.rolearn is not None:
            result['Rolearn'] = self.rolearn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('Rolearn') is not None:
            self.rolearn = m.get('Rolearn')

        return self

class RunInstancesRequestSystemDisk(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        category: str = None,
        description: str = None,
        disk_name: str = None,
        performance_level: str = None,
        size: str = None,
        bursting_enabled: bool = None,
        encrypt_algorithm: str = None,
        encrypted: str = None,
        kmskey_id: str = None,
        provisioned_iops: int = None,
        storage_cluster_id: str = None,
    ):
        # The ID of the automatic snapshot policy applied to the system disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The system disk category. Valid values:
        # 
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: ESSD.
        # - cloud: basic disk.
        # - cloud_auto: ESSD AutoPL disk.
        # - cloud_essd_entry: ESSD Entry disk.
        # 
        # Default value descriptions:
        # 
        # - If InstanceType is a retired and non-I/O optimized instance type, the default value is `cloud`.
        # - In other cases, the default value is `cloud_efficiency`.<props="china">After January 30, 2026, for instance families that only support ESSD, the default value will be changed from cloud_efficiency to cloud_essd PL0. For more information, see [Announcement](https://www.aliyun.com/notice/117844).
        # 
        # > This parameter can be set to `cloud_essd_entry` only when `InstanceType` is set to [u1, universal instance family](https://help.aliyun.com/document_detail/457079.html) (`ecs.u1`) or [e, economy instance family](https://help.aliyun.com/document_detail/108489.html) (`ecs.e`).
        self.category = category
        # The system disk description. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The system disk name. The name must be 2 to 128 characters in length. It can contain letters (including English and Chinese letters) and digits in the Unicode letter category. It can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        self.disk_name = disk_name
        # When creating an ESSD as the system disk, set the performance level of the disk. Valid values:
        # 
        # - PL0: A single disk can deliver up to 10,000 random read/write IOPS.
        # - PL1 (default): A single disk can deliver up to 50,000 random read/write IOPS.
        # - PL2: A single disk can deliver up to 100,000 random read/write IOPS.
        # - PL3: A single disk can deliver up to 1,000,000 random read/write IOPS.
        # 
        # For details on how to select an ESSD performance level, see [ESSD](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The system disk size. Unit: GiB. Valid values:
        # 
        # - Basic disk: 20 to 500.
        # - ESSD:
        #   - PL0: 1 to 2048.
        #   - PL1: 20 to 2048.
        #   - PL2: 461 to 2048.
        #   - PL3: 1261 to 2048.
        # - ESSD AutoPL disk: 1 to 2048.
        # - Other disk categories: 20 to 2048.
        # 
        # The value of this parameter must be greater than or equal to max{1, ImageSize}.
        # 
        # Default value: max{40, the size of the image specified by the ImageId parameter}.
        self.size = size
        # Specifies whether to enable the performance burst feature. Valid values:
        # 
        # - true: Enables the feature.
        # - false: Disables the feature.
        # 
        # >This parameter is supported only when SystemDisk.Category is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # >This parameter is not available.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt the system disk. Valid values:
        # 
        # - true: Encrypts the system disk.
        # 
        # - false: Does not encrypt the system disk.
        # 
        # Default value: false.
        # 
        # >You cannot encrypt the system disk when you create an instance in active Zone D of the China (Hong Kong) region or active Zone A of the Singapore region.
        # 
        # >Notice: When you use a shared encrypted image to create a cloud disk based on an encrypted snapshot, you must set the Encrypted request parameter of the cloud disk to true. This ensures that the created cloud disk uses the key of the shared image recipient.</notice>
        self.encrypted = encrypted
        # The ID of the KMS key used to encrypt the system disk.
        # 
        # > If Encrypted is set to true and KMSKeyId is not specified, the default key is used for encryption, and the KMSKeyId value is returned after the instance is created.
        # > - - If the cloud disk is created from a non-shared encrypted snapshot, the encryption key used by the snapshot is used by default.
        # > - - If the cloud disk is created from a shared encrypted snapshot, the service key is used by default.
        # > - - If the cloud disk is created in a region where account-level default encryption for Block Storage is enabled, the specified account-level key is used by default.
        # > - - In other cases, the service key is used by default.
        self.kmskey_id = kmskey_id
        # The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values: 0 to min{50,000, 1000 × Capacity - Baseline performance}.
        # 
        # Baseline performance = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # >This parameter is supported only when SystemDisk.Category is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.provisioned_iops = provisioned_iops
        # The ID of the dedicated block storage cluster. If you want to use cloud disk resources in a dedicated block storage cluster as the system disk when you create an ECS instance, specify this parameter.
        self.storage_cluster_id = storage_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id

        if self.category is not None:
            result['Category'] = self.category

        if self.description is not None:
            result['Description'] = self.description

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.storage_cluster_id is not None:
            result['StorageClusterId'] = self.storage_cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('StorageClusterId') is not None:
            self.storage_cluster_id = m.get('StorageClusterId')

        return self

class RunInstancesRequestSecurityOptions(DaraModel):
    def __init__(
        self,
        confidential_computing_mode: str = None,
        trusted_system_mode: str = None,
        enable_secure_boot: bool = None,
    ):
        # The confidential computing mode. Valid value: Enclave.
        # 
        # When this parameter is set to Enclave, the ECS instance uses Enclave to build a confidential computing environment. Currently, only the c7, g7, and r7 instance types support specifying this parameter to use Enclave confidential computing when you call RunInstances. Details:
        # 
        # - The confidential computing feature is in invitational preview.
        # 
        # - To create an ECS instance with Enclave confidential computing by calling an API operation, you can only call RunInstances. CreateInstance does not support the SecurityOptions.ConfidentialComputingMode parameter.
        # 
        # - Enclave confidential computing relies on the trusted system (vTPM). When you specify that an ECS instance uses Enclave to build a confidential computing environment, the trusted system is also enabled for the instance. Therefore, when you call this operation, if you set SecurityOptions.ConfidentialComputingMode=Enclave, the created ECS instance will have both the Enclave confidential computing mode and the trusted system enabled, regardless of whether you set SecurityOptions.TrustedSystemMode=vTPM.
        # 
        # For more information about confidential computing, see [Use Enclave to build a confidential computing environment](https://help.aliyun.com/document_detail/203433.html).
        self.confidential_computing_mode = confidential_computing_mode
        # The trusted system mode. Valid value: vTPM.
        # 
        # Currently, the trusted system mode supports the following instance types:
        # - g7, c7, and r7.
        # - security-enhanced instance families (g7t, c7t, and r7t).
        # 
        # When you create an ECS instance of one of the preceding instance types, you must configure this parameter. Details:
        # 
        # - If you use the Alibaba Cloud trusted system, set this parameter to vTPM. This allows the Alibaba Cloud trusted system to perform trusted verification when the instance starts.
        # - If you do not use the Alibaba Cloud trusted system, you can leave this parameter unspecified. However, note that if the ECS instance you create uses the Enclave confidential computing mode (SecurityOptions.ConfidentialComputingMode=Enclave), the trusted system is also enabled for the instance.
        # - To create a trusted ECS instance by calling an API operation, you can only call RunInstances. CreateInstance does not support the SecurityOptions.TrustedSystemMode parameter.
        # > If you specify an instance as a trusted instance when you create it, you can only use images that support the trusted system when you replace the system disk.
        # 
        # For more information about the trusted system, see [Overview of the trusted feature for security-enhanced instance families](https://help.aliyun.com/document_detail/201394.html).
        self.trusted_system_mode = trusted_system_mode
        # Specifies whether to enable UEFI Secure Boot.
        self.enable_secure_boot = enable_secure_boot

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidential_computing_mode is not None:
            result['ConfidentialComputingMode'] = self.confidential_computing_mode

        if self.trusted_system_mode is not None:
            result['TrustedSystemMode'] = self.trusted_system_mode

        if self.enable_secure_boot is not None:
            result['EnableSecureBoot'] = self.enable_secure_boot

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidentialComputingMode') is not None:
            self.confidential_computing_mode = m.get('ConfidentialComputingMode')

        if m.get('TrustedSystemMode') is not None:
            self.trusted_system_mode = m.get('TrustedSystemMode')

        if m.get('EnableSecureBoot') is not None:
            self.enable_secure_boot = m.get('EnableSecureBoot')

        return self

class RunInstancesRequestSchedulerOptions(DaraModel):
    def __init__(
        self,
        dedicated_host_cluster_id: str = None,
    ):
        # The ID of the dedicated host cluster to which the ECS instance belongs. The system automatically selects a dedicated host from the specified dedicated host cluster to deploy the ECS instance.
        # 
        # > This parameter takes effect only when Tenancy is set to host.
        # 
        # If you specify both a dedicated host (DedicatedHostId) and a dedicated host cluster (SchedulerOptions.DedicatedHostClusterId):
        # - If the dedicated host belongs to the dedicated host cluster, the ECS instance is preferentially deployed on the specified dedicated host.
        # - If the dedicated host does not belong to the dedicated host cluster, the ECS instance fails to be created.
        # 
        # <props="china">You can call the [DescribeDedicatedHostClusters](https://help.aliyun.com/document_detail/184145.html) operation to query the list of dedicated host cluster IDs.
        # 
        # <props="intl">You can call the [DescribeDedicatedHostClusters](https://help.aliyun.com/document_detail/184145.html) operation to query the list of dedicated host cluster IDs.
        # 
        # <props="partner">You can call the [DescribeDedicatedHostClusters](https://help.aliyun.com/document_detail/184145.html) operation to query the list of dedicated host cluster IDs.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_cluster_id is not None:
            result['DedicatedHostClusterId'] = self.dedicated_host_cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostClusterId') is not None:
            self.dedicated_host_cluster_id = m.get('DedicatedHostClusterId')

        return self

class RunInstancesRequestPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # The ID of the private pool, which is the ID of the elasticity assurance or capacity reservation service.
        self.id = id
        # The private pool options for instance startup. After the elasticity assurance or capacity reservation service takes effect, private pool capacity is generated for you to select when you start the instance. Valid values:
        # 
        # - Open: Open mode. The system automatically matches open private pool capacity. If no eligible private pool capacity is available, the instance is started by using public pool resources. In this mode, you do not need to specify the PrivatePoolOptions.Id parameter.
        # - Target: Specified mode. The instance is started by using the specified private pool capacity. If the specified private pool capacity is unavailable, the instance fails to be started. In this mode, you must specify the private pool ID, which means the PrivatePoolOptions.Id parameter is required.
        # - None: Unused mode. The instance is started without using private pool capacity.
        # 
        # Default value: None.
        # 
        # In any of the following scenarios, the private pool options for instance startup can only be set to None or left unspecified:
        # - Creating a spot instance.
        # - Creating an ECS instance on a dedicated host (DDH).
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')

        return self

class RunInstancesRequestHibernationOptions(DaraModel):
    def __init__(
        self,
        configured: bool = None,
    ):
        # > This parameter is in invitational preview and is not available.
        self.configured = configured

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configured is not None:
            result['Configured'] = self.configured

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configured') is not None:
            self.configured = m.get('Configured')

        return self

class RunInstancesRequestCpuOptions(DaraModel):
    def __init__(
        self,
        core: int = None,
        numa: str = None,
        threads_per_core: int = None,
        topology_type: str = None,
        nested_virtualization: str = None,
    ):
        # The number of CPU cores.
        # 
        # <props="china">Default value: For more information, see [Customize CPU options](https://help.aliyun.com/document_detail/145895.html).
        self.core = core
        # **[Deprecated]** This parameter is deprecated.
        self.numa = numa
        # The number of CPU threads. The number of vCPUs of the ECS instance is calculated by using the following formula: Number of vCPUs = Value of CpuOptions.Core × Value of CpuOptions.ThreadsPerCore.
        # 
        # - CpuOptions.ThreadsPerCore=1 indicates that CPU hyper-threading is disabled.
        # 
        # - Only specific instance types support the configuration of the number of CPU threads.
        # 
        # <props="china">Valid values and default value: For more information, see [Customize CPU options](https://help.aliyun.com/document_detail/145895.html).
        self.threads_per_core = threads_per_core
        # The CPU topology type of the instance. Valid values:
        # 
        # - ContinuousCoreToHTMapping: When ContinuousCoreToHTMapping is selected, the hyper-threads (HTs) of the same core in the CPU topology of the instance are continuous.
        # - DiscreteCoreToHTMapping: When DiscreteCoreToHTMapping is selected, the HTs of the same core in the instance are discrete.
        # 
        # Default value: None.
        # 
        # > Only specific instance types support this parameter. For more information about the supported instance types, see [View and modify the CPU topology](https://help.aliyun.com/document_detail/2636059.html).
        self.topology_type = topology_type
        # > This parameter is in invitational preview and is not available.
        self.nested_virtualization = nested_virtualization

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.core is not None:
            result['Core'] = self.core

        if self.numa is not None:
            result['Numa'] = self.numa

        if self.threads_per_core is not None:
            result['ThreadsPerCore'] = self.threads_per_core

        if self.topology_type is not None:
            result['TopologyType'] = self.topology_type

        if self.nested_virtualization is not None:
            result['NestedVirtualization'] = self.nested_virtualization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Core') is not None:
            self.core = m.get('Core')

        if m.get('Numa') is not None:
            self.numa = m.get('Numa')

        if m.get('ThreadsPerCore') is not None:
            self.threads_per_core = m.get('ThreadsPerCore')

        if m.get('TopologyType') is not None:
            self.topology_type = m.get('TopologyType')

        if m.get('NestedVirtualization') is not None:
            self.nested_virtualization = m.get('NestedVirtualization')

        return self

