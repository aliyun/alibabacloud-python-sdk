# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeResellerConsumeAmountRequest(DaraModel):
    def __init__(
        self,
        adjust_type: str = None,
        amount: str = None,
        business_type: str = None,
        currency: str = None,
        extend_map: str = None,
        out_biz_id: str = None,
        owner_id: int = None,
        source: str = None,
    ):
        # The type of the consumption amount adjustment. Valid values: increase: The consumption amount increases because new consumption occurs. decrease: The consumption amount decreases because funds are added to the account. This parameter is required.
        # 
        # This parameter is required.
        self.adjust_type = adjust_type
        # The amount to be adjusted. Unit: CNY
        # 
        # This parameter is required.
        self.amount = amount
        # The type of the business.
        # 
        # This parameter is required.
        self.business_type = business_type
        # The type of the currency.
        # 
        # This parameter is required.
        self.currency = currency
        # The extended field of a message.
        self.extend_map = extend_map
        # The ID of the primary key for external business. The ID is used for idempotence verification.
        # 
        # This parameter is required.
        self.out_biz_id = out_biz_id
        # This parameter is required.
        self.owner_id = owner_id
        # The source of the request. Specify the system name for the parameter.
        # 
        # This parameter is required.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjust_type is not None:
            result['AdjustType'] = self.adjust_type

        if self.amount is not None:
            result['Amount'] = self.amount

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.extend_map is not None:
            result['ExtendMap'] = self.extend_map

        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdjustType') is not None:
            self.adjust_type = m.get('AdjustType')

        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('ExtendMap') is not None:
            self.extend_map = m.get('ExtendMap')

        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

