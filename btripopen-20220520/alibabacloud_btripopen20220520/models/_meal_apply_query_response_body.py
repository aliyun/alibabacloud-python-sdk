# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class MealApplyQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.MealApplyQueryResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
        # traceId
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
            temp_model = main_models.MealApplyQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class MealApplyQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        apply_user: main_models.MealApplyQueryResponseBodyModuleApplyUser = None,
        cost_center_id: int = None,
        extend_field: str = None,
        gmt_create: str = None,
        invoice_id: int = None,
        itinerary_list: List[main_models.MealApplyQueryResponseBodyModuleItineraryList] = None,
        meal_amount: int = None,
        meal_cause: str = None,
        project_id: int = None,
        status: int = None,
        third_part_apply_id: str = None,
        third_part_cost_center_id: str = None,
        third_part_invoice_id: str = None,
        third_part_project_id: str = None,
    ):
        self.apply_user = apply_user
        self.cost_center_id = cost_center_id
        self.extend_field = extend_field
        self.gmt_create = gmt_create
        self.invoice_id = invoice_id
        self.itinerary_list = itinerary_list
        self.meal_amount = meal_amount
        self.meal_cause = meal_cause
        self.project_id = project_id
        self.status = status
        self.third_part_apply_id = third_part_apply_id
        self.third_part_cost_center_id = third_part_cost_center_id
        self.third_part_invoice_id = third_part_invoice_id
        self.third_part_project_id = third_part_project_id

    def validate(self):
        if self.apply_user:
            self.apply_user.validate()
        if self.itinerary_list:
            for v1 in self.itinerary_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_user is not None:
            result['apply_user'] = self.apply_user.to_map()

        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id

        if self.extend_field is not None:
            result['extend_field'] = self.extend_field

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.invoice_id is not None:
            result['invoice_id'] = self.invoice_id

        result['itinerary_list'] = []
        if self.itinerary_list is not None:
            for k1 in self.itinerary_list:
                result['itinerary_list'].append(k1.to_map() if k1 else None)

        if self.meal_amount is not None:
            result['meal_amount'] = self.meal_amount

        if self.meal_cause is not None:
            result['meal_cause'] = self.meal_cause

        if self.project_id is not None:
            result['project_id'] = self.project_id

        if self.status is not None:
            result['status'] = self.status

        if self.third_part_apply_id is not None:
            result['third_part_apply_id'] = self.third_part_apply_id

        if self.third_part_cost_center_id is not None:
            result['third_part_cost_center_id'] = self.third_part_cost_center_id

        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id

        if self.third_part_project_id is not None:
            result['third_part_project_id'] = self.third_part_project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_user') is not None:
            temp_model = main_models.MealApplyQueryResponseBodyModuleApplyUser()
            self.apply_user = temp_model.from_map(m.get('apply_user'))

        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('extend_field') is not None:
            self.extend_field = m.get('extend_field')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('invoice_id') is not None:
            self.invoice_id = m.get('invoice_id')

        self.itinerary_list = []
        if m.get('itinerary_list') is not None:
            for k1 in m.get('itinerary_list'):
                temp_model = main_models.MealApplyQueryResponseBodyModuleItineraryList()
                self.itinerary_list.append(temp_model.from_map(k1))

        if m.get('meal_amount') is not None:
            self.meal_amount = m.get('meal_amount')

        if m.get('meal_cause') is not None:
            self.meal_cause = m.get('meal_cause')

        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('third_part_apply_id') is not None:
            self.third_part_apply_id = m.get('third_part_apply_id')

        if m.get('third_part_cost_center_id') is not None:
            self.third_part_cost_center_id = m.get('third_part_cost_center_id')

        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')

        if m.get('third_part_project_id') is not None:
            self.third_part_project_id = m.get('third_part_project_id')

        return self

class MealApplyQueryResponseBodyModuleItineraryList(DaraModel):
    def __init__(
        self,
        cities: List[main_models.MealApplyQueryResponseBodyModuleItineraryListCities] = None,
        end_date: str = None,
        start_date: str = None,
        thirdpart_itinerary_id: str = None,
    ):
        self.cities = cities
        self.end_date = end_date
        self.start_date = start_date
        self.thirdpart_itinerary_id = thirdpart_itinerary_id

    def validate(self):
        if self.cities:
            for v1 in self.cities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['cities'] = []
        if self.cities is not None:
            for k1 in self.cities:
                result['cities'].append(k1.to_map() if k1 else None)

        if self.end_date is not None:
            result['end_date'] = self.end_date

        if self.start_date is not None:
            result['start_date'] = self.start_date

        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cities = []
        if m.get('cities') is not None:
            for k1 in m.get('cities'):
                temp_model = main_models.MealApplyQueryResponseBodyModuleItineraryListCities()
                self.cities.append(temp_model.from_map(k1))

        if m.get('end_date') is not None:
            self.end_date = m.get('end_date')

        if m.get('start_date') is not None:
            self.start_date = m.get('start_date')

        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')

        return self

class MealApplyQueryResponseBodyModuleItineraryListCities(DaraModel):
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

class MealApplyQueryResponseBodyModuleApplyUser(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        user_name: str = None,
    ):
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

