# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class DataHotelsValue(DaraModel):
    def __init__(
        self,
        check_in_date: str = None,
        check_out_date: str = None,
        rooms: List[main_models.DataHotelsValueRooms] = None,
        standard_room_id: str = None,
        offers: List[main_models.DataHotelsValueOffers] = None,
    ):
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.rooms = rooms
        self.standard_room_id = standard_room_id
        self.offers = offers

    def validate(self):
        if self.rooms:
            for v1 in self.rooms:
                 if v1:
                    v1.validate()
        if self.offers:
            for v1 in self.offers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_in_date is not None:
            result['CheckInDate'] = self.check_in_date

        if self.check_out_date is not None:
            result['CheckOutDate'] = self.check_out_date

        result['Rooms'] = []
        if self.rooms is not None:
            for k1 in self.rooms:
                result['Rooms'].append(k1.to_map() if k1 else None)

        if self.standard_room_id is not None:
            result['StandardRoomId'] = self.standard_room_id

        result['Offers'] = []
        if self.offers is not None:
            for k1 in self.offers:
                result['Offers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckInDate') is not None:
            self.check_in_date = m.get('CheckInDate')

        if m.get('CheckOutDate') is not None:
            self.check_out_date = m.get('CheckOutDate')

        self.rooms = []
        if m.get('Rooms') is not None:
            for k1 in m.get('Rooms'):
                temp_model = main_models.DataHotelsValueRooms()
                self.rooms.append(temp_model.from_map(k1))

        if m.get('StandardRoomId') is not None:
            self.standard_room_id = m.get('StandardRoomId')

        self.offers = []
        if m.get('Offers') is not None:
            for k1 in m.get('Offers'):
                temp_model = main_models.DataHotelsValueOffers()
                self.offers.append(temp_model.from_map(k1))

        return self

class DataHotelsValueOffers(DaraModel):
    def __init__(
        self,
        item_offer_key: str = None,
        rate_plan_name: str = None,
        meal_type: str = None,
        meal_count: int = None,
        cancel_policy: main_models.DataHotelsValueOffersCancelPolicy = None,
        selling_total_price: main_models.DataHotelsValueOffersSellingTotalPrice = None,
        selling_daily_prices: List[main_models.DataHotelsValueOffersSellingDailyPrices] = None,
        available_rooms: int = None,
        max_occupancy: int = None,
        confirm_type: str = None,
    ):
        self.item_offer_key = item_offer_key
        self.rate_plan_name = rate_plan_name
        self.meal_type = meal_type
        self.meal_count = meal_count
        self.cancel_policy = cancel_policy
        self.selling_total_price = selling_total_price
        self.selling_daily_prices = selling_daily_prices
        self.available_rooms = available_rooms
        self.max_occupancy = max_occupancy
        self.confirm_type = confirm_type

    def validate(self):
        if self.cancel_policy:
            self.cancel_policy.validate()
        if self.selling_total_price:
            self.selling_total_price.validate()
        if self.selling_daily_prices:
            for v1 in self.selling_daily_prices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_offer_key is not None:
            result['ItemOfferKey'] = self.item_offer_key

        if self.rate_plan_name is not None:
            result['RatePlanName'] = self.rate_plan_name

        if self.meal_type is not None:
            result['MealType'] = self.meal_type

        if self.meal_count is not None:
            result['MealCount'] = self.meal_count

        if self.cancel_policy is not None:
            result['CancelPolicy'] = self.cancel_policy.to_map()

        if self.selling_total_price is not None:
            result['SellingTotalPrice'] = self.selling_total_price.to_map()

        result['SellingDailyPrices'] = []
        if self.selling_daily_prices is not None:
            for k1 in self.selling_daily_prices:
                result['SellingDailyPrices'].append(k1.to_map() if k1 else None)

        if self.available_rooms is not None:
            result['AvailableRooms'] = self.available_rooms

        if self.max_occupancy is not None:
            result['MaxOccupancy'] = self.max_occupancy

        if self.confirm_type is not None:
            result['ConfirmType'] = self.confirm_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemOfferKey') is not None:
            self.item_offer_key = m.get('ItemOfferKey')

        if m.get('RatePlanName') is not None:
            self.rate_plan_name = m.get('RatePlanName')

        if m.get('MealType') is not None:
            self.meal_type = m.get('MealType')

        if m.get('MealCount') is not None:
            self.meal_count = m.get('MealCount')

        if m.get('CancelPolicy') is not None:
            temp_model = main_models.DataHotelsValueOffersCancelPolicy()
            self.cancel_policy = temp_model.from_map(m.get('CancelPolicy'))

        if m.get('SellingTotalPrice') is not None:
            temp_model = main_models.DataHotelsValueOffersSellingTotalPrice()
            self.selling_total_price = temp_model.from_map(m.get('SellingTotalPrice'))

        self.selling_daily_prices = []
        if m.get('SellingDailyPrices') is not None:
            for k1 in m.get('SellingDailyPrices'):
                temp_model = main_models.DataHotelsValueOffersSellingDailyPrices()
                self.selling_daily_prices.append(temp_model.from_map(k1))

        if m.get('AvailableRooms') is not None:
            self.available_rooms = m.get('AvailableRooms')

        if m.get('MaxOccupancy') is not None:
            self.max_occupancy = m.get('MaxOccupancy')

        if m.get('ConfirmType') is not None:
            self.confirm_type = m.get('ConfirmType')

        return self

class DataHotelsValueOffersSellingDailyPrices(DaraModel):
    def __init__(
        self,
        date: str = None,
        price: main_models.DataHotelsValueOffersSellingDailyPricesPrice = None,
        tracer_id: str = None,
    ):
        self.date = date
        self.price = price
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
            temp_model = main_models.DataHotelsValueOffersSellingDailyPricesPrice()
            self.price = temp_model.from_map(m.get('Price'))

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class DataHotelsValueOffersSellingDailyPricesPrice(DaraModel):
    def __init__(
        self,
        amount: float = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        self.amount = amount
        self.currency = currency
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

class DataHotelsValueOffersSellingTotalPrice(DaraModel):
    def __init__(
        self,
        amount: float = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        self.amount = amount
        self.currency = currency
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

class DataHotelsValueOffersCancelPolicy(DaraModel):
    def __init__(
        self,
        policy_type: str = None,
        penalties: List[main_models.DataHotelsValueOffersCancelPolicyPenalties] = None,
        tracer_id: str = None,
    ):
        self.policy_type = policy_type
        self.penalties = penalties
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
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        result['Penalties'] = []
        if self.penalties is not None:
            for k1 in self.penalties:
                result['Penalties'].append(k1.to_map() if k1 else None)

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        self.penalties = []
        if m.get('Penalties') is not None:
            for k1 in m.get('Penalties'):
                temp_model = main_models.DataHotelsValueOffersCancelPolicyPenalties()
                self.penalties.append(temp_model.from_map(k1))

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class DataHotelsValueOffersCancelPolicyPenalties(DaraModel):
    def __init__(
        self,
        start: int = None,
        end: int = None,
        penalty_type: str = None,
        penalty_value: str = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        self.start = start
        self.end = end
        self.penalty_type = penalty_type
        self.penalty_value = penalty_value
        self.currency = currency
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.start is not None:
            result['Start'] = self.start

        if self.end is not None:
            result['End'] = self.end

        if self.penalty_type is not None:
            result['PenaltyType'] = self.penalty_type

        if self.penalty_value is not None:
            result['PenaltyValue'] = self.penalty_value

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('PenaltyType') is not None:
            self.penalty_type = m.get('PenaltyType')

        if m.get('PenaltyValue') is not None:
            self.penalty_value = m.get('PenaltyValue')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class DataHotelsValueRooms(DaraModel):
    def __init__(
        self,
        standard_room_id: str = None,
        lowest_selling_price: main_models.DataHotelsValueRoomsLowestSellingPrice = None,
        offers: List[main_models.DataHotelsValueRoomsOffers] = None,
    ):
        self.standard_room_id = standard_room_id
        self.lowest_selling_price = lowest_selling_price
        self.offers = offers

    def validate(self):
        if self.lowest_selling_price:
            self.lowest_selling_price.validate()
        if self.offers:
            for v1 in self.offers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.standard_room_id is not None:
            result['StandardRoomId'] = self.standard_room_id

        if self.lowest_selling_price is not None:
            result['LowestSellingPrice'] = self.lowest_selling_price.to_map()

        result['Offers'] = []
        if self.offers is not None:
            for k1 in self.offers:
                result['Offers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StandardRoomId') is not None:
            self.standard_room_id = m.get('StandardRoomId')

        if m.get('LowestSellingPrice') is not None:
            temp_model = main_models.DataHotelsValueRoomsLowestSellingPrice()
            self.lowest_selling_price = temp_model.from_map(m.get('LowestSellingPrice'))

        self.offers = []
        if m.get('Offers') is not None:
            for k1 in m.get('Offers'):
                temp_model = main_models.DataHotelsValueRoomsOffers()
                self.offers.append(temp_model.from_map(k1))

        return self

class DataHotelsValueRoomsOffers(DaraModel):
    def __init__(
        self,
        item_offer_key: str = None,
        rate_plan_name: str = None,
        meal_type: str = None,
        meal_count: int = None,
        cancel_policy: main_models.DataHotelsValueRoomsOffersCancelPolicy = None,
        selling_total_price: main_models.DataHotelsValueRoomsOffersSellingTotalPrice = None,
        selling_daily_prices: List[main_models.DataHotelsValueRoomsOffersSellingDailyPrices] = None,
        available_rooms: int = None,
        max_occupancy: int = None,
        confirm_type: str = None,
    ):
        self.item_offer_key = item_offer_key
        self.rate_plan_name = rate_plan_name
        self.meal_type = meal_type
        self.meal_count = meal_count
        self.cancel_policy = cancel_policy
        self.selling_total_price = selling_total_price
        self.selling_daily_prices = selling_daily_prices
        self.available_rooms = available_rooms
        self.max_occupancy = max_occupancy
        self.confirm_type = confirm_type

    def validate(self):
        if self.cancel_policy:
            self.cancel_policy.validate()
        if self.selling_total_price:
            self.selling_total_price.validate()
        if self.selling_daily_prices:
            for v1 in self.selling_daily_prices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_offer_key is not None:
            result['ItemOfferKey'] = self.item_offer_key

        if self.rate_plan_name is not None:
            result['RatePlanName'] = self.rate_plan_name

        if self.meal_type is not None:
            result['MealType'] = self.meal_type

        if self.meal_count is not None:
            result['MealCount'] = self.meal_count

        if self.cancel_policy is not None:
            result['CancelPolicy'] = self.cancel_policy.to_map()

        if self.selling_total_price is not None:
            result['SellingTotalPrice'] = self.selling_total_price.to_map()

        result['SellingDailyPrices'] = []
        if self.selling_daily_prices is not None:
            for k1 in self.selling_daily_prices:
                result['SellingDailyPrices'].append(k1.to_map() if k1 else None)

        if self.available_rooms is not None:
            result['AvailableRooms'] = self.available_rooms

        if self.max_occupancy is not None:
            result['MaxOccupancy'] = self.max_occupancy

        if self.confirm_type is not None:
            result['ConfirmType'] = self.confirm_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemOfferKey') is not None:
            self.item_offer_key = m.get('ItemOfferKey')

        if m.get('RatePlanName') is not None:
            self.rate_plan_name = m.get('RatePlanName')

        if m.get('MealType') is not None:
            self.meal_type = m.get('MealType')

        if m.get('MealCount') is not None:
            self.meal_count = m.get('MealCount')

        if m.get('CancelPolicy') is not None:
            temp_model = main_models.DataHotelsValueRoomsOffersCancelPolicy()
            self.cancel_policy = temp_model.from_map(m.get('CancelPolicy'))

        if m.get('SellingTotalPrice') is not None:
            temp_model = main_models.DataHotelsValueRoomsOffersSellingTotalPrice()
            self.selling_total_price = temp_model.from_map(m.get('SellingTotalPrice'))

        self.selling_daily_prices = []
        if m.get('SellingDailyPrices') is not None:
            for k1 in m.get('SellingDailyPrices'):
                temp_model = main_models.DataHotelsValueRoomsOffersSellingDailyPrices()
                self.selling_daily_prices.append(temp_model.from_map(k1))

        if m.get('AvailableRooms') is not None:
            self.available_rooms = m.get('AvailableRooms')

        if m.get('MaxOccupancy') is not None:
            self.max_occupancy = m.get('MaxOccupancy')

        if m.get('ConfirmType') is not None:
            self.confirm_type = m.get('ConfirmType')

        return self

class DataHotelsValueRoomsOffersSellingDailyPrices(DaraModel):
    def __init__(
        self,
        date: str = None,
        price: main_models.DataHotelsValueRoomsOffersSellingDailyPricesPrice = None,
        tracer_id: str = None,
    ):
        self.date = date
        self.price = price
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
            temp_model = main_models.DataHotelsValueRoomsOffersSellingDailyPricesPrice()
            self.price = temp_model.from_map(m.get('Price'))

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class DataHotelsValueRoomsOffersSellingDailyPricesPrice(DaraModel):
    def __init__(
        self,
        amount: float = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        self.amount = amount
        self.currency = currency
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

class DataHotelsValueRoomsOffersSellingTotalPrice(DaraModel):
    def __init__(
        self,
        amount: float = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        self.amount = amount
        self.currency = currency
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

class DataHotelsValueRoomsOffersCancelPolicy(DaraModel):
    def __init__(
        self,
        policy_type: str = None,
        penalties: List[main_models.DataHotelsValueRoomsOffersCancelPolicyPenalties] = None,
        tracer_id: str = None,
    ):
        self.policy_type = policy_type
        self.penalties = penalties
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
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        result['Penalties'] = []
        if self.penalties is not None:
            for k1 in self.penalties:
                result['Penalties'].append(k1.to_map() if k1 else None)

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        self.penalties = []
        if m.get('Penalties') is not None:
            for k1 in m.get('Penalties'):
                temp_model = main_models.DataHotelsValueRoomsOffersCancelPolicyPenalties()
                self.penalties.append(temp_model.from_map(k1))

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class DataHotelsValueRoomsOffersCancelPolicyPenalties(DaraModel):
    def __init__(
        self,
        start: int = None,
        end: int = None,
        penalty_type: str = None,
        penalty_value: str = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        self.start = start
        self.end = end
        self.penalty_type = penalty_type
        self.penalty_value = penalty_value
        self.currency = currency
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.start is not None:
            result['Start'] = self.start

        if self.end is not None:
            result['End'] = self.end

        if self.penalty_type is not None:
            result['PenaltyType'] = self.penalty_type

        if self.penalty_value is not None:
            result['PenaltyValue'] = self.penalty_value

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('PenaltyType') is not None:
            self.penalty_type = m.get('PenaltyType')

        if m.get('PenaltyValue') is not None:
            self.penalty_value = m.get('PenaltyValue')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class DataHotelsValueRoomsLowestSellingPrice(DaraModel):
    def __init__(
        self,
        amount: float = None,
        currency: str = None,
        tracer_id: str = None,
    ):
        self.amount = amount
        self.currency = currency
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

