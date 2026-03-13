# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class MealApplyAddRequest(DaraModel):
    def __init__(
        self,
        apply_user: main_models.MealApplyAddRequestApplyUser = None,
        cost_center_id: int = None,
        extend_field: str = None,
        invoice_id: int = None,
        itinerary_list: List[main_models.MealApplyAddRequestItineraryList] = None,
        meal_amount: int = None,
        meal_cause: str = None,
        project_code: str = None,
        project_title: str = None,
        status: int = None,
        third_part_apply_id: str = None,
        third_part_cost_center_id: str = None,
        third_part_invoice_id: str = None,
    ):
        # This parameter is required.
        self.apply_user = apply_user
        self.cost_center_id = cost_center_id
        self.extend_field = extend_field
        self.invoice_id = invoice_id
        # This parameter is required.
        self.itinerary_list = itinerary_list
        self.meal_amount = meal_amount
        # This parameter is required.
        self.meal_cause = meal_cause
        self.project_code = project_code
        self.project_title = project_title
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.third_part_apply_id = third_part_apply_id
        self.third_part_cost_center_id = third_part_cost_center_id
        self.third_part_invoice_id = third_part_invoice_id

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

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.status is not None:
            result['status'] = self.status

        if self.third_part_apply_id is not None:
            result['third_part_apply_id'] = self.third_part_apply_id

        if self.third_part_cost_center_id is not None:
            result['third_part_cost_center_id'] = self.third_part_cost_center_id

        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_user') is not None:
            temp_model = main_models.MealApplyAddRequestApplyUser()
            self.apply_user = temp_model.from_map(m.get('apply_user'))

        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('extend_field') is not None:
            self.extend_field = m.get('extend_field')

        if m.get('invoice_id') is not None:
            self.invoice_id = m.get('invoice_id')

        self.itinerary_list = []
        if m.get('itinerary_list') is not None:
            for k1 in m.get('itinerary_list'):
                temp_model = main_models.MealApplyAddRequestItineraryList()
                self.itinerary_list.append(temp_model.from_map(k1))

        if m.get('meal_amount') is not None:
            self.meal_amount = m.get('meal_amount')

        if m.get('meal_cause') is not None:
            self.meal_cause = m.get('meal_cause')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('third_part_apply_id') is not None:
            self.third_part_apply_id = m.get('third_part_apply_id')

        if m.get('third_part_cost_center_id') is not None:
            self.third_part_cost_center_id = m.get('third_part_cost_center_id')

        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')

        return self

class MealApplyAddRequestItineraryList(DaraModel):
    def __init__(
        self,
        cities: List[main_models.MealApplyAddRequestItineraryListCities] = None,
        end_date: str = None,
        start_date: str = None,
        thirdpart_itinerary_id: str = None,
    ):
        # This parameter is required.
        self.cities = cities
        # This parameter is required.
        self.end_date = end_date
        # This parameter is required.
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
                temp_model = main_models.MealApplyAddRequestItineraryListCities()
                self.cities.append(temp_model.from_map(k1))

        if m.get('end_date') is not None:
            self.end_date = m.get('end_date')

        if m.get('start_date') is not None:
            self.start_date = m.get('start_date')

        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')

        return self

class MealApplyAddRequestItineraryListCities(DaraModel):
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

class MealApplyAddRequestApplyUser(DaraModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

