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
        # Specifies whether the instance on a dedicated host is associated with the dedicated host. Valid values:
        self.affinity = affinity
        # The number of ECS instances to create. Valid values: 1 to 100.
        # 
        # The number of ECS instances that are created depends on the values of Amount and MinAmount:
        # 
        # - If MinAmount is not specified: instances are created based on the Amount value. If the inventory is insufficient, the API returns a failure and no instances are created.
        # 
        # - If MinAmount is specified:
        #   - If the available inventory < MinAmount: no ECS instances are created, and the API returns a failure.
        #   - If MinAmount ≤ available inventory < Amount: instances are created based on the available inventory, and the API returns a success.
        #   - If the available inventory ≥ Amount: instances are created based on the specified Amount value, and the API returns a success.
        # 
        # Default value: 1.
        self.amount = amount
        # >This parameter is not publicly available.
        self.arn = arn
        # Specifies whether to automatically complete the payment when you create the instance. Valid values:
        # 
        # - true: The payment is automatically completed.
        # 
        #     > If the balance of your payment method is insufficient, an abnormal order is generated and can only be canceled. If the balance of your payment method is insufficient, set AutoPay to `false`. In this case, an unpaid order is generated. You can then log on to the ECS console to complete the payment.
        # 
        # - false: An order is generated but the payment is not completed.
        # 
        #     > When `InstanceChargeType` is set to `PostPaid`, `AutoPay` cannot be set to `false`.
        # 
        # Default value: true.
        self.auto_pay = auto_pay
        # The automatic release time of the pay-as-you-go instance. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the UTC+0 time zone. The format is `yyyy-MM-ddTHH:mm:ssZ`.
        # 
        # - If the value of seconds (`ss`) is not `00`, the start time of the current minute (`mm`) is used.
        # 
        # - The earliest release time is half an hour after the current time.
        # 
        # - The latest release time cannot be more than three years from the current time.
        self.auto_release_time = auto_release_time
        # Specifies whether to enable auto-renewal. This parameter takes effect only when InstanceChargeType is set to PrePaid. Valid values:
        # 
        # - true: Auto-renewal is enabled.
        # - false: Auto-renewal is not enabled.
        # 
        # Default value: false.
        self.auto_renew = auto_renew
        # The auto-renewal period. Valid values:
        # 
        # <props="china">
        # - PeriodUnit=Week: 1, 2, and 3.
        # - PeriodUnit=Month: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # 
        # 
        # <props="intl">PeriodUnit=Month: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The clock-related property parameters of the instance.
        self.clock_options = clock_options
        # The running mode of the burstable instance. Valid values:
        self.credit_specification = credit_specification
        # The list of data disk information.
        self.data_disk = data_disk
        # The ID of the dedicated host.
        # <props="china">You can call [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/134242.html) to query the list of dedicated host IDs.
        # 
        # <props="intl">You can call [DescribeDedicatedHosts](https://help.aliyun.com/document_detail/134242.html) to query the list of dedicated host IDs.
        # 
        # >Notice: Dedicated hosts do not support spot instances. If you specify the DedicatedHostId parameter, the SpotStrategy and SpotPriceLimit settings in the request are automatically ignored.
        self.dedicated_host_id = dedicated_host_id
        # The release protection property of the instance. Specifies whether the instance can be released from the console or by calling the [DeleteInstance](https://help.aliyun.com/document_detail/25507.html) operation. Valid values:
        # 
        # -  true: Enables release protection for the instance.
        # -  false: Disables release protection for the instance.
        # 
        # Default value: false.
        # 
        # > This property applies only to pay-as-you-go instances and only restricts manual release operations. It does not take effect on system-initiated release operations.
        self.deletion_protection = deletion_protection
        # The group number of the instance in the deployment set. If the deployment set uses the high availability group strategy (AvailabilityGroup), you can use this parameter to specify the group number. Valid values: 1 to 7.
        self.deployment_set_group_no = deployment_set_group_no
        # The ID of the deployment set.
        self.deployment_set_id = deployment_set_id
        # The description of the instance. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to perform only a dry run. Valid values:
        self.dry_run = dry_run
        # The hostname of the instance. The following limits apply:
        self.host_name = host_name
        # Specifies a different hostname for each instance when you create multiple instances.
        self.host_names = host_names
        # The ID of the HPC cluster to which the instance belongs.
        self.hpc_cluster_id = hpc_cluster_id
        # Specifies whether to enable the access channel for instance metadata. Valid values:
        self.http_endpoint = http_endpoint
        # >This parameter is not publicly available.
        self.http_put_response_hop_limit = http_put_response_hop_limit
        # Specifies whether to forcefully use the China Reinforced Mode (IMDSv2) for accessing instance metadata. Valid values:
        # - optional: does not forcefully use the China Reinforced Mode.
        # - required: forcefully uses the China Reinforced Mode. After this value is set, the normal mode cannot be used to access instance metadata.
        # 
        # Default value: optional.
        # >For more information about the modes for accessing instance metadata, see [Instance metadata access mode](https://help.aliyun.com/document_detail/150575.html).
        self.http_tokens = http_tokens
        # The name of the image family. You can set this parameter to obtain the latest available image from the specified image family to create the instance.
        # 
        # The name must be 2 to 128 characters in length. The name cannot start with a special character, a digit, http://, or https://. The name can contain only the following special characters: periods (.), underscores (_), hyphens (-), and colons (:).
        # 
        # Take note of the following items:
        # 
        # - If you set the ImageId parameter, you cannot set this parameter.
        # - If you do not set the ImageId parameter but the launch template specified by LaunchTemplateId or LaunchTemplateName has ImageId configured, you cannot set this parameter.
        # - If you do not set ImageId and the launch template specified by LaunchTemplateId or LaunchTemplateName does not have ImageId configured, you can set this parameter.
        # - If you do not set ImageId and do not set LaunchTemplateId or LaunchTemplateName, you can set this parameter.
        # > For information about image families associated with Alibaba Cloud public images, see [Public image overview](https://help.aliyun.com/document_detail/108393.html).
        self.image_family = image_family
        # The image ID. Specifies the image resource used to start the instance. You can call [DescribeImages](https://help.aliyun.com/document_detail/25534.html) to query available image resources. If you do not specify `LaunchTemplateId` or `LaunchTemplateName` to determine a launch template, and do not specify `ImageFamily` to use the latest available image from an image family, `ImageId` is required.
        self.image_id = image_id
        # The image-related property information.
        self.image_options = image_options
        # The billing method of the instance. Valid values:
        # 
        # -  PrePaid: subscription.
        # -  PostPaid: pay-as-you-go.
        # 
        # Default value: PostPaid.
        # 
        # <props="china">If you set this parameter to PrePaid, make sure that your account supports balance payment or credit payment. Otherwise, the `InvalidPayMethod` error is returned.
        # 
        # <props="intl">If you set this parameter to PrePaid, make sure that your account supports credit payment. Otherwise, the `InvalidPayMethod` error is returned.
        self.instance_charge_type = instance_charge_type
        # The instance name. The name must be 2 to 128 characters in length and can contain characters from the Unicode letter category (including English and Chinese characters) and digits. The name can contain colons (:), underscores (_), periods (.), or hyphens (-). Default value: the `InstanceId` of the instance.
        self.instance_name = instance_name
        # The instance type of the instance. If you do not specify `LaunchTemplateId` or `LaunchTemplateName` to determine the launch template, `InstanceType` is required.
        # 
        # - Instance type selection: See [Instance families](https://help.aliyun.com/document_detail/25378.html) or call [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) to query the performance data of the target instance type, or see [Best practices for instance type selection](https://help.aliyun.com/document_detail/58291.html) to learn how to select an instance type.
        # - Inventory query: Call [DescribeAvailableResource](https://help.aliyun.com/document_detail/66186.html) to query the resource availability in a specific region or zone.
        self.instance_type = instance_type
        # The billing method for network usage. Valid values:
        # 
        # - PayByBandwidth: pay-by-bandwidth.
        # - PayByTraffic: pay-by-traffic.
        # 
        # Default value: PayByTraffic.
        # 
        # > In **pay-by-traffic** mode, the peak inbound and outbound bandwidths are both upper limits and are not guaranteed. When resource contention occurs, the peak bandwidth may be throttled. If your business requires guaranteed bandwidth, use the **pay-by-bandwidth** mode.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth, in Mbit/s. Valid values:
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth, in Mbit/s. Valid values: 0 to 100.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether the instance is I/O optimization enabled. The default value for [retired instance types](https://help.aliyun.com/document_detail/55263.html) is none. The default value for other instance types is optimized. Valid values:
        self.io_optimized = io_optimized
        # Specifies one or more IPv6 addresses for the primary ENI. You can specify up to 10 IPv6 addresses. Valid values of N: 1 to 10.
        # 
        # Example: `Ipv6Address.1=2001:db8:1234:1a00::***`.
        # 
        # Take note of the following items:
        # 
        # - If you set `Ipv6Address.N`, you must set `Amount` to 1 and cannot set `Ipv6AddressCount`.
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Primary`, you cannot set `Ipv6Addresses.N` or `Ipv6AddressCount`. Instead, set `NetworkInterface.N.Ipv6Addresses.N` or `NetworkInterface.N.Ipv6AddressCount`.
        self.ipv_6address = ipv_6address
        # The number of randomly generated IPv6 addresses for the primary ENI. Valid values: 1 to 10.
        self.ipv_6address_count = ipv_6address_count
        # >This parameter is in invitational preview and is not publicly available.
        self.isp = isp
        # The name of the key pair.
        self.key_pair_name = key_pair_name
        # The launch template ID. For more information, call [DescribeLaunchTemplates](https://help.aliyun.com/document_detail/73759.html).
        self.launch_template_id = launch_template_id
        # The launch template name.
        self.launch_template_name = launch_template_name
        # The launch template version. If you specify `LaunchTemplateId` or `LaunchTemplateName` but do not specify the launch template version, the default version is used.
        self.launch_template_version = launch_template_version
        # The minimum Quantity of ECS instances to purchase. Valid values: 1 to 100.
        self.min_amount = min_amount
        # The network interface controller (NIC) information.
        self.network_interface = network_interface
        # The number of queues supported by the primary ENI. Take note of the following items:
        # 
        # - The value cannot exceed the maximum number of queues per ENI allowed by the instance type.
        # 
        # - The total number of queues for all ENIs on the instance cannot exceed the queue quota allowed by the instance type. You can call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query the MaximumQueueNumberPerEni and TotalEniQueueQuantity fields to obtain the maximum number of queues per ENI and the total queue quota for an instance type.
        # 
        # - If NetworkInterface.N.InstanceType is set to Primary, you cannot set NetworkInterfaceQueueNumber. Set NetworkInterface.N.QueueNumber instead.
        self.network_interface_queue_number = network_interface_queue_number
        # The network-related property parameters.
        self.network_options = network_options
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password of the instance. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported:
        self.password = password
        # Specifies whether to use the password preset in the image. Valid values:
        self.password_inherit = password_inherit
        # The duration of the subscription. Unit: specified by `PeriodUnit`. This parameter is required and takes effect only when `InstanceChargeType` is set to `PrePaid`. If `DedicatedHostId` is specified, the value of this parameter cannot exceed the subscription duration of the dedicated host. Valid values:
        # 
        # <props="china">
        # - PeriodUnit=Week: 1, 2, 3, and 4.
        # - PeriodUnit=Month: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        # 
        # 
        # 
        # <props="intl">PeriodUnit=Month: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        self.period = period
        # The unit of the subscription billable methods duration. Valid values:
        self.period_unit = period_unit
        # The private DNS name configuration of the instance.
        self.private_dns_name_options = private_dns_name_options
        # The private IP address of the instance. When you specify a private IP address for a VPC-connected ECS instance, the IP address must be an available address within the CIDR block of the vSwitch specified by `VSwitchId`.
        # 
        # Take note of the following items:
        # 
        # - After you set `PrivateIpAddress`:
        #     - If `Amount` is set to 1, the specified private IP address is assigned to the created ECS instance.
        #     - If `Amount` is set to a value greater than 1, the specified private IP address is used as the start address to sequentially assign consecutive private IP addresses to multiple ECS instances during batch creation. In this case, you cannot attach secondary ENIs to the instances (that is, you cannot set `NetworkInterface.N.*` parameters).
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Primary`, you cannot set `PrivateIpAddress`. Set `NetworkInterface.N.PrimaryIpAddress` instead.
        # 
        # >The first and last three IP addresses of each vSwitch CIDR block are reserved by the system and cannot be specified.
        # For example, if the CIDR block of a vSwitch is 192.168.1.0/24, the IP addresses 192.168.1.0, 192.168.1.253, 192.168.1.254, and 192.168.1.255 are reserved by the system.
        self.private_ip_address = private_ip_address
        # The name of the instance RAM role. You can call the RAM API [ListRoles](https://help.aliyun.com/document_detail/28713.html) to query the instance RAM roles that you have created.
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
        self.security_enhancement_strategy = security_enhancement_strategy
        # The ID of the security group to which the new instance belongs. Instances within the same security group can communicate with each other. The maximum number of instances that a security group can contain varies based on the security group type. For more information, see the security group section in [Limits](~~25412#SecurityGroupQuota~~).
        # 
        # > `SecurityGroupId` determines the network type of the instance. For example, if the specified security group is of the Virtual Private Cloud (VPC) type, the instance is a VPC-type instance, and you must also specify the `VSwitchId` parameter.
        # 
        # If you do not set `LaunchTemplateId` or `LaunchTemplateName` to specify a launch template, the security group ID is required. Note the following items:
        # 
        # - You can set one security group by using `SecurityGroupId`, or set one or more security groups by using `SecurityGroupIds.N`. However, you cannot specify both `SecurityGroupId` and `SecurityGroupIds.N` at the same time.
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Primary`, you cannot set `SecurityGroupId` or `SecurityGroupIds.N`. In this case, you can only set `NetworkInterface.N.SecurityGroupId` or `NetworkInterface.N.SecurityGroupIds.N`.
        self.security_group_id = security_group_id
        # Adds the instance to multiple security groups. The valid values of N depend on the maximum number of security groups to which an instance can belong. For more information, see [Security group limits](https://help.aliyun.com/document_detail/101348.html).
        self.security_group_ids = security_group_ids
        # The protection period of the spot instance. Unit: hours. Valid values:
        # - 1: After the instance is created, Alibaba Cloud guarantees that the instance runs for 1 hour without being automatically released. After 1 hour, the system compares the bid price with the market price and checks resource inventory to determine whether to retain or reclaim the instance.
        # - 0: After the instance is created, Alibaba Cloud does not guarantee the instance running duration. The system compares the bid price with the market price and checks resource inventory to determine whether to retain or reclaim the instance.
        # 
        # Default value: 1.
        # > 
        # > - This parameter supports only the value 0 or 1.
        # > - Spot instances are billed by second. Set an appropriate protection period based on the expected task execution duration.
        # > - Alibaba Cloud sends a notification to you through an ECS system event 5 minutes before the instance is reclaimed.
        self.spot_duration = spot_duration
        # The interruption pattern of the spot instance. Valid values:
        self.spot_interruption_behavior = spot_interruption_behavior
        # The maximum hourly price of the instance. A maximum of three decimal places is supported. This parameter takes effect when the `SpotStrategy` parameter is set to `SpotWithPriceLimit`.
        self.spot_price_limit = spot_price_limit
        # The bidding policy for the pay-as-you-go instance. This parameter takes effect when the `InstanceChargeType` parameter is set to `PostPaid`. Valid values:
        self.spot_strategy = spot_strategy
        # The storage set ID.
        self.storage_set_id = storage_set_id
        # The maximum number of partitions in the storage set. Valid values: greater than or equal to 1.
        self.storage_set_partition_number = storage_set_partition_number
        # The tag information for the instance, disks, and primary ENI.
        self.tag = tag
        # Specifies whether to create the instance on a dedicated host. Valid values:
        self.tenancy = tenancy
        # Specifies whether to automatically append sequential suffixes to `HostName` and `InstanceName` when you create multiple instances. Sequential suffixes start from 001 and can be up to 999. Valid values:
        # - true: Appends sequential suffixes.
        # - false: Does not append sequential suffixes.
        # 
        # Default value: false.
        # 
        # If `HostName` or `InstanceName` is configured in a specified sorting format without the naming suffix `name_suffix`, that is, the naming format is `name_prefix[begin_number,bits]`, `UniqueSuffix` does not take effect, and names are sorted only in the specified order.
        # 
        # For more information, see [Batch configure sequential instance names or hostnames](https://help.aliyun.com/document_detail/196048.html).
        self.unique_suffix = unique_suffix
        # The instance user data. The data must be Base64-encoded. The maximum size of the raw data before Base64 encoding is 32 KB.
        self.user_data = user_data
        # The vSwitch ID. If you are creating a VPC-type ECS instance, you must specify a vSwitch ID. The security group and the vSwitch must belong to the same VPC. You can call [DescribeVSwitches](https://help.aliyun.com/document_detail/35748.html) to query created vSwitches.
        self.v_switch_id = v_switch_id
        # The zone ID of the instance. You can call [DescribeZones](https://help.aliyun.com/document_detail/25610.html) to query the zone list.
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
        # The tag key for the instance, disks, and primary ENI. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with aliyun or acs:. The tag key cannot contain http:// or https://.
        self.key = key
        # The tag value for the instance, disks, and primary ENI. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain http:// or https://.
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
        # Specifies whether to enable DNS AAAA record resolution from the instance ID-based domain name to IPv6. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        # 
        # Default value: false.
        self.enable_instance_id_dns_aaaarecord = enable_instance_id_dns_aaaarecord
        # Specifies whether to enable DNS resolution from the instance ID-based domain name to the IPv4 address. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        # 
        # Default value: false.
        self.enable_instance_id_dns_arecord = enable_instance_id_dns_arecord
        # Specifies whether to enable DNS resolution from IP-based domain names to IPv4 addresses. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        # 
        # Default value: false.
        self.enable_ip_dns_arecord = enable_ip_dns_arecord
        # Specifies whether to enable reverse DNS resolution from IPv4 addresses to IP-type domain names. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        # 
        # Default value: false.
        self.enable_ip_dns_ptr_record = enable_ip_dns_ptr_record
        # The hostname type. Valid values:
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
        # The bandwidth weight value of the instance. The valid values vary by instance type. To query the supported bandwidth weight levels for a specific instance type, call DescribeInstanceTypes. The BandwidthWeighting field in the response indicates the supported bandwidth weight levels. You can use the name field in the returned values as the dictionary value, such as Vpc-L1 or Ebs-L1.
        self.bandwidth_weighting = bandwidth_weighting
        # Specifies whether to enable the Jumbo Frame feature for the instance. Valid values:
        # 
        # - false: does not enable Jumbo Frame. The MTU of all NICs (including the primary ENI and secondary ENIs) on the instance is set to 1500.
        # 
        # - true: enables Jumbo Frame. The MTU of all NICs (including the primary ENI and secondary ENIs) on the instance is set to 8500.
        # 
        # Default value: true.
        # 
        # >Only some instance types of the eighth generation or later support the Jumbo Frame feature. For more information, see [ECS instance MTU](https://help.aliyun.com/document_detail/200512.html).
        self.enable_jumbo_frame = enable_jumbo_frame
        # > This parameter is in invitational preview and is not publicly available.
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
        # Specifies whether to retain the network interface when the instance is released. Valid values:
        # 
        # - true: The network interface is not retained.
        # 
        # - false: The network interface is retained.
        # 
        # Default value: true.
        # 
        # >This parameter takes effect only on secondary ENIs.
        self.delete_on_release = delete_on_release
        # The description of the network interface controller (NIC).
        self.description = description
        # The type of the network interface controller (NIC). The valid values of N cannot exceed the number of network interface controllers (NICs) supported by the instance family. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html) or invoke [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) to query the number of network interface controllers (NICs) supported by the target instance type.
        self.instance_type = instance_type
        # Specifies one or more IPv6 addresses for the primary ENI. You can specify up to 10 IPv6 addresses. Valid values of the second N: 1 to 10.
        # 
        # Example: `Ipv6Address.1=2001:db8:1234:1a00::***`
        # 
        # Take note of the following items:
        # 
        # - This parameter takes effect only when `NetworkInterface.N.InstanceType` is set to `Primary`. If `NetworkInterface.N.InstanceType` is set to `Secondary` or left empty, this parameter cannot be specified.
        # 
        # - If you specify this parameter, `Amount` can only be set to 1, and you cannot specify `Ipv6AddressCount`, `Ipv6Address.N`, or `NetworkInterface.N.Ipv6AddressCount`.
        self.ipv_6address = ipv_6address
        # The number of randomly generated IPv6 addresses for the primary ENI. Valid values: 1 to 10.
        self.ipv_6address_count = ipv_6address_count
        # The index of the physical network card specified for the ENI.
        self.network_card_index = network_card_index
        # The ID of the Elastic Network Interface (ENI) to attach to the instance.
        # 
        # If you set this parameter, the value of `Amount` can only be 1.
        # 
        # >This parameter takes effect only for secondary ENIs. After you specify an existing secondary ENI, you cannot configure other ENI creation parameters.
        self.network_interface_id = network_interface_id
        # The name of the network interface controller (NIC). The name must be 2 to 128 characters in length and can contain letters, digits, and characters that are supported by Unicode in the letter categorization. The name can contain colons (:), underscores (_), periods (.), or hyphens (-).
        self.network_interface_name = network_interface_name
        # The communication mode of the ENI. Valid values:
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # Adds a network interface controller (NIC) and sets the primary IP address.
        self.primary_ip_address = primary_ip_address
        # The number of queues supported by the ENI.
        # 
        # Take note of the following items:
        # 
        # - The value of N cannot exceed the maximum number of ENIs supported by the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html) or call [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) to query the maximum number of ENIs supported by the target instance type.
        # 
        # - The value cannot exceed the maximum number of queues per ENI allowed by the instance type.
        # 
        # - The total number of queues across all ENIs on the instance cannot exceed the total queue quota allowed by the instance type. You can call [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) to query the MaximumQueueNumberPerEni and TotalEniQueueQuantity fields for the maximum number of queues per ENI and the total queue quota of the instance type.
        # 
        # - If NetworkInterface.N.InstanceType is set to Primary and this parameter is specified, you cannot specify the NetworkInterfaceQueueNumber parameter.
        self.queue_number = queue_number
        # The number of queue pairs for the RDMA network interface.
        # 
        # If you want to attach multiple RDMA network interfaces to the instance being created, we recommend that you manually specify QueuePairNumber for each network interface based on the upper limit of `QueuePairNumber` supported by the instance type and the number of network interfaces you plan to use. Ensure that the total QueuePairNumber across all network interfaces does not exceed the maximum value allowed by the instance type. Call [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) to query the upper limits of the instance type.
        # 
        # >Notice: If QueuePairNumber is not specified for an RDMA network interface, the upper limit of QueuePairNumber for all RDMA network interfaces supported by the instance type is used by default. Therefore, once an RDMA network interface without QueuePairNumber specified is attached, no more RDMA network interfaces can be added (regular network interfaces are not affected by this restriction).</notice>
        self.queue_pair_number = queue_pair_number
        # The inbound queue depth of the network interface controller (NIC).
        self.rx_queue_size = rx_queue_size
        # The number of secondary private IPv4 addresses to assign to the network interface. Valid values: 1 to 49.
        # 
        # - The value cannot exceed the maximum number of IP addresses allowed for the instance type. For more information, see [Instance families](~~~25378~~).
        # - NetworkInterface.N.SecondaryPrivateIpAddressCount specifies the number of secondary private IPv4 addresses to assign to the network interface (excluding the primary private IP address of the network interface). The system randomly assigns IP addresses from the available CIDR block of the vSwitch (NetworkInterface.N.VSwitchId) to which the network interface belongs.
        self.secondary_private_ip_address_count = secondary_private_ip_address_count
        # The ID of the security group to which the network interface controller (NIC) belongs.
        self.security_group_id = security_group_id
        # One or more security group IDs to which the ENI belongs.
        # 
        # - The valid values of N for the first dimension do not exceed the number of ENIs supported by the instance type. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html) or call [DescribeInstanceTypes](https://help.aliyun.com/document_detail/2679699.html) to query the number of ENIs supported by the target instance type.
        # - The second N indicates that you can specify one or more security group IDs. The valid values of N are related to the quota for the number of security groups to which an instance can belong. For more information, see [Security group limits](~~25412#SecurityGroupQuota1~~).
        # 
        # Take note of the following items:
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Primary`, you must specify this parameter or `NetworkInterface.N.SecurityGroupId`. In this case, this parameter has the same effect as `SecurityGroupIds.N`, but you cannot specify `SecurityGroupId`, `SecurityGroupIds.N`, or `NetworkInterface.N.SecurityGroupId` at the same time.
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Secondary` or left empty, this parameter is optional. Default value: the security group to which the ECS instance belongs.
        self.security_group_ids = security_group_ids
        # Specifies whether to enable source/destination checking. We recommend that you enable this feature to improve network security. Valid values:
        # 
        # - true: enabled.
        # 
        # - false: disabled.
        # 
        # Default value: false.
        # 
        # > Only some regions support this feature. Before you use this feature, read [Source/destination checking](https://help.aliyun.com/document_detail/2863210.html).
        self.source_dest_check = source_dest_check
        # The outbound queue depth of the network interface controller (NIC).
        self.tx_queue_size = tx_queue_size
        # The ID of the vSwitch to which the network interface controller (NIC) belongs.
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
        # Indicates whether instances that use this image support logon as the ecs-user user. Valid values:
        # 
        # - true: supported.
        # 
        # - false: not supported.
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
        # The ID of the automatic snapshot policy to apply to the data disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable the performance burst feature. Valid values:
        self.bursting_enabled = bursting_enabled
        # The category of data disk N. Valid values:
        # 
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: enterprise SSD.
        # - cloud: basic disk.
        # - cloud_auto: ESSD AutoPL disk.
        # - cloud_regional_disk_auto: regional Enterprise SSD (ESSD).
        # - cloud_essd_entry: ESSD Entry disk.
        #   >cloud_essd_entry is supported only when `InstanceType` is set to an instance type in the `ecs.u1` or `ecs.e` instance family.
        # - elastic_ephemeral_disk_standard: elastic ephemeral disk - Standard Edition.
        # - elastic_ephemeral_disk_premium: elastic ephemeral disk - Premium Edition.
        # 
        # For I/O optimized instances, the default value is cloud_efficiency. For non-I/O optimized instances, the default value is cloud.
        # Notes on default values:
        # 
        # - If InstanceType is set to a retired instance type that is not I/O optimized, the default value is `cloud`.
        # - In other cases, the default value is `cloud_efficiency`.<props="china">After January 30, 2026, if the I/O optimized instance type does not support cloud_auto, the default value is cloud_efficiency. Otherwise, the default value is cloud_auto, and performance burst is enabled by default (which incurs additional fees. For more information, see [Billing examples](~~368372#p_75k_2hp_7gp~~)). For more information, see [Change notice](https://www.aliyun.com/notice/117844).
        self.category = category
        # Specifies whether to release the data disk when the instance is released. Valid values:
        self.delete_with_instance = delete_with_instance
        # The description of the data disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The mount point of the data disk. The naming conventions for mount points vary based on the number of data disks attached:
        self.device = device
        # The name of the data disk. The name must be 2 to 128 characters in length and can contain letters, digits, and characters that are supported by Unicode in the letter category. The name can contain colons (:), underscores (_), periods (.), or hyphens (-).
        self.disk_name = disk_name
        # >This parameter is not publicly available.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt data disk N. Valid values:
        self.encrypted = encrypted
        # The ID of the KMS key for the data disk.
        # 
        # > If Encrypted is set to true and KMSKeyId is not specified, the default key is used for encryption, and the KMSKeyId value is returned after the instance is created.
        # > - - The disk is created from a non-shared encrypted snapshot: The encryption key used by the snapshot is used by default.
        # > - - The disk is created from a shared encrypted snapshot: The service key is used by default.
        # > - - The disk is created in a region where block storage account-level default encryption is enabled: The specified account-level key is used by default.
        # > - - Other cases: The service key is used by default.
        self.kmskey_id = kmskey_id
        # The performance level of the data disk when you create an enterprise SSD as a data disk. The value of N must be the same as the N in `DataDisk.N.Category=cloud_essd`. Valid values:
        # 
        # - PL0: A single disk can deliver up to 10,000 random read/write IOPS.
        # - PL1 (default): A single disk can deliver up to 50,000 random read/write IOPS.
        # - PL2: A single disk can deliver up to 100,000 random read/write IOPS.
        # - PL3: A single disk can deliver up to 1,000,000 random read/write IOPS.
        # 
        # For more information about how to select an ESSD performance level, see [ESSD](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values: 0 to min{50,000, 1000 × Capacity - baseline performance}.
        self.provisioned_iops = provisioned_iops
        # The size of data disk N. Valid values of N: 1 to 16. Unit: GiB. Valid values:
        # 
        # - cloud_efficiency: 20 to 32768.
        # - cloud_ssd: 20 to 32768.
        # - cloud_essd: The valid values depend on the value of `DataDisk.N.PerformanceLevel`. 
        #     - PL0: 1 to 65,536.
        #     - PL1: 20 to 65,536.
        #     - PL2: 461 to 65,536.
        #     - PL3: 1261 to 65,536.
        # - cloud: 5 to 2000.
        # - cloud_auto: 1 to 65,536.
        # - cloud_essd_entry: 10 to 32768.
        # 
        # >The value of this parameter must be greater than or equal to the size of the snapshot specified by `SnapshotId`.
        self.size = size
        # The ID of the snapshot to use to create data disk N. Valid values of N: 1 to 16.
        self.snapshot_id = snapshot_id
        # The ID of the dedicated block storage cluster. If you want to use a disk in a dedicated block storage cluster as the data disk when you create an ECS instance, specify this parameter.
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
        # >This parameter is not publicly available.
        self.assume_role_for = assume_role_for
        # >This parameter is not publicly available.
        self.role_type = role_type
        # >This parameter is not publicly available.
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
        # The category of the system disk. Valid values:
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
        # - If InstanceType is set to a retired instance type that is not I/O optimized, the default value is `cloud`.
        # - In other cases, the default value is `cloud_efficiency`.<props="china">After January 30, 2026, for instance types that support only cloud_essd, the default value is changed from cloud_efficiency to cloud_essd PL0. For more information, see [Change announcement](https://www.aliyun.com/notice/117844).
        # 
        # >This parameter supports the `cloud_essd_entry` value only when `InstanceType` is set to the [u1, universal instance family](https://help.aliyun.com/document_detail/457079.html) (`ecs.u1`) or the [e, economy instance family](https://help.aliyun.com/document_detail/108489.html) (`ecs.e`).
        self.category = category
        # The description of the system disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The name of the system disk. The name must be 2 to 128 characters in length and can contain characters from the Unicode letter category (including English and Chinese characters and digits). The name can contain colons (:), underscores (_), periods (.), or hyphens (-).
        self.disk_name = disk_name
        # The performance level of the enterprise SSD (ESSD) used as the system disk. When you create an ESSD as the system disk, you can set the performance level of the disk. Valid values:
        self.performance_level = performance_level
        # The size of the system disk. Unit: GiB. Valid values:
        # 
        # - Basic disk: 20 to 500.
        # - Enterprise SSD (ESSD):
        #   - PL0: 1 to 2048.
        #   - PL1: 20 to 2048.
        #   - PL2: 461 to 2048.
        #   - PL3: 1261 to 2048.
        # - ESSD AutoPL disk: 1 to 2048.
        # - Other disk types: 20 to 2048.
        # 
        # The value of this parameter must be greater than or equal to max{1, ImageSize}.
        # 
        # Default value: max{40, size of the image specified by ImageId}.
        self.size = size
        # Specifies whether to enable the performance burst feature. Valid values:
        self.bursting_enabled = bursting_enabled
        # >This parameter is not publicly available.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt the system disk. Valid values:
        # 
        # - true: encrypts the system disk.
        # 
        # - false: does not encrypt the system disk.
        # 
        # Default value: false.
        # 
        # >China (Hong Kong) Zone D and Singapore Zone A do not support encrypting the system disk when you create an instance.
        # 
        # >Notice: When you use a shared encrypted image to create a disk based on an encrypted snapshot, you must set the Encrypted parameter to true for the disk to ensure that the created disk uses the key of the account with which the image is shared.
        self.encrypted = encrypted
        # The ID of the KMS key for the system disk.
        # 
        # > If Encrypted is set to true and KMSKeyId is not specified, the default key is used for encryption, and the KMSKeyId value is returned after the instance is created.
        # > - - The disk is created from a non-shared encrypted snapshot: The encryption key used by the snapshot is used by default.
        # > - - The disk is created from a shared encrypted snapshot: The service key is used by default.
        # > - - The disk is created in a region where block storage account-level default encryption is enabled: The specified account-level key is used by default.
        # > - - Other cases: The service key is used by default.
        self.kmskey_id = kmskey_id
        # The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values: 0 to min{50,000, 1000 × Capacity - baseline performance}.
        self.provisioned_iops = provisioned_iops
        # The ID of the dedicated block storage cluster. If you want to use a disk in a dedicated block storage cluster as the system disk when you create an ECS instance, specify this parameter.
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
        self.confidential_computing_mode = confidential_computing_mode
        # The trusted system mode. Valid value: vTPM.
        self.trusted_system_mode = trusted_system_mode
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
        # The ID of the dedicated host cluster to which the ECS instance belongs. The system automatically selects a dedicated host in the cluster to deploy the ECS instance.
        # 
        # > This parameter takes effect only when `Tenancy` is set to `host`.
        # 
        # If you specify both a dedicated host (`DedicatedHostId`) and a dedicated host cluster (`SchedulerOptions.DedicatedHostClusterId`):
        # - If the dedicated host belongs to the dedicated host cluster, the ECS instance is preferentially deployed on the specified dedicated host.
        # - If the dedicated host does not belong to the dedicated host cluster, the ECS instance fails to be created.
        # 
        # <props="china">You can call [DescribeDedicatedHostClusters](https://help.aliyun.com/document_detail/184145.html) to query the list of dedicated host cluster IDs.
        # 
        # <props="intl">You can call [DescribeDedicatedHostClusters](https://help.aliyun.com/document_detail/184145.html) to query the list of dedicated host cluster IDs.
        # 
        # <props="partner">You can call [DescribeDedicatedHostClusters](https://help.aliyun.com/document_detail/184145.html) to query the list of dedicated host cluster IDs.
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
        # The private pool ID, which is the ID of the elasticity assurance or capacity reservation.
        self.id = id
        # The private pool options for instance startup. A private pool is generated after an elasticity assurance or capacity reservation takes effect. You can select a private pool when you start an instance. Valid values:
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
        # >This parameter is in invitational preview and is not publicly available.
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
        # This parameter is deprecated.
        self.numa = numa
        # The number of threads per CPU core. The number of vCPUs of an ECS instance = `CpuOptions.Core` value × `CpuOptions.ThreadsPerCore` value.
        # 
        # - `CpuOptions.ThreadsPerCore=1` indicates that hyper-threading is disabled.
        # 
        # - Only specific instance types support custom CPU thread counts.
        # 
        # <props="china">For the valid values and default value, see [Custom CPU options](https://help.aliyun.com/document_detail/145895.html).
        self.threads_per_core = threads_per_core
        # The CPU topology type of the instance. Valid values:
        # 
        # - ContinuousCoreToHTMapping: The hyper-threads (HTs) within the same core in the CPU topology of the instance are continuous.
        # - DiscreteCoreToHTMapping: The HTs within the same core in the CPU topology of the instance are discrete.
        # 
        # Default value: null.
        # 
        # > Only specific instance families support this parameter. For more information about the supported instance families, see [View and modify CPU topology](https://help.aliyun.com/document_detail/2636059.html).
        self.topology_type = topology_type
        # > This parameter is in invitational preview and is not publicly available.
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

