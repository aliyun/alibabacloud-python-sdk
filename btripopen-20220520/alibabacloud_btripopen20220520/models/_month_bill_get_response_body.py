# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class MonthBillGetResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[main_models.MonthBillGetResponseBodyModule] = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        result['module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['module'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        self.module = []
        if m.get('module') is not None:
            for k1 in m.get('module'):
                temp_model = main_models.MonthBillGetResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class MonthBillGetResponseBodyModule(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        month_account_bill_detail: main_models.MonthBillGetResponseBodyModuleMonthAccountBillDetail = None,
        start_date: str = None,
        url: str = None,
    ):
        self.end_date = end_date
        # CorpMonthAccountBillFeeDetail
        self.month_account_bill_detail = month_account_bill_detail
        self.start_date = start_date
        self.url = url

    def validate(self):
        if self.month_account_bill_detail:
            self.month_account_bill_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['end_date'] = self.end_date

        if self.month_account_bill_detail is not None:
            result['monthAccountBillDetail'] = self.month_account_bill_detail.to_map()

        if self.start_date is not None:
            result['start_date'] = self.start_date

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end_date') is not None:
            self.end_date = m.get('end_date')

        if m.get('monthAccountBillDetail') is not None:
            temp_model = main_models.MonthBillGetResponseBodyModuleMonthAccountBillDetail()
            self.month_account_bill_detail = temp_model.from_map(m.get('monthAccountBillDetail'))

        if m.get('start_date') is not None:
            self.start_date = m.get('start_date')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class MonthBillGetResponseBodyModuleMonthAccountBillDetail(DaraModel):
    def __init__(
        self,
        bill_confirmed: int = None,
        car_amount: float = None,
        damage_amount: float = None,
        flight_amount: float = None,
        fu_point: float = None,
        hotel_amount: float = None,
        ie_flight_amount: float = None,
        ie_hotel_amount: float = None,
        mail_bill_date: int = None,
        meal_amount: float = None,
        service_amount: float = None,
        train_amount: float = None,
        vas_amount: float = None,
    ):
        self.bill_confirmed = bill_confirmed
        # 用车金额（单位：元）
        self.car_amount = car_amount
        # 违约金金额（单位：元）
        self.damage_amount = damage_amount
        # 机票金额（单位：元）
        self.flight_amount = flight_amount
        # 福豆金额（单位：元）
        self.fu_point = fu_point
        # 酒店金额（单位：元）
        self.hotel_amount = hotel_amount
        # 国际机票金额（单位：元）
        self.ie_flight_amount = ie_flight_amount
        self.ie_hotel_amount = ie_hotel_amount
        # 账期日：YYYYMMDD
        self.mail_bill_date = mail_bill_date
        self.meal_amount = meal_amount
        # 服务费金额（单位：元）
        self.service_amount = service_amount
        # 火车票金额（单位：元）
        self.train_amount = train_amount
        self.vas_amount = vas_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_confirmed is not None:
            result['billConfirmed'] = self.bill_confirmed

        if self.car_amount is not None:
            result['carAmount'] = self.car_amount

        if self.damage_amount is not None:
            result['damageAmount'] = self.damage_amount

        if self.flight_amount is not None:
            result['flightAmount'] = self.flight_amount

        if self.fu_point is not None:
            result['fuPoint'] = self.fu_point

        if self.hotel_amount is not None:
            result['hotelAmount'] = self.hotel_amount

        if self.ie_flight_amount is not None:
            result['ieFlightAmount'] = self.ie_flight_amount

        if self.ie_hotel_amount is not None:
            result['ieHotelAmount'] = self.ie_hotel_amount

        if self.mail_bill_date is not None:
            result['mailBillDate'] = self.mail_bill_date

        if self.meal_amount is not None:
            result['mealAmount'] = self.meal_amount

        if self.service_amount is not None:
            result['serviceAmount'] = self.service_amount

        if self.train_amount is not None:
            result['trainAmount'] = self.train_amount

        if self.vas_amount is not None:
            result['vasAmount'] = self.vas_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billConfirmed') is not None:
            self.bill_confirmed = m.get('billConfirmed')

        if m.get('carAmount') is not None:
            self.car_amount = m.get('carAmount')

        if m.get('damageAmount') is not None:
            self.damage_amount = m.get('damageAmount')

        if m.get('flightAmount') is not None:
            self.flight_amount = m.get('flightAmount')

        if m.get('fuPoint') is not None:
            self.fu_point = m.get('fuPoint')

        if m.get('hotelAmount') is not None:
            self.hotel_amount = m.get('hotelAmount')

        if m.get('ieFlightAmount') is not None:
            self.ie_flight_amount = m.get('ieFlightAmount')

        if m.get('ieHotelAmount') is not None:
            self.ie_hotel_amount = m.get('ieHotelAmount')

        if m.get('mailBillDate') is not None:
            self.mail_bill_date = m.get('mailBillDate')

        if m.get('mealAmount') is not None:
            self.meal_amount = m.get('mealAmount')

        if m.get('serviceAmount') is not None:
            self.service_amount = m.get('serviceAmount')

        if m.get('trainAmount') is not None:
            self.train_amount = m.get('trainAmount')

        if m.get('vasAmount') is not None:
            self.vas_amount = m.get('vasAmount')

        return self

