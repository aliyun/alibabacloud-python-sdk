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
        # Specifies whether to enable automatic payment. Default value: false. Valid values:
        # 
        # *   **false:** disables automatic payment. If you select this option, you must go to the Order Center to complete the payment after an order is generated.
        # *   **true:** enables automatic payment. Payments are automatically completed.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the GA instance. Default value: false. Valid values:
        # 
        # *   **true:** enables auto-renewal.
        # *   **false:** disables auto-renewal.
        self.auto_renew = auto_renew
        # The auto-renewal duration. Unit: months.
        # 
        # Valid values: **1** to **12**. Default value: **1**.
        # 
        # >  This parameter takes effect only when **AutoRenew** is set to **true**.
        self.auto_renew_duration = auto_renew_duration
        # Specifies whether to automatically use coupons when making payments. Default value: false. Valid values:
        # 
        # *   **true:** automatically pays bill by using coupons.
        # *   **false:** does not automatically pay bills by using coupons.
        # 
        # >  This parameter takes effect only when **AutoPay** is set to **true**.
        self.auto_use_coupon = auto_use_coupon
        self.bandwidth = bandwidth
        # The bandwidth billing method.
        # 
        # *   **BandwidthPackage:** billed based on bandwidth plans.
        # *   **CDT:** billed based on data transfer.
        # *   **CDT95:** billed based on the 95th percentile bandwidth. The billing is managed by Cloud Data Transfer (CDT). This bandwidth billing method is not available by default. Contact your Alibaba Cloud account manager for more information.
        self.bandwidth_billing_type = bandwidth_billing_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true:** performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The subscription duration of the GA instance.
        # 
        # *   If the **PricingCycle** parameter is set to **Month**, the valid values for the **Duration** parameter are **1** to **9**.
        # *   If the **PricingCycle** parameter is set to **Year**, the valid values for the **Duration** parameter are **1** to **3**.
        # 
        # >  If the **InstanceChargeType** parameter is set to **PREPAY**, you must configure this parameter.
        self.duration = duration
        # The billing method of the GA instance.
        # 
        # *   PREPAY (default): subscription
        # *   POSTPAY: pay-as-you-go
        self.instance_charge_type = instance_charge_type
        # The configurations of the acceleration area.
        self.ip_set_config = ip_set_config
        # The name of the GA instance.
        # 
        # The name must be 2 to 128 characters in length and can contain digits, underscores (_), and hyphens (-). It must start with a letter.
        self.name = name
        # The billing cycle of the GA instance. Valid values:
        # 
        # *   **Month:** billed on a monthly basis.
        # *   **Year:** billed on an annual basis.
        # 
        # >  If the **InstanceChargeType** parameter is set to **PREPAY**, you must configure this parameter.
        self.pricing_cycle = pricing_cycle
        # The coupon code.
        self.promotion_option_no = promotion_option_no
        # The ID of the region in which to create the GA instance. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the standard GA instance belongs.
        self.resource_group_id = resource_group_id
        # The type of the GA instance. Valid values:
        # 
        # *   **1**: Small Ⅰ.
        # *   **2**: Small Ⅱ.
        # *   **3**: Small Ⅲ.
        # *   **5**: Medium Ⅰ.
        # *   **8**: Medium Ⅱ.
        # *   **10**: Medium Ⅲ.
        # *   **20**: Large Ⅰ.
        # *   **30**: Large Ⅱ.
        # *   **40**: Large Ⅲ.
        # *   **50**: Large IV.
        # *   **60**: Large V.
        # *   **70**: Large VI.
        # *   **80**: Large VII.
        # *   **90**: Large VIII.
        # *   **100**: Super Large Ⅰ.
        # *   **200**: Super Large Ⅱ.
        # 
        # > *   GA instances Large III and above are not available by default. To use these instances, contact your Alibaba Cloud account manager.
        # >*   If the **InstanceChargeType** parameter is set to **PREPAY**, you must configure this parameter.
        # 
        # Different specifications provide different capabilities. For more information, see [Instance type](https://help.aliyun.com/document_detail/153127.html).
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
        # The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        # 
        # You can specify up to 20 tag keys.
        self.key = key
        # The tag value of the GA instance. The tag value cannot be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
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
        # *   **UserDefine:** custom nearby access mode. You can select acceleration areas and regions based on your business requirements. GA allocates a separate EIP to each acceleration region.
        # *   **Anycast:** automatic nearby access mode. You do not need to specify an acceleration area. GA allocates an Anycast EIP to multiple regions across the globe. Users can connect to the nearest access point of the Alibaba Cloud global transmission network by sending requests to the Anycast EIP.
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

