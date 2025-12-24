# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateBandwidthResourcePackagesRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        package_size: int = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        region_id: str = None,
    ):
        # The number of the data transfer plans that you want to create at the same time. Valid values: 1 to 20. Default value: 1.
        self.amount = amount
        # Specifies whether to enable the auto-payment feature.
        self.auto_pay = auto_pay
        # The size of the data transfer plan. Valid values: 10 to 1000. Unit: GiB.
        # 
        # This parameter is required.
        self.package_size = package_size
        # The subscription duration. The valid values of this parameter vary based on the value of `PeriodUnit`.
        # 
        # *   If `PeriodUnit` is set to `Month`, the valid values of Period are 1, 3, and 6.
        # *   If `PeriodUnit` is set to `Year`, the valid value of Period is 1.
        # 
        # Default value: 1.
        self.period = period
        # The unit of the subscription duration.
        # 
        # Valid values:
        # 
        # *   Month (default)
        # *   Year
        self.period_unit = period_unit
        # The ID of the promotional activity.
        self.promotion_id = promotion_id
        # The ID of the region. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.package_size is not None:
            result['PackageSize'] = self.package_size

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('PackageSize') is not None:
            self.package_size = m.get('PackageSize')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

