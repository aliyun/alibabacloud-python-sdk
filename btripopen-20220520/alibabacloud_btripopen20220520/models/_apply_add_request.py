# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class ApplyAddRequest(DaraModel):
    def __init__(
        self,
        budget: int = None,
        budget_merge: int = None,
        car_rule: main_models.ApplyAddRequestCarRule = None,
        corp_name: str = None,
        default_standard: main_models.ApplyAddRequestDefaultStandard = None,
        depart_id: str = None,
        depart_name: str = None,
        extend_field: str = None,
        external_traveler_list: List[main_models.ApplyAddRequestExternalTravelerList] = None,
        external_traveler_standard: main_models.ApplyAddRequestExternalTravelerStandard = None,
        flight_budget: int = None,
        hotel_budget: int = None,
        hotel_share: main_models.ApplyAddRequestHotelShare = None,
        international_flight_cabins: str = None,
        intl_flight_budget: int = None,
        intl_hotel_budget: int = None,
        itinerary_list: List[main_models.ApplyAddRequestItineraryList] = None,
        itinerary_rule: int = None,
        itinerary_set_list: List[main_models.ApplyAddRequestItinerarySetList] = None,
        limit_traveler: int = None,
        meal_budget: int = None,
        payment_department_id: str = None,
        payment_department_name: str = None,
        status: int = None,
        sub_corp_id: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_business_id: str = None,
        thirdpart_depart_id: str = None,
        together_book_rule: int = None,
        train_budget: int = None,
        traveler_list: List[main_models.ApplyAddRequestTravelerList] = None,
        traveler_standard: List[main_models.ApplyAddRequestTravelerStandard] = None,
        trip_cause: str = None,
        trip_day: int = None,
        trip_title: str = None,
        type: int = None,
        union_no: str = None,
        user_id: str = None,
        user_name: str = None,
        vehicle_budget: int = None,
    ):
        self.budget = budget
        self.budget_merge = budget_merge
        self.car_rule = car_rule
        self.corp_name = corp_name
        self.default_standard = default_standard
        self.depart_id = depart_id
        self.depart_name = depart_name
        # 可将补充描述传入此字段，账单中将会体现此字段的值。可以用于企业的统计和对账
        self.extend_field = extend_field
        self.external_traveler_list = external_traveler_list
        self.external_traveler_standard = external_traveler_standard
        self.flight_budget = flight_budget
        self.hotel_budget = hotel_budget
        self.hotel_share = hotel_share
        self.international_flight_cabins = international_flight_cabins
        self.intl_flight_budget = intl_flight_budget
        self.intl_hotel_budget = intl_hotel_budget
        self.itinerary_list = itinerary_list
        self.itinerary_rule = itinerary_rule
        self.itinerary_set_list = itinerary_set_list
        self.limit_traveler = limit_traveler
        self.meal_budget = meal_budget
        self.payment_department_id = payment_department_id
        self.payment_department_name = payment_department_name
        self.status = status
        self.sub_corp_id = sub_corp_id
        # This parameter is required.
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_business_id = thirdpart_business_id
        self.thirdpart_depart_id = thirdpart_depart_id
        self.together_book_rule = together_book_rule
        self.train_budget = train_budget
        self.traveler_list = traveler_list
        self.traveler_standard = traveler_standard
        # This parameter is required.
        self.trip_cause = trip_cause
        self.trip_day = trip_day
        # This parameter is required.
        self.trip_title = trip_title
        self.type = type
        self.union_no = union_no
        # This parameter is required.
        self.user_id = user_id
        self.user_name = user_name
        self.vehicle_budget = vehicle_budget

    def validate(self):
        if self.car_rule:
            self.car_rule.validate()
        if self.default_standard:
            self.default_standard.validate()
        if self.external_traveler_list:
            for v1 in self.external_traveler_list:
                 if v1:
                    v1.validate()
        if self.external_traveler_standard:
            self.external_traveler_standard.validate()
        if self.hotel_share:
            self.hotel_share.validate()
        if self.itinerary_list:
            for v1 in self.itinerary_list:
                 if v1:
                    v1.validate()
        if self.itinerary_set_list:
            for v1 in self.itinerary_set_list:
                 if v1:
                    v1.validate()
        if self.traveler_list:
            for v1 in self.traveler_list:
                 if v1:
                    v1.validate()
        if self.traveler_standard:
            for v1 in self.traveler_standard:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.budget is not None:
            result['budget'] = self.budget

        if self.budget_merge is not None:
            result['budget_merge'] = self.budget_merge

        if self.car_rule is not None:
            result['car_rule'] = self.car_rule.to_map()

        if self.corp_name is not None:
            result['corp_name'] = self.corp_name

        if self.default_standard is not None:
            result['default_standard'] = self.default_standard.to_map()

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        if self.extend_field is not None:
            result['extend_field'] = self.extend_field

        result['external_traveler_list'] = []
        if self.external_traveler_list is not None:
            for k1 in self.external_traveler_list:
                result['external_traveler_list'].append(k1.to_map() if k1 else None)

        if self.external_traveler_standard is not None:
            result['external_traveler_standard'] = self.external_traveler_standard.to_map()

        if self.flight_budget is not None:
            result['flight_budget'] = self.flight_budget

        if self.hotel_budget is not None:
            result['hotel_budget'] = self.hotel_budget

        if self.hotel_share is not None:
            result['hotel_share'] = self.hotel_share.to_map()

        if self.international_flight_cabins is not None:
            result['international_flight_cabins'] = self.international_flight_cabins

        if self.intl_flight_budget is not None:
            result['intl_flight_budget'] = self.intl_flight_budget

        if self.intl_hotel_budget is not None:
            result['intl_hotel_budget'] = self.intl_hotel_budget

        result['itinerary_list'] = []
        if self.itinerary_list is not None:
            for k1 in self.itinerary_list:
                result['itinerary_list'].append(k1.to_map() if k1 else None)

        if self.itinerary_rule is not None:
            result['itinerary_rule'] = self.itinerary_rule

        result['itinerary_set_list'] = []
        if self.itinerary_set_list is not None:
            for k1 in self.itinerary_set_list:
                result['itinerary_set_list'].append(k1.to_map() if k1 else None)

        if self.limit_traveler is not None:
            result['limit_traveler'] = self.limit_traveler

        if self.meal_budget is not None:
            result['meal_budget'] = self.meal_budget

        if self.payment_department_id is not None:
            result['payment_department_id'] = self.payment_department_id

        if self.payment_department_name is not None:
            result['payment_department_name'] = self.payment_department_name

        if self.status is not None:
            result['status'] = self.status

        if self.sub_corp_id is not None:
            result['sub_corp_id'] = self.sub_corp_id

        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id

        if self.thirdpart_business_id is not None:
            result['thirdpart_business_id'] = self.thirdpart_business_id

        if self.thirdpart_depart_id is not None:
            result['thirdpart_depart_id'] = self.thirdpart_depart_id

        if self.together_book_rule is not None:
            result['together_book_rule'] = self.together_book_rule

        if self.train_budget is not None:
            result['train_budget'] = self.train_budget

        result['traveler_list'] = []
        if self.traveler_list is not None:
            for k1 in self.traveler_list:
                result['traveler_list'].append(k1.to_map() if k1 else None)

        result['traveler_standard'] = []
        if self.traveler_standard is not None:
            for k1 in self.traveler_standard:
                result['traveler_standard'].append(k1.to_map() if k1 else None)

        if self.trip_cause is not None:
            result['trip_cause'] = self.trip_cause

        if self.trip_day is not None:
            result['trip_day'] = self.trip_day

        if self.trip_title is not None:
            result['trip_title'] = self.trip_title

        if self.type is not None:
            result['type'] = self.type

        if self.union_no is not None:
            result['union_no'] = self.union_no

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        if self.vehicle_budget is not None:
            result['vehicle_budget'] = self.vehicle_budget

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('budget') is not None:
            self.budget = m.get('budget')

        if m.get('budget_merge') is not None:
            self.budget_merge = m.get('budget_merge')

        if m.get('car_rule') is not None:
            temp_model = main_models.ApplyAddRequestCarRule()
            self.car_rule = temp_model.from_map(m.get('car_rule'))

        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        if m.get('default_standard') is not None:
            temp_model = main_models.ApplyAddRequestDefaultStandard()
            self.default_standard = temp_model.from_map(m.get('default_standard'))

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        if m.get('extend_field') is not None:
            self.extend_field = m.get('extend_field')

        self.external_traveler_list = []
        if m.get('external_traveler_list') is not None:
            for k1 in m.get('external_traveler_list'):
                temp_model = main_models.ApplyAddRequestExternalTravelerList()
                self.external_traveler_list.append(temp_model.from_map(k1))

        if m.get('external_traveler_standard') is not None:
            temp_model = main_models.ApplyAddRequestExternalTravelerStandard()
            self.external_traveler_standard = temp_model.from_map(m.get('external_traveler_standard'))

        if m.get('flight_budget') is not None:
            self.flight_budget = m.get('flight_budget')

        if m.get('hotel_budget') is not None:
            self.hotel_budget = m.get('hotel_budget')

        if m.get('hotel_share') is not None:
            temp_model = main_models.ApplyAddRequestHotelShare()
            self.hotel_share = temp_model.from_map(m.get('hotel_share'))

        if m.get('international_flight_cabins') is not None:
            self.international_flight_cabins = m.get('international_flight_cabins')

        if m.get('intl_flight_budget') is not None:
            self.intl_flight_budget = m.get('intl_flight_budget')

        if m.get('intl_hotel_budget') is not None:
            self.intl_hotel_budget = m.get('intl_hotel_budget')

        self.itinerary_list = []
        if m.get('itinerary_list') is not None:
            for k1 in m.get('itinerary_list'):
                temp_model = main_models.ApplyAddRequestItineraryList()
                self.itinerary_list.append(temp_model.from_map(k1))

        if m.get('itinerary_rule') is not None:
            self.itinerary_rule = m.get('itinerary_rule')

        self.itinerary_set_list = []
        if m.get('itinerary_set_list') is not None:
            for k1 in m.get('itinerary_set_list'):
                temp_model = main_models.ApplyAddRequestItinerarySetList()
                self.itinerary_set_list.append(temp_model.from_map(k1))

        if m.get('limit_traveler') is not None:
            self.limit_traveler = m.get('limit_traveler')

        if m.get('meal_budget') is not None:
            self.meal_budget = m.get('meal_budget')

        if m.get('payment_department_id') is not None:
            self.payment_department_id = m.get('payment_department_id')

        if m.get('payment_department_name') is not None:
            self.payment_department_name = m.get('payment_department_name')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('sub_corp_id') is not None:
            self.sub_corp_id = m.get('sub_corp_id')

        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')

        if m.get('thirdpart_business_id') is not None:
            self.thirdpart_business_id = m.get('thirdpart_business_id')

        if m.get('thirdpart_depart_id') is not None:
            self.thirdpart_depart_id = m.get('thirdpart_depart_id')

        if m.get('together_book_rule') is not None:
            self.together_book_rule = m.get('together_book_rule')

        if m.get('train_budget') is not None:
            self.train_budget = m.get('train_budget')

        self.traveler_list = []
        if m.get('traveler_list') is not None:
            for k1 in m.get('traveler_list'):
                temp_model = main_models.ApplyAddRequestTravelerList()
                self.traveler_list.append(temp_model.from_map(k1))

        self.traveler_standard = []
        if m.get('traveler_standard') is not None:
            for k1 in m.get('traveler_standard'):
                temp_model = main_models.ApplyAddRequestTravelerStandard()
                self.traveler_standard.append(temp_model.from_map(k1))

        if m.get('trip_cause') is not None:
            self.trip_cause = m.get('trip_cause')

        if m.get('trip_day') is not None:
            self.trip_day = m.get('trip_day')

        if m.get('trip_title') is not None:
            self.trip_title = m.get('trip_title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('union_no') is not None:
            self.union_no = m.get('union_no')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        if m.get('vehicle_budget') is not None:
            self.vehicle_budget = m.get('vehicle_budget')

        return self

class ApplyAddRequestTravelerStandard(DaraModel):
    def __init__(
        self,
        business_discount: int = None,
        car_city_set: List[main_models.ApplyAddRequestTravelerStandardCarCitySet] = None,
        economy_discount: int = None,
        first_discount: int = None,
        flight_cabins: str = None,
        flight_intl_rule_code: int = None,
        flight_rule_code: int = None,
        hotel_citys: List[main_models.ApplyAddRequestTravelerStandardHotelCitys] = None,
        hotel_intl_citys: List[main_models.ApplyAddRequestTravelerStandardHotelIntlCitys] = None,
        hotel_intl_rule_code: int = None,
        hotel_rule_code: int = None,
        international_flight_cabins: str = None,
        premium_economy_discount: int = None,
        reserve_type: int = None,
        train_rule_code: int = None,
        train_seats: str = None,
        user_id: str = None,
    ):
        self.business_discount = business_discount
        self.car_city_set = car_city_set
        self.economy_discount = economy_discount
        self.first_discount = first_discount
        self.flight_cabins = flight_cabins
        self.flight_intl_rule_code = flight_intl_rule_code
        self.flight_rule_code = flight_rule_code
        self.hotel_citys = hotel_citys
        self.hotel_intl_citys = hotel_intl_citys
        self.hotel_intl_rule_code = hotel_intl_rule_code
        self.hotel_rule_code = hotel_rule_code
        self.international_flight_cabins = international_flight_cabins
        self.premium_economy_discount = premium_economy_discount
        self.reserve_type = reserve_type
        self.train_rule_code = train_rule_code
        self.train_seats = train_seats
        self.user_id = user_id

    def validate(self):
        if self.car_city_set:
            for v1 in self.car_city_set:
                 if v1:
                    v1.validate()
        if self.hotel_citys:
            for v1 in self.hotel_citys:
                 if v1:
                    v1.validate()
        if self.hotel_intl_citys:
            for v1 in self.hotel_intl_citys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_discount is not None:
            result['business_discount'] = self.business_discount

        result['car_city_set'] = []
        if self.car_city_set is not None:
            for k1 in self.car_city_set:
                result['car_city_set'].append(k1.to_map() if k1 else None)

        if self.economy_discount is not None:
            result['economy_discount'] = self.economy_discount

        if self.first_discount is not None:
            result['first_discount'] = self.first_discount

        if self.flight_cabins is not None:
            result['flight_cabins'] = self.flight_cabins

        if self.flight_intl_rule_code is not None:
            result['flight_intl_rule_code'] = self.flight_intl_rule_code

        if self.flight_rule_code is not None:
            result['flight_rule_code'] = self.flight_rule_code

        result['hotel_citys'] = []
        if self.hotel_citys is not None:
            for k1 in self.hotel_citys:
                result['hotel_citys'].append(k1.to_map() if k1 else None)

        result['hotel_intl_citys'] = []
        if self.hotel_intl_citys is not None:
            for k1 in self.hotel_intl_citys:
                result['hotel_intl_citys'].append(k1.to_map() if k1 else None)

        if self.hotel_intl_rule_code is not None:
            result['hotel_intl_rule_code'] = self.hotel_intl_rule_code

        if self.hotel_rule_code is not None:
            result['hotel_rule_code'] = self.hotel_rule_code

        if self.international_flight_cabins is not None:
            result['international_flight_cabins'] = self.international_flight_cabins

        if self.premium_economy_discount is not None:
            result['premium_economy_discount'] = self.premium_economy_discount

        if self.reserve_type is not None:
            result['reserve_type'] = self.reserve_type

        if self.train_rule_code is not None:
            result['train_rule_code'] = self.train_rule_code

        if self.train_seats is not None:
            result['train_seats'] = self.train_seats

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('business_discount') is not None:
            self.business_discount = m.get('business_discount')

        self.car_city_set = []
        if m.get('car_city_set') is not None:
            for k1 in m.get('car_city_set'):
                temp_model = main_models.ApplyAddRequestTravelerStandardCarCitySet()
                self.car_city_set.append(temp_model.from_map(k1))

        if m.get('economy_discount') is not None:
            self.economy_discount = m.get('economy_discount')

        if m.get('first_discount') is not None:
            self.first_discount = m.get('first_discount')

        if m.get('flight_cabins') is not None:
            self.flight_cabins = m.get('flight_cabins')

        if m.get('flight_intl_rule_code') is not None:
            self.flight_intl_rule_code = m.get('flight_intl_rule_code')

        if m.get('flight_rule_code') is not None:
            self.flight_rule_code = m.get('flight_rule_code')

        self.hotel_citys = []
        if m.get('hotel_citys') is not None:
            for k1 in m.get('hotel_citys'):
                temp_model = main_models.ApplyAddRequestTravelerStandardHotelCitys()
                self.hotel_citys.append(temp_model.from_map(k1))

        self.hotel_intl_citys = []
        if m.get('hotel_intl_citys') is not None:
            for k1 in m.get('hotel_intl_citys'):
                temp_model = main_models.ApplyAddRequestTravelerStandardHotelIntlCitys()
                self.hotel_intl_citys.append(temp_model.from_map(k1))

        if m.get('hotel_intl_rule_code') is not None:
            self.hotel_intl_rule_code = m.get('hotel_intl_rule_code')

        if m.get('hotel_rule_code') is not None:
            self.hotel_rule_code = m.get('hotel_rule_code')

        if m.get('international_flight_cabins') is not None:
            self.international_flight_cabins = m.get('international_flight_cabins')

        if m.get('premium_economy_discount') is not None:
            self.premium_economy_discount = m.get('premium_economy_discount')

        if m.get('reserve_type') is not None:
            self.reserve_type = m.get('reserve_type')

        if m.get('train_rule_code') is not None:
            self.train_rule_code = m.get('train_rule_code')

        if m.get('train_seats') is not None:
            self.train_seats = m.get('train_seats')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class ApplyAddRequestTravelerStandardHotelIntlCitys(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        fee: int = None,
    ):
        self.city_code = city_code
        self.city_name = city_name
        self.fee = fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.fee is not None:
            result['fee'] = self.fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('fee') is not None:
            self.fee = m.get('fee')

        return self

class ApplyAddRequestTravelerStandardHotelCitys(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        fee: int = None,
    ):
        self.city_code = city_code
        self.city_name = city_name
        self.fee = fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.fee is not None:
            result['fee'] = self.fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('fee') is not None:
            self.fee = m.get('fee')

        return self

class ApplyAddRequestTravelerStandardCarCitySet(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
    ):
        # This parameter is required.
        self.city_code = city_code
        # This parameter is required.
        self.city_name = city_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        return self

class ApplyAddRequestTravelerList(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        cost_center_id: int = None,
        invoice_id: int = None,
        payment_department_id: str = None,
        payment_department_name: str = None,
        project_code: str = None,
        project_title: str = None,
        third_part_invoice_id: str = None,
        thirdpart_cost_center_id: str = None,
        thirdpart_depart_id: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.attribute = attribute
        self.cost_center_id = cost_center_id
        self.invoice_id = invoice_id
        self.payment_department_id = payment_department_id
        self.payment_department_name = payment_department_name
        self.project_code = project_code
        self.project_title = project_title
        self.third_part_invoice_id = third_part_invoice_id
        self.thirdpart_cost_center_id = thirdpart_cost_center_id
        self.thirdpart_depart_id = thirdpart_depart_id
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['attribute'] = self.attribute

        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id

        if self.invoice_id is not None:
            result['invoice_id'] = self.invoice_id

        if self.payment_department_id is not None:
            result['payment_department_id'] = self.payment_department_id

        if self.payment_department_name is not None:
            result['payment_department_name'] = self.payment_department_name

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id

        if self.thirdpart_cost_center_id is not None:
            result['thirdpart_cost_center_id'] = self.thirdpart_cost_center_id

        if self.thirdpart_depart_id is not None:
            result['thirdpart_depart_id'] = self.thirdpart_depart_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')

        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('invoice_id') is not None:
            self.invoice_id = m.get('invoice_id')

        if m.get('payment_department_id') is not None:
            self.payment_department_id = m.get('payment_department_id')

        if m.get('payment_department_name') is not None:
            self.payment_department_name = m.get('payment_department_name')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')

        if m.get('thirdpart_cost_center_id') is not None:
            self.thirdpart_cost_center_id = m.get('thirdpart_cost_center_id')

        if m.get('thirdpart_depart_id') is not None:
            self.thirdpart_depart_id = m.get('thirdpart_depart_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class ApplyAddRequestItinerarySetList(DaraModel):
    def __init__(
        self,
        arr_date: str = None,
        attribute: str = None,
        city_code_set: str = None,
        city_set: str = None,
        cost_center_id: int = None,
        dep_date: str = None,
        invoice_id: int = None,
        itinerary_id: str = None,
        itinerary_travel_standard: main_models.ApplyAddRequestItinerarySetListItineraryTravelStandard = None,
        project_code: str = None,
        project_title: str = None,
        province_travel_city_adcodes: List[str] = None,
        third_part_invoice_id: str = None,
        thirdpart_cost_center_id: str = None,
        traffic_type: int = None,
    ):
        # This parameter is required.
        self.arr_date = arr_date
        self.attribute = attribute
        # This parameter is required.
        self.city_code_set = city_code_set
        # This parameter is required.
        self.city_set = city_set
        self.cost_center_id = cost_center_id
        # This parameter is required.
        self.dep_date = dep_date
        self.invoice_id = invoice_id
        # This parameter is required.
        self.itinerary_id = itinerary_id
        self.itinerary_travel_standard = itinerary_travel_standard
        self.project_code = project_code
        self.project_title = project_title
        self.province_travel_city_adcodes = province_travel_city_adcodes
        self.third_part_invoice_id = third_part_invoice_id
        self.thirdpart_cost_center_id = thirdpart_cost_center_id
        # This parameter is required.
        self.traffic_type = traffic_type

    def validate(self):
        if self.itinerary_travel_standard:
            self.itinerary_travel_standard.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_date is not None:
            result['arr_date'] = self.arr_date

        if self.attribute is not None:
            result['attribute'] = self.attribute

        if self.city_code_set is not None:
            result['city_code_set'] = self.city_code_set

        if self.city_set is not None:
            result['city_set'] = self.city_set

        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.invoice_id is not None:
            result['invoice_id'] = self.invoice_id

        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id

        if self.itinerary_travel_standard is not None:
            result['itinerary_travel_standard'] = self.itinerary_travel_standard.to_map()

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.province_travel_city_adcodes is not None:
            result['province_travel_city_adcodes'] = self.province_travel_city_adcodes

        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id

        if self.thirdpart_cost_center_id is not None:
            result['thirdpart_cost_center_id'] = self.thirdpart_cost_center_id

        if self.traffic_type is not None:
            result['traffic_type'] = self.traffic_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')

        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')

        if m.get('city_code_set') is not None:
            self.city_code_set = m.get('city_code_set')

        if m.get('city_set') is not None:
            self.city_set = m.get('city_set')

        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('invoice_id') is not None:
            self.invoice_id = m.get('invoice_id')

        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')

        if m.get('itinerary_travel_standard') is not None:
            temp_model = main_models.ApplyAddRequestItinerarySetListItineraryTravelStandard()
            self.itinerary_travel_standard = temp_model.from_map(m.get('itinerary_travel_standard'))

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('province_travel_city_adcodes') is not None:
            self.province_travel_city_adcodes = m.get('province_travel_city_adcodes')

        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')

        if m.get('thirdpart_cost_center_id') is not None:
            self.thirdpart_cost_center_id = m.get('thirdpart_cost_center_id')

        if m.get('traffic_type') is not None:
            self.traffic_type = m.get('traffic_type')

        return self

class ApplyAddRequestItinerarySetListItineraryTravelStandard(DaraModel):
    def __init__(
        self,
        hotel_available_nights_per_day: int = None,
    ):
        self.hotel_available_nights_per_day = hotel_available_nights_per_day

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_available_nights_per_day is not None:
            result['hotel_available_nights_per_day'] = self.hotel_available_nights_per_day

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hotel_available_nights_per_day') is not None:
            self.hotel_available_nights_per_day = m.get('hotel_available_nights_per_day')

        return self

class ApplyAddRequestItineraryList(DaraModel):
    def __init__(
        self,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_date: str = None,
        attribute: str = None,
        cost_center_id: int = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_date: str = None,
        invoice_id: int = None,
        itinerary_id: str = None,
        itinerary_travel_standard: main_models.ApplyAddRequestItineraryListItineraryTravelStandard = None,
        need_hotel: bool = None,
        need_traffic: bool = None,
        project_code: str = None,
        project_title: str = None,
        province_travel_city_adcodes: List[str] = None,
        third_part_invoice_id: str = None,
        thirdpart_cost_center_id: str = None,
        traffic_type: int = None,
        trip_way: int = None,
    ):
        # This parameter is required.
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        # This parameter is required.
        self.arr_date = arr_date
        self.attribute = attribute
        self.cost_center_id = cost_center_id
        # This parameter is required.
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        # This parameter is required.
        self.dep_date = dep_date
        self.invoice_id = invoice_id
        # This parameter is required.
        self.itinerary_id = itinerary_id
        self.itinerary_travel_standard = itinerary_travel_standard
        self.need_hotel = need_hotel
        self.need_traffic = need_traffic
        self.project_code = project_code
        self.project_title = project_title
        self.province_travel_city_adcodes = province_travel_city_adcodes
        self.third_part_invoice_id = third_part_invoice_id
        self.thirdpart_cost_center_id = thirdpart_cost_center_id
        # This parameter is required.
        self.traffic_type = traffic_type
        # This parameter is required.
        self.trip_way = trip_way

    def validate(self):
        if self.itinerary_travel_standard:
            self.itinerary_travel_standard.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_date is not None:
            result['arr_date'] = self.arr_date

        if self.attribute is not None:
            result['attribute'] = self.attribute

        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.invoice_id is not None:
            result['invoice_id'] = self.invoice_id

        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id

        if self.itinerary_travel_standard is not None:
            result['itinerary_travel_standard'] = self.itinerary_travel_standard.to_map()

        if self.need_hotel is not None:
            result['need_hotel'] = self.need_hotel

        if self.need_traffic is not None:
            result['need_traffic'] = self.need_traffic

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.province_travel_city_adcodes is not None:
            result['province_travel_city_adcodes'] = self.province_travel_city_adcodes

        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id

        if self.thirdpart_cost_center_id is not None:
            result['thirdpart_cost_center_id'] = self.thirdpart_cost_center_id

        if self.traffic_type is not None:
            result['traffic_type'] = self.traffic_type

        if self.trip_way is not None:
            result['trip_way'] = self.trip_way

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')

        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')

        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('invoice_id') is not None:
            self.invoice_id = m.get('invoice_id')

        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')

        if m.get('itinerary_travel_standard') is not None:
            temp_model = main_models.ApplyAddRequestItineraryListItineraryTravelStandard()
            self.itinerary_travel_standard = temp_model.from_map(m.get('itinerary_travel_standard'))

        if m.get('need_hotel') is not None:
            self.need_hotel = m.get('need_hotel')

        if m.get('need_traffic') is not None:
            self.need_traffic = m.get('need_traffic')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('province_travel_city_adcodes') is not None:
            self.province_travel_city_adcodes = m.get('province_travel_city_adcodes')

        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')

        if m.get('thirdpart_cost_center_id') is not None:
            self.thirdpart_cost_center_id = m.get('thirdpart_cost_center_id')

        if m.get('traffic_type') is not None:
            self.traffic_type = m.get('traffic_type')

        if m.get('trip_way') is not None:
            self.trip_way = m.get('trip_way')

        return self

class ApplyAddRequestItineraryListItineraryTravelStandard(DaraModel):
    def __init__(
        self,
        hotel_available_nights_per_day: int = None,
    ):
        self.hotel_available_nights_per_day = hotel_available_nights_per_day

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_available_nights_per_day is not None:
            result['hotel_available_nights_per_day'] = self.hotel_available_nights_per_day

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hotel_available_nights_per_day') is not None:
            self.hotel_available_nights_per_day = m.get('hotel_available_nights_per_day')

        return self

class ApplyAddRequestHotelShare(DaraModel):
    def __init__(
        self,
        param: str = None,
        type: str = None,
    ):
        self.param = param
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param is not None:
            result['param'] = self.param

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('param') is not None:
            self.param = m.get('param')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ApplyAddRequestExternalTravelerStandard(DaraModel):
    def __init__(
        self,
        business_discount: int = None,
        economy_discount: int = None,
        first_discount: int = None,
        flight_cabins: str = None,
        flight_intl_rule_code: int = None,
        flight_rule_code: int = None,
        hotel_citys: List[main_models.ApplyAddRequestExternalTravelerStandardHotelCitys] = None,
        hotel_intl_citys: List[main_models.ApplyAddRequestExternalTravelerStandardHotelIntlCitys] = None,
        hotel_intl_rule_code: int = None,
        hotel_rule_code: int = None,
        international_flight_cabins: str = None,
        premium_economy_discount: int = None,
        reserve_type: int = None,
        train_rule_code: int = None,
        train_seats: str = None,
    ):
        self.business_discount = business_discount
        self.economy_discount = economy_discount
        self.first_discount = first_discount
        self.flight_cabins = flight_cabins
        self.flight_intl_rule_code = flight_intl_rule_code
        self.flight_rule_code = flight_rule_code
        self.hotel_citys = hotel_citys
        self.hotel_intl_citys = hotel_intl_citys
        self.hotel_intl_rule_code = hotel_intl_rule_code
        self.hotel_rule_code = hotel_rule_code
        self.international_flight_cabins = international_flight_cabins
        self.premium_economy_discount = premium_economy_discount
        self.reserve_type = reserve_type
        self.train_rule_code = train_rule_code
        self.train_seats = train_seats

    def validate(self):
        if self.hotel_citys:
            for v1 in self.hotel_citys:
                 if v1:
                    v1.validate()
        if self.hotel_intl_citys:
            for v1 in self.hotel_intl_citys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_discount is not None:
            result['business_discount'] = self.business_discount

        if self.economy_discount is not None:
            result['economy_discount'] = self.economy_discount

        if self.first_discount is not None:
            result['first_discount'] = self.first_discount

        if self.flight_cabins is not None:
            result['flight_cabins'] = self.flight_cabins

        if self.flight_intl_rule_code is not None:
            result['flight_intl_rule_code'] = self.flight_intl_rule_code

        if self.flight_rule_code is not None:
            result['flight_rule_code'] = self.flight_rule_code

        result['hotel_citys'] = []
        if self.hotel_citys is not None:
            for k1 in self.hotel_citys:
                result['hotel_citys'].append(k1.to_map() if k1 else None)

        result['hotel_intl_citys'] = []
        if self.hotel_intl_citys is not None:
            for k1 in self.hotel_intl_citys:
                result['hotel_intl_citys'].append(k1.to_map() if k1 else None)

        if self.hotel_intl_rule_code is not None:
            result['hotel_intl_rule_code'] = self.hotel_intl_rule_code

        if self.hotel_rule_code is not None:
            result['hotel_rule_code'] = self.hotel_rule_code

        if self.international_flight_cabins is not None:
            result['international_flight_cabins'] = self.international_flight_cabins

        if self.premium_economy_discount is not None:
            result['premium_economy_discount'] = self.premium_economy_discount

        if self.reserve_type is not None:
            result['reserve_type'] = self.reserve_type

        if self.train_rule_code is not None:
            result['train_rule_code'] = self.train_rule_code

        if self.train_seats is not None:
            result['train_seats'] = self.train_seats

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('business_discount') is not None:
            self.business_discount = m.get('business_discount')

        if m.get('economy_discount') is not None:
            self.economy_discount = m.get('economy_discount')

        if m.get('first_discount') is not None:
            self.first_discount = m.get('first_discount')

        if m.get('flight_cabins') is not None:
            self.flight_cabins = m.get('flight_cabins')

        if m.get('flight_intl_rule_code') is not None:
            self.flight_intl_rule_code = m.get('flight_intl_rule_code')

        if m.get('flight_rule_code') is not None:
            self.flight_rule_code = m.get('flight_rule_code')

        self.hotel_citys = []
        if m.get('hotel_citys') is not None:
            for k1 in m.get('hotel_citys'):
                temp_model = main_models.ApplyAddRequestExternalTravelerStandardHotelCitys()
                self.hotel_citys.append(temp_model.from_map(k1))

        self.hotel_intl_citys = []
        if m.get('hotel_intl_citys') is not None:
            for k1 in m.get('hotel_intl_citys'):
                temp_model = main_models.ApplyAddRequestExternalTravelerStandardHotelIntlCitys()
                self.hotel_intl_citys.append(temp_model.from_map(k1))

        if m.get('hotel_intl_rule_code') is not None:
            self.hotel_intl_rule_code = m.get('hotel_intl_rule_code')

        if m.get('hotel_rule_code') is not None:
            self.hotel_rule_code = m.get('hotel_rule_code')

        if m.get('international_flight_cabins') is not None:
            self.international_flight_cabins = m.get('international_flight_cabins')

        if m.get('premium_economy_discount') is not None:
            self.premium_economy_discount = m.get('premium_economy_discount')

        if m.get('reserve_type') is not None:
            self.reserve_type = m.get('reserve_type')

        if m.get('train_rule_code') is not None:
            self.train_rule_code = m.get('train_rule_code')

        if m.get('train_seats') is not None:
            self.train_seats = m.get('train_seats')

        return self

class ApplyAddRequestExternalTravelerStandardHotelIntlCitys(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        fee: int = None,
    ):
        self.city_code = city_code
        self.city_name = city_name
        self.fee = fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.fee is not None:
            result['fee'] = self.fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('fee') is not None:
            self.fee = m.get('fee')

        return self

class ApplyAddRequestExternalTravelerStandardHotelCitys(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        fee: int = None,
    ):
        self.city_code = city_code
        self.city_name = city_name
        self.fee = fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.fee is not None:
            result['fee'] = self.fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('fee') is not None:
            self.fee = m.get('fee')

        return self

class ApplyAddRequestExternalTravelerList(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        cost_center_id: int = None,
        external_user_id: str = None,
        invoice_id: int = None,
        payment_department_id: str = None,
        payment_department_name: str = None,
        project_code: str = None,
        project_title: str = None,
        third_part_invoice_id: str = None,
        thirdpart_cost_center_id: str = None,
        thirdpart_depart_id: str = None,
        user_name: str = None,
        user_name_en: str = None,
    ):
        self.attribute = attribute
        self.cost_center_id = cost_center_id
        self.external_user_id = external_user_id
        self.invoice_id = invoice_id
        self.payment_department_id = payment_department_id
        self.payment_department_name = payment_department_name
        self.project_code = project_code
        self.project_title = project_title
        self.third_part_invoice_id = third_part_invoice_id
        self.thirdpart_cost_center_id = thirdpart_cost_center_id
        self.thirdpart_depart_id = thirdpart_depart_id
        self.user_name = user_name
        self.user_name_en = user_name_en

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['attribute'] = self.attribute

        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id

        if self.external_user_id is not None:
            result['external_user_id'] = self.external_user_id

        if self.invoice_id is not None:
            result['invoice_id'] = self.invoice_id

        if self.payment_department_id is not None:
            result['payment_department_id'] = self.payment_department_id

        if self.payment_department_name is not None:
            result['payment_department_name'] = self.payment_department_name

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id

        if self.thirdpart_cost_center_id is not None:
            result['thirdpart_cost_center_id'] = self.thirdpart_cost_center_id

        if self.thirdpart_depart_id is not None:
            result['thirdpart_depart_id'] = self.thirdpart_depart_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        if self.user_name_en is not None:
            result['user_name_en'] = self.user_name_en

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')

        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('external_user_id') is not None:
            self.external_user_id = m.get('external_user_id')

        if m.get('invoice_id') is not None:
            self.invoice_id = m.get('invoice_id')

        if m.get('payment_department_id') is not None:
            self.payment_department_id = m.get('payment_department_id')

        if m.get('payment_department_name') is not None:
            self.payment_department_name = m.get('payment_department_name')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')

        if m.get('thirdpart_cost_center_id') is not None:
            self.thirdpart_cost_center_id = m.get('thirdpart_cost_center_id')

        if m.get('thirdpart_depart_id') is not None:
            self.thirdpart_depart_id = m.get('thirdpart_depart_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        if m.get('user_name_en') is not None:
            self.user_name_en = m.get('user_name_en')

        return self

class ApplyAddRequestDefaultStandard(DaraModel):
    def __init__(
        self,
        business_discount: int = None,
        economy_discount: int = None,
        first_discount: int = None,
        flight_cabins: str = None,
        flight_intl_rule_code: int = None,
        flight_rule_code: int = None,
        hotel_citys: List[main_models.ApplyAddRequestDefaultStandardHotelCitys] = None,
        hotel_intl_citys: List[main_models.ApplyAddRequestDefaultStandardHotelIntlCitys] = None,
        hotel_intl_rule_code: int = None,
        hotel_rule_code: int = None,
        international_flight_cabins: str = None,
        premium_economy_discount: int = None,
        reserve_type: int = None,
        train_rule_code: int = None,
        train_seats: str = None,
    ):
        self.business_discount = business_discount
        self.economy_discount = economy_discount
        self.first_discount = first_discount
        self.flight_cabins = flight_cabins
        self.flight_intl_rule_code = flight_intl_rule_code
        self.flight_rule_code = flight_rule_code
        self.hotel_citys = hotel_citys
        self.hotel_intl_citys = hotel_intl_citys
        self.hotel_intl_rule_code = hotel_intl_rule_code
        self.hotel_rule_code = hotel_rule_code
        self.international_flight_cabins = international_flight_cabins
        self.premium_economy_discount = premium_economy_discount
        self.reserve_type = reserve_type
        self.train_rule_code = train_rule_code
        self.train_seats = train_seats

    def validate(self):
        if self.hotel_citys:
            for v1 in self.hotel_citys:
                 if v1:
                    v1.validate()
        if self.hotel_intl_citys:
            for v1 in self.hotel_intl_citys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_discount is not None:
            result['business_discount'] = self.business_discount

        if self.economy_discount is not None:
            result['economy_discount'] = self.economy_discount

        if self.first_discount is not None:
            result['first_discount'] = self.first_discount

        if self.flight_cabins is not None:
            result['flight_cabins'] = self.flight_cabins

        if self.flight_intl_rule_code is not None:
            result['flight_intl_rule_code'] = self.flight_intl_rule_code

        if self.flight_rule_code is not None:
            result['flight_rule_code'] = self.flight_rule_code

        result['hotel_citys'] = []
        if self.hotel_citys is not None:
            for k1 in self.hotel_citys:
                result['hotel_citys'].append(k1.to_map() if k1 else None)

        result['hotel_intl_citys'] = []
        if self.hotel_intl_citys is not None:
            for k1 in self.hotel_intl_citys:
                result['hotel_intl_citys'].append(k1.to_map() if k1 else None)

        if self.hotel_intl_rule_code is not None:
            result['hotel_intl_rule_code'] = self.hotel_intl_rule_code

        if self.hotel_rule_code is not None:
            result['hotel_rule_code'] = self.hotel_rule_code

        if self.international_flight_cabins is not None:
            result['international_flight_cabins'] = self.international_flight_cabins

        if self.premium_economy_discount is not None:
            result['premium_economy_discount'] = self.premium_economy_discount

        if self.reserve_type is not None:
            result['reserve_type'] = self.reserve_type

        if self.train_rule_code is not None:
            result['train_rule_code'] = self.train_rule_code

        if self.train_seats is not None:
            result['train_seats'] = self.train_seats

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('business_discount') is not None:
            self.business_discount = m.get('business_discount')

        if m.get('economy_discount') is not None:
            self.economy_discount = m.get('economy_discount')

        if m.get('first_discount') is not None:
            self.first_discount = m.get('first_discount')

        if m.get('flight_cabins') is not None:
            self.flight_cabins = m.get('flight_cabins')

        if m.get('flight_intl_rule_code') is not None:
            self.flight_intl_rule_code = m.get('flight_intl_rule_code')

        if m.get('flight_rule_code') is not None:
            self.flight_rule_code = m.get('flight_rule_code')

        self.hotel_citys = []
        if m.get('hotel_citys') is not None:
            for k1 in m.get('hotel_citys'):
                temp_model = main_models.ApplyAddRequestDefaultStandardHotelCitys()
                self.hotel_citys.append(temp_model.from_map(k1))

        self.hotel_intl_citys = []
        if m.get('hotel_intl_citys') is not None:
            for k1 in m.get('hotel_intl_citys'):
                temp_model = main_models.ApplyAddRequestDefaultStandardHotelIntlCitys()
                self.hotel_intl_citys.append(temp_model.from_map(k1))

        if m.get('hotel_intl_rule_code') is not None:
            self.hotel_intl_rule_code = m.get('hotel_intl_rule_code')

        if m.get('hotel_rule_code') is not None:
            self.hotel_rule_code = m.get('hotel_rule_code')

        if m.get('international_flight_cabins') is not None:
            self.international_flight_cabins = m.get('international_flight_cabins')

        if m.get('premium_economy_discount') is not None:
            self.premium_economy_discount = m.get('premium_economy_discount')

        if m.get('reserve_type') is not None:
            self.reserve_type = m.get('reserve_type')

        if m.get('train_rule_code') is not None:
            self.train_rule_code = m.get('train_rule_code')

        if m.get('train_seats') is not None:
            self.train_seats = m.get('train_seats')

        return self

class ApplyAddRequestDefaultStandardHotelIntlCitys(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        fee: int = None,
    ):
        self.city_code = city_code
        self.city_name = city_name
        self.fee = fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.fee is not None:
            result['fee'] = self.fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('fee') is not None:
            self.fee = m.get('fee')

        return self

class ApplyAddRequestDefaultStandardHotelCitys(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
        fee: int = None,
    ):
        self.city_code = city_code
        self.city_name = city_name
        self.fee = fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.fee is not None:
            result['fee'] = self.fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('fee') is not None:
            self.fee = m.get('fee')

        return self

class ApplyAddRequestCarRule(DaraModel):
    def __init__(
        self,
        scenario_template_id: str = None,
        scenario_template_name: str = None,
    ):
        self.scenario_template_id = scenario_template_id
        self.scenario_template_name = scenario_template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scenario_template_id is not None:
            result['scenario_template_id'] = self.scenario_template_id

        if self.scenario_template_name is not None:
            result['scenario_template_name'] = self.scenario_template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scenario_template_id') is not None:
            self.scenario_template_id = m.get('scenario_template_id')

        if m.get('scenario_template_name') is not None:
            self.scenario_template_name = m.get('scenario_template_name')

        return self

