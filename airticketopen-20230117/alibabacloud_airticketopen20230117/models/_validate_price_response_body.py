# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class ValidatePriceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ValidatePriceResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
        tracer_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success
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
            temp_model = main_models.ValidatePriceResponseBodyData()
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

class ValidatePriceResponseBodyData(DaraModel):
    def __init__(
        self,
        cancellation_policies: List[main_models.ValidatePriceResponseBodyDataCancellationPolicies] = None,
        item_offer_id: str = None,
        pricing: main_models.ValidatePriceResponseBodyDataPricing = None,
        tracer_id: str = None,
    ):
        self.cancellation_policies = cancellation_policies
        self.item_offer_id = item_offer_id
        self.pricing = pricing
        self.tracer_id = tracer_id

    def validate(self):
        if self.cancellation_policies:
            for v1 in self.cancellation_policies:
                 if v1:
                    v1.validate()
        if self.pricing:
            self.pricing.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CancellationPolicies'] = []
        if self.cancellation_policies is not None:
            for k1 in self.cancellation_policies:
                result['CancellationPolicies'].append(k1.to_map() if k1 else None)

        if self.item_offer_id is not None:
            result['ItemOfferId'] = self.item_offer_id

        if self.pricing is not None:
            result['Pricing'] = self.pricing.to_map()

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cancellation_policies = []
        if m.get('CancellationPolicies') is not None:
            for k1 in m.get('CancellationPolicies'):
                temp_model = main_models.ValidatePriceResponseBodyDataCancellationPolicies()
                self.cancellation_policies.append(temp_model.from_map(k1))

        if m.get('ItemOfferId') is not None:
            self.item_offer_id = m.get('ItemOfferId')

        if m.get('Pricing') is not None:
            temp_model = main_models.ValidatePriceResponseBodyDataPricing()
            self.pricing = temp_model.from_map(m.get('Pricing'))

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class ValidatePriceResponseBodyDataPricing(DaraModel):
    def __init__(
        self,
        currency: str = None,
        nightly_prices: List[main_models.ValidatePriceResponseBodyDataPricingNightlyPrices] = None,
        total_amount: str = None,
        tracer_id: str = None,
    ):
        self.currency = currency
        self.nightly_prices = nightly_prices
        self.total_amount = total_amount
        self.tracer_id = tracer_id

    def validate(self):
        if self.nightly_prices:
            for v1 in self.nightly_prices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        result['NightlyPrices'] = []
        if self.nightly_prices is not None:
            for k1 in self.nightly_prices:
                result['NightlyPrices'].append(k1.to_map() if k1 else None)

        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        self.nightly_prices = []
        if m.get('NightlyPrices') is not None:
            for k1 in m.get('NightlyPrices'):
                temp_model = main_models.ValidatePriceResponseBodyDataPricingNightlyPrices()
                self.nightly_prices.append(temp_model.from_map(k1))

        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class ValidatePriceResponseBodyDataPricingNightlyPrices(DaraModel):
    def __init__(
        self,
        amount: str = None,
        date: str = None,
        tracer_id: str = None,
    ):
        self.amount = amount
        self.date = date
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

        if self.date is not None:
            result['Date'] = self.date

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class ValidatePriceResponseBodyDataCancellationPolicies(DaraModel):
    def __init__(
        self,
        penalties: List[main_models.ValidatePriceResponseBodyDataCancellationPoliciesPenalties] = None,
        policy_type: str = None,
        tracer_id: str = None,
    ):
        self.penalties = penalties
        self.policy_type = policy_type
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
                temp_model = main_models.ValidatePriceResponseBodyDataCancellationPoliciesPenalties()
                self.penalties.append(temp_model.from_map(k1))

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class ValidatePriceResponseBodyDataCancellationPoliciesPenalties(DaraModel):
    def __init__(
        self,
        currency: str = None,
        end: int = None,
        penalty_type: str = None,
        penalty_value: str = None,
        start: int = None,
        tracer_id: str = None,
    ):
        self.currency = currency
        self.end = end
        self.penalty_type = penalty_type
        self.penalty_value = penalty_value
        self.start = start
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

