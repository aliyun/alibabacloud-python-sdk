# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelOrderPreValidateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.HotelOrderPreValidateResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        # requestId
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
            temp_model = main_models.HotelOrderPreValidateResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelOrderPreValidateResponseBodyModule(DaraModel):
    def __init__(
        self,
        extend_info: str = None,
        item_invoice: main_models.HotelOrderPreValidateResponseBodyModuleItemInvoice = None,
        itinerary_no: str = None,
        promotion_info: main_models.HotelOrderPreValidateResponseBodyModulePromotionInfo = None,
        rate_plan_daily: List[main_models.HotelOrderPreValidateResponseBodyModuleRatePlanDaily] = None,
        rate_plan_id: int = None,
        rate_plan_info: main_models.HotelOrderPreValidateResponseBodyModuleRatePlanInfo = None,
        validate_res_key: str = None,
    ):
        self.extend_info = extend_info
        self.item_invoice = item_invoice
        self.itinerary_no = itinerary_no
        self.promotion_info = promotion_info
        self.rate_plan_daily = rate_plan_daily
        self.rate_plan_id = rate_plan_id
        self.rate_plan_info = rate_plan_info
        self.validate_res_key = validate_res_key

    def validate(self):
        if self.item_invoice:
            self.item_invoice.validate()
        if self.promotion_info:
            self.promotion_info.validate()
        if self.rate_plan_daily:
            for v1 in self.rate_plan_daily:
                 if v1:
                    v1.validate()
        if self.rate_plan_info:
            self.rate_plan_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extend_info is not None:
            result['extend_info'] = self.extend_info

        if self.item_invoice is not None:
            result['item_invoice'] = self.item_invoice.to_map()

        if self.itinerary_no is not None:
            result['itinerary_no'] = self.itinerary_no

        if self.promotion_info is not None:
            result['promotion_info'] = self.promotion_info.to_map()

        result['rate_plan_daily'] = []
        if self.rate_plan_daily is not None:
            for k1 in self.rate_plan_daily:
                result['rate_plan_daily'].append(k1.to_map() if k1 else None)

        if self.rate_plan_id is not None:
            result['rate_plan_id'] = self.rate_plan_id

        if self.rate_plan_info is not None:
            result['rate_plan_info'] = self.rate_plan_info.to_map()

        if self.validate_res_key is not None:
            result['validate_res_key'] = self.validate_res_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extend_info') is not None:
            self.extend_info = m.get('extend_info')

        if m.get('item_invoice') is not None:
            temp_model = main_models.HotelOrderPreValidateResponseBodyModuleItemInvoice()
            self.item_invoice = temp_model.from_map(m.get('item_invoice'))

        if m.get('itinerary_no') is not None:
            self.itinerary_no = m.get('itinerary_no')

        if m.get('promotion_info') is not None:
            temp_model = main_models.HotelOrderPreValidateResponseBodyModulePromotionInfo()
            self.promotion_info = temp_model.from_map(m.get('promotion_info'))

        self.rate_plan_daily = []
        if m.get('rate_plan_daily') is not None:
            for k1 in m.get('rate_plan_daily'):
                temp_model = main_models.HotelOrderPreValidateResponseBodyModuleRatePlanDaily()
                self.rate_plan_daily.append(temp_model.from_map(k1))

        if m.get('rate_plan_id') is not None:
            self.rate_plan_id = m.get('rate_plan_id')

        if m.get('rate_plan_info') is not None:
            temp_model = main_models.HotelOrderPreValidateResponseBodyModuleRatePlanInfo()
            self.rate_plan_info = temp_model.from_map(m.get('rate_plan_info'))

        if m.get('validate_res_key') is not None:
            self.validate_res_key = m.get('validate_res_key')

        return self

class HotelOrderPreValidateResponseBodyModuleRatePlanInfo(DaraModel):
    def __init__(
        self,
        bed_desc: str = None,
        btrip_hotel_cancel_policy_dto: main_models.HotelOrderPreValidateResponseBodyModuleRatePlanInfoBtripHotelCancelPolicyDTO = None,
        cert_type_list: List[str] = None,
        earliest_check_in_time: str = None,
        latest_check_out_time: str = None,
        max_booking_num: int = None,
        max_occupancy_num: int = None,
        need_certificate: bool = None,
        need_email: bool = None,
        need_english_name: bool = None,
        total_order_price: int = None,
        total_room_price: int = None,
    ):
        self.bed_desc = bed_desc
        self.btrip_hotel_cancel_policy_dto = btrip_hotel_cancel_policy_dto
        self.cert_type_list = cert_type_list
        self.earliest_check_in_time = earliest_check_in_time
        self.latest_check_out_time = latest_check_out_time
        self.max_booking_num = max_booking_num
        self.max_occupancy_num = max_occupancy_num
        self.need_certificate = need_certificate
        self.need_email = need_email
        self.need_english_name = need_english_name
        self.total_order_price = total_order_price
        self.total_room_price = total_room_price

    def validate(self):
        if self.btrip_hotel_cancel_policy_dto:
            self.btrip_hotel_cancel_policy_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bed_desc is not None:
            result['bed_desc'] = self.bed_desc

        if self.btrip_hotel_cancel_policy_dto is not None:
            result['btrip_hotel_cancel_policy_d_t_o'] = self.btrip_hotel_cancel_policy_dto.to_map()

        if self.cert_type_list is not None:
            result['cert_type_list'] = self.cert_type_list

        if self.earliest_check_in_time is not None:
            result['earliest_check_in_time'] = self.earliest_check_in_time

        if self.latest_check_out_time is not None:
            result['latest_check_out_time'] = self.latest_check_out_time

        if self.max_booking_num is not None:
            result['max_booking_num'] = self.max_booking_num

        if self.max_occupancy_num is not None:
            result['max_occupancy_num'] = self.max_occupancy_num

        if self.need_certificate is not None:
            result['need_certificate'] = self.need_certificate

        if self.need_email is not None:
            result['need_email'] = self.need_email

        if self.need_english_name is not None:
            result['need_english_name'] = self.need_english_name

        if self.total_order_price is not None:
            result['total_order_price'] = self.total_order_price

        if self.total_room_price is not None:
            result['total_room_price'] = self.total_room_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bed_desc') is not None:
            self.bed_desc = m.get('bed_desc')

        if m.get('btrip_hotel_cancel_policy_d_t_o') is not None:
            temp_model = main_models.HotelOrderPreValidateResponseBodyModuleRatePlanInfoBtripHotelCancelPolicyDTO()
            self.btrip_hotel_cancel_policy_dto = temp_model.from_map(m.get('btrip_hotel_cancel_policy_d_t_o'))

        if m.get('cert_type_list') is not None:
            self.cert_type_list = m.get('cert_type_list')

        if m.get('earliest_check_in_time') is not None:
            self.earliest_check_in_time = m.get('earliest_check_in_time')

        if m.get('latest_check_out_time') is not None:
            self.latest_check_out_time = m.get('latest_check_out_time')

        if m.get('max_booking_num') is not None:
            self.max_booking_num = m.get('max_booking_num')

        if m.get('max_occupancy_num') is not None:
            self.max_occupancy_num = m.get('max_occupancy_num')

        if m.get('need_certificate') is not None:
            self.need_certificate = m.get('need_certificate')

        if m.get('need_email') is not None:
            self.need_email = m.get('need_email')

        if m.get('need_english_name') is not None:
            self.need_english_name = m.get('need_english_name')

        if m.get('total_order_price') is not None:
            self.total_order_price = m.get('total_order_price')

        if m.get('total_room_price') is not None:
            self.total_room_price = m.get('total_room_price')

        return self

class HotelOrderPreValidateResponseBodyModuleRatePlanInfoBtripHotelCancelPolicyDTO(DaraModel):
    def __init__(
        self,
        btrip_hotel_cancel_policy_info_dtolist: List[main_models.HotelOrderPreValidateResponseBodyModuleRatePlanInfoBtripHotelCancelPolicyDTOBtripHotelCancelPolicyInfoDTOList] = None,
        cancel_policy_type: int = None,
        content: str = None,
        short_desc: str = None,
    ):
        self.btrip_hotel_cancel_policy_info_dtolist = btrip_hotel_cancel_policy_info_dtolist
        self.cancel_policy_type = cancel_policy_type
        self.content = content
        self.short_desc = short_desc

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

        if self.content is not None:
            result['content'] = self.content

        if self.short_desc is not None:
            result['short_desc'] = self.short_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.btrip_hotel_cancel_policy_info_dtolist = []
        if m.get('btrip_hotel_cancel_policy_info_d_t_o_list') is not None:
            for k1 in m.get('btrip_hotel_cancel_policy_info_d_t_o_list'):
                temp_model = main_models.HotelOrderPreValidateResponseBodyModuleRatePlanInfoBtripHotelCancelPolicyDTOBtripHotelCancelPolicyInfoDTOList()
                self.btrip_hotel_cancel_policy_info_dtolist.append(temp_model.from_map(k1))

        if m.get('cancel_policy_type') is not None:
            self.cancel_policy_type = m.get('cancel_policy_type')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('short_desc') is not None:
            self.short_desc = m.get('short_desc')

        return self

class HotelOrderPreValidateResponseBodyModuleRatePlanInfoBtripHotelCancelPolicyDTOBtripHotelCancelPolicyInfoDTOList(DaraModel):
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

class HotelOrderPreValidateResponseBodyModuleRatePlanDaily(DaraModel):
    def __init__(
        self,
        board: str = None,
        discount_price: str = None,
        max_booking_num: int = None,
        price: int = None,
        rate_start_time: str = None,
        room_count: int = None,
        rounding_discount_price: str = None,
        rounding_price: str = None,
        service_fee: int = None,
    ):
        self.board = board
        self.discount_price = discount_price
        self.max_booking_num = max_booking_num
        self.price = price
        self.rate_start_time = rate_start_time
        self.room_count = room_count
        self.rounding_discount_price = rounding_discount_price
        self.rounding_price = rounding_price
        self.service_fee = service_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.board is not None:
            result['board'] = self.board

        if self.discount_price is not None:
            result['discount_price'] = self.discount_price

        if self.max_booking_num is not None:
            result['max_booking_num'] = self.max_booking_num

        if self.price is not None:
            result['price'] = self.price

        if self.rate_start_time is not None:
            result['rate_start_time'] = self.rate_start_time

        if self.room_count is not None:
            result['room_count'] = self.room_count

        if self.rounding_discount_price is not None:
            result['rounding_discount_price'] = self.rounding_discount_price

        if self.rounding_price is not None:
            result['rounding_price'] = self.rounding_price

        if self.service_fee is not None:
            result['service_fee'] = self.service_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('board') is not None:
            self.board = m.get('board')

        if m.get('discount_price') is not None:
            self.discount_price = m.get('discount_price')

        if m.get('max_booking_num') is not None:
            self.max_booking_num = m.get('max_booking_num')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('rate_start_time') is not None:
            self.rate_start_time = m.get('rate_start_time')

        if m.get('room_count') is not None:
            self.room_count = m.get('room_count')

        if m.get('rounding_discount_price') is not None:
            self.rounding_discount_price = m.get('rounding_discount_price')

        if m.get('rounding_price') is not None:
            self.rounding_price = m.get('rounding_price')

        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')

        return self

class HotelOrderPreValidateResponseBodyModulePromotionInfo(DaraModel):
    def __init__(
        self,
        ext_attr_map: Dict[str, str] = None,
        promotion_detail_info_list: List[main_models.HotelOrderPreValidateResponseBodyModulePromotionInfoPromotionDetailInfoList] = None,
        promotion_total_price: int = None,
    ):
        self.ext_attr_map = ext_attr_map
        self.promotion_detail_info_list = promotion_detail_info_list
        self.promotion_total_price = promotion_total_price

    def validate(self):
        if self.promotion_detail_info_list:
            for v1 in self.promotion_detail_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext_attr_map is not None:
            result['ext_attr_map'] = self.ext_attr_map

        result['promotion_detail_info_list'] = []
        if self.promotion_detail_info_list is not None:
            for k1 in self.promotion_detail_info_list:
                result['promotion_detail_info_list'].append(k1.to_map() if k1 else None)

        if self.promotion_total_price is not None:
            result['promotion_total_price'] = self.promotion_total_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ext_attr_map') is not None:
            self.ext_attr_map = m.get('ext_attr_map')

        self.promotion_detail_info_list = []
        if m.get('promotion_detail_info_list') is not None:
            for k1 in m.get('promotion_detail_info_list'):
                temp_model = main_models.HotelOrderPreValidateResponseBodyModulePromotionInfoPromotionDetailInfoList()
                self.promotion_detail_info_list.append(temp_model.from_map(k1))

        if m.get('promotion_total_price') is not None:
            self.promotion_total_price = m.get('promotion_total_price')

        return self

class HotelOrderPreValidateResponseBodyModulePromotionInfoPromotionDetailInfoList(DaraModel):
    def __init__(
        self,
        check_status: bool = None,
        need_check: bool = None,
        promotion_code: str = None,
        promotion_id: str = None,
        promotion_name: str = None,
        promotion_price: int = None,
        promotion_type: str = None,
    ):
        self.check_status = check_status
        self.need_check = need_check
        self.promotion_code = promotion_code
        self.promotion_id = promotion_id
        self.promotion_name = promotion_name
        self.promotion_price = promotion_price
        self.promotion_type = promotion_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_status is not None:
            result['check_status'] = self.check_status

        if self.need_check is not None:
            result['need_check'] = self.need_check

        if self.promotion_code is not None:
            result['promotion_code'] = self.promotion_code

        if self.promotion_id is not None:
            result['promotion_id'] = self.promotion_id

        if self.promotion_name is not None:
            result['promotion_name'] = self.promotion_name

        if self.promotion_price is not None:
            result['promotion_price'] = self.promotion_price

        if self.promotion_type is not None:
            result['promotion_type'] = self.promotion_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_status') is not None:
            self.check_status = m.get('check_status')

        if m.get('need_check') is not None:
            self.need_check = m.get('need_check')

        if m.get('promotion_code') is not None:
            self.promotion_code = m.get('promotion_code')

        if m.get('promotion_id') is not None:
            self.promotion_id = m.get('promotion_id')

        if m.get('promotion_name') is not None:
            self.promotion_name = m.get('promotion_name')

        if m.get('promotion_price') is not None:
            self.promotion_price = m.get('promotion_price')

        if m.get('promotion_type') is not None:
            self.promotion_type = m.get('promotion_type')

        return self

class HotelOrderPreValidateResponseBodyModuleItemInvoice(DaraModel):
    def __init__(
        self,
        support_special: bool = None,
    ):
        self.support_special = support_special

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.support_special is not None:
            result['support_special'] = self.support_special

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('support_special') is not None:
            self.support_special = m.get('support_special')

        return self

