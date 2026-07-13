# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class CarApplyAddRequest(DaraModel):
    def __init__(
        self,
        cause: str = None,
        city: str = None,
        city_code_set: str = None,
        date: str = None,
        finished_date: str = None,
        itinerary_list: List[main_models.CarApplyAddRequestItineraryList] = None,
        project_code: str = None,
        project_name: str = None,
        status: int = None,
        third_part_apply_id: str = None,
        third_part_cost_center_id: str = None,
        third_part_invoice_id: str = None,
        times_total: int = None,
        times_type: int = None,
        times_used: int = None,
        title: str = None,
        traveler_standard: List[main_models.CarApplyAddRequestTravelerStandard] = None,
        user_id: str = None,
    ):
        # The reason for the business trip.
        # 
        # This parameter is required.
        self.cause = cause
        # The cities for car service. Separate multiple cities with Chinese commas (，).
        # Note: A maximum of 10 cities are supported. The values in city and city_code_set must correspond one to one.
        self.city = city
        # The city code set for intra-city car service. Separate multiple cities with Chinese commas (，).
        # Note: 1) Either city_code_set or city is required. If both are specified, city_code_set takes precedence.
        # A maximum of 10 cities are supported.
        self.city_code_set = city_code_set
        # The car service time. This parameter is controlled on a daily basis. For example, a value of 2021-03-18 20:26:56 indicates that the car service is available on 2021-03-18. For multi-day scenarios, use this parameter together with the finished_date parameter. The time must be in the yyyy-MM-dd HH:mm:ss format.
        self.date = date
        # The car service end time. This parameter is controlled on a daily basis. For example, if date is set to 2021-03-18 20:26:56 and finished_date is set to 2021-03-30 20:26:56, the car service is available from 2021-03-18 (inclusive) to 2021-03-30 (inclusive). If this parameter is not specified, the value of date is used as the end time. The time must be in the yyyy-MM-dd HH:mm:ss format.
        self.finished_date = finished_date
        self.itinerary_list = itinerary_list
        # The project code associated with the approval form.
        self.project_code = project_code
        # The project name associated with the approval form.
        self.project_name = project_name
        # The approval status.
        # 
        # This parameter is required.
        self.status = status
        # The ID of the third-party approval form.
        # 
        # This parameter is required.
        self.third_part_apply_id = third_part_apply_id
        # The ID of the third-party cost center associated with the approval form.
        # >Warning: This field is required. To make it optional, contact operations.
        self.third_part_cost_center_id = third_part_cost_center_id
        # The ID of the third-party invoice header associated with the approval form.
        # 
        # >Warning: This field is required. To make it optional, contact operations.
        self.third_part_invoice_id = third_part_invoice_id
        # The total number of times the approval form can be used.
        self.times_total = times_total
        # The usage count type of the approval form. If the enterprise does not need to limit the number of times the approval form can be used, set this parameter to 1 (unlimited) and set both times_total and times_used to 0.
        # 
        # Valid values:
        # 
        # - 1: Unlimited.
        # - 2: User-specified count.
        self.times_type = times_type
        # The number of times the approval form has been used.
        self.times_used = times_used
        # The title of the approval form.
        # 
        # This parameter is required.
        self.title = title
        # The intra-city car service rules.
        self.traveler_standard = traveler_standard
        # The third-party employee ID of the user who initiates the approval.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.itinerary_list:
            for v1 in self.itinerary_list:
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
        if self.cause is not None:
            result['cause'] = self.cause

        if self.city is not None:
            result['city'] = self.city

        if self.city_code_set is not None:
            result['city_code_set'] = self.city_code_set

        if self.date is not None:
            result['date'] = self.date

        if self.finished_date is not None:
            result['finished_date'] = self.finished_date

        result['itinerary_list'] = []
        if self.itinerary_list is not None:
            for k1 in self.itinerary_list:
                result['itinerary_list'].append(k1.to_map() if k1 else None)

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_name is not None:
            result['project_name'] = self.project_name

        if self.status is not None:
            result['status'] = self.status

        if self.third_part_apply_id is not None:
            result['third_part_apply_id'] = self.third_part_apply_id

        if self.third_part_cost_center_id is not None:
            result['third_part_cost_center_id'] = self.third_part_cost_center_id

        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id

        if self.times_total is not None:
            result['times_total'] = self.times_total

        if self.times_type is not None:
            result['times_type'] = self.times_type

        if self.times_used is not None:
            result['times_used'] = self.times_used

        if self.title is not None:
            result['title'] = self.title

        result['traveler_standard'] = []
        if self.traveler_standard is not None:
            for k1 in self.traveler_standard:
                result['traveler_standard'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cause') is not None:
            self.cause = m.get('cause')

        if m.get('city') is not None:
            self.city = m.get('city')

        if m.get('city_code_set') is not None:
            self.city_code_set = m.get('city_code_set')

        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('finished_date') is not None:
            self.finished_date = m.get('finished_date')

        self.itinerary_list = []
        if m.get('itinerary_list') is not None:
            for k1 in m.get('itinerary_list'):
                temp_model = main_models.CarApplyAddRequestItineraryList()
                self.itinerary_list.append(temp_model.from_map(k1))

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_name') is not None:
            self.project_name = m.get('project_name')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('third_part_apply_id') is not None:
            self.third_part_apply_id = m.get('third_part_apply_id')

        if m.get('third_part_cost_center_id') is not None:
            self.third_part_cost_center_id = m.get('third_part_cost_center_id')

        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')

        if m.get('times_total') is not None:
            self.times_total = m.get('times_total')

        if m.get('times_type') is not None:
            self.times_type = m.get('times_type')

        if m.get('times_used') is not None:
            self.times_used = m.get('times_used')

        if m.get('title') is not None:
            self.title = m.get('title')

        self.traveler_standard = []
        if m.get('traveler_standard') is not None:
            for k1 in m.get('traveler_standard'):
                temp_model = main_models.CarApplyAddRequestTravelerStandard()
                self.traveler_standard.append(temp_model.from_map(k1))

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class CarApplyAddRequestTravelerStandard(DaraModel):
    def __init__(
        self,
        car_city_set: List[main_models.CarApplyAddRequestTravelerStandardCarCitySet] = None,
        user_id: str = None,
    ):
        # The cross-city car service rules. Optional. If specified, cross-city rules are read from the approval form data.
        self.car_city_set = car_city_set
        # The user ID of the traveler.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.car_city_set:
            for v1 in self.car_city_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['car_city_set'] = []
        if self.car_city_set is not None:
            for k1 in self.car_city_set:
                result['car_city_set'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.car_city_set = []
        if m.get('car_city_set') is not None:
            for k1 in m.get('car_city_set'):
                temp_model = main_models.CarApplyAddRequestTravelerStandardCarCitySet()
                self.car_city_set.append(temp_model.from_map(k1))

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class CarApplyAddRequestTravelerStandardCarCitySet(DaraModel):
    def __init__(
        self,
        city_code: str = None,
        city_name: str = None,
    ):
        # The cross-city city code. Only 6-digit codes are supported. Separate multiple values with Chinese commas.
        # Note: A maximum of 10 cities are supported. The values in city_code and city_name must correspond one to one.
        # 
        # This parameter is required.
        self.city_code = city_code
        # The cross-city city name. Separate multiple values with Chinese commas.
        # Note: A maximum of 10 cities are supported. The values in city_code and city_name must correspond one to one.
        # 
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

class CarApplyAddRequestItineraryList(DaraModel):
    def __init__(
        self,
        city: str = None,
        city_code_set: str = None,
        date: str = None,
        finished_date: str = None,
    ):
        self.city = city
        self.city_code_set = city_code_set
        self.date = date
        self.finished_date = finished_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['city'] = self.city

        if self.city_code_set is not None:
            result['city_code_set'] = self.city_code_set

        if self.date is not None:
            result['date'] = self.date

        if self.finished_date is not None:
            result['finished_date'] = self.finished_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city') is not None:
            self.city = m.get('city')

        if m.get('city_code_set') is not None:
            self.city_code_set = m.get('city_code_set')

        if m.get('date') is not None:
            self.date = m.get('date')

        if m.get('finished_date') is not None:
            self.finished_date = m.get('finished_date')

        return self

