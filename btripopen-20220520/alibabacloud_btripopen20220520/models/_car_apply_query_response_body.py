# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class CarApplyQueryResponseBody(DaraModel):
    def __init__(
        self,
        apply_list: List[main_models.CarApplyQueryResponseBodyApplyList] = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
        trace_id: str = None,
    ):
        self.apply_list = apply_list
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.total = total
        self.trace_id = trace_id

    def validate(self):
        if self.apply_list:
            for v1 in self.apply_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['apply_list'] = []
        if self.apply_list is not None:
            for k1 in self.apply_list:
                result['apply_list'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total is not None:
            result['total'] = self.total

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_list = []
        if m.get('apply_list') is not None:
            for k1 in m.get('apply_list'):
                temp_model = main_models.CarApplyQueryResponseBodyApplyList()
                self.apply_list.append(temp_model.from_map(k1))

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('total') is not None:
            self.total = m.get('total')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class CarApplyQueryResponseBodyApplyList(DaraModel):
    def __init__(
        self,
        approver_list: List[main_models.CarApplyQueryResponseBodyApplyListApproverList] = None,
        business_type: str = None,
        depart_id: str = None,
        depart_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        itinerary_list: List[main_models.CarApplyQueryResponseBodyApplyListItineraryList] = None,
        order_id: int = None,
        related_third_apply_id: str = None,
        status: int = None,
        status_desc: str = None,
        thirdpart_id: str = None,
        traveler_standard: List[main_models.CarApplyQueryResponseBodyApplyListTravelerStandard] = None,
        trip_cause: str = None,
        trip_title: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.approver_list = approver_list
        self.business_type = business_type
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.itinerary_list = itinerary_list
        self.order_id = order_id
        self.related_third_apply_id = related_third_apply_id
        self.status = status
        self.status_desc = status_desc
        self.thirdpart_id = thirdpart_id
        self.traveler_standard = traveler_standard
        self.trip_cause = trip_cause
        self.trip_title = trip_title
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.approver_list:
            for v1 in self.approver_list:
                 if v1:
                    v1.validate()
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
        result['approver_list'] = []
        if self.approver_list is not None:
            for k1 in self.approver_list:
                result['approver_list'].append(k1.to_map() if k1 else None)

        if self.business_type is not None:
            result['business_type'] = self.business_type

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified

        result['itinerary_list'] = []
        if self.itinerary_list is not None:
            for k1 in self.itinerary_list:
                result['itinerary_list'].append(k1.to_map() if k1 else None)

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.related_third_apply_id is not None:
            result['related_third_apply_id'] = self.related_third_apply_id

        if self.status is not None:
            result['status'] = self.status

        if self.status_desc is not None:
            result['status_desc'] = self.status_desc

        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id

        result['traveler_standard'] = []
        if self.traveler_standard is not None:
            for k1 in self.traveler_standard:
                result['traveler_standard'].append(k1.to_map() if k1 else None)

        if self.trip_cause is not None:
            result['trip_cause'] = self.trip_cause

        if self.trip_title is not None:
            result['trip_title'] = self.trip_title

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.approver_list = []
        if m.get('approver_list') is not None:
            for k1 in m.get('approver_list'):
                temp_model = main_models.CarApplyQueryResponseBodyApplyListApproverList()
                self.approver_list.append(temp_model.from_map(k1))

        if m.get('business_type') is not None:
            self.business_type = m.get('business_type')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')

        self.itinerary_list = []
        if m.get('itinerary_list') is not None:
            for k1 in m.get('itinerary_list'):
                temp_model = main_models.CarApplyQueryResponseBodyApplyListItineraryList()
                self.itinerary_list.append(temp_model.from_map(k1))

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('related_third_apply_id') is not None:
            self.related_third_apply_id = m.get('related_third_apply_id')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('status_desc') is not None:
            self.status_desc = m.get('status_desc')

        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')

        self.traveler_standard = []
        if m.get('traveler_standard') is not None:
            for k1 in m.get('traveler_standard'):
                temp_model = main_models.CarApplyQueryResponseBodyApplyListTravelerStandard()
                self.traveler_standard.append(temp_model.from_map(k1))

        if m.get('trip_cause') is not None:
            self.trip_cause = m.get('trip_cause')

        if m.get('trip_title') is not None:
            self.trip_title = m.get('trip_title')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class CarApplyQueryResponseBodyApplyListTravelerStandard(DaraModel):
    def __init__(
        self,
        car_city_set: List[main_models.CarApplyQueryResponseBodyApplyListTravelerStandardCarCitySet] = None,
        user_id: str = None,
    ):
        self.car_city_set = car_city_set
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
                temp_model = main_models.CarApplyQueryResponseBodyApplyListTravelerStandardCarCitySet()
                self.car_city_set.append(temp_model.from_map(k1))

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class CarApplyQueryResponseBodyApplyListTravelerStandardCarCitySet(DaraModel):
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

class CarApplyQueryResponseBodyApplyListItineraryList(DaraModel):
    def __init__(
        self,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_date: str = None,
        cost_center_id: int = None,
        cost_center_name: str = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_date: str = None,
        invoice_id: int = None,
        invoice_name: str = None,
        itinerary_id: str = None,
        project_code: str = None,
        project_title: str = None,
        traffic_type: int = None,
    ):
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.arr_date = arr_date
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.dep_date = dep_date
        self.invoice_id = invoice_id
        self.invoice_name = invoice_name
        self.itinerary_id = itinerary_id
        self.project_code = project_code
        self.project_title = project_title
        self.traffic_type = traffic_type

    def validate(self):
        pass

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

        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id

        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.invoice_id is not None:
            result['invoice_id'] = self.invoice_id

        if self.invoice_name is not None:
            result['invoice_name'] = self.invoice_name

        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.traffic_type is not None:
            result['traffic_type'] = self.traffic_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')

        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('invoice_id') is not None:
            self.invoice_id = m.get('invoice_id')

        if m.get('invoice_name') is not None:
            self.invoice_name = m.get('invoice_name')

        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('traffic_type') is not None:
            self.traffic_type = m.get('traffic_type')

        return self

class CarApplyQueryResponseBodyApplyListApproverList(DaraModel):
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

