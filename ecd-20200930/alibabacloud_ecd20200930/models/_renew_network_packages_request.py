# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RenewNetworkPackagesRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        network_package_id: List[str] = None,
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
        self.auto_renew = auto_renew
        # The IDs of premium bandwidth plans. You can specify up to 100 IDs.
        # 
        # This parameter is required.
        self.network_package_id = network_package_id
        # The subscription duration if you specify subscription as the new billing method for the cloud desktop. The unit of the value is specified by the `PeriodUnit` parameter. This parameter takes effect only when the `ChargeType` parameter is set to `PrePaid`.
        # 
        # *   If the `PeriodUnit` parameter is set to `Week`, the valid value of the Period parameter is 1.
        # *   If the `PeriodUnit` parameter is set to `Month`, the valid values of the Period parameter are 1, 2, 3, and 6.
        # *   If the `PeriodUnit` parameter is set to `Year`, the valid values of the Period parameter are 1, 2, 3, 4, and 5.
        self.period = period
        # The unit of the renewal duration specified by the Period parameter. Valid values:
        # 
        # *   Month
        # *   Year
        # 
        # Default value: Month.
        self.period_unit = period_unit
        # The promotion ID.
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

        if self.network_package_id is not None:
            result['NetworkPackageId'] = self.network_package_id

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

        if m.get('NetworkPackageId') is not None:
            self.network_package_id = m.get('NetworkPackageId')

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

