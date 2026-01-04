# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class RunInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_release_time: str = None,
        auto_renew: bool = None,
        auto_use_coupon: str = None,
        billing_cycle: str = None,
        carrier: str = None,
        data_disk_shrink: str = None,
        deletion_protection: bool = None,
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
        system_disk_shrink: str = None,
        tag: List[main_models.RunInstancesShrinkRequestTag] = None,
        unique_suffix: bool = None,
        user_data: str = None,
        v_switch_id: str = None,
    ):
        # The number of instances that you want to create. Valid values: 1 to 100.
        self.amount = amount
        # The time when to automatically release the pay-as-you-go instance. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in Coordinated Universal Time (UTC).
        # 
        # *   If the value of `ss` is not `00`, the start time is automatically rounded down to the nearest minute based on the value of `mm`.
        # *   The specified time must be at least one hour later than the current time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.auto_release_time = auto_release_time
        # Specifies whether to enable auto-renewal for the premium bandwidth plan. Valid values:
        # 
        # *   **true**.
        # *   **false** (default).
        # 
        # >  This parameter is not available when InstanceChargeType is set to PostPaid.
        self.auto_renew = auto_renew
        # Specifies whether to use coupons. Default value: true.
        self.auto_use_coupon = auto_use_coupon
        # The billing cycle of computing resources of the instance. Only pay-as-you-go instances are supported. Valid values:
        # 
        # *   **Day**.
        # *   **Month**.
        self.billing_cycle = billing_cycle
        # The Internet service provider (ISP).
        # 
        # >  This parameter required if ScheduleAreaLevel is set to Region.\\
        # If you set ScheduleAreaLevel to Region, a node has multiple ISPs, and you do not specify an ISP, then the create instance uses the ISP of the node. If the node has two ISPs, such as China Mobile and China Unicom, the created instance has two ISPs.\\
        # You can call the DescribeRegionIsps operation to query ISPs of the edge node.[](~~2637461~~)
        self.carrier = carrier
        # The specifications of data disks.
        self.data_disk_shrink = data_disk_shrink
        self.deletion_protection = deletion_protection
        # The ID of the node.
        # 
        # >  This parameter is required if ScheduleAreaLevel is set to Region and is not available if ScheduleAreaLevel is set to other values.
        self.ens_region_id = ens_region_id
        # The name of the host.
        self.host_name = host_name
        # The ID of the image. For ARM PCB-based server instances, leave this parameter empty. For other instances, this parameter is required.
        self.image_id = image_id
        # The billing policy of the instance. Valid values:
        # 
        # *   **instance**: Bills are generated based on instances.
        # *   If you do not specify this parameter, bills are generated based on users.
        self.instance_charge_strategy = instance_charge_strategy
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription.
        # *   **PostPaid:** pay-as-you-go.
        self.instance_charge_type = instance_charge_type
        # The name of the instance. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with `http://` or `https://`. It can contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # The default value of this parameter is the value of the InstanceId parameter.
        self.instance_name = instance_name
        # The instance type.
        self.instance_type = instance_type
        # The bandwidth billing method. Valid values:
        # 
        # *   **BandwidthByDay**: pay by daily peak bandwidth
        # *   **95BandwidthByMonth**: pay by monthly 95th percentile bandwidth
        # 
        # >  This parameter is required if you purchase an ENS instance for the first time. The value that you specified is used as the default value for subsequent purchases.
        self.internet_charge_type = internet_charge_type
        # The maximum public bandwidth. If the value of this parameter is greater than 0, a public IP address is assigned to the instance.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The type of the IP address. Valid values:
        # 
        # *   **ipv4** (default).
        # *   **ipv6**.
        # *   **ipv4Andipv6** (single stack).
        # *   **ipv4Withipv6** (dual stack).
        self.ip_type = ip_type
        self.ipv_6address_count = ipv_6address_count
        # The name of the key pair.
        # 
        # >  You need to specify at least one of **Password**, **KeyPairName**, and **PasswordInherit**.
        self.key_pair_name = key_pair_name
        self.launch_template_id = launch_template_id
        self.launch_template_name = launch_template_name
        self.launch_template_version = launch_template_version
        # The code of the region.
        # 
        # >  This parameter is not available if ScheduleAreaLevel is set to Region and is required if ScheduleAreaLevel is set to other values.
        self.net_district_code = net_district_code
        # The ID of the network.
        # 
        # >  This parameter is available only if ScheduleAreaLevel is set to Region and cannot be configured if ScheduleAreaLevel is set to other values. Otherwise, an error occurs.
        self.net_work_id = net_work_id
        # The password that is used to connect to the instance.
        # 
        # >  You need to specify at least one of **Password**, **KeyPairName**, and **PasswordInherit**.
        self.password = password
        # Specifies whether to use the preset password of the image. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  You need to specify at least one of **Password**, **KeyPairName**, and **PasswordInherit**.
        self.password_inherit = password_inherit
        # The unit of the subscription period.
        # 
        # *   If **PeriodUnit** is set to **Day**, **Period** can only be set to **3**.
        # *   If **PeriodUnit** is **Month**, **Period** can be set to **1 to 9** or **12**.
        self.period = period
        # The unit of the subscription period. Valid values:
        # 
        # *   **Month** (default).
        # *   **Day**.
        self.period_unit = period_unit
        # The private IP address.
        # 
        # >  This parameter is available only if ScheduleAreaLevel is set to Region and cannot be configured if ScheduleAreaLevel is set to other values. Otherwise, an error occurs. If you specify a private IP address, the number of instances must be 1. The private IP address takes effect only when the private IP address and the vSwitch ID are not empty.
        self.private_ip_address = private_ip_address
        # Specifies whether to enable public IP address identification. Valid values: true and false. Default value: false.
        self.public_ip_identification = public_ip_identification
        # The scheduling level. This parameter specifies area-level scheduling or node-level scheduling. Valid values:
        # 
        # *   **Big**: greater area
        # *   **Middle**: province
        # *   **Small**: city
        # *   **Region**: node
        self.schedule_area_level = schedule_area_level
        # The scheduling price policy. Valid values:
        # 
        # *   **PriceHighPriority**: The high price prevails.
        # *   **PriceLowPriority**: The low price prevails.
        self.scheduling_price_strategy = scheduling_price_strategy
        # The scheduling policy of the taint. Valid values:
        # 
        # *   **Concentrate**
        # *   **Disperse**
        # 
        # >  If ScheduleAreaLevel is set to Region, set this parameter to **Concentrate**. If ScheduleAreaLevel is set to other values, set this parameter to Concentrate or Disperse based on your business requirements.
        self.scheduling_strategy = scheduling_strategy
        # The ID of security group.
        self.security_id = security_id
        # The protection period of the preemptible instance. Unit: hours. Default value: 1. Valid values:
        # 
        # *   1: After a preemptible instance is created, Alibaba Cloud ensures that the instance is not automatically released within 1 hour. After the 1-hour protection period ends, the system compares the bid price with the market price and checks the resource inventory to determine whether to retain or release the instance.
        # *   0: After a preemptible instance is created, Alibaba Cloud does not ensure that the instance runs for 1 hour. The system compares the bid price with the market price and checks the resource inventory to determine whether to retain or release the instance.
        # 
        # Alibaba Cloud sends an ECS system event to notify you 5 minutes before the instance is released. Preemptible instances are billed by second. We recommend that you specify an appropriate protection period based on your business requirements.
        self.spot_duration = spot_duration
        # The bidding policy for the pay-as-you-go instance. This parameter is valid only when the `InstanceChargeType` parameter is set to `PostPaid`. Valid values:
        # 
        # *   NoSpot: The elastic container instances are pay-as-you-go instances.
        # *   SpotAsPriceGo: The instance is a preemptible instance for which the market price at the time of purchase is automatically used as the bidding price.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy
        # The specification of the system disk.
        self.system_disk_shrink = system_disk_shrink
        # The tags.
        self.tag = tag
        # Specifies whether to append sequential suffixes to the hostname specified by the **HostName** parameter and to the instance name specified by the **InstanceName** parameter. The sequential suffixes range from 001 to 999.
        self.unique_suffix = unique_suffix
        # The custom data. The maximum data size is 16 KB. You can specify **UserData**. **UserData** must be Base64-encoded.
        self.user_data = user_data
        # The ID of the vSwitch.
        # 
        # >  This parameter is available only if ScheduleAreaLevel is set to Region and cannot be configured if ScheduleAreaLevel is set to other values. Otherwise, an error occurs.
        self.v_switch_id = v_switch_id

    def validate(self):
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

        if self.data_disk_shrink is not None:
            result['DataDisk'] = self.data_disk_shrink

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

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

        if self.system_disk_shrink is not None:
            result['SystemDisk'] = self.system_disk_shrink

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

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

        if m.get('DataDisk') is not None:
            self.data_disk_shrink = m.get('DataDisk')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

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
            self.system_disk_shrink = m.get('SystemDisk')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.RunInstancesShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UniqueSuffix') is not None:
            self.unique_suffix = m.get('UniqueSuffix')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class RunInstancesShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

