# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RenewDesktopsRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        desktop_id: List[str] = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        region_id: str = None,
        reseller_owner_uid: int = None,
        resource_type: str = None,
    ):
        # Specifies whether to enable automatic payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal.
        self.auto_renew = auto_renew
        # The list of cloud computer IDs. Only monthly subscription cloud computers can be renewed.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # The renewal duration. Valid values of this parameter are determined by the value of the `PeriodUnit` parameter.
        # 
        # - If `PeriodUnit` is set to `Month`, valid values are 1, 2, 3, and 6.
        # 
        # - If `PeriodUnit` is set to `Year`, valid values are 1 to 5.
        # 
        # Default value: 1.
        self.period = period
        # The unit of the renewal duration, which is the unit of the `Period` parameter.
        self.period_unit = period_unit
        # The promotion ID.
        self.promotion_id = promotion_id
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The user ID for resource ownership in the reselling pattern. You do not need to specify this parameter if you are not using the reselling pattern.
        self.reseller_owner_uid = reseller_owner_uid
        # > This parameter is not publicly available.
        self.resource_type = resource_type

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

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

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

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

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

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

