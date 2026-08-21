# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEdgeMobileAgentPackageRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        biz_region_id: str = None,
        client_token: str = None,
        device_class: str = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        quantity: int = None,
    ):
        # Specifies whether to enable automatic payment. Valid values:
        # 
        # - **true**: Enable automatic payment. Make sure that your account balance is sufficient.
        # - **false** (default): Generate the order without making a payment.
        # 
        # 
        # 
        # 
        # > If your payment method has an insufficient balance, set this parameter to false. An unpaid order is generated, and you can log on to the WUYING Cloud Phone console to complete the payment.
        # >
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # * **true**: Enable auto-renewal.
        # * **false** (default): Disable auto-renewal.
        self.auto_renew = auto_renew
        # The region where the agent is located.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The idempotency token.
        self.client_token = client_token
        # The device form factor.
        # 
        # This parameter is required.
        self.device_class = device_class
        # The subscription duration of the resource. The unit is specified by `PeriodUnit`.
        # 
        # This parameter is required.
        self.period = period
        # The unit of the subscription duration.
        # 
        # Valid values:
        # - **Month**: month.
        # - **Year**: year.
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The promotion ID.
        self.promotion_id = promotion_id
        # The number of packages.
        # 
        # This parameter is required.
        self.quantity = quantity

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

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.device_class is not None:
            result['DeviceClass'] = self.device_class

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeviceClass') is not None:
            self.device_class = m.get('DeviceClass')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        return self

