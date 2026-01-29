# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryRedeemResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryRedeemResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryRedeemResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryRedeemResponseBodyData(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        redeem: main_models.QueryRedeemResponseBodyDataRedeem = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned per page.
        self.page_size = page_size
        # The details of the redemption coupon.
        self.redeem = redeem
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.redeem:
            self.redeem.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.redeem is not None:
            result['Redeem'] = self.redeem.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Redeem') is not None:
            temp_model = main_models.QueryRedeemResponseBodyDataRedeem()
            self.redeem = temp_model.from_map(m.get('Redeem'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryRedeemResponseBodyDataRedeem(DaraModel):
    def __init__(
        self,
        redeem: List[main_models.QueryRedeemResponseBodyDataRedeemRedeem] = None,
    ):
        self.redeem = redeem

    def validate(self):
        if self.redeem:
            for v1 in self.redeem:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Redeem'] = []
        if self.redeem is not None:
            for k1 in self.redeem:
                result['Redeem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.redeem = []
        if m.get('Redeem') is not None:
            for k1 in m.get('Redeem'):
                temp_model = main_models.QueryRedeemResponseBodyDataRedeemRedeem()
                self.redeem.append(temp_model.from_map(k1))

        return self

class QueryRedeemResponseBodyDataRedeemRedeem(DaraModel):
    def __init__(
        self,
        applicable_products: str = None,
        balance: str = None,
        effective_time: str = None,
        expiry_time: str = None,
        granted_time: str = None,
        nominal_value: str = None,
        redeem_id: str = None,
        redeem_no: str = None,
        specification: str = None,
        status: str = None,
    ):
        # The services to which the redemption coupon is applicable.
        self.applicable_products = applicable_products
        # The balance of the redemption coupon.
        self.balance = balance
        # The time when the redemption coupon took effect.
        self.effective_time = effective_time
        # The time when the redemption coupon expired.
        self.expiry_time = expiry_time
        # The time when the redemption coupon was issued.
        self.granted_time = granted_time
        # The nominal value of the redemption coupon.
        self.nominal_value = nominal_value
        # The ID of the redemption coupon.
        self.redeem_id = redeem_id
        # The number of the redemption coupon.
        self.redeem_no = redeem_no
        # The specifications of the redemption coupon.
        self.specification = specification
        # The status of the redemption coupon. Valid values:
        # 
        # *   Generated
        # *   CallBack
        # *   RefundPending
        # *   Canceled
        # *   Order_Canceled
        # *   ActivePending
        # *   ActiveSuccess
        # *   ExchangePending
        # *   ExchangeSuccess
        # *   Expired
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicable_products is not None:
            result['ApplicableProducts'] = self.applicable_products

        if self.balance is not None:
            result['Balance'] = self.balance

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time

        if self.granted_time is not None:
            result['GrantedTime'] = self.granted_time

        if self.nominal_value is not None:
            result['NominalValue'] = self.nominal_value

        if self.redeem_id is not None:
            result['RedeemId'] = self.redeem_id

        if self.redeem_no is not None:
            result['RedeemNo'] = self.redeem_no

        if self.specification is not None:
            result['Specification'] = self.specification

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicableProducts') is not None:
            self.applicable_products = m.get('ApplicableProducts')

        if m.get('Balance') is not None:
            self.balance = m.get('Balance')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')

        if m.get('GrantedTime') is not None:
            self.granted_time = m.get('GrantedTime')

        if m.get('NominalValue') is not None:
            self.nominal_value = m.get('NominalValue')

        if m.get('RedeemId') is not None:
            self.redeem_id = m.get('RedeemId')

        if m.get('RedeemNo') is not None:
            self.redeem_no = m.get('RedeemNo')

        if m.get('Specification') is not None:
            self.specification = m.get('Specification')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

