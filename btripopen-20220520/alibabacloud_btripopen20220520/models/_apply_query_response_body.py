# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class ApplyQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.ApplyQueryResponseBodyModule = None,
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
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

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

        if m.get('module') is not None:
            temp_model = main_models.ApplyQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class ApplyQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        apply_show_id: str = None,
        approver_list: List[main_models.ApplyQueryResponseBodyModuleApproverList] = None,
        budget: int = None,
        budget_merge: int = None,
        car_rule: main_models.ApplyQueryResponseBodyModuleCarRule = None,
        corp_id: str = None,
        corp_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        extend_field: str = None,
        external_traveler_list: List[main_models.ApplyQueryResponseBodyModuleExternalTravelerList] = None,
        flight_budget: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hotel_budget: int = None,
        hotel_share: main_models.ApplyQueryResponseBodyModuleHotelShare = None,
        id: int = None,
        intl_flight_budget: int = None,
        intl_hotel_budget: int = None,
        itinerary_list: List[main_models.ApplyQueryResponseBodyModuleItineraryList] = None,
        itinerary_rule: int = None,
        itinerary_set_list: List[main_models.ApplyQueryResponseBodyModuleItinerarySetList] = None,
        limit_traveler: int = None,
        meal_budget: int = None,
        payment_department_id: str = None,
        payment_department_name: str = None,
        status: int = None,
        status_desc: str = None,
        thirdpart_business_id: str = None,
        thirdpart_id: str = None,
        together_book_rule: int = None,
        train_budget: int = None,
        traveler_list: List[main_models.ApplyQueryResponseBodyModuleTravelerList] = None,
        trip_cause: str = None,
        trip_day: int = None,
        trip_title: str = None,
        type: int = None,
        union_no: str = None,
        user_id: str = None,
        user_name: str = None,
        vehicle_budget: int = None,
    ):
        self.apply_show_id = apply_show_id
        self.approver_list = approver_list
        self.budget = budget
        self.budget_merge = budget_merge
        self.car_rule = car_rule
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        # 补充描述，账单中将会体现此字段的值。可以用于企业的统计和对账
        self.extend_field = extend_field
        self.external_traveler_list = external_traveler_list
        self.flight_budget = flight_budget
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.hotel_budget = hotel_budget
        self.hotel_share = hotel_share
        self.id = id
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
        self.status_desc = status_desc
        self.thirdpart_business_id = thirdpart_business_id
        self.thirdpart_id = thirdpart_id
        self.together_book_rule = together_book_rule
        self.train_budget = train_budget
        self.traveler_list = traveler_list
        self.trip_cause = trip_cause
        self.trip_day = trip_day
        self.trip_title = trip_title
        self.type = type
        self.union_no = union_no
        self.user_id = user_id
        self.user_name = user_name
        self.vehicle_budget = vehicle_budget

    def validate(self):
        if self.approver_list:
            for v1 in self.approver_list:
                 if v1:
                    v1.validate()
        if self.car_rule:
            self.car_rule.validate()
        if self.external_traveler_list:
            for v1 in self.external_traveler_list:
                 if v1:
                    v1.validate()
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

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_show_id is not None:
            result['apply_show_id'] = self.apply_show_id

        result['approver_list'] = []
        if self.approver_list is not None:
            for k1 in self.approver_list:
                result['approver_list'].append(k1.to_map() if k1 else None)

        if self.budget is not None:
            result['budget'] = self.budget

        if self.budget_merge is not None:
            result['budget_merge'] = self.budget_merge

        if self.car_rule is not None:
            result['car_rule'] = self.car_rule.to_map()

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.corp_name is not None:
            result['corp_name'] = self.corp_name

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

        if self.flight_budget is not None:
            result['flight_budget'] = self.flight_budget

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified

        if self.hotel_budget is not None:
            result['hotel_budget'] = self.hotel_budget

        if self.hotel_share is not None:
            result['hotel_share'] = self.hotel_share.to_map()

        if self.id is not None:
            result['id'] = self.id

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

        if self.status_desc is not None:
            result['status_desc'] = self.status_desc

        if self.thirdpart_business_id is not None:
            result['thirdpart_business_id'] = self.thirdpart_business_id

        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id

        if self.together_book_rule is not None:
            result['together_book_rule'] = self.together_book_rule

        if self.train_budget is not None:
            result['train_budget'] = self.train_budget

        result['traveler_list'] = []
        if self.traveler_list is not None:
            for k1 in self.traveler_list:
                result['traveler_list'].append(k1.to_map() if k1 else None)

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
        if m.get('apply_show_id') is not None:
            self.apply_show_id = m.get('apply_show_id')

        self.approver_list = []
        if m.get('approver_list') is not None:
            for k1 in m.get('approver_list'):
                temp_model = main_models.ApplyQueryResponseBodyModuleApproverList()
                self.approver_list.append(temp_model.from_map(k1))

        if m.get('budget') is not None:
            self.budget = m.get('budget')

        if m.get('budget_merge') is not None:
            self.budget_merge = m.get('budget_merge')

        if m.get('car_rule') is not None:
            temp_model = main_models.ApplyQueryResponseBodyModuleCarRule()
            self.car_rule = temp_model.from_map(m.get('car_rule'))

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        if m.get('extend_field') is not None:
            self.extend_field = m.get('extend_field')

        self.external_traveler_list = []
        if m.get('external_traveler_list') is not None:
            for k1 in m.get('external_traveler_list'):
                temp_model = main_models.ApplyQueryResponseBodyModuleExternalTravelerList()
                self.external_traveler_list.append(temp_model.from_map(k1))

        if m.get('flight_budget') is not None:
            self.flight_budget = m.get('flight_budget')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')

        if m.get('hotel_budget') is not None:
            self.hotel_budget = m.get('hotel_budget')

        if m.get('hotel_share') is not None:
            temp_model = main_models.ApplyQueryResponseBodyModuleHotelShare()
            self.hotel_share = temp_model.from_map(m.get('hotel_share'))

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('intl_flight_budget') is not None:
            self.intl_flight_budget = m.get('intl_flight_budget')

        if m.get('intl_hotel_budget') is not None:
            self.intl_hotel_budget = m.get('intl_hotel_budget')

        self.itinerary_list = []
        if m.get('itinerary_list') is not None:
            for k1 in m.get('itinerary_list'):
                temp_model = main_models.ApplyQueryResponseBodyModuleItineraryList()
                self.itinerary_list.append(temp_model.from_map(k1))

        if m.get('itinerary_rule') is not None:
            self.itinerary_rule = m.get('itinerary_rule')

        self.itinerary_set_list = []
        if m.get('itinerary_set_list') is not None:
            for k1 in m.get('itinerary_set_list'):
                temp_model = main_models.ApplyQueryResponseBodyModuleItinerarySetList()
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

        if m.get('status_desc') is not None:
            self.status_desc = m.get('status_desc')

        if m.get('thirdpart_business_id') is not None:
            self.thirdpart_business_id = m.get('thirdpart_business_id')

        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')

        if m.get('together_book_rule') is not None:
            self.together_book_rule = m.get('together_book_rule')

        if m.get('train_budget') is not None:
            self.train_budget = m.get('train_budget')

        self.traveler_list = []
        if m.get('traveler_list') is not None:
            for k1 in m.get('traveler_list'):
                temp_model = main_models.ApplyQueryResponseBodyModuleTravelerList()
                self.traveler_list.append(temp_model.from_map(k1))

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

class ApplyQueryResponseBodyModuleTravelerList(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        business_discount: int = None,
        car_city_set: List[main_models.ApplyQueryResponseBodyModuleTravelerListCarCitySet] = None,
        cost_center_name: str = None,
        depart_id: str = None,
        economy_discount: int = None,
        first_discount: int = None,
        flight_cabins: str = None,
        flight_intl_rule_code: int = None,
        flight_rule_code: int = None,
        hotel_citys: List[main_models.ApplyQueryResponseBodyModuleTravelerListHotelCitys] = None,
        hotel_intl_citys: List[main_models.ApplyQueryResponseBodyModuleTravelerListHotelIntlCitys] = None,
        hotel_intl_rule_code: int = None,
        hotel_rule_code: int = None,
        invoice_name: str = None,
        payment_department_id: str = None,
        payment_department_name: str = None,
        premium_economy_discount: int = None,
        project_code: str = None,
        project_title: str = None,
        reserve_type: int = None,
        third_part_invoice_id: str = None,
        thirdpart_cost_center_id: str = None,
        thirdpart_depart_id: str = None,
        train_rule_code: int = None,
        train_seats: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.attribute = attribute
        self.business_discount = business_discount
        self.car_city_set = car_city_set
        self.cost_center_name = cost_center_name
        self.depart_id = depart_id
        self.economy_discount = economy_discount
        self.first_discount = first_discount
        self.flight_cabins = flight_cabins
        self.flight_intl_rule_code = flight_intl_rule_code
        self.flight_rule_code = flight_rule_code
        self.hotel_citys = hotel_citys
        self.hotel_intl_citys = hotel_intl_citys
        self.hotel_intl_rule_code = hotel_intl_rule_code
        self.hotel_rule_code = hotel_rule_code
        self.invoice_name = invoice_name
        self.payment_department_id = payment_department_id
        self.payment_department_name = payment_department_name
        self.premium_economy_discount = premium_economy_discount
        self.project_code = project_code
        self.project_title = project_title
        self.reserve_type = reserve_type
        self.third_part_invoice_id = third_part_invoice_id
        self.thirdpart_cost_center_id = thirdpart_cost_center_id
        self.thirdpart_depart_id = thirdpart_depart_id
        self.train_rule_code = train_rule_code
        self.train_seats = train_seats
        self.user_id = user_id
        self.user_name = user_name

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
        if self.attribute is not None:
            result['attribute'] = self.attribute

        if self.business_discount is not None:
            result['business_discount'] = self.business_discount

        result['car_city_set'] = []
        if self.car_city_set is not None:
            for k1 in self.car_city_set:
                result['car_city_set'].append(k1.to_map() if k1 else None)

        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

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

        if self.invoice_name is not None:
            result['invoice_name'] = self.invoice_name

        if self.payment_department_id is not None:
            result['payment_department_id'] = self.payment_department_id

        if self.payment_department_name is not None:
            result['payment_department_name'] = self.payment_department_name

        if self.premium_economy_discount is not None:
            result['premium_economy_discount'] = self.premium_economy_discount

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.reserve_type is not None:
            result['reserve_type'] = self.reserve_type

        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id

        if self.thirdpart_cost_center_id is not None:
            result['thirdpart_cost_center_id'] = self.thirdpart_cost_center_id

        if self.thirdpart_depart_id is not None:
            result['thirdpart_depart_id'] = self.thirdpart_depart_id

        if self.train_rule_code is not None:
            result['train_rule_code'] = self.train_rule_code

        if self.train_seats is not None:
            result['train_seats'] = self.train_seats

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')

        if m.get('business_discount') is not None:
            self.business_discount = m.get('business_discount')

        self.car_city_set = []
        if m.get('car_city_set') is not None:
            for k1 in m.get('car_city_set'):
                temp_model = main_models.ApplyQueryResponseBodyModuleTravelerListCarCitySet()
                self.car_city_set.append(temp_model.from_map(k1))

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

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
                temp_model = main_models.ApplyQueryResponseBodyModuleTravelerListHotelCitys()
                self.hotel_citys.append(temp_model.from_map(k1))

        self.hotel_intl_citys = []
        if m.get('hotel_intl_citys') is not None:
            for k1 in m.get('hotel_intl_citys'):
                temp_model = main_models.ApplyQueryResponseBodyModuleTravelerListHotelIntlCitys()
                self.hotel_intl_citys.append(temp_model.from_map(k1))

        if m.get('hotel_intl_rule_code') is not None:
            self.hotel_intl_rule_code = m.get('hotel_intl_rule_code')

        if m.get('hotel_rule_code') is not None:
            self.hotel_rule_code = m.get('hotel_rule_code')

        if m.get('invoice_name') is not None:
            self.invoice_name = m.get('invoice_name')

        if m.get('payment_department_id') is not None:
            self.payment_department_id = m.get('payment_department_id')

        if m.get('payment_department_name') is not None:
            self.payment_department_name = m.get('payment_department_name')

        if m.get('premium_economy_discount') is not None:
            self.premium_economy_discount = m.get('premium_economy_discount')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('reserve_type') is not None:
            self.reserve_type = m.get('reserve_type')

        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')

        if m.get('thirdpart_cost_center_id') is not None:
            self.thirdpart_cost_center_id = m.get('thirdpart_cost_center_id')

        if m.get('thirdpart_depart_id') is not None:
            self.thirdpart_depart_id = m.get('thirdpart_depart_id')

        if m.get('train_rule_code') is not None:
            self.train_rule_code = m.get('train_rule_code')

        if m.get('train_seats') is not None:
            self.train_seats = m.get('train_seats')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class ApplyQueryResponseBodyModuleTravelerListHotelIntlCitys(DaraModel):
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

class ApplyQueryResponseBodyModuleTravelerListHotelCitys(DaraModel):
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

class ApplyQueryResponseBodyModuleTravelerListCarCitySet(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
    ):
        self.city_code = city_code
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

class ApplyQueryResponseBodyModuleItinerarySetList(DaraModel):
    def __init__(
        self,
        arr_date: str = None,
        attribute: str = None,
        city_code_set: str = None,
        city_set: str = None,
        cost_center_name: str = None,
        dep_date: str = None,
        invoice_name: str = None,
        itinerary_id: str = None,
        itinerary_travel_standard: main_models.ApplyQueryResponseBodyModuleItinerarySetListItineraryTravelStandard = None,
        project_code: str = None,
        project_title: str = None,
        thirdpart_cost_center_id: str = None,
        thirdpart_invoice_id: str = None,
        thirdpart_itinerary_id: str = None,
        traffic_type: int = None,
    ):
        self.arr_date = arr_date
        self.attribute = attribute
        self.city_code_set = city_code_set
        self.city_set = city_set
        self.cost_center_name = cost_center_name
        self.dep_date = dep_date
        self.invoice_name = invoice_name
        self.itinerary_id = itinerary_id
        self.itinerary_travel_standard = itinerary_travel_standard
        self.project_code = project_code
        self.project_title = project_title
        self.thirdpart_cost_center_id = thirdpart_cost_center_id
        self.thirdpart_invoice_id = thirdpart_invoice_id
        self.thirdpart_itinerary_id = thirdpart_itinerary_id
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

        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.invoice_name is not None:
            result['invoice_name'] = self.invoice_name

        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id

        if self.itinerary_travel_standard is not None:
            result['itinerary_travel_standard'] = self.itinerary_travel_standard.to_map()

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.thirdpart_cost_center_id is not None:
            result['thirdpart_cost_center_id'] = self.thirdpart_cost_center_id

        if self.thirdpart_invoice_id is not None:
            result['thirdpart_invoice_id'] = self.thirdpart_invoice_id

        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id

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

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('invoice_name') is not None:
            self.invoice_name = m.get('invoice_name')

        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')

        if m.get('itinerary_travel_standard') is not None:
            temp_model = main_models.ApplyQueryResponseBodyModuleItinerarySetListItineraryTravelStandard()
            self.itinerary_travel_standard = temp_model.from_map(m.get('itinerary_travel_standard'))

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('thirdpart_cost_center_id') is not None:
            self.thirdpart_cost_center_id = m.get('thirdpart_cost_center_id')

        if m.get('thirdpart_invoice_id') is not None:
            self.thirdpart_invoice_id = m.get('thirdpart_invoice_id')

        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')

        if m.get('traffic_type') is not None:
            self.traffic_type = m.get('traffic_type')

        return self

class ApplyQueryResponseBodyModuleItinerarySetListItineraryTravelStandard(DaraModel):
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

class ApplyQueryResponseBodyModuleItineraryList(DaraModel):
    def __init__(
        self,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_date: str = None,
        attribute: str = None,
        cost_center_name: str = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_date: str = None,
        invoice_name: str = None,
        itinerary_id: str = None,
        itinerary_travel_standard: main_models.ApplyQueryResponseBodyModuleItineraryListItineraryTravelStandard = None,
        project_code: str = None,
        project_title: str = None,
        thirdpart_cost_center_id: str = None,
        thirdpart_invoice_id: str = None,
        thirdpart_itinerary_id: str = None,
        traffic_type: int = None,
        trip_way: int = None,
    ):
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.arr_date = arr_date
        self.attribute = attribute
        self.cost_center_name = cost_center_name
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.dep_date = dep_date
        self.invoice_name = invoice_name
        self.itinerary_id = itinerary_id
        self.itinerary_travel_standard = itinerary_travel_standard
        self.project_code = project_code
        self.project_title = project_title
        self.thirdpart_cost_center_id = thirdpart_cost_center_id
        self.thirdpart_invoice_id = thirdpart_invoice_id
        self.thirdpart_itinerary_id = thirdpart_itinerary_id
        self.traffic_type = traffic_type
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

        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.invoice_name is not None:
            result['invoice_name'] = self.invoice_name

        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id

        if self.itinerary_travel_standard is not None:
            result['itinerary_travel_standard'] = self.itinerary_travel_standard.to_map()

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.thirdpart_cost_center_id is not None:
            result['thirdpart_cost_center_id'] = self.thirdpart_cost_center_id

        if self.thirdpart_invoice_id is not None:
            result['thirdpart_invoice_id'] = self.thirdpart_invoice_id

        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id

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

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('invoice_name') is not None:
            self.invoice_name = m.get('invoice_name')

        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')

        if m.get('itinerary_travel_standard') is not None:
            temp_model = main_models.ApplyQueryResponseBodyModuleItineraryListItineraryTravelStandard()
            self.itinerary_travel_standard = temp_model.from_map(m.get('itinerary_travel_standard'))

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('thirdpart_cost_center_id') is not None:
            self.thirdpart_cost_center_id = m.get('thirdpart_cost_center_id')

        if m.get('thirdpart_invoice_id') is not None:
            self.thirdpart_invoice_id = m.get('thirdpart_invoice_id')

        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')

        if m.get('traffic_type') is not None:
            self.traffic_type = m.get('traffic_type')

        if m.get('trip_way') is not None:
            self.trip_way = m.get('trip_way')

        return self

class ApplyQueryResponseBodyModuleItineraryListItineraryTravelStandard(DaraModel):
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

class ApplyQueryResponseBodyModuleHotelShare(DaraModel):
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

class ApplyQueryResponseBodyModuleExternalTravelerList(DaraModel):
    def __init__(
        self,
        attribute: str = None,
        business_discount: int = None,
        cost_center_name: str = None,
        depart_id: str = None,
        economy_discount: int = None,
        external_user_id: str = None,
        first_discount: int = None,
        flight_cabins: str = None,
        flight_intl_rule_code: int = None,
        flight_rule_code: int = None,
        hotel_citys: List[main_models.ApplyQueryResponseBodyModuleExternalTravelerListHotelCitys] = None,
        hotel_intl_citys: List[main_models.ApplyQueryResponseBodyModuleExternalTravelerListHotelIntlCitys] = None,
        hotel_intl_rule_code: int = None,
        hotel_rule_code: int = None,
        invoice_name: str = None,
        payment_department_id: str = None,
        payment_department_name: str = None,
        premium_economy_discount: int = None,
        project_code: str = None,
        project_title: str = None,
        reserve_type: int = None,
        third_part_invoice_id: str = None,
        thirdpart_cost_center_id: str = None,
        thirdpart_depart_id: str = None,
        train_rule_code: int = None,
        train_seats: str = None,
        user_name: str = None,
    ):
        self.attribute = attribute
        self.business_discount = business_discount
        self.cost_center_name = cost_center_name
        self.depart_id = depart_id
        self.economy_discount = economy_discount
        self.external_user_id = external_user_id
        self.first_discount = first_discount
        self.flight_cabins = flight_cabins
        self.flight_intl_rule_code = flight_intl_rule_code
        self.flight_rule_code = flight_rule_code
        self.hotel_citys = hotel_citys
        self.hotel_intl_citys = hotel_intl_citys
        self.hotel_intl_rule_code = hotel_intl_rule_code
        self.hotel_rule_code = hotel_rule_code
        self.invoice_name = invoice_name
        self.payment_department_id = payment_department_id
        self.payment_department_name = payment_department_name
        self.premium_economy_discount = premium_economy_discount
        self.project_code = project_code
        self.project_title = project_title
        self.reserve_type = reserve_type
        self.third_part_invoice_id = third_part_invoice_id
        self.thirdpart_cost_center_id = thirdpart_cost_center_id
        self.thirdpart_depart_id = thirdpart_depart_id
        self.train_rule_code = train_rule_code
        self.train_seats = train_seats
        self.user_name = user_name

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
        if self.attribute is not None:
            result['attribute'] = self.attribute

        if self.business_discount is not None:
            result['business_discount'] = self.business_discount

        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.economy_discount is not None:
            result['economy_discount'] = self.economy_discount

        if self.external_user_id is not None:
            result['external_user_id'] = self.external_user_id

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

        if self.invoice_name is not None:
            result['invoice_name'] = self.invoice_name

        if self.payment_department_id is not None:
            result['payment_department_id'] = self.payment_department_id

        if self.payment_department_name is not None:
            result['payment_department_name'] = self.payment_department_name

        if self.premium_economy_discount is not None:
            result['premium_economy_discount'] = self.premium_economy_discount

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.reserve_type is not None:
            result['reserve_type'] = self.reserve_type

        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id

        if self.thirdpart_cost_center_id is not None:
            result['thirdpart_cost_center_id'] = self.thirdpart_cost_center_id

        if self.thirdpart_depart_id is not None:
            result['thirdpart_depart_id'] = self.thirdpart_depart_id

        if self.train_rule_code is not None:
            result['train_rule_code'] = self.train_rule_code

        if self.train_seats is not None:
            result['train_seats'] = self.train_seats

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')

        if m.get('business_discount') is not None:
            self.business_discount = m.get('business_discount')

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('economy_discount') is not None:
            self.economy_discount = m.get('economy_discount')

        if m.get('external_user_id') is not None:
            self.external_user_id = m.get('external_user_id')

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
                temp_model = main_models.ApplyQueryResponseBodyModuleExternalTravelerListHotelCitys()
                self.hotel_citys.append(temp_model.from_map(k1))

        self.hotel_intl_citys = []
        if m.get('hotel_intl_citys') is not None:
            for k1 in m.get('hotel_intl_citys'):
                temp_model = main_models.ApplyQueryResponseBodyModuleExternalTravelerListHotelIntlCitys()
                self.hotel_intl_citys.append(temp_model.from_map(k1))

        if m.get('hotel_intl_rule_code') is not None:
            self.hotel_intl_rule_code = m.get('hotel_intl_rule_code')

        if m.get('hotel_rule_code') is not None:
            self.hotel_rule_code = m.get('hotel_rule_code')

        if m.get('invoice_name') is not None:
            self.invoice_name = m.get('invoice_name')

        if m.get('payment_department_id') is not None:
            self.payment_department_id = m.get('payment_department_id')

        if m.get('payment_department_name') is not None:
            self.payment_department_name = m.get('payment_department_name')

        if m.get('premium_economy_discount') is not None:
            self.premium_economy_discount = m.get('premium_economy_discount')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('reserve_type') is not None:
            self.reserve_type = m.get('reserve_type')

        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')

        if m.get('thirdpart_cost_center_id') is not None:
            self.thirdpart_cost_center_id = m.get('thirdpart_cost_center_id')

        if m.get('thirdpart_depart_id') is not None:
            self.thirdpart_depart_id = m.get('thirdpart_depart_id')

        if m.get('train_rule_code') is not None:
            self.train_rule_code = m.get('train_rule_code')

        if m.get('train_seats') is not None:
            self.train_seats = m.get('train_seats')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class ApplyQueryResponseBodyModuleExternalTravelerListHotelIntlCitys(DaraModel):
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

class ApplyQueryResponseBodyModuleExternalTravelerListHotelCitys(DaraModel):
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

class ApplyQueryResponseBodyModuleCarRule(DaraModel):
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

class ApplyQueryResponseBodyModuleApproverList(DaraModel):
    def __init__(
        self,
        note: str = None,
        operate_time: str = None,
        order: int = None,
        status: int = None,
        status_desc: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.note = note
        self.operate_time = operate_time
        self.order = order
        self.status = status
        self.status_desc = status_desc
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.note is not None:
            result['note'] = self.note

        if self.operate_time is not None:
            result['operate_time'] = self.operate_time

        if self.order is not None:
            result['order'] = self.order

        if self.status is not None:
            result['status'] = self.status

        if self.status_desc is not None:
            result['status_desc'] = self.status_desc

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('note') is not None:
            self.note = m.get('note')

        if m.get('operate_time') is not None:
            self.operate_time = m.get('operate_time')

        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('status_desc') is not None:
            self.status_desc = m.get('status_desc')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

