# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class CreateAndroidInstanceGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        bandwidth_package_id: str = None,
        bandwidth_package_type: str = None,
        biz_region_id: str = None,
        charge_type: str = None,
        client_token: str = None,
        enable_ipv_6: bool = None,
        gpu_acceleration: bool = None,
        image_id: str = None,
        instance_group_name: str = None,
        instance_group_spec: str = None,
        instance_version: str = None,
        ipv_6bandwidth: int = None,
        key_pair_id: str = None,
        network_info_shrink: str = None,
        network_type: str = None,
        number_of_instances: int = None,
        office_site_id: str = None,
        paid_call_back_url: str = None,
        period: int = None,
        period_unit: str = None,
        policy_group_id: str = None,
        promotion_id: str = None,
        sale_mode: str = None,
        stream_mode: int = None,
        tag: List[main_models.CreateAndroidInstanceGroupShrinkRequestTag] = None,
        v_switch_id: str = None,
    ):
        # The number of instance groups to create. Valid values: 1 to 100. Default value: 1.
        self.amount = amount
        # Specifies whether to enable automatic payment. Default value: false.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for subscription resources. Default value: false.
        self.auto_renew = auto_renew
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth_package_type = bandwidth_package_type
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the regions where Cloud Phone instances are available.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The billing method.
        self.charge_type = charge_type
        # A client-generated token to ensure request idempotence. This parameter prevents duplicate requests. The token can be up to 100 characters in length.
        self.client_token = client_token
        # > This parameter is not publicly available.
        self.enable_ipv_6 = enable_ipv_6
        # Specifies whether to enable GPU acceleration.
        self.gpu_acceleration = gpu_acceleration
        # The image ID. You can call the [DescribeImageList](~~DescribeImageList~~) operation to query available images for Cloud Phone instances.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The name of the instance group.
        # 
        # > The name can be up to 30 characters in length. It must start with an uppercase or lowercase letter or a Chinese character, and cannot start with `http://` or `https://`. The name can contain only Chinese characters, letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        self.instance_group_name = instance_group_name
        # The instance group specification. You can call the [DescribeSpec](~~DescribeSpec~~) operation to query the specifications that are available for Cloud Phone instances.
        # 
        # This parameter is required.
        self.instance_group_spec = instance_group_spec
        self.instance_version = instance_version
        # > This parameter is not publicly available.
        self.ipv_6bandwidth = ipv_6bandwidth
        # The key pair ID. If you specify a valid key pair ID when you create the instance group, the system attaches the key pair to all successfully created instances. No separate API call is required to attach the key pair.
        # 
        # > Attaching a key pair during a scale-out operation is not supported.
        self.key_pair_id = key_pair_id
        self.network_info_shrink = network_info_shrink
        self.network_type = network_type
        # The number of instances in the instance group. The maximum value is 100.
        self.number_of_instances = number_of_instances
        # The network ID.
        # 
        # - To create instances in a Shared Network: This parameter is optional. Specify the ID of a **Shared Network**. You can find the ID on the [Cloud Phone console > Network](https://wya.wuying.aliyun.com/network) page. If no Shared Network is available in the console, you can omit this parameter. The system automatically creates a Shared Network when you create the instance group.
        # 
        # - To create instances in a VPC: This parameter is required. Specify the ID of a **VPC**. You can find the ID on the [Cloud Phone console > Network](https://wya.wuying.aliyun.com/network) page. If no VPC is available in the console, you must create one first.
        self.office_site_id = office_site_id
        self.paid_call_back_url = paid_call_back_url
        # The subscription duration. The PeriodUnit parameter specifies the unit.
        self.period = period
        # The unit of the subscription duration.
        self.period_unit = period_unit
        # The policy ID. You can call the [ListPolicyGroups](~~ListPolicyGroups~~) operation to query available policies.
        self.policy_group_id = policy_group_id
        self.promotion_id = promotion_id
        self.sale_mode = sale_mode
        self.stream_mode = stream_mode
        # The resource tags.
        self.tag = tag
        # The vSwitch ID. You can call the [DescribeVSwitches](https://help.aliyun.com/document_detail/448774.html) operation to query available vSwitches.
        # 
        # - If you create instances in a Shared Network, omit this parameter.
        # 
        # - If you create instances in a VPC, this parameter is required. The system creates the instances in the specified vSwitch.
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

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id

        if self.bandwidth_package_type is not None:
            result['BandwidthPackageType'] = self.bandwidth_package_type

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_ipv_6 is not None:
            result['EnableIpv6'] = self.enable_ipv_6

        if self.gpu_acceleration is not None:
            result['GpuAcceleration'] = self.gpu_acceleration

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_group_name is not None:
            result['InstanceGroupName'] = self.instance_group_name

        if self.instance_group_spec is not None:
            result['InstanceGroupSpec'] = self.instance_group_spec

        if self.instance_version is not None:
            result['InstanceVersion'] = self.instance_version

        if self.ipv_6bandwidth is not None:
            result['Ipv6Bandwidth'] = self.ipv_6bandwidth

        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id

        if self.network_info_shrink is not None:
            result['NetworkInfo'] = self.network_info_shrink

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.number_of_instances is not None:
            result['NumberOfInstances'] = self.number_of_instances

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.paid_call_back_url is not None:
            result['PaidCallBackUrl'] = self.paid_call_back_url

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.sale_mode is not None:
            result['SaleMode'] = self.sale_mode

        if self.stream_mode is not None:
            result['StreamMode'] = self.stream_mode

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')

        if m.get('BandwidthPackageType') is not None:
            self.bandwidth_package_type = m.get('BandwidthPackageType')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableIpv6') is not None:
            self.enable_ipv_6 = m.get('EnableIpv6')

        if m.get('GpuAcceleration') is not None:
            self.gpu_acceleration = m.get('GpuAcceleration')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceGroupName') is not None:
            self.instance_group_name = m.get('InstanceGroupName')

        if m.get('InstanceGroupSpec') is not None:
            self.instance_group_spec = m.get('InstanceGroupSpec')

        if m.get('InstanceVersion') is not None:
            self.instance_version = m.get('InstanceVersion')

        if m.get('Ipv6Bandwidth') is not None:
            self.ipv_6bandwidth = m.get('Ipv6Bandwidth')

        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')

        if m.get('NetworkInfo') is not None:
            self.network_info_shrink = m.get('NetworkInfo')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('NumberOfInstances') is not None:
            self.number_of_instances = m.get('NumberOfInstances')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PaidCallBackUrl') is not None:
            self.paid_call_back_url = m.get('PaidCallBackUrl')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('SaleMode') is not None:
            self.sale_mode = m.get('SaleMode')

        if m.get('StreamMode') is not None:
            self.stream_mode = m.get('StreamMode')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateAndroidInstanceGroupShrinkRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class CreateAndroidInstanceGroupShrinkRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

