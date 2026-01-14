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
        # *   **false:** disables automatic payment. If you select this option, you must go to the Order Center to complete the payment after an order is generated. This is the default value.
        # *   **true:** enables automatic payment. Payments are automatically completed.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the basic GA instance. Valid values:
        # 
        # *   **true:** enables auto-renewal for the basic GA instance.
        # *   **false:** disables auto-renewal for the basic GA instance. This is the default value.
        self.auto_renew = auto_renew
        # The auto-renewal duration. Unit: months.
        # 
        # Valid values: **1** to **12**. Default value: **1**.
        # 
        # >  This parameter takes effect only when the **AutoPay** parameter is set to **true**.
        self.auto_renew_duration = auto_renew_duration
        # Specifies whether to automatically apply coupons to your bills. Valid values:
        # 
        # *   **true:** automatically applies coupons to your bills.
        # *   **false:** does not automatically apply coupons to your bills. This is the default value.
        # 
        # >  This parameter takes effect only when the **AutoPay** parameter is set to **true**.
        self.auto_use_coupon = auto_use_coupon
        # The bandwidth billing method. Valid values:
        # 
        # *   **BandwidthPackage:** billed based on bandwidth plans.
        # *   **CDT:** billed based on data transfer. The bills are managed by using Cloud Data Transfer (CDT).
        # *   **CDT95:** billed based on the 95th percentile bandwidth. The bills are managed by using Cloud Data Transfer (CDT). This bandwidth billing method is not available by default. Contact your Alibaba Cloud account manager for more information.
        self.bandwidth_billing_type = bandwidth_billing_type
        # The billing method. Valid values:
        # 
        # *   **PREPAY** (default)
        # *   **POSTPAY**
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true:** performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed. This is the default value.
        self.dry_run = dry_run
        # The subscription duration of the GA instance.
        # 
        # *   If you set **PricingCycle** to **Month**, the valid values for **Duration** are **1** to **9**.
        # *   If you set **PricingCycle** to **Year**, the valid values for **Duration** are **1** to **3**.
        self.duration = duration
        # The billing cycle. Valid values:
        # 
        # *   **Month**
        # *   **Year**
        self.pricing_cycle = pricing_cycle
        # The code of the coupon.
        # 
        # >  This parameter takes effect only for accounts registered on the international site (alibabacloud.com).
        self.promotion_option_no = promotion_option_no
        # The ID of the region where the basic GA instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the basic GA instance belongs.
        self.resource_group_id = resource_group_id
        # The tags of the basic GA instance.
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
        # The tag key. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `aliyun` or `acs:`.
        # 
        # You can specify up to 20 tag keys.
        self.key = key
        # The tag value. The tag value cannot be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. It cannot start with `acs:` or `aliyun`.
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

