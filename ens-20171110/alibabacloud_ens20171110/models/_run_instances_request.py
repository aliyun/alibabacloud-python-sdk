# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class RunInstancesRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_install_cloud_assistant: bool = None,
        auto_release_time: str = None,
        auto_renew: bool = None,
        auto_use_coupon: str = None,
        billing_cycle: str = None,
        carrier: str = None,
        cloud_assistant_region: str = None,
        data_disk: List[main_models.RunInstancesRequestDataDisk] = None,
        deletion_protection: bool = None,
        deployment_set_id: str = None,
        ens_region_id: str = None,
        host_name: str = None,
        image_id: str = None,
        instance_charge_strategy: str = None,
        instance_charge_type: str = None,
        instance_name: str = None,
        instance_type: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_out: int = None,
        ip_type: str = None,
        ipv_6address_count: int = None,
        key_pair_name: str = None,
        launch_template_id: str = None,
        launch_template_name: str = None,
        launch_template_version: int = None,
        net_district_code: str = None,
        net_work_id: str = None,
        password: str = None,
        password_inherit: bool = None,
        period: int = None,
        period_unit: str = None,
        private_ip_address: str = None,
        public_ip_identification: bool = None,
        schedule_area_level: str = None,
        scheduling_price_strategy: str = None,
        scheduling_strategy: str = None,
        security_id: str = None,
        spot_duration: int = None,
        spot_strategy: str = None,
        system_disk: main_models.RunInstancesRequestSystemDisk = None,
        tag: List[main_models.RunInstancesRequestTag] = None,
        unique_suffix: bool = None,
        user_data: str = None,
        v_switch_id: str = None,
        vpd_id: str = None,
        vpd_vswitch_ids: List[str] = None,
    ):
        # The number of instances to create. Valid values: 1 to 100.
        self.amount = amount
        # Specifies whether to automatically install the Cloud Assistant client on the instance.
        self.auto_install_cloud_assistant = auto_install_cloud_assistant
        # The automatic release time of the pay-as-you-go instance. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        # 
        # - If the value of seconds (`ss`) is not `00`, the time is automatically set to the start of the current minute (`mm`).
        # 
        # - The earliest release time is one hour after the current time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.auto_release_time = auto_release_time
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # - **true**: enables auto-renewal.
        # - **false**: does not enable auto-renewal. (Default)
        # 
        # >This parameter is invalid for pay-as-you-go instances.
        self.auto_renew = auto_renew
        # Specifies whether to use coupons. Default value: true (AutoUseCoupon=true).
        self.auto_use_coupon = auto_use_coupon
        # The billing cycle for instance compute resources. Only instance-level pay-as-you-go is supported. Valid values:
        # 
        # - **Day**: daily billing.
        # 
        # - **Month**: monthly billing.
        self.billing_cycle = billing_cycle
        # The carrier.
        # >This parameter is required for region-level scheduling.</br>
        # >For node-level scheduling, if a node has multiple carriers and you do not specify a carrier, instances are created for each carrier on the node. For example, if a node has both China Mobile and China Unicom carriers, instances with two ISPs are created.</br>You can call [DescribeRegionIsps](https://help.aliyun.com/document_detail/2637461.html) to query the carrier information of a node.
        self.carrier = carrier
        # The region for Cloud Assistant access. Valid values: cn-zhangjiakou (Zhangjiakou) and ap-southeast-1 (Singapore).
        self.cloud_assistant_region = cloud_assistant_region
        # The data cloud disk specifications.
        self.data_disk = data_disk
        # The release protection property of the instance. Specifies whether the instance can be released from the console or by calling an API operation. Valid values: 
        # 
        # -  true: Enables instance release protection.
        # -  false: Disables instance release protection.
        # 
        # Default value: false.
        # 
        # > This property applies only to pay-as-you-go instances and can only restrict manual release operations. It does not take effect on system-initiated release operations.
        self.deletion_protection = deletion_protection
        # The deployment set ID.
        self.deployment_set_id = deployment_set_id
        # The node ID.
        # 
        # > This parameter is required for node-level scheduling and is invalid for region-level scheduling.
        self.ens_region_id = ens_region_id
        # The hostname.
        self.host_name = host_name
        # The image ID. This parameter cannot be specified for ARM-based instances. This parameter is required for other instance types.
        self.image_id = image_id
        # The instance billing strategy. Valid values:
        # 
        # - **instance**: instance-level billing.
        # - If not specified, the default is user-level billing.
        self.instance_charge_strategy = instance_charge_strategy
        # The billing method of the instance. Valid values:
        # - **PrePaid**: subscription.
        # - **PostPaid**: pay-as-you-go.
        self.instance_charge_type = instance_charge_type
        # The instance name. The name must be 2 to 128 characters in length and must start with a letter or Chinese character. It cannot start with `http://` or `https://`. It can contain Chinese characters, letters, digits, colons (:), underscores (_), periods (.), or hyphens (-).
        # 
        # Default value: the InstanceId of the instance.
        self.instance_name = instance_name
        # The instance type.
        self.instance_type = instance_type
        # Billable methods for bandwidth. Valid values:
        # - **BandwidthByDay**: daily peak bandwidth
        # - **95BandwidthByMonth**: monthly 95th percentile bandwidth
        # 
        # > You can select a billing method only for the first purchase. Subsequent purchases use the billing method selected during the first purchase by default.
        self.internet_charge_type = internet_charge_type
        # The maximum public bandwidth. If the value of this parameter is greater than 0, a public IP address is automatically assigned to the instance.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The IP type. Valid values:
        # 
        # - **ipv4** (default): IPv4.
        # 
        # - **ipv6**: IPv6.
        # 
        # - **ipv4Andipv6**: IPv4 and IPv6 (single stack).
        # - **ipv4Withipv6**: IPv4 and IPv6 (dual-stack).
        self.ip_type = ip_type
        # The number of randomly generated IPv6 addresses to assign to the primary ENI of the private network.
        self.ipv_6address_count = ipv_6address_count
        # The key pair name.
        # > Specify at least one of **Password**, **KeyPairName**, and **PasswordInherit**.
        self.key_pair_name = key_pair_name
        # The ID of the instance launch template.
        self.launch_template_id = launch_template_id
        # The name of the instance launch template.
        self.launch_template_name = launch_template_name
        # The version of the instance launch template.
        self.launch_template_version = launch_template_version
        # The region code.
        # >This parameter is required for region-level scheduling and is invalid for node-level scheduling.
        self.net_district_code = net_district_code
        # The network ID.
        # 
        # >This parameter can only be used for node-level scheduling. An error is returned if this parameter is specified for region-level scheduling. If you do not specify vSwitch information, only the validity of the network ID is verified. The actual resource creation does not use this network ID.
        self.net_work_id = net_work_id
        # The instance password.
        # 
        # > Specify at least one of **Password**, **KeyPairName**, and **PasswordInherit**.
        self.password = password
        # Specifies whether to use the preset password of the image. Valid values:
        # 
        # - **true**: uses the preset password.
        # - **false**: does not use the preset password.
        # 
        # > Specify at least one of **Password**, **KeyPairName**, and **PasswordInherit**.
        self.password_inherit = password_inherit
        # The duration of the purchased resource.
        # 
        # - If **PeriodUnit** is set to **Day**, **Period** can only be set to **3**.
        # 
        # - If **PeriodUnit** is set to **Month**, **Period** can be set to **1-9** or **12**.
        self.period = period
        # The unit of the purchase duration. Valid values:
        # - **Month** (default): monthly purchase.
        # - **Day**: daily purchase.
        self.period_unit = period_unit
        # The private IP address.
        # >This parameter can only be used for node-level scheduling. An error is returned if this parameter is specified for region-level scheduling.
        # If a private IP address is specified, the number of instances can only be 1. The private IP address takes effect only when both the private IP address and vSwitch ID are specified.
        self.private_ip_address = private_ip_address
        # Specifies whether to enable public IP identification. Valid values:
        # 
        # - true: enables public IP identification.
        # 
        # - false: does not enable public IP identification.
        # 
        # Default value: true.
        self.public_ip_identification = public_ip_identification
        # The scheduling level. Use this parameter to specify node-level or region-level scheduling. Valid values:
        # 
        # - **Big**: major area
        # - **Middle**: province
        # - **Small**: city
        # - **Region**: node
        self.schedule_area_level = schedule_area_level
        # The scheduling price strategy. Valid values:
        # 
        # - **PriceHighPriority**: high price first
        # - **PriceLowPriority**: low price first
        self.scheduling_price_strategy = scheduling_price_strategy
        # The scheduling strategy. Valid values:
        # 
        # - **Concentrate**: concentrated
        # - **Disperse**: dispersed
        # 
        # > For node-level scheduling, the value is **Concentrate**. For region-level scheduling, select a value based on your requirements.
        self.scheduling_strategy = scheduling_strategy
        # The security group ID.
        self.security_id = security_id
        # The protection period of the spot instance.
        # 
        # Unit: hours.
        self.spot_duration = spot_duration
        # The bidding policy for the pay-as-you-go instance. This parameter takes effect when the `InstanceChargeType` parameter is set to `PostPaid`. Valid values:
        # 
        # - NoSpot: a regular pay-as-you-go instance.
        # - SpotAsPriceGo: the system automatically bids at the current market price.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy
        # The system cloud disk specifications.
        self.system_disk = system_disk
        # The tags that are bound to the instance.
        self.tag = tag
        # Specifies whether to add sequential suffixes to **HostName** and **InstanceName**. The sequential suffixes start from 001 and cannot exceed 999.
        self.unique_suffix = unique_suffix
        # The custom user data. Maximum size: 16 KB. You can pass in **UserData** information. **UserData** is Base64-encoded.
        self.user_data = user_data
        # The vSwitch ID.
        # 
        # >This parameter can only be used for node-level scheduling. An error is returned if this parameter is specified for region-level scheduling.
        self.v_switch_id = v_switch_id
        # The VPD network ID.
        self.vpd_id = vpd_id
        # The list of VPD vSwitch IDs.
        self.vpd_vswitch_ids = vpd_vswitch_ids

    def validate(self):
        if self.data_disk:
            for v1 in self.data_disk:
                 if v1:
                    v1.validate()
        if self.system_disk:
            self.system_disk.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.auto_install_cloud_assistant is not None:
            result['AutoInstallCloudAssistant'] = self.auto_install_cloud_assistant

        if self.auto_release_time is not None:
            result['AutoReleaseTime'] = self.auto_release_time

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.carrier is not None:
            result['Carrier'] = self.carrier

        if self.cloud_assistant_region is not None:
            result['CloudAssistantRegion'] = self.cloud_assistant_region

        result['DataDisk'] = []
        if self.data_disk is not None:
            for k1 in self.data_disk:
                result['DataDisk'].append(k1.to_map() if k1 else None)

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_charge_strategy is not None:
            result['InstanceChargeStrategy'] = self.instance_charge_strategy

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        if self.launch_template_name is not None:
            result['LaunchTemplateName'] = self.launch_template_name

        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version

        if self.net_district_code is not None:
            result['NetDistrictCode'] = self.net_district_code

        if self.net_work_id is not None:
            result['NetWorkId'] = self.net_work_id

        if self.password is not None:
            result['Password'] = self.password

        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.public_ip_identification is not None:
            result['PublicIpIdentification'] = self.public_ip_identification

        if self.schedule_area_level is not None:
            result['ScheduleAreaLevel'] = self.schedule_area_level

        if self.scheduling_price_strategy is not None:
            result['SchedulingPriceStrategy'] = self.scheduling_price_strategy

        if self.scheduling_strategy is not None:
            result['SchedulingStrategy'] = self.scheduling_strategy

        if self.security_id is not None:
            result['SecurityId'] = self.security_id

        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.unique_suffix is not None:
            result['UniqueSuffix'] = self.unique_suffix

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        if self.vpd_vswitch_ids is not None:
            result['VpdVSwitchIds'] = self.vpd_vswitch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoInstallCloudAssistant') is not None:
            self.auto_install_cloud_assistant = m.get('AutoInstallCloudAssistant')

        if m.get('AutoReleaseTime') is not None:
            self.auto_release_time = m.get('AutoReleaseTime')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')

        if m.get('CloudAssistantRegion') is not None:
            self.cloud_assistant_region = m.get('CloudAssistantRegion')

        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.RunInstancesRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceChargeStrategy') is not None:
            self.instance_charge_strategy = m.get('InstanceChargeStrategy')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        if m.get('LaunchTemplateName') is not None:
            self.launch_template_name = m.get('LaunchTemplateName')

        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')

        if m.get('NetDistrictCode') is not None:
            self.net_district_code = m.get('NetDistrictCode')

        if m.get('NetWorkId') is not None:
            self.net_work_id = m.get('NetWorkId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('PublicIpIdentification') is not None:
            self.public_ip_identification = m.get('PublicIpIdentification')

        if m.get('ScheduleAreaLevel') is not None:
            self.schedule_area_level = m.get('ScheduleAreaLevel')

        if m.get('SchedulingPriceStrategy') is not None:
            self.scheduling_price_strategy = m.get('SchedulingPriceStrategy')

        if m.get('SchedulingStrategy') is not None:
            self.scheduling_strategy = m.get('SchedulingStrategy')

        if m.get('SecurityId') is not None:
            self.security_id = m.get('SecurityId')

        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.RunInstancesRequestSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.RunInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UniqueSuffix') is not None:
            self.unique_suffix = m.get('UniqueSuffix')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        if m.get('VpdVSwitchIds') is not None:
            self.vpd_vswitch_ids = m.get('VpdVSwitchIds')

        return self

class RunInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The custom tag key.
        self.key = key
        # The tag value. The tag value cannot exceed 128 characters in length, and cannot start with `aliyun` or `acs:`, or contain `http://` or `https://`.
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

class RunInstancesRequestSystemDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        size: int = None,
    ):
        # The type of the system cloud disk.
        self.category = category
        # The size of the system cloud disk. Unit: GiB.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class RunInstancesRequestDataDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        encrypted: bool = None,
        kmskey_id: str = None,
        size: int = None,
    ):
        # The disk category. Valid values:
        # - **cloud_efficiency**: ultra cloud disk
        # - **cloud_ssd**: all-flash cloud disk
        # - **local_hdd**: local HDD
        # - **local_ssd**: local SSD
        self.category = category
        # Specifies whether to encrypt the cloud disk. Valid values:
        # 
        # - true: encrypts the cloud disk.
        # 
        # - false (default): does not encrypt the cloud disk.
        self.encrypted = encrypted
        # The ID of the KMS key used by the cloud disk. Valid values:
        # 
        # - true: encrypts the cloud disk.
        # 
        # - false (default): does not encrypt the cloud disk.
        # 
        # > If Encrypted is set to true and KMSKeyId is empty, the default service key is used.
        self.kmskey_id = kmskey_id
        # The size of the data cloud disk. Unit: GiB.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

