# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewDesktopGroupRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        desktop_group_id: str = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        reseller_owner_uid: int = None,
    ):
        # Specifies whether to enable the auto-payment feature.
        # 
        # Valid values:
        # 
        # *   true (default): enables the auto-payment feature. Make sure that your account balance is sufficient. Otherwise, an abnormal order is generated.
        # *   false: disables the auto-payment feature. In this case, an order is generated but you need to make the payment manually. You can log on to the EDS console and complete the payment based on the order ID on the Orders page.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.auto_renew = auto_renew
        # The ID of the shared group.
        # 
        # This parameter is required.
        self.desktop_group_id = desktop_group_id
        # The renewal duration. Valid values of this parameter are determined by the value of the `PeriodUnit` parameter.
        # 
        # *   Valid values if you set the `PeriodUnit` parameter to `Month`: 1, 2, 3, and 6
        # *   Valid values if you set the `PeriodUnit` parameter to `Year`: 1, 2, 3, 4, and 5
        # 
        # Default value: 1
        self.period = period
        # The unit of the renewal duration specified by the `Period` parameter.
        # 
        # Valid values:
        # 
        # *   Month (default)
        # *   Year
        self.period_unit = period_unit
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the regions supported by Elastic Desktop Service (EDS).
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

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

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

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        return self

