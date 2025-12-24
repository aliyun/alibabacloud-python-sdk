# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNetworkPackageRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        bandwidth: int = None,
        channel_cookie: str = None,
        internet_charge_type: str = None,
        office_site_id: str = None,
        pay_type: str = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        region_id: str = None,
        reseller_owner_uid: int = None,
    ):
        # Specifies whether to enable the automatic payment feature.
        # 
        # Valid values:
        # 
        # *   true (default): enables the auto-payment feature.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     Make sure that your account has sufficient balance. Otherwise, no order is generated.
        # 
        #     <!-- -->
        # 
        # *   false: disables the auto-payment feature. In this case, an order is generated but you need to make the payment manually.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     To make the payment, log on to the Elastic Desktop Service console, go to the Orders page, and find the order based on the order ID.
        # 
        #     <!-- -->
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the premium bandwidth plan.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.auto_renew = auto_renew
        # The bandwidth provided by the premium bandwidth plan. Unit: Mbit/s.
        # 
        # *   Valid values if the premium bandwidth plan is a subscription plan: 2 to 1000.
        # *   Valid values if the premium bandwidth plan is a pay-as-you-go plan that charges by data transfer (PayByTraffic): 2 to 200.
        # *   Valid values if the premium bandwidth plan is a pay-as-you-go plan that charges by fixed bandwidth (PayByBandwidth): 2 to 1000.
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        self.channel_cookie = channel_cookie
        # The charge type of the premium bandwidth plan.
        # 
        # *   Valid value when the `PayType` parameter is set to `PrePaid`:
        # 
        #     *   PayByBandwidth: charges by fixed bandwidth.
        # 
        # *   Valid values when the `PayType` parameter is set to `PostPaid`:
        # 
        #     *   PayByTraffic: charges by data transfer.
        #     *   PayByBandwidth: charges by fixed bandwidth.
        self.internet_charge_type = internet_charge_type
        # The office network ID.
        self.office_site_id = office_site_id
        # The billing method of the premium bandwidth plan.
        # 
        # Valid values:
        # 
        # *   PostPaid: pay-as-you-go
        # *   PrePaid: subscription
        self.pay_type = pay_type
        # The subscription duration of the premium bandwidth plan. This parameter takes effect and is required only when the `PayType` parameter is set to `PrePaid`. The valid values of this parameter vary based on the `PeriodUnit` value.
        # 
        # *   Valid value when the `PeriodUnit` parameter is set to `Week`: 1
        # *   Valid values when the `PeriodUnit` parameter is set to `Month`: 1, 2, 3, and 6
        # *   Valid values when the `PeriodUnit` parameter is set to `Year`: 1, 2, and 3
        # 
        # Default value: 1.
        self.period = period
        # The unit of the subscription duration of the premium bandwidth plan. This parameter takes effect and is required only when the `PayType` parameter is set to `PrePaid`.
        # 
        # Valid values:
        # 
        # *   Month
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Year
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Week
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.period_unit = period_unit
        # The ID of the sales promotion.
        self.promotion_id = promotion_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.reseller_owner_uid = reseller_owner_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.channel_cookie is not None:
            result['ChannelCookie'] = self.channel_cookie

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ChannelCookie') is not None:
            self.channel_cookie = m.get('ChannelCookie')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        return self

