# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateBandwidthPackageRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        auto_use_coupon: str = None,
        bandwidth: int = None,
        bandwidth_type: str = None,
        billing_type: str = None,
        cbn_geographic_region_id_a: str = None,
        cbn_geographic_region_id_b: str = None,
        charge_type: str = None,
        client_token: str = None,
        duration: str = None,
        pricing_cycle: str = None,
        promotion_option_no: str = None,
        ratio: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[main_models.CreateBandwidthPackageRequestTag] = None,
        type: str = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # *   **false** (default): disables automatic payment. If you select this option, you must go to the Order Center to complete the payment after an order is generated.
        # *   **true**: enables automatic payment. Payments are automatically completed.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the bandwidth plan. Valid values:
        # 
        # *   **true**: enables auto-renewal.
        # *   **false** (default): does not enable auto-renewal.
        self.auto_renew = auto_renew
        # The auto-renewal duration. Unit: months.
        # 
        # Valid values: **1** to **12**. Default value: **1**.
        # 
        # >  This parameter is required only if **AutoRenew** is set to **true**.
        self.auto_renew_duration = auto_renew_duration
        # Specifies whether to automatically pay bills by using coupons. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        # 
        # >  This parameter is required only if **AutoPay** is set to **true**.
        self.auto_use_coupon = auto_use_coupon
        # The bandwidth of the bandwidth plan. Unit: Mbit/s.
        # 
        # Valid values: **2** to **2000**.
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        # The type of the bandwidth. Valid values:
        # 
        # *   **Basic**: standard bandwidth
        # *   **Enhanced**: enhanced bandwidth
        # *   **Advanced**: premium bandwidth
        # 
        # If **Type** is set to **Basic**, this parameter is required.
        self.bandwidth_type = bandwidth_type
        # The metering method that is used when you use the pay-as-you-go billing method. Valid values:
        # 
        # *   **PayByTraffic** (default)
        # *   **PayBY95** By default, the pay-by-95th-percentile metering method is unavailable. If you want to use the metering method, contact your account manager.
        # 
        # >  This parameter takes effect only if you set **ChargeType** to **POSTPAY**.
        self.billing_type = billing_type
        # Area A to be connected. Set the value to **China-mainland**.
        # 
        # You can set this parameter only if you call this operation on the international site (alibabacloud.com).
        self.cbn_geographic_region_id_a = cbn_geographic_region_id_a
        # Area B to be connected. Set the value to **Global**.
        # 
        # You can set this parameter only if you call this operation on the international site (alibabacloud.com).
        self.cbn_geographic_region_id_b = cbn_geographic_region_id_b
        # The billing method of the bandwidth plan. Valid values:
        # 
        # *   **PREPAY** (default): subscription.
        # *   **POSTPAY**: pay-as-you-go. By default, the pay-as-you-go billing method is unavailable. If you want to use the billing method, contact your account manager.
        self.charge_type = charge_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The subscription duration.
        # 
        # *   If the **PricingCycle** parameter is set to **Month**, the valid values for the **Duration** parameter are **1** to **9**.
        # *   If the **PricingCycle** parameter is set to **Year**, the valid values for the **Duration** parameter are **1** to **3**.
        # 
        # If **ChargeType** is set to **PREPAY**, this parameter is required.
        self.duration = duration
        # The billing cycle. Valid values:
        # 
        # *   **Month**: billed on a monthly basis.
        # *   **Year**: billed on an annual basis.
        # 
        # If **ChargeType** is set to **PREPAY**, this parameter is required.
        self.pricing_cycle = pricing_cycle
        # The coupon code.
        # 
        # >  This parameter is only available on the international site (alibabacloud.com).
        self.promotion_option_no = promotion_option_no
        # The percentage of the minimum bandwidth guaranteed if the pay-by-95th-percentile-bandwidth metering method is used. Valid values: **30** to **100**.
        # 
        # >  This parameter is required only if **BillingType** is set to **PayBY95**.
        self.ratio = ratio
        # The ID of the region where the GA instance is deployed. **cn-hangzhou** is returned.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags to add to the bandwidth plan.
        self.tag = tag
        # The type of the bandwidth plan. Valid values:
        # 
        # *   **Basic**: a basic bandwidth plan
        # *   **CrossDomain**: a cross-region acceleration bandwidth plan
        # 
        # If you call this operation on the Alibaba Cloud China site, only **Basic** is supported.
        # 
        # This parameter is required.
        self.type = type

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

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type

        if self.billing_type is not None:
            result['BillingType'] = self.billing_type

        if self.cbn_geographic_region_id_a is not None:
            result['CbnGeographicRegionIdA'] = self.cbn_geographic_region_id_a

        if self.cbn_geographic_region_id_b is not None:
            result['CbnGeographicRegionIdB'] = self.cbn_geographic_region_id_b

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        if self.ratio is not None:
            result['Ratio'] = self.ratio

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

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

        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')

        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')

        if m.get('CbnGeographicRegionIdA') is not None:
            self.cbn_geographic_region_id_a = m.get('CbnGeographicRegionIdA')

        if m.get('CbnGeographicRegionIdB') is not None:
            self.cbn_geographic_region_id_b = m.get('CbnGeographicRegionIdB')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateBandwidthPackageRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateBandwidthPackageRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # The tag keys cannot be an empty string. The tag key can be up to 64 characters in length, and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can specify at most 20 tag keys.
        self.key = key
        # The tag value.
        # 
        # Each tag key corresponds to a tag value. Valid values of **N**: **1** to **20**.
        # 
        # The value cannot exceed 128 characters in length, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

