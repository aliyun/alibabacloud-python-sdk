# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateLaunchTemplateRequest(DaraModel):
    def __init__(
        self,
        system_disk: main_models.CreateLaunchTemplateRequestSystemDisk = None,
        auto_release_time: str = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        credit_specification: str = None,
        data_disk: List[main_models.CreateLaunchTemplateRequestDataDisk] = None,
        deletion_protection: bool = None,
        deployment_set_id: str = None,
        description: str = None,
        enable_vm_os_config: bool = None,
        host_name: str = None,
        http_endpoint: str = None,
        http_put_response_hop_limit: int = None,
        http_tokens: str = None,
        image_id: str = None,
        image_options: main_models.CreateLaunchTemplateRequestImageOptions = None,
        image_owner_alias: str = None,
        instance_charge_type: str = None,
        instance_name: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        ipv_6address_count: int = None,
        key_pair_name: str = None,
        launch_template_name: str = None,
        network_interface: List[main_models.CreateLaunchTemplateRequestNetworkInterface] = None,
        network_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        password_inherit: bool = None,
        period: int = None,
        period_unit: str = None,
        private_ip_address: str = None,
        ram_role_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_enhancement_strategy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        security_options: main_models.CreateLaunchTemplateRequestSecurityOptions = None,
        spot_duration: int = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        tag: List[main_models.CreateLaunchTemplateRequestTag] = None,
        template_resource_group_id: str = None,
        template_tag: List[main_models.CreateLaunchTemplateRequestTemplateTag] = None,
        user_data: str = None,
        v_switch_id: str = None,
        version_description: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.system_disk = system_disk
        # The automatic release time. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # - If the value of seconds (`ss`) is not `00`, the time is automatically rounded down to the start of the current minute (`mm`).
        # 
        # - The earliest release time is 30 minutes after the current time.
        # 
        # - The latest release time cannot be more than three years from the current time.
        self.auto_release_time = auto_release_time
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # - true: enables auto-renewal.
        # - false: does not enable auto-renewal.
        # 
        # Default value: false.
        # 
        # > This parameter takes effect only when `InstanceChargeType` is set to `PrePaid`.
        self.auto_renew = auto_renew
        # The auto-renewal period. Valid values: 
        #          
        # <props="china">
        # - If PeriodUnit is set to Week: 1, 2, and 3.
        # - If PeriodUnit is set to Month: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # 
        # 
        # <props="intl">If PeriodUnit is set to Month: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # The running mode of the burstable instance. Valid values:
        # 
        # - Standard: standard mode. For more information, see the performance constrained mode section in [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        # - Unlimited: unlimited mode. For more information, see the unlimited mode section in [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.credit_specification = credit_specification
        # The list of data disk information.
        self.data_disk = data_disk
        # The release protection attribute of the instance. Specifies whether the instance can be released from the console or by calling [DeleteInstance](https://help.aliyun.com/document_detail/25507.html). Valid values:
        # - true: enables release protection.
        # 
        # - false: disables release protection.
        # 
        # Default value: false.
        # 
        # > This attribute applies only to pay-as-you-go instances. It can only restrict manual release operations and does not affect system-initiated releases.
        self.deletion_protection = deletion_protection
        # The ID of the deployment set.
        self.deployment_set_id = deployment_set_id
        # The description of the instance. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable the operating system configuration of the instance.
        # > This parameter will be deprecated. For better compatibility, use other parameters.
        self.enable_vm_os_config = enable_vm_os_config
        # The hostname of the Elastic Compute Service server.
        # 
        # -   The hostname cannot start or end with a period (.) or a hyphen (-). It cannot contain consecutive periods (.) or hyphens (-).
        # -   Windows instances: The hostname must be 2 to 15 characters in length and cannot contain periods (.) or consist entirely of digits. It can contain letters, digits, and hyphens (-).
        # -   Other instances (such as Linux): The hostname must be 2 to 64 characters in length. It can contain multiple periods (.), with each segment between periods allowing letters, digits, and hyphens (-).
        self.host_name = host_name
        # Specifies whether to enable the access channel for instance metadata. Valid values:
        # 
        # - enabled: enables the access channel.
        # - disabled: disables the access channel.
        # 
        # Default value: enabled.
        # 
        # > For more information about instance metadata, see [Overview of ECS instance metadata](https://help.aliyun.com/document_detail/108460.html).
        self.http_endpoint = http_endpoint
        # > This parameter is not available for use.
        self.http_put_response_hop_limit = http_put_response_hop_limit
        # Specifies whether to forcefully use the security-hardened mode (IMDSv2) to access instance metadata. Valid values:
        # 
        # - optional: does not forcefully use the security-hardened mode.
        # - required: forcefully uses the security-hardened mode. After you set this value, instance metadata cannot be accessed in normal mode.
        # 
        # Default value: optional.
        # 
        # > For more information about the modes for
        # [Instance metadata overview](https://help.aliyun.com/document_detail/108460.html)
        self.http_tokens = http_tokens
        # The image ID. You can call [DescribeImages](https://help.aliyun.com/document_detail/25534.html) to query available image resources.
        self.image_id = image_id
        # The image-related property information.
        self.image_options = image_options
        # The source of the image. Valid values:
        # 
        # - system: a public image provided by Alibaba Cloud.
        # - self: a custom image that you created.
        # - others: a shared image from another Alibaba Cloud account.
        # - marketplace: an image from <props="china"><ph>[Alibaba Cloud Marketplace](https://market.aliyun.com/)</ph><props="intl"><ph>[Alibaba Cloud Marketplace](https://marketplace.alibabacloud.com/)</ph>. You can use Alibaba Cloud Marketplace images directly without subscribing to them first. Check the billing details of the Alibaba Cloud Marketplace image on your own.
        self.image_owner_alias = image_owner_alias
        # The billing method of the instance. Valid values:
        # 
        # - PrePaid: subscription. If you set this parameter to PrePaid, <props="china"><ph>confirm that your account supports balance payments and credit payments</ph><props="intl"><ph>confirm that your account supports credit payments</ph>. Otherwise, an `InvalidPayMethod` error is returned.
        # - PostPaid: pay-as-you-go.
        self.instance_charge_type = instance_charge_type
        # The name of the instance. The name must be 2 to 128 characters in length and can contain letters, digits, and characters from the Unicode letter category (including Chinese characters). The name can contain colons (:), underscores (_), periods (.), and hyphens (-). The default value is the `InstanceId` of the instance.
        # 
        # When you create multiple ECS instances, you can specify sequential instance names. The names can contain brackets ([]) and commas (,). For more information, see [Specify sequential instance names or hostnames](https://help.aliyun.com/document_detail/196048.html).
        self.instance_name = instance_name
        # The instance type. For more information, see [Instance family](https://help.aliyun.com/document_detail/25378.html). You can also invoke [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) to query the most recent instance type list.
        self.instance_type = instance_type
        # The billing method for network usage. Valid values:
        # 
        # - PayByBandwidth: pay-by-bandwidth.
        # - PayByTraffic: pay-by-traffic.
        # 
        # > In **pay-by-traffic** mode, the peak inbound and outbound bandwidths are used as bandwidth upper limits instead of guaranteed service metrics. When resource contention occurs, the peak bandwidth may be limited. If your workloads require guaranteed bandwidth, use the **pay-by-bandwidth** mode.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth. Unit: Mbit/s. Valid values:
        # 
        # - If the purchased outbound public bandwidth is less than or equal to 10 Mbit/s: 1 to 10. Default value: 10.
        # - If the purchased outbound public bandwidth is greater than 10 Mbit/s: 1 to the value of `InternetMaxBandwidthOut`. Default value: the value of `InternetMaxBandwidthOut`.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s. Valid values: 0 to 100.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether the instance is I/O optimized. Valid values:
        # 
        # -   none: not I/O optimized.
        # -   optimized: I/O optimized.
        self.io_optimized = io_optimized
        # The number of randomly generated IPv6 addresses to assign to the primary ENI. Valid values: 1 to 10.
        self.ipv_6address_count = ipv_6address_count
        # The name of the key pair.
        # 
        # -   For Windows instances, this parameter is ignored. Even if you specify this parameter, only the `Password` content is used.
        # -   For Linux instances, password-based logon is disabled during initialization.
        self.key_pair_name = key_pair_name
        # The name of the launch template. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with `http://` or `https://`. The name can contain digits, colons (:), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.launch_template_name = launch_template_name
        # The network interface controller (NIC) information.
        self.network_interface = network_interface
        # The network type of the instance. Valid values:
        # 
        # - classic: classic network. This feature has been retired. For more information, see [Retirement notice](https://help.aliyun.com/document_detail/2833134.html).
        # - vpc: VPC.
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to use the password preset in the image.
        # 
        # > When you use this parameter, the Password parameter must be empty. Make sure that the image you use has a password configured.
        self.password_inherit = password_inherit
        # The subscription duration of the resource. Unit: months. This parameter takes effect and is required only when `InstanceChargeType` is set to `PrePaid`. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        self.period = period
        # The unit of the subscription billable methods duration. Valid values: 
        # 
        # <props="china">
        # - Week.
        # - Month (default).
        # 
        # 
        # 
        # <props="intl">Month (default).
        self.period_unit = period_unit
        # The private IP address of the instance.
        # 
        # When you specify a private IP address for a VPC-connected ECS instance, the IP address must be from the idle CIDR block of the vSwitch (`VSwitchId`).
        self.private_ip_address = private_ip_address
        # The name of the instance RAM role. You can call the RAM API [ListRoles](https://help.aliyun.com/document_detail/28713.html) to query the instance RAM roles that you have created.
        self.ram_role_name = ram_role_name
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the instance, block storage, and elastic network interface controller (NIC) belong.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable security hardening for the operating system. Valid values:
        # 
        # -   Active: enables security hardening. This value is applicable only to public images.
        # -   Deactive: does not enable security hardening. This value is applicable to all image types.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The ID of the security group to which the instance belongs. Instances in the same security group can communicate with each other. A security group can contain up to 1,000 instances.
        # 
        # > You cannot specify both `SecurityGroupId` and `SecurityGroupIds.N`.
        self.security_group_id = security_group_id
        # The IDs of one or more security groups to which the instance belongs. The valid value range of N depends on the maximum number of security groups to which an instance can belong. For more information, see [Limits](https://help.aliyun.com/document_detail/25412.html).
        # 
        # > You cannot specify both `SecurityGroupId` and `SecurityGroupIds.N`.
        self.security_group_ids = security_group_ids
        # The security options.
        self.security_options = security_options
        # The protection period of the spot instance. Unit: hours. Default value: 1. Valid values:
        # - 1: After a spot instance is created, Alibaba Cloud ensures that the instance is not automatically released within 1 hour. After the 1-hour protection period ends, the system compares the bid price with the market price and checks the resource inventory to determine whether to retain automatic release the instance.
        # - 0: After a spot instance is created, Alibaba Cloud does not ensure that the instance runs for 1 hour. The system compares the bid price with the market price and checks the resource inventory to determine whether to retain automatic release the instance.
        # 
        # Alibaba Cloud sends an ECS system event notification 5 minutes before the instance is released. Spot instances are billed by second. Select an appropriate protection period based on the expected task execution duration.
        # 
        # > This parameter takes effect only when SpotStrategy is set to SpotWithPriceLimit or SpotAsPriceGo.
        self.spot_duration = spot_duration
        # The maximum hourly price of the instance. This parameter supports up to three decimal places and takes effect when `SpotStrategy` is set to `SpotWithPriceLimit`.
        self.spot_price_limit = spot_price_limit
        # The preemption policy for the pay-as-you-go instance. This parameter takes effect when `InstanceChargeType` is set to `PostPaid`. Valid values:
        # 
        # -   NoSpot: The instance is a regular pay-as-you-go instance.
        # -   SpotWithPriceLimit: The instance is a spot instance with a user-defined maximum hourly price.
        # -   SpotAsPriceGo: The instance is a spot instance for which the market price at the time of purchase is automatically used as the bid price.
        self.spot_strategy = spot_strategy
        # The tags for instances, disks, and primary ENIs created from this template version.
        # 
        # <details>
        # <summary>Scenarios</summary>
        # After you call CreateLaunchTemplate to create a template, the auto-generated default version uses these tags to tag instances, disks, and primary ENIs when you create instances.
        # </details>
        self.tag = tag
        # The ID of the resource group to which the launch template belongs.
        self.template_resource_group_id = template_resource_group_id
        # The tag key-value pairs of the launch template itself.
        # 
        # > Currently, you can create and query tags for launch templates only by using API operations. The console does not support creating or viewing these tags.
        self.template_tag = template_tag
        # The instance user data. The data must be Base64-encoded. The maximum size of the raw data is 32 KB.
        self.user_data = user_data
        # The vSwitch ID. This parameter is required when you create a VPC-connected instance.
        self.v_switch_id = v_switch_id
        # The description of the launch template version. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.version_description = version_description
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()
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
        if self.security_options:
            self.security_options.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
        if self.template_tag:
            for v1 in self.template_tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.auto_release_time is not None:
            result['AutoReleaseTime'] = self.auto_release_time

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification

        result['DataDisk'] = []
        if self.data_disk is not None:
            for k1 in self.data_disk:
                result['DataDisk'].append(k1.to_map() if k1 else None)

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_vm_os_config is not None:
            result['EnableVmOsConfig'] = self.enable_vm_os_config

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.http_endpoint is not None:
            result['HttpEndpoint'] = self.http_endpoint

        if self.http_put_response_hop_limit is not None:
            result['HttpPutResponseHopLimit'] = self.http_put_response_hop_limit

        if self.http_tokens is not None:
            result['HttpTokens'] = self.http_tokens

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_options is not None:
            result['ImageOptions'] = self.image_options.to_map()

        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias

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

        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.launch_template_name is not None:
            result['LaunchTemplateName'] = self.launch_template_name

        result['NetworkInterface'] = []
        if self.network_interface is not None:
            for k1 in self.network_interface:
                result['NetworkInterface'].append(k1.to_map() if k1 else None)

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

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

        if self.security_options is not None:
            result['SecurityOptions'] = self.security_options.to_map()

        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration

        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.template_resource_group_id is not None:
            result['TemplateResourceGroupId'] = self.template_resource_group_id

        result['TemplateTag'] = []
        if self.template_tag is not None:
            for k1 in self.template_tag:
                result['TemplateTag'].append(k1.to_map() if k1 else None)

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.version_description is not None:
            result['VersionDescription'] = self.version_description

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SystemDisk') is not None:
            temp_model = main_models.CreateLaunchTemplateRequestSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('AutoReleaseTime') is not None:
            self.auto_release_time = m.get('AutoReleaseTime')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')

        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.CreateLaunchTemplateRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableVmOsConfig') is not None:
            self.enable_vm_os_config = m.get('EnableVmOsConfig')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('HttpEndpoint') is not None:
            self.http_endpoint = m.get('HttpEndpoint')

        if m.get('HttpPutResponseHopLimit') is not None:
            self.http_put_response_hop_limit = m.get('HttpPutResponseHopLimit')

        if m.get('HttpTokens') is not None:
            self.http_tokens = m.get('HttpTokens')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageOptions') is not None:
            temp_model = main_models.CreateLaunchTemplateRequestImageOptions()
            self.image_options = temp_model.from_map(m.get('ImageOptions'))

        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')

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

        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('LaunchTemplateName') is not None:
            self.launch_template_name = m.get('LaunchTemplateName')

        self.network_interface = []
        if m.get('NetworkInterface') is not None:
            for k1 in m.get('NetworkInterface'):
                temp_model = main_models.CreateLaunchTemplateRequestNetworkInterface()
                self.network_interface.append(temp_model.from_map(k1))

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

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

        if m.get('SecurityOptions') is not None:
            temp_model = main_models.CreateLaunchTemplateRequestSecurityOptions()
            self.security_options = temp_model.from_map(m.get('SecurityOptions'))

        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')

        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateLaunchTemplateRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TemplateResourceGroupId') is not None:
            self.template_resource_group_id = m.get('TemplateResourceGroupId')

        self.template_tag = []
        if m.get('TemplateTag') is not None:
            for k1 in m.get('TemplateTag'):
                temp_model = main_models.CreateLaunchTemplateRequestTemplateTag()
                self.template_tag.append(temp_model.from_map(k1))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateLaunchTemplateRequestTemplateTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the launch template. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the launch template. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. The tag value cannot contain `http://` or `https://`.
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

class CreateLaunchTemplateRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key for instances, disks, and primary ENIs created from this template version. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with aliyun or acs:. The tag key cannot contain http:// or https://.
        self.key = key
        # The tag value for instances, disks, and primary ENIs created from this template version. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain http:// or https://.
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

class CreateLaunchTemplateRequestSecurityOptions(DaraModel):
    def __init__(
        self,
        trusted_system_mode: str = None,
    ):
        # The trusted system mode. Set the value to vTPM.
        # 
        # The following instance families support trusted system mode:
        # - g7, c7, and r7.
        # - Enhanced instance families (g7t, c7t, and r7t).
        # 
        # When you create ECS instances of the preceding instance types, you must configure this parameter. Take note of the following items:
        # 
        # - To use Alibaba Cloud Trusted System, set this parameter to vTPM. Then, Alibaba Cloud Trusted System performs trusted verification when the instance starts.
        # - If you do not use Alibaba Cloud Trusted System, you do not need to configure this parameter. However, if the ECS instance that you create uses the Enclave-based confidential computing pattern (`SecurityOptions.ConfidentialComputingMode=Enclave`), the trusted system is also enabled for the instance.
        # - When you use OpenAPI to create a trusted ECS instance, you can only invoke `RunInstances`. `CreateInstance` does not support the `SecurityOptions.TrustedSystemMode` parameter.
        # > If you specify the instance as a trusted instance during creation, you can replace the system disk only with an image that supports the trusted system.
        # 
        # For more information about the trusted system, see [Overview of trusted features for security-enhanced instances](https://help.aliyun.com/document_detail/201394.html).
        self.trusted_system_mode = trusted_system_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.trusted_system_mode is not None:
            result['TrustedSystemMode'] = self.trusted_system_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrustedSystemMode') is not None:
            self.trusted_system_mode = m.get('TrustedSystemMode')

        return self

class CreateLaunchTemplateRequestNetworkInterface(DaraModel):
    def __init__(
        self,
        delete_on_release: bool = None,
        description: str = None,
        instance_type: str = None,
        network_interface_name: str = None,
        network_interface_traffic_mode: str = None,
        primary_ip_address: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        v_switch_id: str = None,
    ):
        # Specifies whether to retain the ENI when the instance is released. Valid values:
        # 
        # - true: does not retain the ENI.
        # 
        # - false: retains the ENI.
        # 
        # Default value: true.
        # 
        # > This parameter takes effect only for secondary ENIs.
        self.delete_on_release = delete_on_release
        # The description of the secondary network interface controller (NIC). The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`. The value of N in `NetworkInterface.N` cannot be greater than 1.
        self.description = description
        # The type of the network interface controller (NIC). Valid values of N: 1 to 2. If you set N to 1, you can configure a primary or secondary NIC. If you set N to 2, you must configure one primary NIC and one secondary NIC.
        # 
        # Valid values:
        # 
        # - Primary: primary NIC.
        # - Secondary: secondary NIC.
        # 
        # Default value: Secondary.
        self.instance_type = instance_type
        # The name of the network interface controller (NIC).
        # 
        # Take note of the following items:
        # 
        # - Valid values of N: 1 to 2. If you set N to 1, you can configure a primary or secondary NIC. If you set N to 2, you must configure one primary NIC and one secondary NIC.
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Primary`, you do not need to set this parameter.
        self.network_interface_name = network_interface_name
        # The communication mode of the primary ENI. Valid values:
        # 
        # - Standard: uses the TCP communication mode.
        # - HighPerformance: enables the Elastic RDMA Interface (ERI) and uses the RDMA communication mode.
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # Adds a network interface controller (NIC) and sets the primary IP address.
        # 
        # Take note of the following items:
        # 
        # - Valid values of N: 1 to 2.
        #     - If you set N to 1, you can configure a primary or secondary NIC. If the `Amount` parameter is set to a value greater than 1 and you configure a primary NIC with this parameter specified, consecutive primary IP addresses starting from the specified IP address are allocated to multiple ECS instances in batch. In this case, you cannot attach a secondary NIC to the instances.
        #     - If you set N to 2, you must configure one primary NIC and one secondary NIC. If the `Amount` parameter is set to a value greater than 1 and this parameter is specified for the primary NIC, you cannot configure a secondary NIC (that is, you cannot set `NetworkInterface.2.InstanceType=Secondary`).
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Primary`, this parameter has the same effect as `PrivateIpAddress`, but you cannot specify both this parameter and `PrivateIpAddress`.
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Secondary` or left empty, this parameter specifies the primary IP address of the secondary NIC. By default, an IP address is randomly selected from the vSwitch CIDR block to which the NIC belongs.
        # 
        # > When you create an ECS instance, you can attach up to one secondary NIC. After the instance is created, you can invoke [CreateNetworkInterface](https://help.aliyun.com/document_detail/58504.html) and [AttachNetworkInterface](https://help.aliyun.com/document_detail/58515.html) to attach more secondary NICs.
        self.primary_ip_address = primary_ip_address
        # The ID of the security group to which the network interface controller (NIC) belongs.
        # 
        # Take note of the following items:
        # 
        # - Valid values of N: 1 to 2. If you set N to 1, you can configure a primary or secondary NIC. If you set N to 2, you must configure one primary NIC and one secondary NIC.
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Primary`, you must set this parameter. This parameter has the same effect as `SecurityGroupId`, but you cannot specify `SecurityGroupId`, `SecurityGroupIds.N`, or `NetworkInterface.N.SecurityGroupIds.N`.
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Secondary` or left empty, this parameter is optional. Default value: the security group of the ECS instance.
        self.security_group_id = security_group_id
        # The IDs of one or more security groups to which the network interface controller (NIC) belongs.
        # 
        # - The first N has a valid value range of 1 to 2. If you set N to 1, you can configure a primary or secondary NIC. If you set N to 2, you must configure one primary NIC and one secondary NIC.
        # - The second N specifies one or more security group IDs. The valid value range of N depends on the maximum number of security groups to which an instance can belong. For more information, see [Security group limits](~~25412#SecurityGroupQuota1~~).
        # 
        # Take note of the following items:
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Primary`, you must set this parameter or `NetworkInterface.N.SecurityGroupId`. This parameter has the same effect as `SecurityGroupIds.N`, but you cannot specify `SecurityGroupId`, `SecurityGroupIds.N`, or `NetworkInterface.N.SecurityGroupId`.
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Secondary` or left empty, this parameter is optional. Default value: the security group of the ECS instance.
        self.security_group_ids = security_group_ids
        # The vSwitch ID of the network interface controller (NIC).
        # 
        # Take note of the following items:
        # 
        # - Valid values of N: 1 to 2. If you set N to 1, you can configure a primary or secondary NIC. If you set N to 2, you must configure one primary NIC and one secondary NIC.
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Primary`, this parameter is required. This parameter has the same effect as `VSwitchId`, but you cannot specify both this parameter and `VSwitchId`.
        # 
        # - If `NetworkInterface.N.InstanceType` is set to `Secondary` or left empty, this parameter is optional. Default value: the vSwitch of the ECS instance.
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

        if self.network_interface_name is not None:
            result['NetworkInterfaceName'] = self.network_interface_name

        if self.network_interface_traffic_mode is not None:
            result['NetworkInterfaceTrafficMode'] = self.network_interface_traffic_mode

        if self.primary_ip_address is not None:
            result['PrimaryIpAddress'] = self.primary_ip_address

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

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

        if m.get('NetworkInterfaceName') is not None:
            self.network_interface_name = m.get('NetworkInterfaceName')

        if m.get('NetworkInterfaceTrafficMode') is not None:
            self.network_interface_traffic_mode = m.get('NetworkInterfaceTrafficMode')

        if m.get('PrimaryIpAddress') is not None:
            self.primary_ip_address = m.get('PrimaryIpAddress')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class CreateLaunchTemplateRequestImageOptions(DaraModel):
    def __init__(
        self,
        login_as_non_root: bool = None,
    ):
        # Indicates whether the instance that uses this image supports logon with the ecs-user account.
        # Valid values:
        # - true: supported.
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

class CreateLaunchTemplateRequestDataDisk(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        delete_with_instance: bool = None,
        description: str = None,
        device: str = None,
        disk_name: str = None,
        encrypted: str = None,
        kmskey_id: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        # The ID of the automatic snapshot policy applied to the data disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable the performance burst feature. Valid values:
        # 
        # - true: enables the performance burst feature.
        # - false: does not enable the performance burst feature.
        self.bursting_enabled = bursting_enabled
        # The category of data disk N. Valid values:
        # 
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: enterprise SSD.
        # - cloud: basic disk.
        # - cloud_auto: ESSD AutoPL disk.
        # - cloud_regional_disk_auto: regional ESSD.
        # - cloud_essd_entry: ESSD Entry disk.
        #   > The cloud_essd_entry value is supported only when `InstanceType` is set to the `ecs.u1` or `ecs.e` instance family.
        # - elastic_ephemeral_disk_standard: elastic ephemeral disk - standard.
        # - elastic_ephemeral_disk_premium: elastic ephemeral disk - Premium Edition.
        # 
        # For I/O optimized instances, the default value is cloud_efficiency. For non-I/O optimized instances, the default value is cloud.
        # Default value description:
        # 
        # - If InstanceType is a retired instance type that is not I/O optimized, the default value of this parameter is `cloud`.
        # - In other cases, the default value is `cloud_efficiency`.<props="china">After January 30, 2026, if the I/O optimized instance type does not support cloud_auto, the default value is cloud_efficiency. Otherwise, the default value is cloud_auto, and the performance burst feature is enabled by default (which incurs additional fees. For details, see [Billing examples](~~368372#p_75k_2hp_7gp~~)). For more information, see [Change notice](https://www.aliyun.com/notice/117844).
        self.category = category
        # Specifies whether to release the data disk when the instance is released. Valid values:
        # 
        # - true: releases the data disk when the instance is released.
        # - false: does not release the data disk when the instance is released.
        # 
        # Default value: true.
        self.delete_with_instance = delete_with_instance
        # The description of the data disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The mount point of the data disk. The naming convention varies based on the number of data disks attached:
        # - 1 to 25 data disks: /dev/xvd`[b-z]`
        # 
        # - More than 25 data disks: /dev/xvd`[aa-zz]`. For example, the 26th data disk is named /dev/xvdaa, the 27th data disk is named /dev/xvdab, and so on.
        # 
        # > This parameter is intended only for full image (whole-machine image) scenarios. You can set this parameter to the mount point of a data disk in the full image and modify the corresponding `DataDisk.N.Size` and `DataDisk.N.Category` parameters to change the disk category and size of the data disk in the full image.
        self.device = device
        # The name of the data disk. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with `http://` or `https://`. The name can contain digits, colons (:), underscores (_), and hyphens (-).
        self.disk_name = disk_name
        # Specifies whether to encrypt the data disk.
        self.encrypted = encrypted
        # The KMS key ID for the data disk.
        self.kmskey_id = kmskey_id
        # The performance level of the ESSD used as a data disk. The value of N must be the same as that in `DataDisk.N.Category=cloud_essd`. Valid values:
        # 
        # - PL0: a single disk can deliver up to 10,000 random read/write IOPS.
        # - PL1 (default): a single disk can deliver up to 50,000 random read/write IOPS.
        # - PL2: a single disk can deliver up to 100,000 random read/write IOPS.
        # - PL3: a single disk can deliver up to 1,000,000 random read/write IOPS.
        # 
        # For information about how to select an ESSD performance level, see [Enterprise SSDs](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values: 0 to min{50000, 1000 × Capacity - Baseline Performance}.
        # 
        # Baseline Performance = min{1,800 + 50 × Capacity, 50,000}
        # 
        # > This parameter is supported only when DiskCategory is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html) and [Modify the provisioned performance of an ESSD AutoPL disk](https://help.aliyun.com/document_detail/413275.html).
        self.provisioned_iops = provisioned_iops
        # The size of data disk N. Valid values of N: 1 to 16. Unit: GiB. Valid values:
        # 
        # -   cloud: 5 to 2000.
        # -   cloud_efficiency: 20 to 32768.
        # -   cloud_ssd: 20 to 32768.
        # -   cloud_essd: The valid value range depends on the value of `DataDisk.N.PerformanceLevel`.
        #     - PL0: 1 to 32768.
        #     - PL1: 20 to 32768.
        #     - PL2: 461 to 32768.
        #     - PL3: 1261 to 32768.
        # - cloud_auto: 1 to 32,768.
        # - cloud_essd_entry: 10 to 32,768.
        # 
        # The value of this parameter must be greater than or equal to the size of the snapshot specified by `SnapshotId`.
        self.size = size
        # The ID of the snapshot used to create data disk N. Valid values of N: 1 to 16. After you specify `DataDisk.N.SnapshotId`, the `DataDisk.N.Size` parameter is ignored. The actual size of the created disk is the size of the specified snapshot.
        # 
        # > You cannot use snapshots created on or before July 15, 2013. Such requests are rejected.
        self.snapshot_id = snapshot_id

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

        return self

class CreateLaunchTemplateRequestSystemDisk(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        delete_with_instance: bool = None,
        description: str = None,
        disk_name: str = None,
        encrypted: str = None,
        iops: int = None,
        kmskey_id: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
    ):
        # The ID of the automatic snapshot policy applied to the system disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable the performance burst feature. Valid values:
        # 
        # - true: enables the performance burst feature.
        # - false: does not enable the performance burst feature.
        self.bursting_enabled = bursting_enabled
        # The category of the system disk. Valid values:
        # 
        # -   cloud: basic disk.
        # -   cloud_efficiency: ultra disk.
        # -   cloud_ssd: standard SSD.
        # -   cloud_essd: enterprise SSD (ESSD). You can use the `SystemDisk.PerformanceLevel` parameter to set the performance level of the disk.
        # - cloud_auto: ESSD AutoPL disk.
        # - cloud_essd_entry: ESSD Entry disk.
        # 
        # For retired instance types that are not I/O optimized, the default value is cloud. Otherwise, the default value is cloud_efficiency.
        self.category = category
        # Specifies whether to release the system disk when the instance is released. Valid values:
        # 
        # - true: releases the system disk when the instance is released.
        # - false: does not release the system disk when the instance is released.
        # 
        # Default value: true.
        self.delete_with_instance = delete_with_instance
        # The description of the system disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The name of the system disk. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with `http://` or `https://`. The name can contain digits, colons (:), underscores (_), and hyphens (-).
        self.disk_name = disk_name
        # Specifies whether to encrypt the system disk. Valid values:
        # 
        # - true: encrypts the system disk.
        # - false: does not encrypt the system disk.
        # 
        # Default value: false.
        # 
        # > Zone D in Hong Kong (China) and Zone A in Singapore do not support system disk encryption when you create instances.
        self.encrypted = encrypted
        # > This parameter is in invitational preview and is not publicly available.
        self.iops = iops
        # The KMS key ID of the system disk.
        self.kmskey_id = kmskey_id
        # The performance level of the ESSD used as the system disk. Valid values:
        # 
        # - PL0 (default): a single disk can deliver up to 10,000 random read/write IOPS.
        # - PL1: a single disk can deliver up to 50,000 random read/write IOPS.
        # - PL2: a single disk can deliver up to 100,000 random read/write IOPS.
        # - PL3: a single disk can deliver up to 1,000,000 random read/write IOPS.
        # 
        # For information about how to select an ESSD performance level, see [Enterprise SSDs](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values: 0 to min{50000, 1000 × Capacity - Baseline Performance}.
        # 
        # Baseline Performance = min{1,800 + 50 × Capacity, 50,000}
        # 
        # > This parameter is supported only when DiskCategory is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html) and [Modify the provisioned performance of an ESSD AutoPL disk](https://help.aliyun.com/document_detail/413275.html).
        self.provisioned_iops = provisioned_iops
        # The size of the system disk. Unit: GiB. Valid values:
        # 
        # - cloud: 20 to 500.
        # - Other disk categories: 20 to 2048.
        # 
        # The value of this parameter must be greater than or equal to max{20, ImageSize}.
        self.size = size

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

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.iops is not None:
            result['Iops'] = self.iops

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.size is not None:
            result['Size'] = self.size

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

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('Iops') is not None:
            self.iops = m.get('Iops')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

