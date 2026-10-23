# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBandwidthPackagePriceRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        biz_region_id: str = None,
        internet_charge_type: str = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        purchase_channel_type: str = None,
    ):
        # This parameter is required.
        self.bandwidth = bandwidth
        # This parameter is required.
        self.biz_region_id = biz_region_id
        self.internet_charge_type = internet_charge_type
        self.period = period
        self.period_unit = period_unit
        self.promotion_id = promotion_id
        self.purchase_channel_type = purchase_channel_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.purchase_channel_type is not None:
            result['PurchaseChannelType'] = self.purchase_channel_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('PurchaseChannelType') is not None:
            self.purchase_channel_type = m.get('PurchaseChannelType')

        return self

