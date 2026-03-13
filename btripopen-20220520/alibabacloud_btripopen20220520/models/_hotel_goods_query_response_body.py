# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelGoodsQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.HotelGoodsQueryResponseBodyModule = None,
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
            temp_model = main_models.HotelGoodsQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelGoodsQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        address: str = None,
        booking_instructions: Dict[str, str] = None,
        can_foreigner: bool = None,
        check_in: str = None,
        check_out: str = None,
        descriptions: List[str] = None,
        dinamic_banner_pic_urls: List[str] = None,
        early_arrival_time: str = None,
        hotel_group_desc: str = None,
        hotel_id: int = None,
        hotel_name: str = None,
        late_arrival_time: str = None,
        rooms: List[main_models.HotelGoodsQueryResponseBodyModuleRooms] = None,
        search_id: str = None,
    ):
        self.address = address
        self.booking_instructions = booking_instructions
        self.can_foreigner = can_foreigner
        self.check_in = check_in
        self.check_out = check_out
        self.descriptions = descriptions
        self.dinamic_banner_pic_urls = dinamic_banner_pic_urls
        self.early_arrival_time = early_arrival_time
        self.hotel_group_desc = hotel_group_desc
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.late_arrival_time = late_arrival_time
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

        if self.booking_instructions is not None:
            result['booking_instructions'] = self.booking_instructions

        if self.can_foreigner is not None:
            result['can_foreigner'] = self.can_foreigner

        if self.check_in is not None:
            result['check_in'] = self.check_in

        if self.check_out is not None:
            result['check_out'] = self.check_out

        if self.descriptions is not None:
            result['descriptions'] = self.descriptions

        if self.dinamic_banner_pic_urls is not None:
            result['dinamic_banner_pic_urls'] = self.dinamic_banner_pic_urls

        if self.early_arrival_time is not None:
            result['early_arrival_time'] = self.early_arrival_time

        if self.hotel_group_desc is not None:
            result['hotel_group_desc'] = self.hotel_group_desc

        if self.hotel_id is not None:
            result['hotel_id'] = self.hotel_id

        if self.hotel_name is not None:
            result['hotel_name'] = self.hotel_name

        if self.late_arrival_time is not None:
            result['late_arrival_time'] = self.late_arrival_time

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

        if m.get('booking_instructions') is not None:
            self.booking_instructions = m.get('booking_instructions')

        if m.get('can_foreigner') is not None:
            self.can_foreigner = m.get('can_foreigner')

        if m.get('check_in') is not None:
            self.check_in = m.get('check_in')

        if m.get('check_out') is not None:
            self.check_out = m.get('check_out')

        if m.get('descriptions') is not None:
            self.descriptions = m.get('descriptions')

        if m.get('dinamic_banner_pic_urls') is not None:
            self.dinamic_banner_pic_urls = m.get('dinamic_banner_pic_urls')

        if m.get('early_arrival_time') is not None:
            self.early_arrival_time = m.get('early_arrival_time')

        if m.get('hotel_group_desc') is not None:
            self.hotel_group_desc = m.get('hotel_group_desc')

        if m.get('hotel_id') is not None:
            self.hotel_id = m.get('hotel_id')

        if m.get('hotel_name') is not None:
            self.hotel_name = m.get('hotel_name')

        if m.get('late_arrival_time') is not None:
            self.late_arrival_time = m.get('late_arrival_time')

        self.rooms = []
        if m.get('rooms') is not None:
            for k1 in m.get('rooms'):
                temp_model = main_models.HotelGoodsQueryResponseBodyModuleRooms()
                self.rooms.append(temp_model.from_map(k1))

        if m.get('search_id') is not None:
            self.search_id = m.get('search_id')

        return self

class HotelGoodsQueryResponseBodyModuleRooms(DaraModel):
    def __init__(
        self,
        area: str = None,
        bed_type_string: str = None,
        extra_bed: bool = None,
        facility: str = None,
        floor: str = None,
        max_occupancy: int = None,
        name: str = None,
        network_service: str = None,
        pics: str = None,
        rates: List[main_models.HotelGoodsQueryResponseBodyModuleRoomsRates] = None,
        room_dasc: str = None,
        room_facility: List[str] = None,
        room_service: List[main_models.HotelGoodsQueryResponseBodyModuleRoomsRoomService] = None,
        srid: int = None,
        status: int = None,
        window_type: str = None,
    ):
        self.area = area
        self.bed_type_string = bed_type_string
        self.extra_bed = extra_bed
        self.facility = facility
        self.floor = floor
        self.max_occupancy = max_occupancy
        self.name = name
        self.network_service = network_service
        self.pics = pics
        self.rates = rates
        self.room_dasc = room_dasc
        self.room_facility = room_facility
        self.room_service = room_service
        self.srid = srid
        self.status = status
        self.window_type = window_type

    def validate(self):
        if self.rates:
            for v1 in self.rates:
                 if v1:
                    v1.validate()
        if self.room_service:
            for v1 in self.room_service:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['area'] = self.area

        if self.bed_type_string is not None:
            result['bed_type_string'] = self.bed_type_string

        if self.extra_bed is not None:
            result['extra_bed'] = self.extra_bed

        if self.facility is not None:
            result['facility'] = self.facility

        if self.floor is not None:
            result['floor'] = self.floor

        if self.max_occupancy is not None:
            result['max_occupancy'] = self.max_occupancy

        if self.name is not None:
            result['name'] = self.name

        if self.network_service is not None:
            result['network_service'] = self.network_service

        if self.pics is not None:
            result['pics'] = self.pics

        result['rates'] = []
        if self.rates is not None:
            for k1 in self.rates:
                result['rates'].append(k1.to_map() if k1 else None)

        if self.room_dasc is not None:
            result['room_dasc'] = self.room_dasc

        if self.room_facility is not None:
            result['room_facility'] = self.room_facility

        result['room_service'] = []
        if self.room_service is not None:
            for k1 in self.room_service:
                result['room_service'].append(k1.to_map() if k1 else None)

        if self.srid is not None:
            result['srid'] = self.srid

        if self.status is not None:
            result['status'] = self.status

        if self.window_type is not None:
            result['window_type'] = self.window_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('area') is not None:
            self.area = m.get('area')

        if m.get('bed_type_string') is not None:
            self.bed_type_string = m.get('bed_type_string')

        if m.get('extra_bed') is not None:
            self.extra_bed = m.get('extra_bed')

        if m.get('facility') is not None:
            self.facility = m.get('facility')

        if m.get('floor') is not None:
            self.floor = m.get('floor')

        if m.get('max_occupancy') is not None:
            self.max_occupancy = m.get('max_occupancy')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('network_service') is not None:
            self.network_service = m.get('network_service')

        if m.get('pics') is not None:
            self.pics = m.get('pics')

        self.rates = []
        if m.get('rates') is not None:
            for k1 in m.get('rates'):
                temp_model = main_models.HotelGoodsQueryResponseBodyModuleRoomsRates()
                self.rates.append(temp_model.from_map(k1))

        if m.get('room_dasc') is not None:
            self.room_dasc = m.get('room_dasc')

        if m.get('room_facility') is not None:
            self.room_facility = m.get('room_facility')

        self.room_service = []
        if m.get('room_service') is not None:
            for k1 in m.get('room_service'):
                temp_model = main_models.HotelGoodsQueryResponseBodyModuleRoomsRoomService()
                self.room_service.append(temp_model.from_map(k1))

        if m.get('srid') is not None:
            self.srid = m.get('srid')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('window_type') is not None:
            self.window_type = m.get('window_type')

        return self

class HotelGoodsQueryResponseBodyModuleRoomsRoomService(DaraModel):
    def __init__(
        self,
        color: str = None,
        desc: str = None,
        highlight_color_color: str = None,
        title: str = None,
    ):
        self.color = color
        self.desc = desc
        self.highlight_color_color = highlight_color_color
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.color is not None:
            result['color'] = self.color

        if self.desc is not None:
            result['desc'] = self.desc

        if self.highlight_color_color is not None:
            result['highlight_color_color'] = self.highlight_color_color

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('color') is not None:
            self.color = m.get('color')

        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('highlight_color_color') is not None:
            self.highlight_color_color = m.get('highlight_color_color')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class HotelGoodsQueryResponseBodyModuleRoomsRates(DaraModel):
    def __init__(
        self,
        bed_desc: str = None,
        bed_type: str = None,
        breakfast: str = None,
        btrip_cancel_rule: main_models.HotelGoodsQueryResponseBodyModuleRoomsRatesBtripCancelRule = None,
        btrip_hotel_cancel_desc: List[main_models.HotelGoodsQueryResponseBodyModuleRoomsRatesBtripHotelCancelDesc] = None,
        can_smoking: bool = None,
        cancel_policy_desc: str = None,
        cancel_policy_type: int = None,
        company_aassist: str = None,
        company_assist_type: str = None,
        confirm_type: int = None,
        currency_code: str = None,
        daily_price_format_yuan: str = None,
        daily_price_view: str = None,
        discount_desc: main_models.HotelGoodsQueryResponseBodyModuleRoomsRatesDiscountDesc = None,
        end_time_daily: str = None,
        hotel_detail_rate_price_dto: List[main_models.HotelGoodsQueryResponseBodyModuleRoomsRatesHotelDetailRatePriceDTO] = None,
        hotel_member_benefit: Dict[str, str] = None,
        instant_confirm: bool = None,
        inventory_desc: str = None,
        inventory_price: str = None,
        is_business_pay_4goods: bool = None,
        is_guarantee: int = None,
        is_need_email: bool = None,
        item_id: int = None,
        last_cancel_time: str = None,
        max_occupancy: int = None,
        min_adv_hours: int = None,
        min_days: int = None,
        need_certificate: bool = None,
        nod: int = None,
        nop: int = None,
        order_ship_time: int = None,
        payment_type: int = None,
        price_type: int = None,
        promotion_info: str = None,
        rate_id: int = None,
        rate_key: str = None,
        rate_plan_name: str = None,
        rp_id: int = None,
        seller_id: int = None,
        start_time_daily: str = None,
        status: int = None,
        supplier_code: str = None,
        supplier_name: str = None,
        support_special_invoice: bool = None,
        unrounding_daily_price_format_yuan: str = None,
    ):
        self.bed_desc = bed_desc
        self.bed_type = bed_type
        self.breakfast = breakfast
        self.btrip_cancel_rule = btrip_cancel_rule
        self.btrip_hotel_cancel_desc = btrip_hotel_cancel_desc
        self.can_smoking = can_smoking
        self.cancel_policy_desc = cancel_policy_desc
        self.cancel_policy_type = cancel_policy_type
        self.company_aassist = company_aassist
        self.company_assist_type = company_assist_type
        self.confirm_type = confirm_type
        self.currency_code = currency_code
        self.daily_price_format_yuan = daily_price_format_yuan
        self.daily_price_view = daily_price_view
        self.discount_desc = discount_desc
        self.end_time_daily = end_time_daily
        self.hotel_detail_rate_price_dto = hotel_detail_rate_price_dto
        self.hotel_member_benefit = hotel_member_benefit
        self.instant_confirm = instant_confirm
        self.inventory_desc = inventory_desc
        self.inventory_price = inventory_price
        self.is_business_pay_4goods = is_business_pay_4goods
        self.is_guarantee = is_guarantee
        self.is_need_email = is_need_email
        self.item_id = item_id
        self.last_cancel_time = last_cancel_time
        self.max_occupancy = max_occupancy
        self.min_adv_hours = min_adv_hours
        self.min_days = min_days
        self.need_certificate = need_certificate
        self.nod = nod
        self.nop = nop
        self.order_ship_time = order_ship_time
        self.payment_type = payment_type
        self.price_type = price_type
        self.promotion_info = promotion_info
        self.rate_id = rate_id
        self.rate_key = rate_key
        self.rate_plan_name = rate_plan_name
        self.rp_id = rp_id
        self.seller_id = seller_id
        self.start_time_daily = start_time_daily
        self.status = status
        self.supplier_code = supplier_code
        self.supplier_name = supplier_name
        self.support_special_invoice = support_special_invoice
        self.unrounding_daily_price_format_yuan = unrounding_daily_price_format_yuan

    def validate(self):
        if self.btrip_cancel_rule:
            self.btrip_cancel_rule.validate()
        if self.btrip_hotel_cancel_desc:
            for v1 in self.btrip_hotel_cancel_desc:
                 if v1:
                    v1.validate()
        if self.discount_desc:
            self.discount_desc.validate()
        if self.hotel_detail_rate_price_dto:
            for v1 in self.hotel_detail_rate_price_dto:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bed_desc is not None:
            result['bed_desc'] = self.bed_desc

        if self.bed_type is not None:
            result['bed_type'] = self.bed_type

        if self.breakfast is not None:
            result['breakfast'] = self.breakfast

        if self.btrip_cancel_rule is not None:
            result['btrip_cancel_rule'] = self.btrip_cancel_rule.to_map()

        result['btrip_hotel_cancel_desc'] = []
        if self.btrip_hotel_cancel_desc is not None:
            for k1 in self.btrip_hotel_cancel_desc:
                result['btrip_hotel_cancel_desc'].append(k1.to_map() if k1 else None)

        if self.can_smoking is not None:
            result['can_smoking'] = self.can_smoking

        if self.cancel_policy_desc is not None:
            result['cancel_policy_desc'] = self.cancel_policy_desc

        if self.cancel_policy_type is not None:
            result['cancel_policy_type'] = self.cancel_policy_type

        if self.company_aassist is not None:
            result['company_aassist'] = self.company_aassist

        if self.company_assist_type is not None:
            result['company_assist_type'] = self.company_assist_type

        if self.confirm_type is not None:
            result['confirm_type'] = self.confirm_type

        if self.currency_code is not None:
            result['currency_code'] = self.currency_code

        if self.daily_price_format_yuan is not None:
            result['daily_price_format_yuan'] = self.daily_price_format_yuan

        if self.daily_price_view is not None:
            result['daily_price_view'] = self.daily_price_view

        if self.discount_desc is not None:
            result['discount_desc'] = self.discount_desc.to_map()

        if self.end_time_daily is not None:
            result['end_time_daily'] = self.end_time_daily

        result['hotel_detail_rate_price_d_t_o'] = []
        if self.hotel_detail_rate_price_dto is not None:
            for k1 in self.hotel_detail_rate_price_dto:
                result['hotel_detail_rate_price_d_t_o'].append(k1.to_map() if k1 else None)

        if self.hotel_member_benefit is not None:
            result['hotel_member_benefit'] = self.hotel_member_benefit

        if self.instant_confirm is not None:
            result['instant_confirm'] = self.instant_confirm

        if self.inventory_desc is not None:
            result['inventory_desc'] = self.inventory_desc

        if self.inventory_price is not None:
            result['inventory_price'] = self.inventory_price

        if self.is_business_pay_4goods is not None:
            result['is_business_pay4_goods'] = self.is_business_pay_4goods

        if self.is_guarantee is not None:
            result['is_guarantee'] = self.is_guarantee

        if self.is_need_email is not None:
            result['is_need_email'] = self.is_need_email

        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.last_cancel_time is not None:
            result['last_cancel_time'] = self.last_cancel_time

        if self.max_occupancy is not None:
            result['max_occupancy'] = self.max_occupancy

        if self.min_adv_hours is not None:
            result['min_adv_hours'] = self.min_adv_hours

        if self.min_days is not None:
            result['min_days'] = self.min_days

        if self.need_certificate is not None:
            result['need_certificate'] = self.need_certificate

        if self.nod is not None:
            result['nod'] = self.nod

        if self.nop is not None:
            result['nop'] = self.nop

        if self.order_ship_time is not None:
            result['order_ship_time'] = self.order_ship_time

        if self.payment_type is not None:
            result['payment_type'] = self.payment_type

        if self.price_type is not None:
            result['price_type'] = self.price_type

        if self.promotion_info is not None:
            result['promotion_info'] = self.promotion_info

        if self.rate_id is not None:
            result['rate_id'] = self.rate_id

        if self.rate_key is not None:
            result['rate_key'] = self.rate_key

        if self.rate_plan_name is not None:
            result['rate_plan_name'] = self.rate_plan_name

        if self.rp_id is not None:
            result['rp_id'] = self.rp_id

        if self.seller_id is not None:
            result['seller_id'] = self.seller_id

        if self.start_time_daily is not None:
            result['start_time_daily'] = self.start_time_daily

        if self.status is not None:
            result['status'] = self.status

        if self.supplier_code is not None:
            result['supplier_code'] = self.supplier_code

        if self.supplier_name is not None:
            result['supplier_name'] = self.supplier_name

        if self.support_special_invoice is not None:
            result['support_special_invoice'] = self.support_special_invoice

        if self.unrounding_daily_price_format_yuan is not None:
            result['unrounding_daily_price_format_yuan'] = self.unrounding_daily_price_format_yuan

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bed_desc') is not None:
            self.bed_desc = m.get('bed_desc')

        if m.get('bed_type') is not None:
            self.bed_type = m.get('bed_type')

        if m.get('breakfast') is not None:
            self.breakfast = m.get('breakfast')

        if m.get('btrip_cancel_rule') is not None:
            temp_model = main_models.HotelGoodsQueryResponseBodyModuleRoomsRatesBtripCancelRule()
            self.btrip_cancel_rule = temp_model.from_map(m.get('btrip_cancel_rule'))

        self.btrip_hotel_cancel_desc = []
        if m.get('btrip_hotel_cancel_desc') is not None:
            for k1 in m.get('btrip_hotel_cancel_desc'):
                temp_model = main_models.HotelGoodsQueryResponseBodyModuleRoomsRatesBtripHotelCancelDesc()
                self.btrip_hotel_cancel_desc.append(temp_model.from_map(k1))

        if m.get('can_smoking') is not None:
            self.can_smoking = m.get('can_smoking')

        if m.get('cancel_policy_desc') is not None:
            self.cancel_policy_desc = m.get('cancel_policy_desc')

        if m.get('cancel_policy_type') is not None:
            self.cancel_policy_type = m.get('cancel_policy_type')

        if m.get('company_aassist') is not None:
            self.company_aassist = m.get('company_aassist')

        if m.get('company_assist_type') is not None:
            self.company_assist_type = m.get('company_assist_type')

        if m.get('confirm_type') is not None:
            self.confirm_type = m.get('confirm_type')

        if m.get('currency_code') is not None:
            self.currency_code = m.get('currency_code')

        if m.get('daily_price_format_yuan') is not None:
            self.daily_price_format_yuan = m.get('daily_price_format_yuan')

        if m.get('daily_price_view') is not None:
            self.daily_price_view = m.get('daily_price_view')

        if m.get('discount_desc') is not None:
            temp_model = main_models.HotelGoodsQueryResponseBodyModuleRoomsRatesDiscountDesc()
            self.discount_desc = temp_model.from_map(m.get('discount_desc'))

        if m.get('end_time_daily') is not None:
            self.end_time_daily = m.get('end_time_daily')

        self.hotel_detail_rate_price_dto = []
        if m.get('hotel_detail_rate_price_d_t_o') is not None:
            for k1 in m.get('hotel_detail_rate_price_d_t_o'):
                temp_model = main_models.HotelGoodsQueryResponseBodyModuleRoomsRatesHotelDetailRatePriceDTO()
                self.hotel_detail_rate_price_dto.append(temp_model.from_map(k1))

        if m.get('hotel_member_benefit') is not None:
            self.hotel_member_benefit = m.get('hotel_member_benefit')

        if m.get('instant_confirm') is not None:
            self.instant_confirm = m.get('instant_confirm')

        if m.get('inventory_desc') is not None:
            self.inventory_desc = m.get('inventory_desc')

        if m.get('inventory_price') is not None:
            self.inventory_price = m.get('inventory_price')

        if m.get('is_business_pay4_goods') is not None:
            self.is_business_pay_4goods = m.get('is_business_pay4_goods')

        if m.get('is_guarantee') is not None:
            self.is_guarantee = m.get('is_guarantee')

        if m.get('is_need_email') is not None:
            self.is_need_email = m.get('is_need_email')

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('last_cancel_time') is not None:
            self.last_cancel_time = m.get('last_cancel_time')

        if m.get('max_occupancy') is not None:
            self.max_occupancy = m.get('max_occupancy')

        if m.get('min_adv_hours') is not None:
            self.min_adv_hours = m.get('min_adv_hours')

        if m.get('min_days') is not None:
            self.min_days = m.get('min_days')

        if m.get('need_certificate') is not None:
            self.need_certificate = m.get('need_certificate')

        if m.get('nod') is not None:
            self.nod = m.get('nod')

        if m.get('nop') is not None:
            self.nop = m.get('nop')

        if m.get('order_ship_time') is not None:
            self.order_ship_time = m.get('order_ship_time')

        if m.get('payment_type') is not None:
            self.payment_type = m.get('payment_type')

        if m.get('price_type') is not None:
            self.price_type = m.get('price_type')

        if m.get('promotion_info') is not None:
            self.promotion_info = m.get('promotion_info')

        if m.get('rate_id') is not None:
            self.rate_id = m.get('rate_id')

        if m.get('rate_key') is not None:
            self.rate_key = m.get('rate_key')

        if m.get('rate_plan_name') is not None:
            self.rate_plan_name = m.get('rate_plan_name')

        if m.get('rp_id') is not None:
            self.rp_id = m.get('rp_id')

        if m.get('seller_id') is not None:
            self.seller_id = m.get('seller_id')

        if m.get('start_time_daily') is not None:
            self.start_time_daily = m.get('start_time_daily')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('supplier_code') is not None:
            self.supplier_code = m.get('supplier_code')

        if m.get('supplier_name') is not None:
            self.supplier_name = m.get('supplier_name')

        if m.get('support_special_invoice') is not None:
            self.support_special_invoice = m.get('support_special_invoice')

        if m.get('unrounding_daily_price_format_yuan') is not None:
            self.unrounding_daily_price_format_yuan = m.get('unrounding_daily_price_format_yuan')

        return self

class HotelGoodsQueryResponseBodyModuleRoomsRatesHotelDetailRatePriceDTO(DaraModel):
    def __init__(
        self,
        before_discount_price: int = None,
        breakfast: str = None,
        discount_price: int = None,
        last_discounts_price: int = None,
        last_discounts_rounding_price: int = None,
        last_num: int = None,
        rate_start_time: str = None,
        status: int = None,
    ):
        self.before_discount_price = before_discount_price
        self.breakfast = breakfast
        self.discount_price = discount_price
        self.last_discounts_price = last_discounts_price
        self.last_discounts_rounding_price = last_discounts_rounding_price
        self.last_num = last_num
        self.rate_start_time = rate_start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.before_discount_price is not None:
            result['before_discount_price'] = self.before_discount_price

        if self.breakfast is not None:
            result['breakfast'] = self.breakfast

        if self.discount_price is not None:
            result['discount_price'] = self.discount_price

        if self.last_discounts_price is not None:
            result['last_discounts_price'] = self.last_discounts_price

        if self.last_discounts_rounding_price is not None:
            result['last_discounts_rounding_price'] = self.last_discounts_rounding_price

        if self.last_num is not None:
            result['last_num'] = self.last_num

        if self.rate_start_time is not None:
            result['rate_start_time'] = self.rate_start_time

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('before_discount_price') is not None:
            self.before_discount_price = m.get('before_discount_price')

        if m.get('breakfast') is not None:
            self.breakfast = m.get('breakfast')

        if m.get('discount_price') is not None:
            self.discount_price = m.get('discount_price')

        if m.get('last_discounts_price') is not None:
            self.last_discounts_price = m.get('last_discounts_price')

        if m.get('last_discounts_rounding_price') is not None:
            self.last_discounts_rounding_price = m.get('last_discounts_rounding_price')

        if m.get('last_num') is not None:
            self.last_num = m.get('last_num')

        if m.get('rate_start_time') is not None:
            self.rate_start_time = m.get('rate_start_time')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class HotelGoodsQueryResponseBodyModuleRoomsRatesDiscountDesc(DaraModel):
    def __init__(
        self,
        cash_reduce_total: str = None,
        dinamic_label: str = None,
        discount_detail: List[main_models.HotelGoodsQueryResponseBodyModuleRoomsRatesDiscountDescDiscountDetail] = None,
        sub_title: str = None,
        title: str = None,
    ):
        self.cash_reduce_total = cash_reduce_total
        self.dinamic_label = dinamic_label
        self.discount_detail = discount_detail
        self.sub_title = sub_title
        self.title = title

    def validate(self):
        if self.discount_detail:
            for v1 in self.discount_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cash_reduce_total is not None:
            result['cash_reduce_total'] = self.cash_reduce_total

        if self.dinamic_label is not None:
            result['dinamic_label'] = self.dinamic_label

        result['discount_detail'] = []
        if self.discount_detail is not None:
            for k1 in self.discount_detail:
                result['discount_detail'].append(k1.to_map() if k1 else None)

        if self.sub_title is not None:
            result['sub_title'] = self.sub_title

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cash_reduce_total') is not None:
            self.cash_reduce_total = m.get('cash_reduce_total')

        if m.get('dinamic_label') is not None:
            self.dinamic_label = m.get('dinamic_label')

        self.discount_detail = []
        if m.get('discount_detail') is not None:
            for k1 in m.get('discount_detail'):
                temp_model = main_models.HotelGoodsQueryResponseBodyModuleRoomsRatesDiscountDescDiscountDetail()
                self.discount_detail.append(temp_model.from_map(k1))

        if m.get('sub_title') is not None:
            self.sub_title = m.get('sub_title')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class HotelGoodsQueryResponseBodyModuleRoomsRatesDiscountDescDiscountDetail(DaraModel):
    def __init__(
        self,
        label_name: List[str] = None,
        money_desc: str = None,
    ):
        self.label_name = label_name
        self.money_desc = money_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_name is not None:
            result['label_name'] = self.label_name

        if self.money_desc is not None:
            result['money_desc'] = self.money_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label_name') is not None:
            self.label_name = m.get('label_name')

        if m.get('money_desc') is not None:
            self.money_desc = m.get('money_desc')

        return self

class HotelGoodsQueryResponseBodyModuleRoomsRatesBtripHotelCancelDesc(DaraModel):
    def __init__(
        self,
        desc: str = None,
        title: str = None,
    ):
        self.desc = desc
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class HotelGoodsQueryResponseBodyModuleRoomsRatesBtripCancelRule(DaraModel):
    def __init__(
        self,
        btrip_hotel_cancel_policy_dto: main_models.HotelGoodsQueryResponseBodyModuleRoomsRatesBtripCancelRuleBtripHotelCancelPolicyDTO = None,
        cancel_policy_title: str = None,
        check_in: str = None,
    ):
        self.btrip_hotel_cancel_policy_dto = btrip_hotel_cancel_policy_dto
        self.cancel_policy_title = cancel_policy_title
        self.check_in = check_in

    def validate(self):
        if self.btrip_hotel_cancel_policy_dto:
            self.btrip_hotel_cancel_policy_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.btrip_hotel_cancel_policy_dto is not None:
            result['btrip_hotel_cancel_policy_d_t_o'] = self.btrip_hotel_cancel_policy_dto.to_map()

        if self.cancel_policy_title is not None:
            result['cancel_policy_title'] = self.cancel_policy_title

        if self.check_in is not None:
            result['check_in'] = self.check_in

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_hotel_cancel_policy_d_t_o') is not None:
            temp_model = main_models.HotelGoodsQueryResponseBodyModuleRoomsRatesBtripCancelRuleBtripHotelCancelPolicyDTO()
            self.btrip_hotel_cancel_policy_dto = temp_model.from_map(m.get('btrip_hotel_cancel_policy_d_t_o'))

        if m.get('cancel_policy_title') is not None:
            self.cancel_policy_title = m.get('cancel_policy_title')

        if m.get('check_in') is not None:
            self.check_in = m.get('check_in')

        return self

class HotelGoodsQueryResponseBodyModuleRoomsRatesBtripCancelRuleBtripHotelCancelPolicyDTO(DaraModel):
    def __init__(
        self,
        btrip_hotel_cancel_policy_info_dtolist: List[main_models.HotelGoodsQueryResponseBodyModuleRoomsRatesBtripCancelRuleBtripHotelCancelPolicyDTOBtripHotelCancelPolicyInfoDTOList] = None,
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
                temp_model = main_models.HotelGoodsQueryResponseBodyModuleRoomsRatesBtripCancelRuleBtripHotelCancelPolicyDTOBtripHotelCancelPolicyInfoDTOList()
                self.btrip_hotel_cancel_policy_info_dtolist.append(temp_model.from_map(k1))

        if m.get('cancel_policy_type') is not None:
            self.cancel_policy_type = m.get('cancel_policy_type')

        return self

class HotelGoodsQueryResponseBodyModuleRoomsRatesBtripCancelRuleBtripHotelCancelPolicyDTOBtripHotelCancelPolicyInfoDTOList(DaraModel):
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

