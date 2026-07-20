# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelPricePullResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.HotelPricePullResponseBodyModule = None,
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
            result['request_id'] = self.request_id

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
            temp_model = main_models.HotelPricePullResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelPricePullResponseBodyModule(DaraModel):
    def __init__(
        self,
        hotel_price_infos: List[main_models.HotelPricePullResponseBodyModuleHotelPriceInfos] = None,
    ):
        self.hotel_price_infos = hotel_price_infos

    def validate(self):
        if self.hotel_price_infos:
            for v1 in self.hotel_price_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['hotel_price_infos'] = []
        if self.hotel_price_infos is not None:
            for k1 in self.hotel_price_infos:
                result['hotel_price_infos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hotel_price_infos = []
        if m.get('hotel_price_infos') is not None:
            for k1 in m.get('hotel_price_infos'):
                temp_model = main_models.HotelPricePullResponseBodyModuleHotelPriceInfos()
                self.hotel_price_infos.append(temp_model.from_map(k1))

        return self

class HotelPricePullResponseBodyModuleHotelPriceInfos(DaraModel):
    def __init__(
        self,
        address: str = None,
        hotel_id: str = None,
        hotel_name: str = None,
        rooms: List[main_models.HotelPricePullResponseBodyModuleHotelPriceInfosRooms] = None,
        search_id: str = None,
    ):
        self.address = address
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.rooms = rooms
        self.search_id = search_id

    def validate(self):
        if self.rooms:
            for v1 in self.rooms:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.hotel_id is not None:
            result['hotel_id'] = self.hotel_id

        if self.hotel_name is not None:
            result['hotel_name'] = self.hotel_name

        result['rooms'] = []
        if self.rooms is not None:
            for k1 in self.rooms:
                result['rooms'].append(k1.to_map() if k1 else None)

        if self.search_id is not None:
            result['search_id'] = self.search_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('hotel_id') is not None:
            self.hotel_id = m.get('hotel_id')

        if m.get('hotel_name') is not None:
            self.hotel_name = m.get('hotel_name')

        self.rooms = []
        if m.get('rooms') is not None:
            for k1 in m.get('rooms'):
                temp_model = main_models.HotelPricePullResponseBodyModuleHotelPriceInfosRooms()
                self.rooms.append(temp_model.from_map(k1))

        if m.get('search_id') is not None:
            self.search_id = m.get('search_id')

        return self

class HotelPricePullResponseBodyModuleHotelPriceInfosRooms(DaraModel):
    def __init__(
        self,
        area: str = None,
        bed: str = None,
        bed_type_string: str = None,
        facility: str = None,
        floor: str = None,
        max_occupancy: int = None,
        network_service: str = None,
        pics: List[str] = None,
        rates: List[main_models.HotelPricePullResponseBodyModuleHotelPriceInfosRoomsRates] = None,
        room_id: str = None,
        room_name: str = None,
        status: int = None,
        window_type: str = None,
    ):
        self.area = area
        self.bed = bed
        self.bed_type_string = bed_type_string
        self.facility = facility
        self.floor = floor
        self.max_occupancy = max_occupancy
        self.network_service = network_service
        self.pics = pics
        self.rates = rates
        self.room_id = room_id
        self.room_name = room_name
        self.status = status
        self.window_type = window_type

    def validate(self):
        if self.rates:
            for v1 in self.rates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['area'] = self.area

        if self.bed is not None:
            result['bed'] = self.bed

        if self.bed_type_string is not None:
            result['bed_type_string'] = self.bed_type_string

        if self.facility is not None:
            result['facility'] = self.facility

        if self.floor is not None:
            result['floor'] = self.floor

        if self.max_occupancy is not None:
            result['max_occupancy'] = self.max_occupancy

        if self.network_service is not None:
            result['network_service'] = self.network_service

        if self.pics is not None:
            result['pics'] = self.pics

        result['rates'] = []
        if self.rates is not None:
            for k1 in self.rates:
                result['rates'].append(k1.to_map() if k1 else None)

        if self.room_id is not None:
            result['room_id'] = self.room_id

        if self.room_name is not None:
            result['room_name'] = self.room_name

        if self.status is not None:
            result['status'] = self.status

        if self.window_type is not None:
            result['window_type'] = self.window_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('area') is not None:
            self.area = m.get('area')

        if m.get('bed') is not None:
            self.bed = m.get('bed')

        if m.get('bed_type_string') is not None:
            self.bed_type_string = m.get('bed_type_string')

        if m.get('facility') is not None:
            self.facility = m.get('facility')

        if m.get('floor') is not None:
            self.floor = m.get('floor')

        if m.get('max_occupancy') is not None:
            self.max_occupancy = m.get('max_occupancy')

        if m.get('network_service') is not None:
            self.network_service = m.get('network_service')

        if m.get('pics') is not None:
            self.pics = m.get('pics')

        self.rates = []
        if m.get('rates') is not None:
            for k1 in m.get('rates'):
                temp_model = main_models.HotelPricePullResponseBodyModuleHotelPriceInfosRoomsRates()
                self.rates.append(temp_model.from_map(k1))

        if m.get('room_id') is not None:
            self.room_id = m.get('room_id')

        if m.get('room_name') is not None:
            self.room_name = m.get('room_name')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('window_type') is not None:
            self.window_type = m.get('window_type')

        return self

class HotelPricePullResponseBodyModuleHotelPriceInfosRoomsRates(DaraModel):
    def __init__(
        self,
        breakfast: str = None,
        breakfast_count: int = None,
        btrip_hotel_cancel_policy: main_models.HotelPricePullResponseBodyModuleHotelPriceInfosRoomsRatesBtripHotelCancelPolicy = None,
        cancel_policy_desc: str = None,
        company_aassist: str = None,
        currency_code: str = None,
        instant_confirm: bool = None,
        item_id: str = None,
        max_adv_hours: int = None,
        max_days: int = None,
        min_adv_hours: int = None,
        min_days: int = None,
        nod: int = None,
        nop: int = None,
        payment_type: int = None,
        price: int = None,
        promotion_info: str = None,
        quota: int = None,
        rate_dailys: List[main_models.HotelPricePullResponseBodyModuleHotelPriceInfosRoomsRatesRateDailys] = None,
        rate_id: str = None,
        rate_plan_name: str = None,
        rp_id: str = None,
        seller_id: str = None,
        support_special_invoice: bool = None,
    ):
        self.breakfast = breakfast
        self.breakfast_count = breakfast_count
        self.btrip_hotel_cancel_policy = btrip_hotel_cancel_policy
        self.cancel_policy_desc = cancel_policy_desc
        self.company_aassist = company_aassist
        self.currency_code = currency_code
        self.instant_confirm = instant_confirm
        self.item_id = item_id
        self.max_adv_hours = max_adv_hours
        self.max_days = max_days
        self.min_adv_hours = min_adv_hours
        self.min_days = min_days
        self.nod = nod
        self.nop = nop
        self.payment_type = payment_type
        self.price = price
        self.promotion_info = promotion_info
        self.quota = quota
        self.rate_dailys = rate_dailys
        self.rate_id = rate_id
        self.rate_plan_name = rate_plan_name
        self.rp_id = rp_id
        self.seller_id = seller_id
        self.support_special_invoice = support_special_invoice

    def validate(self):
        if self.btrip_hotel_cancel_policy:
            self.btrip_hotel_cancel_policy.validate()
        if self.rate_dailys:
            for v1 in self.rate_dailys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.breakfast is not None:
            result['breakfast'] = self.breakfast

        if self.breakfast_count is not None:
            result['breakfast_count'] = self.breakfast_count

        if self.btrip_hotel_cancel_policy is not None:
            result['btrip_hotel_cancel_policy'] = self.btrip_hotel_cancel_policy.to_map()

        if self.cancel_policy_desc is not None:
            result['cancel_policy_desc'] = self.cancel_policy_desc

        if self.company_aassist is not None:
            result['company_aassist'] = self.company_aassist

        if self.currency_code is not None:
            result['currency_code'] = self.currency_code

        if self.instant_confirm is not None:
            result['instant_confirm'] = self.instant_confirm

        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.max_adv_hours is not None:
            result['max_adv_hours'] = self.max_adv_hours

        if self.max_days is not None:
            result['max_days'] = self.max_days

        if self.min_adv_hours is not None:
            result['min_adv_hours'] = self.min_adv_hours

        if self.min_days is not None:
            result['min_days'] = self.min_days

        if self.nod is not None:
            result['nod'] = self.nod

        if self.nop is not None:
            result['nop'] = self.nop

        if self.payment_type is not None:
            result['payment_type'] = self.payment_type

        if self.price is not None:
            result['price'] = self.price

        if self.promotion_info is not None:
            result['promotion_info'] = self.promotion_info

        if self.quota is not None:
            result['quota'] = self.quota

        result['rate_dailys'] = []
        if self.rate_dailys is not None:
            for k1 in self.rate_dailys:
                result['rate_dailys'].append(k1.to_map() if k1 else None)

        if self.rate_id is not None:
            result['rate_id'] = self.rate_id

        if self.rate_plan_name is not None:
            result['rate_plan_name'] = self.rate_plan_name

        if self.rp_id is not None:
            result['rp_id'] = self.rp_id

        if self.seller_id is not None:
            result['seller_id'] = self.seller_id

        if self.support_special_invoice is not None:
            result['support_special_invoice'] = self.support_special_invoice

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('breakfast') is not None:
            self.breakfast = m.get('breakfast')

        if m.get('breakfast_count') is not None:
            self.breakfast_count = m.get('breakfast_count')

        if m.get('btrip_hotel_cancel_policy') is not None:
            temp_model = main_models.HotelPricePullResponseBodyModuleHotelPriceInfosRoomsRatesBtripHotelCancelPolicy()
            self.btrip_hotel_cancel_policy = temp_model.from_map(m.get('btrip_hotel_cancel_policy'))

        if m.get('cancel_policy_desc') is not None:
            self.cancel_policy_desc = m.get('cancel_policy_desc')

        if m.get('company_aassist') is not None:
            self.company_aassist = m.get('company_aassist')

        if m.get('currency_code') is not None:
            self.currency_code = m.get('currency_code')

        if m.get('instant_confirm') is not None:
            self.instant_confirm = m.get('instant_confirm')

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('max_adv_hours') is not None:
            self.max_adv_hours = m.get('max_adv_hours')

        if m.get('max_days') is not None:
            self.max_days = m.get('max_days')

        if m.get('min_adv_hours') is not None:
            self.min_adv_hours = m.get('min_adv_hours')

        if m.get('min_days') is not None:
            self.min_days = m.get('min_days')

        if m.get('nod') is not None:
            self.nod = m.get('nod')

        if m.get('nop') is not None:
            self.nop = m.get('nop')

        if m.get('payment_type') is not None:
            self.payment_type = m.get('payment_type')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('promotion_info') is not None:
            self.promotion_info = m.get('promotion_info')

        if m.get('quota') is not None:
            self.quota = m.get('quota')

        self.rate_dailys = []
        if m.get('rate_dailys') is not None:
            for k1 in m.get('rate_dailys'):
                temp_model = main_models.HotelPricePullResponseBodyModuleHotelPriceInfosRoomsRatesRateDailys()
                self.rate_dailys.append(temp_model.from_map(k1))

        if m.get('rate_id') is not None:
            self.rate_id = m.get('rate_id')

        if m.get('rate_plan_name') is not None:
            self.rate_plan_name = m.get('rate_plan_name')

        if m.get('rp_id') is not None:
            self.rp_id = m.get('rp_id')

        if m.get('seller_id') is not None:
            self.seller_id = m.get('seller_id')

        if m.get('support_special_invoice') is not None:
            self.support_special_invoice = m.get('support_special_invoice')

        return self

class HotelPricePullResponseBodyModuleHotelPriceInfosRoomsRatesRateDailys(DaraModel):
    def __init__(
        self,
        discount_price: int = None,
        last_discounts_price: int = None,
        price: int = None,
        start_date: str = None,
    ):
        self.discount_price = discount_price
        self.last_discounts_price = last_discounts_price
        self.price = price
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.discount_price is not None:
            result['discount_price'] = self.discount_price

        if self.last_discounts_price is not None:
            result['last_discounts_price'] = self.last_discounts_price

        if self.price is not None:
            result['price'] = self.price

        if self.start_date is not None:
            result['start_date'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('discount_price') is not None:
            self.discount_price = m.get('discount_price')

        if m.get('last_discounts_price') is not None:
            self.last_discounts_price = m.get('last_discounts_price')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('start_date') is not None:
            self.start_date = m.get('start_date')

        return self

class HotelPricePullResponseBodyModuleHotelPriceInfosRoomsRatesBtripHotelCancelPolicy(DaraModel):
    def __init__(
        self,
        btrip_hotel_cancel_policy_info_dtolist: List[main_models.HotelPricePullResponseBodyModuleHotelPriceInfosRoomsRatesBtripHotelCancelPolicyBtripHotelCancelPolicyInfoDTOList] = None,
        cancel_policy_type: int = None,
    ):
        self.btrip_hotel_cancel_policy_info_dtolist = btrip_hotel_cancel_policy_info_dtolist
        self.cancel_policy_type = cancel_policy_type

    def validate(self):
        if self.btrip_hotel_cancel_policy_info_dtolist:
            for v1 in self.btrip_hotel_cancel_policy_info_dtolist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['btrip_hotel_cancel_policy_info_d_t_o_list'] = []
        if self.btrip_hotel_cancel_policy_info_dtolist is not None:
            for k1 in self.btrip_hotel_cancel_policy_info_dtolist:
                result['btrip_hotel_cancel_policy_info_d_t_o_list'].append(k1.to_map() if k1 else None)

        if self.cancel_policy_type is not None:
            result['cancel_policy_type'] = self.cancel_policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.btrip_hotel_cancel_policy_info_dtolist = []
        if m.get('btrip_hotel_cancel_policy_info_d_t_o_list') is not None:
            for k1 in m.get('btrip_hotel_cancel_policy_info_d_t_o_list'):
                temp_model = main_models.HotelPricePullResponseBodyModuleHotelPriceInfosRoomsRatesBtripHotelCancelPolicyBtripHotelCancelPolicyInfoDTOList()
                self.btrip_hotel_cancel_policy_info_dtolist.append(temp_model.from_map(k1))

        if m.get('cancel_policy_type') is not None:
            self.cancel_policy_type = m.get('cancel_policy_type')

        return self

class HotelPricePullResponseBodyModuleHotelPriceInfosRoomsRatesBtripHotelCancelPolicyBtripHotelCancelPolicyInfoDTOList(DaraModel):
    def __init__(
        self,
        hour: int = None,
        value: int = None,
    ):
        self.hour = hour
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hour is not None:
            result['hour'] = self.hour

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hour') is not None:
            self.hour = m.get('hour')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

