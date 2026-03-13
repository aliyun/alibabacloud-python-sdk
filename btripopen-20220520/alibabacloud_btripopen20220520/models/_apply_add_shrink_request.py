# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyAddShrinkRequest(DaraModel):
    def __init__(
        self,
        budget: int = None,
        budget_merge: int = None,
        car_rule_shrink: str = None,
        corp_name: str = None,
        default_standard_shrink: str = None,
        depart_id: str = None,
        depart_name: str = None,
        extend_field: str = None,
        external_traveler_list_shrink: str = None,
        external_traveler_standard_shrink: str = None,
        flight_budget: int = None,
        hotel_budget: int = None,
        hotel_share_shrink: str = None,
        international_flight_cabins: str = None,
        intl_flight_budget: int = None,
        intl_hotel_budget: int = None,
        itinerary_list_shrink: str = None,
        itinerary_rule: int = None,
        itinerary_set_list_shrink: str = None,
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
        traveler_list_shrink: str = None,
        traveler_standard_shrink: str = None,
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
        self.car_rule_shrink = car_rule_shrink
        self.corp_name = corp_name
        self.default_standard_shrink = default_standard_shrink
        self.depart_id = depart_id
        self.depart_name = depart_name
        # 可将补充描述传入此字段，账单中将会体现此字段的值。可以用于企业的统计和对账
        self.extend_field = extend_field
        self.external_traveler_list_shrink = external_traveler_list_shrink
        self.external_traveler_standard_shrink = external_traveler_standard_shrink
        self.flight_budget = flight_budget
        self.hotel_budget = hotel_budget
        self.hotel_share_shrink = hotel_share_shrink
        self.international_flight_cabins = international_flight_cabins
        self.intl_flight_budget = intl_flight_budget
        self.intl_hotel_budget = intl_hotel_budget
        self.itinerary_list_shrink = itinerary_list_shrink
        self.itinerary_rule = itinerary_rule
        self.itinerary_set_list_shrink = itinerary_set_list_shrink
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
        self.traveler_list_shrink = traveler_list_shrink
        self.traveler_standard_shrink = traveler_standard_shrink
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
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.budget is not None:
            result['budget'] = self.budget

        if self.budget_merge is not None:
            result['budget_merge'] = self.budget_merge

        if self.car_rule_shrink is not None:
            result['car_rule'] = self.car_rule_shrink

        if self.corp_name is not None:
            result['corp_name'] = self.corp_name

        if self.default_standard_shrink is not None:
            result['default_standard'] = self.default_standard_shrink

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        if self.extend_field is not None:
            result['extend_field'] = self.extend_field

        if self.external_traveler_list_shrink is not None:
            result['external_traveler_list'] = self.external_traveler_list_shrink

        if self.external_traveler_standard_shrink is not None:
            result['external_traveler_standard'] = self.external_traveler_standard_shrink

        if self.flight_budget is not None:
            result['flight_budget'] = self.flight_budget

        if self.hotel_budget is not None:
            result['hotel_budget'] = self.hotel_budget

        if self.hotel_share_shrink is not None:
            result['hotel_share'] = self.hotel_share_shrink

        if self.international_flight_cabins is not None:
            result['international_flight_cabins'] = self.international_flight_cabins

        if self.intl_flight_budget is not None:
            result['intl_flight_budget'] = self.intl_flight_budget

        if self.intl_hotel_budget is not None:
            result['intl_hotel_budget'] = self.intl_hotel_budget

        if self.itinerary_list_shrink is not None:
            result['itinerary_list'] = self.itinerary_list_shrink

        if self.itinerary_rule is not None:
            result['itinerary_rule'] = self.itinerary_rule

        if self.itinerary_set_list_shrink is not None:
            result['itinerary_set_list'] = self.itinerary_set_list_shrink

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

        if self.traveler_list_shrink is not None:
            result['traveler_list'] = self.traveler_list_shrink

        if self.traveler_standard_shrink is not None:
            result['traveler_standard'] = self.traveler_standard_shrink

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
            self.car_rule_shrink = m.get('car_rule')

        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        if m.get('default_standard') is not None:
            self.default_standard_shrink = m.get('default_standard')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        if m.get('extend_field') is not None:
            self.extend_field = m.get('extend_field')

        if m.get('external_traveler_list') is not None:
            self.external_traveler_list_shrink = m.get('external_traveler_list')

        if m.get('external_traveler_standard') is not None:
            self.external_traveler_standard_shrink = m.get('external_traveler_standard')

        if m.get('flight_budget') is not None:
            self.flight_budget = m.get('flight_budget')

        if m.get('hotel_budget') is not None:
            self.hotel_budget = m.get('hotel_budget')

        if m.get('hotel_share') is not None:
            self.hotel_share_shrink = m.get('hotel_share')

        if m.get('international_flight_cabins') is not None:
            self.international_flight_cabins = m.get('international_flight_cabins')

        if m.get('intl_flight_budget') is not None:
            self.intl_flight_budget = m.get('intl_flight_budget')

        if m.get('intl_hotel_budget') is not None:
            self.intl_hotel_budget = m.get('intl_hotel_budget')

        if m.get('itinerary_list') is not None:
            self.itinerary_list_shrink = m.get('itinerary_list')

        if m.get('itinerary_rule') is not None:
            self.itinerary_rule = m.get('itinerary_rule')

        if m.get('itinerary_set_list') is not None:
            self.itinerary_set_list_shrink = m.get('itinerary_set_list')

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

        if m.get('traveler_list') is not None:
            self.traveler_list_shrink = m.get('traveler_list')

        if m.get('traveler_standard') is not None:
            self.traveler_standard_shrink = m.get('traveler_standard')

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

