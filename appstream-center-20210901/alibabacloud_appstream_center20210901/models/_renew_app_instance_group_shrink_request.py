# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenewAppInstanceGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        auto_pay: bool = None,
        period: int = None,
        period_unit: str = None,
        product_type: str = None,
        promotion_id: str = None,
        renew_amount: int = None,
        renew_mode: str = None,
        renew_nodes_shrink: str = None,
    ):
        # The ID of the delivery group.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # Specifies whether to enable automatic payment.
        self.auto_pay = auto_pay
        # The numeric part of the resource purchase duration. This parameter is used together with PeriodUnit to specify the complete purchase duration.
        # 
        # This parameter is required.
        self.period = period
        # The unit part of the resource purchase duration. This parameter is used together with Period to specify the complete purchase duration. Valid combinations of Period and PeriodUnit:
        # 
        # - 1 Week (1 week)
        # - 1 Month (1 month)
        # - 2 Month (2 months)
        # - 3 Month (3 months)
        # - 6 Month (6 months)
        # - 1 Year (1 year)
        # - 2 Year (2 years)
        # - 3 Year (3 years)
        # 
        # > This parameter is case-sensitive. For example, `Week` is valid, but `week` is invalid. If the request parameters do not match the combinations listed above, such as `2 Week`, the call to this operation succeeds, but an error occurs during the order placement phase.
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The product type.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The promotion ID. You can obtain this value by calling the [GetResourcePrice](https://help.aliyun.com/document_detail/428503.html) operation.
        self.promotion_id = promotion_id
        self.renew_amount = renew_amount
        self.renew_mode = renew_mode
        self.renew_nodes_shrink = renew_nodes_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.renew_amount is not None:
            result['RenewAmount'] = self.renew_amount

        if self.renew_mode is not None:
            result['RenewMode'] = self.renew_mode

        if self.renew_nodes_shrink is not None:
            result['RenewNodes'] = self.renew_nodes_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('RenewAmount') is not None:
            self.renew_amount = m.get('RenewAmount')

        if m.get('RenewMode') is not None:
            self.renew_mode = m.get('RenewMode')

        if m.get('RenewNodes') is not None:
            self.renew_nodes_shrink = m.get('RenewNodes')

        return self

