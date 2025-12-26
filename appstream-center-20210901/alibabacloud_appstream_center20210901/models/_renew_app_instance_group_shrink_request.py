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
        # 
        # Valid values:
        # 
        # *   true
        # *   false: manual payment. This is the default value.
        self.auto_pay = auto_pay
        # The subscription duration of resources. This parameter must be configured together with `PeriodUnit`.
        # 
        # This parameter is required.
        self.period = period
        # The unit of the subscription duration. This parameter must be configured together with `Period`. The following items describe valid values for the combinations of `Period` and `PeriodUnit`:
        # 
        # *   1 Week
        # *   1 Month
        # *   2 Month
        # *   3 Month
        # *   6 Month
        # *   1 Year
        # *   2 Year
        # *   3 Year
        # 
        # >  The value of this parameter is case-insensitive. For example, `Week` is valid and `week` is invalid. If you specify a value combination other than the preceding combinations, such as `2 Week`, the operation can still be called. However, an error occurs when you place the order.
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The product type.
        # 
        # Valid value:
        # 
        # *   CloudApp: App Streaming
        # 
        # This parameter is required.
        self.product_type = product_type
        # The promotion ID. You can call the [GetResourcePrice](https://help.aliyun.com/document_detail/428503.html) operation to obtain the ID.
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

