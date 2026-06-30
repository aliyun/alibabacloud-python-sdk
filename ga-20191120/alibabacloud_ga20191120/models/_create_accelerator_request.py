# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateAcceleratorRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        auto_use_coupon: str = None,
        bandwidth: int = None,
        bandwidth_billing_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        duration: int = None,
        instance_charge_type: str = None,
        ip_set_config: main_models.CreateAcceleratorRequestIpSetConfig = None,
        name: str = None,
        pricing_cycle: str = None,
        promotion_option_no: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        spec: str = None,
        tag: List[main_models.CreateAcceleratorRequestTag] = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # - **false** (default): Disables automatic payment. After an order is generated, go to the Order Hub to complete the payment.
        # 
        # - **true**: Enables automatic payment. The system automatically completes the payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the instance. Valid values:
        # 
        # - **true**: Yes.
        # 
        # - **false** (default): No.
        self.auto_renew = auto_renew
        # The auto-renewal duration. Unit: month.
        # 
        # Valid values: **1** to **12**. Default value: **1**.
        # 
        # > This parameter is valid only when **AutoRenew** is set to **true**.
        self.auto_renew_duration = auto_renew_duration
        # Specifies whether to automatically apply coupons to your bills. Valid values:
        # 
        # - **true**: Yes.
        # 
        # - **false** (default): No.
        # 
        # > This parameter is valid only when **AutoPay** is set to **true**.
        self.auto_use_coupon = auto_use_coupon
        # The bandwidth of the standard GA instance. Unit: **Mbps**.
        # 
        # Valid values: 200 to 5000.
        # 
        # > This parameter is required and valid only when the access mode of the acceleration area is Anycast.
        self.bandwidth = bandwidth
        # The bandwidth billing method.
        # 
        # - **BandwidthPackage**: Billed by bandwidth plan.
        # 
        # - **CDT**: Billed by data transfer.
        self.bandwidth_billing_type = bandwidth_billing_type
        # A client token that is used to ensure the idempotence of the request.
        # 
        # Generate a parameter value from your client to make sure that the value is unique among different requests. The ClientToken parameter can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the request as the **ClientToken**. The **RequestId** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: Performs a dry run. The system checks the required parameters, request format, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # 
        # - **false** (default): Sends a normal request. If the request passes the check, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The subscription duration.
        # 
        # - If **PricingCycle** is set to **Month**, the valid values for **Duration** are **1** to **9**.
        # 
        # - If **PricingCycle** is set to **Year**, the valid values for **Duration** are **1** to **3**.
        # 
        # > This parameter is required if **InstanceChargeType** (the billing method of the GA instance) is set to **PREPAY** (subscription).
        self.duration = duration
        # The billing method of the GA instance.
        # 
        # - PREPAY (default): subscription.
        # 
        # - POSTPAY: pay-as-you-go.
        self.instance_charge_type = instance_charge_type
        # The configurations of the acceleration area.
        self.ip_set_config = ip_set_config
        # The name of the GA instance.
        # 
        # The name must be 1 to 128 characters in length, start with a letter, and can contain digits, underscores (_), and hyphens (-).
        self.name = name
        # The billing cycle. Valid values:
        # 
        # - **Month**: Billed by month.
        # 
        # - **Year**: Billed by year.
        # 
        # > This parameter is required if **InstanceChargeType** (the billing method of the GA instance) is set to **PREPAY** (subscription).
        self.pricing_cycle = pricing_cycle
        # The coupon code.
        # 
        # > This parameter is available only on the Alibaba Cloud International Website (www\\.alibabacloud.com).
        self.promotion_option_no = promotion_option_no
        # The region ID of the GA instance. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the standard GA instance belongs.
        self.resource_group_id = resource_group_id
        # The instance type of the GA instance. Valid values:
        # 
        # - **1**: Small I
        # 
        # - **2**: Small II
        # 
        # - **3**: Small III
        # 
        # - **5**: Medium I
        # 
        # - **8**: Medium II
        # 
        # - **10**: Medium III
        # 
        # - **20**: Large I
        # 
        # - **30**: Large II
        # 
        # - **40**: Large III
        # 
        # - **50**: Large IV
        # 
        # - **60**: Large V
        # 
        # - **70**: Large VI
        # 
        # - **80**: Large VII
        # 
        # - **90**: Large VIII
        # 
        # - **100**: Super Large I
        # 
        # - **200**: Super Large II
        # 
        # > * Currently, the Large III and higher instance types are available only to users on the whitelist. To use these instance types, contact your account manager.
        # >
        # > * This parameter is required if **InstanceChargeType** (the billing method of the GA instance) is set to **PREPAY** (subscription).
        # 
        # The definitions of different instance types are different. For more information, see [Instance types](https://help.aliyun.com/document_detail/153127.html).
        self.spec = spec
        # The tags of the GA instance.
        self.tag = tag

    def validate(self):
        if self.ip_set_config:
            self.ip_set_config.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.ip_set_config is not None:
            result['IpSetConfig'] = self.ip_set_config.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.spec is not None:
            result['Spec'] = self.spec

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('IpSetConfig') is not None:
            temp_model = main_models.CreateAcceleratorRequestIpSetConfig()
            self.ip_set_config = temp_model.from_map(m.get('IpSetConfig'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateAcceleratorRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateAcceleratorRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the GA instance. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # You can specify up to 20 tag keys.
        self.key = key
        # The tag value of the GA instance. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # You can specify up to 20 tag values.
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

class CreateAcceleratorRequestIpSetConfig(DaraModel):
    def __init__(
        self,
        access_mode: str = None,
    ):
        # The access mode of the acceleration area. Valid values:
        # 
        # - **UserDefine**: Custom nearby access mode. Select acceleration areas and regions as needed. Global Accelerator provides a separate elastic IP address (EIP) for each acceleration region.
        # 
        # - **Anycast**: Automatic nearby access mode. You do not need to configure an acceleration area. Global Accelerator provides an Anycast EIP for multiple regions. Users connect to the nearest access point of the Alibaba Cloud network using the Anycast EIP.
        self.access_mode = access_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')

        return self

