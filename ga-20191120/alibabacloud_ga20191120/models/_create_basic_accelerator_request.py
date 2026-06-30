# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateBasicAcceleratorRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        auto_use_coupon: str = None,
        bandwidth_billing_type: str = None,
        charge_type: str = None,
        client_token: str = None,
        dry_run: bool = None,
        duration: int = None,
        pricing_cycle: str = None,
        promotion_option_no: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[main_models.CreateBasicAcceleratorRequestTag] = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # - **false** (default): disables automatic payment. After an order is generated, go to the Order Center to complete the payment.
        # 
        # - **true**: enables automatic payment. The order is automatically paid.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal.
        # 
        # - **true**: enables auto-renewal.
        # 
        # - **false** (default): disables auto-renewal.
        self.auto_renew = auto_renew
        # The auto-renewal duration. Unit: months.
        # 
        # Valid values: **1** to **12**. Default value: **1**.
        # 
        # > This parameter takes effect only when **AutoRenew** is set to **true**.
        self.auto_renew_duration = auto_renew_duration
        # Specifies whether to use coupons for automatic payment of the bill. Valid values:
        # 
        # - **true**: uses coupons.
        # 
        # - **false** (default): does not use coupons.
        # 
        # > This parameter takes effect only when **AutoPay** is set to **true**.
        self.auto_use_coupon = auto_use_coupon
        # The bandwidth billing method. Valid values:
        # - **BandwidthPackage**: billed by bandwidth plan.
        # - **CDT**: billed by traffic and settled through unified settlement by Cloud Data Transfer (CDT).
        # - **CDT95**: billed by the 95th percentile bandwidth and settled through unified settlement by CDT. This bandwidth billing method is available only to users in the whitelist.
        self.bandwidth_billing_type = bandwidth_billing_type
        # The billing method. Valid values:
        # - **PREPAY (default)**: subscription.
        # - **POSTPAY**: pay-as-you-go.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # - **true**: performs a dry run without creating the resource. The system checks the required parameters, request syntax, and business limitations. If the check fails, the corresponding error is returned. If the check succeeds, the `DryRunOperation` error code is returned.
        # - **false** (default): performs a dry run and sends the request. If the check succeeds, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The subscription duration.
        # 
        # - If **PricingCycle** is set to **Month**, valid values of **Duration** are **1** to **9**.
        # 
        # - If **PricingCycle** is set to **Year**, valid values of **Duration** are **1** to **3**.
        self.duration = duration
        # The billing cycle. Valid values:
        # 
        # - **Month**: billed on a monthly basis.
        # 
        # - **Year**: billed on a yearly basis.
        self.pricing_cycle = pricing_cycle
        # The coupon number.
        # > This parameter is applicable only to the China site (aliyun.com).
        self.promotion_option_no = promotion_option_no
        # The region ID of the basic Alibaba Cloud Global Accelerator (GA) instance. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the basic Alibaba Cloud Global Accelerator (GA) instance belongs.
        self.resource_group_id = resource_group_id
        # The labels of the basic Alibaba Cloud Global Accelerator (GA) instance.
        self.tag = tag

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
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.bandwidth_billing_type is not None:
            result['BandwidthBillingType'] = self.bandwidth_billing_type

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

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

        if m.get('BandwidthBillingType') is not None:
            self.bandwidth_billing_type = m.get('BandwidthBillingType')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateBasicAcceleratorRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateBasicAcceleratorRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The label key of the basic Alibaba Cloud Global Accelerator (GA) instance. If you specify this parameter, the value cannot be an empty string.
        # 
        # The label key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # You can specify up to 20 label keys.
        self.key = key
        # The label value of the basic Alibaba Cloud Global Accelerator (GA) instance. If you specify this parameter, the value cannot be an empty string.
        # 
        # The label value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # You can specify up to 20 label values.
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

