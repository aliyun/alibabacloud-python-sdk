# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVirtualBridgeLevelRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        bridge_id: str = None,
        bridge_level: str = None,
        paid_call_back_url: str = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        region_id: str = None,
    ):
        # Specifies whether to enable automatic payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. This parameter takes effect and is optional only when the billing method is `PrePaid`.
        self.auto_renew = auto_renew
        # The virtual bridge ID.
        # 
        # This parameter is required.
        self.bridge_id = bridge_id
        # The virtual bridge specifications.
        # 
        # This parameter is required.
        self.bridge_level = bridge_level
        # The payment callback URL.
        self.paid_call_back_url = paid_call_back_url
        # The renewal duration. Valid values of this parameter are determined by the value of the `PeriodUnit` parameter.
        # 
        # - If `PeriodUnit` is set to `Month`, valid values are 1, 2, 3, and 6.
        # - If `PeriodUnit` is set to `Year`, valid values are 1, 2, and 3.
        # 
        # Default value: 1.
        self.period = period
        # The unit of the subscription duration for the prepaid cloud disk. This parameter takes effect and is required only when the `CdsChargeType` parameter is set to `PrePaid`.
        self.period_unit = period_unit
        # The promotion ID. You can call the pricing query operation to obtain the list of matched promotion IDs.
        self.promotion_id = promotion_id
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the list of regions supported by WUYING Workspace.
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
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.bridge_id is not None:
            result['BridgeId'] = self.bridge_id

        if self.bridge_level is not None:
            result['BridgeLevel'] = self.bridge_level

        if self.paid_call_back_url is not None:
            result['PaidCallBackUrl'] = self.paid_call_back_url

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
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BridgeId') is not None:
            self.bridge_id = m.get('BridgeId')

        if m.get('BridgeLevel') is not None:
            self.bridge_level = m.get('BridgeLevel')

        if m.get('PaidCallBackUrl') is not None:
            self.paid_call_back_url = m.get('PaidCallBackUrl')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

