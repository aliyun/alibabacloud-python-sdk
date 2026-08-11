# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class GlobalHotelValidatePriceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GlobalHotelValidatePriceResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        tracer_id: str = None,
    ):
        # The business data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The unique request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # TracerId
        self.tracer_id = tracer_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GlobalHotelValidatePriceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelValidatePriceResponseBodyData(DaraModel):
    def __init__(
        self,
        cancellation_policies: List[main_models.GlobalHotelValidatePriceResponseBodyDataCancellationPolicies] = None,
        daily_prices: List[main_models.GlobalHotelValidatePriceResponseBodyDataDailyPrices] = None,
        item_offer_id: str = None,
        total_price: main_models.GlobalHotelValidatePriceResponseBodyDataTotalPrice = None,
        tracer_id: str = None,
    ):
        # The cancellation policies.
        self.cancellation_policies = cancellation_policies
        # The list of daily prices.
        self.daily_prices = daily_prices
        # The price validation result ID, used for subsequent order creation.
        self.item_offer_id = item_offer_id
        # The total selling price.
        self.total_price = total_price
        # TracerId
        self.tracer_id = tracer_id

    def validate(self):
        if self.cancellation_policies:
            for v1 in self.cancellation_policies:
                 if v1:
                    v1.validate()
        if self.daily_prices:
            for v1 in self.daily_prices:
                 if v1:
                    v1.validate()
        if self.total_price:
            self.total_price.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CancellationPolicies'] = []
        if self.cancellation_policies is not None:
            for k1 in self.cancellation_policies:
                result['CancellationPolicies'].append(k1.to_map() if k1 else None)

        result['DailyPrices'] = []
        if self.daily_prices is not None:
            for k1 in self.daily_prices:
                result['DailyPrices'].append(k1.to_map() if k1 else None)

        if self.item_offer_id is not None:
            result['ItemOfferId'] = self.item_offer_id

        if self.total_price is not None:
            result['TotalPrice'] = self.total_price.to_map()

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cancellation_policies = []
        if m.get('CancellationPolicies') is not None:
            for k1 in m.get('CancellationPolicies'):
                temp_model = main_models.GlobalHotelValidatePriceResponseBodyDataCancellationPolicies()
                self.cancellation_policies.append(temp_model.from_map(k1))

        self.daily_prices = []
        if m.get('DailyPrices') is not None:
            for k1 in m.get('DailyPrices'):
                temp_model = main_models.GlobalHotelValidatePriceResponseBodyDataDailyPrices()
                self.daily_prices.append(temp_model.from_map(k1))

        if m.get('ItemOfferId') is not None:
            self.item_offer_id = m.get('ItemOfferId')

        if m.get('TotalPrice') is not None:
            temp_model = main_models.GlobalHotelValidatePriceResponseBodyDataTotalPrice()
            self.total_price = temp_model.from_map(m.get('TotalPrice'))

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelValidatePriceResponseBodyDataTotalPrice(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        # The amount in the smallest currency unit.
        self.amount = amount
        # The currency code (ISO 4217).
        self.currency = currency
        # null
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelValidatePriceResponseBodyDataDailyPrices(DaraModel):
    def __init__(
        self,
        date: str = None,
        price: main_models.GlobalHotelValidatePriceResponseBodyDataDailyPricesPrice = None,
        tracer_id: str = None,
    ):
        # The date in yyyy-MM-dd format, in the local time zone of the hotel.
        self.date = date
        # The price for the night.
        self.price = price
        # null
        self.tracer_id = tracer_id

    def validate(self):
        if self.price:
            self.price.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.price is not None:
            result['Price'] = self.price.to_map()

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('Price') is not None:
            temp_model = main_models.GlobalHotelValidatePriceResponseBodyDataDailyPricesPrice()
            self.price = temp_model.from_map(m.get('Price'))

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelValidatePriceResponseBodyDataDailyPricesPrice(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        # The amount in the smallest currency unit.
        self.amount = amount
        # The currency code (ISO 4217).
        self.currency = currency
        # null
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelValidatePriceResponseBodyDataCancellationPolicies(DaraModel):
    def __init__(
        self,
        penalties: List[main_models.GlobalHotelValidatePriceResponseBodyDataCancellationPoliciesPenalties] = None,
        policy_type: str = None,
        tracer_id: str = None,
    ):
        # The list of cancellation penalty details.
        self.penalties = penalties
        # The cancellation policy type (FREE_CANCEL/CONDITIONAL/NON_REFUNDABLE).
        self.policy_type = policy_type
        # TracerId
        self.tracer_id = tracer_id

    def validate(self):
        if self.penalties:
            for v1 in self.penalties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Penalties'] = []
        if self.penalties is not None:
            for k1 in self.penalties:
                result['Penalties'].append(k1.to_map() if k1 else None)

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.penalties = []
        if m.get('Penalties') is not None:
            for k1 in m.get('Penalties'):
                temp_model = main_models.GlobalHotelValidatePriceResponseBodyDataCancellationPoliciesPenalties()
                self.penalties.append(temp_model.from_map(k1))

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class GlobalHotelValidatePriceResponseBodyDataCancellationPoliciesPenalties(DaraModel):
    def __init__(
        self,
        currency: str = None,
        end: str = None,
        penalty_type: str = None,
        penalty_value: str = None,
        start: str = None,
        tracer_id: str = None,
    ):
        # The currency code. This field has a value only when the penalty type is AMOUNT.
        self.currency = currency
        # The effective end time as a UTC millisecond timestamp.
        self.end = end
        # The penalty type (PERCENT/NIGHTS/NON_CANCELLABLE).
        self.penalty_type = penalty_type
        # The penalty value (percentage, amount, or number of nights). This field is not present when PenaltyType is NON_CANCELLABLE.
        self.penalty_value = penalty_value
        # The effective start time as a UTC millisecond timestamp.
        self.start = start
        # TracerId
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.end is not None:
            result['End'] = self.end

        if self.penalty_type is not None:
            result['PenaltyType'] = self.penalty_type

        if self.penalty_value is not None:
            result['PenaltyValue'] = self.penalty_value

        if self.start is not None:
            result['Start'] = self.start

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('PenaltyType') is not None:
            self.penalty_type = m.get('PenaltyType')

        if m.get('PenaltyValue') is not None:
            self.penalty_value = m.get('PenaltyValue')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

