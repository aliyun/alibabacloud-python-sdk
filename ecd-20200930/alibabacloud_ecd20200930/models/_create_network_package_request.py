# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
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
        tag: List[main_models.CreateNetworkPackageRequestTag] = None,
    ):
        # Specifies whether to enable automatic payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal.
        self.auto_renew = auto_renew
        # The bandwidth of the premium bandwidth plan. Unit: Mbit/s.    
        # 
        # - If the premium bandwidth plan uses the subscription billing method, the valid values are 2 to 1000.
        # - If the premium bandwidth plan uses the pay-as-you-go billing method and the billing type is pay-by-data-transfer (PayByTraffic), the valid values are 2 to 200.
        # - If the premium bandwidth plan uses the pay-as-you-go billing method and the billing type is pay-by-bandwidth (PayByBandwidth), the valid values are 2 to 1000.
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        self.channel_cookie = channel_cookie
        # The billable methods of the premium bandwidth plan.
        # 
        # - If the parameter `PayType` is set to `PrePaid`, valid values:
        #     - PayByBandwidth: billing by fixed bandwidth.
        # - If the parameter `PayType` is set to `PostPaid`, valid values:
        #     - PayByTraffic: billing by data transfer.
        #     - PayByBandwidth: billing by fixed bandwidth.
        self.internet_charge_type = internet_charge_type
        # The office network ID.
        self.office_site_id = office_site_id
        # The billing method.
        self.pay_type = pay_type
        # The subscription duration of the premium bandwidth plan. This parameter takes effect and is required only when PayType is set to PrePaid. Valid values are determined by the PeriodUnit parameter.
        # 
        # - If PeriodUnit is set to Week, the valid value is 1.
        # - If PeriodUnit is set to Month, valid values are 1, 2, 3, and 6.
        # - If PeriodUnit is set to Year, valid values are 1, 2, and 3.
        # 
        # Default value: 1.
        self.period = period
        # The unit of the subscription duration for the premium bandwidth plan. This parameter takes effect and is required only when PayType is set to PrePaid.
        self.period_unit = period_unit
        # The promotion ID.
        self.promotion_id = promotion_id
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.reseller_owner_uid = reseller_owner_uid
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

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateNetworkPackageRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateNetworkPackageRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

