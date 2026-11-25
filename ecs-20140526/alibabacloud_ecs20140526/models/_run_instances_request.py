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
        # Specifies whether the instance is associated with a dedicated host. Valid values:
        # 
        # - default: The instance is not associated with a dedicated host. If an instance with economical mode enabled is stopped and then started, and the original dedicated host has insufficient available resources, the instance is placed on another dedicated host in the automatic deployment resource pool.
        # 
        # - host: The instance is associated with a dedicated host. If an instance with economical mode enabled is stopped and then started, it remains on the original dedicated host. If the original dedicated host has insufficient available resources, the instance fails to start.
        # 
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
        # > This parameter is not available.
        self.arn = arn
        # Specifies whether to automatically pay for the instance when you create the instance. Valid values:
        # 
        # - true: Automatically pays for the instance.
        # 
        #     > If you set this parameter to true, make sure that automatic payment method has sufficient balance. Otherwise, an abnormal order is generated and can only be canceled. If automatic payment method has insufficient balance, you can set AutoPay to false. In this case, an unpaid order is generated, and you can log on to the ECS console to pay for the order.
        # 
        # - false: Generates an order without deducting fees.
        # 
        #     > If InstanceChargeType is set to PostPaid, you cannot set AutoPay to false.
        # 
        # Default value: true.
        self.auto_pay = auto_pay
        # The automatic release time of the pay-as-you-go instance. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # - If the seconds (ss) value is not 00, it is automatically set to the start of the current minute (mm).
        # 
        # - The minimum release time is half an hour after the current time.
        # 
        # - The maximum release time cannot exceed three years from the current time.
        # [ISO 8601](https://help.aliyun.com/document_detail/25696.html)
        self.auto_release_time = auto_release_time
        # Specifies whether to enable auto-renewal. This parameter takes effect only when InstanceChargeType is set to PrePaid. Valid values:
        # 
        # - true: enables auto-renewal.
        # - false: disables auto-renewal.
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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The clock configurations of the instance.
        self.clock_options = clock_options
        # The performance mode of the burstable instance. Valid values:
        # 
        # - Standard: standard mode. For more information about instance performance, see the "Standard mode" section in [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        # - Unlimited: unlimited mode. For more information about instance performance, see the "Unlimited mode" section in [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.credit_specification = credit_specification
        # The data disk configurations.
        self.data_disk = data_disk
        # The dedicated host ID.
        # <props="china">You can invoke [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/134242.html) to query the dedicated host ID list.
        # 
        # <props="intl">You can invoke [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/134242.html) to query the dedicated host ID list.
        # 
        # >Notice: Dedicated hosts do not support the creation of spot instance. After you specify the `DedicatedHostId` parameter, the `SpotStrategy` and `SpotPriceLimit` Settings in the request are automatically ignored.</notice>
        self.dedicated_host_id = dedicated_host_id
        # The release protection property of the instance. It specifies whether the instance can be released through the console or API ([DeleteInstance](https://help.aliyun.com/document_detail/25507.html)). Valid values: 
        # 
        # -  true: enables release protection.
        # -  false: disables release protection.
        # 
        # Default value: false.
        # 
        # > This property applies only to pay-as-you-go instances and can only restrict manual release operations. It does not take effect on system release operations.
        self.deletion_protection = deletion_protection
        # The group number of the instance in the deployment set. If the deployment set policy is set to AvailabilityGroup, you can use this parameter to specify the group number. Valid values: 1 to 7.
        self.deployment_set_group_no = deployment_set_group_no
        # The ID of the deployment set.
        self.deployment_set_id = deployment_set_id
        # The instance description. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # Specifies whether to perform only a dry run on the request. Valid values:
        # 
        # -  true: performs a dry run and does not create the instance. Check items include whether required parameters are specified, the request format, service limits, and ECS inventory. If the check fails, the corresponding error is returned. If the check succeeds, the DryRunOperation error code is returned.
        # -  false (default): performs a normal request and creates the instance directly after the check succeeds.
        self.dry_run = dry_run
        # The hostname of the instance. Limits:
        # 
        # - Periods (.) and hyphens (-) cannot be used as the first or last character, and cannot be used consecutively.
        # - Windows instances: The name must be 2 to 15 characters in length. It cannot contain periods (.) or contain only digits. It can contain uppercase and lowercase letters, digits, and hyphens (-).
        # - Other instances (such as Linux instances):
        #     - The name must be 2 to 64 characters in length. It can contain multiple periods (.). The string between two periods is a segment, which can contain uppercase and lowercase letters, digits, and hyphens (-).
        #     - You can use the ${instance_id} placeholder to write the instance ID into the HostName parameter. For example, if HostName=k8s-${instance_id} and the created ECS instance ID is i-123abc****, the hostname of the instance is k8s-i-123abc****.
        # 
        # When you create multiple ECS instances, you can:
        # 
        # - Specify sequential hostnames in batches. For more information, see [Specify sequential instance names or hostnames](https://help.aliyun.com/document_detail/196048.html).
        # - Specify hostnames for multiple instances separately by using the HostNames.N parameter. Note that you cannot specify both HostName and HostNames.N.
        self.host_name = host_name
        # Specifies different hostnames for each instance when you create multiple instances.
        self.host_names = host_names
        # The ID of the HPC cluster to which the instance belongs. 
        # 
        # This parameter is required when you create an SCC instance. You can call [CreateHpcCluster](https://help.aliyun.com/document_detail/109138.html) to create an HPC cluster.
        self.hpc_cluster_id = hpc_cluster_id
        # Specifies whether to enable the access channel for instance metadata. Valid values:
        # - enabled: enables the access channel.
        # - disabled: disables the access channel.
        # 
        # Default value: enabled.
        # > For more information about instance metadata, see [Overview of instance metadata](https://help.aliyun.com/document_detail/49122.html).
        self.http_endpoint = http_endpoint
        # > This parameter is not available.
        self.http_put_response_hop_limit = http_put_response_hop_limit
        # Specifies whether to forcibly use the security hardening mode (IMDSv2) when you access instance metadata. Valid values:
        # - optional: does not forcibly use the security hardening mode.
        # - required: forcibly uses the security hardening mode. After this value is set, instance metadata cannot be accessed in normal mode.
        # 
        # Default value: optional.
        # > For more information about the modes for accessing instance metadata, see [Access modes of instance metadata](https://help.aliyun.com/document_detail/150575.html).
        self.http_tokens = http_tokens
        # The image family name. Set this parameter to use the latest available image in the specified image family to create the instance.
        # 
        # The name must be 2 to 128 characters in length. It cannot start with a special character, digit, http://, or https://. It can contain only the following special characters: periods (.), underscores (_), hyphens (-), and colons (:).
        # 
        # Take note of the following items:
        # 
        # - If ImageId is specified, you cannot specify this parameter.
        # - If ImageId is not specified but the launch template specified by LaunchTemplateId or LaunchTemplateName has ImageId configured, you cannot specify this parameter.
        # - If ImageId is not specified and the launch template specified by LaunchTemplateId or LaunchTemplateName does not have ImageId configured, you can specify this parameter.
        # - If neither ImageId nor LaunchTemplateId and LaunchTemplateName are specified, you can specify this parameter.
        # > For information about the image families associated with Alibaba Cloud official images, see [Public images](https://help.aliyun.com/document_detail/108393.html).
        self.image_family = image_family
        # The image ID. The image resource selected when the instance is started. You can call [DescribeImages](https://help.aliyun.com/document_detail/25534.html) to query available image resources. If you do not specify LaunchTemplateId or LaunchTemplateName to determine a launch template, and do not specify ImageFamily to use the latest available image in an image family, ImageId is required.
        self.image_id = image_id
        # The image configurations.
        self.image_options = image_options
        # The billing method of the instance. Valid values:
        # 
        # -  PrePaid: subscription.
        # -  PostPaid: pay-as-you-go.
        # 
        # Default value: PostPaid.
        # 
        # <props="china">When you select subscription, you must ensure that your account supports balance payment or credit payment. Otherwise, an InvalidPayMethod error is returned.
        # 
        # <props="intl">When you select subscription, you must ensure that your account supports credit payment. Otherwise, an InvalidPayMethod error is returned.
        self.instance_charge_type = instance_charge_type
        # The instance name. The name must be 2 to 128 characters in length. It can contain letters and digits in Unicode, and can include colons (:), underscores (_), periods (.), and hyphens (-). The default value is the InstanceId of the instance.
        # 
        # When you create multiple ECS instances, you can specify sequential instance names in batches, which can include square brackets ([]) and commas (,). For more information, see [Specify sequential instance names or hostnames](https://help.aliyun.com/document_detail/196048.html).
        self.instance_name = instance_name
        # The instance type. If you do not specify `LaunchTemplateId` or `LaunchTemplateName` to determine a launch template, `InstanceType` is a required parameter.  
        # 
        # - Instance type selection: See [instance family](https://help.aliyun.com/document_detail/25378.html) or invoke [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) to view the performance data of the target instance type, or see [Best practices for instance type selection](https://help.aliyun.com/document_detail/58291.html) to learn how to select an instance type.
        # - Inventory query: invoke [DescribeAvailableResource](https://help.aliyun.com/document_detail/66186.html) to view the active resource supply in a specific region or zone.
        self.instance_type = instance_type
        # The network billing method. Valid values:
        # 
        # - PayByBandwidth: pay-by-bandwidth.
        # - PayByTraffic: pay-by-traffic.
        # 
        # Default value: PayByTraffic.
        # 
        # > In **pay-by-traffic** mode, the peak inbound and outbound bandwidths are bandwidth upper limits and are not guaranteed service level indicators. When resource contention occurs, the peak bandwidth may be limited. If your business requires guaranteed bandwidth, use the **pay-by-bandwidth** mode.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth. Unit: Mbit/s. Valid values:
        # 
        # - When the purchased outbound public bandwidth is less than or equal to 10 Mbit/s: 1 to 10. Default value: 10.
        # - When the purchased outbound public bandwidth is greater than 10 Mbit/s: 1 to the value of InternetMaxBandwidthOut. Default value: the value of InternetMaxBandwidthOut.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s. Valid values: 0 to 100.
        # 
        # Default value: 0.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether the instance is an I/O optimized instance. For [retired instance types](https://help.aliyun.com/document_detail/55263.html), the default value is none. For other instance types, the default value is optimization. Valid values:
        # 
        # - none: The instance is not I/O optimization.
        # - optimized: The instance is I/O optimization.
        self.io_optimized = io_optimized
        # The IPv6 addresses that are assigned to the primary ENI. You can specify up to 10 IPv6 addresses. Valid values of N: 1 to 10.
        # 
        # Example: Ipv6Address.1=2001:db8:1234:1a00::***.
        # 
        # Note:
        # 
        # - If you specify Ipv6Address.N, the value of Amount can only be 1, and you cannot specify Ipv6AddressCount at the same time.
        # 
        # - If NetworkInterface.N.InstanceType is set to Primary, you cannot specify Ipv6Addresses.N or Ipv6AddressCount. Instead, you must specify NetworkInterface.N.Ipv6Addresses.N or NetworkInterface.N.Ipv6AddressCount.
        self.ipv_6address = ipv_6address
        # The number of IPv6 addresses to be randomly generated for the primary ENI. Valid values: 1 to 10.
        #          
        # Take note of the following items:
        # 
        # - You cannot specify both Ipv6Address.N and Ipv6AddressCount.
        # 
        # - If NetworkInterface.N.InstanceType is set to Primary, you cannot specify Ipv6Address.N or Ipv6AddressCount. You can only specify NetworkInterface.N.Ipv6Address.N or NetworkInterface.N.Ipv6AddressCount.
        self.ipv_6address_count = ipv_6address_count
        # >This parameter is in invitational preview and is not available for public use.
        self.isp = isp
        # The key pair name.
        # >For Windows instances, this parameter is ignored. The default value is empty. Even if this parameter is specified, only the Password parameter takes effect.
        self.key_pair_name = key_pair_name
        # The launch template ID. For more information, call [DescribeLaunchTemplates](https://help.aliyun.com/document_detail/73759.html).
        # 
        # When you use a launch template to create an instance, you must specify LaunchTemplateId or LaunchTemplateName to determine the launch template.
        self.launch_template_id = launch_template_id
        # The launch template name.
        # 
        # When you use a launch template to create an instance, you must specify LaunchTemplateId or LaunchTemplateName to determine the launch template.
        self.launch_template_name = launch_template_name
        # The launch template version. If you specify LaunchTemplateId or LaunchTemplateName but do not specify the launch template version, the default version is used.
        self.launch_template_version = launch_template_version
        # The unique identifier of the managed host, such as mh-f2d3647ca21****.
        self.managed_host_id = managed_host_id
        # The minimum Quantity of ECS instances to purchase. Valid values: 1 to 100.
        # 
        # The number of successfully created ECS instances depends on the specified Amount and minAmount:
        # 
        # - When minAmount is not specified: Instances are created based on the Amount value. If the inventory is insufficient, the API returns a creation failed, and no instances are created.
        # 
        # - When minAmount is specified:
        #   - If the ECS inventory < minAmount: No ECS instances are created, and the API returns a creation failed.
        #   - If minAmount ≤ ECS inventory < Amount: Instances are created based on the inventory, and the API returns a creation success.
        #   - If the ECS inventory ≥ Amount: Instances are created based on the specified Amount, and the API returns a creation success.
        self.min_amount = min_amount
        # The ENI information.
        self.network_interface = network_interface
        # The number of queues for the primary ENI. Take note of the following items:
        # 
        # - The value cannot exceed the maximum number of queues per ENI allowed by the instance type.
        # 
        # - The total number of queues for all ENIs of the instance cannot exceed the total queue quota allowed by the instance type. You can call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query the MaximumQueueNumberPerEni and TotalEniQueueQuantity fields for the maximum number of queues per ENI and the total quota of the instance type.
        # 
        # - If NetworkInterface.N.InstanceType is set to Primary, you cannot specify NetworkInterfaceQueueNumber. You can only specify NetworkInterface.N.QueueNumber.
        self.network_interface_queue_number = network_interface_queue_number
        # The network configurations.
        self.network_options = network_options
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The instance password. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The special characters can be:
        # 
        # ```
        # ()`~!@#$%^&*-_+=|{}[]:;\\"<>,.?/
        # ```
        # 
        # For Windows instances, the password cannot start with a forward slash (/).
        # 
        # > If you specify the Password parameter, we recommend that you send the request over HTTPS to prevent password leaks.
        self.password = password
        # Specifies whether to use the preset password of the image. Valid values:
        # 
        # - true: Uses the preset password.
        # - false: Does not use the preset password.
        # 
        # Default value: false.
        # 
        # > When you use this parameter, the Password parameter must be empty, and you must ensure that the image you use has a password configured.
        self.password_inherit = password_inherit
        # The subscription period of the resource. The unit is specified by PeriodUnit. This parameter takes effect and is required only when InstanceChargeType is set to PrePaid. If DedicatedHostId is specified, the value cannot exceed the subscription period of the dedicated host. Valid values:
        # 
        # <props="china">
        # - When PeriodUnit is set to Week, valid values of Period are 1, 2, 3, and 4.
        # - When PeriodUnit is set to Month, valid values of Period are 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        # 
        # 
        # 
        # <props="intl">When PeriodUnit is set to Month, valid values of Period are 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        self.period = period
        # The billing unit of the subscription billing method. Valid values: 
        # 
        # <props="china">
        # - Week.
        # - Month (default).
        # 
        # 
        # 
        # <props="intl">Month (default).
        self.period_unit = period_unit
        # The private DNS name configurations of the instance.
        # 
        # 
        # For more information about private Private domain resolution, see [Private Private domain resolution for ECS](https://help.aliyun.com/document_detail/2844797.html).
        self.private_dns_name_options = private_dns_name_options
        # The private IP address of the instance. When you specify system reserved IP address for a VPC-type ECS instance, the IP address must be selected from the idle CIDR block of the vSwitch (VSwitchId).
        # 
        # Take note of the following items:
        # 
        # - After PrivateIpAddress is specified:
        #     - If the Amount parameter is set to 1, it indicates that system reserved IP address is assigned to the single ECS instance being created.
        #     - If the Amount parameter is set to a value greater than 1, it indicates that when multiple ECS instances are created in batches, consecutive private IP addresses starting from the specified private IP address are assigned to the instances. Note that in this case, you cannot bind secondary ENIs to the instances (that is, you cannot specify parameters like NetworkInterface.N.*).
        # 
        # -  If NetworkInterface.N.InstanceType is set to Primary, you cannot specify PrivateIpAddress. You can only specify NetworkInterface.N.PrimaryIpAddress.
        # 
        # >The first and the last three IP addresses of each vSwitch are reserved by the system and cannot be specified.
        # For example, if the vSwitch CIDR block is 192.168.1.0/24, the four IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved by the system.
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
        # - Active: enables security hardening. This value takes effect only for public images.
        # - Deactive: disables security hardening. This value takes effect for all image types.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The ID of the security group to which the new instance belongs. Instances in the same security group can access each other. The maximum number of instances that a security group can contain depends on the security group type. For more information, see the "Security group limits" section in [Limits](~~25412#SecurityGroupQuota~~).
        # 
        # > SecurityGroupId determines the network type of the instance. For example, if the network type of the specified security group is VPC, the instance is a VPC-type instance and the VSwitchId parameter must be specified.
        # 
        # If you do not specify LaunchTemplateId or LaunchTemplateName to determine a launch template, the security group ID is required. Take note of the following items:
        # 
        # - You can specify one security group by using SecurityGroupId, or specify one or more security groups by using SecurityGroupIds.N. However, you cannot specify both SecurityGroupId and SecurityGroupIds.N.
        # 
        # - If NetworkInterface.N.InstanceType is set to Primary, you cannot specify SecurityGroupId or SecurityGroupIds.N. You can only specify NetworkInterface.N.SecurityGroupId or NetworkInterface.N.SecurityGroupIds.N.
        self.security_group_id = security_group_id
        # Adds the instance to multiple security groups at the same time. The valid values of N depend on the quota of security groups that the instance can join. For more information, see [Security group limits](https://help.aliyun.com/document_detail/101348.html).
        # 
        # Note:
        # - You cannot specify both SecurityGroupId and SecurityGroupIds.N at the same time.
        # - If NetworkInterface.N.InstanceType is set to Primary, you cannot specify SecurityGroupId or SecurityGroupIds.N. You can only specify NetworkInterface.N.SecurityGroupId or NetworkInterface.N.SecurityGroupIds.N.
        self.security_group_ids = security_group_ids
        # The protection period of the spot instance. Unit: hours. Valid values:
        # - 1: After the spot instance is created, Alibaba Cloud guarantees that the spot instance will not be automatic release within 1 hour. After 1 hour, the system compares the bid price with the marketplace price and checks the resource inventory in real-time to determine whether to retain or revoke the spot instance.
        # - 0: After the spot instance is created, Alibaba Cloud does not guarantee the runtime of the spot instance. The system compares the bid price with the marketplace price and checks the resource inventory in real-time to determine whether to retain or revoke the spot instance.
        # 
        # Default value: 1.
        # > 
        # > - This parameter currently only supports 0 or 1.
        # > - Preemptible instances are billing by the second. We recommend that you select an appropriate protection period based on the execution duration of your specific node.
        # > - Alibaba Cloud sends a notification through an ECS system event 5 minutes before the spot instance is reclaimed.
        self.spot_duration = spot_duration
        # The break mode of the preemptible instance. Valid values:
        # 
        # - Terminate: releases the instance.
        # - Stop: puts the instance into economical mode.
        # 
        #   For more information about economical mode, see [economical mode for pay-as-you-go instances](https://help.aliyun.com/document_detail/63353.html).
        # 
        # Default value: Terminate.
        self.spot_interruption_behavior = spot_interruption_behavior
        # The maximum hourly price for the instance. It supports up to three decimal places. This parameter takes effect only when SpotStrategy is set to SpotWithPriceLimit.
        self.spot_price_limit = spot_price_limit
        # The bidding policy for the pay-as-you-go instance. This parameter takes effect only when InstanceChargeType is set to PostPaid. Valid values:
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
        # The tag configurations of the instance, cloud disks, and primary ENI.
        self.tag = tag
        # Specifies whether to create the instance on a dedicated host. Valid values:
        # - default: creates the instance on a non-dedicated host.
        # - host: creates the instance on a dedicated host. If you do not specify DedicatedHostId, Alibaba Cloud automatically selects a dedicated host to place the instance.
        # Default value: default.
        self.tenancy = tenancy
        # Specifies whether to automatically append sequential suffixes to HostName and InstanceName when you create multiple instances. The sequential suffix starts from 001 and increments up to 999. Valid values:
        # - true: Appends sequential suffixes.
        # - false: Does not append sequential suffixes.
        # 
        # Default value: false.
        # 
        # If HostName or InstanceName is set in a specified sorting format without the name_suffix naming suffix, meaning the naming format is name_prefix[begin_number,bits], UniqueSuffix does not take effect, and the names are sorted only in the specified order.
        # 
        # For more information, see [Specify sequential instance names or hostnames](https://help.aliyun.com/document_detail/196048.html).
        self.unique_suffix = unique_suffix
        # The instance user data. The data must be Base64-encoded, and the size of the custom data before Base64 encoding cannot exceed 32 KB.
        # 
        # For more information about the limits, format, and execution frequency of instance user data, see [Instance user data](https://help.aliyun.com/document_detail/49121.html).
        # 
        # >To ensure the security of UserData during transmission, avoid transmitting sensitive data such as passwords and private keys in plaintext. If you need to transmit such information, we recommend that you encrypt the data first, encode it in Base64, and then decrypt it inside the instance to ensure information security.
        self.user_data = user_data
        # The vSwitch ID. If you create a VPC-type ECS instance, you must specify a vSwitch ID, and the security group and the vSwitch must belong to the same VPC. You can call [DescribeVSwitches](https://help.aliyun.com/document_detail/35748.html) to query information about created vSwitches.
        # 
        # Take note of the following items:
        # 
        # - If you specify the VSwitchId parameter, the ZoneId parameter must be set to the zone where the vSwitch resides. You can also leave ZoneId unspecified, and the system automatically selects the zone where the specified vSwitch resides.
        # 
        # - If NetworkInterface.N.InstanceType is set to Primary, you cannot specify VSwitchId. You can only specify NetworkInterface.N.VSwitchId.
        self.v_switch_id = v_switch_id
        # The zone ID of the instance. You can call [DescribeZones](https://help.aliyun.com/document_detail/25610.html) to obtain the zone list.
        # 
        # > If you specify the VSwitchId parameter, the ZoneId parameter must be set to the zone where the vSwitch resides. You can also leave the ZoneId parameter unspecified, and the system automatically selects the zone where the specified vSwitch resides.
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
        # The tag key of the instance, cloud disks, and primary ENI. Valid values of N: 1 to 20. The tag key cannot be an empty string. It can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        self.key = key
        # The tag value of the instance, cloud disks, and primary ENI. Valid values of N: 1 to 20. The tag value can be an empty string. It can be up to 128 characters in length and cannot contain http:// or https://.
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
        # - false: Disables the Jumbo Frame feature. The maximum transmission unit (MTU) of all ENIs, including the primary ENI and secondary ENIs, is set to 1500.
        # 
        # - true: Enables the Jumbo Frame feature. The MTU of all ENIs, including the primary ENI and secondary ENIs, is set to 8500.
        # 
        # Default value: true.
        # 
        # > Only specific eighth-generation and later instance types support the Jumbo Frame feature. For more information, see [MTU of ECS instances](https://help.aliyun.com/document_detail/200512.html).
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
        # > This parameter takes effect only for secondary ENIs.
        self.delete_on_release = delete_on_release
        # The description of the ENI.
        # 
        # Note:
        # 
        # - The valid values of N cannot exceed the maximum number of network interface controller (NIC) supported by the target instance type. For more information, see [instance family](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controller (NIC) supported by the target instance type.
        # - The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        # - If NetworkInterface.N.InstanceType is specified as Primary, you do not need to configure the Settings for this parameter.
        self.description = description
        # The type of the ENI. The valid values of N cannot exceed the maximum number of network interface controller (NIC) supported by the target instance type. For more information, see [instance family](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controller (NIC) supported by the target instance type.
        # 
        # Valid values of the parameter:
        # 
        # - Primary: primary ENI.
        # - Secondary: secondary ENI.
        # 
        # Default value: Secondary.
        self.instance_type = instance_type
        # The IPv6 addresses that are assigned to the primary ENI. You can specify up to 10 IPv6 addresses. Valid values of the second N: 1 to 10.
        # 
        # Example: Ipv6Address.1=2001:db8:1234:1a00::***.
        # 
        # Note:
        # 
        # - This parameter takes effect only when NetworkInterface.N.InstanceType is set to Primary. If NetworkInterface.N.InstanceType is set to Secondary or left empty, you cannot specify this parameter.
        # 
        # - After you specify this parameter, the value of Amount can only be 1, and you cannot specify Ipv6AddressCount, Ipv6Address.N, or NetworkInterface.N.Ipv6AddressCount.
        self.ipv_6address = ipv_6address
        # The number of IPv6 addresses that are randomly generated for the primary ENI. Valid values: 1 to 10.
        # 
        # Note:
        # 
        # - This parameter takes effect only when NetworkInterface.N.InstanceType is set to Primary. If NetworkInterface.N.InstanceType is set to Secondary or left empty, you cannot specify this parameter.
        # 
        # - After you specify this parameter, you cannot specify Ipv6AddressCount, Ipv6Address.N, or NetworkInterface.N.Ipv6Address.N.
        self.ipv_6address_count = ipv_6address_count
        # The index of the network card specified for the network interface controller (NIC).
        # 
        # Note:
        # - Only specific instance types support specifying the network card index.
        # - If NetworkInterface.N.InstanceType is specified as Primary and the instance type supports network card, you can only configure the Settings for this parameter to 0.
        # - If NetworkInterface.N.InstanceType is specified as Secondary or left empty and the instance type supports network card, you can configure the Settings for this parameter based on the instance family. For more information, see [instance family](https://help.aliyun.com/document_detail/25378.html).
        self.network_card_index = network_card_index
        # The ID of the ENI that is attached to the instance.
        # 
        # After you configure the Settings for this parameter, the value of Amount can only be 1.
        # 
        # > This parameter takes effect only for secondary ENIs. After you specify an existing secondary ENI, you cannot configure other network interface controller (NIC) creation parameters.
        self.network_interface_id = network_interface_id
        # The name of the ENI. The name must be 2 to 128 characters in length. It can contain characters that fall under the letter categorization in Unicode, such as letters, Chinese characters, and digits. It can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # Note:
        # 
        # - The valid values of N cannot exceed the maximum number of network interface controller (NIC) supported by the target instance type. For more information, see [instance family](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controller (NIC) supported by the target instance family.
        # 
        # - If NetworkInterface.N.InstanceType is specified as Primary, you do not need to configure the Settings for this parameter.
        self.network_interface_name = network_interface_name
        # The communication pattern of the network interface controller (NIC). Valid values of the parameter:
        # 
        # - Standard: Uses the TCP communication pattern.
        # - HighPerformance: Enables the Elastic RDMA Interface (ERI) and uses the RDMA communication pattern.
        # 
        # Default value: Standard.
        # 
        # > The number of Elastic Network Interface (ENI) in RDMA mode cannot exceed the limit of the instance type. For more information, see [instance family](https://help.aliyun.com/document_detail/25378.html).
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # Adds an ENI and configures the primary IP address.
        # 
        # Note:
        # 
        # - The valid values of N cannot exceed the maximum number of network interface controller (NIC) supported by the target instance type. For more information, see [instance family](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controller (NIC) supported by the target instance type.
        #     - When you configure the Settings for one ENI, you can configure one primary ENI or one secondary ENI. If the value of the Amount parameter is greater than 1, and you configure a primary ENI and specify this parameter, consecutive primary IP addresses are allocated to multiple ECS instances starting from the specified primary IP address when you create target instances in batches. Note that you cannot attach secondary ENIs to target instances in this case.
        #     - Note that if the value of the Amount parameter is greater than 1 and you have configured the Settings for this parameter for the primary ENI, you cannot configure secondary ENIs. This means you cannot specify NetworkInterface.2.InstanceType as Secondary.
        # 
        # - If NetworkInterface.N.InstanceType is specified as Primary, this parameter serves the same purpose as PrivateIpAddress. Note that you cannot specify both this parameter and PrivateIpAddress at the same time.
        # 
        # - If NetworkInterface.N.InstanceType is specified as Secondary or left empty, this parameter specifies the primary IP address of the secondary ENI. By default, an IP address is randomly selected from the vSwitch CIDR block of the vSwitch to which the ENI belongs.
        # 
        # >- The first and last three IP addresses of each vSwitch are system reserved IP addresses and cannot be specified.
        # For example, if the vSwitch CIDR block of the vSwitch is 192.168.1.0/24, the four IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are system reserved IP addresses.
        self.primary_ip_address = primary_ip_address
        # The number of queues for the ENI.
        # 
        # Note:
        # 
        # - The valid values of N cannot exceed the maximum number of network interface controller (NIC) supported by the target instance type. For more information, see [instance family](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controller (NIC) supported by the target instance type.
        # 
        # - The value cannot exceed the maximum number of queues per ENI allowed by the target instance type.
        # 
        # - The total number of queues for all ENIs of the target instance cannot exceed the total queue quota allowed by the target instance type. You can invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query the MaximumQueueNumberPerEni and TotalEniQueueQuantity fields for the maximum number of queues per ENI and the total queue quota of the target instance type.
        # 
        # - If NetworkInterface.N.InstanceType is specified as Primary and you specify this parameter, you cannot configure the Settings for the NetworkInterfaceQueueNumber parameter.
        self.queue_number = queue_number
        # The number of queues for the RDMA ENI.
        # 
        # If you want to attach multiple RDMA ENIs to the instance, we recommend that you manually specify QueuePairNumber for each ENI based on the maximum QueuePairNumber supported by the instance type and the number of ENIs you plan to use. Make sure that the total QueuePairNumber of all ENIs does not exceed the maximum value allowed by the instance type. You can call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum value for the instance type.
        # 
        # >Notice: If QueuePairNumber is not specified for an RDMA ENI, the maximum QueuePairNumber supported by all RDMA ENIs of the instance type is used by default. Therefore, after you attach an RDMA ENI for which QueuePairNumber is not specified, you cannot attach more RDMA ENIs. Regular ENIs are not subject to this limit.</notice>
        self.queue_pair_number = queue_pair_number
        # The inbound queue depth of the ENI.
        # 
        # 
        # <props="china">
        # 
        # > This parameter is in invitational preview and is not available. If you want to use this parameter, [submit a ticket](https://selfservice.console.aliyun.com/ticket/createIndex) to apply for the whitelist.
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
        # When you use this parameter, take note of the following items:
        # 
        # - This parameter is applicable only to seventh-generation and later ECS instance types.
        # 
        # - This parameter is applicable only to Linux images.
        # 
        # - A larger inbound queue depth can improve inbound throughput and reduce the packet loss rate, but it consumes more memory.
        self.rx_queue_size = rx_queue_size
        # The number of secondary private IPv4 addresses that are allocated to the network interface controller (NIC). Valid values: 1 to 49.
        # 
        # - The value cannot exceed the limit on the number of IP addresses for the instance type. For more information, see [instance family](~~~25378~~).
        # - NetworkInterface.N.SecondaryPrivateIpAddressCount specifies the number of secondary private IPv4 addresses that are allocated to the network interface controller (NIC), excluding the primary private IP address of the network interface controller (NIC). The system randomly allocates these addresses from the active CIDR block of the vSwitch (NetworkInterface.N.VSwitchId) to which the network interface controller (NIC) belongs.
        self.secondary_private_ip_address_count = secondary_private_ip_address_count
        # The ID of the security group to which the ENI belongs.
        # 
        # Note:
        # 
        # - The valid values of N cannot exceed the maximum number of network interface controller (NIC) supported by the target instance type. For more information, see [instance family](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controller (NIC) supported by the target instance type.
        # 
        # - If NetworkInterface.N.InstanceType is specified as Primary, you must configure the Settings for this parameter. In this case, this parameter serves the same purpose as SecurityGroupId. Note that you cannot configure the Settings for SecurityGroupId, SecurityGroupIds.N, or NetworkInterface.N.SecurityGroupIds.N at the same time.
        # 
        # - If NetworkInterface.N.InstanceType is specified as Secondary or left empty, this parameter is optional. The default value is the security group to which the ECS instance belongs.
        self.security_group_id = security_group_id
        # The IDs of one or more security groups to which the ENI belongs.
        # 
        # - The valid values of N cannot exceed the maximum number of network interface controller (NIC) supported by the target instance type. For more information, see [instance family](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controller (NIC) supported by the target instance type.
        # - The second N specifies the IDs of one or more security groups. The valid values of N depend on the quota of security groups that the target instance can join. For more information, see [Security group limits](~~25412#SecurityGroupQuota1~~).
        # 
        # Note:
        # 
        # - If NetworkInterface.N.InstanceType is specified as Primary, you must configure the Settings for this parameter or NetworkInterface.N.SecurityGroupId. In this case, this parameter serves the same purpose as SecurityGroupIds.N. Note that you cannot configure the Settings for SecurityGroupId, SecurityGroupIds.N, or NetworkInterface.N.SecurityGroupId at the same time.
        # 
        # - If NetworkInterface.N.InstanceType is specified as Secondary or left empty, this parameter is optional. The default value is the security group to which the ECS instance belongs.
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
        # > This parameter is in invitational preview and is not available. If you want to use this parameter, [submit a ticket](https://selfservice.console.aliyun.com/ticket/createIndex) to apply for the whitelist.
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
        # When you use this parameter, take note of the following items:
        # 
        # - This parameter is applicable only to seventh-generation and later ECS instance types.
        # 
        # - This parameter is applicable only to Linux images.
        # 
        # - A larger outbound queue depth can improve outbound throughput and reduce the packet loss rate, but it consumes more memory.
        self.tx_queue_size = tx_queue_size
        # The ID of the vSwitch to which the ENI belongs.
        # 
        # Note:
        # 
        # - The valid values of N cannot exceed the maximum number of network interface controller (NIC) supported by the target instance type. For more information, see [instance family](https://help.aliyun.com/document_detail/25378.html) or invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) operation to query the maximum number of network interface controller (NIC) supported by the target instance type.  
        # - If NetworkInterface.N.InstanceType is specified as Primary, you must configure the Settings for this parameter. In this case, this parameter serves the same purpose as VSwitchId. Note that you cannot configure the Settings for both this parameter and VSwitchId at the same time.
        # 
        # - If NetworkInterface.N.InstanceType is specified as Secondary or left empty, this parameter is optional. The default value is the vSwitch to which the ECS instance belongs.
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
        # Specifies whether the instance that uses the image supports logons by using the ecs-user username. Valid values:
        # 
        # - true: Supports logons by using the ecs-user username.
        # 
        # - false: Does not support logons by using the ecs-user username.
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
        # The ID of the automatic snapshot policy that is applied to the data disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable the performance burst feature. Valid values:
        # 
        # - true: Enables the feature.
        # - false: Disables the feature.
        # 
        # > This parameter is supported only when DiskCategory is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The category of data disk N. Valid values:
        # 
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: ESSD.
        # - cloud: basic disk.
        # - cloud_auto: ESSD AutoPL disk.
        # - cloud_regional_disk_auto: regional ESSD.
        # - cloud_essd_entry: ESSD Entry disk.
        #   > This parameter supports cloud_essd_entry only when InstanceType is specified as an instance type in the ecs.u1 or ecs.e instance family.
        # - elastic_ephemeral_disk_standard: elastic ephemeral disk - Standard Edition.
        # - elastic_ephemeral_disk_premium: elastic ephemeral disk - Premium Edition.
        # 
        # For I/O optimized instances, the default Settings are cloud_efficiency. For non-I/O optimized instances, the default Settings are cloud.
        # Default value description:
        # 
        # - If InstanceType is configured as a retired and non-I/O optimized instance type, the default Settings are cloud.
        # - In other cases, the default Settings are cloud_efficiency. <props="china">After January 30, 2026, if the I/O optimized instance type does not support cloud_auto, the default Settings are cloud_efficiency. Otherwise, the default Settings are cloud_auto, and the performance burst feature is enabled by default. This feature incurs additional fees. For details, see [Billing examples](~~368372#p_75k_2hp_7gp~~). For more information, see [Announcement](https://www.aliyun.com/notice/117844).
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
        # > - This parameter is applicable only to full images. You can set this parameter to the mount point of the data disk in the full image and modify the DataDisk.N.Size and DataDisk.N.Category parameters to change the category and size of the data disk in the full image.
        # > - When you use a full image to create an instance, the data disks in the full image are created as the first n data disks of the ECS instance.
        self.device = device
        # The name of the data disk. The name must be 2 to 128 characters in length. It can contain characters that fall under the letter category in Unicode, such as letters, Chinese characters, and digits. It can also contain colons (:), underscores (_), periods (.), and hyphens (-).
        self.disk_name = disk_name
        # > This parameter is not available.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt data disk N. Valid values:
        # - true: Encrypts the data disk.
        # - false: Does not encrypt the data disk.
        # 
        # Default value: false.
        # 
        # 
        # >Notice: When you use a shared encrypted image to create a cloud disk based on an encrypted snapshot, you must specify the request parameter Encrypted=true for the cloud disk. This ensures that the created cloud disk uses the key of the user to whom the image is shared.
        self.encrypted = encrypted
        # The ID of the KMS key that is used to encrypt the data disk.
        # 
        # > If Encrypted is set to true and KMSKeyId is not specified, the default key is used for encryption, and the KMSKeyId value is returned after the instance is created.
        # > - - If the cloud disk is created from an unshared encrypted snapshot, the encryption key used by the snapshot is used by default.
        # > - - If the cloud disk is created from a shared encrypted snapshot, the service key is used by default.
        # > - - If the cloud disk is created in a region where account-level default encryption for block storage is enabled, the specified account-level key is used by default.
        # > - - In other cases, the service key is used by default.
        self.kmskey_id = kmskey_id
        # When you create an ESSD as a data disk, configure the Settings for the performance level of the disk. The value of N must be the same as the value of N in DataDisk.N.Category=cloud_essd. Valid values:
        # 
        # - PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # - PL1 (default): A single ESSD can deliver up to 50,000 random read/write IOPS.
        # - PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # - PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        # 
        # For more information about how to select the performance level of an ESSD, see [ESSD](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values: 0 to min{50,000, 1000 × Capacity - Baseline performance}.
        # 
        # Baseline performance = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # > This parameter is supported only when DiskCategory is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
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
        # > The value of this parameter must be greater than or equal to the size of the snapshot specified by the SnapshotId parameter.
        self.size = size
        # The ID of the snapshot that is used to create data disk N. Valid values of N: 1 to 16.
        # 
        # If you specify the DataDisk.N.SnapshotId parameter, the DataDisk.N.Size parameter is ignored. The size of the created cloud disk is the same as the size of the specified snapshot. You cannot use snapshots that were created on or before July 15, 2013. Otherwise, the request is rejected and an error is reported.
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
        # > This parameter is not available.
        self.assume_role_for = assume_role_for
        # > This parameter is not available.
        self.role_type = role_type
        # > This parameter is not available.
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
        # - cloud_essd: enterprise SSD.
        # - cloud: basic disk.
        # - cloud_auto: ESSD AutoPL disk.
        # - cloud_essd_entry: ESSD Entry disk.
        # 
        # Default value description:
        # 
        # - If InstanceType is a retired and non-I/O optimization instance type, the default value is `cloud`.
        # - In other cases, the default value is `cloud_efficiency`.<props="china">After January 30, 2026, for instance types that only support `cloud_essd`, the default value will be changed from `cloud_efficiency` to `cloud_essd` PL0. For more details, see [Announcement](https://www.aliyun.com/notice/117844).
        # 
        # >The value of this parameter can be `cloud_essd_entry` only when the value of `InstanceType` is [u1, universal instance family](https://help.aliyun.com/document_detail/457079.html) (`ecs.u1`) or [e, economy instance family](https://help.aliyun.com/document_detail/108489.html) (`ecs.e`).
        self.category = category
        # The system disk description. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The system disk name. The name must be 2 to 128 characters in length. It can contain letters and digits in Unicode, and can include colons (:), underscores (_), periods (.), and hyphens (-).
        self.disk_name = disk_name
        # When creating an enterprise SSD as the system disk, Settings the performance level of the disk. Valid values:
        # 
        # - PL0: A single disk can deliver up to 10,000 random read/write IOPS.
        # - PL1 (default): A single disk can deliver up to 50,000 random read/write IOPS.
        # - PL2: A single disk can deliver up to 100,000 random read/write IOPS.
        # - PL3: A single disk can deliver up to 1,000,000 random read/write IOPS.
        # 
        # For more information about how to select an enterprise SSD performance level, see [enterprise SSDs](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The system disk size. Unit: GiB. Valid values:
        # 
        # - Basic disk: 20 to 500.
        # - enterprise SSD:
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
        # > This parameter is supported only when SystemDisk.Category is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # > This parameter is not available.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt the system disk. Valid values:
        # 
        # - true: Encrypts the system disk.
        # 
        # - false: Does not encrypt the system disk.
        # 
        # Default value: false.
        # 
        # > You cannot encrypt the system disk when you create an instance in Hong Kong (China) Zone D or Singapore Zone A.
        # 
        # >Notice: When you use a shared encrypted image to create a cloud disk based on an encrypted snapshot, you must specify the request parameter Encrypted=true for the cloud disk. This ensures that the created cloud disk uses the key of the user to whom the image is shared.
        self.encrypted = encrypted
        # The ID of the KMS key that is used to encrypt the system disk.
        # 
        # > If Encrypted is set to true and KMSKeyId is not specified, the default key is used for encryption, and the KMSKeyId value is returned after the instance is created.
        # > - - If the cloud disk is created from an unshared encrypted snapshot, the encryption key used by the snapshot is used by default.
        # > - - If the cloud disk is created from a shared encrypted snapshot, the service key is used by default.
        # > - - If the cloud disk is created in a region where account-level default encryption for block storage is enabled, the specified account-level key is used by default.
        # > - - In other cases, the service key is used by default.
        self.kmskey_id = kmskey_id
        # The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values: 0 to min{50,000, 1000 × Capacity - Baseline performance}.
        # 
        # Baseline performance = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # > This parameter is supported only when SystemDisk.Category is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
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
        # When this parameter is set to Enclave, the ECS instance uses Enclave to build a confidential computing environment. Currently, only the c7, g7, and r7 instance families support specifying this parameter when you call RunInstances to use Enclave confidential computing. Note the following:
        # 
        # - The confidential computing feature is in invitational preview.
        # 
        # - To create an ECS instance with Enclave confidential computing by calling API operations, you can only call RunInstances. CreateInstance does not support the SecurityOptions.ConfidentialComputingMode parameter.
        # 
        # - Enclave confidential computing relies on the trusted system (vTPM). When you specify that an ECS instance uses Enclave to build a confidential computing environment, the trusted system is also enabled for the instance. Therefore, when you call this operation, if you set SecurityOptions.ConfidentialComputingMode=Enclave, the created ECS instance will have both the Enclave confidential computing mode and the trusted system enabled, regardless of whether you set SecurityOptions.TrustedSystemMode=vTPM.
        # 
        # For more information about confidential computing, see [Use Enclave to build a confidential computing environment](https://help.aliyun.com/document_detail/203433.html).
        self.confidential_computing_mode = confidential_computing_mode
        # The trusted system mode. Valid value: vTPM.
        # 
        # Currently, the trusted system mode supports the following instance families:
        # - g7, c7, and r7.
        # - Security-enhanced instance families (g7t, c7t, and r7t).
        # 
        # When you create an ECS instance of the preceding instance families, you must configure this parameter. Details:
        # 
        # - If you use the Alibaba Cloud trusted system, set this parameter to vTPM. This allows the instance to complete trusted verification through the Alibaba Cloud trusted system during startup.
        # - If you do not use the Alibaba Cloud trusted system, you can leave this parameter unspecified. However, note that if the ECS instance you create uses the Enclave confidential computing mode (SecurityOptions.ConfidentialComputingMode=Enclave), the trusted system is also enabled for the instance.
        # - To create a trusted ECS instance by calling API operations, you can only call RunInstances. CreateInstance does not support the SecurityOptions.TrustedSystemMode parameter.
        # > If you specify an instance as a trusted instance when you create it, you can only use images that support the trusted system when you replace the system disk.
        # 
        # For more information about the trusted system, see [Overview of the trusted feature for security-enhanced instances](https://help.aliyun.com/document_detail/201394.html).
        self.trusted_system_mode = trusted_system_mode
        # Specifies whether to enable UEFI Secure Boot. Valid values:
        # - true: Enabled.
        # - false: Disabled.
        # 
        # Default value: false.
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
        # When you specify both a dedicated host (DedicatedHostId) and a dedicated host cluster (SchedulerOptions.DedicatedHostClusterId):
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
        # The ID of the private pool, which is the ID of the elasticity assurance or capacity reservation.
        self.id = id
        # The private pool matching criteria for instance startup. After an elasticity assurance or capacity reservation takes effect, a private pool is generated for you to select when you start an instance. Valid values:
        # 
        # - Open: open mode. The system automatically matches an open private pool. If no eligible private pool is available, the instance uses public pool resources to start. In this mode, you do not need to specify the PrivatePoolOptions.Id parameter.
        # - Target: specified mode. The instance uses the specified private pool to start. If the specified private pool is unavailable, the instance fails to start. In this mode, you must specify the private pool ID, which means the PrivatePoolOptions.Id parameter is required.
        # - None: no private pool mode. The instance does not use a private pool to start.
        # 
        # Default value: None.
        # 
        # In any of the following scenarios, the private pool matching criteria for instance startup can only be set to None or left unspecified:
        # - Creating a spot instance.
        # - Creating an ECS instance on a dedicated host.
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
        # >This parameter is in invitational preview and is not available for public use.
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
        # <props="china">Default value: see [Custom CPU options](https://help.aliyun.com/document_detail/145895.html).
        self.core = core
        # **[Deprecated]** This parameter is deprecated.
        self.numa = numa
        # The number of threads per core. The number of vCPUs of the ECS instance = the value of CpuOptions.Core × the value of CpuOptions.ThreadsPerCore.
        # 
        # - CpuOptions.ThreadsPerCore=1 indicates that CPU hyper-threading is disabled.
        # 
        # - Only specific instance types support configuring the number of CPU threads.
        # 
        # <props="china">Valid values and default value: see [Custom CPU options](https://help.aliyun.com/document_detail/145895.html).
        self.threads_per_core = threads_per_core
        # The CPU topology type of the instance. Valid values:
        # 
        # - ContinuousCoreToHTMapping: When this value is selected, the hyper-threads of the same core in the CPU topology of the instance are continuous.
        # - DiscreteCoreToHTMapping: When this value is selected, the hyper-threads of the same core in the instance are discrete.
        # 
        # Default value: none.
        # 
        # > Only specific instance families support this parameter. For more information about the supported instance families, see [View and modify the CPU topology](https://help.aliyun.com/document_detail/2636059.html).
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

