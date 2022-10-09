# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AccessTokenRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        app_secret: str = None,
    ):
        self.app_key = app_key
        self.app_secret = app_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['app_key'] = self.app_key
        if self.app_secret is not None:
            result['app_secret'] = self.app_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_key') is not None:
            self.app_key = m.get('app_key')
        if m.get('app_secret') is not None:
            self.app_secret = m.get('app_secret')
        return self


class AccessTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        expire: int = None,
        token: str = None,
    ):
        self.expire = expire
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire is not None:
            result['expire'] = self.expire
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expire') is not None:
            self.expire = m.get('expire')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class AccessTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AccessTokenResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = AccessTokenResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class AccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AccessTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddressGetHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class AddressGetRequest(TeaModel):
    def __init__(
        self,
        action_type: int = None,
        itinerary_id: str = None,
        phone: str = None,
        type: int = None,
        user_id: str = None,
    ):
        self.action_type = action_type
        self.itinerary_id = itinerary_id
        self.phone = phone
        self.type = type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['action_type'] = self.action_type
        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id
        if self.phone is not None:
            result['phone'] = self.phone
        if self.type is not None:
            result['type'] = self.type
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action_type') is not None:
            self.action_type = m.get('action_type')
        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class AddressGetResponseBodyModule(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class AddressGetResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: AddressGetResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = AddressGetResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class AddressGetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddressGetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddressGetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AirportSearchHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class AirportSearchRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        type: int = None,
    ):
        self.keyword = keyword
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AirportSearchResponseBodyModuleCities(TeaModel):
    def __init__(
        self,
        code: str = None,
        distance: int = None,
        name: str = None,
        travel_name: str = None,
    ):
        self.code = code
        self.distance = distance
        self.name = name
        self.travel_name = travel_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.distance is not None:
            result['distance'] = self.distance
        if self.name is not None:
            result['name'] = self.name
        if self.travel_name is not None:
            result['travel_name'] = self.travel_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('distance') is not None:
            self.distance = m.get('distance')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('travel_name') is not None:
            self.travel_name = m.get('travel_name')
        return self


class AirportSearchResponseBodyModule(TeaModel):
    def __init__(
        self,
        cities: List[AirportSearchResponseBodyModuleCities] = None,
        nearby: bool = None,
    ):
        self.cities = cities
        self.nearby = nearby

    def validate(self):
        if self.cities:
            for k in self.cities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['cities'] = []
        if self.cities is not None:
            for k in self.cities:
                result['cities'].append(k.to_map() if k else None)
        if self.nearby is not None:
            result['nearby'] = self.nearby
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cities = []
        if m.get('cities') is not None:
            for k in m.get('cities'):
                temp_model = AirportSearchResponseBodyModuleCities()
                self.cities.append(temp_model.from_map(k))
        if m.get('nearby') is not None:
            self.nearby = m.get('nearby')
        return self


class AirportSearchResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: AirportSearchResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = AirportSearchResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class AirportSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AirportSearchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AirportSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyAddHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class ApplyAddRequestExternalTravelerList(TeaModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class ApplyAddRequestExternalTravelerStandardHotelCitys(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ApplyAddRequestExternalTravelerStandard(TeaModel):
    def __init__(
        self,
        business_discount: int = None,
        economy_discount: int = None,
        first_discount: int = None,
        flight_cabins: str = None,
        hotel_citys: List[ApplyAddRequestExternalTravelerStandardHotelCitys] = None,
        reserve_type: int = None,
        train_seats: str = None,
    ):
        self.business_discount = business_discount
        self.economy_discount = economy_discount
        self.first_discount = first_discount
        self.flight_cabins = flight_cabins
        self.hotel_citys = hotel_citys
        self.reserve_type = reserve_type
        self.train_seats = train_seats

    def validate(self):
        if self.hotel_citys:
            for k in self.hotel_citys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_discount is not None:
            result['business_discount'] = self.business_discount
        if self.economy_discount is not None:
            result['economy_discount'] = self.economy_discount
        if self.first_discount is not None:
            result['first_discount'] = self.first_discount
        if self.flight_cabins is not None:
            result['flight_cabins'] = self.flight_cabins
        result['hotel_citys'] = []
        if self.hotel_citys is not None:
            for k in self.hotel_citys:
                result['hotel_citys'].append(k.to_map() if k else None)
        if self.reserve_type is not None:
            result['reserve_type'] = self.reserve_type
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
        self.hotel_citys = []
        if m.get('hotel_citys') is not None:
            for k in m.get('hotel_citys'):
                temp_model = ApplyAddRequestExternalTravelerStandardHotelCitys()
                self.hotel_citys.append(temp_model.from_map(k))
        if m.get('reserve_type') is not None:
            self.reserve_type = m.get('reserve_type')
        if m.get('train_seats') is not None:
            self.train_seats = m.get('train_seats')
        return self


class ApplyAddRequestHotelShare(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ApplyAddRequestItineraryList(TeaModel):
    def __init__(
        self,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_date: str = None,
        cost_center_id: int = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_date: str = None,
        invoice_id: int = None,
        itinerary_id: str = None,
        need_hotel: bool = None,
        need_traffic: bool = None,
        project_code: str = None,
        project_title: str = None,
        third_part_invoice_id: str = None,
        thirdpart_cost_center_id: str = None,
        traffic_type: int = None,
        trip_way: int = None,
    ):
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.arr_date = arr_date
        self.cost_center_id = cost_center_id
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.dep_date = dep_date
        self.invoice_id = invoice_id
        self.itinerary_id = itinerary_id
        self.need_hotel = need_hotel
        self.need_traffic = need_traffic
        self.project_code = project_code
        self.project_title = project_title
        self.third_part_invoice_id = third_part_invoice_id
        self.thirdpart_cost_center_id = thirdpart_cost_center_id
        self.traffic_type = traffic_type
        self.trip_way = trip_way

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city
        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code
        if self.arr_date is not None:
            result['arr_date'] = self.arr_date
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
        if self.need_hotel is not None:
            result['need_hotel'] = self.need_hotel
        if self.need_traffic is not None:
            result['need_traffic'] = self.need_traffic
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_title is not None:
            result['project_title'] = self.project_title
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
        if m.get('need_hotel') is not None:
            self.need_hotel = m.get('need_hotel')
        if m.get('need_traffic') is not None:
            self.need_traffic = m.get('need_traffic')
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')
        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')
        if m.get('thirdpart_cost_center_id') is not None:
            self.thirdpart_cost_center_id = m.get('thirdpart_cost_center_id')
        if m.get('traffic_type') is not None:
            self.traffic_type = m.get('traffic_type')
        if m.get('trip_way') is not None:
            self.trip_way = m.get('trip_way')
        return self


class ApplyAddRequestItinerarySetList(TeaModel):
    def __init__(
        self,
        arr_date: str = None,
        city_code_set: str = None,
        city_set: str = None,
        cost_center_id: int = None,
        dep_date: str = None,
        invoice_id: int = None,
        itinerary_id: str = None,
        project_code: str = None,
        project_title: str = None,
        third_part_invoice_id: str = None,
        thirdpart_cost_center_id: str = None,
        traffic_type: int = None,
    ):
        self.arr_date = arr_date
        self.city_code_set = city_code_set
        self.city_set = city_set
        self.cost_center_id = cost_center_id
        self.dep_date = dep_date
        self.invoice_id = invoice_id
        self.itinerary_id = itinerary_id
        self.project_code = project_code
        self.project_title = project_title
        self.third_part_invoice_id = third_part_invoice_id
        self.thirdpart_cost_center_id = thirdpart_cost_center_id
        self.traffic_type = traffic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arr_date is not None:
            result['arr_date'] = self.arr_date
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
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_title is not None:
            result['project_title'] = self.project_title
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
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')
        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')
        if m.get('thirdpart_cost_center_id') is not None:
            self.thirdpart_cost_center_id = m.get('thirdpart_cost_center_id')
        if m.get('traffic_type') is not None:
            self.traffic_type = m.get('traffic_type')
        return self


class ApplyAddRequestTravelerList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ApplyAddRequestTravelerStandardHotelCitys(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ApplyAddRequestTravelerStandard(TeaModel):
    def __init__(
        self,
        business_discount: int = None,
        economy_discount: int = None,
        first_discount: int = None,
        flight_cabins: str = None,
        hotel_citys: List[ApplyAddRequestTravelerStandardHotelCitys] = None,
        reserve_type: int = None,
        train_seats: str = None,
        user_id: str = None,
    ):
        self.business_discount = business_discount
        self.economy_discount = economy_discount
        self.first_discount = first_discount
        self.flight_cabins = flight_cabins
        self.hotel_citys = hotel_citys
        self.reserve_type = reserve_type
        self.train_seats = train_seats
        self.user_id = user_id

    def validate(self):
        if self.hotel_citys:
            for k in self.hotel_citys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_discount is not None:
            result['business_discount'] = self.business_discount
        if self.economy_discount is not None:
            result['economy_discount'] = self.economy_discount
        if self.first_discount is not None:
            result['first_discount'] = self.first_discount
        if self.flight_cabins is not None:
            result['flight_cabins'] = self.flight_cabins
        result['hotel_citys'] = []
        if self.hotel_citys is not None:
            for k in self.hotel_citys:
                result['hotel_citys'].append(k.to_map() if k else None)
        if self.reserve_type is not None:
            result['reserve_type'] = self.reserve_type
        if self.train_seats is not None:
            result['train_seats'] = self.train_seats
        if self.user_id is not None:
            result['user_id'] = self.user_id
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
        self.hotel_citys = []
        if m.get('hotel_citys') is not None:
            for k in m.get('hotel_citys'):
                temp_model = ApplyAddRequestTravelerStandardHotelCitys()
                self.hotel_citys.append(temp_model.from_map(k))
        if m.get('reserve_type') is not None:
            self.reserve_type = m.get('reserve_type')
        if m.get('train_seats') is not None:
            self.train_seats = m.get('train_seats')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class ApplyAddRequest(TeaModel):
    def __init__(
        self,
        budget: int = None,
        budget_merge: int = None,
        corp_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        external_traveler_list: List[ApplyAddRequestExternalTravelerList] = None,
        external_traveler_standard: ApplyAddRequestExternalTravelerStandard = None,
        flight_budget: int = None,
        hotel_budget: int = None,
        hotel_share: ApplyAddRequestHotelShare = None,
        international_flight_cabins: str = None,
        itinerary_list: List[ApplyAddRequestItineraryList] = None,
        itinerary_rule: int = None,
        itinerary_set_list: List[ApplyAddRequestItinerarySetList] = None,
        limit_traveler: int = None,
        status: int = None,
        thirdpart_apply_id: str = None,
        thirdpart_business_id: str = None,
        together_book_rule: int = None,
        train_budget: int = None,
        traveler_list: List[ApplyAddRequestTravelerList] = None,
        traveler_standard: List[ApplyAddRequestTravelerStandard] = None,
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
        self.corp_name = corp_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.external_traveler_list = external_traveler_list
        self.external_traveler_standard = external_traveler_standard
        self.flight_budget = flight_budget
        self.hotel_budget = hotel_budget
        self.hotel_share = hotel_share
        self.international_flight_cabins = international_flight_cabins
        self.itinerary_list = itinerary_list
        self.itinerary_rule = itinerary_rule
        self.itinerary_set_list = itinerary_set_list
        self.limit_traveler = limit_traveler
        self.status = status
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_business_id = thirdpart_business_id
        self.together_book_rule = together_book_rule
        self.train_budget = train_budget
        self.traveler_list = traveler_list
        self.traveler_standard = traveler_standard
        self.trip_cause = trip_cause
        self.trip_day = trip_day
        self.trip_title = trip_title
        self.type = type
        self.union_no = union_no
        self.user_id = user_id
        self.user_name = user_name
        self.vehicle_budget = vehicle_budget

    def validate(self):
        if self.external_traveler_list:
            for k in self.external_traveler_list:
                if k:
                    k.validate()
        if self.external_traveler_standard:
            self.external_traveler_standard.validate()
        if self.hotel_share:
            self.hotel_share.validate()
        if self.itinerary_list:
            for k in self.itinerary_list:
                if k:
                    k.validate()
        if self.itinerary_set_list:
            for k in self.itinerary_set_list:
                if k:
                    k.validate()
        if self.traveler_list:
            for k in self.traveler_list:
                if k:
                    k.validate()
        if self.traveler_standard:
            for k in self.traveler_standard:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.budget is not None:
            result['budget'] = self.budget
        if self.budget_merge is not None:
            result['budget_merge'] = self.budget_merge
        if self.corp_name is not None:
            result['corp_name'] = self.corp_name
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.depart_name is not None:
            result['depart_name'] = self.depart_name
        result['external_traveler_list'] = []
        if self.external_traveler_list is not None:
            for k in self.external_traveler_list:
                result['external_traveler_list'].append(k.to_map() if k else None)
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
        result['itinerary_list'] = []
        if self.itinerary_list is not None:
            for k in self.itinerary_list:
                result['itinerary_list'].append(k.to_map() if k else None)
        if self.itinerary_rule is not None:
            result['itinerary_rule'] = self.itinerary_rule
        result['itinerary_set_list'] = []
        if self.itinerary_set_list is not None:
            for k in self.itinerary_set_list:
                result['itinerary_set_list'].append(k.to_map() if k else None)
        if self.limit_traveler is not None:
            result['limit_traveler'] = self.limit_traveler
        if self.status is not None:
            result['status'] = self.status
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.thirdpart_business_id is not None:
            result['thirdpart_business_id'] = self.thirdpart_business_id
        if self.together_book_rule is not None:
            result['together_book_rule'] = self.together_book_rule
        if self.train_budget is not None:
            result['train_budget'] = self.train_budget
        result['traveler_list'] = []
        if self.traveler_list is not None:
            for k in self.traveler_list:
                result['traveler_list'].append(k.to_map() if k else None)
        result['traveler_standard'] = []
        if self.traveler_standard is not None:
            for k in self.traveler_standard:
                result['traveler_standard'].append(k.to_map() if k else None)
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
        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')
        self.external_traveler_list = []
        if m.get('external_traveler_list') is not None:
            for k in m.get('external_traveler_list'):
                temp_model = ApplyAddRequestExternalTravelerList()
                self.external_traveler_list.append(temp_model.from_map(k))
        if m.get('external_traveler_standard') is not None:
            temp_model = ApplyAddRequestExternalTravelerStandard()
            self.external_traveler_standard = temp_model.from_map(m['external_traveler_standard'])
        if m.get('flight_budget') is not None:
            self.flight_budget = m.get('flight_budget')
        if m.get('hotel_budget') is not None:
            self.hotel_budget = m.get('hotel_budget')
        if m.get('hotel_share') is not None:
            temp_model = ApplyAddRequestHotelShare()
            self.hotel_share = temp_model.from_map(m['hotel_share'])
        if m.get('international_flight_cabins') is not None:
            self.international_flight_cabins = m.get('international_flight_cabins')
        self.itinerary_list = []
        if m.get('itinerary_list') is not None:
            for k in m.get('itinerary_list'):
                temp_model = ApplyAddRequestItineraryList()
                self.itinerary_list.append(temp_model.from_map(k))
        if m.get('itinerary_rule') is not None:
            self.itinerary_rule = m.get('itinerary_rule')
        self.itinerary_set_list = []
        if m.get('itinerary_set_list') is not None:
            for k in m.get('itinerary_set_list'):
                temp_model = ApplyAddRequestItinerarySetList()
                self.itinerary_set_list.append(temp_model.from_map(k))
        if m.get('limit_traveler') is not None:
            self.limit_traveler = m.get('limit_traveler')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('thirdpart_business_id') is not None:
            self.thirdpart_business_id = m.get('thirdpart_business_id')
        if m.get('together_book_rule') is not None:
            self.together_book_rule = m.get('together_book_rule')
        if m.get('train_budget') is not None:
            self.train_budget = m.get('train_budget')
        self.traveler_list = []
        if m.get('traveler_list') is not None:
            for k in m.get('traveler_list'):
                temp_model = ApplyAddRequestTravelerList()
                self.traveler_list.append(temp_model.from_map(k))
        self.traveler_standard = []
        if m.get('traveler_standard') is not None:
            for k in m.get('traveler_standard'):
                temp_model = ApplyAddRequestTravelerStandard()
                self.traveler_standard.append(temp_model.from_map(k))
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


class ApplyAddShrinkRequest(TeaModel):
    def __init__(
        self,
        budget: int = None,
        budget_merge: int = None,
        corp_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        external_traveler_list_shrink: str = None,
        external_traveler_standard_shrink: str = None,
        flight_budget: int = None,
        hotel_budget: int = None,
        hotel_share_shrink: str = None,
        international_flight_cabins: str = None,
        itinerary_list_shrink: str = None,
        itinerary_rule: int = None,
        itinerary_set_list_shrink: str = None,
        limit_traveler: int = None,
        status: int = None,
        thirdpart_apply_id: str = None,
        thirdpart_business_id: str = None,
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
        self.corp_name = corp_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.external_traveler_list_shrink = external_traveler_list_shrink
        self.external_traveler_standard_shrink = external_traveler_standard_shrink
        self.flight_budget = flight_budget
        self.hotel_budget = hotel_budget
        self.hotel_share_shrink = hotel_share_shrink
        self.international_flight_cabins = international_flight_cabins
        self.itinerary_list_shrink = itinerary_list_shrink
        self.itinerary_rule = itinerary_rule
        self.itinerary_set_list_shrink = itinerary_set_list_shrink
        self.limit_traveler = limit_traveler
        self.status = status
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_business_id = thirdpart_business_id
        self.together_book_rule = together_book_rule
        self.train_budget = train_budget
        self.traveler_list_shrink = traveler_list_shrink
        self.traveler_standard_shrink = traveler_standard_shrink
        self.trip_cause = trip_cause
        self.trip_day = trip_day
        self.trip_title = trip_title
        self.type = type
        self.union_no = union_no
        self.user_id = user_id
        self.user_name = user_name
        self.vehicle_budget = vehicle_budget

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.budget is not None:
            result['budget'] = self.budget
        if self.budget_merge is not None:
            result['budget_merge'] = self.budget_merge
        if self.corp_name is not None:
            result['corp_name'] = self.corp_name
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.depart_name is not None:
            result['depart_name'] = self.depart_name
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
        if self.itinerary_list_shrink is not None:
            result['itinerary_list'] = self.itinerary_list_shrink
        if self.itinerary_rule is not None:
            result['itinerary_rule'] = self.itinerary_rule
        if self.itinerary_set_list_shrink is not None:
            result['itinerary_set_list'] = self.itinerary_set_list_shrink
        if self.limit_traveler is not None:
            result['limit_traveler'] = self.limit_traveler
        if self.status is not None:
            result['status'] = self.status
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.thirdpart_business_id is not None:
            result['thirdpart_business_id'] = self.thirdpart_business_id
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
        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')
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
        if m.get('itinerary_list') is not None:
            self.itinerary_list_shrink = m.get('itinerary_list')
        if m.get('itinerary_rule') is not None:
            self.itinerary_rule = m.get('itinerary_rule')
        if m.get('itinerary_set_list') is not None:
            self.itinerary_set_list_shrink = m.get('itinerary_set_list')
        if m.get('limit_traveler') is not None:
            self.limit_traveler = m.get('limit_traveler')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('thirdpart_business_id') is not None:
            self.thirdpart_business_id = m.get('thirdpart_business_id')
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


class ApplyAddResponseBodyModule(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        thirdpart_apply_id: str = None,
        thirdpart_business_id: str = None,
    ):
        self.apply_id = apply_id
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_business_id = thirdpart_business_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.thirdpart_business_id is not None:
            result['thirdpart_business_id'] = self.thirdpart_business_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('thirdpart_business_id') is not None:
            self.thirdpart_business_id = m.get('thirdpart_business_id')
        return self


class ApplyAddResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: ApplyAddResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ApplyAddResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class ApplyAddResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyAddResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyAddResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyApproveHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class ApplyApproveRequest(TeaModel):
    def __init__(
        self,
        apply_id: str = None,
        note: str = None,
        operate_time: str = None,
        status: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.apply_id = apply_id
        self.note = note
        self.operate_time = operate_time
        self.status = status
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.note is not None:
            result['note'] = self.note
        if self.operate_time is not None:
            result['operate_time'] = self.operate_time
        if self.status is not None:
            result['status'] = self.status
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('note') is not None:
            self.note = m.get('note')
        if m.get('operate_time') is not None:
            self.operate_time = m.get('operate_time')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class ApplyApproveResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.module is not None:
            result['module'] = self.module
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['trace_id'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('module') is not None:
            self.module = m.get('module')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('trace_id') is not None:
            self.trace_id = m.get('trace_id')
        return self


class ApplyApproveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyApproveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyApproveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyListQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class ApplyListQueryRequest(TeaModel):
    def __init__(
        self,
        all_apply: bool = None,
        depart_id: str = None,
        end_time: str = None,
        gmt_modified: str = None,
        only_shang_lv_apply: bool = None,
        page: int = None,
        page_size: int = None,
        start_time: str = None,
        type: int = None,
        union_no: str = None,
        user_id: str = None,
    ):
        self.all_apply = all_apply
        self.depart_id = depart_id
        self.end_time = end_time
        self.gmt_modified = gmt_modified
        self.only_shang_lv_apply = only_shang_lv_apply
        self.page = page
        self.page_size = page_size
        self.start_time = start_time
        self.type = type
        self.union_no = union_no
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_apply is not None:
            result['all_apply'] = self.all_apply
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified
        if self.only_shang_lv_apply is not None:
            result['only_shang_lv_apply'] = self.only_shang_lv_apply
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.type is not None:
            result['type'] = self.type
        if self.union_no is not None:
            result['union_no'] = self.union_no
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all_apply') is not None:
            self.all_apply = m.get('all_apply')
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')
        if m.get('only_shang_lv_apply') is not None:
            self.only_shang_lv_apply = m.get('only_shang_lv_apply')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('union_no') is not None:
            self.union_no = m.get('union_no')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class ApplyListQueryResponseBodyModuleListApproverList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ApplyListQueryResponseBodyModuleListExternalTravelerList(TeaModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class ApplyListQueryResponseBodyModuleListItineraryList(TeaModel):
    def __init__(
        self,
        arr_city: str = None,
        arr_date: str = None,
        cost_center_name: str = None,
        dep_city: str = None,
        dep_date: str = None,
        invoice_name: str = None,
        itinerary_id: str = None,
        project_code: str = None,
        project_title: str = None,
        traffic_type: int = None,
        trip_way: int = None,
    ):
        self.arr_city = arr_city
        self.arr_date = arr_date
        self.cost_center_name = cost_center_name
        self.dep_city = dep_city
        self.dep_date = dep_date
        self.invoice_name = invoice_name
        self.itinerary_id = itinerary_id
        self.project_code = project_code
        self.project_title = project_title
        self.traffic_type = traffic_type
        self.trip_way = trip_way

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city
        if self.arr_date is not None:
            result['arr_date'] = self.arr_date
        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name
        if self.dep_city is not None:
            result['dep_city'] = self.dep_city
        if self.dep_date is not None:
            result['dep_date'] = self.dep_date
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
        if self.trip_way is not None:
            result['trip_way'] = self.trip_way
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')
        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')
        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')
        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')
        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')
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
        if m.get('trip_way') is not None:
            self.trip_way = m.get('trip_way')
        return self


class ApplyListQueryResponseBodyModuleListItinerarySetList(TeaModel):
    def __init__(
        self,
        arr_date: str = None,
        city_code_set: str = None,
        city_set: str = None,
        cost_center_name: str = None,
        dep_date: str = None,
        invoice_name: str = None,
        itinerary_id: str = None,
        project_code: str = None,
        project_title: str = None,
        traffic_type: int = None,
    ):
        self.arr_date = arr_date
        self.city_code_set = city_code_set
        self.city_set = city_set
        self.cost_center_name = cost_center_name
        self.dep_date = dep_date
        self.invoice_name = invoice_name
        self.itinerary_id = itinerary_id
        self.project_code = project_code
        self.project_title = project_title
        self.traffic_type = traffic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arr_date is not None:
            result['arr_date'] = self.arr_date
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
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_title is not None:
            result['project_title'] = self.project_title
        if self.traffic_type is not None:
            result['traffic_type'] = self.traffic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')
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
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')
        if m.get('traffic_type') is not None:
            self.traffic_type = m.get('traffic_type')
        return self


class ApplyListQueryResponseBodyModuleListTravelerList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ApplyListQueryResponseBodyModuleList(TeaModel):
    def __init__(
        self,
        apply_show_id: str = None,
        approver_list: List[ApplyListQueryResponseBodyModuleListApproverList] = None,
        corp_id: str = None,
        corp_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        external_traveler_list: List[ApplyListQueryResponseBodyModuleListExternalTravelerList] = None,
        flow_code: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        itinerary_list: List[ApplyListQueryResponseBodyModuleListItineraryList] = None,
        itinerary_rule: int = None,
        itinerary_set_list: List[ApplyListQueryResponseBodyModuleListItinerarySetList] = None,
        status: int = None,
        status_desc: str = None,
        thirdpart_business_id: str = None,
        thirdpart_id: str = None,
        traveler_list: List[ApplyListQueryResponseBodyModuleListTravelerList] = None,
        trip_cause: str = None,
        trip_day: int = None,
        trip_title: str = None,
        type: int = None,
        union_no: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.apply_show_id = apply_show_id
        self.approver_list = approver_list
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.external_traveler_list = external_traveler_list
        self.flow_code = flow_code
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.itinerary_list = itinerary_list
        self.itinerary_rule = itinerary_rule
        self.itinerary_set_list = itinerary_set_list
        self.status = status
        self.status_desc = status_desc
        self.thirdpart_business_id = thirdpart_business_id
        self.thirdpart_id = thirdpart_id
        self.traveler_list = traveler_list
        self.trip_cause = trip_cause
        self.trip_day = trip_day
        self.trip_title = trip_title
        self.type = type
        self.union_no = union_no
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.approver_list:
            for k in self.approver_list:
                if k:
                    k.validate()
        if self.external_traveler_list:
            for k in self.external_traveler_list:
                if k:
                    k.validate()
        if self.itinerary_list:
            for k in self.itinerary_list:
                if k:
                    k.validate()
        if self.itinerary_set_list:
            for k in self.itinerary_set_list:
                if k:
                    k.validate()
        if self.traveler_list:
            for k in self.traveler_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_show_id is not None:
            result['apply_show_id'] = self.apply_show_id
        result['approver_list'] = []
        if self.approver_list is not None:
            for k in self.approver_list:
                result['approver_list'].append(k.to_map() if k else None)
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.corp_name is not None:
            result['corp_name'] = self.corp_name
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.depart_name is not None:
            result['depart_name'] = self.depart_name
        result['external_traveler_list'] = []
        if self.external_traveler_list is not None:
            for k in self.external_traveler_list:
                result['external_traveler_list'].append(k.to_map() if k else None)
        if self.flow_code is not None:
            result['flow_code'] = self.flow_code
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        result['itinerary_list'] = []
        if self.itinerary_list is not None:
            for k in self.itinerary_list:
                result['itinerary_list'].append(k.to_map() if k else None)
        if self.itinerary_rule is not None:
            result['itinerary_rule'] = self.itinerary_rule
        result['itinerary_set_list'] = []
        if self.itinerary_set_list is not None:
            for k in self.itinerary_set_list:
                result['itinerary_set_list'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.status_desc is not None:
            result['status_desc'] = self.status_desc
        if self.thirdpart_business_id is not None:
            result['thirdpart_business_id'] = self.thirdpart_business_id
        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id
        result['traveler_list'] = []
        if self.traveler_list is not None:
            for k in self.traveler_list:
                result['traveler_list'].append(k.to_map() if k else None)
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_show_id') is not None:
            self.apply_show_id = m.get('apply_show_id')
        self.approver_list = []
        if m.get('approver_list') is not None:
            for k in m.get('approver_list'):
                temp_model = ApplyListQueryResponseBodyModuleListApproverList()
                self.approver_list.append(temp_model.from_map(k))
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')
        self.external_traveler_list = []
        if m.get('external_traveler_list') is not None:
            for k in m.get('external_traveler_list'):
                temp_model = ApplyListQueryResponseBodyModuleListExternalTravelerList()
                self.external_traveler_list.append(temp_model.from_map(k))
        if m.get('flow_code') is not None:
            self.flow_code = m.get('flow_code')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')
        if m.get('id') is not None:
            self.id = m.get('id')
        self.itinerary_list = []
        if m.get('itinerary_list') is not None:
            for k in m.get('itinerary_list'):
                temp_model = ApplyListQueryResponseBodyModuleListItineraryList()
                self.itinerary_list.append(temp_model.from_map(k))
        if m.get('itinerary_rule') is not None:
            self.itinerary_rule = m.get('itinerary_rule')
        self.itinerary_set_list = []
        if m.get('itinerary_set_list') is not None:
            for k in m.get('itinerary_set_list'):
                temp_model = ApplyListQueryResponseBodyModuleListItinerarySetList()
                self.itinerary_set_list.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('status_desc') is not None:
            self.status_desc = m.get('status_desc')
        if m.get('thirdpart_business_id') is not None:
            self.thirdpart_business_id = m.get('thirdpart_business_id')
        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')
        self.traveler_list = []
        if m.get('traveler_list') is not None:
            for k in m.get('traveler_list'):
                temp_model = ApplyListQueryResponseBodyModuleListTravelerList()
                self.traveler_list.append(temp_model.from_map(k))
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
        return self


class ApplyListQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module_list: List[ApplyListQueryResponseBodyModuleList] = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module_list = module_list
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module_list:
            for k in self.module_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        result['module_list'] = []
        if self.module_list is not None:
            for k in self.module_list:
                result['module_list'].append(k.to_map() if k else None)
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
        self.module_list = []
        if m.get('module_list') is not None:
            for k in m.get('module_list'):
                temp_model = ApplyListQueryResponseBodyModuleList()
                self.module_list.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class ApplyListQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyListQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyListQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyModifyHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class ApplyModifyRequestExternalTravelerList(TeaModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class ApplyModifyRequestExternalTravelerStandardHotelCitys(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ApplyModifyRequestExternalTravelerStandard(TeaModel):
    def __init__(
        self,
        business_discount: int = None,
        economy_discount: int = None,
        first_discount: int = None,
        flight_cabins: str = None,
        hotel_citys: List[ApplyModifyRequestExternalTravelerStandardHotelCitys] = None,
        reserve_type: int = None,
        train_seats: str = None,
    ):
        self.business_discount = business_discount
        self.economy_discount = economy_discount
        self.first_discount = first_discount
        self.flight_cabins = flight_cabins
        self.hotel_citys = hotel_citys
        self.reserve_type = reserve_type
        self.train_seats = train_seats

    def validate(self):
        if self.hotel_citys:
            for k in self.hotel_citys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_discount is not None:
            result['business_discount'] = self.business_discount
        if self.economy_discount is not None:
            result['economy_discount'] = self.economy_discount
        if self.first_discount is not None:
            result['first_discount'] = self.first_discount
        if self.flight_cabins is not None:
            result['flight_cabins'] = self.flight_cabins
        result['hotel_citys'] = []
        if self.hotel_citys is not None:
            for k in self.hotel_citys:
                result['hotel_citys'].append(k.to_map() if k else None)
        if self.reserve_type is not None:
            result['reserve_type'] = self.reserve_type
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
        self.hotel_citys = []
        if m.get('hotel_citys') is not None:
            for k in m.get('hotel_citys'):
                temp_model = ApplyModifyRequestExternalTravelerStandardHotelCitys()
                self.hotel_citys.append(temp_model.from_map(k))
        if m.get('reserve_type') is not None:
            self.reserve_type = m.get('reserve_type')
        if m.get('train_seats') is not None:
            self.train_seats = m.get('train_seats')
        return self


class ApplyModifyRequestHotelShare(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ApplyModifyRequestItineraryList(TeaModel):
    def __init__(
        self,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_date: str = None,
        cost_center_id: int = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_date: str = None,
        invoice_id: int = None,
        itinerary_id: str = None,
        need_hotel: bool = None,
        need_traffic: bool = None,
        project_code: str = None,
        project_title: str = None,
        third_part_invoice_id: str = None,
        thirdpart_cost_center_id: str = None,
        traffic_type: int = None,
        trip_way: int = None,
    ):
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.arr_date = arr_date
        self.cost_center_id = cost_center_id
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.dep_date = dep_date
        self.invoice_id = invoice_id
        self.itinerary_id = itinerary_id
        self.need_hotel = need_hotel
        self.need_traffic = need_traffic
        self.project_code = project_code
        self.project_title = project_title
        self.third_part_invoice_id = third_part_invoice_id
        self.thirdpart_cost_center_id = thirdpart_cost_center_id
        self.traffic_type = traffic_type
        self.trip_way = trip_way

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city
        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code
        if self.arr_date is not None:
            result['arr_date'] = self.arr_date
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
        if self.need_hotel is not None:
            result['need_hotel'] = self.need_hotel
        if self.need_traffic is not None:
            result['need_traffic'] = self.need_traffic
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_title is not None:
            result['project_title'] = self.project_title
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
        if m.get('need_hotel') is not None:
            self.need_hotel = m.get('need_hotel')
        if m.get('need_traffic') is not None:
            self.need_traffic = m.get('need_traffic')
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')
        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')
        if m.get('thirdpart_cost_center_id') is not None:
            self.thirdpart_cost_center_id = m.get('thirdpart_cost_center_id')
        if m.get('traffic_type') is not None:
            self.traffic_type = m.get('traffic_type')
        if m.get('trip_way') is not None:
            self.trip_way = m.get('trip_way')
        return self


class ApplyModifyRequestItinerarySetList(TeaModel):
    def __init__(
        self,
        arr_date: str = None,
        city_code_set: str = None,
        city_set: str = None,
        cost_center_id: int = None,
        dep_date: str = None,
        invoice_id: int = None,
        itinerary_id: str = None,
        project_code: str = None,
        project_title: str = None,
        third_part_invoice_id: str = None,
        thirdpart_cost_center_id: str = None,
        traffic_type: int = None,
    ):
        self.arr_date = arr_date
        self.city_code_set = city_code_set
        self.city_set = city_set
        self.cost_center_id = cost_center_id
        self.dep_date = dep_date
        self.invoice_id = invoice_id
        self.itinerary_id = itinerary_id
        self.project_code = project_code
        self.project_title = project_title
        self.third_part_invoice_id = third_part_invoice_id
        self.thirdpart_cost_center_id = thirdpart_cost_center_id
        self.traffic_type = traffic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arr_date is not None:
            result['arr_date'] = self.arr_date
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
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_title is not None:
            result['project_title'] = self.project_title
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
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')
        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')
        if m.get('thirdpart_cost_center_id') is not None:
            self.thirdpart_cost_center_id = m.get('thirdpart_cost_center_id')
        if m.get('traffic_type') is not None:
            self.traffic_type = m.get('traffic_type')
        return self


class ApplyModifyRequestTravelerList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ApplyModifyRequestTravelerStandardHotelCitys(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ApplyModifyRequestTravelerStandard(TeaModel):
    def __init__(
        self,
        business_discount: int = None,
        economy_discount: int = None,
        first_discount: int = None,
        flight_cabins: str = None,
        hotel_citys: List[ApplyModifyRequestTravelerStandardHotelCitys] = None,
        reserve_type: int = None,
        train_seats: str = None,
        user_id: str = None,
    ):
        self.business_discount = business_discount
        self.economy_discount = economy_discount
        self.first_discount = first_discount
        self.flight_cabins = flight_cabins
        self.hotel_citys = hotel_citys
        self.reserve_type = reserve_type
        self.train_seats = train_seats
        self.user_id = user_id

    def validate(self):
        if self.hotel_citys:
            for k in self.hotel_citys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_discount is not None:
            result['business_discount'] = self.business_discount
        if self.economy_discount is not None:
            result['economy_discount'] = self.economy_discount
        if self.first_discount is not None:
            result['first_discount'] = self.first_discount
        if self.flight_cabins is not None:
            result['flight_cabins'] = self.flight_cabins
        result['hotel_citys'] = []
        if self.hotel_citys is not None:
            for k in self.hotel_citys:
                result['hotel_citys'].append(k.to_map() if k else None)
        if self.reserve_type is not None:
            result['reserve_type'] = self.reserve_type
        if self.train_seats is not None:
            result['train_seats'] = self.train_seats
        if self.user_id is not None:
            result['user_id'] = self.user_id
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
        self.hotel_citys = []
        if m.get('hotel_citys') is not None:
            for k in m.get('hotel_citys'):
                temp_model = ApplyModifyRequestTravelerStandardHotelCitys()
                self.hotel_citys.append(temp_model.from_map(k))
        if m.get('reserve_type') is not None:
            self.reserve_type = m.get('reserve_type')
        if m.get('train_seats') is not None:
            self.train_seats = m.get('train_seats')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class ApplyModifyRequest(TeaModel):
    def __init__(
        self,
        budget: int = None,
        budget_merge: int = None,
        corp_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        external_traveler_list: List[ApplyModifyRequestExternalTravelerList] = None,
        external_traveler_standard: ApplyModifyRequestExternalTravelerStandard = None,
        flight_budget: int = None,
        hotel_budget: int = None,
        hotel_share: ApplyModifyRequestHotelShare = None,
        itinerary_list: List[ApplyModifyRequestItineraryList] = None,
        itinerary_rule: int = None,
        itinerary_set_list: List[ApplyModifyRequestItinerarySetList] = None,
        limit_traveler: int = None,
        status: int = None,
        thirdpart_apply_id: str = None,
        thirdpart_business_id: str = None,
        together_book_rule: int = None,
        train_budget: int = None,
        traveler_list: List[ApplyModifyRequestTravelerList] = None,
        traveler_standard: List[ApplyModifyRequestTravelerStandard] = None,
        trip_cause: str = None,
        trip_day: int = None,
        trip_title: str = None,
        union_no: str = None,
        user_id: str = None,
        user_name: str = None,
        vehicle_budget: int = None,
    ):
        self.budget = budget
        self.budget_merge = budget_merge
        self.corp_name = corp_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.external_traveler_list = external_traveler_list
        self.external_traveler_standard = external_traveler_standard
        self.flight_budget = flight_budget
        self.hotel_budget = hotel_budget
        self.hotel_share = hotel_share
        self.itinerary_list = itinerary_list
        self.itinerary_rule = itinerary_rule
        self.itinerary_set_list = itinerary_set_list
        self.limit_traveler = limit_traveler
        self.status = status
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_business_id = thirdpart_business_id
        self.together_book_rule = together_book_rule
        self.train_budget = train_budget
        self.traveler_list = traveler_list
        self.traveler_standard = traveler_standard
        self.trip_cause = trip_cause
        self.trip_day = trip_day
        self.trip_title = trip_title
        self.union_no = union_no
        self.user_id = user_id
        self.user_name = user_name
        self.vehicle_budget = vehicle_budget

    def validate(self):
        if self.external_traveler_list:
            for k in self.external_traveler_list:
                if k:
                    k.validate()
        if self.external_traveler_standard:
            self.external_traveler_standard.validate()
        if self.hotel_share:
            self.hotel_share.validate()
        if self.itinerary_list:
            for k in self.itinerary_list:
                if k:
                    k.validate()
        if self.itinerary_set_list:
            for k in self.itinerary_set_list:
                if k:
                    k.validate()
        if self.traveler_list:
            for k in self.traveler_list:
                if k:
                    k.validate()
        if self.traveler_standard:
            for k in self.traveler_standard:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.budget is not None:
            result['budget'] = self.budget
        if self.budget_merge is not None:
            result['budget_merge'] = self.budget_merge
        if self.corp_name is not None:
            result['corp_name'] = self.corp_name
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.depart_name is not None:
            result['depart_name'] = self.depart_name
        result['external_traveler_list'] = []
        if self.external_traveler_list is not None:
            for k in self.external_traveler_list:
                result['external_traveler_list'].append(k.to_map() if k else None)
        if self.external_traveler_standard is not None:
            result['external_traveler_standard'] = self.external_traveler_standard.to_map()
        if self.flight_budget is not None:
            result['flight_budget'] = self.flight_budget
        if self.hotel_budget is not None:
            result['hotel_budget'] = self.hotel_budget
        if self.hotel_share is not None:
            result['hotel_share'] = self.hotel_share.to_map()
        result['itinerary_list'] = []
        if self.itinerary_list is not None:
            for k in self.itinerary_list:
                result['itinerary_list'].append(k.to_map() if k else None)
        if self.itinerary_rule is not None:
            result['itinerary_rule'] = self.itinerary_rule
        result['itinerary_set_list'] = []
        if self.itinerary_set_list is not None:
            for k in self.itinerary_set_list:
                result['itinerary_set_list'].append(k.to_map() if k else None)
        if self.limit_traveler is not None:
            result['limit_traveler'] = self.limit_traveler
        if self.status is not None:
            result['status'] = self.status
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.thirdpart_business_id is not None:
            result['thirdpart_business_id'] = self.thirdpart_business_id
        if self.together_book_rule is not None:
            result['together_book_rule'] = self.together_book_rule
        if self.train_budget is not None:
            result['train_budget'] = self.train_budget
        result['traveler_list'] = []
        if self.traveler_list is not None:
            for k in self.traveler_list:
                result['traveler_list'].append(k.to_map() if k else None)
        result['traveler_standard'] = []
        if self.traveler_standard is not None:
            for k in self.traveler_standard:
                result['traveler_standard'].append(k.to_map() if k else None)
        if self.trip_cause is not None:
            result['trip_cause'] = self.trip_cause
        if self.trip_day is not None:
            result['trip_day'] = self.trip_day
        if self.trip_title is not None:
            result['trip_title'] = self.trip_title
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
        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')
        self.external_traveler_list = []
        if m.get('external_traveler_list') is not None:
            for k in m.get('external_traveler_list'):
                temp_model = ApplyModifyRequestExternalTravelerList()
                self.external_traveler_list.append(temp_model.from_map(k))
        if m.get('external_traveler_standard') is not None:
            temp_model = ApplyModifyRequestExternalTravelerStandard()
            self.external_traveler_standard = temp_model.from_map(m['external_traveler_standard'])
        if m.get('flight_budget') is not None:
            self.flight_budget = m.get('flight_budget')
        if m.get('hotel_budget') is not None:
            self.hotel_budget = m.get('hotel_budget')
        if m.get('hotel_share') is not None:
            temp_model = ApplyModifyRequestHotelShare()
            self.hotel_share = temp_model.from_map(m['hotel_share'])
        self.itinerary_list = []
        if m.get('itinerary_list') is not None:
            for k in m.get('itinerary_list'):
                temp_model = ApplyModifyRequestItineraryList()
                self.itinerary_list.append(temp_model.from_map(k))
        if m.get('itinerary_rule') is not None:
            self.itinerary_rule = m.get('itinerary_rule')
        self.itinerary_set_list = []
        if m.get('itinerary_set_list') is not None:
            for k in m.get('itinerary_set_list'):
                temp_model = ApplyModifyRequestItinerarySetList()
                self.itinerary_set_list.append(temp_model.from_map(k))
        if m.get('limit_traveler') is not None:
            self.limit_traveler = m.get('limit_traveler')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('thirdpart_business_id') is not None:
            self.thirdpart_business_id = m.get('thirdpart_business_id')
        if m.get('together_book_rule') is not None:
            self.together_book_rule = m.get('together_book_rule')
        if m.get('train_budget') is not None:
            self.train_budget = m.get('train_budget')
        self.traveler_list = []
        if m.get('traveler_list') is not None:
            for k in m.get('traveler_list'):
                temp_model = ApplyModifyRequestTravelerList()
                self.traveler_list.append(temp_model.from_map(k))
        self.traveler_standard = []
        if m.get('traveler_standard') is not None:
            for k in m.get('traveler_standard'):
                temp_model = ApplyModifyRequestTravelerStandard()
                self.traveler_standard.append(temp_model.from_map(k))
        if m.get('trip_cause') is not None:
            self.trip_cause = m.get('trip_cause')
        if m.get('trip_day') is not None:
            self.trip_day = m.get('trip_day')
        if m.get('trip_title') is not None:
            self.trip_title = m.get('trip_title')
        if m.get('union_no') is not None:
            self.union_no = m.get('union_no')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        if m.get('vehicle_budget') is not None:
            self.vehicle_budget = m.get('vehicle_budget')
        return self


class ApplyModifyShrinkRequest(TeaModel):
    def __init__(
        self,
        budget: int = None,
        budget_merge: int = None,
        corp_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        external_traveler_list_shrink: str = None,
        external_traveler_standard_shrink: str = None,
        flight_budget: int = None,
        hotel_budget: int = None,
        hotel_share_shrink: str = None,
        itinerary_list_shrink: str = None,
        itinerary_rule: int = None,
        itinerary_set_list_shrink: str = None,
        limit_traveler: int = None,
        status: int = None,
        thirdpart_apply_id: str = None,
        thirdpart_business_id: str = None,
        together_book_rule: int = None,
        train_budget: int = None,
        traveler_list_shrink: str = None,
        traveler_standard_shrink: str = None,
        trip_cause: str = None,
        trip_day: int = None,
        trip_title: str = None,
        union_no: str = None,
        user_id: str = None,
        user_name: str = None,
        vehicle_budget: int = None,
    ):
        self.budget = budget
        self.budget_merge = budget_merge
        self.corp_name = corp_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.external_traveler_list_shrink = external_traveler_list_shrink
        self.external_traveler_standard_shrink = external_traveler_standard_shrink
        self.flight_budget = flight_budget
        self.hotel_budget = hotel_budget
        self.hotel_share_shrink = hotel_share_shrink
        self.itinerary_list_shrink = itinerary_list_shrink
        self.itinerary_rule = itinerary_rule
        self.itinerary_set_list_shrink = itinerary_set_list_shrink
        self.limit_traveler = limit_traveler
        self.status = status
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_business_id = thirdpart_business_id
        self.together_book_rule = together_book_rule
        self.train_budget = train_budget
        self.traveler_list_shrink = traveler_list_shrink
        self.traveler_standard_shrink = traveler_standard_shrink
        self.trip_cause = trip_cause
        self.trip_day = trip_day
        self.trip_title = trip_title
        self.union_no = union_no
        self.user_id = user_id
        self.user_name = user_name
        self.vehicle_budget = vehicle_budget

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.budget is not None:
            result['budget'] = self.budget
        if self.budget_merge is not None:
            result['budget_merge'] = self.budget_merge
        if self.corp_name is not None:
            result['corp_name'] = self.corp_name
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.depart_name is not None:
            result['depart_name'] = self.depart_name
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
        if self.itinerary_list_shrink is not None:
            result['itinerary_list'] = self.itinerary_list_shrink
        if self.itinerary_rule is not None:
            result['itinerary_rule'] = self.itinerary_rule
        if self.itinerary_set_list_shrink is not None:
            result['itinerary_set_list'] = self.itinerary_set_list_shrink
        if self.limit_traveler is not None:
            result['limit_traveler'] = self.limit_traveler
        if self.status is not None:
            result['status'] = self.status
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.thirdpart_business_id is not None:
            result['thirdpart_business_id'] = self.thirdpart_business_id
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
        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')
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
        if m.get('itinerary_list') is not None:
            self.itinerary_list_shrink = m.get('itinerary_list')
        if m.get('itinerary_rule') is not None:
            self.itinerary_rule = m.get('itinerary_rule')
        if m.get('itinerary_set_list') is not None:
            self.itinerary_set_list_shrink = m.get('itinerary_set_list')
        if m.get('limit_traveler') is not None:
            self.limit_traveler = m.get('limit_traveler')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('thirdpart_business_id') is not None:
            self.thirdpart_business_id = m.get('thirdpart_business_id')
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
        if m.get('union_no') is not None:
            self.union_no = m.get('union_no')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        if m.get('vehicle_budget') is not None:
            self.vehicle_budget = m.get('vehicle_budget')
        return self


class ApplyModifyResponseBodyModule(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        thirdpart_apply_id: str = None,
        thirdpart_business_id: str = None,
    ):
        self.apply_id = apply_id
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_business_id = thirdpart_business_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.thirdpart_business_id is not None:
            result['thirdpart_business_id'] = self.thirdpart_business_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('thirdpart_business_id') is not None:
            self.thirdpart_business_id = m.get('thirdpart_business_id')
        return self


class ApplyModifyResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: ApplyModifyResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ApplyModifyResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class ApplyModifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyModifyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyModifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class ApplyQueryRequest(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        apply_show_id: str = None,
        thirdpart_apply_id: str = None,
        type: int = None,
    ):
        self.apply_id = apply_id
        self.apply_show_id = apply_show_id
        self.thirdpart_apply_id = thirdpart_apply_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.apply_show_id is not None:
            result['apply_show_id'] = self.apply_show_id
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('apply_show_id') is not None:
            self.apply_show_id = m.get('apply_show_id')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ApplyQueryResponseBodyModuleApproverList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ApplyQueryResponseBodyModuleExternalTravelerListHotelCitys(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ApplyQueryResponseBodyModuleExternalTravelerList(TeaModel):
    def __init__(
        self,
        business_discount: int = None,
        economy_discount: int = None,
        first_discount: int = None,
        flight_cabins: str = None,
        hotel_citys: List[ApplyQueryResponseBodyModuleExternalTravelerListHotelCitys] = None,
        reserve_type: int = None,
        train_seats: str = None,
        user_name: str = None,
    ):
        self.business_discount = business_discount
        self.economy_discount = economy_discount
        self.first_discount = first_discount
        self.flight_cabins = flight_cabins
        self.hotel_citys = hotel_citys
        self.reserve_type = reserve_type
        self.train_seats = train_seats
        self.user_name = user_name

    def validate(self):
        if self.hotel_citys:
            for k in self.hotel_citys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_discount is not None:
            result['business_discount'] = self.business_discount
        if self.economy_discount is not None:
            result['economy_discount'] = self.economy_discount
        if self.first_discount is not None:
            result['first_discount'] = self.first_discount
        if self.flight_cabins is not None:
            result['flight_cabins'] = self.flight_cabins
        result['hotel_citys'] = []
        if self.hotel_citys is not None:
            for k in self.hotel_citys:
                result['hotel_citys'].append(k.to_map() if k else None)
        if self.reserve_type is not None:
            result['reserve_type'] = self.reserve_type
        if self.train_seats is not None:
            result['train_seats'] = self.train_seats
        if self.user_name is not None:
            result['user_name'] = self.user_name
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
        self.hotel_citys = []
        if m.get('hotel_citys') is not None:
            for k in m.get('hotel_citys'):
                temp_model = ApplyQueryResponseBodyModuleExternalTravelerListHotelCitys()
                self.hotel_citys.append(temp_model.from_map(k))
        if m.get('reserve_type') is not None:
            self.reserve_type = m.get('reserve_type')
        if m.get('train_seats') is not None:
            self.train_seats = m.get('train_seats')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class ApplyQueryResponseBodyModuleHotelShare(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ApplyQueryResponseBodyModuleItineraryList(TeaModel):
    def __init__(
        self,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_date: str = None,
        cost_center_name: str = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_date: str = None,
        invoice_name: str = None,
        itinerary_id: str = None,
        project_code: str = None,
        project_title: str = None,
        traffic_type: int = None,
        trip_way: int = None,
    ):
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.arr_date = arr_date
        self.cost_center_name = cost_center_name
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.dep_date = dep_date
        self.invoice_name = invoice_name
        self.itinerary_id = itinerary_id
        self.project_code = project_code
        self.project_title = project_title
        self.traffic_type = traffic_type
        self.trip_way = trip_way

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city
        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code
        if self.arr_date is not None:
            result['arr_date'] = self.arr_date
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
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_title is not None:
            result['project_title'] = self.project_title
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
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')
        if m.get('traffic_type') is not None:
            self.traffic_type = m.get('traffic_type')
        if m.get('trip_way') is not None:
            self.trip_way = m.get('trip_way')
        return self


class ApplyQueryResponseBodyModuleItinerarySetList(TeaModel):
    def __init__(
        self,
        arr_date: str = None,
        city_code_set: str = None,
        city_set: str = None,
        cost_center_name: str = None,
        dep_date: str = None,
        invoice_name: str = None,
        itinerary_id: str = None,
        project_code: str = None,
        project_title: str = None,
        traffic_type: int = None,
    ):
        self.arr_date = arr_date
        self.city_code_set = city_code_set
        self.city_set = city_set
        self.cost_center_name = cost_center_name
        self.dep_date = dep_date
        self.invoice_name = invoice_name
        self.itinerary_id = itinerary_id
        self.project_code = project_code
        self.project_title = project_title
        self.traffic_type = traffic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arr_date is not None:
            result['arr_date'] = self.arr_date
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
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_title is not None:
            result['project_title'] = self.project_title
        if self.traffic_type is not None:
            result['traffic_type'] = self.traffic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')
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
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')
        if m.get('traffic_type') is not None:
            self.traffic_type = m.get('traffic_type')
        return self


class ApplyQueryResponseBodyModuleTravelerListHotelCitys(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ApplyQueryResponseBodyModuleTravelerList(TeaModel):
    def __init__(
        self,
        business_discount: int = None,
        economy_discount: int = None,
        first_discount: int = None,
        flight_cabins: str = None,
        hotel_citys: List[ApplyQueryResponseBodyModuleTravelerListHotelCitys] = None,
        reserve_type: int = None,
        train_seats: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.business_discount = business_discount
        self.economy_discount = economy_discount
        self.first_discount = first_discount
        self.flight_cabins = flight_cabins
        self.hotel_citys = hotel_citys
        self.reserve_type = reserve_type
        self.train_seats = train_seats
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.hotel_citys:
            for k in self.hotel_citys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_discount is not None:
            result['business_discount'] = self.business_discount
        if self.economy_discount is not None:
            result['economy_discount'] = self.economy_discount
        if self.first_discount is not None:
            result['first_discount'] = self.first_discount
        if self.flight_cabins is not None:
            result['flight_cabins'] = self.flight_cabins
        result['hotel_citys'] = []
        if self.hotel_citys is not None:
            for k in self.hotel_citys:
                result['hotel_citys'].append(k.to_map() if k else None)
        if self.reserve_type is not None:
            result['reserve_type'] = self.reserve_type
        if self.train_seats is not None:
            result['train_seats'] = self.train_seats
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
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
        self.hotel_citys = []
        if m.get('hotel_citys') is not None:
            for k in m.get('hotel_citys'):
                temp_model = ApplyQueryResponseBodyModuleTravelerListHotelCitys()
                self.hotel_citys.append(temp_model.from_map(k))
        if m.get('reserve_type') is not None:
            self.reserve_type = m.get('reserve_type')
        if m.get('train_seats') is not None:
            self.train_seats = m.get('train_seats')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class ApplyQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        apply_show_id: str = None,
        approver_list: List[ApplyQueryResponseBodyModuleApproverList] = None,
        budget: int = None,
        budget_merge: int = None,
        corp_id: str = None,
        corp_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        external_traveler_list: List[ApplyQueryResponseBodyModuleExternalTravelerList] = None,
        flight_budget: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        hotel_budget: int = None,
        hotel_share: ApplyQueryResponseBodyModuleHotelShare = None,
        id: int = None,
        itinerary_list: List[ApplyQueryResponseBodyModuleItineraryList] = None,
        itinerary_rule: int = None,
        itinerary_set_list: List[ApplyQueryResponseBodyModuleItinerarySetList] = None,
        limit_traveler: int = None,
        status: int = None,
        status_desc: str = None,
        thirdpart_business_id: str = None,
        thirdpart_id: str = None,
        together_book_rule: int = None,
        train_budget: int = None,
        traveler_list: List[ApplyQueryResponseBodyModuleTravelerList] = None,
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
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.external_traveler_list = external_traveler_list
        self.flight_budget = flight_budget
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.hotel_budget = hotel_budget
        self.hotel_share = hotel_share
        self.id = id
        self.itinerary_list = itinerary_list
        self.itinerary_rule = itinerary_rule
        self.itinerary_set_list = itinerary_set_list
        self.limit_traveler = limit_traveler
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
            for k in self.approver_list:
                if k:
                    k.validate()
        if self.external_traveler_list:
            for k in self.external_traveler_list:
                if k:
                    k.validate()
        if self.hotel_share:
            self.hotel_share.validate()
        if self.itinerary_list:
            for k in self.itinerary_list:
                if k:
                    k.validate()
        if self.itinerary_set_list:
            for k in self.itinerary_set_list:
                if k:
                    k.validate()
        if self.traveler_list:
            for k in self.traveler_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_show_id is not None:
            result['apply_show_id'] = self.apply_show_id
        result['approver_list'] = []
        if self.approver_list is not None:
            for k in self.approver_list:
                result['approver_list'].append(k.to_map() if k else None)
        if self.budget is not None:
            result['budget'] = self.budget
        if self.budget_merge is not None:
            result['budget_merge'] = self.budget_merge
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.corp_name is not None:
            result['corp_name'] = self.corp_name
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.depart_name is not None:
            result['depart_name'] = self.depart_name
        result['external_traveler_list'] = []
        if self.external_traveler_list is not None:
            for k in self.external_traveler_list:
                result['external_traveler_list'].append(k.to_map() if k else None)
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
        result['itinerary_list'] = []
        if self.itinerary_list is not None:
            for k in self.itinerary_list:
                result['itinerary_list'].append(k.to_map() if k else None)
        if self.itinerary_rule is not None:
            result['itinerary_rule'] = self.itinerary_rule
        result['itinerary_set_list'] = []
        if self.itinerary_set_list is not None:
            for k in self.itinerary_set_list:
                result['itinerary_set_list'].append(k.to_map() if k else None)
        if self.limit_traveler is not None:
            result['limit_traveler'] = self.limit_traveler
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
            for k in self.traveler_list:
                result['traveler_list'].append(k.to_map() if k else None)
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
            for k in m.get('approver_list'):
                temp_model = ApplyQueryResponseBodyModuleApproverList()
                self.approver_list.append(temp_model.from_map(k))
        if m.get('budget') is not None:
            self.budget = m.get('budget')
        if m.get('budget_merge') is not None:
            self.budget_merge = m.get('budget_merge')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')
        self.external_traveler_list = []
        if m.get('external_traveler_list') is not None:
            for k in m.get('external_traveler_list'):
                temp_model = ApplyQueryResponseBodyModuleExternalTravelerList()
                self.external_traveler_list.append(temp_model.from_map(k))
        if m.get('flight_budget') is not None:
            self.flight_budget = m.get('flight_budget')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')
        if m.get('hotel_budget') is not None:
            self.hotel_budget = m.get('hotel_budget')
        if m.get('hotel_share') is not None:
            temp_model = ApplyQueryResponseBodyModuleHotelShare()
            self.hotel_share = temp_model.from_map(m['hotel_share'])
        if m.get('id') is not None:
            self.id = m.get('id')
        self.itinerary_list = []
        if m.get('itinerary_list') is not None:
            for k in m.get('itinerary_list'):
                temp_model = ApplyQueryResponseBodyModuleItineraryList()
                self.itinerary_list.append(temp_model.from_map(k))
        if m.get('itinerary_rule') is not None:
            self.itinerary_rule = m.get('itinerary_rule')
        self.itinerary_set_list = []
        if m.get('itinerary_set_list') is not None:
            for k in m.get('itinerary_set_list'):
                temp_model = ApplyQueryResponseBodyModuleItinerarySetList()
                self.itinerary_set_list.append(temp_model.from_map(k))
        if m.get('limit_traveler') is not None:
            self.limit_traveler = m.get('limit_traveler')
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
            for k in m.get('traveler_list'):
                temp_model = ApplyQueryResponseBodyModuleTravelerList()
                self.traveler_list.append(temp_model.from_map(k))
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


class ApplyQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: ApplyQueryResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ApplyQueryResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class ApplyQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CarApplyAddHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class CarApplyAddRequest(TeaModel):
    def __init__(
        self,
        cause: str = None,
        city: str = None,
        date: str = None,
        finished_date: str = None,
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
        user_id: str = None,
    ):
        self.cause = cause
        self.city = city
        self.date = date
        self.finished_date = finished_date
        self.project_code = project_code
        self.project_name = project_name
        self.status = status
        self.third_part_apply_id = third_part_apply_id
        self.third_part_cost_center_id = third_part_cost_center_id
        self.third_part_invoice_id = third_part_invoice_id
        self.times_total = times_total
        self.times_type = times_type
        self.times_used = times_used
        self.title = title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cause is not None:
            result['cause'] = self.cause
        if self.city is not None:
            result['city'] = self.city
        if self.date is not None:
            result['date'] = self.date
        if self.finished_date is not None:
            result['finished_date'] = self.finished_date
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
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cause') is not None:
            self.cause = m.get('cause')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('finished_date') is not None:
            self.finished_date = m.get('finished_date')
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
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CarApplyAddResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: int = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.module is not None:
            result['module'] = self.module
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
            self.module = m.get('module')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class CarApplyAddResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CarApplyAddResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CarApplyAddResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CarApplyModifyHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class CarApplyModifyRequest(TeaModel):
    def __init__(
        self,
        operate_time: str = None,
        remark: str = None,
        status: int = None,
        third_part_apply_id: str = None,
        user_id: str = None,
    ):
        self.operate_time = operate_time
        self.remark = remark
        self.status = status
        self.third_part_apply_id = third_part_apply_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operate_time is not None:
            result['operate_time'] = self.operate_time
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.third_part_apply_id is not None:
            result['third_part_apply_id'] = self.third_part_apply_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operate_time') is not None:
            self.operate_time = m.get('operate_time')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('third_part_apply_id') is not None:
            self.third_part_apply_id = m.get('third_part_apply_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CarApplyModifyResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: bool = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.module is not None:
            result['module'] = self.module
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
            self.module = m.get('module')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class CarApplyModifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CarApplyModifyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CarApplyModifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CarApplyQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class CarApplyQueryRequest(TeaModel):
    def __init__(
        self,
        created_end_at: str = None,
        created_start_at: str = None,
        page_number: int = None,
        page_size: int = None,
        third_part_apply_id: str = None,
        user_id: str = None,
    ):
        self.created_end_at = created_end_at
        self.created_start_at = created_start_at
        self.page_number = page_number
        self.page_size = page_size
        self.third_part_apply_id = third_part_apply_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_end_at is not None:
            result['created_end_at'] = self.created_end_at
        if self.created_start_at is not None:
            result['created_start_at'] = self.created_start_at
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.third_part_apply_id is not None:
            result['third_part_apply_id'] = self.third_part_apply_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_end_at') is not None:
            self.created_end_at = m.get('created_end_at')
        if m.get('created_start_at') is not None:
            self.created_start_at = m.get('created_start_at')
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('third_part_apply_id') is not None:
            self.third_part_apply_id = m.get('third_part_apply_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CarApplyQueryResponseBodyApplyListApproverList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CarApplyQueryResponseBodyApplyListItineraryList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CarApplyQueryResponseBodyApplyList(TeaModel):
    def __init__(
        self,
        approver_list: List[CarApplyQueryResponseBodyApplyListApproverList] = None,
        depart_id: str = None,
        depart_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        itinerary_list: List[CarApplyQueryResponseBodyApplyListItineraryList] = None,
        status: int = None,
        status_desc: str = None,
        thirdpart_id: str = None,
        trip_cause: str = None,
        trip_title: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.approver_list = approver_list
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.itinerary_list = itinerary_list
        self.status = status
        self.status_desc = status_desc
        self.thirdpart_id = thirdpart_id
        self.trip_cause = trip_cause
        self.trip_title = trip_title
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.approver_list:
            for k in self.approver_list:
                if k:
                    k.validate()
        if self.itinerary_list:
            for k in self.itinerary_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['approver_list'] = []
        if self.approver_list is not None:
            for k in self.approver_list:
                result['approver_list'].append(k.to_map() if k else None)
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
            for k in self.itinerary_list:
                result['itinerary_list'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.status_desc is not None:
            result['status_desc'] = self.status_desc
        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id
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
            for k in m.get('approver_list'):
                temp_model = CarApplyQueryResponseBodyApplyListApproverList()
                self.approver_list.append(temp_model.from_map(k))
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
            for k in m.get('itinerary_list'):
                temp_model = CarApplyQueryResponseBodyApplyListItineraryList()
                self.itinerary_list.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('status_desc') is not None:
            self.status_desc = m.get('status_desc')
        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')
        if m.get('trip_cause') is not None:
            self.trip_cause = m.get('trip_cause')
        if m.get('trip_title') is not None:
            self.trip_title = m.get('trip_title')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class CarApplyQueryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        apply_list: List[CarApplyQueryResponseBodyApplyList] = None,
        code: int = None,
        message: str = None,
        success: bool = None,
        total: int = None,
        trace_id: str = None,
    ):
        self.request_id = request_id
        self.apply_list = apply_list
        self.code = code
        self.message = message
        self.success = success
        self.total = total
        self.trace_id = trace_id

    def validate(self):
        if self.apply_list:
            for k in self.apply_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['apply_list'] = []
        if self.apply_list is not None:
            for k in self.apply_list:
                result['apply_list'].append(k.to_map() if k else None)
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.total is not None:
            result['total'] = self.total
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.apply_list = []
        if m.get('apply_list') is not None:
            for k in m.get('apply_list'):
                temp_model = CarApplyQueryResponseBodyApplyList()
                self.apply_list.append(temp_model.from_map(k))
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class CarApplyQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CarApplyQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CarApplyQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CarBillSettlementQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class CarBillSettlementQueryRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        period_end: str = None,
        period_start: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.period_end = period_end
        self.period_start = period_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['page_no'] = self.page_no
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.period_end is not None:
            result['period_end'] = self.period_end
        if self.period_start is not None:
            result['period_start'] = self.period_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_no') is not None:
            self.page_no = m.get('page_no')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('period_end') is not None:
            self.period_end = m.get('period_end')
        if m.get('period_start') is not None:
            self.period_start = m.get('period_start')
        return self


class CarBillSettlementQueryResponseBodyModuleDataList(TeaModel):
    def __init__(
        self,
        alipay_trade_no: str = None,
        apply_id: str = None,
        arr_city: str = None,
        arr_date: str = None,
        arr_location: str = None,
        arr_time: str = None,
        bill_record_time: str = None,
        book_time: str = None,
        booker_id: str = None,
        booker_job_no: str = None,
        booker_name: str = None,
        business_category: str = None,
        capital_direction: str = None,
        car_level: str = None,
        cascade_department: str = None,
        cost_center: str = None,
        cost_center_number: str = None,
        coupon: float = None,
        coupon_price: float = None,
        department: str = None,
        department_id: str = None,
        dept_city: str = None,
        dept_date: str = None,
        dept_location: str = None,
        dept_time: str = None,
        estimate_drive_distance: str = None,
        estimate_price: float = None,
        fee_type: str = None,
        index: str = None,
        invoice_title: str = None,
        memo: str = None,
        order_id: str = None,
        order_price: float = None,
        over_apply_id: str = None,
        person_settle_fee: float = None,
        primary_id: int = None,
        project_code: str = None,
        project_name: str = None,
        provider_name: str = None,
        real_drive_distance: str = None,
        real_from_addr: str = None,
        real_to_addr: str = None,
        remark: str = None,
        service_fee: float = None,
        settlement_fee: float = None,
        settlement_grant_fee: float = None,
        settlement_time: str = None,
        settlement_type: str = None,
        special_order: str = None,
        special_reason: str = None,
        status: int = None,
        sub_order_id: str = None,
        traveler_id: str = None,
        traveler_job_no: str = None,
        traveler_name: str = None,
        user_confirm_desc: str = None,
        voucher_type: int = None,
    ):
        self.alipay_trade_no = alipay_trade_no
        self.apply_id = apply_id
        self.arr_city = arr_city
        self.arr_date = arr_date
        self.arr_location = arr_location
        self.arr_time = arr_time
        self.bill_record_time = bill_record_time
        self.book_time = book_time
        self.booker_id = booker_id
        self.booker_job_no = booker_job_no
        self.booker_name = booker_name
        self.business_category = business_category
        self.capital_direction = capital_direction
        self.car_level = car_level
        self.cascade_department = cascade_department
        self.cost_center = cost_center
        self.cost_center_number = cost_center_number
        self.coupon = coupon
        self.coupon_price = coupon_price
        self.department = department
        self.department_id = department_id
        self.dept_city = dept_city
        self.dept_date = dept_date
        self.dept_location = dept_location
        self.dept_time = dept_time
        self.estimate_drive_distance = estimate_drive_distance
        self.estimate_price = estimate_price
        self.fee_type = fee_type
        self.index = index
        self.invoice_title = invoice_title
        self.memo = memo
        self.order_id = order_id
        self.order_price = order_price
        self.over_apply_id = over_apply_id
        self.person_settle_fee = person_settle_fee
        self.primary_id = primary_id
        self.project_code = project_code
        self.project_name = project_name
        self.provider_name = provider_name
        self.real_drive_distance = real_drive_distance
        self.real_from_addr = real_from_addr
        self.real_to_addr = real_to_addr
        self.remark = remark
        self.service_fee = service_fee
        self.settlement_fee = settlement_fee
        self.settlement_grant_fee = settlement_grant_fee
        self.settlement_time = settlement_time
        self.settlement_type = settlement_type
        self.special_order = special_order
        self.special_reason = special_reason
        self.status = status
        self.sub_order_id = sub_order_id
        self.traveler_id = traveler_id
        self.traveler_job_no = traveler_job_no
        self.traveler_name = traveler_name
        self.user_confirm_desc = user_confirm_desc
        self.voucher_type = voucher_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alipay_trade_no is not None:
            result['alipay_trade_no'] = self.alipay_trade_no
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city
        if self.arr_date is not None:
            result['arr_date'] = self.arr_date
        if self.arr_location is not None:
            result['arr_location'] = self.arr_location
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time
        if self.bill_record_time is not None:
            result['bill_record_time'] = self.bill_record_time
        if self.book_time is not None:
            result['book_time'] = self.book_time
        if self.booker_id is not None:
            result['booker_id'] = self.booker_id
        if self.booker_job_no is not None:
            result['booker_job_no'] = self.booker_job_no
        if self.booker_name is not None:
            result['booker_name'] = self.booker_name
        if self.business_category is not None:
            result['business_category'] = self.business_category
        if self.capital_direction is not None:
            result['capital_direction'] = self.capital_direction
        if self.car_level is not None:
            result['car_level'] = self.car_level
        if self.cascade_department is not None:
            result['cascade_department'] = self.cascade_department
        if self.cost_center is not None:
            result['cost_center'] = self.cost_center
        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number
        if self.coupon is not None:
            result['coupon'] = self.coupon
        if self.coupon_price is not None:
            result['coupon_price'] = self.coupon_price
        if self.department is not None:
            result['department'] = self.department
        if self.department_id is not None:
            result['department_id'] = self.department_id
        if self.dept_city is not None:
            result['dept_city'] = self.dept_city
        if self.dept_date is not None:
            result['dept_date'] = self.dept_date
        if self.dept_location is not None:
            result['dept_location'] = self.dept_location
        if self.dept_time is not None:
            result['dept_time'] = self.dept_time
        if self.estimate_drive_distance is not None:
            result['estimate_drive_distance'] = self.estimate_drive_distance
        if self.estimate_price is not None:
            result['estimate_price'] = self.estimate_price
        if self.fee_type is not None:
            result['fee_type'] = self.fee_type
        if self.index is not None:
            result['index'] = self.index
        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title
        if self.memo is not None:
            result['memo'] = self.memo
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.order_price is not None:
            result['order_price'] = self.order_price
        if self.over_apply_id is not None:
            result['over_apply_id'] = self.over_apply_id
        if self.person_settle_fee is not None:
            result['person_settle_fee'] = self.person_settle_fee
        if self.primary_id is not None:
            result['primary_id'] = self.primary_id
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_name is not None:
            result['project_name'] = self.project_name
        if self.provider_name is not None:
            result['provider_name'] = self.provider_name
        if self.real_drive_distance is not None:
            result['real_drive_distance'] = self.real_drive_distance
        if self.real_from_addr is not None:
            result['real_from_addr'] = self.real_from_addr
        if self.real_to_addr is not None:
            result['real_to_addr'] = self.real_to_addr
        if self.remark is not None:
            result['remark'] = self.remark
        if self.service_fee is not None:
            result['service_fee'] = self.service_fee
        if self.settlement_fee is not None:
            result['settlement_fee'] = self.settlement_fee
        if self.settlement_grant_fee is not None:
            result['settlement_grant_fee'] = self.settlement_grant_fee
        if self.settlement_time is not None:
            result['settlement_time'] = self.settlement_time
        if self.settlement_type is not None:
            result['settlement_type'] = self.settlement_type
        if self.special_order is not None:
            result['special_order'] = self.special_order
        if self.special_reason is not None:
            result['special_reason'] = self.special_reason
        if self.status is not None:
            result['status'] = self.status
        if self.sub_order_id is not None:
            result['sub_order_id'] = self.sub_order_id
        if self.traveler_id is not None:
            result['traveler_id'] = self.traveler_id
        if self.traveler_job_no is not None:
            result['traveler_job_no'] = self.traveler_job_no
        if self.traveler_name is not None:
            result['traveler_name'] = self.traveler_name
        if self.user_confirm_desc is not None:
            result['user_confirm_desc'] = self.user_confirm_desc
        if self.voucher_type is not None:
            result['voucher_type'] = self.voucher_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alipay_trade_no') is not None:
            self.alipay_trade_no = m.get('alipay_trade_no')
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')
        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')
        if m.get('arr_location') is not None:
            self.arr_location = m.get('arr_location')
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')
        if m.get('bill_record_time') is not None:
            self.bill_record_time = m.get('bill_record_time')
        if m.get('book_time') is not None:
            self.book_time = m.get('book_time')
        if m.get('booker_id') is not None:
            self.booker_id = m.get('booker_id')
        if m.get('booker_job_no') is not None:
            self.booker_job_no = m.get('booker_job_no')
        if m.get('booker_name') is not None:
            self.booker_name = m.get('booker_name')
        if m.get('business_category') is not None:
            self.business_category = m.get('business_category')
        if m.get('capital_direction') is not None:
            self.capital_direction = m.get('capital_direction')
        if m.get('car_level') is not None:
            self.car_level = m.get('car_level')
        if m.get('cascade_department') is not None:
            self.cascade_department = m.get('cascade_department')
        if m.get('cost_center') is not None:
            self.cost_center = m.get('cost_center')
        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')
        if m.get('coupon') is not None:
            self.coupon = m.get('coupon')
        if m.get('coupon_price') is not None:
            self.coupon_price = m.get('coupon_price')
        if m.get('department') is not None:
            self.department = m.get('department')
        if m.get('department_id') is not None:
            self.department_id = m.get('department_id')
        if m.get('dept_city') is not None:
            self.dept_city = m.get('dept_city')
        if m.get('dept_date') is not None:
            self.dept_date = m.get('dept_date')
        if m.get('dept_location') is not None:
            self.dept_location = m.get('dept_location')
        if m.get('dept_time') is not None:
            self.dept_time = m.get('dept_time')
        if m.get('estimate_drive_distance') is not None:
            self.estimate_drive_distance = m.get('estimate_drive_distance')
        if m.get('estimate_price') is not None:
            self.estimate_price = m.get('estimate_price')
        if m.get('fee_type') is not None:
            self.fee_type = m.get('fee_type')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('order_price') is not None:
            self.order_price = m.get('order_price')
        if m.get('over_apply_id') is not None:
            self.over_apply_id = m.get('over_apply_id')
        if m.get('person_settle_fee') is not None:
            self.person_settle_fee = m.get('person_settle_fee')
        if m.get('primary_id') is not None:
            self.primary_id = m.get('primary_id')
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_name') is not None:
            self.project_name = m.get('project_name')
        if m.get('provider_name') is not None:
            self.provider_name = m.get('provider_name')
        if m.get('real_drive_distance') is not None:
            self.real_drive_distance = m.get('real_drive_distance')
        if m.get('real_from_addr') is not None:
            self.real_from_addr = m.get('real_from_addr')
        if m.get('real_to_addr') is not None:
            self.real_to_addr = m.get('real_to_addr')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')
        if m.get('settlement_fee') is not None:
            self.settlement_fee = m.get('settlement_fee')
        if m.get('settlement_grant_fee') is not None:
            self.settlement_grant_fee = m.get('settlement_grant_fee')
        if m.get('settlement_time') is not None:
            self.settlement_time = m.get('settlement_time')
        if m.get('settlement_type') is not None:
            self.settlement_type = m.get('settlement_type')
        if m.get('special_order') is not None:
            self.special_order = m.get('special_order')
        if m.get('special_reason') is not None:
            self.special_reason = m.get('special_reason')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('sub_order_id') is not None:
            self.sub_order_id = m.get('sub_order_id')
        if m.get('traveler_id') is not None:
            self.traveler_id = m.get('traveler_id')
        if m.get('traveler_job_no') is not None:
            self.traveler_job_no = m.get('traveler_job_no')
        if m.get('traveler_name') is not None:
            self.traveler_name = m.get('traveler_name')
        if m.get('user_confirm_desc') is not None:
            self.user_confirm_desc = m.get('user_confirm_desc')
        if m.get('voucher_type') is not None:
            self.voucher_type = m.get('voucher_type')
        return self


class CarBillSettlementQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        data_list: List[CarBillSettlementQueryResponseBodyModuleDataList] = None,
        period_end: str = None,
        period_start: str = None,
        total_num: int = None,
    ):
        self.category = category
        self.corp_id = corp_id
        self.data_list = data_list
        self.period_end = period_end
        self.period_start = period_start
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        result['data_list'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['data_list'].append(k.to_map() if k else None)
        if self.period_end is not None:
            result['period_end'] = self.period_end
        if self.period_start is not None:
            result['period_start'] = self.period_start
        if self.total_num is not None:
            result['total_num'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        self.data_list = []
        if m.get('data_list') is not None:
            for k in m.get('data_list'):
                temp_model = CarBillSettlementQueryResponseBodyModuleDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('period_end') is not None:
            self.period_end = m.get('period_end')
        if m.get('period_start') is not None:
            self.period_start = m.get('period_start')
        if m.get('total_num') is not None:
            self.total_num = m.get('total_num')
        return self


class CarBillSettlementQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: CarBillSettlementQueryResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CarBillSettlementQueryResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class CarBillSettlementQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CarBillSettlementQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CarBillSettlementQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CarOrderListQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class CarOrderListQueryRequest(TeaModel):
    def __init__(
        self,
        all_apply: bool = None,
        apply_id: int = None,
        depart_id: str = None,
        end_time: str = None,
        page: int = None,
        page_size: int = None,
        start_time: str = None,
        thirdpart_apply_id: str = None,
        update_end_time: str = None,
        update_start_time: str = None,
        user_id: str = None,
    ):
        self.all_apply = all_apply
        self.apply_id = apply_id
        self.depart_id = depart_id
        self.end_time = end_time
        self.page = page
        self.page_size = page_size
        self.start_time = start_time
        self.thirdpart_apply_id = thirdpart_apply_id
        self.update_end_time = update_end_time
        self.update_start_time = update_start_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_apply is not None:
            result['all_apply'] = self.all_apply
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.update_end_time is not None:
            result['update_end_time'] = self.update_end_time
        if self.update_start_time is not None:
            result['update_start_time'] = self.update_start_time
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all_apply') is not None:
            self.all_apply = m.get('all_apply')
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('update_end_time') is not None:
            self.update_end_time = m.get('update_end_time')
        if m.get('update_start_time') is not None:
            self.update_start_time = m.get('update_start_time')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CarOrderListQueryResponseBodyModulePriceInfoList(TeaModel):
    def __init__(
        self,
        category_code: int = None,
        category_type: int = None,
        gmt_create: str = None,
        passenger_name: str = None,
        pay_type: int = None,
        person_price: float = None,
        price: float = None,
        trade_id: str = None,
        type: int = None,
    ):
        self.category_code = category_code
        self.category_type = category_type
        self.gmt_create = gmt_create
        self.passenger_name = passenger_name
        self.pay_type = pay_type
        self.person_price = person_price
        self.price = price
        self.trade_id = trade_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_code is not None:
            result['category_code'] = self.category_code
        if self.category_type is not None:
            result['category_type'] = self.category_type
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name
        if self.pay_type is not None:
            result['pay_type'] = self.pay_type
        if self.person_price is not None:
            result['person_price'] = self.person_price
        if self.price is not None:
            result['price'] = self.price
        if self.trade_id is not None:
            result['trade_id'] = self.trade_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category_code') is not None:
            self.category_code = m.get('category_code')
        if m.get('category_type') is not None:
            self.category_type = m.get('category_type')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')
        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')
        if m.get('person_price') is not None:
            self.person_price = m.get('person_price')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('trade_id') is not None:
            self.trade_id = m.get('trade_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CarOrderListQueryResponseBodyModuleUserAffiliateList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CarOrderListQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        apply_show_id: str = None,
        btrip_title: str = None,
        business_category: str = None,
        cancel_time: str = None,
        car_info: str = None,
        car_level: int = None,
        corp_id: str = None,
        corp_name: str = None,
        cost_center_id: int = None,
        cost_center_name: str = None,
        cost_center_number: str = None,
        dept_id: int = None,
        dept_name: str = None,
        driver_confirm_time: str = None,
        estimate_price: float = None,
        from_address: str = None,
        from_city_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        invoice_id: int = None,
        invoice_title: str = None,
        is_special: bool = None,
        memo: str = None,
        order_status: int = None,
        passenger_name: str = None,
        pay_time: str = None,
        price_info_list: List[CarOrderListQueryResponseBodyModulePriceInfoList] = None,
        project_code: str = None,
        project_id: int = None,
        project_title: str = None,
        provider: int = None,
        publish_time: str = None,
        real_from_address: str = None,
        real_from_city_name: str = None,
        real_to_address: str = None,
        real_to_city_name: str = None,
        service_type: int = None,
        special_types: List[str] = None,
        taken_time: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_itinerary_id: str = None,
        to_address: str = None,
        to_city_name: str = None,
        travel_distance: float = None,
        user_affiliate_list: List[CarOrderListQueryResponseBodyModuleUserAffiliateList] = None,
        user_confirm: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.apply_id = apply_id
        self.apply_show_id = apply_show_id
        self.btrip_title = btrip_title
        self.business_category = business_category
        self.cancel_time = cancel_time
        self.car_info = car_info
        self.car_level = car_level
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.cost_center_number = cost_center_number
        self.dept_id = dept_id
        self.dept_name = dept_name
        self.driver_confirm_time = driver_confirm_time
        self.estimate_price = estimate_price
        self.from_address = from_address
        self.from_city_name = from_city_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.invoice_id = invoice_id
        self.invoice_title = invoice_title
        self.is_special = is_special
        self.memo = memo
        self.order_status = order_status
        self.passenger_name = passenger_name
        self.pay_time = pay_time
        self.price_info_list = price_info_list
        self.project_code = project_code
        self.project_id = project_id
        self.project_title = project_title
        self.provider = provider
        self.publish_time = publish_time
        self.real_from_address = real_from_address
        self.real_from_city_name = real_from_city_name
        self.real_to_address = real_to_address
        self.real_to_city_name = real_to_city_name
        self.service_type = service_type
        self.special_types = special_types
        self.taken_time = taken_time
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_itinerary_id = thirdpart_itinerary_id
        self.to_address = to_address
        self.to_city_name = to_city_name
        self.travel_distance = travel_distance
        self.user_affiliate_list = user_affiliate_list
        self.user_confirm = user_confirm
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.price_info_list:
            for k in self.price_info_list:
                if k:
                    k.validate()
        if self.user_affiliate_list:
            for k in self.user_affiliate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.apply_show_id is not None:
            result['apply_show_id'] = self.apply_show_id
        if self.btrip_title is not None:
            result['btrip_title'] = self.btrip_title
        if self.business_category is not None:
            result['business_category'] = self.business_category
        if self.cancel_time is not None:
            result['cancel_time'] = self.cancel_time
        if self.car_info is not None:
            result['car_info'] = self.car_info
        if self.car_level is not None:
            result['car_level'] = self.car_level
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.corp_name is not None:
            result['corp_name'] = self.corp_name
        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id
        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name
        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number
        if self.dept_id is not None:
            result['dept_id'] = self.dept_id
        if self.dept_name is not None:
            result['dept_name'] = self.dept_name
        if self.driver_confirm_time is not None:
            result['driver_confirm_time'] = self.driver_confirm_time
        if self.estimate_price is not None:
            result['estimate_price'] = self.estimate_price
        if self.from_address is not None:
            result['from_address'] = self.from_address
        if self.from_city_name is not None:
            result['from_city_name'] = self.from_city_name
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.invoice_id is not None:
            result['invoice_id'] = self.invoice_id
        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title
        if self.is_special is not None:
            result['is_special'] = self.is_special
        if self.memo is not None:
            result['memo'] = self.memo
        if self.order_status is not None:
            result['order_status'] = self.order_status
        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name
        if self.pay_time is not None:
            result['pay_time'] = self.pay_time
        result['price_info_list'] = []
        if self.price_info_list is not None:
            for k in self.price_info_list:
                result['price_info_list'].append(k.to_map() if k else None)
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.project_title is not None:
            result['project_title'] = self.project_title
        if self.provider is not None:
            result['provider'] = self.provider
        if self.publish_time is not None:
            result['publish_time'] = self.publish_time
        if self.real_from_address is not None:
            result['real_from_address'] = self.real_from_address
        if self.real_from_city_name is not None:
            result['real_from_city_name'] = self.real_from_city_name
        if self.real_to_address is not None:
            result['real_to_address'] = self.real_to_address
        if self.real_to_city_name is not None:
            result['real_to_city_name'] = self.real_to_city_name
        if self.service_type is not None:
            result['service_type'] = self.service_type
        if self.special_types is not None:
            result['special_types'] = self.special_types
        if self.taken_time is not None:
            result['taken_time'] = self.taken_time
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id
        if self.to_address is not None:
            result['to_address'] = self.to_address
        if self.to_city_name is not None:
            result['to_city_name'] = self.to_city_name
        if self.travel_distance is not None:
            result['travel_distance'] = self.travel_distance
        result['user_affiliate_list'] = []
        if self.user_affiliate_list is not None:
            for k in self.user_affiliate_list:
                result['user_affiliate_list'].append(k.to_map() if k else None)
        if self.user_confirm is not None:
            result['user_confirm'] = self.user_confirm
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('apply_show_id') is not None:
            self.apply_show_id = m.get('apply_show_id')
        if m.get('btrip_title') is not None:
            self.btrip_title = m.get('btrip_title')
        if m.get('business_category') is not None:
            self.business_category = m.get('business_category')
        if m.get('cancel_time') is not None:
            self.cancel_time = m.get('cancel_time')
        if m.get('car_info') is not None:
            self.car_info = m.get('car_info')
        if m.get('car_level') is not None:
            self.car_level = m.get('car_level')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')
        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')
        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')
        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')
        if m.get('dept_id') is not None:
            self.dept_id = m.get('dept_id')
        if m.get('dept_name') is not None:
            self.dept_name = m.get('dept_name')
        if m.get('driver_confirm_time') is not None:
            self.driver_confirm_time = m.get('driver_confirm_time')
        if m.get('estimate_price') is not None:
            self.estimate_price = m.get('estimate_price')
        if m.get('from_address') is not None:
            self.from_address = m.get('from_address')
        if m.get('from_city_name') is not None:
            self.from_city_name = m.get('from_city_name')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('invoice_id') is not None:
            self.invoice_id = m.get('invoice_id')
        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')
        if m.get('is_special') is not None:
            self.is_special = m.get('is_special')
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')
        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')
        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')
        self.price_info_list = []
        if m.get('price_info_list') is not None:
            for k in m.get('price_info_list'):
                temp_model = CarOrderListQueryResponseBodyModulePriceInfoList()
                self.price_info_list.append(temp_model.from_map(k))
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('publish_time') is not None:
            self.publish_time = m.get('publish_time')
        if m.get('real_from_address') is not None:
            self.real_from_address = m.get('real_from_address')
        if m.get('real_from_city_name') is not None:
            self.real_from_city_name = m.get('real_from_city_name')
        if m.get('real_to_address') is not None:
            self.real_to_address = m.get('real_to_address')
        if m.get('real_to_city_name') is not None:
            self.real_to_city_name = m.get('real_to_city_name')
        if m.get('service_type') is not None:
            self.service_type = m.get('service_type')
        if m.get('special_types') is not None:
            self.special_types = m.get('special_types')
        if m.get('taken_time') is not None:
            self.taken_time = m.get('taken_time')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')
        if m.get('to_address') is not None:
            self.to_address = m.get('to_address')
        if m.get('to_city_name') is not None:
            self.to_city_name = m.get('to_city_name')
        if m.get('travel_distance') is not None:
            self.travel_distance = m.get('travel_distance')
        self.user_affiliate_list = []
        if m.get('user_affiliate_list') is not None:
            for k in m.get('user_affiliate_list'):
                temp_model = CarOrderListQueryResponseBodyModuleUserAffiliateList()
                self.user_affiliate_list.append(temp_model.from_map(k))
        if m.get('user_confirm') is not None:
            self.user_confirm = m.get('user_confirm')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class CarOrderListQueryResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        total_number: int = None,
    ):
        self.page = page
        self.page_size = page_size
        self.total_number = total_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_number is not None:
            result['total_number'] = self.total_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_number') is not None:
            self.total_number = m.get('total_number')
        return self


class CarOrderListQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: List[CarOrderListQueryResponseBodyModule] = None,
        page_info: CarOrderListQueryResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.page_info = page_info
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            for k in self.module:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        result['module'] = []
        if self.module is not None:
            for k in self.module:
                result['module'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
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
        self.module = []
        if m.get('module') is not None:
            for k in m.get('module'):
                temp_model = CarOrderListQueryResponseBodyModule()
                self.module.append(temp_model.from_map(k))
        if m.get('page_info') is not None:
            temp_model = CarOrderListQueryResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['page_info'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class CarOrderListQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CarOrderListQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CarOrderListQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CitySearchHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class CitySearchRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
    ):
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        return self


class CitySearchResponseBodyModuleCities(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        region: int = None,
    ):
        self.code = code
        self.name = name
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.name is not None:
            result['name'] = self.name
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self


class CitySearchResponseBodyModule(TeaModel):
    def __init__(
        self,
        cities: List[CitySearchResponseBodyModuleCities] = None,
    ):
        self.cities = cities

    def validate(self):
        if self.cities:
            for k in self.cities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['cities'] = []
        if self.cities is not None:
            for k in self.cities:
                result['cities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cities = []
        if m.get('cities') is not None:
            for k in m.get('cities'):
                temp_model = CitySearchResponseBodyModuleCities()
                self.cities.append(temp_model.from_map(k))
        return self


class CitySearchResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: CitySearchResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CitySearchResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class CitySearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CitySearchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CitySearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CommonApplyQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class CommonApplyQueryRequest(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        biz_category: int = None,
        user_id: str = None,
    ):
        self.apply_id = apply_id
        self.biz_category = biz_category
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.biz_category is not None:
            result['biz_category'] = self.biz_category
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('biz_category') is not None:
            self.biz_category = m.get('biz_category')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CommonApplyQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        biz_category: int = None,
        cause: str = None,
        corp_id: str = None,
        extend_value: str = None,
        gmt_create: str = None,
        status: int = None,
        thirdpart_corp_id: str = None,
        thirdpart_id: str = None,
        trip_cause: str = None,
        user_id: str = None,
    ):
        self.apply_id = apply_id
        self.biz_category = biz_category
        self.cause = cause
        self.corp_id = corp_id
        self.extend_value = extend_value
        self.gmt_create = gmt_create
        self.status = status
        self.thirdpart_corp_id = thirdpart_corp_id
        self.thirdpart_id = thirdpart_id
        self.trip_cause = trip_cause
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.biz_category is not None:
            result['biz_category'] = self.biz_category
        if self.cause is not None:
            result['cause'] = self.cause
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.extend_value is not None:
            result['extend_value'] = self.extend_value
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.status is not None:
            result['status'] = self.status
        if self.thirdpart_corp_id is not None:
            result['thirdpart_corp_id'] = self.thirdpart_corp_id
        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id
        if self.trip_cause is not None:
            result['trip_cause'] = self.trip_cause
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('biz_category') is not None:
            self.biz_category = m.get('biz_category')
        if m.get('cause') is not None:
            self.cause = m.get('cause')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('extend_value') is not None:
            self.extend_value = m.get('extend_value')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thirdpart_corp_id') is not None:
            self.thirdpart_corp_id = m.get('thirdpart_corp_id')
        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')
        if m.get('trip_cause') is not None:
            self.trip_cause = m.get('trip_cause')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CommonApplyQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: CommonApplyQueryResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CommonApplyQueryResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class CommonApplyQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CommonApplyQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CommonApplyQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CommonApplySyncHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class CommonApplySyncRequest(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        biz_category: int = None,
        remark: str = None,
        status: int = None,
        thirdparty_flow_id: str = None,
        user_id: str = None,
    ):
        self.apply_id = apply_id
        self.biz_category = biz_category
        self.remark = remark
        self.status = status
        self.thirdparty_flow_id = thirdparty_flow_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.biz_category is not None:
            result['biz_category'] = self.biz_category
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.thirdparty_flow_id is not None:
            result['thirdparty_flow_id'] = self.thirdparty_flow_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('biz_category') is not None:
            self.biz_category = m.get('biz_category')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thirdparty_flow_id') is not None:
            self.thirdparty_flow_id = m.get('thirdparty_flow_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CommonApplySyncResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: bool = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.module is not None:
            result['module'] = self.module
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
            self.module = m.get('module')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class CommonApplySyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CommonApplySyncResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CommonApplySyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CorpTokenHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_access_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_access_token = x_acs_btrip_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_access_token is not None:
            result['x-acs-btrip-access-token'] = self.x_acs_btrip_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-access-token') is not None:
            self.x_acs_btrip_access_token = m.get('x-acs-btrip-access-token')
        return self


class CorpTokenRequest(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        type: int = None,
    ):
        self.corp_id = corp_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CorpTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        expire: int = None,
        token: str = None,
    ):
        self.expire = expire
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire is not None:
            result['expire'] = self.expire
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expire') is not None:
            self.expire = m.get('expire')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class CorpTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CorpTokenResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        trace_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CorpTokenResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class CorpTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CorpTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CorpTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CostCenterDeleteHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class CostCenterDeleteRequest(TeaModel):
    def __init__(
        self,
        thirdpart_id: str = None,
    ):
        self.thirdpart_id = thirdpart_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')
        return self


class CostCenterDeleteResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
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
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class CostCenterDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CostCenterDeleteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CostCenterDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CostCenterModifyHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class CostCenterModifyRequest(TeaModel):
    def __init__(
        self,
        alipay_no: str = None,
        number: str = None,
        scope: int = None,
        thirdpart_id: str = None,
        title: str = None,
    ):
        self.alipay_no = alipay_no
        self.number = number
        self.scope = scope
        self.thirdpart_id = thirdpart_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alipay_no is not None:
            result['alipay_no'] = self.alipay_no
        if self.number is not None:
            result['number'] = self.number
        if self.scope is not None:
            result['scope'] = self.scope
        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alipay_no') is not None:
            self.alipay_no = m.get('alipay_no')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class CostCenterModifyResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
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
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class CostCenterModifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CostCenterModifyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CostCenterModifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CostCenterQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class CostCenterQueryRequest(TeaModel):
    def __init__(
        self,
        need_org_entity: bool = None,
        thirdpart_id: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.need_org_entity = need_org_entity
        self.thirdpart_id = thirdpart_id
        self.title = title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_org_entity is not None:
            result['need_org_entity'] = self.need_org_entity
        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id
        if self.title is not None:
            result['title'] = self.title
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('need_org_entity') is not None:
            self.need_org_entity = m.get('need_org_entity')
        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CostCenterQueryResponseBodyModuleEntityDOS(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        entity_id: str = None,
        entity_type: str = None,
        name: str = None,
        user_num: int = None,
    ):
        self.corp_id = corp_id
        self.entity_id = entity_id
        self.entity_type = entity_type
        self.name = name
        self.user_num = user_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.entity_id is not None:
            result['entity_id'] = self.entity_id
        if self.entity_type is not None:
            result['entity_type'] = self.entity_type
        if self.name is not None:
            result['name'] = self.name
        if self.user_num is not None:
            result['user_num'] = self.user_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('entity_id') is not None:
            self.entity_id = m.get('entity_id')
        if m.get('entity_type') is not None:
            self.entity_type = m.get('entity_type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('user_num') is not None:
            self.user_num = m.get('user_num')
        return self


class CostCenterQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        alipay_no: str = None,
        corp_id: str = None,
        entity_dos: List[CostCenterQueryResponseBodyModuleEntityDOS] = None,
        id: int = None,
        number: str = None,
        rule_code: int = None,
        scope: int = None,
        thirdpart_id: str = None,
        title: str = None,
    ):
        self.alipay_no = alipay_no
        self.corp_id = corp_id
        self.entity_dos = entity_dos
        self.id = id
        self.number = number
        self.rule_code = rule_code
        self.scope = scope
        self.thirdpart_id = thirdpart_id
        self.title = title

    def validate(self):
        if self.entity_dos:
            for k in self.entity_dos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alipay_no is not None:
            result['alipay_no'] = self.alipay_no
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        result['entity_d_o_s'] = []
        if self.entity_dos is not None:
            for k in self.entity_dos:
                result['entity_d_o_s'].append(k.to_map() if k else None)
        if self.id is not None:
            result['id'] = self.id
        if self.number is not None:
            result['number'] = self.number
        if self.rule_code is not None:
            result['rule_code'] = self.rule_code
        if self.scope is not None:
            result['scope'] = self.scope
        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alipay_no') is not None:
            self.alipay_no = m.get('alipay_no')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        self.entity_dos = []
        if m.get('entity_d_o_s') is not None:
            for k in m.get('entity_d_o_s'):
                temp_model = CostCenterQueryResponseBodyModuleEntityDOS()
                self.entity_dos.append(temp_model.from_map(k))
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('rule_code') is not None:
            self.rule_code = m.get('rule_code')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class CostCenterQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: List[CostCenterQueryResponseBodyModule] = None,
        more_page: bool = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.more_page = more_page
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            for k in self.module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        result['module'] = []
        if self.module is not None:
            for k in self.module:
                result['module'].append(k.to_map() if k else None)
        if self.more_page is not None:
            result['more_page'] = self.more_page
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
        self.module = []
        if m.get('module') is not None:
            for k in m.get('module'):
                temp_model = CostCenterQueryResponseBodyModule()
                self.module.append(temp_model.from_map(k))
        if m.get('more_page') is not None:
            self.more_page = m.get('more_page')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class CostCenterQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CostCenterQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CostCenterQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CostCenterSaveHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class CostCenterSaveRequest(TeaModel):
    def __init__(
        self,
        alipay_no: str = None,
        number: str = None,
        scope: int = None,
        thirdpart_id: str = None,
        title: str = None,
    ):
        self.alipay_no = alipay_no
        self.number = number
        self.scope = scope
        self.thirdpart_id = thirdpart_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alipay_no is not None:
            result['alipay_no'] = self.alipay_no
        if self.number is not None:
            result['number'] = self.number
        if self.scope is not None:
            result['scope'] = self.scope
        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alipay_no') is not None:
            self.alipay_no = m.get('alipay_no')
        if m.get('number') is not None:
            self.number = m.get('number')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class CostCenterSaveResponseBodyModule(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class CostCenterSaveResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: CostCenterSaveResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CostCenterSaveResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class CostCenterSaveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CostCenterSaveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CostCenterSaveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DepartmentSaveHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class DepartmentSaveRequestDepartList(TeaModel):
    def __init__(
        self,
        depart_id: int = None,
        depart_name: str = None,
        depart_pid: int = None,
        manager_ids: str = None,
        status: int = None,
        third_depart_id: str = None,
        third_depart_pid: str = None,
    ):
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.depart_pid = depart_pid
        self.manager_ids = manager_ids
        self.status = status
        self.third_depart_id = third_depart_id
        self.third_depart_pid = third_depart_pid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.depart_name is not None:
            result['depart_name'] = self.depart_name
        if self.depart_pid is not None:
            result['depart_pid'] = self.depart_pid
        if self.manager_ids is not None:
            result['manager_ids'] = self.manager_ids
        if self.status is not None:
            result['status'] = self.status
        if self.third_depart_id is not None:
            result['third_depart_id'] = self.third_depart_id
        if self.third_depart_pid is not None:
            result['third_depart_pid'] = self.third_depart_pid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')
        if m.get('depart_pid') is not None:
            self.depart_pid = m.get('depart_pid')
        if m.get('manager_ids') is not None:
            self.manager_ids = m.get('manager_ids')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('third_depart_id') is not None:
            self.third_depart_id = m.get('third_depart_id')
        if m.get('third_depart_pid') is not None:
            self.third_depart_pid = m.get('third_depart_pid')
        return self


class DepartmentSaveRequest(TeaModel):
    def __init__(
        self,
        depart_list: List[DepartmentSaveRequestDepartList] = None,
    ):
        self.depart_list = depart_list

    def validate(self):
        if self.depart_list:
            for k in self.depart_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['depart_list'] = []
        if self.depart_list is not None:
            for k in self.depart_list:
                result['depart_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.depart_list = []
        if m.get('depart_list') is not None:
            for k in m.get('depart_list'):
                temp_model = DepartmentSaveRequestDepartList()
                self.depart_list.append(temp_model.from_map(k))
        return self


class DepartmentSaveShrinkRequest(TeaModel):
    def __init__(
        self,
        depart_list_shrink: str = None,
    ):
        self.depart_list_shrink = depart_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.depart_list_shrink is not None:
            result['depart_list'] = self.depart_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('depart_list') is not None:
            self.depart_list_shrink = m.get('depart_list')
        return self


class DepartmentSaveResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.module is not None:
            result['module'] = self.module
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
            self.module = m.get('module')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class DepartmentSaveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DepartmentSaveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DepartmentSaveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EntityAddHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class EntityAddRequestEntityDOList(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
    ):
        self.entity_id = entity_id
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['entity_id'] = self.entity_id
        if self.entity_type is not None:
            result['entity_type'] = self.entity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entity_id') is not None:
            self.entity_id = m.get('entity_id')
        if m.get('entity_type') is not None:
            self.entity_type = m.get('entity_type')
        return self


class EntityAddRequest(TeaModel):
    def __init__(
        self,
        entity_dolist: List[EntityAddRequestEntityDOList] = None,
        thirdpart_id: str = None,
    ):
        self.entity_dolist = entity_dolist
        self.thirdpart_id = thirdpart_id

    def validate(self):
        if self.entity_dolist:
            for k in self.entity_dolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['entity_d_o_list'] = []
        if self.entity_dolist is not None:
            for k in self.entity_dolist:
                result['entity_d_o_list'].append(k.to_map() if k else None)
        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entity_dolist = []
        if m.get('entity_d_o_list') is not None:
            for k in m.get('entity_d_o_list'):
                temp_model = EntityAddRequestEntityDOList()
                self.entity_dolist.append(temp_model.from_map(k))
        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')
        return self


class EntityAddShrinkRequest(TeaModel):
    def __init__(
        self,
        entity_dolist_shrink: str = None,
        thirdpart_id: str = None,
    ):
        self.entity_dolist_shrink = entity_dolist_shrink
        self.thirdpart_id = thirdpart_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_dolist_shrink is not None:
            result['entity_d_o_list'] = self.entity_dolist_shrink
        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entity_d_o_list') is not None:
            self.entity_dolist_shrink = m.get('entity_d_o_list')
        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')
        return self


class EntityAddResponseBodyModule(TeaModel):
    def __init__(
        self,
        add_num: int = None,
        selected_user_num: int = None,
    ):
        self.add_num = add_num
        self.selected_user_num = selected_user_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_num is not None:
            result['add_num'] = self.add_num
        if self.selected_user_num is not None:
            result['selected_user_num'] = self.selected_user_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('add_num') is not None:
            self.add_num = m.get('add_num')
        if m.get('selected_user_num') is not None:
            self.selected_user_num = m.get('selected_user_num')
        return self


class EntityAddResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: EntityAddResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = EntityAddResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class EntityAddResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EntityAddResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EntityAddResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EntityDeleteHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class EntityDeleteRequestEntityDOList(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
    ):
        self.entity_id = entity_id
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['entity_id'] = self.entity_id
        if self.entity_type is not None:
            result['entity_type'] = self.entity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entity_id') is not None:
            self.entity_id = m.get('entity_id')
        if m.get('entity_type') is not None:
            self.entity_type = m.get('entity_type')
        return self


class EntityDeleteRequest(TeaModel):
    def __init__(
        self,
        del_all: bool = None,
        entity_dolist: List[EntityDeleteRequestEntityDOList] = None,
        thirdpart_id: str = None,
    ):
        self.del_all = del_all
        self.entity_dolist = entity_dolist
        self.thirdpart_id = thirdpart_id

    def validate(self):
        if self.entity_dolist:
            for k in self.entity_dolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.del_all is not None:
            result['del_all'] = self.del_all
        result['entity_d_o_list'] = []
        if self.entity_dolist is not None:
            for k in self.entity_dolist:
                result['entity_d_o_list'].append(k.to_map() if k else None)
        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('del_all') is not None:
            self.del_all = m.get('del_all')
        self.entity_dolist = []
        if m.get('entity_d_o_list') is not None:
            for k in m.get('entity_d_o_list'):
                temp_model = EntityDeleteRequestEntityDOList()
                self.entity_dolist.append(temp_model.from_map(k))
        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')
        return self


class EntityDeleteShrinkRequest(TeaModel):
    def __init__(
        self,
        del_all: bool = None,
        entity_dolist_shrink: str = None,
        thirdpart_id: str = None,
    ):
        self.del_all = del_all
        self.entity_dolist_shrink = entity_dolist_shrink
        self.thirdpart_id = thirdpart_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.del_all is not None:
            result['del_all'] = self.del_all
        if self.entity_dolist_shrink is not None:
            result['entity_d_o_list'] = self.entity_dolist_shrink
        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('del_all') is not None:
            self.del_all = m.get('del_all')
        if m.get('entity_d_o_list') is not None:
            self.entity_dolist_shrink = m.get('entity_d_o_list')
        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')
        return self


class EntityDeleteResponseBodyModule(TeaModel):
    def __init__(
        self,
        remove_num: int = None,
        selected_user_num: int = None,
    ):
        self.remove_num = remove_num
        self.selected_user_num = selected_user_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remove_num is not None:
            result['remove_num'] = self.remove_num
        if self.selected_user_num is not None:
            result['selected_user_num'] = self.selected_user_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('remove_num') is not None:
            self.remove_num = m.get('remove_num')
        if m.get('selected_user_num') is not None:
            self.selected_user_num = m.get('selected_user_num')
        return self


class EntityDeleteResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: EntityDeleteResponseBodyModule = None,
        more_page: bool = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.more_page = more_page
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.module is not None:
            result['module'] = self.module.to_map()
        if self.more_page is not None:
            result['more_page'] = self.more_page
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
            temp_model = EntityDeleteResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('more_page') is not None:
            self.more_page = m.get('more_page')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class EntityDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EntityDeleteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EntityDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EntitySetHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class EntitySetRequestEntityDOList(TeaModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
    ):
        self.entity_id = entity_id
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_id is not None:
            result['entity_id'] = self.entity_id
        if self.entity_type is not None:
            result['entity_type'] = self.entity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entity_id') is not None:
            self.entity_id = m.get('entity_id')
        if m.get('entity_type') is not None:
            self.entity_type = m.get('entity_type')
        return self


class EntitySetRequest(TeaModel):
    def __init__(
        self,
        entity_dolist: List[EntitySetRequestEntityDOList] = None,
        thirdpart_id: str = None,
    ):
        self.entity_dolist = entity_dolist
        self.thirdpart_id = thirdpart_id

    def validate(self):
        if self.entity_dolist:
            for k in self.entity_dolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['entity_d_o_list'] = []
        if self.entity_dolist is not None:
            for k in self.entity_dolist:
                result['entity_d_o_list'].append(k.to_map() if k else None)
        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entity_dolist = []
        if m.get('entity_d_o_list') is not None:
            for k in m.get('entity_d_o_list'):
                temp_model = EntitySetRequestEntityDOList()
                self.entity_dolist.append(temp_model.from_map(k))
        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')
        return self


class EntitySetShrinkRequest(TeaModel):
    def __init__(
        self,
        entity_dolist_shrink: str = None,
        thirdpart_id: str = None,
    ):
        self.entity_dolist_shrink = entity_dolist_shrink
        self.thirdpart_id = thirdpart_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_dolist_shrink is not None:
            result['entity_d_o_list'] = self.entity_dolist_shrink
        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entity_d_o_list') is not None:
            self.entity_dolist_shrink = m.get('entity_d_o_list')
        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')
        return self


class EntitySetResponseBodyModule(TeaModel):
    def __init__(
        self,
        add_num: int = None,
        remove_num: int = None,
        selected_user_num: int = None,
    ):
        self.add_num = add_num
        self.remove_num = remove_num
        self.selected_user_num = selected_user_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_num is not None:
            result['add_num'] = self.add_num
        if self.remove_num is not None:
            result['remove_num'] = self.remove_num
        if self.selected_user_num is not None:
            result['selected_user_num'] = self.selected_user_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('add_num') is not None:
            self.add_num = m.get('add_num')
        if m.get('remove_num') is not None:
            self.remove_num = m.get('remove_num')
        if m.get('selected_user_num') is not None:
            self.selected_user_num = m.get('selected_user_num')
        return self


class EntitySetResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: EntitySetResponseBodyModule = None,
        more_page: bool = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.more_page = more_page
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.module is not None:
            result['module'] = self.module.to_map()
        if self.more_page is not None:
            result['more_page'] = self.more_page
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
            temp_model = EntitySetResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('more_page') is not None:
            self.more_page = m.get('more_page')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class EntitySetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EntitySetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EntitySetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExceedApplySyncHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class ExceedApplySyncRequest(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        biz_category: int = None,
        remark: str = None,
        status: int = None,
        thirdparty_flow_id: str = None,
        user_id: str = None,
    ):
        self.apply_id = apply_id
        self.biz_category = biz_category
        self.remark = remark
        self.status = status
        self.thirdparty_flow_id = thirdparty_flow_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.biz_category is not None:
            result['biz_category'] = self.biz_category
        if self.remark is not None:
            result['remark'] = self.remark
        if self.status is not None:
            result['status'] = self.status
        if self.thirdparty_flow_id is not None:
            result['thirdparty_flow_id'] = self.thirdparty_flow_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('biz_category') is not None:
            self.biz_category = m.get('biz_category')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thirdparty_flow_id') is not None:
            self.thirdparty_flow_id = m.get('thirdparty_flow_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class ExceedApplySyncResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: int = None,
        message: str = None,
        module: bool = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.module = module
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.module is not None:
            result['module'] = self.module
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('module') is not None:
            self.module = m.get('module')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class ExceedApplySyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExceedApplySyncResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExceedApplySyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlightBillSettlementQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class FlightBillSettlementQueryRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        period_end: str = None,
        period_start: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.period_end = period_end
        self.period_start = period_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['page_no'] = self.page_no
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.period_end is not None:
            result['period_end'] = self.period_end
        if self.period_start is not None:
            result['period_start'] = self.period_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_no') is not None:
            self.page_no = m.get('page_no')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('period_end') is not None:
            self.period_end = m.get('period_end')
        if m.get('period_start') is not None:
            self.period_start = m.get('period_start')
        return self


class FlightBillSettlementQueryResponseBodyModuleDataList(TeaModel):
    def __init__(
        self,
        advance_day: int = None,
        airline_corp_code: str = None,
        airline_corp_name: str = None,
        alipay_trade_no: str = None,
        apply_id: str = None,
        arr_airport_code: str = None,
        arr_city: str = None,
        arr_date: str = None,
        arr_station: str = None,
        arr_time: str = None,
        bill_record_time: str = None,
        book_time: str = None,
        booker_id: str = None,
        booker_job_no: str = None,
        booker_name: str = None,
        btrip_coupon_fee: float = None,
        build_fee: float = None,
        cabin: str = None,
        cabin_class: str = None,
        capital_direction: str = None,
        cascade_department: str = None,
        change_fee: float = None,
        corp_pay_order_fee: float = None,
        cost_center: str = None,
        cost_center_number: str = None,
        coupon: float = None,
        dep_airport_code: str = None,
        department: str = None,
        department_id: str = None,
        dept_city: str = None,
        dept_date: str = None,
        dept_station: str = None,
        dept_time: str = None,
        discount: str = None,
        fee_type: str = None,
        flight_no: str = None,
        index: str = None,
        insurance_fee: float = None,
        invoice_title: str = None,
        itinerary_num: str = None,
        itinerary_price: float = None,
        most_difference_dept_time: str = None,
        most_difference_discount: str = None,
        most_difference_flight_no: str = None,
        most_difference_price: float = None,
        most_difference_reason: str = None,
        most_price: float = None,
        negotiation_coupon_fee: float = None,
        oil_fee: float = None,
        order_id: str = None,
        over_apply_id: str = None,
        primary_id: int = None,
        project_code: str = None,
        project_name: str = None,
        refund_fee: float = None,
        refund_upgrade_cost: float = None,
        remark: str = None,
        repeat_refund: str = None,
        seal_price: float = None,
        service_fee: float = None,
        settlement_fee: float = None,
        settlement_grant_fee: float = None,
        settlement_time: str = None,
        settlement_type: str = None,
        status: int = None,
        ticket_id: str = None,
        traveler_id: str = None,
        traveler_job_no: str = None,
        traveler_name: str = None,
        upgrade_cost: float = None,
        voucher_type: int = None,
    ):
        self.advance_day = advance_day
        self.airline_corp_code = airline_corp_code
        self.airline_corp_name = airline_corp_name
        self.alipay_trade_no = alipay_trade_no
        self.apply_id = apply_id
        self.arr_airport_code = arr_airport_code
        self.arr_city = arr_city
        self.arr_date = arr_date
        self.arr_station = arr_station
        self.arr_time = arr_time
        self.bill_record_time = bill_record_time
        self.book_time = book_time
        self.booker_id = booker_id
        self.booker_job_no = booker_job_no
        self.booker_name = booker_name
        self.btrip_coupon_fee = btrip_coupon_fee
        self.build_fee = build_fee
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.capital_direction = capital_direction
        self.cascade_department = cascade_department
        self.change_fee = change_fee
        self.corp_pay_order_fee = corp_pay_order_fee
        self.cost_center = cost_center
        self.cost_center_number = cost_center_number
        self.coupon = coupon
        self.dep_airport_code = dep_airport_code
        self.department = department
        self.department_id = department_id
        self.dept_city = dept_city
        self.dept_date = dept_date
        self.dept_station = dept_station
        self.dept_time = dept_time
        self.discount = discount
        self.fee_type = fee_type
        self.flight_no = flight_no
        self.index = index
        self.insurance_fee = insurance_fee
        self.invoice_title = invoice_title
        self.itinerary_num = itinerary_num
        self.itinerary_price = itinerary_price
        self.most_difference_dept_time = most_difference_dept_time
        self.most_difference_discount = most_difference_discount
        self.most_difference_flight_no = most_difference_flight_no
        self.most_difference_price = most_difference_price
        self.most_difference_reason = most_difference_reason
        self.most_price = most_price
        self.negotiation_coupon_fee = negotiation_coupon_fee
        self.oil_fee = oil_fee
        self.order_id = order_id
        self.over_apply_id = over_apply_id
        self.primary_id = primary_id
        self.project_code = project_code
        self.project_name = project_name
        self.refund_fee = refund_fee
        self.refund_upgrade_cost = refund_upgrade_cost
        self.remark = remark
        self.repeat_refund = repeat_refund
        self.seal_price = seal_price
        self.service_fee = service_fee
        self.settlement_fee = settlement_fee
        self.settlement_grant_fee = settlement_grant_fee
        self.settlement_time = settlement_time
        self.settlement_type = settlement_type
        self.status = status
        self.ticket_id = ticket_id
        self.traveler_id = traveler_id
        self.traveler_job_no = traveler_job_no
        self.traveler_name = traveler_name
        self.upgrade_cost = upgrade_cost
        self.voucher_type = voucher_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advance_day is not None:
            result['advance_day'] = self.advance_day
        if self.airline_corp_code is not None:
            result['airline_corp_code'] = self.airline_corp_code
        if self.airline_corp_name is not None:
            result['airline_corp_name'] = self.airline_corp_name
        if self.alipay_trade_no is not None:
            result['alipay_trade_no'] = self.alipay_trade_no
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.arr_airport_code is not None:
            result['arr_airport_code'] = self.arr_airport_code
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city
        if self.arr_date is not None:
            result['arr_date'] = self.arr_date
        if self.arr_station is not None:
            result['arr_station'] = self.arr_station
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time
        if self.bill_record_time is not None:
            result['bill_record_time'] = self.bill_record_time
        if self.book_time is not None:
            result['book_time'] = self.book_time
        if self.booker_id is not None:
            result['booker_id'] = self.booker_id
        if self.booker_job_no is not None:
            result['booker_job_no'] = self.booker_job_no
        if self.booker_name is not None:
            result['booker_name'] = self.booker_name
        if self.btrip_coupon_fee is not None:
            result['btrip_coupon_fee'] = self.btrip_coupon_fee
        if self.build_fee is not None:
            result['build_fee'] = self.build_fee
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.capital_direction is not None:
            result['capital_direction'] = self.capital_direction
        if self.cascade_department is not None:
            result['cascade_department'] = self.cascade_department
        if self.change_fee is not None:
            result['change_fee'] = self.change_fee
        if self.corp_pay_order_fee is not None:
            result['corp_pay_order_fee'] = self.corp_pay_order_fee
        if self.cost_center is not None:
            result['cost_center'] = self.cost_center
        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number
        if self.coupon is not None:
            result['coupon'] = self.coupon
        if self.dep_airport_code is not None:
            result['dep_airport_code'] = self.dep_airport_code
        if self.department is not None:
            result['department'] = self.department
        if self.department_id is not None:
            result['department_id'] = self.department_id
        if self.dept_city is not None:
            result['dept_city'] = self.dept_city
        if self.dept_date is not None:
            result['dept_date'] = self.dept_date
        if self.dept_station is not None:
            result['dept_station'] = self.dept_station
        if self.dept_time is not None:
            result['dept_time'] = self.dept_time
        if self.discount is not None:
            result['discount'] = self.discount
        if self.fee_type is not None:
            result['fee_type'] = self.fee_type
        if self.flight_no is not None:
            result['flight_no'] = self.flight_no
        if self.index is not None:
            result['index'] = self.index
        if self.insurance_fee is not None:
            result['insurance_fee'] = self.insurance_fee
        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title
        if self.itinerary_num is not None:
            result['itinerary_num'] = self.itinerary_num
        if self.itinerary_price is not None:
            result['itinerary_price'] = self.itinerary_price
        if self.most_difference_dept_time is not None:
            result['most_difference_dept_time'] = self.most_difference_dept_time
        if self.most_difference_discount is not None:
            result['most_difference_discount'] = self.most_difference_discount
        if self.most_difference_flight_no is not None:
            result['most_difference_flight_no'] = self.most_difference_flight_no
        if self.most_difference_price is not None:
            result['most_difference_price'] = self.most_difference_price
        if self.most_difference_reason is not None:
            result['most_difference_reason'] = self.most_difference_reason
        if self.most_price is not None:
            result['most_price'] = self.most_price
        if self.negotiation_coupon_fee is not None:
            result['negotiation_coupon_fee'] = self.negotiation_coupon_fee
        if self.oil_fee is not None:
            result['oil_fee'] = self.oil_fee
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.over_apply_id is not None:
            result['over_apply_id'] = self.over_apply_id
        if self.primary_id is not None:
            result['primary_id'] = self.primary_id
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_name is not None:
            result['project_name'] = self.project_name
        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee
        if self.refund_upgrade_cost is not None:
            result['refund_upgrade_cost'] = self.refund_upgrade_cost
        if self.remark is not None:
            result['remark'] = self.remark
        if self.repeat_refund is not None:
            result['repeat_refund'] = self.repeat_refund
        if self.seal_price is not None:
            result['seal_price'] = self.seal_price
        if self.service_fee is not None:
            result['service_fee'] = self.service_fee
        if self.settlement_fee is not None:
            result['settlement_fee'] = self.settlement_fee
        if self.settlement_grant_fee is not None:
            result['settlement_grant_fee'] = self.settlement_grant_fee
        if self.settlement_time is not None:
            result['settlement_time'] = self.settlement_time
        if self.settlement_type is not None:
            result['settlement_type'] = self.settlement_type
        if self.status is not None:
            result['status'] = self.status
        if self.ticket_id is not None:
            result['ticket_id'] = self.ticket_id
        if self.traveler_id is not None:
            result['traveler_id'] = self.traveler_id
        if self.traveler_job_no is not None:
            result['traveler_job_no'] = self.traveler_job_no
        if self.traveler_name is not None:
            result['traveler_name'] = self.traveler_name
        if self.upgrade_cost is not None:
            result['upgrade_cost'] = self.upgrade_cost
        if self.voucher_type is not None:
            result['voucher_type'] = self.voucher_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advance_day') is not None:
            self.advance_day = m.get('advance_day')
        if m.get('airline_corp_code') is not None:
            self.airline_corp_code = m.get('airline_corp_code')
        if m.get('airline_corp_name') is not None:
            self.airline_corp_name = m.get('airline_corp_name')
        if m.get('alipay_trade_no') is not None:
            self.alipay_trade_no = m.get('alipay_trade_no')
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('arr_airport_code') is not None:
            self.arr_airport_code = m.get('arr_airport_code')
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')
        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')
        if m.get('arr_station') is not None:
            self.arr_station = m.get('arr_station')
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')
        if m.get('bill_record_time') is not None:
            self.bill_record_time = m.get('bill_record_time')
        if m.get('book_time') is not None:
            self.book_time = m.get('book_time')
        if m.get('booker_id') is not None:
            self.booker_id = m.get('booker_id')
        if m.get('booker_job_no') is not None:
            self.booker_job_no = m.get('booker_job_no')
        if m.get('booker_name') is not None:
            self.booker_name = m.get('booker_name')
        if m.get('btrip_coupon_fee') is not None:
            self.btrip_coupon_fee = m.get('btrip_coupon_fee')
        if m.get('build_fee') is not None:
            self.build_fee = m.get('build_fee')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('capital_direction') is not None:
            self.capital_direction = m.get('capital_direction')
        if m.get('cascade_department') is not None:
            self.cascade_department = m.get('cascade_department')
        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')
        if m.get('corp_pay_order_fee') is not None:
            self.corp_pay_order_fee = m.get('corp_pay_order_fee')
        if m.get('cost_center') is not None:
            self.cost_center = m.get('cost_center')
        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')
        if m.get('coupon') is not None:
            self.coupon = m.get('coupon')
        if m.get('dep_airport_code') is not None:
            self.dep_airport_code = m.get('dep_airport_code')
        if m.get('department') is not None:
            self.department = m.get('department')
        if m.get('department_id') is not None:
            self.department_id = m.get('department_id')
        if m.get('dept_city') is not None:
            self.dept_city = m.get('dept_city')
        if m.get('dept_date') is not None:
            self.dept_date = m.get('dept_date')
        if m.get('dept_station') is not None:
            self.dept_station = m.get('dept_station')
        if m.get('dept_time') is not None:
            self.dept_time = m.get('dept_time')
        if m.get('discount') is not None:
            self.discount = m.get('discount')
        if m.get('fee_type') is not None:
            self.fee_type = m.get('fee_type')
        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('insurance_fee') is not None:
            self.insurance_fee = m.get('insurance_fee')
        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')
        if m.get('itinerary_num') is not None:
            self.itinerary_num = m.get('itinerary_num')
        if m.get('itinerary_price') is not None:
            self.itinerary_price = m.get('itinerary_price')
        if m.get('most_difference_dept_time') is not None:
            self.most_difference_dept_time = m.get('most_difference_dept_time')
        if m.get('most_difference_discount') is not None:
            self.most_difference_discount = m.get('most_difference_discount')
        if m.get('most_difference_flight_no') is not None:
            self.most_difference_flight_no = m.get('most_difference_flight_no')
        if m.get('most_difference_price') is not None:
            self.most_difference_price = m.get('most_difference_price')
        if m.get('most_difference_reason') is not None:
            self.most_difference_reason = m.get('most_difference_reason')
        if m.get('most_price') is not None:
            self.most_price = m.get('most_price')
        if m.get('negotiation_coupon_fee') is not None:
            self.negotiation_coupon_fee = m.get('negotiation_coupon_fee')
        if m.get('oil_fee') is not None:
            self.oil_fee = m.get('oil_fee')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('over_apply_id') is not None:
            self.over_apply_id = m.get('over_apply_id')
        if m.get('primary_id') is not None:
            self.primary_id = m.get('primary_id')
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_name') is not None:
            self.project_name = m.get('project_name')
        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')
        if m.get('refund_upgrade_cost') is not None:
            self.refund_upgrade_cost = m.get('refund_upgrade_cost')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('repeat_refund') is not None:
            self.repeat_refund = m.get('repeat_refund')
        if m.get('seal_price') is not None:
            self.seal_price = m.get('seal_price')
        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')
        if m.get('settlement_fee') is not None:
            self.settlement_fee = m.get('settlement_fee')
        if m.get('settlement_grant_fee') is not None:
            self.settlement_grant_fee = m.get('settlement_grant_fee')
        if m.get('settlement_time') is not None:
            self.settlement_time = m.get('settlement_time')
        if m.get('settlement_type') is not None:
            self.settlement_type = m.get('settlement_type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('ticket_id') is not None:
            self.ticket_id = m.get('ticket_id')
        if m.get('traveler_id') is not None:
            self.traveler_id = m.get('traveler_id')
        if m.get('traveler_job_no') is not None:
            self.traveler_job_no = m.get('traveler_job_no')
        if m.get('traveler_name') is not None:
            self.traveler_name = m.get('traveler_name')
        if m.get('upgrade_cost') is not None:
            self.upgrade_cost = m.get('upgrade_cost')
        if m.get('voucher_type') is not None:
            self.voucher_type = m.get('voucher_type')
        return self


class FlightBillSettlementQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        data_list: List[FlightBillSettlementQueryResponseBodyModuleDataList] = None,
        period_end: str = None,
        period_start: str = None,
        total_num: int = None,
    ):
        self.category = category
        self.corp_id = corp_id
        self.data_list = data_list
        self.period_end = period_end
        self.period_start = period_start
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        result['data_list'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['data_list'].append(k.to_map() if k else None)
        if self.period_end is not None:
            result['period_end'] = self.period_end
        if self.period_start is not None:
            result['period_start'] = self.period_start
        if self.total_num is not None:
            result['total_num'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        self.data_list = []
        if m.get('data_list') is not None:
            for k in m.get('data_list'):
                temp_model = FlightBillSettlementQueryResponseBodyModuleDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('period_end') is not None:
            self.period_end = m.get('period_end')
        if m.get('period_start') is not None:
            self.period_start = m.get('period_start')
        if m.get('total_num') is not None:
            self.total_num = m.get('total_num')
        return self


class FlightBillSettlementQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: FlightBillSettlementQueryResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = FlightBillSettlementQueryResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class FlightBillSettlementQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FlightBillSettlementQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FlightBillSettlementQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlightExceedApplyQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class FlightExceedApplyQueryRequest(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
    ):
        self.apply_id = apply_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        return self


class FlightExceedApplyQueryResponseBodyModuleApplyIntentionInfoDo(TeaModel):
    def __init__(
        self,
        arr_city: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        cabin: str = None,
        cabin_class: int = None,
        cabin_class_str: str = None,
        dep_city: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        discount: str = None,
        flight_no: str = None,
        price: int = None,
        type: int = None,
    ):
        self.arr_city = arr_city
        self.arr_city_name = arr_city_name
        self.arr_time = arr_time
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.cabin_class_str = cabin_class_str
        self.dep_city = dep_city
        self.dep_city_name = dep_city_name
        self.dep_time = dep_time
        self.discount = discount
        self.flight_no = flight_no
        self.price = price
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city
        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.cabin_class_str is not None:
            result['cabin_class_str'] = self.cabin_class_str
        if self.dep_city is not None:
            result['dep_city'] = self.dep_city
        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name
        if self.dep_time is not None:
            result['dep_time'] = self.dep_time
        if self.discount is not None:
            result['discount'] = self.discount
        if self.flight_no is not None:
            result['flight_no'] = self.flight_no
        if self.price is not None:
            result['price'] = self.price
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')
        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('cabin_class_str') is not None:
            self.cabin_class_str = m.get('cabin_class_str')
        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')
        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')
        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')
        if m.get('discount') is not None:
            self.discount = m.get('discount')
        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class FlightExceedApplyQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        apply_intention_info_do: FlightExceedApplyQueryResponseBodyModuleApplyIntentionInfoDo = None,
        btrip_cause: str = None,
        corp_id: str = None,
        exceed_reason: str = None,
        exceed_type: int = None,
        origin_standard: str = None,
        status: int = None,
        submit_time: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_corp_id: str = None,
        user_id: str = None,
    ):
        self.apply_id = apply_id
        self.apply_intention_info_do = apply_intention_info_do
        self.btrip_cause = btrip_cause
        self.corp_id = corp_id
        self.exceed_reason = exceed_reason
        self.exceed_type = exceed_type
        self.origin_standard = origin_standard
        self.status = status
        self.submit_time = submit_time
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_corp_id = thirdpart_corp_id
        self.user_id = user_id

    def validate(self):
        if self.apply_intention_info_do:
            self.apply_intention_info_do.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.apply_intention_info_do is not None:
            result['apply_intention_info_do'] = self.apply_intention_info_do.to_map()
        if self.btrip_cause is not None:
            result['btrip_cause'] = self.btrip_cause
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.exceed_reason is not None:
            result['exceed_reason'] = self.exceed_reason
        if self.exceed_type is not None:
            result['exceed_type'] = self.exceed_type
        if self.origin_standard is not None:
            result['origin_standard'] = self.origin_standard
        if self.status is not None:
            result['status'] = self.status
        if self.submit_time is not None:
            result['submit_time'] = self.submit_time
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.thirdpart_corp_id is not None:
            result['thirdpart_corp_id'] = self.thirdpart_corp_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('apply_intention_info_do') is not None:
            temp_model = FlightExceedApplyQueryResponseBodyModuleApplyIntentionInfoDo()
            self.apply_intention_info_do = temp_model.from_map(m['apply_intention_info_do'])
        if m.get('btrip_cause') is not None:
            self.btrip_cause = m.get('btrip_cause')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('exceed_reason') is not None:
            self.exceed_reason = m.get('exceed_reason')
        if m.get('exceed_type') is not None:
            self.exceed_type = m.get('exceed_type')
        if m.get('origin_standard') is not None:
            self.origin_standard = m.get('origin_standard')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('submit_time') is not None:
            self.submit_time = m.get('submit_time')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('thirdpart_corp_id') is not None:
            self.thirdpart_corp_id = m.get('thirdpart_corp_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class FlightExceedApplyQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: FlightExceedApplyQueryResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = FlightExceedApplyQueryResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class FlightExceedApplyQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FlightExceedApplyQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FlightExceedApplyQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlightOrderListQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class FlightOrderListQueryRequest(TeaModel):
    def __init__(
        self,
        all_apply: bool = None,
        apply_id: int = None,
        depart_id: str = None,
        end_time: str = None,
        page: int = None,
        page_size: int = None,
        start_time: str = None,
        thirdpart_apply_id: str = None,
        update_end_time: str = None,
        update_start_time: str = None,
        user_id: str = None,
    ):
        self.all_apply = all_apply
        self.apply_id = apply_id
        self.depart_id = depart_id
        self.end_time = end_time
        self.page = page
        self.page_size = page_size
        self.start_time = start_time
        self.thirdpart_apply_id = thirdpart_apply_id
        self.update_end_time = update_end_time
        self.update_start_time = update_start_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_apply is not None:
            result['all_apply'] = self.all_apply
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.update_end_time is not None:
            result['update_end_time'] = self.update_end_time
        if self.update_start_time is not None:
            result['update_start_time'] = self.update_start_time
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all_apply') is not None:
            self.all_apply = m.get('all_apply')
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('update_end_time') is not None:
            self.update_end_time = m.get('update_end_time')
        if m.get('update_start_time') is not None:
            self.update_start_time = m.get('update_start_time')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class FlightOrderListQueryResponseBodyModuleCostCenter(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        id: int = None,
        name: str = None,
        number: str = None,
    ):
        self.corp_id = corp_id
        self.id = id
        self.name = name
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        return self


class FlightOrderListQueryResponseBodyModuleInsureInfoList(TeaModel):
    def __init__(
        self,
        insure_no: str = None,
        name: str = None,
        status: int = None,
    ):
        self.insure_no = insure_no
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.insure_no is not None:
            result['insure_no'] = self.insure_no
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('insure_no') is not None:
            self.insure_no = m.get('insure_no')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class FlightOrderListQueryResponseBodyModuleInvoice(TeaModel):
    def __init__(
        self,
        id: int = None,
        title: str = None,
    ):
        self.id = id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class FlightOrderListQueryResponseBodyModulePriceInfoList(TeaModel):
    def __init__(
        self,
        category_code: int = None,
        category_type: int = None,
        change_flight_no: str = None,
        discount: str = None,
        end_time: str = None,
        gmt_create: str = None,
        original_ticket_no: str = None,
        passenger_name: str = None,
        pay_type: int = None,
        price: float = None,
        start_time: str = None,
        ticket_no: str = None,
        trade_id: str = None,
        type: int = None,
    ):
        self.category_code = category_code
        self.category_type = category_type
        self.change_flight_no = change_flight_no
        self.discount = discount
        self.end_time = end_time
        self.gmt_create = gmt_create
        self.original_ticket_no = original_ticket_no
        self.passenger_name = passenger_name
        self.pay_type = pay_type
        self.price = price
        self.start_time = start_time
        self.ticket_no = ticket_no
        self.trade_id = trade_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_code is not None:
            result['category_code'] = self.category_code
        if self.category_type is not None:
            result['category_type'] = self.category_type
        if self.change_flight_no is not None:
            result['change_flight_no'] = self.change_flight_no
        if self.discount is not None:
            result['discount'] = self.discount
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.original_ticket_no is not None:
            result['original_ticket_no'] = self.original_ticket_no
        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name
        if self.pay_type is not None:
            result['pay_type'] = self.pay_type
        if self.price is not None:
            result['price'] = self.price
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no
        if self.trade_id is not None:
            result['trade_id'] = self.trade_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category_code') is not None:
            self.category_code = m.get('category_code')
        if m.get('category_type') is not None:
            self.category_type = m.get('category_type')
        if m.get('change_flight_no') is not None:
            self.change_flight_no = m.get('change_flight_no')
        if m.get('discount') is not None:
            self.discount = m.get('discount')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('original_ticket_no') is not None:
            self.original_ticket_no = m.get('original_ticket_no')
        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')
        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')
        if m.get('trade_id') is not None:
            self.trade_id = m.get('trade_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class FlightOrderListQueryResponseBodyModuleUserAffiliateList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class FlightOrderListQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        arr_airport: str = None,
        arr_city: str = None,
        btrip_title: str = None,
        cabin_class: str = None,
        contact_name: str = None,
        corp_id: str = None,
        corp_name: str = None,
        cost_center: FlightOrderListQueryResponseBodyModuleCostCenter = None,
        dep_airport: str = None,
        dep_city: str = None,
        dep_date: str = None,
        depart_id: str = None,
        depart_name: str = None,
        discount: str = None,
        flight_no: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        insure_info_list: List[FlightOrderListQueryResponseBodyModuleInsureInfoList] = None,
        invoice: FlightOrderListQueryResponseBodyModuleInvoice = None,
        passenger_count: int = None,
        passenger_name: str = None,
        price_info_list: List[FlightOrderListQueryResponseBodyModulePriceInfoList] = None,
        project_code: str = None,
        project_id: int = None,
        project_title: str = None,
        ret_date: str = None,
        status: int = None,
        third_part_project_id: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_itinerary_id: str = None,
        trip_type: int = None,
        user_affiliate_list: List[FlightOrderListQueryResponseBodyModuleUserAffiliateList] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.apply_id = apply_id
        self.arr_airport = arr_airport
        self.arr_city = arr_city
        self.btrip_title = btrip_title
        self.cabin_class = cabin_class
        self.contact_name = contact_name
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.cost_center = cost_center
        self.dep_airport = dep_airport
        self.dep_city = dep_city
        self.dep_date = dep_date
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.discount = discount
        self.flight_no = flight_no
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.insure_info_list = insure_info_list
        self.invoice = invoice
        self.passenger_count = passenger_count
        self.passenger_name = passenger_name
        self.price_info_list = price_info_list
        self.project_code = project_code
        self.project_id = project_id
        self.project_title = project_title
        self.ret_date = ret_date
        self.status = status
        self.third_part_project_id = third_part_project_id
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_itinerary_id = thirdpart_itinerary_id
        self.trip_type = trip_type
        self.user_affiliate_list = user_affiliate_list
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.cost_center:
            self.cost_center.validate()
        if self.insure_info_list:
            for k in self.insure_info_list:
                if k:
                    k.validate()
        if self.invoice:
            self.invoice.validate()
        if self.price_info_list:
            for k in self.price_info_list:
                if k:
                    k.validate()
        if self.user_affiliate_list:
            for k in self.user_affiliate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.arr_airport is not None:
            result['arr_airport'] = self.arr_airport
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city
        if self.btrip_title is not None:
            result['btrip_title'] = self.btrip_title
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.contact_name is not None:
            result['contact_name'] = self.contact_name
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.corp_name is not None:
            result['corp_name'] = self.corp_name
        if self.cost_center is not None:
            result['cost_center'] = self.cost_center.to_map()
        if self.dep_airport is not None:
            result['dep_airport'] = self.dep_airport
        if self.dep_city is not None:
            result['dep_city'] = self.dep_city
        if self.dep_date is not None:
            result['dep_date'] = self.dep_date
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.depart_name is not None:
            result['depart_name'] = self.depart_name
        if self.discount is not None:
            result['discount'] = self.discount
        if self.flight_no is not None:
            result['flight_no'] = self.flight_no
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        result['insure_info_list'] = []
        if self.insure_info_list is not None:
            for k in self.insure_info_list:
                result['insure_info_list'].append(k.to_map() if k else None)
        if self.invoice is not None:
            result['invoice'] = self.invoice.to_map()
        if self.passenger_count is not None:
            result['passenger_count'] = self.passenger_count
        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name
        result['price_info_list'] = []
        if self.price_info_list is not None:
            for k in self.price_info_list:
                result['price_info_list'].append(k.to_map() if k else None)
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.project_title is not None:
            result['project_title'] = self.project_title
        if self.ret_date is not None:
            result['ret_date'] = self.ret_date
        if self.status is not None:
            result['status'] = self.status
        if self.third_part_project_id is not None:
            result['third_part_project_id'] = self.third_part_project_id
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id
        if self.trip_type is not None:
            result['trip_type'] = self.trip_type
        result['user_affiliate_list'] = []
        if self.user_affiliate_list is not None:
            for k in self.user_affiliate_list:
                result['user_affiliate_list'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('arr_airport') is not None:
            self.arr_airport = m.get('arr_airport')
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')
        if m.get('btrip_title') is not None:
            self.btrip_title = m.get('btrip_title')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('contact_name') is not None:
            self.contact_name = m.get('contact_name')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')
        if m.get('cost_center') is not None:
            temp_model = FlightOrderListQueryResponseBodyModuleCostCenter()
            self.cost_center = temp_model.from_map(m['cost_center'])
        if m.get('dep_airport') is not None:
            self.dep_airport = m.get('dep_airport')
        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')
        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')
        if m.get('discount') is not None:
            self.discount = m.get('discount')
        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')
        if m.get('id') is not None:
            self.id = m.get('id')
        self.insure_info_list = []
        if m.get('insure_info_list') is not None:
            for k in m.get('insure_info_list'):
                temp_model = FlightOrderListQueryResponseBodyModuleInsureInfoList()
                self.insure_info_list.append(temp_model.from_map(k))
        if m.get('invoice') is not None:
            temp_model = FlightOrderListQueryResponseBodyModuleInvoice()
            self.invoice = temp_model.from_map(m['invoice'])
        if m.get('passenger_count') is not None:
            self.passenger_count = m.get('passenger_count')
        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')
        self.price_info_list = []
        if m.get('price_info_list') is not None:
            for k in m.get('price_info_list'):
                temp_model = FlightOrderListQueryResponseBodyModulePriceInfoList()
                self.price_info_list.append(temp_model.from_map(k))
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')
        if m.get('ret_date') is not None:
            self.ret_date = m.get('ret_date')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('third_part_project_id') is not None:
            self.third_part_project_id = m.get('third_part_project_id')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')
        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')
        self.user_affiliate_list = []
        if m.get('user_affiliate_list') is not None:
            for k in m.get('user_affiliate_list'):
                temp_model = FlightOrderListQueryResponseBodyModuleUserAffiliateList()
                self.user_affiliate_list.append(temp_model.from_map(k))
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class FlightOrderListQueryResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        total_number: int = None,
    ):
        self.page = page
        self.page_size = page_size
        self.total_number = total_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_number is not None:
            result['total_number'] = self.total_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_number') is not None:
            self.total_number = m.get('total_number')
        return self


class FlightOrderListQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: List[FlightOrderListQueryResponseBodyModule] = None,
        page_info: FlightOrderListQueryResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.page_info = page_info
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            for k in self.module:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        result['module'] = []
        if self.module is not None:
            for k in self.module:
                result['module'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
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
        self.module = []
        if m.get('module') is not None:
            for k in m.get('module'):
                temp_model = FlightOrderListQueryResponseBodyModule()
                self.module.append(temp_model.from_map(k))
        if m.get('page_info') is not None:
            temp_model = FlightOrderListQueryResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['page_info'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class FlightOrderListQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FlightOrderListQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FlightOrderListQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlightOrderQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class FlightOrderQueryRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        user_id: str = None,
    ):
        self.order_id = order_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class FlightOrderQueryResponseBodyModuleFlightChangeTicketInfoList(TeaModel):
    def __init__(
        self,
        arr_time: str = None,
        change_cabin: str = None,
        change_cabin_level: str = None,
        change_fee: float = None,
        change_flight_no: str = None,
        change_order_id: int = None,
        change_reason: str = None,
        change_type: int = None,
        dep_time: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        origin_ticket_no: str = None,
        ticket_no: str = None,
        upgrade_fee: float = None,
    ):
        self.arr_time = arr_time
        self.change_cabin = change_cabin
        self.change_cabin_level = change_cabin_level
        self.change_fee = change_fee
        self.change_flight_no = change_flight_no
        self.change_order_id = change_order_id
        self.change_reason = change_reason
        self.change_type = change_type
        self.dep_time = dep_time
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.origin_ticket_no = origin_ticket_no
        self.ticket_no = ticket_no
        self.upgrade_fee = upgrade_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time
        if self.change_cabin is not None:
            result['change_cabin'] = self.change_cabin
        if self.change_cabin_level is not None:
            result['change_cabin_level'] = self.change_cabin_level
        if self.change_fee is not None:
            result['change_fee'] = self.change_fee
        if self.change_flight_no is not None:
            result['change_flight_no'] = self.change_flight_no
        if self.change_order_id is not None:
            result['change_order_id'] = self.change_order_id
        if self.change_reason is not None:
            result['change_reason'] = self.change_reason
        if self.change_type is not None:
            result['change_type'] = self.change_type
        if self.dep_time is not None:
            result['dep_time'] = self.dep_time
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify
        if self.origin_ticket_no is not None:
            result['origin_ticket_no'] = self.origin_ticket_no
        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no
        if self.upgrade_fee is not None:
            result['upgrade_fee'] = self.upgrade_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')
        if m.get('change_cabin') is not None:
            self.change_cabin = m.get('change_cabin')
        if m.get('change_cabin_level') is not None:
            self.change_cabin_level = m.get('change_cabin_level')
        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')
        if m.get('change_flight_no') is not None:
            self.change_flight_no = m.get('change_flight_no')
        if m.get('change_order_id') is not None:
            self.change_order_id = m.get('change_order_id')
        if m.get('change_reason') is not None:
            self.change_reason = m.get('change_reason')
        if m.get('change_type') is not None:
            self.change_type = m.get('change_type')
        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')
        if m.get('origin_ticket_no') is not None:
            self.origin_ticket_no = m.get('origin_ticket_no')
        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')
        if m.get('upgrade_fee') is not None:
            self.upgrade_fee = m.get('upgrade_fee')
        return self


class FlightOrderQueryResponseBodyModuleFlightInfoList(TeaModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        arr_airport_code: str = None,
        arr_airport_name: str = None,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        cabin: str = None,
        cabin_level: str = None,
        dep_airport_code: str = None,
        dep_airport_name: str = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        flight_mile: int = None,
        flight_no: str = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.arr_airport_code = arr_airport_code
        self.arr_airport_name = arr_airport_name
        self.arr_city_code = arr_city_code
        self.arr_city_name = arr_city_name
        self.arr_time = arr_time
        self.cabin = cabin
        self.cabin_level = cabin_level
        self.dep_airport_code = dep_airport_code
        self.dep_airport_name = dep_airport_name
        self.dep_city_code = dep_city_code
        self.dep_city_name = dep_city_name
        self.dep_time = dep_time
        self.flight_mile = flight_mile
        self.flight_no = flight_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.airline_code is not None:
            result['airline_code'] = self.airline_code
        if self.airline_name is not None:
            result['airline_name'] = self.airline_name
        if self.arr_airport_code is not None:
            result['arr_airport_code'] = self.arr_airport_code
        if self.arr_airport_name is not None:
            result['arr_airport_name'] = self.arr_airport_name
        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code
        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_level is not None:
            result['cabin_level'] = self.cabin_level
        if self.dep_airport_code is not None:
            result['dep_airport_code'] = self.dep_airport_code
        if self.dep_airport_name is not None:
            result['dep_airport_name'] = self.dep_airport_name
        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code
        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name
        if self.dep_time is not None:
            result['dep_time'] = self.dep_time
        if self.flight_mile is not None:
            result['flight_mile'] = self.flight_mile
        if self.flight_no is not None:
            result['flight_no'] = self.flight_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')
        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')
        if m.get('arr_airport_code') is not None:
            self.arr_airport_code = m.get('arr_airport_code')
        if m.get('arr_airport_name') is not None:
            self.arr_airport_name = m.get('arr_airport_name')
        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')
        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_level') is not None:
            self.cabin_level = m.get('cabin_level')
        if m.get('dep_airport_code') is not None:
            self.dep_airport_code = m.get('dep_airport_code')
        if m.get('dep_airport_name') is not None:
            self.dep_airport_name = m.get('dep_airport_name')
        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')
        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')
        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')
        if m.get('flight_mile') is not None:
            self.flight_mile = m.get('flight_mile')
        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')
        return self


class FlightOrderQueryResponseBodyModuleFlightRefundTicketInfoList(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modify: str = None,
        refund_order_id: int = None,
        refund_reason: str = None,
        refund_ticket_fee: float = None,
        refund_type: int = None,
        ticket_no: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.refund_order_id = refund_order_id
        self.refund_reason = refund_reason
        self.refund_ticket_fee = refund_ticket_fee
        self.refund_type = refund_type
        self.ticket_no = ticket_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify
        if self.refund_order_id is not None:
            result['refund_order_id'] = self.refund_order_id
        if self.refund_reason is not None:
            result['refund_reason'] = self.refund_reason
        if self.refund_ticket_fee is not None:
            result['refund_ticket_fee'] = self.refund_ticket_fee
        if self.refund_type is not None:
            result['refund_type'] = self.refund_type
        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')
        if m.get('refund_order_id') is not None:
            self.refund_order_id = m.get('refund_order_id')
        if m.get('refund_reason') is not None:
            self.refund_reason = m.get('refund_reason')
        if m.get('refund_ticket_fee') is not None:
            self.refund_ticket_fee = m.get('refund_ticket_fee')
        if m.get('refund_type') is not None:
            self.refund_type = m.get('refund_type')
        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')
        return self


class FlightOrderQueryResponseBodyModuleFlightTicketInfoList(TeaModel):
    def __init__(
        self,
        build_price: float = None,
        changed: bool = None,
        discount: int = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        oil_price: float = None,
        pay_type: int = None,
        settle_price: float = None,
        ticket_no: str = None,
        ticket_price: float = None,
        ticket_status: str = None,
        ticket_status_code: int = None,
        user_id: str = None,
    ):
        self.build_price = build_price
        self.changed = changed
        self.discount = discount
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.oil_price = oil_price
        self.pay_type = pay_type
        self.settle_price = settle_price
        self.ticket_no = ticket_no
        self.ticket_price = ticket_price
        self.ticket_status = ticket_status
        self.ticket_status_code = ticket_status_code
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_price is not None:
            result['build_price'] = self.build_price
        if self.changed is not None:
            result['changed'] = self.changed
        if self.discount is not None:
            result['discount'] = self.discount
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify
        if self.oil_price is not None:
            result['oil_price'] = self.oil_price
        if self.pay_type is not None:
            result['pay_type'] = self.pay_type
        if self.settle_price is not None:
            result['settle_price'] = self.settle_price
        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no
        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price
        if self.ticket_status is not None:
            result['ticket_status'] = self.ticket_status
        if self.ticket_status_code is not None:
            result['ticket_status_code'] = self.ticket_status_code
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('build_price') is not None:
            self.build_price = m.get('build_price')
        if m.get('changed') is not None:
            self.changed = m.get('changed')
        if m.get('discount') is not None:
            self.discount = m.get('discount')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')
        if m.get('oil_price') is not None:
            self.oil_price = m.get('oil_price')
        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')
        if m.get('settle_price') is not None:
            self.settle_price = m.get('settle_price')
        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')
        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')
        if m.get('ticket_status') is not None:
            self.ticket_status = m.get('ticket_status')
        if m.get('ticket_status_code') is not None:
            self.ticket_status_code = m.get('ticket_status_code')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class FlightOrderQueryResponseBodyModuleInsuranceInfoList(TeaModel):
    def __init__(
        self,
        amount: float = None,
        insurance_no: str = None,
        status: int = None,
        type: str = None,
    ):
        self.amount = amount
        self.insurance_no = insurance_no
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.insurance_no is not None:
            result['insurance_no'] = self.insurance_no
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('insurance_no') is not None:
            self.insurance_no = m.get('insurance_no')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class FlightOrderQueryResponseBodyModuleInvoiceInfo(TeaModel):
    def __init__(
        self,
        id: int = None,
        title: str = None,
    ):
        self.id = id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class FlightOrderQueryResponseBodyModuleOrderBaseInfo(TeaModel):
    def __init__(
        self,
        apply_id: str = None,
        btrip_title: str = None,
        contact_name: str = None,
        corp_id: str = None,
        corp_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        itinerary_id: str = None,
        order_id: int = None,
        order_status: int = None,
        thirdpart_apply_id: str = None,
        thirdpart_corp_id: str = None,
        thirdpart_itinerary_id: str = None,
        trip_type: int = None,
        user_id: str = None,
    ):
        self.apply_id = apply_id
        self.btrip_title = btrip_title
        self.contact_name = contact_name
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.itinerary_id = itinerary_id
        self.order_id = order_id
        self.order_status = order_status
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_corp_id = thirdpart_corp_id
        self.thirdpart_itinerary_id = thirdpart_itinerary_id
        self.trip_type = trip_type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.btrip_title is not None:
            result['btrip_title'] = self.btrip_title
        if self.contact_name is not None:
            result['contact_name'] = self.contact_name
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.corp_name is not None:
            result['corp_name'] = self.corp_name
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.depart_name is not None:
            result['depart_name'] = self.depart_name
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify
        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.order_status is not None:
            result['order_status'] = self.order_status
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.thirdpart_corp_id is not None:
            result['thirdpart_corp_id'] = self.thirdpart_corp_id
        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id
        if self.trip_type is not None:
            result['trip_type'] = self.trip_type
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('btrip_title') is not None:
            self.btrip_title = m.get('btrip_title')
        if m.get('contact_name') is not None:
            self.contact_name = m.get('contact_name')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')
        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('thirdpart_corp_id') is not None:
            self.thirdpart_corp_id = m.get('thirdpart_corp_id')
        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')
        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class FlightOrderQueryResponseBodyModulePassengerInfoList(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        cost_center_name: str = None,
        cost_center_number: str = None,
        project_code: str = None,
        project_id: int = None,
        project_title: str = None,
        thirdpart_project_id: str = None,
        user_id: str = None,
        user_name: str = None,
        user_type: int = None,
    ):
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.cost_center_number = cost_center_number
        self.project_code = project_code
        self.project_id = project_id
        self.project_title = project_title
        self.thirdpart_project_id = thirdpart_project_id
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id
        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name
        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.project_title is not None:
            result['project_title'] = self.project_title
        if self.thirdpart_project_id is not None:
            result['thirdpart_project_id'] = self.thirdpart_project_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        if self.user_type is not None:
            result['user_type'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')
        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')
        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')
        if m.get('thirdpart_project_id') is not None:
            self.thirdpart_project_id = m.get('thirdpart_project_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')
        return self


class FlightOrderQueryResponseBodyModulePriceInfoList(TeaModel):
    def __init__(
        self,
        category_code: int = None,
        gmt_create: str = None,
        passenger_name: str = None,
        pay_type: int = None,
        price: float = None,
        trade_id: str = None,
        type: int = None,
    ):
        self.category_code = category_code
        self.gmt_create = gmt_create
        self.passenger_name = passenger_name
        self.pay_type = pay_type
        self.price = price
        self.trade_id = trade_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_code is not None:
            result['category_code'] = self.category_code
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name
        if self.pay_type is not None:
            result['pay_type'] = self.pay_type
        if self.price is not None:
            result['price'] = self.price
        if self.trade_id is not None:
            result['trade_id'] = self.trade_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category_code') is not None:
            self.category_code = m.get('category_code')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')
        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('trade_id') is not None:
            self.trade_id = m.get('trade_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class FlightOrderQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        flight_change_ticket_info_list: List[FlightOrderQueryResponseBodyModuleFlightChangeTicketInfoList] = None,
        flight_info_list: List[FlightOrderQueryResponseBodyModuleFlightInfoList] = None,
        flight_refund_ticket_info_list: List[FlightOrderQueryResponseBodyModuleFlightRefundTicketInfoList] = None,
        flight_ticket_info_list: List[FlightOrderQueryResponseBodyModuleFlightTicketInfoList] = None,
        insurance_info_list: List[FlightOrderQueryResponseBodyModuleInsuranceInfoList] = None,
        invoice_info: FlightOrderQueryResponseBodyModuleInvoiceInfo = None,
        order_base_info: FlightOrderQueryResponseBodyModuleOrderBaseInfo = None,
        passenger_info_list: List[FlightOrderQueryResponseBodyModulePassengerInfoList] = None,
        price_info_list: List[FlightOrderQueryResponseBodyModulePriceInfoList] = None,
    ):
        self.flight_change_ticket_info_list = flight_change_ticket_info_list
        self.flight_info_list = flight_info_list
        self.flight_refund_ticket_info_list = flight_refund_ticket_info_list
        self.flight_ticket_info_list = flight_ticket_info_list
        self.insurance_info_list = insurance_info_list
        self.invoice_info = invoice_info
        self.order_base_info = order_base_info
        self.passenger_info_list = passenger_info_list
        self.price_info_list = price_info_list

    def validate(self):
        if self.flight_change_ticket_info_list:
            for k in self.flight_change_ticket_info_list:
                if k:
                    k.validate()
        if self.flight_info_list:
            for k in self.flight_info_list:
                if k:
                    k.validate()
        if self.flight_refund_ticket_info_list:
            for k in self.flight_refund_ticket_info_list:
                if k:
                    k.validate()
        if self.flight_ticket_info_list:
            for k in self.flight_ticket_info_list:
                if k:
                    k.validate()
        if self.insurance_info_list:
            for k in self.insurance_info_list:
                if k:
                    k.validate()
        if self.invoice_info:
            self.invoice_info.validate()
        if self.order_base_info:
            self.order_base_info.validate()
        if self.passenger_info_list:
            for k in self.passenger_info_list:
                if k:
                    k.validate()
        if self.price_info_list:
            for k in self.price_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['flight_change_ticket_info_list'] = []
        if self.flight_change_ticket_info_list is not None:
            for k in self.flight_change_ticket_info_list:
                result['flight_change_ticket_info_list'].append(k.to_map() if k else None)
        result['flight_info_list'] = []
        if self.flight_info_list is not None:
            for k in self.flight_info_list:
                result['flight_info_list'].append(k.to_map() if k else None)
        result['flight_refund_ticket_info_list'] = []
        if self.flight_refund_ticket_info_list is not None:
            for k in self.flight_refund_ticket_info_list:
                result['flight_refund_ticket_info_list'].append(k.to_map() if k else None)
        result['flight_ticket_info_list'] = []
        if self.flight_ticket_info_list is not None:
            for k in self.flight_ticket_info_list:
                result['flight_ticket_info_list'].append(k.to_map() if k else None)
        result['insurance_info_list'] = []
        if self.insurance_info_list is not None:
            for k in self.insurance_info_list:
                result['insurance_info_list'].append(k.to_map() if k else None)
        if self.invoice_info is not None:
            result['invoice_info'] = self.invoice_info.to_map()
        if self.order_base_info is not None:
            result['order_base_info'] = self.order_base_info.to_map()
        result['passenger_info_list'] = []
        if self.passenger_info_list is not None:
            for k in self.passenger_info_list:
                result['passenger_info_list'].append(k.to_map() if k else None)
        result['price_info_list'] = []
        if self.price_info_list is not None:
            for k in self.price_info_list:
                result['price_info_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_change_ticket_info_list = []
        if m.get('flight_change_ticket_info_list') is not None:
            for k in m.get('flight_change_ticket_info_list'):
                temp_model = FlightOrderQueryResponseBodyModuleFlightChangeTicketInfoList()
                self.flight_change_ticket_info_list.append(temp_model.from_map(k))
        self.flight_info_list = []
        if m.get('flight_info_list') is not None:
            for k in m.get('flight_info_list'):
                temp_model = FlightOrderQueryResponseBodyModuleFlightInfoList()
                self.flight_info_list.append(temp_model.from_map(k))
        self.flight_refund_ticket_info_list = []
        if m.get('flight_refund_ticket_info_list') is not None:
            for k in m.get('flight_refund_ticket_info_list'):
                temp_model = FlightOrderQueryResponseBodyModuleFlightRefundTicketInfoList()
                self.flight_refund_ticket_info_list.append(temp_model.from_map(k))
        self.flight_ticket_info_list = []
        if m.get('flight_ticket_info_list') is not None:
            for k in m.get('flight_ticket_info_list'):
                temp_model = FlightOrderQueryResponseBodyModuleFlightTicketInfoList()
                self.flight_ticket_info_list.append(temp_model.from_map(k))
        self.insurance_info_list = []
        if m.get('insurance_info_list') is not None:
            for k in m.get('insurance_info_list'):
                temp_model = FlightOrderQueryResponseBodyModuleInsuranceInfoList()
                self.insurance_info_list.append(temp_model.from_map(k))
        if m.get('invoice_info') is not None:
            temp_model = FlightOrderQueryResponseBodyModuleInvoiceInfo()
            self.invoice_info = temp_model.from_map(m['invoice_info'])
        if m.get('order_base_info') is not None:
            temp_model = FlightOrderQueryResponseBodyModuleOrderBaseInfo()
            self.order_base_info = temp_model.from_map(m['order_base_info'])
        self.passenger_info_list = []
        if m.get('passenger_info_list') is not None:
            for k in m.get('passenger_info_list'):
                temp_model = FlightOrderQueryResponseBodyModulePassengerInfoList()
                self.passenger_info_list.append(temp_model.from_map(k))
        self.price_info_list = []
        if m.get('price_info_list') is not None:
            for k in m.get('price_info_list'):
                temp_model = FlightOrderQueryResponseBodyModulePriceInfoList()
                self.price_info_list.append(temp_model.from_map(k))
        return self


class FlightOrderQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: FlightOrderQueryResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = FlightOrderQueryResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class FlightOrderQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FlightOrderQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FlightOrderQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HotelBillSettlementQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class HotelBillSettlementQueryRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        period_end: str = None,
        period_start: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.period_end = period_end
        self.period_start = period_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['page_no'] = self.page_no
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.period_end is not None:
            result['period_end'] = self.period_end
        if self.period_start is not None:
            result['period_start'] = self.period_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_no') is not None:
            self.page_no = m.get('page_no')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('period_end') is not None:
            self.period_end = m.get('period_end')
        if m.get('period_start') is not None:
            self.period_start = m.get('period_start')
        return self


class HotelBillSettlementQueryResponseBodyModuleDataList(TeaModel):
    def __init__(
        self,
        alipay_trade_no: str = None,
        apply_id: str = None,
        bill_record_time: str = None,
        book_time: str = None,
        booker_id: str = None,
        booker_job_no: str = None,
        booker_name: str = None,
        capital_direction: str = None,
        cascade_department: str = None,
        check_in_date: str = None,
        checkout_date: str = None,
        city: str = None,
        city_code: str = None,
        corp_refund_fee: float = None,
        corp_total_fee: float = None,
        cost_center: str = None,
        cost_center_number: str = None,
        department: str = None,
        department_id: str = None,
        fee_type: str = None,
        fees: float = None,
        fu_point_fee: float = None,
        hotel_name: str = None,
        index: str = None,
        invoice_title: str = None,
        is_negotiation: str = None,
        is_share_str: str = None,
        nights: int = None,
        order_id: str = None,
        order_price: float = None,
        order_type: str = None,
        over_apply_id: str = None,
        person_refund_fee: float = None,
        person_settle_price: float = None,
        primary_id: int = None,
        project_code: str = None,
        project_name: str = None,
        promotion_fee: float = None,
        remark: str = None,
        room_number: int = None,
        room_price: float = None,
        room_type: str = None,
        service_fee: float = None,
        settlement_fee: float = None,
        settlement_grant_fee: float = None,
        settlement_time: str = None,
        settlement_type: str = None,
        status: int = None,
        total_nights: int = None,
        traveler_id: str = None,
        traveler_job_no: str = None,
        traveler_name: str = None,
        voucher_type: int = None,
    ):
        self.alipay_trade_no = alipay_trade_no
        self.apply_id = apply_id
        self.bill_record_time = bill_record_time
        self.book_time = book_time
        self.booker_id = booker_id
        self.booker_job_no = booker_job_no
        self.booker_name = booker_name
        self.capital_direction = capital_direction
        self.cascade_department = cascade_department
        self.check_in_date = check_in_date
        self.checkout_date = checkout_date
        self.city = city
        self.city_code = city_code
        self.corp_refund_fee = corp_refund_fee
        self.corp_total_fee = corp_total_fee
        self.cost_center = cost_center
        self.cost_center_number = cost_center_number
        self.department = department
        self.department_id = department_id
        self.fee_type = fee_type
        self.fees = fees
        self.fu_point_fee = fu_point_fee
        self.hotel_name = hotel_name
        self.index = index
        self.invoice_title = invoice_title
        self.is_negotiation = is_negotiation
        self.is_share_str = is_share_str
        self.nights = nights
        self.order_id = order_id
        self.order_price = order_price
        self.order_type = order_type
        self.over_apply_id = over_apply_id
        self.person_refund_fee = person_refund_fee
        self.person_settle_price = person_settle_price
        self.primary_id = primary_id
        self.project_code = project_code
        self.project_name = project_name
        self.promotion_fee = promotion_fee
        self.remark = remark
        self.room_number = room_number
        self.room_price = room_price
        self.room_type = room_type
        self.service_fee = service_fee
        self.settlement_fee = settlement_fee
        self.settlement_grant_fee = settlement_grant_fee
        self.settlement_time = settlement_time
        self.settlement_type = settlement_type
        self.status = status
        self.total_nights = total_nights
        self.traveler_id = traveler_id
        self.traveler_job_no = traveler_job_no
        self.traveler_name = traveler_name
        self.voucher_type = voucher_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alipay_trade_no is not None:
            result['alipay_trade_no'] = self.alipay_trade_no
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.bill_record_time is not None:
            result['bill_record_time'] = self.bill_record_time
        if self.book_time is not None:
            result['book_time'] = self.book_time
        if self.booker_id is not None:
            result['booker_id'] = self.booker_id
        if self.booker_job_no is not None:
            result['booker_job_no'] = self.booker_job_no
        if self.booker_name is not None:
            result['booker_name'] = self.booker_name
        if self.capital_direction is not None:
            result['capital_direction'] = self.capital_direction
        if self.cascade_department is not None:
            result['cascade_department'] = self.cascade_department
        if self.check_in_date is not None:
            result['check_in_date'] = self.check_in_date
        if self.checkout_date is not None:
            result['checkout_date'] = self.checkout_date
        if self.city is not None:
            result['city'] = self.city
        if self.city_code is not None:
            result['city_code'] = self.city_code
        if self.corp_refund_fee is not None:
            result['corp_refund_fee'] = self.corp_refund_fee
        if self.corp_total_fee is not None:
            result['corp_total_fee'] = self.corp_total_fee
        if self.cost_center is not None:
            result['cost_center'] = self.cost_center
        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number
        if self.department is not None:
            result['department'] = self.department
        if self.department_id is not None:
            result['department_id'] = self.department_id
        if self.fee_type is not None:
            result['fee_type'] = self.fee_type
        if self.fees is not None:
            result['fees'] = self.fees
        if self.fu_point_fee is not None:
            result['fu_point_fee'] = self.fu_point_fee
        if self.hotel_name is not None:
            result['hotel_name'] = self.hotel_name
        if self.index is not None:
            result['index'] = self.index
        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title
        if self.is_negotiation is not None:
            result['is_negotiation'] = self.is_negotiation
        if self.is_share_str is not None:
            result['is_share_str'] = self.is_share_str
        if self.nights is not None:
            result['nights'] = self.nights
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.order_price is not None:
            result['order_price'] = self.order_price
        if self.order_type is not None:
            result['order_type'] = self.order_type
        if self.over_apply_id is not None:
            result['over_apply_id'] = self.over_apply_id
        if self.person_refund_fee is not None:
            result['person_refund_fee'] = self.person_refund_fee
        if self.person_settle_price is not None:
            result['person_settle_price'] = self.person_settle_price
        if self.primary_id is not None:
            result['primary_id'] = self.primary_id
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_name is not None:
            result['project_name'] = self.project_name
        if self.promotion_fee is not None:
            result['promotion_fee'] = self.promotion_fee
        if self.remark is not None:
            result['remark'] = self.remark
        if self.room_number is not None:
            result['room_number'] = self.room_number
        if self.room_price is not None:
            result['room_price'] = self.room_price
        if self.room_type is not None:
            result['room_type'] = self.room_type
        if self.service_fee is not None:
            result['service_fee'] = self.service_fee
        if self.settlement_fee is not None:
            result['settlement_fee'] = self.settlement_fee
        if self.settlement_grant_fee is not None:
            result['settlement_grant_fee'] = self.settlement_grant_fee
        if self.settlement_time is not None:
            result['settlement_time'] = self.settlement_time
        if self.settlement_type is not None:
            result['settlement_type'] = self.settlement_type
        if self.status is not None:
            result['status'] = self.status
        if self.total_nights is not None:
            result['total_nights'] = self.total_nights
        if self.traveler_id is not None:
            result['traveler_id'] = self.traveler_id
        if self.traveler_job_no is not None:
            result['traveler_job_no'] = self.traveler_job_no
        if self.traveler_name is not None:
            result['traveler_name'] = self.traveler_name
        if self.voucher_type is not None:
            result['voucher_type'] = self.voucher_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alipay_trade_no') is not None:
            self.alipay_trade_no = m.get('alipay_trade_no')
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('bill_record_time') is not None:
            self.bill_record_time = m.get('bill_record_time')
        if m.get('book_time') is not None:
            self.book_time = m.get('book_time')
        if m.get('booker_id') is not None:
            self.booker_id = m.get('booker_id')
        if m.get('booker_job_no') is not None:
            self.booker_job_no = m.get('booker_job_no')
        if m.get('booker_name') is not None:
            self.booker_name = m.get('booker_name')
        if m.get('capital_direction') is not None:
            self.capital_direction = m.get('capital_direction')
        if m.get('cascade_department') is not None:
            self.cascade_department = m.get('cascade_department')
        if m.get('check_in_date') is not None:
            self.check_in_date = m.get('check_in_date')
        if m.get('checkout_date') is not None:
            self.checkout_date = m.get('checkout_date')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')
        if m.get('corp_refund_fee') is not None:
            self.corp_refund_fee = m.get('corp_refund_fee')
        if m.get('corp_total_fee') is not None:
            self.corp_total_fee = m.get('corp_total_fee')
        if m.get('cost_center') is not None:
            self.cost_center = m.get('cost_center')
        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')
        if m.get('department') is not None:
            self.department = m.get('department')
        if m.get('department_id') is not None:
            self.department_id = m.get('department_id')
        if m.get('fee_type') is not None:
            self.fee_type = m.get('fee_type')
        if m.get('fees') is not None:
            self.fees = m.get('fees')
        if m.get('fu_point_fee') is not None:
            self.fu_point_fee = m.get('fu_point_fee')
        if m.get('hotel_name') is not None:
            self.hotel_name = m.get('hotel_name')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')
        if m.get('is_negotiation') is not None:
            self.is_negotiation = m.get('is_negotiation')
        if m.get('is_share_str') is not None:
            self.is_share_str = m.get('is_share_str')
        if m.get('nights') is not None:
            self.nights = m.get('nights')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('order_price') is not None:
            self.order_price = m.get('order_price')
        if m.get('order_type') is not None:
            self.order_type = m.get('order_type')
        if m.get('over_apply_id') is not None:
            self.over_apply_id = m.get('over_apply_id')
        if m.get('person_refund_fee') is not None:
            self.person_refund_fee = m.get('person_refund_fee')
        if m.get('person_settle_price') is not None:
            self.person_settle_price = m.get('person_settle_price')
        if m.get('primary_id') is not None:
            self.primary_id = m.get('primary_id')
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_name') is not None:
            self.project_name = m.get('project_name')
        if m.get('promotion_fee') is not None:
            self.promotion_fee = m.get('promotion_fee')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('room_number') is not None:
            self.room_number = m.get('room_number')
        if m.get('room_price') is not None:
            self.room_price = m.get('room_price')
        if m.get('room_type') is not None:
            self.room_type = m.get('room_type')
        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')
        if m.get('settlement_fee') is not None:
            self.settlement_fee = m.get('settlement_fee')
        if m.get('settlement_grant_fee') is not None:
            self.settlement_grant_fee = m.get('settlement_grant_fee')
        if m.get('settlement_time') is not None:
            self.settlement_time = m.get('settlement_time')
        if m.get('settlement_type') is not None:
            self.settlement_type = m.get('settlement_type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('total_nights') is not None:
            self.total_nights = m.get('total_nights')
        if m.get('traveler_id') is not None:
            self.traveler_id = m.get('traveler_id')
        if m.get('traveler_job_no') is not None:
            self.traveler_job_no = m.get('traveler_job_no')
        if m.get('traveler_name') is not None:
            self.traveler_name = m.get('traveler_name')
        if m.get('voucher_type') is not None:
            self.voucher_type = m.get('voucher_type')
        return self


class HotelBillSettlementQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        data_list: List[HotelBillSettlementQueryResponseBodyModuleDataList] = None,
        period_end: str = None,
        period_start: str = None,
        total_num: int = None,
    ):
        self.category = category
        self.corp_id = corp_id
        self.data_list = data_list
        self.period_end = period_end
        self.period_start = period_start
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        result['data_list'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['data_list'].append(k.to_map() if k else None)
        if self.period_end is not None:
            result['period_end'] = self.period_end
        if self.period_start is not None:
            result['period_start'] = self.period_start
        if self.total_num is not None:
            result['total_num'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        self.data_list = []
        if m.get('data_list') is not None:
            for k in m.get('data_list'):
                temp_model = HotelBillSettlementQueryResponseBodyModuleDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('period_end') is not None:
            self.period_end = m.get('period_end')
        if m.get('period_start') is not None:
            self.period_start = m.get('period_start')
        if m.get('total_num') is not None:
            self.total_num = m.get('total_num')
        return self


class HotelBillSettlementQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: HotelBillSettlementQueryResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HotelBillSettlementQueryResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class HotelBillSettlementQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HotelBillSettlementQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HotelBillSettlementQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HotelExceedApplyQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class HotelExceedApplyQueryRequest(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
    ):
        self.apply_id = apply_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        return self


class HotelExceedApplyQueryResponseBodyModuleApplyIntentionInfoDo(TeaModel):
    def __init__(
        self,
        check_in: str = None,
        check_out: str = None,
        city_code: str = None,
        city_name: str = None,
        price: int = None,
        together: bool = None,
        type: int = None,
    ):
        self.check_in = check_in
        self.check_out = check_out
        self.city_code = city_code
        self.city_name = city_name
        self.price = price
        self.together = together
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_in is not None:
            result['check_in'] = self.check_in
        if self.check_out is not None:
            result['check_out'] = self.check_out
        if self.city_code is not None:
            result['city_code'] = self.city_code
        if self.city_name is not None:
            result['city_name'] = self.city_name
        if self.price is not None:
            result['price'] = self.price
        if self.together is not None:
            result['together'] = self.together
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_in') is not None:
            self.check_in = m.get('check_in')
        if m.get('check_out') is not None:
            self.check_out = m.get('check_out')
        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')
        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('together') is not None:
            self.together = m.get('together')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class HotelExceedApplyQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        apply_intention_info_do: HotelExceedApplyQueryResponseBodyModuleApplyIntentionInfoDo = None,
        btrip_cause: str = None,
        corp_id: str = None,
        exceed_reason: str = None,
        exceed_type: int = None,
        origin_standard: str = None,
        status: int = None,
        submit_time: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_corp_id: str = None,
        user_id: str = None,
    ):
        self.apply_id = apply_id
        self.apply_intention_info_do = apply_intention_info_do
        self.btrip_cause = btrip_cause
        self.corp_id = corp_id
        self.exceed_reason = exceed_reason
        self.exceed_type = exceed_type
        self.origin_standard = origin_standard
        self.status = status
        self.submit_time = submit_time
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_corp_id = thirdpart_corp_id
        self.user_id = user_id

    def validate(self):
        if self.apply_intention_info_do:
            self.apply_intention_info_do.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.apply_intention_info_do is not None:
            result['apply_intention_info_do'] = self.apply_intention_info_do.to_map()
        if self.btrip_cause is not None:
            result['btrip_cause'] = self.btrip_cause
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.exceed_reason is not None:
            result['exceed_reason'] = self.exceed_reason
        if self.exceed_type is not None:
            result['exceed_type'] = self.exceed_type
        if self.origin_standard is not None:
            result['origin_standard'] = self.origin_standard
        if self.status is not None:
            result['status'] = self.status
        if self.submit_time is not None:
            result['submit_time'] = self.submit_time
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.thirdpart_corp_id is not None:
            result['thirdpart_corp_id'] = self.thirdpart_corp_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('apply_intention_info_do') is not None:
            temp_model = HotelExceedApplyQueryResponseBodyModuleApplyIntentionInfoDo()
            self.apply_intention_info_do = temp_model.from_map(m['apply_intention_info_do'])
        if m.get('btrip_cause') is not None:
            self.btrip_cause = m.get('btrip_cause')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('exceed_reason') is not None:
            self.exceed_reason = m.get('exceed_reason')
        if m.get('exceed_type') is not None:
            self.exceed_type = m.get('exceed_type')
        if m.get('origin_standard') is not None:
            self.origin_standard = m.get('origin_standard')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('submit_time') is not None:
            self.submit_time = m.get('submit_time')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('thirdpart_corp_id') is not None:
            self.thirdpart_corp_id = m.get('thirdpart_corp_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class HotelExceedApplyQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: HotelExceedApplyQueryResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = HotelExceedApplyQueryResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class HotelExceedApplyQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HotelExceedApplyQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HotelExceedApplyQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HotelOrderListQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class HotelOrderListQueryRequest(TeaModel):
    def __init__(
        self,
        all_apply: bool = None,
        apply_id: int = None,
        depart_id: str = None,
        end_time: str = None,
        page: int = None,
        page_size: int = None,
        start_time: str = None,
        thirdpart_apply_id: str = None,
        update_end_time: str = None,
        update_start_time: str = None,
        user_id: str = None,
    ):
        self.all_apply = all_apply
        self.apply_id = apply_id
        self.depart_id = depart_id
        self.end_time = end_time
        self.page = page
        self.page_size = page_size
        self.start_time = start_time
        self.thirdpart_apply_id = thirdpart_apply_id
        self.update_end_time = update_end_time
        self.update_start_time = update_start_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_apply is not None:
            result['all_apply'] = self.all_apply
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.update_end_time is not None:
            result['update_end_time'] = self.update_end_time
        if self.update_start_time is not None:
            result['update_start_time'] = self.update_start_time
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all_apply') is not None:
            self.all_apply = m.get('all_apply')
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('update_end_time') is not None:
            self.update_end_time = m.get('update_end_time')
        if m.get('update_start_time') is not None:
            self.update_start_time = m.get('update_start_time')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class HotelOrderListQueryResponseBodyModuleCostCenter(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        id: int = None,
        name: str = None,
        number: str = None,
    ):
        self.corp_id = corp_id
        self.id = id
        self.name = name
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        return self


class HotelOrderListQueryResponseBodyModuleInvoice(TeaModel):
    def __init__(
        self,
        id: int = None,
        invoice_type: int = None,
        title: str = None,
    ):
        self.id = id
        self.invoice_type = invoice_type
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.invoice_type is not None:
            result['invoice_type'] = self.invoice_type
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('invoice_type') is not None:
            self.invoice_type = m.get('invoice_type')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class HotelOrderListQueryResponseBodyModulePriceInfoList(TeaModel):
    def __init__(
        self,
        category_code: int = None,
        category_type: int = None,
        gmt_create: str = None,
        passenger_name: str = None,
        pay_type: int = None,
        price: float = None,
        trade_id: str = None,
        type: int = None,
    ):
        self.category_code = category_code
        self.category_type = category_type
        self.gmt_create = gmt_create
        self.passenger_name = passenger_name
        self.pay_type = pay_type
        self.price = price
        self.trade_id = trade_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_code is not None:
            result['category_code'] = self.category_code
        if self.category_type is not None:
            result['category_type'] = self.category_type
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name
        if self.pay_type is not None:
            result['pay_type'] = self.pay_type
        if self.price is not None:
            result['price'] = self.price
        if self.trade_id is not None:
            result['trade_id'] = self.trade_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category_code') is not None:
            self.category_code = m.get('category_code')
        if m.get('category_type') is not None:
            self.category_type = m.get('category_type')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')
        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('trade_id') is not None:
            self.trade_id = m.get('trade_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class HotelOrderListQueryResponseBodyModuleUserAffiliateList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class HotelOrderListQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        btrip_title: str = None,
        check_in: str = None,
        check_out: str = None,
        city: str = None,
        contact_name: str = None,
        corp_id: str = None,
        corp_name: str = None,
        cost_center: HotelOrderListQueryResponseBodyModuleCostCenter = None,
        depart_id: str = None,
        depart_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        guest: str = None,
        hotel_name: str = None,
        hotel_support_vat_invoice_type: int = None,
        id: int = None,
        invoice: HotelOrderListQueryResponseBodyModuleInvoice = None,
        night: int = None,
        order_status: int = None,
        order_status_desc: str = None,
        order_type: int = None,
        order_type_desc: str = None,
        price_info_list: List[HotelOrderListQueryResponseBodyModulePriceInfoList] = None,
        project_code: str = None,
        project_id: int = None,
        project_title: str = None,
        room_num: int = None,
        room_type: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_itinerary_id: str = None,
        thirdpart_project_id: str = None,
        user_affiliate_list: List[HotelOrderListQueryResponseBodyModuleUserAffiliateList] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.apply_id = apply_id
        self.btrip_title = btrip_title
        self.check_in = check_in
        self.check_out = check_out
        self.city = city
        self.contact_name = contact_name
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.cost_center = cost_center
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.guest = guest
        self.hotel_name = hotel_name
        self.hotel_support_vat_invoice_type = hotel_support_vat_invoice_type
        self.id = id
        self.invoice = invoice
        self.night = night
        self.order_status = order_status
        self.order_status_desc = order_status_desc
        self.order_type = order_type
        self.order_type_desc = order_type_desc
        self.price_info_list = price_info_list
        self.project_code = project_code
        self.project_id = project_id
        self.project_title = project_title
        self.room_num = room_num
        self.room_type = room_type
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_itinerary_id = thirdpart_itinerary_id
        self.thirdpart_project_id = thirdpart_project_id
        self.user_affiliate_list = user_affiliate_list
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.cost_center:
            self.cost_center.validate()
        if self.invoice:
            self.invoice.validate()
        if self.price_info_list:
            for k in self.price_info_list:
                if k:
                    k.validate()
        if self.user_affiliate_list:
            for k in self.user_affiliate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.btrip_title is not None:
            result['btrip_title'] = self.btrip_title
        if self.check_in is not None:
            result['check_in'] = self.check_in
        if self.check_out is not None:
            result['check_out'] = self.check_out
        if self.city is not None:
            result['city'] = self.city
        if self.contact_name is not None:
            result['contact_name'] = self.contact_name
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.corp_name is not None:
            result['corp_name'] = self.corp_name
        if self.cost_center is not None:
            result['cost_center'] = self.cost_center.to_map()
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.depart_name is not None:
            result['depart_name'] = self.depart_name
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified
        if self.guest is not None:
            result['guest'] = self.guest
        if self.hotel_name is not None:
            result['hotel_name'] = self.hotel_name
        if self.hotel_support_vat_invoice_type is not None:
            result['hotel_support_vat_invoice_type'] = self.hotel_support_vat_invoice_type
        if self.id is not None:
            result['id'] = self.id
        if self.invoice is not None:
            result['invoice'] = self.invoice.to_map()
        if self.night is not None:
            result['night'] = self.night
        if self.order_status is not None:
            result['order_status'] = self.order_status
        if self.order_status_desc is not None:
            result['order_status_desc'] = self.order_status_desc
        if self.order_type is not None:
            result['order_type'] = self.order_type
        if self.order_type_desc is not None:
            result['order_type_desc'] = self.order_type_desc
        result['price_info_list'] = []
        if self.price_info_list is not None:
            for k in self.price_info_list:
                result['price_info_list'].append(k.to_map() if k else None)
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.project_title is not None:
            result['project_title'] = self.project_title
        if self.room_num is not None:
            result['room_num'] = self.room_num
        if self.room_type is not None:
            result['room_type'] = self.room_type
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id
        if self.thirdpart_project_id is not None:
            result['thirdpart_project_id'] = self.thirdpart_project_id
        result['user_affiliate_list'] = []
        if self.user_affiliate_list is not None:
            for k in self.user_affiliate_list:
                result['user_affiliate_list'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('btrip_title') is not None:
            self.btrip_title = m.get('btrip_title')
        if m.get('check_in') is not None:
            self.check_in = m.get('check_in')
        if m.get('check_out') is not None:
            self.check_out = m.get('check_out')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('contact_name') is not None:
            self.contact_name = m.get('contact_name')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')
        if m.get('cost_center') is not None:
            temp_model = HotelOrderListQueryResponseBodyModuleCostCenter()
            self.cost_center = temp_model.from_map(m['cost_center'])
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')
        if m.get('guest') is not None:
            self.guest = m.get('guest')
        if m.get('hotel_name') is not None:
            self.hotel_name = m.get('hotel_name')
        if m.get('hotel_support_vat_invoice_type') is not None:
            self.hotel_support_vat_invoice_type = m.get('hotel_support_vat_invoice_type')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('invoice') is not None:
            temp_model = HotelOrderListQueryResponseBodyModuleInvoice()
            self.invoice = temp_model.from_map(m['invoice'])
        if m.get('night') is not None:
            self.night = m.get('night')
        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')
        if m.get('order_status_desc') is not None:
            self.order_status_desc = m.get('order_status_desc')
        if m.get('order_type') is not None:
            self.order_type = m.get('order_type')
        if m.get('order_type_desc') is not None:
            self.order_type_desc = m.get('order_type_desc')
        self.price_info_list = []
        if m.get('price_info_list') is not None:
            for k in m.get('price_info_list'):
                temp_model = HotelOrderListQueryResponseBodyModulePriceInfoList()
                self.price_info_list.append(temp_model.from_map(k))
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')
        if m.get('room_num') is not None:
            self.room_num = m.get('room_num')
        if m.get('room_type') is not None:
            self.room_type = m.get('room_type')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')
        if m.get('thirdpart_project_id') is not None:
            self.thirdpart_project_id = m.get('thirdpart_project_id')
        self.user_affiliate_list = []
        if m.get('user_affiliate_list') is not None:
            for k in m.get('user_affiliate_list'):
                temp_model = HotelOrderListQueryResponseBodyModuleUserAffiliateList()
                self.user_affiliate_list.append(temp_model.from_map(k))
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class HotelOrderListQueryResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        total_number: int = None,
    ):
        self.page = page
        self.page_size = page_size
        self.total_number = total_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_number is not None:
            result['total_number'] = self.total_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_number') is not None:
            self.total_number = m.get('total_number')
        return self


class HotelOrderListQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: List[HotelOrderListQueryResponseBodyModule] = None,
        page_info: HotelOrderListQueryResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.page_info = page_info
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            for k in self.module:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        result['module'] = []
        if self.module is not None:
            for k in self.module:
                result['module'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
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
        self.module = []
        if m.get('module') is not None:
            for k in m.get('module'):
                temp_model = HotelOrderListQueryResponseBodyModule()
                self.module.append(temp_model.from_map(k))
        if m.get('page_info') is not None:
            temp_model = HotelOrderListQueryResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['page_info'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class HotelOrderListQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HotelOrderListQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = HotelOrderListQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IeFlightBillSettlementQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class IeFlightBillSettlementQueryRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        period_end: str = None,
        period_start: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.period_end = period_end
        self.period_start = period_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['page_no'] = self.page_no
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.period_end is not None:
            result['period_end'] = self.period_end
        if self.period_start is not None:
            result['period_start'] = self.period_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_no') is not None:
            self.page_no = m.get('page_no')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('period_end') is not None:
            self.period_end = m.get('period_end')
        if m.get('period_start') is not None:
            self.period_start = m.get('period_start')
        return self


class IeFlightBillSettlementQueryResponseBodyModuleDataList(TeaModel):
    def __init__(
        self,
        advance_day: int = None,
        airline_corp_code: str = None,
        airline_corp_name: str = None,
        alipay_trade_no: str = None,
        apply_id: str = None,
        arr_airport_code: str = None,
        arr_city: str = None,
        arr_date: str = None,
        arr_station: str = None,
        arr_time: str = None,
        bill_record_time: str = None,
        book_mode: str = None,
        book_time: str = None,
        booker_id: str = None,
        booker_job_no: str = None,
        booker_name: str = None,
        btrip_coupon_fee: float = None,
        cabin: str = None,
        cabin_class: str = None,
        capital_direction: str = None,
        cascade_department: str = None,
        change_fee: float = None,
        corp_pay_order_fee: float = None,
        cost_center: str = None,
        cost_center_number: str = None,
        coupon: float = None,
        dep_airport_code: str = None,
        department: str = None,
        department_id: str = None,
        dept_city: str = None,
        dept_date: str = None,
        dept_station: str = None,
        dept_time: str = None,
        discount: str = None,
        fee_type: str = None,
        flight_no: str = None,
        index: str = None,
        insurance_fee: float = None,
        insurance_number: str = None,
        invoice_title: str = None,
        most_difference_dept_time: str = None,
        most_difference_discount: str = None,
        most_difference_flight_no: str = None,
        most_difference_price: float = None,
        most_difference_reason: str = None,
        most_price: float = None,
        negotiation_coupon_fee: float = None,
        order_id: str = None,
        order_status_desc: str = None,
        over_apply_id: str = None,
        primary_id: int = None,
        project_code: str = None,
        project_name: str = None,
        refund_fee: float = None,
        remark: str = None,
        repeat_refund: str = None,
        seal_price: float = None,
        segment_type: str = None,
        service_fee: float = None,
        settlement_fee: float = None,
        settlement_grant_fee: float = None,
        settlement_time: str = None,
        settlement_type: str = None,
        status: int = None,
        sub_order_id: str = None,
        tax_fee: float = None,
        ticket_id: str = None,
        trade: str = None,
        traveler_id: str = None,
        traveler_job_no: str = None,
        traveler_name: str = None,
        voucher_type: int = None,
    ):
        self.advance_day = advance_day
        self.airline_corp_code = airline_corp_code
        self.airline_corp_name = airline_corp_name
        self.alipay_trade_no = alipay_trade_no
        self.apply_id = apply_id
        self.arr_airport_code = arr_airport_code
        self.arr_city = arr_city
        self.arr_date = arr_date
        self.arr_station = arr_station
        self.arr_time = arr_time
        self.bill_record_time = bill_record_time
        self.book_mode = book_mode
        self.book_time = book_time
        self.booker_id = booker_id
        self.booker_job_no = booker_job_no
        self.booker_name = booker_name
        self.btrip_coupon_fee = btrip_coupon_fee
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.capital_direction = capital_direction
        self.cascade_department = cascade_department
        self.change_fee = change_fee
        self.corp_pay_order_fee = corp_pay_order_fee
        self.cost_center = cost_center
        self.cost_center_number = cost_center_number
        self.coupon = coupon
        self.dep_airport_code = dep_airport_code
        self.department = department
        self.department_id = department_id
        self.dept_city = dept_city
        self.dept_date = dept_date
        self.dept_station = dept_station
        self.dept_time = dept_time
        self.discount = discount
        self.fee_type = fee_type
        self.flight_no = flight_no
        self.index = index
        self.insurance_fee = insurance_fee
        self.insurance_number = insurance_number
        self.invoice_title = invoice_title
        self.most_difference_dept_time = most_difference_dept_time
        self.most_difference_discount = most_difference_discount
        self.most_difference_flight_no = most_difference_flight_no
        self.most_difference_price = most_difference_price
        self.most_difference_reason = most_difference_reason
        self.most_price = most_price
        self.negotiation_coupon_fee = negotiation_coupon_fee
        self.order_id = order_id
        self.order_status_desc = order_status_desc
        self.over_apply_id = over_apply_id
        self.primary_id = primary_id
        self.project_code = project_code
        self.project_name = project_name
        self.refund_fee = refund_fee
        self.remark = remark
        self.repeat_refund = repeat_refund
        self.seal_price = seal_price
        self.segment_type = segment_type
        self.service_fee = service_fee
        self.settlement_fee = settlement_fee
        self.settlement_grant_fee = settlement_grant_fee
        self.settlement_time = settlement_time
        self.settlement_type = settlement_type
        self.status = status
        self.sub_order_id = sub_order_id
        self.tax_fee = tax_fee
        self.ticket_id = ticket_id
        self.trade = trade
        self.traveler_id = traveler_id
        self.traveler_job_no = traveler_job_no
        self.traveler_name = traveler_name
        self.voucher_type = voucher_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advance_day is not None:
            result['advance_day'] = self.advance_day
        if self.airline_corp_code is not None:
            result['airline_corp_code'] = self.airline_corp_code
        if self.airline_corp_name is not None:
            result['airline_corp_name'] = self.airline_corp_name
        if self.alipay_trade_no is not None:
            result['alipay_trade_no'] = self.alipay_trade_no
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.arr_airport_code is not None:
            result['arr_airport_code'] = self.arr_airport_code
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city
        if self.arr_date is not None:
            result['arr_date'] = self.arr_date
        if self.arr_station is not None:
            result['arr_station'] = self.arr_station
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time
        if self.bill_record_time is not None:
            result['bill_record_time'] = self.bill_record_time
        if self.book_mode is not None:
            result['book_mode'] = self.book_mode
        if self.book_time is not None:
            result['book_time'] = self.book_time
        if self.booker_id is not None:
            result['booker_id'] = self.booker_id
        if self.booker_job_no is not None:
            result['booker_job_no'] = self.booker_job_no
        if self.booker_name is not None:
            result['booker_name'] = self.booker_name
        if self.btrip_coupon_fee is not None:
            result['btrip_coupon_fee'] = self.btrip_coupon_fee
        if self.cabin is not None:
            result['cabin'] = self.cabin
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class
        if self.capital_direction is not None:
            result['capital_direction'] = self.capital_direction
        if self.cascade_department is not None:
            result['cascade_department'] = self.cascade_department
        if self.change_fee is not None:
            result['change_fee'] = self.change_fee
        if self.corp_pay_order_fee is not None:
            result['corp_pay_order_fee'] = self.corp_pay_order_fee
        if self.cost_center is not None:
            result['cost_center'] = self.cost_center
        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number
        if self.coupon is not None:
            result['coupon'] = self.coupon
        if self.dep_airport_code is not None:
            result['dep_airport_code'] = self.dep_airport_code
        if self.department is not None:
            result['department'] = self.department
        if self.department_id is not None:
            result['department_id'] = self.department_id
        if self.dept_city is not None:
            result['dept_city'] = self.dept_city
        if self.dept_date is not None:
            result['dept_date'] = self.dept_date
        if self.dept_station is not None:
            result['dept_station'] = self.dept_station
        if self.dept_time is not None:
            result['dept_time'] = self.dept_time
        if self.discount is not None:
            result['discount'] = self.discount
        if self.fee_type is not None:
            result['fee_type'] = self.fee_type
        if self.flight_no is not None:
            result['flight_no'] = self.flight_no
        if self.index is not None:
            result['index'] = self.index
        if self.insurance_fee is not None:
            result['insurance_fee'] = self.insurance_fee
        if self.insurance_number is not None:
            result['insurance_number'] = self.insurance_number
        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title
        if self.most_difference_dept_time is not None:
            result['most_difference_dept_time'] = self.most_difference_dept_time
        if self.most_difference_discount is not None:
            result['most_difference_discount'] = self.most_difference_discount
        if self.most_difference_flight_no is not None:
            result['most_difference_flight_no'] = self.most_difference_flight_no
        if self.most_difference_price is not None:
            result['most_difference_price'] = self.most_difference_price
        if self.most_difference_reason is not None:
            result['most_difference_reason'] = self.most_difference_reason
        if self.most_price is not None:
            result['most_price'] = self.most_price
        if self.negotiation_coupon_fee is not None:
            result['negotiation_coupon_fee'] = self.negotiation_coupon_fee
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.order_status_desc is not None:
            result['order_status_desc'] = self.order_status_desc
        if self.over_apply_id is not None:
            result['over_apply_id'] = self.over_apply_id
        if self.primary_id is not None:
            result['primary_id'] = self.primary_id
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_name is not None:
            result['project_name'] = self.project_name
        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee
        if self.remark is not None:
            result['remark'] = self.remark
        if self.repeat_refund is not None:
            result['repeat_refund'] = self.repeat_refund
        if self.seal_price is not None:
            result['seal_price'] = self.seal_price
        if self.segment_type is not None:
            result['segment_type'] = self.segment_type
        if self.service_fee is not None:
            result['service_fee'] = self.service_fee
        if self.settlement_fee is not None:
            result['settlement_fee'] = self.settlement_fee
        if self.settlement_grant_fee is not None:
            result['settlement_grant_fee'] = self.settlement_grant_fee
        if self.settlement_time is not None:
            result['settlement_time'] = self.settlement_time
        if self.settlement_type is not None:
            result['settlement_type'] = self.settlement_type
        if self.status is not None:
            result['status'] = self.status
        if self.sub_order_id is not None:
            result['sub_order_id'] = self.sub_order_id
        if self.tax_fee is not None:
            result['tax_fee'] = self.tax_fee
        if self.ticket_id is not None:
            result['ticket_id'] = self.ticket_id
        if self.trade is not None:
            result['trade'] = self.trade
        if self.traveler_id is not None:
            result['traveler_id'] = self.traveler_id
        if self.traveler_job_no is not None:
            result['traveler_job_no'] = self.traveler_job_no
        if self.traveler_name is not None:
            result['traveler_name'] = self.traveler_name
        if self.voucher_type is not None:
            result['voucher_type'] = self.voucher_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advance_day') is not None:
            self.advance_day = m.get('advance_day')
        if m.get('airline_corp_code') is not None:
            self.airline_corp_code = m.get('airline_corp_code')
        if m.get('airline_corp_name') is not None:
            self.airline_corp_name = m.get('airline_corp_name')
        if m.get('alipay_trade_no') is not None:
            self.alipay_trade_no = m.get('alipay_trade_no')
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('arr_airport_code') is not None:
            self.arr_airport_code = m.get('arr_airport_code')
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')
        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')
        if m.get('arr_station') is not None:
            self.arr_station = m.get('arr_station')
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')
        if m.get('bill_record_time') is not None:
            self.bill_record_time = m.get('bill_record_time')
        if m.get('book_mode') is not None:
            self.book_mode = m.get('book_mode')
        if m.get('book_time') is not None:
            self.book_time = m.get('book_time')
        if m.get('booker_id') is not None:
            self.booker_id = m.get('booker_id')
        if m.get('booker_job_no') is not None:
            self.booker_job_no = m.get('booker_job_no')
        if m.get('booker_name') is not None:
            self.booker_name = m.get('booker_name')
        if m.get('btrip_coupon_fee') is not None:
            self.btrip_coupon_fee = m.get('btrip_coupon_fee')
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')
        if m.get('capital_direction') is not None:
            self.capital_direction = m.get('capital_direction')
        if m.get('cascade_department') is not None:
            self.cascade_department = m.get('cascade_department')
        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')
        if m.get('corp_pay_order_fee') is not None:
            self.corp_pay_order_fee = m.get('corp_pay_order_fee')
        if m.get('cost_center') is not None:
            self.cost_center = m.get('cost_center')
        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')
        if m.get('coupon') is not None:
            self.coupon = m.get('coupon')
        if m.get('dep_airport_code') is not None:
            self.dep_airport_code = m.get('dep_airport_code')
        if m.get('department') is not None:
            self.department = m.get('department')
        if m.get('department_id') is not None:
            self.department_id = m.get('department_id')
        if m.get('dept_city') is not None:
            self.dept_city = m.get('dept_city')
        if m.get('dept_date') is not None:
            self.dept_date = m.get('dept_date')
        if m.get('dept_station') is not None:
            self.dept_station = m.get('dept_station')
        if m.get('dept_time') is not None:
            self.dept_time = m.get('dept_time')
        if m.get('discount') is not None:
            self.discount = m.get('discount')
        if m.get('fee_type') is not None:
            self.fee_type = m.get('fee_type')
        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('insurance_fee') is not None:
            self.insurance_fee = m.get('insurance_fee')
        if m.get('insurance_number') is not None:
            self.insurance_number = m.get('insurance_number')
        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')
        if m.get('most_difference_dept_time') is not None:
            self.most_difference_dept_time = m.get('most_difference_dept_time')
        if m.get('most_difference_discount') is not None:
            self.most_difference_discount = m.get('most_difference_discount')
        if m.get('most_difference_flight_no') is not None:
            self.most_difference_flight_no = m.get('most_difference_flight_no')
        if m.get('most_difference_price') is not None:
            self.most_difference_price = m.get('most_difference_price')
        if m.get('most_difference_reason') is not None:
            self.most_difference_reason = m.get('most_difference_reason')
        if m.get('most_price') is not None:
            self.most_price = m.get('most_price')
        if m.get('negotiation_coupon_fee') is not None:
            self.negotiation_coupon_fee = m.get('negotiation_coupon_fee')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('order_status_desc') is not None:
            self.order_status_desc = m.get('order_status_desc')
        if m.get('over_apply_id') is not None:
            self.over_apply_id = m.get('over_apply_id')
        if m.get('primary_id') is not None:
            self.primary_id = m.get('primary_id')
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_name') is not None:
            self.project_name = m.get('project_name')
        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('repeat_refund') is not None:
            self.repeat_refund = m.get('repeat_refund')
        if m.get('seal_price') is not None:
            self.seal_price = m.get('seal_price')
        if m.get('segment_type') is not None:
            self.segment_type = m.get('segment_type')
        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')
        if m.get('settlement_fee') is not None:
            self.settlement_fee = m.get('settlement_fee')
        if m.get('settlement_grant_fee') is not None:
            self.settlement_grant_fee = m.get('settlement_grant_fee')
        if m.get('settlement_time') is not None:
            self.settlement_time = m.get('settlement_time')
        if m.get('settlement_type') is not None:
            self.settlement_type = m.get('settlement_type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('sub_order_id') is not None:
            self.sub_order_id = m.get('sub_order_id')
        if m.get('tax_fee') is not None:
            self.tax_fee = m.get('tax_fee')
        if m.get('ticket_id') is not None:
            self.ticket_id = m.get('ticket_id')
        if m.get('trade') is not None:
            self.trade = m.get('trade')
        if m.get('traveler_id') is not None:
            self.traveler_id = m.get('traveler_id')
        if m.get('traveler_job_no') is not None:
            self.traveler_job_no = m.get('traveler_job_no')
        if m.get('traveler_name') is not None:
            self.traveler_name = m.get('traveler_name')
        if m.get('voucher_type') is not None:
            self.voucher_type = m.get('voucher_type')
        return self


class IeFlightBillSettlementQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        data_list: List[IeFlightBillSettlementQueryResponseBodyModuleDataList] = None,
        period_end: str = None,
        period_start: str = None,
        total_num: int = None,
    ):
        self.category = category
        self.corp_id = corp_id
        self.data_list = data_list
        self.period_end = period_end
        self.period_start = period_start
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        result['data_list'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['data_list'].append(k.to_map() if k else None)
        if self.period_end is not None:
            result['period_end'] = self.period_end
        if self.period_start is not None:
            result['period_start'] = self.period_start
        if self.total_num is not None:
            result['total_num'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        self.data_list = []
        if m.get('data_list') is not None:
            for k in m.get('data_list'):
                temp_model = IeFlightBillSettlementQueryResponseBodyModuleDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('period_end') is not None:
            self.period_end = m.get('period_end')
        if m.get('period_start') is not None:
            self.period_start = m.get('period_start')
        if m.get('total_num') is not None:
            self.total_num = m.get('total_num')
        return self


class IeFlightBillSettlementQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: IeFlightBillSettlementQueryResponseBodyModule = None,
        more_page: bool = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.more_page = more_page
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.module is not None:
            result['module'] = self.module.to_map()
        if self.more_page is not None:
            result['more_page'] = self.more_page
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
            temp_model = IeFlightBillSettlementQueryResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('more_page') is not None:
            self.more_page = m.get('more_page')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class IeFlightBillSettlementQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IeFlightBillSettlementQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IeFlightBillSettlementQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvoiceAddHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class InvoiceAddRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        bank_name: str = None,
        bank_no: str = None,
        tax_no: str = None,
        tel: str = None,
        third_part_id: str = None,
        title: str = None,
        type: int = None,
    ):
        self.address = address
        self.bank_name = bank_name
        self.bank_no = bank_no
        self.tax_no = tax_no
        self.tel = tel
        self.third_part_id = third_part_id
        self.title = title
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.bank_name is not None:
            result['bank_name'] = self.bank_name
        if self.bank_no is not None:
            result['bank_no'] = self.bank_no
        if self.tax_no is not None:
            result['tax_no'] = self.tax_no
        if self.tel is not None:
            result['tel'] = self.tel
        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('bank_name') is not None:
            self.bank_name = m.get('bank_name')
        if m.get('bank_no') is not None:
            self.bank_no = m.get('bank_no')
        if m.get('tax_no') is not None:
            self.tax_no = m.get('tax_no')
        if m.get('tel') is not None:
            self.tel = m.get('tel')
        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class InvoiceAddResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
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
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class InvoiceAddResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InvoiceAddResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InvoiceAddResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvoiceDeleteHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class InvoiceDeleteRequest(TeaModel):
    def __init__(
        self,
        third_part_id: str = None,
    ):
        self.third_part_id = third_part_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')
        return self


class InvoiceDeleteResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
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
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class InvoiceDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InvoiceDeleteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InvoiceDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvoiceModifyHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class InvoiceModifyRequest(TeaModel):
    def __init__(
        self,
        address: str = None,
        bank_name: str = None,
        bank_no: str = None,
        tax_no: str = None,
        tel: str = None,
        third_part_id: str = None,
        title: str = None,
        type: int = None,
    ):
        self.address = address
        self.bank_name = bank_name
        self.bank_no = bank_no
        self.tax_no = tax_no
        self.tel = tel
        self.third_part_id = third_part_id
        self.title = title
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address
        if self.bank_name is not None:
            result['bank_name'] = self.bank_name
        if self.bank_no is not None:
            result['bank_no'] = self.bank_no
        if self.tax_no is not None:
            result['tax_no'] = self.tax_no
        if self.tel is not None:
            result['tel'] = self.tel
        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('bank_name') is not None:
            self.bank_name = m.get('bank_name')
        if m.get('bank_no') is not None:
            self.bank_no = m.get('bank_no')
        if m.get('tax_no') is not None:
            self.tax_no = m.get('tax_no')
        if m.get('tel') is not None:
            self.tel = m.get('tel')
        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class InvoiceModifyResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
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
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class InvoiceModifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InvoiceModifyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InvoiceModifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvoiceRuleSaveHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class InvoiceRuleSaveRequestEntities(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: int = None,
    ):
        self.id = id
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class InvoiceRuleSaveRequest(TeaModel):
    def __init__(
        self,
        all_employe: bool = None,
        entities: List[InvoiceRuleSaveRequestEntities] = None,
        third_part_id: str = None,
    ):
        self.all_employe = all_employe
        self.entities = entities
        self.third_part_id = third_part_id

    def validate(self):
        if self.entities:
            for k in self.entities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_employe is not None:
            result['all_employe'] = self.all_employe
        result['entities'] = []
        if self.entities is not None:
            for k in self.entities:
                result['entities'].append(k.to_map() if k else None)
        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all_employe') is not None:
            self.all_employe = m.get('all_employe')
        self.entities = []
        if m.get('entities') is not None:
            for k in m.get('entities'):
                temp_model = InvoiceRuleSaveRequestEntities()
                self.entities.append(temp_model.from_map(k))
        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')
        return self


class InvoiceRuleSaveShrinkRequest(TeaModel):
    def __init__(
        self,
        all_employe: bool = None,
        entities_shrink: str = None,
        third_part_id: str = None,
    ):
        self.all_employe = all_employe
        self.entities_shrink = entities_shrink
        self.third_part_id = third_part_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_employe is not None:
            result['all_employe'] = self.all_employe
        if self.entities_shrink is not None:
            result['entities'] = self.entities_shrink
        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all_employe') is not None:
            self.all_employe = m.get('all_employe')
        if m.get('entities') is not None:
            self.entities_shrink = m.get('entities')
        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')
        return self


class InvoiceRuleSaveResponseBodyModule(TeaModel):
    def __init__(
        self,
        add_num: int = None,
        remove_num: int = None,
    ):
        self.add_num = add_num
        self.remove_num = remove_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_num is not None:
            result['add_num'] = self.add_num
        if self.remove_num is not None:
            result['remove_num'] = self.remove_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('add_num') is not None:
            self.add_num = m.get('add_num')
        if m.get('remove_num') is not None:
            self.remove_num = m.get('remove_num')
        return self


class InvoiceRuleSaveResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: InvoiceRuleSaveResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = InvoiceRuleSaveResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class InvoiceRuleSaveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InvoiceRuleSaveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InvoiceRuleSaveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvoiceSearchHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class InvoiceSearchRequest(TeaModel):
    def __init__(
        self,
        title: str = None,
        user_id: str = None,
    ):
        self.title = title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['title'] = self.title
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class InvoiceSearchResponseBodyModule(TeaModel):
    def __init__(
        self,
        id: int = None,
        third_part_invoice_id: str = None,
        title: str = None,
    ):
        self.id = id
        self.third_part_invoice_id = third_part_invoice_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class InvoiceSearchResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: List[InvoiceSearchResponseBodyModule] = None,
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
            for k in self.module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        result['module'] = []
        if self.module is not None:
            for k in self.module:
                result['module'].append(k.to_map() if k else None)
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
        self.module = []
        if m.get('module') is not None:
            for k in m.get('module'):
                temp_model = InvoiceSearchResponseBodyModule()
                self.module.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class InvoiceSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InvoiceSearchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InvoiceSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IsvUserSaveHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class IsvUserSaveRequestUserList(TeaModel):
    def __init__(
        self,
        depart_id: int = None,
        email: str = None,
        job_no: str = None,
        leave_status: int = None,
        manager_user_id: str = None,
        phone: str = None,
        position: str = None,
        position_level: str = None,
        real_name_en: str = None,
        third_depart_id: str = None,
        third_depart_id_list: List[str] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.depart_id = depart_id
        self.email = email
        self.job_no = job_no
        self.leave_status = leave_status
        self.manager_user_id = manager_user_id
        self.phone = phone
        self.position = position
        self.position_level = position_level
        self.real_name_en = real_name_en
        self.third_depart_id = third_depart_id
        self.third_depart_id_list = third_depart_id_list
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.email is not None:
            result['email'] = self.email
        if self.job_no is not None:
            result['job_no'] = self.job_no
        if self.leave_status is not None:
            result['leave_status'] = self.leave_status
        if self.manager_user_id is not None:
            result['manager_user_id'] = self.manager_user_id
        if self.phone is not None:
            result['phone'] = self.phone
        if self.position is not None:
            result['position'] = self.position
        if self.position_level is not None:
            result['position_level'] = self.position_level
        if self.real_name_en is not None:
            result['real_name_en'] = self.real_name_en
        if self.third_depart_id is not None:
            result['third_depart_id'] = self.third_depart_id
        if self.third_depart_id_list is not None:
            result['third_depart_id_list'] = self.third_depart_id_list
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('job_no') is not None:
            self.job_no = m.get('job_no')
        if m.get('leave_status') is not None:
            self.leave_status = m.get('leave_status')
        if m.get('manager_user_id') is not None:
            self.manager_user_id = m.get('manager_user_id')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('position') is not None:
            self.position = m.get('position')
        if m.get('position_level') is not None:
            self.position_level = m.get('position_level')
        if m.get('real_name_en') is not None:
            self.real_name_en = m.get('real_name_en')
        if m.get('third_depart_id') is not None:
            self.third_depart_id = m.get('third_depart_id')
        if m.get('third_depart_id_list') is not None:
            self.third_depart_id_list = m.get('third_depart_id_list')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class IsvUserSaveRequest(TeaModel):
    def __init__(
        self,
        user_list: List[IsvUserSaveRequestUserList] = None,
    ):
        self.user_list = user_list

    def validate(self):
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['user_list'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['user_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_list = []
        if m.get('user_list') is not None:
            for k in m.get('user_list'):
                temp_model = IsvUserSaveRequestUserList()
                self.user_list.append(temp_model.from_map(k))
        return self


class IsvUserSaveShrinkRequest(TeaModel):
    def __init__(
        self,
        user_list_shrink: str = None,
    ):
        self.user_list_shrink = user_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_list_shrink is not None:
            result['user_list'] = self.user_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_list') is not None:
            self.user_list_shrink = m.get('user_list')
        return self


class IsvUserSaveResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: str = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.module is not None:
            result['module'] = self.module
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
            self.module = m.get('module')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class IsvUserSaveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IsvUserSaveResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IsvUserSaveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MonthBillGetHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class MonthBillGetRequest(TeaModel):
    def __init__(
        self,
        bill_month: str = None,
    ):
        self.bill_month = bill_month

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_month is not None:
            result['bill_month'] = self.bill_month
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bill_month') is not None:
            self.bill_month = m.get('bill_month')
        return self


class MonthBillGetResponseBodyModule(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        start_date: str = None,
        url: str = None,
    ):
        self.end_date = end_date
        self.start_date = start_date
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['end_date'] = self.end_date
        if self.start_date is not None:
            result['start_date'] = self.start_date
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end_date') is not None:
            self.end_date = m.get('end_date')
        if m.get('start_date') is not None:
            self.start_date = m.get('start_date')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class MonthBillGetResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: List[MonthBillGetResponseBodyModule] = None,
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
            for k in self.module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        result['module'] = []
        if self.module is not None:
            for k in self.module:
                result['module'].append(k.to_map() if k else None)
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
        self.module = []
        if m.get('module') is not None:
            for k in m.get('module'):
                temp_model = MonthBillGetResponseBodyModule()
                self.module.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class MonthBillGetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MonthBillGetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MonthBillGetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProjectAddHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class ProjectAddRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        project_name: str = None,
        third_part_cost_center_id: str = None,
        third_part_id: str = None,
        third_part_invoice_id: str = None,
    ):
        self.code = code
        self.project_name = project_name
        self.third_part_cost_center_id = third_part_cost_center_id
        self.third_part_id = third_part_id
        self.third_part_invoice_id = third_part_invoice_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.project_name is not None:
            result['project_name'] = self.project_name
        if self.third_part_cost_center_id is not None:
            result['third_part_cost_center_id'] = self.third_part_cost_center_id
        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id
        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('project_name') is not None:
            self.project_name = m.get('project_name')
        if m.get('third_part_cost_center_id') is not None:
            self.third_part_cost_center_id = m.get('third_part_cost_center_id')
        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')
        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')
        return self


class ProjectAddResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: int = None,
        more_page: bool = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.more_page = more_page
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.module is not None:
            result['module'] = self.module
        if self.more_page is not None:
            result['more_page'] = self.more_page
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
            self.module = m.get('module')
        if m.get('more_page') is not None:
            self.more_page = m.get('more_page')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class ProjectAddResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ProjectAddResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ProjectAddResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProjectDeleteHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class ProjectDeleteRequest(TeaModel):
    def __init__(
        self,
        third_part_id: str = None,
    ):
        self.third_part_id = third_part_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')
        return self


class ProjectDeleteResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: bool = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.module is not None:
            result['module'] = self.module
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
            self.module = m.get('module')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class ProjectDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ProjectDeleteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ProjectDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProjectModifyHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class ProjectModifyRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        project_name: str = None,
        third_part_cost_center_id: str = None,
        third_part_id: str = None,
        third_part_invoice_id: str = None,
    ):
        self.code = code
        self.project_name = project_name
        self.third_part_cost_center_id = third_part_cost_center_id
        self.third_part_id = third_part_id
        self.third_part_invoice_id = third_part_invoice_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.project_name is not None:
            result['project_name'] = self.project_name
        if self.third_part_cost_center_id is not None:
            result['third_part_cost_center_id'] = self.third_part_cost_center_id
        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id
        if self.third_part_invoice_id is not None:
            result['third_part_invoice_id'] = self.third_part_invoice_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('project_name') is not None:
            self.project_name = m.get('project_name')
        if m.get('third_part_cost_center_id') is not None:
            self.third_part_cost_center_id = m.get('third_part_cost_center_id')
        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')
        if m.get('third_part_invoice_id') is not None:
            self.third_part_invoice_id = m.get('third_part_invoice_id')
        return self


class ProjectModifyResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: bool = None,
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
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.module is not None:
            result['module'] = self.module
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
            self.module = m.get('module')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class ProjectModifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ProjectModifyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ProjectModifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TrainBillSettlementQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class TrainBillSettlementQueryRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        period_end: str = None,
        period_start: str = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.period_end = period_end
        self.period_start = period_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['page_no'] = self.page_no
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.period_end is not None:
            result['period_end'] = self.period_end
        if self.period_start is not None:
            result['period_start'] = self.period_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_no') is not None:
            self.page_no = m.get('page_no')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('period_end') is not None:
            self.period_end = m.get('period_end')
        if m.get('period_start') is not None:
            self.period_start = m.get('period_start')
        return self


class TrainBillSettlementQueryResponseBodyModuleDataList(TeaModel):
    def __init__(
        self,
        alipay_trade_no: str = None,
        apply_id: str = None,
        arr_date: str = None,
        arr_station: str = None,
        arr_time: str = None,
        bill_record_time: str = None,
        book_time: str = None,
        booker_id: str = None,
        booker_job_no: str = None,
        booker_name: str = None,
        capital_direction: str = None,
        cascade_department: str = None,
        change_fee: float = None,
        cost_center: str = None,
        cost_center_number: str = None,
        coupon: float = None,
        department: str = None,
        department_id: str = None,
        dept_date: str = None,
        dept_station: str = None,
        dept_time: str = None,
        fee_type: str = None,
        index: str = None,
        invoice_title: str = None,
        order_id: str = None,
        order_price: float = None,
        over_apply_id: str = None,
        primary_id: int = None,
        project_code: str = None,
        project_name: str = None,
        refund_fee: float = None,
        remark: str = None,
        run_time: str = None,
        seat_no: str = None,
        seat_type: str = None,
        service_fee: float = None,
        settlement_fee: float = None,
        settlement_grant_fee: float = None,
        settlement_time: str = None,
        settlement_type: str = None,
        status: int = None,
        ticket_no: str = None,
        ticket_price: float = None,
        train_no: str = None,
        train_type: str = None,
        traveler_id: str = None,
        traveler_job_no: str = None,
        traveler_name: str = None,
        voucher_type: int = None,
    ):
        self.alipay_trade_no = alipay_trade_no
        self.apply_id = apply_id
        self.arr_date = arr_date
        self.arr_station = arr_station
        self.arr_time = arr_time
        self.bill_record_time = bill_record_time
        self.book_time = book_time
        self.booker_id = booker_id
        self.booker_job_no = booker_job_no
        self.booker_name = booker_name
        self.capital_direction = capital_direction
        self.cascade_department = cascade_department
        self.change_fee = change_fee
        self.cost_center = cost_center
        self.cost_center_number = cost_center_number
        self.coupon = coupon
        self.department = department
        self.department_id = department_id
        self.dept_date = dept_date
        self.dept_station = dept_station
        self.dept_time = dept_time
        self.fee_type = fee_type
        self.index = index
        self.invoice_title = invoice_title
        self.order_id = order_id
        self.order_price = order_price
        self.over_apply_id = over_apply_id
        self.primary_id = primary_id
        self.project_code = project_code
        self.project_name = project_name
        self.refund_fee = refund_fee
        self.remark = remark
        self.run_time = run_time
        self.seat_no = seat_no
        self.seat_type = seat_type
        self.service_fee = service_fee
        self.settlement_fee = settlement_fee
        self.settlement_grant_fee = settlement_grant_fee
        self.settlement_time = settlement_time
        self.settlement_type = settlement_type
        self.status = status
        self.ticket_no = ticket_no
        self.ticket_price = ticket_price
        self.train_no = train_no
        self.train_type = train_type
        self.traveler_id = traveler_id
        self.traveler_job_no = traveler_job_no
        self.traveler_name = traveler_name
        self.voucher_type = voucher_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alipay_trade_no is not None:
            result['alipay_trade_no'] = self.alipay_trade_no
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.arr_date is not None:
            result['arr_date'] = self.arr_date
        if self.arr_station is not None:
            result['arr_station'] = self.arr_station
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time
        if self.bill_record_time is not None:
            result['bill_record_time'] = self.bill_record_time
        if self.book_time is not None:
            result['book_time'] = self.book_time
        if self.booker_id is not None:
            result['booker_id'] = self.booker_id
        if self.booker_job_no is not None:
            result['booker_job_no'] = self.booker_job_no
        if self.booker_name is not None:
            result['booker_name'] = self.booker_name
        if self.capital_direction is not None:
            result['capital_direction'] = self.capital_direction
        if self.cascade_department is not None:
            result['cascade_department'] = self.cascade_department
        if self.change_fee is not None:
            result['change_fee'] = self.change_fee
        if self.cost_center is not None:
            result['cost_center'] = self.cost_center
        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number
        if self.coupon is not None:
            result['coupon'] = self.coupon
        if self.department is not None:
            result['department'] = self.department
        if self.department_id is not None:
            result['department_id'] = self.department_id
        if self.dept_date is not None:
            result['dept_date'] = self.dept_date
        if self.dept_station is not None:
            result['dept_station'] = self.dept_station
        if self.dept_time is not None:
            result['dept_time'] = self.dept_time
        if self.fee_type is not None:
            result['fee_type'] = self.fee_type
        if self.index is not None:
            result['index'] = self.index
        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.order_price is not None:
            result['order_price'] = self.order_price
        if self.over_apply_id is not None:
            result['over_apply_id'] = self.over_apply_id
        if self.primary_id is not None:
            result['primary_id'] = self.primary_id
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_name is not None:
            result['project_name'] = self.project_name
        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee
        if self.remark is not None:
            result['remark'] = self.remark
        if self.run_time is not None:
            result['run_time'] = self.run_time
        if self.seat_no is not None:
            result['seat_no'] = self.seat_no
        if self.seat_type is not None:
            result['seat_type'] = self.seat_type
        if self.service_fee is not None:
            result['service_fee'] = self.service_fee
        if self.settlement_fee is not None:
            result['settlement_fee'] = self.settlement_fee
        if self.settlement_grant_fee is not None:
            result['settlement_grant_fee'] = self.settlement_grant_fee
        if self.settlement_time is not None:
            result['settlement_time'] = self.settlement_time
        if self.settlement_type is not None:
            result['settlement_type'] = self.settlement_type
        if self.status is not None:
            result['status'] = self.status
        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no
        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price
        if self.train_no is not None:
            result['train_no'] = self.train_no
        if self.train_type is not None:
            result['train_type'] = self.train_type
        if self.traveler_id is not None:
            result['traveler_id'] = self.traveler_id
        if self.traveler_job_no is not None:
            result['traveler_job_no'] = self.traveler_job_no
        if self.traveler_name is not None:
            result['traveler_name'] = self.traveler_name
        if self.voucher_type is not None:
            result['voucher_type'] = self.voucher_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alipay_trade_no') is not None:
            self.alipay_trade_no = m.get('alipay_trade_no')
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')
        if m.get('arr_station') is not None:
            self.arr_station = m.get('arr_station')
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')
        if m.get('bill_record_time') is not None:
            self.bill_record_time = m.get('bill_record_time')
        if m.get('book_time') is not None:
            self.book_time = m.get('book_time')
        if m.get('booker_id') is not None:
            self.booker_id = m.get('booker_id')
        if m.get('booker_job_no') is not None:
            self.booker_job_no = m.get('booker_job_no')
        if m.get('booker_name') is not None:
            self.booker_name = m.get('booker_name')
        if m.get('capital_direction') is not None:
            self.capital_direction = m.get('capital_direction')
        if m.get('cascade_department') is not None:
            self.cascade_department = m.get('cascade_department')
        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')
        if m.get('cost_center') is not None:
            self.cost_center = m.get('cost_center')
        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')
        if m.get('coupon') is not None:
            self.coupon = m.get('coupon')
        if m.get('department') is not None:
            self.department = m.get('department')
        if m.get('department_id') is not None:
            self.department_id = m.get('department_id')
        if m.get('dept_date') is not None:
            self.dept_date = m.get('dept_date')
        if m.get('dept_station') is not None:
            self.dept_station = m.get('dept_station')
        if m.get('dept_time') is not None:
            self.dept_time = m.get('dept_time')
        if m.get('fee_type') is not None:
            self.fee_type = m.get('fee_type')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('order_price') is not None:
            self.order_price = m.get('order_price')
        if m.get('over_apply_id') is not None:
            self.over_apply_id = m.get('over_apply_id')
        if m.get('primary_id') is not None:
            self.primary_id = m.get('primary_id')
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_name') is not None:
            self.project_name = m.get('project_name')
        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('run_time') is not None:
            self.run_time = m.get('run_time')
        if m.get('seat_no') is not None:
            self.seat_no = m.get('seat_no')
        if m.get('seat_type') is not None:
            self.seat_type = m.get('seat_type')
        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')
        if m.get('settlement_fee') is not None:
            self.settlement_fee = m.get('settlement_fee')
        if m.get('settlement_grant_fee') is not None:
            self.settlement_grant_fee = m.get('settlement_grant_fee')
        if m.get('settlement_time') is not None:
            self.settlement_time = m.get('settlement_time')
        if m.get('settlement_type') is not None:
            self.settlement_type = m.get('settlement_type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')
        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')
        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')
        if m.get('train_type') is not None:
            self.train_type = m.get('train_type')
        if m.get('traveler_id') is not None:
            self.traveler_id = m.get('traveler_id')
        if m.get('traveler_job_no') is not None:
            self.traveler_job_no = m.get('traveler_job_no')
        if m.get('traveler_name') is not None:
            self.traveler_name = m.get('traveler_name')
        if m.get('voucher_type') is not None:
            self.voucher_type = m.get('voucher_type')
        return self


class TrainBillSettlementQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        data_list: List[TrainBillSettlementQueryResponseBodyModuleDataList] = None,
        period_end: str = None,
        period_start: str = None,
        total_num: int = None,
    ):
        self.category = category
        self.corp_id = corp_id
        self.data_list = data_list
        self.period_end = period_end
        self.period_start = period_start
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        result['data_list'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['data_list'].append(k.to_map() if k else None)
        if self.period_end is not None:
            result['period_end'] = self.period_end
        if self.period_start is not None:
            result['period_start'] = self.period_start
        if self.total_num is not None:
            result['total_num'] = self.total_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        self.data_list = []
        if m.get('data_list') is not None:
            for k in m.get('data_list'):
                temp_model = TrainBillSettlementQueryResponseBodyModuleDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('period_end') is not None:
            self.period_end = m.get('period_end')
        if m.get('period_start') is not None:
            self.period_start = m.get('period_start')
        if m.get('total_num') is not None:
            self.total_num = m.get('total_num')
        return self


class TrainBillSettlementQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: TrainBillSettlementQueryResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = TrainBillSettlementQueryResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class TrainBillSettlementQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TrainBillSettlementQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TrainBillSettlementQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TrainExceedApplyQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class TrainExceedApplyQueryRequest(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
    ):
        self.apply_id = apply_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        return self


class TrainExceedApplyQueryResponseBodyModuleApplyIntentionInfoDO(TeaModel):
    def __init__(
        self,
        arr_city: str = None,
        arr_city_name: str = None,
        arr_station: str = None,
        arr_time: str = None,
        dep_city: str = None,
        dep_city_name: str = None,
        dep_station: str = None,
        dep_time: str = None,
        price: int = None,
        seat_name: str = None,
        train_no: str = None,
        train_type_desc: str = None,
        type: int = None,
    ):
        self.arr_city = arr_city
        self.arr_city_name = arr_city_name
        self.arr_station = arr_station
        self.arr_time = arr_time
        self.dep_city = dep_city
        self.dep_city_name = dep_city_name
        self.dep_station = dep_station
        self.dep_time = dep_time
        self.price = price
        self.seat_name = seat_name
        self.train_no = train_no
        self.train_type_desc = train_type_desc
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city
        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name
        if self.arr_station is not None:
            result['arr_station'] = self.arr_station
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time
        if self.dep_city is not None:
            result['dep_city'] = self.dep_city
        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name
        if self.dep_station is not None:
            result['dep_station'] = self.dep_station
        if self.dep_time is not None:
            result['dep_time'] = self.dep_time
        if self.price is not None:
            result['price'] = self.price
        if self.seat_name is not None:
            result['seat_name'] = self.seat_name
        if self.train_no is not None:
            result['train_no'] = self.train_no
        if self.train_type_desc is not None:
            result['train_type_desc'] = self.train_type_desc
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')
        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')
        if m.get('arr_station') is not None:
            self.arr_station = m.get('arr_station')
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')
        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')
        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')
        if m.get('dep_station') is not None:
            self.dep_station = m.get('dep_station')
        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('seat_name') is not None:
            self.seat_name = m.get('seat_name')
        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')
        if m.get('train_type_desc') is not None:
            self.train_type_desc = m.get('train_type_desc')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class TrainExceedApplyQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        apply_intention_info_do: TrainExceedApplyQueryResponseBodyModuleApplyIntentionInfoDO = None,
        btrip_cause: str = None,
        corp_id: str = None,
        exceed_reason: str = None,
        exceed_type: int = None,
        origin_standard: str = None,
        status: int = None,
        submit_time: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_corp_id: str = None,
        user_id: str = None,
    ):
        self.apply_id = apply_id
        self.apply_intention_info_do = apply_intention_info_do
        self.btrip_cause = btrip_cause
        self.corp_id = corp_id
        self.exceed_reason = exceed_reason
        self.exceed_type = exceed_type
        self.origin_standard = origin_standard
        self.status = status
        self.submit_time = submit_time
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_corp_id = thirdpart_corp_id
        self.user_id = user_id

    def validate(self):
        if self.apply_intention_info_do:
            self.apply_intention_info_do.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.apply_intention_info_do is not None:
            result['apply_intention_info_d_o'] = self.apply_intention_info_do.to_map()
        if self.btrip_cause is not None:
            result['btrip_cause'] = self.btrip_cause
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.exceed_reason is not None:
            result['exceed_reason'] = self.exceed_reason
        if self.exceed_type is not None:
            result['exceed_type'] = self.exceed_type
        if self.origin_standard is not None:
            result['origin_standard'] = self.origin_standard
        if self.status is not None:
            result['status'] = self.status
        if self.submit_time is not None:
            result['submit_time'] = self.submit_time
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.thirdpart_corp_id is not None:
            result['thirdpart_corp_id'] = self.thirdpart_corp_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('apply_intention_info_d_o') is not None:
            temp_model = TrainExceedApplyQueryResponseBodyModuleApplyIntentionInfoDO()
            self.apply_intention_info_do = temp_model.from_map(m['apply_intention_info_d_o'])
        if m.get('btrip_cause') is not None:
            self.btrip_cause = m.get('btrip_cause')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('exceed_reason') is not None:
            self.exceed_reason = m.get('exceed_reason')
        if m.get('exceed_type') is not None:
            self.exceed_type = m.get('exceed_type')
        if m.get('origin_standard') is not None:
            self.origin_standard = m.get('origin_standard')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('submit_time') is not None:
            self.submit_time = m.get('submit_time')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('thirdpart_corp_id') is not None:
            self.thirdpart_corp_id = m.get('thirdpart_corp_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class TrainExceedApplyQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: TrainExceedApplyQueryResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = TrainExceedApplyQueryResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class TrainExceedApplyQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TrainExceedApplyQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TrainExceedApplyQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TrainOrderListQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class TrainOrderListQueryRequest(TeaModel):
    def __init__(
        self,
        all_apply: bool = None,
        apply_id: int = None,
        depart_id: str = None,
        end_time: str = None,
        page: int = None,
        page_size: int = None,
        start_time: str = None,
        thirdpart_apply_id: str = None,
        update_end_time: str = None,
        update_start_time: str = None,
        user_id: str = None,
    ):
        self.all_apply = all_apply
        self.apply_id = apply_id
        self.depart_id = depart_id
        self.end_time = end_time
        self.page = page
        self.page_size = page_size
        self.start_time = start_time
        self.thirdpart_apply_id = thirdpart_apply_id
        self.update_end_time = update_end_time
        self.update_start_time = update_start_time
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_apply is not None:
            result['all_apply'] = self.all_apply
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.update_end_time is not None:
            result['update_end_time'] = self.update_end_time
        if self.update_start_time is not None:
            result['update_start_time'] = self.update_start_time
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all_apply') is not None:
            self.all_apply = m.get('all_apply')
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('update_end_time') is not None:
            self.update_end_time = m.get('update_end_time')
        if m.get('update_start_time') is not None:
            self.update_start_time = m.get('update_start_time')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class TrainOrderListQueryResponseBodyModuleCostCenter(TeaModel):
    def __init__(
        self,
        corp_id: str = None,
        id: int = None,
        name: str = None,
        number: str = None,
    ):
        self.corp_id = corp_id
        self.id = id
        self.name = name
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.number is not None:
            result['number'] = self.number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('number') is not None:
            self.number = m.get('number')
        return self


class TrainOrderListQueryResponseBodyModuleInvoice(TeaModel):
    def __init__(
        self,
        id: int = None,
        title: str = None,
    ):
        self.id = id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class TrainOrderListQueryResponseBodyModulePriceInfoList(TeaModel):
    def __init__(
        self,
        category_code: int = None,
        category_type: int = None,
        end_city: str = None,
        end_time: str = None,
        gmt_create: str = None,
        original_train_no: str = None,
        passenger_name: str = None,
        pay_type: int = None,
        price: float = None,
        seat_type: str = None,
        start_city: str = None,
        start_time: str = None,
        trade_id: str = None,
        train_no: str = None,
        type: int = None,
    ):
        self.category_code = category_code
        self.category_type = category_type
        self.end_city = end_city
        self.end_time = end_time
        self.gmt_create = gmt_create
        self.original_train_no = original_train_no
        self.passenger_name = passenger_name
        self.pay_type = pay_type
        self.price = price
        self.seat_type = seat_type
        self.start_city = start_city
        self.start_time = start_time
        self.trade_id = trade_id
        self.train_no = train_no
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_code is not None:
            result['category_code'] = self.category_code
        if self.category_type is not None:
            result['category_type'] = self.category_type
        if self.end_city is not None:
            result['end_city'] = self.end_city
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.original_train_no is not None:
            result['original_train_no'] = self.original_train_no
        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name
        if self.pay_type is not None:
            result['pay_type'] = self.pay_type
        if self.price is not None:
            result['price'] = self.price
        if self.seat_type is not None:
            result['seat_type'] = self.seat_type
        if self.start_city is not None:
            result['start_city'] = self.start_city
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.trade_id is not None:
            result['trade_id'] = self.trade_id
        if self.train_no is not None:
            result['train_no'] = self.train_no
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category_code') is not None:
            self.category_code = m.get('category_code')
        if m.get('category_type') is not None:
            self.category_type = m.get('category_type')
        if m.get('end_city') is not None:
            self.end_city = m.get('end_city')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('original_train_no') is not None:
            self.original_train_no = m.get('original_train_no')
        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')
        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('seat_type') is not None:
            self.seat_type = m.get('seat_type')
        if m.get('start_city') is not None:
            self.start_city = m.get('start_city')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('trade_id') is not None:
            self.trade_id = m.get('trade_id')
        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class TrainOrderListQueryResponseBodyModuleUserAffiliateList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TrainOrderListQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        apply_id: int = None,
        arr_city: str = None,
        arr_station: str = None,
        arr_time: str = None,
        btrip_title: str = None,
        contact_name: str = None,
        corp_id: str = None,
        corp_name: str = None,
        cost_center: TrainOrderListQueryResponseBodyModuleCostCenter = None,
        dep_city: str = None,
        dep_station: str = None,
        dep_time: str = None,
        depart_id: str = None,
        depart_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        invoice: TrainOrderListQueryResponseBodyModuleInvoice = None,
        price_info_list: List[TrainOrderListQueryResponseBodyModulePriceInfoList] = None,
        project_code: str = None,
        project_id: int = None,
        project_title: str = None,
        rider_name: str = None,
        run_time: str = None,
        seat_type: str = None,
        status: int = None,
        third_part_project_id: str = None,
        thirdpart_apply_id: str = None,
        thirdpart_itinerary_id: str = None,
        ticket_count: int = None,
        ticket_no_12306: str = None,
        train_number: str = None,
        train_type: str = None,
        user_affiliate_list: List[TrainOrderListQueryResponseBodyModuleUserAffiliateList] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.apply_id = apply_id
        self.arr_city = arr_city
        self.arr_station = arr_station
        self.arr_time = arr_time
        self.btrip_title = btrip_title
        self.contact_name = contact_name
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.cost_center = cost_center
        self.dep_city = dep_city
        self.dep_station = dep_station
        self.dep_time = dep_time
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.invoice = invoice
        self.price_info_list = price_info_list
        self.project_code = project_code
        self.project_id = project_id
        self.project_title = project_title
        self.rider_name = rider_name
        self.run_time = run_time
        self.seat_type = seat_type
        self.status = status
        self.third_part_project_id = third_part_project_id
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_itinerary_id = thirdpart_itinerary_id
        self.ticket_count = ticket_count
        self.ticket_no_12306 = ticket_no_12306
        self.train_number = train_number
        self.train_type = train_type
        self.user_affiliate_list = user_affiliate_list
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.cost_center:
            self.cost_center.validate()
        if self.invoice:
            self.invoice.validate()
        if self.price_info_list:
            for k in self.price_info_list:
                if k:
                    k.validate()
        if self.user_affiliate_list:
            for k in self.user_affiliate_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city
        if self.arr_station is not None:
            result['arr_station'] = self.arr_station
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time
        if self.btrip_title is not None:
            result['btrip_title'] = self.btrip_title
        if self.contact_name is not None:
            result['contact_name'] = self.contact_name
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.corp_name is not None:
            result['corp_name'] = self.corp_name
        if self.cost_center is not None:
            result['cost_center'] = self.cost_center.to_map()
        if self.dep_city is not None:
            result['dep_city'] = self.dep_city
        if self.dep_station is not None:
            result['dep_station'] = self.dep_station
        if self.dep_time is not None:
            result['dep_time'] = self.dep_time
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.depart_name is not None:
            result['depart_name'] = self.depart_name
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.invoice is not None:
            result['invoice'] = self.invoice.to_map()
        result['price_info_list'] = []
        if self.price_info_list is not None:
            for k in self.price_info_list:
                result['price_info_list'].append(k.to_map() if k else None)
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.project_title is not None:
            result['project_title'] = self.project_title
        if self.rider_name is not None:
            result['rider_name'] = self.rider_name
        if self.run_time is not None:
            result['run_time'] = self.run_time
        if self.seat_type is not None:
            result['seat_type'] = self.seat_type
        if self.status is not None:
            result['status'] = self.status
        if self.third_part_project_id is not None:
            result['third_part_project_id'] = self.third_part_project_id
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id
        if self.ticket_count is not None:
            result['ticket_count'] = self.ticket_count
        if self.ticket_no_12306 is not None:
            result['ticket_no12306'] = self.ticket_no_12306
        if self.train_number is not None:
            result['train_number'] = self.train_number
        if self.train_type is not None:
            result['train_type'] = self.train_type
        result['user_affiliate_list'] = []
        if self.user_affiliate_list is not None:
            for k in self.user_affiliate_list:
                result['user_affiliate_list'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')
        if m.get('arr_station') is not None:
            self.arr_station = m.get('arr_station')
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')
        if m.get('btrip_title') is not None:
            self.btrip_title = m.get('btrip_title')
        if m.get('contact_name') is not None:
            self.contact_name = m.get('contact_name')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')
        if m.get('cost_center') is not None:
            temp_model = TrainOrderListQueryResponseBodyModuleCostCenter()
            self.cost_center = temp_model.from_map(m['cost_center'])
        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')
        if m.get('dep_station') is not None:
            self.dep_station = m.get('dep_station')
        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('invoice') is not None:
            temp_model = TrainOrderListQueryResponseBodyModuleInvoice()
            self.invoice = temp_model.from_map(m['invoice'])
        self.price_info_list = []
        if m.get('price_info_list') is not None:
            for k in m.get('price_info_list'):
                temp_model = TrainOrderListQueryResponseBodyModulePriceInfoList()
                self.price_info_list.append(temp_model.from_map(k))
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')
        if m.get('rider_name') is not None:
            self.rider_name = m.get('rider_name')
        if m.get('run_time') is not None:
            self.run_time = m.get('run_time')
        if m.get('seat_type') is not None:
            self.seat_type = m.get('seat_type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('third_part_project_id') is not None:
            self.third_part_project_id = m.get('third_part_project_id')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')
        if m.get('ticket_count') is not None:
            self.ticket_count = m.get('ticket_count')
        if m.get('ticket_no12306') is not None:
            self.ticket_no_12306 = m.get('ticket_no12306')
        if m.get('train_number') is not None:
            self.train_number = m.get('train_number')
        if m.get('train_type') is not None:
            self.train_type = m.get('train_type')
        self.user_affiliate_list = []
        if m.get('user_affiliate_list') is not None:
            for k in m.get('user_affiliate_list'):
                temp_model = TrainOrderListQueryResponseBodyModuleUserAffiliateList()
                self.user_affiliate_list.append(temp_model.from_map(k))
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class TrainOrderListQueryResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        total_number: int = None,
    ):
        self.page = page
        self.page_size = page_size
        self.total_number = total_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_number is not None:
            result['total_number'] = self.total_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_number') is not None:
            self.total_number = m.get('total_number')
        return self


class TrainOrderListQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: List[TrainOrderListQueryResponseBodyModule] = None,
        page_info: TrainOrderListQueryResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.page_info = page_info
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            for k in self.module:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        result['module'] = []
        if self.module is not None:
            for k in self.module:
                result['module'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
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
        self.module = []
        if m.get('module') is not None:
            for k in m.get('module'):
                temp_model = TrainOrderListQueryResponseBodyModule()
                self.module.append(temp_model.from_map(k))
        if m.get('page_info') is not None:
            temp_model = TrainOrderListQueryResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['page_info'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class TrainOrderListQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TrainOrderListQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TrainOrderListQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TrainOrderQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class TrainOrderQueryRequest(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        user_id: str = None,
    ):
        self.order_id = order_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class TrainOrderQueryResponseBodyModuleChangeTicketInfoList(TeaModel):
    def __init__(
        self,
        change_coach_no: str = None,
        change_gap_fee: float = None,
        change_handling_fee: float = None,
        change_seat_no: str = None,
        change_seat_type_name: str = None,
        change_service_fee: float = None,
        change_train_no: str = None,
        change_train_type_name: str = None,
        check_in_time: str = None,
        check_out_time: str = None,
        end_time: str = None,
        from_station_name: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        origin_ticket_no: str = None,
        out_ticket_status: str = None,
        start_time: str = None,
        ticket_no: str = None,
        to_station_name: str = None,
    ):
        self.change_coach_no = change_coach_no
        self.change_gap_fee = change_gap_fee
        self.change_handling_fee = change_handling_fee
        self.change_seat_no = change_seat_no
        self.change_seat_type_name = change_seat_type_name
        self.change_service_fee = change_service_fee
        self.change_train_no = change_train_no
        self.change_train_type_name = change_train_type_name
        self.check_in_time = check_in_time
        self.check_out_time = check_out_time
        self.end_time = end_time
        self.from_station_name = from_station_name
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.origin_ticket_no = origin_ticket_no
        self.out_ticket_status = out_ticket_status
        self.start_time = start_time
        self.ticket_no = ticket_no
        self.to_station_name = to_station_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_coach_no is not None:
            result['change_coach_no'] = self.change_coach_no
        if self.change_gap_fee is not None:
            result['change_gap_fee'] = self.change_gap_fee
        if self.change_handling_fee is not None:
            result['change_handling_fee'] = self.change_handling_fee
        if self.change_seat_no is not None:
            result['change_seat_no'] = self.change_seat_no
        if self.change_seat_type_name is not None:
            result['change_seat_type_name'] = self.change_seat_type_name
        if self.change_service_fee is not None:
            result['change_service_fee'] = self.change_service_fee
        if self.change_train_no is not None:
            result['change_train_no'] = self.change_train_no
        if self.change_train_type_name is not None:
            result['change_train_type_name'] = self.change_train_type_name
        if self.check_in_time is not None:
            result['check_in_time'] = self.check_in_time
        if self.check_out_time is not None:
            result['check_out_time'] = self.check_out_time
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.from_station_name is not None:
            result['from_station_name'] = self.from_station_name
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify
        if self.origin_ticket_no is not None:
            result['origin_ticket_no'] = self.origin_ticket_no
        if self.out_ticket_status is not None:
            result['out_ticket_status'] = self.out_ticket_status
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no
        if self.to_station_name is not None:
            result['to_station_name'] = self.to_station_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_coach_no') is not None:
            self.change_coach_no = m.get('change_coach_no')
        if m.get('change_gap_fee') is not None:
            self.change_gap_fee = m.get('change_gap_fee')
        if m.get('change_handling_fee') is not None:
            self.change_handling_fee = m.get('change_handling_fee')
        if m.get('change_seat_no') is not None:
            self.change_seat_no = m.get('change_seat_no')
        if m.get('change_seat_type_name') is not None:
            self.change_seat_type_name = m.get('change_seat_type_name')
        if m.get('change_service_fee') is not None:
            self.change_service_fee = m.get('change_service_fee')
        if m.get('change_train_no') is not None:
            self.change_train_no = m.get('change_train_no')
        if m.get('change_train_type_name') is not None:
            self.change_train_type_name = m.get('change_train_type_name')
        if m.get('check_in_time') is not None:
            self.check_in_time = m.get('check_in_time')
        if m.get('check_out_time') is not None:
            self.check_out_time = m.get('check_out_time')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('from_station_name') is not None:
            self.from_station_name = m.get('from_station_name')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')
        if m.get('origin_ticket_no') is not None:
            self.origin_ticket_no = m.get('origin_ticket_no')
        if m.get('out_ticket_status') is not None:
            self.out_ticket_status = m.get('out_ticket_status')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')
        if m.get('to_station_name') is not None:
            self.to_station_name = m.get('to_station_name')
        return self


class TrainOrderQueryResponseBodyModuleInvoiceInfo(TeaModel):
    def __init__(
        self,
        id: int = None,
        title: str = None,
    ):
        self.id = id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class TrainOrderQueryResponseBodyModuleOrderBaseInfo(TeaModel):
    def __init__(
        self,
        apply_id: str = None,
        btrip_title: str = None,
        contact_name: str = None,
        corp_id: str = None,
        corp_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        itinerary_id: str = None,
        order_id: int = None,
        order_status: int = None,
        thirdpart_apply_id: str = None,
        thirdpart_corp_id: str = None,
        thirdpart_itinerary_id: str = None,
        trip_type: int = None,
        user_id: str = None,
    ):
        self.apply_id = apply_id
        self.btrip_title = btrip_title
        self.contact_name = contact_name
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.itinerary_id = itinerary_id
        self.order_id = order_id
        self.order_status = order_status
        self.thirdpart_apply_id = thirdpart_apply_id
        self.thirdpart_corp_id = thirdpart_corp_id
        self.thirdpart_itinerary_id = thirdpart_itinerary_id
        self.trip_type = trip_type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id
        if self.btrip_title is not None:
            result['btrip_title'] = self.btrip_title
        if self.contact_name is not None:
            result['contact_name'] = self.contact_name
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id
        if self.corp_name is not None:
            result['corp_name'] = self.corp_name
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id
        if self.depart_name is not None:
            result['depart_name'] = self.depart_name
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify
        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.order_status is not None:
            result['order_status'] = self.order_status
        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id
        if self.thirdpart_corp_id is not None:
            result['thirdpart_corp_id'] = self.thirdpart_corp_id
        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id
        if self.trip_type is not None:
            result['trip_type'] = self.trip_type
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')
        if m.get('btrip_title') is not None:
            self.btrip_title = m.get('btrip_title')
        if m.get('contact_name') is not None:
            self.contact_name = m.get('contact_name')
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')
        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')
        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')
        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')
        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')
        if m.get('thirdpart_corp_id') is not None:
            self.thirdpart_corp_id = m.get('thirdpart_corp_id')
        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')
        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class TrainOrderQueryResponseBodyModulePassengerInfoList(TeaModel):
    def __init__(
        self,
        cost_center_id: int = None,
        cost_center_name: str = None,
        cost_center_number: str = None,
        project_code: str = None,
        project_id: int = None,
        project_title: str = None,
        thirdpart_project_id: str = None,
        user_id: str = None,
        user_name: str = None,
        user_type: int = None,
    ):
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.cost_center_number = cost_center_number
        self.project_code = project_code
        self.project_id = project_id
        self.project_title = project_title
        self.thirdpart_project_id = thirdpart_project_id
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id
        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name
        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number
        if self.project_code is not None:
            result['project_code'] = self.project_code
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.project_title is not None:
            result['project_title'] = self.project_title
        if self.thirdpart_project_id is not None:
            result['thirdpart_project_id'] = self.thirdpart_project_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        if self.user_type is not None:
            result['user_type'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')
        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')
        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')
        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')
        if m.get('thirdpart_project_id') is not None:
            self.thirdpart_project_id = m.get('thirdpart_project_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')
        return self


class TrainOrderQueryResponseBodyModulePriceInfoList(TeaModel):
    def __init__(
        self,
        category_code: int = None,
        gmt_create: str = None,
        passenger_name: str = None,
        pay_type: int = None,
        price: float = None,
        trade_id: str = None,
        type: int = None,
    ):
        self.category_code = category_code
        self.gmt_create = gmt_create
        self.passenger_name = passenger_name
        self.pay_type = pay_type
        self.price = price
        self.trade_id = trade_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_code is not None:
            result['category_code'] = self.category_code
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name
        if self.pay_type is not None:
            result['pay_type'] = self.pay_type
        if self.price is not None:
            result['price'] = self.price
        if self.trade_id is not None:
            result['trade_id'] = self.trade_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category_code') is not None:
            self.category_code = m.get('category_code')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')
        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')
        if m.get('price') is not None:
            self.price = m.get('price')
        if m.get('trade_id') is not None:
            self.trade_id = m.get('trade_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class TrainOrderQueryResponseBodyModuleRefundTicketInfoList(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modify: str = None,
        refund_fee: float = None,
        refund_service_fee: float = None,
        ticket_no: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.refund_fee = refund_fee
        self.refund_service_fee = refund_service_fee
        self.ticket_no = ticket_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify
        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee
        if self.refund_service_fee is not None:
            result['refund_service_fee'] = self.refund_service_fee
        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')
        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')
        if m.get('refund_service_fee') is not None:
            self.refund_service_fee = m.get('refund_service_fee')
        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')
        return self


class TrainOrderQueryResponseBodyModuleTicketInfoList(TeaModel):
    def __init__(
        self,
        changed: bool = None,
        check_in_time: str = None,
        check_out_time: str = None,
        coach_no: str = None,
        end_time: str = None,
        gmt_create: str = None,
        gmt_modify: str = None,
        out_ticket_status: str = None,
        pay_type: int = None,
        seat_no: str = None,
        seat_type_name: str = None,
        service_fee: float = None,
        start_time: str = None,
        ticket_no: str = None,
        ticket_price: float = None,
        ticket_status: int = None,
        train_type_name: str = None,
        user_id: str = None,
    ):
        self.changed = changed
        self.check_in_time = check_in_time
        self.check_out_time = check_out_time
        self.coach_no = coach_no
        self.end_time = end_time
        self.gmt_create = gmt_create
        self.gmt_modify = gmt_modify
        self.out_ticket_status = out_ticket_status
        self.pay_type = pay_type
        self.seat_no = seat_no
        self.seat_type_name = seat_type_name
        self.service_fee = service_fee
        self.start_time = start_time
        self.ticket_no = ticket_no
        self.ticket_price = ticket_price
        self.ticket_status = ticket_status
        self.train_type_name = train_type_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.changed is not None:
            result['changed'] = self.changed
        if self.check_in_time is not None:
            result['check_in_time'] = self.check_in_time
        if self.check_out_time is not None:
            result['check_out_time'] = self.check_out_time
        if self.coach_no is not None:
            result['coach_no'] = self.coach_no
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create
        if self.gmt_modify is not None:
            result['gmt_modify'] = self.gmt_modify
        if self.out_ticket_status is not None:
            result['out_ticket_status'] = self.out_ticket_status
        if self.pay_type is not None:
            result['pay_type'] = self.pay_type
        if self.seat_no is not None:
            result['seat_no'] = self.seat_no
        if self.seat_type_name is not None:
            result['seat_type_name'] = self.seat_type_name
        if self.service_fee is not None:
            result['service_fee'] = self.service_fee
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no
        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price
        if self.ticket_status is not None:
            result['ticket_status'] = self.ticket_status
        if self.train_type_name is not None:
            result['train_type_name'] = self.train_type_name
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('changed') is not None:
            self.changed = m.get('changed')
        if m.get('check_in_time') is not None:
            self.check_in_time = m.get('check_in_time')
        if m.get('check_out_time') is not None:
            self.check_out_time = m.get('check_out_time')
        if m.get('coach_no') is not None:
            self.coach_no = m.get('coach_no')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')
        if m.get('gmt_modify') is not None:
            self.gmt_modify = m.get('gmt_modify')
        if m.get('out_ticket_status') is not None:
            self.out_ticket_status = m.get('out_ticket_status')
        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')
        if m.get('seat_no') is not None:
            self.seat_no = m.get('seat_no')
        if m.get('seat_type_name') is not None:
            self.seat_type_name = m.get('seat_type_name')
        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')
        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')
        if m.get('ticket_status') is not None:
            self.ticket_status = m.get('ticket_status')
        if m.get('train_type_name') is not None:
            self.train_type_name = m.get('train_type_name')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class TrainOrderQueryResponseBodyModuleTrainInfo(TeaModel):
    def __init__(
        self,
        arr_time: str = None,
        dep_time: str = None,
        from_station_name: str = None,
        run_time: int = None,
        to_station_name: str = None,
        train_no: str = None,
    ):
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.from_station_name = from_station_name
        self.run_time = run_time
        self.to_station_name = to_station_name
        self.train_no = train_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time
        if self.dep_time is not None:
            result['dep_time'] = self.dep_time
        if self.from_station_name is not None:
            result['from_station_name'] = self.from_station_name
        if self.run_time is not None:
            result['run_time'] = self.run_time
        if self.to_station_name is not None:
            result['to_station_name'] = self.to_station_name
        if self.train_no is not None:
            result['train_no'] = self.train_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')
        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')
        if m.get('from_station_name') is not None:
            self.from_station_name = m.get('from_station_name')
        if m.get('run_time') is not None:
            self.run_time = m.get('run_time')
        if m.get('to_station_name') is not None:
            self.to_station_name = m.get('to_station_name')
        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')
        return self


class TrainOrderQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        change_ticket_info_list: List[TrainOrderQueryResponseBodyModuleChangeTicketInfoList] = None,
        invoice_info: TrainOrderQueryResponseBodyModuleInvoiceInfo = None,
        order_base_info: TrainOrderQueryResponseBodyModuleOrderBaseInfo = None,
        passenger_info_list: List[TrainOrderQueryResponseBodyModulePassengerInfoList] = None,
        price_info_list: List[TrainOrderQueryResponseBodyModulePriceInfoList] = None,
        refund_ticket_info_list: List[TrainOrderQueryResponseBodyModuleRefundTicketInfoList] = None,
        ticket_info_list: List[TrainOrderQueryResponseBodyModuleTicketInfoList] = None,
        train_info: TrainOrderQueryResponseBodyModuleTrainInfo = None,
    ):
        self.change_ticket_info_list = change_ticket_info_list
        self.invoice_info = invoice_info
        self.order_base_info = order_base_info
        self.passenger_info_list = passenger_info_list
        self.price_info_list = price_info_list
        self.refund_ticket_info_list = refund_ticket_info_list
        self.ticket_info_list = ticket_info_list
        self.train_info = train_info

    def validate(self):
        if self.change_ticket_info_list:
            for k in self.change_ticket_info_list:
                if k:
                    k.validate()
        if self.invoice_info:
            self.invoice_info.validate()
        if self.order_base_info:
            self.order_base_info.validate()
        if self.passenger_info_list:
            for k in self.passenger_info_list:
                if k:
                    k.validate()
        if self.price_info_list:
            for k in self.price_info_list:
                if k:
                    k.validate()
        if self.refund_ticket_info_list:
            for k in self.refund_ticket_info_list:
                if k:
                    k.validate()
        if self.ticket_info_list:
            for k in self.ticket_info_list:
                if k:
                    k.validate()
        if self.train_info:
            self.train_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['change_ticket_info_list'] = []
        if self.change_ticket_info_list is not None:
            for k in self.change_ticket_info_list:
                result['change_ticket_info_list'].append(k.to_map() if k else None)
        if self.invoice_info is not None:
            result['invoice_info'] = self.invoice_info.to_map()
        if self.order_base_info is not None:
            result['order_base_info'] = self.order_base_info.to_map()
        result['passenger_info_list'] = []
        if self.passenger_info_list is not None:
            for k in self.passenger_info_list:
                result['passenger_info_list'].append(k.to_map() if k else None)
        result['price_info_list'] = []
        if self.price_info_list is not None:
            for k in self.price_info_list:
                result['price_info_list'].append(k.to_map() if k else None)
        result['refund_ticket_info_list'] = []
        if self.refund_ticket_info_list is not None:
            for k in self.refund_ticket_info_list:
                result['refund_ticket_info_list'].append(k.to_map() if k else None)
        result['ticket_info_list'] = []
        if self.ticket_info_list is not None:
            for k in self.ticket_info_list:
                result['ticket_info_list'].append(k.to_map() if k else None)
        if self.train_info is not None:
            result['train_info'] = self.train_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_ticket_info_list = []
        if m.get('change_ticket_info_list') is not None:
            for k in m.get('change_ticket_info_list'):
                temp_model = TrainOrderQueryResponseBodyModuleChangeTicketInfoList()
                self.change_ticket_info_list.append(temp_model.from_map(k))
        if m.get('invoice_info') is not None:
            temp_model = TrainOrderQueryResponseBodyModuleInvoiceInfo()
            self.invoice_info = temp_model.from_map(m['invoice_info'])
        if m.get('order_base_info') is not None:
            temp_model = TrainOrderQueryResponseBodyModuleOrderBaseInfo()
            self.order_base_info = temp_model.from_map(m['order_base_info'])
        self.passenger_info_list = []
        if m.get('passenger_info_list') is not None:
            for k in m.get('passenger_info_list'):
                temp_model = TrainOrderQueryResponseBodyModulePassengerInfoList()
                self.passenger_info_list.append(temp_model.from_map(k))
        self.price_info_list = []
        if m.get('price_info_list') is not None:
            for k in m.get('price_info_list'):
                temp_model = TrainOrderQueryResponseBodyModulePriceInfoList()
                self.price_info_list.append(temp_model.from_map(k))
        self.refund_ticket_info_list = []
        if m.get('refund_ticket_info_list') is not None:
            for k in m.get('refund_ticket_info_list'):
                temp_model = TrainOrderQueryResponseBodyModuleRefundTicketInfoList()
                self.refund_ticket_info_list.append(temp_model.from_map(k))
        self.ticket_info_list = []
        if m.get('ticket_info_list') is not None:
            for k in m.get('ticket_info_list'):
                temp_model = TrainOrderQueryResponseBodyModuleTicketInfoList()
                self.ticket_info_list.append(temp_model.from_map(k))
        if m.get('train_info') is not None:
            temp_model = TrainOrderQueryResponseBodyModuleTrainInfo()
            self.train_info = temp_model.from_map(m['train_info'])
        return self


class TrainOrderQueryResponseBody(TeaModel):
    def __init__(
        self,
        module: TrainOrderQueryResponseBodyModule = None,
        request_id: str = None,
        result_code: int = None,
        result_msg: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.module = module
        self.request_id = request_id
        self.result_code = result_code
        self.result_msg = result_msg
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['module'] = self.module.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result_code is not None:
            result['result_code'] = self.result_code
        if self.result_msg is not None:
            result['result_msg'] = self.result_msg
        if self.success is not None:
            result['success'] = self.success
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('module') is not None:
            temp_model = TrainOrderQueryResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result_code') is not None:
            self.result_code = m.get('result_code')
        if m.get('result_msg') is not None:
            self.result_msg = m.get('result_msg')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class TrainOrderQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TrainOrderQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TrainOrderQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TrainStationSearchHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class TrainStationSearchRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
    ):
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        return self


class TrainStationSearchResponseBodyModuleCities(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class TrainStationSearchResponseBodyModule(TeaModel):
    def __init__(
        self,
        cities: List[TrainStationSearchResponseBodyModuleCities] = None,
    ):
        self.cities = cities

    def validate(self):
        if self.cities:
            for k in self.cities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['cities'] = []
        if self.cities is not None:
            for k in self.cities:
                result['cities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cities = []
        if m.get('cities') is not None:
            for k in m.get('cities'):
                temp_model = TrainStationSearchResponseBodyModuleCities()
                self.cities.append(temp_model.from_map(k))
        return self


class TrainStationSearchResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: TrainStationSearchResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = TrainStationSearchResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class TrainStationSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TrainStationSearchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TrainStationSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UserQueryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_btrip_so_corp_token: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_btrip_so_corp_token = x_acs_btrip_so_corp_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_btrip_so_corp_token is not None:
            result['x-acs-btrip-so-corp-token'] = self.x_acs_btrip_so_corp_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-btrip-so-corp-token') is not None:
            self.x_acs_btrip_so_corp_token = m.get('x-acs-btrip-so-corp-token')
        return self


class UserQueryRequest(TeaModel):
    def __init__(
        self,
        modified_time_greater_or_equal_than: str = None,
        page_size: int = None,
        page_token: str = None,
        third_part_job_no: str = None,
    ):
        self.modified_time_greater_or_equal_than = modified_time_greater_or_equal_than
        self.page_size = page_size
        self.page_token = page_token
        self.third_part_job_no = third_part_job_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modified_time_greater_or_equal_than is not None:
            result['modified_time_greater_or_equal_than'] = self.modified_time_greater_or_equal_than
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.page_token is not None:
            result['page_token'] = self.page_token
        if self.third_part_job_no is not None:
            result['third_part_job_no'] = self.third_part_job_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modified_time_greater_or_equal_than') is not None:
            self.modified_time_greater_or_equal_than = m.get('modified_time_greater_or_equal_than')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('page_token') is not None:
            self.page_token = m.get('page_token')
        if m.get('third_part_job_no') is not None:
            self.third_part_job_no = m.get('third_part_job_no')
        return self


class UserQueryResponseBodyModuleItems(TeaModel):
    def __init__(
        self,
        employee_nick: str = None,
        third_part_employee_id: str = None,
        third_part_job_no: str = None,
    ):
        self.employee_nick = employee_nick
        self.third_part_employee_id = third_part_employee_id
        self.third_part_job_no = third_part_job_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.employee_nick is not None:
            result['employee_nick'] = self.employee_nick
        if self.third_part_employee_id is not None:
            result['third_part_employee_id'] = self.third_part_employee_id
        if self.third_part_job_no is not None:
            result['third_part_job_no'] = self.third_part_job_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('employee_nick') is not None:
            self.employee_nick = m.get('employee_nick')
        if m.get('third_part_employee_id') is not None:
            self.third_part_employee_id = m.get('third_part_employee_id')
        if m.get('third_part_job_no') is not None:
            self.third_part_job_no = m.get('third_part_job_no')
        return self


class UserQueryResponseBodyModule(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        items: List[UserQueryResponseBodyModuleItems] = None,
        page_token: str = None,
        total: int = None,
    ):
        self.has_more = has_more
        self.items = items
        self.page_token = page_token
        self.total = total

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['has_more'] = self.has_more
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.page_token is not None:
            result['page_token'] = self.page_token
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('has_more') is not None:
            self.has_more = m.get('has_more')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = UserQueryResponseBodyModuleItems()
                self.items.append(temp_model.from_map(k))
        if m.get('page_token') is not None:
            self.page_token = m.get('page_token')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class UserQueryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: UserQueryResponseBodyModule = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = UserQueryResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class UserQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UserQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UserQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


