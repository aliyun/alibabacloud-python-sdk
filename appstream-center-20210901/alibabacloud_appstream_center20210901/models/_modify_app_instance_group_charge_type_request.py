# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyAppInstanceGroupChargeTypeRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_ids: List[str] = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_region_id: str = None,
        charge_type: str = None,
        period: int = None,
        period_unit: str = None,
        product_type: str = None,
        promotion_id: str = None,
    ):
        # The list of delivery group IDs to be modified, in JSON array format. **You must and can only specify one item per request**. The resources must belong to the current account, the specified product, and the business region.
        # 
        # This parameter is required.
        self.app_instance_group_ids = app_instance_group_ids
        # Specifies whether to allow automatic payment for the conversion order. Default value: `false`. Valid values:
        # 
        # - `true`: Automatic payment is allowed.
        # - `false`: Automatic payment is not allowed. If an unpaid order is generated, you must complete the payment separately.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the order. We recommend that you explicitly specify this parameter for subscription orders to determine whether to enable auto-renewal. Valid values:
        # 
        # - `true`: Auto-renewal is enabled.
        # - `false`: Auto-renewal is not enabled.
        self.auto_renew = auto_renew
        # The business region ID of the target delivery group. It must be the same as the actual region to which the resource belongs.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The target billing method after conversion. It must be different from the current billing method. Valid values:
        # 
        # - `PrePaid`: subscription
        # - `PostPaid`: pay-as-you-go
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The numeric part of the purchase duration, used together with `PeriodUnit`. When converting to subscription and a purchase duration is required, specify both parameters. For example, `1` and `Month` indicate a purchase duration of one month. The available purchase durations are determined by the sales rules of the target resource.
        self.period = period
        # The unit of the purchase duration, used together with `Period`. This parameter is case-sensitive. Valid values:
        # 
        # - `Hour`: hour
        # - `Day`: day
        # - `Week`: week
        # - `Month`: month
        # - `Year`: year
        # 
        # These units do not mean that any combination is available for every product. When converting to subscription, select a period supported by the target resource. For example, for a resource that supports monthly purchase, you can set `Period` to `1` and `PeriodUnit` to `Month`.
        self.period_unit = period_unit
        # The product type. Set this parameter to the following fixed value when you call the operation:
        # 
        # - `CloudApp`: WUYING Cloud Application.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The ID of the promotion used for the conversion order. It takes effect only when an order is created and the promotion is applicable. If omitted, no specific coupon is specified. The availability of the promotion is subject to the order result.
        self.promotion_id = promotion_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_ids is not None:
            result['AppInstanceGroupIds'] = self.app_instance_group_ids

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupIds') is not None:
            self.app_instance_group_ids = m.get('AppInstanceGroupIds')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        return self

