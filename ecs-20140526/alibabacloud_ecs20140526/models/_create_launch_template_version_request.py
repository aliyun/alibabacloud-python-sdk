# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateLaunchTemplateVersionRequest(DaraModel):
    def __init__(
        self,
        system_disk: main_models.CreateLaunchTemplateVersionRequestSystemDisk = None,
        auto_release_time: str = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        credit_specification: str = None,
        data_disk: List[main_models.CreateLaunchTemplateVersionRequestDataDisk] = None,
        deletion_protection: bool = None,
        deployment_set_id: str = None,
        description: str = None,
        enable_vm_os_config: bool = None,
        host_name: str = None,
        http_endpoint: str = None,
        http_put_response_hop_limit: int = None,
        http_tokens: str = None,
        image_id: str = None,
        image_options: main_models.CreateLaunchTemplateVersionRequestImageOptions = None,
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
        launch_template_id: str = None,
        launch_template_name: str = None,
        network_interface: List[main_models.CreateLaunchTemplateVersionRequestNetworkInterface] = None,
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
        security_options: main_models.CreateLaunchTemplateVersionRequestSecurityOptions = None,
        spot_duration: int = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        tag: List[main_models.CreateLaunchTemplateVersionRequestTag] = None,
        user_data: str = None,
        v_switch_id: str = None,
        version_description: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.system_disk = system_disk
        # The automatic release time. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. For more information, see [ISO 8601](https://help.aliyun.com/document_detail/25696.html).
        # 
        # - If the value of seconds (`ss`) is not `00`, the time is automatically rounded down to the current minute (`mm`).
        # 
        # - The release time must be at least 30 minutes later than the current time.
        # 
        # - The release time cannot be more than three years later than the current time.
        self.auto_release_time = auto_release_time
        # Specifies whether to enable auto-renewal. This parameter takes effect only when the `InstanceChargeType` parameter is set to `PrePaid`. Valid values:
        # 
        # - true: Enables auto-renewal.
        # - false: Disables auto-renewal.
        # 
        # Default value: false.
        self.auto_renew = auto_renew
        # The auto-renewal period. Valid values: 
        #          
        # <props="china">
        # - Valid values when PeriodUnit is set to Week: 1, 2, and 3.
        # - Valid values when PeriodUnit is set to Month: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # 
        # 
        # <props="intl">Valid values when PeriodUnit is set to Month: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # The operating mode of the burstable instance. Valid values:
        # 
        # - Standard: standard mode. For more information about the instance performance in this mode, see the "Standard mode" section in [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        # - Unlimited: unlimited mode. For more information about the instance performance in this mode, see the "Unlimited mode" section in [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.credit_specification = credit_specification
        # The data disks.
        self.data_disk = data_disk
        # The release protection property of the instance. This property specifies whether the instance can be released by using the ECS console or by calling the [DeleteInstance](https://help.aliyun.com/document_detail/25507.html) operation. Valid values:
        # - true: Enables release protection for the instance.
        # 
        # - false: Disables release protection for the instance.
        # 
        # Default value: false.
        # 
        # > This property applies only to pay-as-you-go instances. It can prevent only manual release operations, but not system release operations.
        self.deletion_protection = deletion_protection
        # The ID of the deployment set.
        self.deployment_set_id = deployment_set_id
        # The instance description. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable the operating system configuration of the instance.
        self.enable_vm_os_config = enable_vm_os_config
        # The hostname of the cloud server.
        # 
        # -   The hostname cannot start or end with a period (.) or a hyphen (-). It cannot contain consecutive periods (.) or hyphens (-).
        # -   For a Windows instance, the hostname must be 2 to 15 characters in length. It cannot contain periods (.) or contain only digits. It can contain letters, digits, and hyphens (-).
        # -   For an instance of other operating systems such as Linux, the hostname must be 2 to 64 characters in length. It can contain multiple periods (.). The characters between two consecutive periods are considered a segment. Each segment can contain letters, digits, and hyphens (-).
        self.host_name = host_name
        # Specifies whether to enable the access channel for instance metadata. Valid values:
        # 
        # - enabled: Enables the access channel.
        # - disabled: Disables the access channel.
        # 
        # Default value: enabled.
        # 
        # > For more information about instance metadata, see [Overview of instance metadata](https://help.aliyun.com/document_detail/108460.html).
        self.http_endpoint = http_endpoint
        # > This parameter is not available.
        self.http_put_response_hop_limit = http_put_response_hop_limit
        # Specifies whether to forcibly use the security hardening mode (IMDSv2) to access instance metadata. Valid values:
        # 
        # - optional: Does not forcibly use the security hardening mode.
        # - required: Forcibly uses the security hardening mode. After you set this value, you cannot access instance metadata in normal mode.
        # 
        # Default value: optional.
        # 
        # > For more information about the modes for accessing instance metadata, see [Overview of instance metadata](https://help.aliyun.com/document_detail/108460.html).
        self.http_tokens = http_tokens
        # The image ID. This is the image resource selected when the instance is started. You can call the [DescribeImages](https://help.aliyun.com/document_detail/25534.html) operation to query the available image resources.
        self.image_id = image_id
        # The image-related properties.
        self.image_options = image_options
        # The image source.
        # > This parameter will be deprecated soon. To improve compatibility, use other parameters instead.
        self.image_owner_alias = image_owner_alias
        # The billing method of the instance. Valid values:
        # 
        # <props="china">
        # - PrePaid: subscription. If you select this billing method, you must confirm that your account supports balance payment and credit payment. Otherwise, an `InvalidPayMethod` fault is returned.
        # - PostPaid: pay-as-you-go.
        # 
        # 
        # <props="intl">
        # - PrePaid: subscription. If you select this billing method, you must confirm that your account supports credit payment. Otherwise, an `InvalidPayMethod` fault is returned.
        # - PostPaid: pay-as-you-go.
        # 
        # 
        # <props="partner">
        # - PrePaid: subscription. If you select this billing method, you must confirm that your account supports credit payment. Otherwise, an `InvalidPayMethod` fault is returned.
        # - PostPaid: pay-as-you-go.
        self.instance_charge_type = instance_charge_type
        # The instance name. The name must be 2 to 128 characters in length and can contain letters and digits in the Unicode letter category. It can contain colons (:), underscores (_), periods (.), and hyphens (-). The default value is the `InstanceId` of the instance.
        # 
        # When you create multiple ECS instances, you can specify sequential instance names in batches. The names can contain brackets ([]) and commas (,). For more information, see [Specify sequential instance names or hostnames](https://help.aliyun.com/document_detail/196048.html).
        self.instance_name = instance_name
        # The instance type. For more information, see [instance family](https://help.aliyun.com/document_detail/25378.html). You can also invoke the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query the most recent instance type list.
        self.instance_type = instance_type
        # The billing method for outbound Internet bandwidth. Valid values:
        # 
        # - PayByBandwidth: pay-by-bandwidth
        # - PayByTraffic: pay-by-traffic
        # 
        # > In the **pay-by-traffic** pattern, the peak inbound and outbound bandwidths are used as upper limits of bandwidths instead of guaranteed performance specifications. In the event of resource contention, the peak bandwidths cannot be guaranteed. If your business requires guaranteed bandwidths, use the **pay-by-bandwidth** pattern.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth. Unit: Mbit/s. Valid values:
        # 
        # - If the purchased outbound public bandwidth is less than or equal to 10 Mbit/s: 1 to 10. Default value: 10.
        # - If the purchased outbound public bandwidth is greater than 10 Mbit/s: 1 to the value of `InternetMaxBandwidthOut`. Default value: the value of `InternetMaxBandwidthOut`.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s. Valid values: 0 to 100.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether the instance is an I/O optimized instance. Valid values:
        # 
        # -   none: The instance is not I/O optimization.
        # -   optimized: The instance is I/O optimization.
        self.io_optimized = io_optimized
        # The number of IPv6 addresses to be randomly generated for the primary ENI. Valid values: 1 to 10.
        self.ipv_6address_count = ipv_6address_count
        # The name of the key pair.
        # 
        # -   For a Windows instance, this parameter is ignored. Even if this parameter is specified, only the `Password` parameter takes effect.
        # -   For a Linux instance, password logon is disabled by default.
        self.key_pair_name = key_pair_name
        # The launch template ID. For more information, call the [DescribeLaunchTemplates](https://help.aliyun.com/document_detail/73759.html) operation. You must specify `LaunchTemplateId` or `LaunchTemplateName` to identify the launch template.
        self.launch_template_id = launch_template_id
        # The name of the launch template. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with `http://` or `https://`. It can contain digits, colons (:), underscores (_), and hyphens (-).
        self.launch_template_name = launch_template_name
        # The elastic network interface controller (NIC) information.
        self.network_interface = network_interface
        # The network type of the instance. Valid values:
        # 
        # - vpc: VPC
        # - classic: classic network. The classic network is no longer available. For more information, see [Notice on the discontinuation of the classic network](https://help.aliyun.com/document_detail/2833134.html).
        self.network_type = network_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # Specifies whether to use the preset password of the image. Valid values:
        # - true
        # - false
        # 
        # Default value: false.
        # 
        # > When you specify this parameter, leave the Password parameter empty. Make sure that the specified image has a preset password.
        self.password_inherit = password_inherit
        # The subscription period of the instance. Unit: months. This parameter is required and takes effect only when `InstanceChargeType` is set to `PrePaid`. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        self.period = period
        # The unit of the subscription Billable methods. Valid values: 
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
        # When you specify a private IP address for a VPC-type ECS instance, make sure that the IP address is an idle IP address within the CIDR block of the vSwitch specified by `VSwitchId`.
        self.private_ip_address = private_ip_address
        # The name of the instance RAM role. You can call the RAM API operation [ListRoles](https://help.aliyun.com/document_detail/28713.html) to query the instance RAM roles that you have created.
        self.ram_role_name = ram_role_name
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable security hardening for the operating system. Valid values:
        # 
        # -   Active: enables security hardening. This value is applicable only to public images.
        # -   Deactive: disables security hardening. This value is applicable to all image types.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The ID of the security group to which the instance created by using this version belongs. Instances in the same security group can access each other.
        # 
        # > You cannot specify both `SecurityGroupId` and `SecurityGroupIds.N`.
        self.security_group_id = security_group_id
        # The security groups to which the instance is added. The valid values of N are subject to the quota of security groups to which an instance can be added. For more information, see [Limits](https://help.aliyun.com/document_detail/25412.html).
        # 
        # > You cannot specify both `SecurityGroupId` and `SecurityGroupIds.N` at the same time.
        self.security_group_ids = security_group_ids
        # The security options.
        self.security_options = security_options
        # The protection period of the spot instance. Unit: hours. Default value: 1. Valid values:
        # - 1: Alibaba Cloud guarantees that the instance is not subject to automatic release for 1 hour after it is created. After 1 hour, the system compares the bid price with the marketplace price and checks the resource inventory to determine whether to retain or revoke the instance.
        # - 0: Alibaba Cloud does not guarantee that the instance is retained for 1 hour after it is created. The system compares the bid price with the marketplace price and checks the resource inventory to determine whether to retain or revoke the instance.
        # 
        # Alibaba Cloud sends you a notification by using an ECS system event 5 minutes before the instance is revoked. Spot instances use second billing. We recommend that you select an appropriate protection period based on the execution duration of your specific tasks.
        # 
        # > This parameter takes effect only when SpotStrategy is set to SpotWithPriceLimit or SpotAsPriceGo.
        self.spot_duration = spot_duration
        # The maximum hourly price of the instance. The value can be accurate to three decimal places.
        self.spot_price_limit = spot_price_limit
        # The preemption policy for the pay-as-you-go instance. This parameter takes effect when `InstanceChargeType` is set to `PostPaid`. Valid values:
        # 
        # -   NoSpot: Spot instance is a regular pay-as-you-go instance.
        # -   SpotWithPriceLimit: Spot instance is a preemptible instance with a user-defined maximum hourly price.
        # -   SpotAsPriceGo: Spot instance is a preemptible instance for which the market price is automatically used as the bid price.
        self.spot_strategy = spot_strategy
        # The tags of the instances, disks, and primary ENIs created by using this version.
        self.tag = tag
        # Instance user data of the instance. Instance user data must be encoded in Base64. The maximum size of the raw data is 32 KB.
        self.user_data = user_data
        # The ID of the vSwitch. This parameter is required when you create a VPC-type instance.
        self.v_switch_id = v_switch_id
        # The description of the launch template version. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.version_description = version_description
        # The ID of the virtual private cloud (VPC) to which the instance belongs.
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

        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

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
            temp_model = main_models.CreateLaunchTemplateVersionRequestSystemDisk()
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
                temp_model = main_models.CreateLaunchTemplateVersionRequestDataDisk()
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
            temp_model = main_models.CreateLaunchTemplateVersionRequestImageOptions()
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

        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        if m.get('LaunchTemplateName') is not None:
            self.launch_template_name = m.get('LaunchTemplateName')

        self.network_interface = []
        if m.get('NetworkInterface') is not None:
            for k1 in m.get('NetworkInterface'):
                temp_model = main_models.CreateLaunchTemplateVersionRequestNetworkInterface()
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
            temp_model = main_models.CreateLaunchTemplateVersionRequestSecurityOptions()
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
                temp_model = main_models.CreateLaunchTemplateVersionRequestTag()
                self.tag.append(temp_model.from_map(k1))

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

class CreateLaunchTemplateVersionRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instances, disks, and primary ENIs created by using this version. Valid values of N: 1 to 20. If you specify this parameter, it cannot be an empty string. The tag key can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://.
        self.key = key
        # The tag value of the instances, disks, and primary ENIs created by using this version. Valid values of N: 1 to 20. If you specify this parameter, it can be an empty string. The tag value can be up to 128 characters in length and cannot contain http:// or https://.
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

class CreateLaunchTemplateVersionRequestSecurityOptions(DaraModel):
    def __init__(
        self,
        trusted_system_mode: str = None,
    ):
        # The trusted system mode. Valid values: vTPM.
        # 
        # Currently, the trusted system mode supports the following instance families:
        # - g7, c7, and r7.
        # - Security-enhanced instance families (g7t, c7t, and r7t).
        # 
        # When you create an ECS instance of the preceding instance families, you must configure the settings for this parameter. Details:
        # 
        # - If you use the Alibaba Cloud trusted system, set this parameter to vTPM. This way, the Alibaba Cloud trusted system performs trusted verification when the instance starts.
        # - If you do not use the Alibaba Cloud trusted system, you can leave this parameter empty. However, if the ECS instance that you create uses the Enclave-based confidential computing mode (`SecurityOptions.ConfidentialComputingMode=Enclave`), the trusted system is also enabled for the instance.
        # - To create a trusted ECS instance by invoking an API operation, you can only invoke the `RunInstances` operation. The `CreateInstance` operation does not support the `SecurityOptions.TrustedSystemMode` parameter.
        # > If you specify an instance as a trusted instance when you create it, you can only use images that support the trusted system when you replace the system disk.
        # 
        # For more information about the trusted system, see [Overview of the trusted feature for security-enhanced instances](https://help.aliyun.com/document_detail/201394.html).
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

class CreateLaunchTemplateVersionRequestNetworkInterface(DaraModel):
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
        # - true: Do not retain the ENI.
        # 
        # - false: Retain the ENI.
        # 
        # Default value: true.
        # 
        # > This parameter takes effect only for secondary ENIs.
        self.delete_on_release = delete_on_release
        # The description of the secondary elastic network interface controller (NIC). The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`. The value of N in `NetworkInterface.N` cannot be greater than 1.
        self.description = description
        # The Elastic Network Interface (ENI) type. Valid values of N: 1 and 2. If N is set to 1, you can configure one primary ENI or one secondary ENI. If N is set to 2, you must configure one primary ENI and one secondary ENI.
        # 
        # Valid values:
        # 
        # - Primary: primary ENI
        # - Secondary: secondary ENI
        # 
        # Default value: Secondary.
        self.instance_type = instance_type
        # The name of the secondary elastic network interface controller (NIC). The value of N in `NetworkInterface.N` cannot be greater than 1.
        self.network_interface_name = network_interface_name
        # The communication mode of the primary ENI. Valid values:
        # 
        # - Standard: uses the TCP communication mode.
        # - HighPerformance: enables the Elastic RDMA Interface (ERI) and uses the RDMA communication mode.
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # The primary private IP address of the secondary elastic network interface controller (NIC). The value of N in `NetworkInterface.N` cannot be greater than 1.
        self.primary_ip_address = primary_ip_address
        # The ID of the security group to which the secondary elastic network interface controller (NIC) belongs. The security group of the secondary elastic network interface controller (NIC) and the security group of the instance must be in the same VPC. The value of N in `NetworkInterface.N` cannot be greater than 1.
        # 
        # > You cannot specify both `NetworkInterface.N.SecurityGroupId` and `NetworkInterface.N.SecurityGroupIds.N`.
        self.security_group_id = security_group_id
        # The IDs of one or more security groups to which the secondary elastic network interface controller (NIC) belongs. The security groups and the secondary elastic network interface controller (NIC) must be in the same VPC. The valid values of N in `SecurityGroupIds.N` depend on the quota of security groups to which the secondary elastic network interface controller (NIC) can be added. For more information, see [Limits](https://help.aliyun.com/document_detail/25412.html). The value of N in `NetworkInterface.N` cannot be greater than 1.
        # 
        # > You cannot specify both `NetworkInterface.N.SecurityGroupId` and `NetworkInterface.N.SecurityGroupIds.N`.
        self.security_group_ids = security_group_ids
        # The ID of the vSwitch to which the secondary elastic network interface controller (NIC) belongs. The instance and the secondary elastic network interface controller (NIC) must be in the same active zone of the same VPC, but they can belong to different vSwitches. The value of N in `NetworkInterface.N` cannot be greater than 1.
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

class CreateLaunchTemplateVersionRequestImageOptions(DaraModel):
    def __init__(
        self,
        login_as_non_root: bool = None,
    ):
        # Specifies whether instances that use this image support logons by the ecs-user user. Valid values:
        # - true: Yes.
        # - false: No.
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

class CreateLaunchTemplateVersionRequestDataDisk(DaraModel):
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
        # Specifies whether to enable performance burst. Valid values:
        # 
        # - true
        # - false
        self.bursting_enabled = bursting_enabled
        # The category of data disk N. Valid values:
        # 
        # - cloud_efficiency: ultra disk
        # - cloud_ssd: standard SSD
        # - cloud_essd: ESSD
        # - cloud: basic disk
        # - cloud_auto: ESSD AutoPL disk
        # - cloud_regional_disk_auto: regional ESSD
        # - cloud_essd_entry: ESSD Entry disk
        #   > The `cloud_essd_entry` value is supported only when `InstanceType` is set to an instance type in the `ecs.u1` or `ecs.e` family.
        # - elastic_ephemeral_disk_standard: standard elastic ephemeral disk
        # - elastic_ephemeral_disk_premium: Premium Edition elastic ephemeral disk
        # 
        # Default value: cloud_efficiency for I/O optimization instances, and cloud for non-I/O optimization instances.
        # Parameter default value description:
        # 
        # - If the instance type is a retired instance type that is not I/O optimization, the default value is `cloud`.
        # - In other cases, the default value is `cloud_efficiency`.<props="china"> After January 30, 2026, if the I/O optimization instance type does not support cloud_auto, the default value is cloud_efficiency. Otherwise, the default value is cloud_auto, and performance burst is enabled by default, which incurs additional fees. For more details, see [Billing examples](~~368372#p_75k_2hp_7gp~~) and [Announcement on changes](https://www.aliyun.com/notice/117844).
        self.category = category
        # Specifies whether to release the data disk when the instance is released. Valid values:
        # 
        # - true: Release the data disk when the instance is released.
        # - false: Do not release the data disk when the instance is released.
        # 
        # Default value: true.
        self.delete_with_instance = delete_with_instance
        # The description of the data disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The mount point of the data disk. The naming conventions for mount points vary based on the number of attached data disks:
        # - 1 to 25 data disks: /dev/xvd`[b-z]`
        # 
        # - More than 25 data disks: /dev/xvd`[aa-zz]`. For example, the 26th data disk is named /dev/xvdaa, and the 27th data disk is named /dev/xvdab.
        # 
        # > This parameter is applicable only to full images. You can set this parameter to the mount point of the data disk in the full image and modify the `DataDisk.N.Size` and `DataDisk.N.Category` parameters to change the category and size of the data disk in the full image.
        self.device = device
        # The name of the data disk. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with `http://` or `https://`. It can contain digits, colons (:), underscores (_), and hyphens (-).
        self.disk_name = disk_name
        # Specifies whether to encrypt the data disk.
        self.encrypted = encrypted
        # The ID of the Key Management Service (KMS) key used by the data disk.
        self.kmskey_id = kmskey_id
        # The performance level settings of the ESSD used as the data disk. The value of N must be the same as that in `DataDisk.N.Category=cloud_essd`. Valid values:
        # 
        # - PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # - PL1 (default): A single ESSD can deliver up to 50,000 random read/write IOPS.
        # - PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # - PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        # 
        # For more details about how to select the performance level of an ESSD, see [ESSD](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The number of provisioned read/write IOPS for the ESSD AutoPL disk. Valid values: 0 to min{50000, 1000 × Capacity - Baseline performance}.
        # 
        # Baseline performance = min{1800 + 50 × Capacity, 50000}.
        # 
        # > This parameter is supported only when DiskCategory is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html) and [Modify the provisioned performance of an ESSD AutoPL disk](https://help.aliyun.com/document_detail/413275.html).
        self.provisioned_iops = provisioned_iops
        # The size of data disk N. Valid values of N: 1 to 16. Unit: GiB. Valid values:
        # 
        # -   cloud: 5 to 2000
        # -   cloud_efficiency: 20 to 32768
        # -   cloud_ssd: 20 to 32768
        # -   cloud_essd: The valid values are subject to the value of `DataDisk.N.PerformanceLevel`.   
        #     - PL0: 1 to 32768
        #     - PL1: 20 to 32768
        #     - PL2: 461 to 32768
        #     - PL3: 1261 to 32768
        # -   cloud_auto: 1 to 32768
        # -   cloud_essd_entry: 10 to 32768
        # 
        # The value of this parameter must be greater than or equal to the size of the snapshot specified by the `SnapshotId` parameter.
        self.size = size
        # The ID of the snapshot used to create data disk N. Valid values of N: 1 to 16. When the `DataDisk.N.SnapshotId` parameter is specified, the `DataDisk.N.Size` parameter is ignored. The size of the created disk is the same as that of the specified snapshot.
        # 
        # You cannot use snapshots that were created on or before July 15, 2013. Otherwise, an error is returned and your request is rejected.
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

class CreateLaunchTemplateVersionRequestSystemDisk(DaraModel):
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
        # Specifies whether to enable performance burst. Valid values:
        # 
        # - true
        # - false
        self.bursting_enabled = bursting_enabled
        # The category of the system disk. Valid values:
        # 
        # -   cloud: basic disk
        # -   cloud_efficiency: ultra disk
        # -   cloud_ssd: standard SSD
        # -   cloud_auto: ESSD AutoPL disk
        # -   cloud_essd: ESSD. You can use the `SystemDisk.PerformanceLevel` parameter for the performance level settings of the disk.
        # -   cloud_essd_entry: ESSD Entry disk
        # 
        # Default value: cloud for retired instance types that are not I/O optimization instances, and cloud_efficiency for other instance types.
        self.category = category
        # Specifies whether to release the system disk when the instance is released. Valid values:
        # 
        # - true: Release the system disk when the instance is released.
        # - false: Do not release the system disk when the instance is released.
        # 
        # Default value: true.
        self.delete_with_instance = delete_with_instance
        # The description of the system disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The name of the system disk. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with `http://` or `https://`. It can contain digits, colons (:), underscores (_), and hyphens (-).
        self.disk_name = disk_name
        # Specifies whether to encrypt the system disk. Valid values:
        # 
        # - true: Encrypts the system disk.
        # 
        # - false: Does not encrypt the system disk.
        # 
        # Default value: false.
        # 
        # > You cannot encrypt the system disk when you create an instance in Hong Kong (China) Zone D or Singapore Zone A.
        self.encrypted = encrypted
        # > This parameter is not available.
        self.iops = iops
        # The KMS key ID of the system disk.
        self.kmskey_id = kmskey_id
        # The performance level settings of the ESSD used as the system disk. Valid values:
        # 
        # - PL0 (default): A single ESSD can deliver up to 10,000 random read/write IOPS.
        # - PL1: A single ESSD can deliver up to 50,000 random read/write IOPS.
        # - PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # - PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        # 
        # For more details about how to select the performance level of an ESSD, see [ESSD](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The number of provisioned read/write IOPS for the ESSD AutoPL disk. Valid values: 0 to min{50000, 1000 × Capacity - Baseline performance}.
        # 
        # Baseline performance = min{1800 + 50 × Capacity, 50000}.
        # 
        # > This parameter is supported only when DiskCategory is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html) and [Modify the provisioned performance of an ESSD AutoPL disk](https://help.aliyun.com/document_detail/413275.html).
        self.provisioned_iops = provisioned_iops
        # The size of the system disk. Unit: GiB. Valid values:
        # 
        # - cloud: 20 to 500
        # - Other disk categories: 20 to 2048
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

