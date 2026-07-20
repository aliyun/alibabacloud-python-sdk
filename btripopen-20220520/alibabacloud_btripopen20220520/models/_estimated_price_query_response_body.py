# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class EstimatedPriceQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: main_models.EstimatedPriceQueryResponseBodyModule = None,
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
            temp_model = main_models.EstimatedPriceQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class EstimatedPriceQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        hotel_fee_detail: List[main_models.EstimatedPriceQueryResponseBodyModuleHotelFeeDetail] = None,
        total_hotel_fee: int = None,
        traffic_fee: main_models.EstimatedPriceQueryResponseBodyModuleTrafficFee = None,
    ):
        self.hotel_fee_detail = hotel_fee_detail
        # 酒店费用总额，单位为元
        self.total_hotel_fee = total_hotel_fee
        self.traffic_fee = traffic_fee

    def validate(self):
        if self.hotel_fee_detail:
            for v1 in self.hotel_fee_detail:
                 if v1:
                    v1.validate()
        if self.traffic_fee:
            self.traffic_fee.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['hotel_fee_detail'] = []
        if self.hotel_fee_detail is not None:
            for k1 in self.hotel_fee_detail:
                result['hotel_fee_detail'].append(k1.to_map() if k1 else None)

        if self.total_hotel_fee is not None:
            result['total_hotel_fee'] = self.total_hotel_fee

        if self.traffic_fee is not None:
            result['traffic_fee'] = self.traffic_fee.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hotel_fee_detail = []
        if m.get('hotel_fee_detail') is not None:
            for k1 in m.get('hotel_fee_detail'):
                temp_model = main_models.EstimatedPriceQueryResponseBodyModuleHotelFeeDetail()
                self.hotel_fee_detail.append(temp_model.from_map(k1))

        if m.get('total_hotel_fee') is not None:
            self.total_hotel_fee = m.get('total_hotel_fee')

        if m.get('traffic_fee') is not None:
            temp_model = main_models.EstimatedPriceQueryResponseBodyModuleTrafficFee()
            self.traffic_fee = temp_model.from_map(m.get('traffic_fee'))

        return self

class EstimatedPriceQueryResponseBodyModuleTrafficFee(DaraModel):
    def __init__(
        self,
        btrip_routes: List[main_models.EstimatedPriceQueryResponseBodyModuleTrafficFeeBtripRoutes] = None,
        err_msg: str = None,
        max_fee: int = None,
        min_fee: int = None,
        success: bool = None,
    ):
        self.btrip_routes = btrip_routes
        self.err_msg = err_msg
        self.max_fee = max_fee
        self.min_fee = min_fee
        self.success = success

    def validate(self):
        if self.btrip_routes:
            for v1 in self.btrip_routes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['btrip_routes'] = []
        if self.btrip_routes is not None:
            for k1 in self.btrip_routes:
                result['btrip_routes'].append(k1.to_map() if k1 else None)

        if self.err_msg is not None:
            result['err_msg'] = self.err_msg

        if self.max_fee is not None:
            result['max_fee'] = self.max_fee

        if self.min_fee is not None:
            result['min_fee'] = self.min_fee

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.btrip_routes = []
        if m.get('btrip_routes') is not None:
            for k1 in m.get('btrip_routes'):
                temp_model = main_models.EstimatedPriceQueryResponseBodyModuleTrafficFeeBtripRoutes()
                self.btrip_routes.append(temp_model.from_map(k1))

        if m.get('err_msg') is not None:
            self.err_msg = m.get('err_msg')

        if m.get('max_fee') is not None:
            self.max_fee = m.get('max_fee')

        if m.get('min_fee') is not None:
            self.min_fee = m.get('min_fee')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class EstimatedPriceQueryResponseBodyModuleTrafficFeeBtripRoutes(DaraModel):
    def __init__(
        self,
        arr_city: str = None,
        arr_date: int = None,
        cheapest: main_models.EstimatedPriceQueryResponseBodyModuleTrafficFeeBtripRoutesCheapest = None,
        dep_city: str = None,
        dep_date: int = None,
        err_msg: str = None,
        itinerary_id: str = None,
        most_expensive: main_models.EstimatedPriceQueryResponseBodyModuleTrafficFeeBtripRoutesMostExpensive = None,
        success: bool = None,
    ):
        self.arr_city = arr_city
        self.arr_date = arr_date
        self.cheapest = cheapest
        self.dep_city = dep_city
        self.dep_date = dep_date
        self.err_msg = err_msg
        self.itinerary_id = itinerary_id
        self.most_expensive = most_expensive
        self.success = success

    def validate(self):
        if self.cheapest:
            self.cheapest.validate()
        if self.most_expensive:
            self.most_expensive.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_date is not None:
            result['arr_date'] = self.arr_date

        if self.cheapest is not None:
            result['cheapest'] = self.cheapest.to_map()

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.err_msg is not None:
            result['err_msg'] = self.err_msg

        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id

        if self.most_expensive is not None:
            result['most_expensive'] = self.most_expensive.to_map()

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')

        if m.get('cheapest') is not None:
            temp_model = main_models.EstimatedPriceQueryResponseBodyModuleTrafficFeeBtripRoutesCheapest()
            self.cheapest = temp_model.from_map(m.get('cheapest'))

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('err_msg') is not None:
            self.err_msg = m.get('err_msg')

        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')

        if m.get('most_expensive') is not None:
            temp_model = main_models.EstimatedPriceQueryResponseBodyModuleTrafficFeeBtripRoutesMostExpensive()
            self.most_expensive = temp_model.from_map(m.get('most_expensive'))

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class EstimatedPriceQueryResponseBodyModuleTrafficFeeBtripRoutesMostExpensive(DaraModel):
    def __init__(
        self,
        arr_time: str = None,
        dep_time: str = None,
        fee: int = None,
        seat_grade: str = None,
        vehicle_no: str = None,
    ):
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.fee = fee
        self.seat_grade = seat_grade
        self.vehicle_no = vehicle_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.fee is not None:
            result['fee'] = self.fee

        if self.seat_grade is not None:
            result['seat_grade'] = self.seat_grade

        if self.vehicle_no is not None:
            result['vehicle_no'] = self.vehicle_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('fee') is not None:
            self.fee = m.get('fee')

        if m.get('seat_grade') is not None:
            self.seat_grade = m.get('seat_grade')

        if m.get('vehicle_no') is not None:
            self.vehicle_no = m.get('vehicle_no')

        return self

class EstimatedPriceQueryResponseBodyModuleTrafficFeeBtripRoutesCheapest(DaraModel):
    def __init__(
        self,
        arr_time: str = None,
        dep_time: str = None,
        fee: int = None,
        seat_grade: str = None,
        vehicle_no: str = None,
    ):
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.fee = fee
        self.seat_grade = seat_grade
        self.vehicle_no = vehicle_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.fee is not None:
            result['fee'] = self.fee

        if self.seat_grade is not None:
            result['seat_grade'] = self.seat_grade

        if self.vehicle_no is not None:
            result['vehicle_no'] = self.vehicle_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('fee') is not None:
            self.fee = m.get('fee')

        if m.get('seat_grade') is not None:
            self.seat_grade = m.get('seat_grade')

        if m.get('vehicle_no') is not None:
            self.vehicle_no = m.get('vehicle_no')

        return self

class EstimatedPriceQueryResponseBodyModuleHotelFeeDetail(DaraModel):
    def __init__(
        self,
        city: str = None,
        criterion: int = None,
        itinerary_id: str = None,
        total: int = None,
        trip_days: int = None,
    ):
        self.city = city
        self.criterion = criterion
        self.itinerary_id = itinerary_id
        self.total = total
        self.trip_days = trip_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.city is not None:
            result['city'] = self.city

        if self.criterion is not None:
            result['criterion'] = self.criterion

        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id

        if self.total is not None:
            result['total'] = self.total

        if self.trip_days is not None:
            result['trip_days'] = self.trip_days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city') is not None:
            self.city = m.get('city')

        if m.get('criterion') is not None:
            self.criterion = m.get('criterion')

        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')

        if m.get('total') is not None:
            self.total = m.get('total')

        if m.get('trip_days') is not None:
            self.trip_days = m.get('trip_days')

        return self

