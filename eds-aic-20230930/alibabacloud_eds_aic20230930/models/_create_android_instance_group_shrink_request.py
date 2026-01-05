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
        ipv_6bandwidth: int = None,
        key_pair_id: str = None,
        network_info_shrink: str = None,
        network_type: str = None,
        number_of_instances: int = None,
        office_site_id: str = None,
        period: int = None,
        period_unit: str = None,
        policy_group_id: str = None,
        promotion_id: str = None,
        stream_mode: int = None,
        tag: List[main_models.CreateAndroidInstanceGroupShrinkRequestTag] = None,
        v_switch_id: str = None,
    ):
        # The number of instance groups. Default value: 1. Maximum value: 1.
        self.amount = amount
        # Specifies whether to enable automatic payment. Default value: false.
        # 
        # Valid values:
        # 
        # *   true: enables automatic payment. Make sure that your Alibaba Cloud account has sufficient balance.
        # *   false: disables automatic payment. You must manually complete the payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. Default value: false.
        # 
        # Valid values:
        # 
        # *   true: automatically renew resource upon expiration.
        # *   false: manually renew resources upon expiration.
        self.auto_renew = auto_renew
        self.bandwidth_package_id = bandwidth_package_id
        self.bandwidth_package_type = bandwidth_package_type
        # The ID of the region. You can call the DescribeRegions operation to query the regions where Cloud Phone is supported.
        # 
        # Valid values:
        # 
        # *   cn-shenzhen: China (Shenzhen).
        # *   cn-beijing: China (Beijing).
        # *   cn-shanghai: China (Shanghai).
        # *   cn-hongkong: China (Hong Kong).
        # *   ap-southeast-1: Singapore.
        # *   cn-hangzhou: China (Hangzhou).
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go.
        # *   PrePaid: subscription.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request. The value cannot exceed 100 characters in length.
        self.client_token = client_token
        # >  This parameter is not publicly available.
        self.enable_ipv_6 = enable_ipv_6
        # Specifies whether to enable GPU acceleration.
        # 
        # Valid values:
        # 
        # *   true: enables GPU acceleration.
        # *   false (default): disables GPU acceleration.
        self.gpu_acceleration = gpu_acceleration
        # The ID of the image. You can call the [DescribeImageList](https://help.aliyun.com/document_detail/2807324.html) operation to query images.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The name of the instance group.
        # 
        # >  The name can be up to 30 characters in length. It can contain letters, digits, colons (:), underscores (_), periods (.), or hyphens (-). It must start with letters but cannot start with `http://` or `https://`.
        self.instance_group_name = instance_group_name
        # The specifications of the instance group. You can call the [DescribeSpec](https://help.aliyun.com/document_detail/2807299.html) operation to query the available specifications.
        # 
        # Valid values:
        # 
        # *   acp.perf.large: Performance (8 vCPUs, 16 GiB of memory, and 32 GiB of storage.
        # *   acp.basic.small: Lightweight (2 vCPUs, 4 GiB of memory, and 32 GiB of storage).
        # *   acp.std.large: Standard (4 vCPUs, 8 GiB of memory, and 32 GiB of storage).
        # 
        # This parameter is required.
        self.instance_group_spec = instance_group_spec
        # >  This parameter is not publicly available.
        self.ipv_6bandwidth = ipv_6bandwidth
        # The ID of the key pair. When you create an instance group and specify a valid key pair ID, all cloud phone instances within the group will automatically be bound to that key pair upon creation. This eliminates the need to manually bind key pairs to individual cloud phone instances.
        # 
        # >  Binding key pairs to cloud phone instances is currently not supported during instance group resizing.
        self.key_pair_id = key_pair_id
        self.network_info_shrink = network_info_shrink
        self.network_type = network_type
        # The number of cloud phones in the instance group. Maximum value: 100.
        self.number_of_instances = number_of_instances
        # The ID of the network.
        # 
        # *   This parameter is required if you assign a shared network to cloud phones. You can go to the [Network](https://wya.wuying.aliyun.com/network) page of the Cloud Phone console to retrieve the ID of a **shared network**. If no shared network is available in the Cloud Phone console, you can leave this parameter empty. The system automatically creates one when you create an instance group.
        # *   This parameter is required if you assign a virtual private cloud (VPC) to cloud phones. You can go to the [Network](https://wya.wuying.aliyun.com/network) page of the Cloud Phone console to retrieve the ID of a **VPC**. If no VPC is available in the Cloud Phone console, you must first create one.
        self.office_site_id = office_site_id
        # The subscription duration. The unit is specified by PeriodUnit.
        self.period = period
        # The unit of the subscription duration.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        # *   Hour (Note that this unit is supported only by pay-as-you-go.)
        self.period_unit = period_unit
        # The ID of the policy. You can call the [ListPolicyGroups](https://help.aliyun.com/document_detail/2807352.html) operation to query policies.
        self.policy_group_id = policy_group_id
        self.promotion_id = promotion_id
        self.stream_mode = stream_mode
        # The tags
        self.tag = tag
        # The ID of the vSwitch. You can call the [DescribeVSwitches](https://help.aliyun.com/document_detail/448774.html) operation to query vSwitches.
        # 
        # *   This parameter is not required if you assign a shared network to cloud phones.
        # *   This parameter is required if you assign a VPC to cloud phones. The vSwitch specified by this parameter is used to create cloud phones.
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

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

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

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

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

