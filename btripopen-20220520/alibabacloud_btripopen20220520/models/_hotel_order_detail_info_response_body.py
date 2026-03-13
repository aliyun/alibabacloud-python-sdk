# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelOrderDetailInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.HotelOrderDetailInfoResponseBodyModule = None,
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
            temp_model = main_models.HotelOrderDetailInfoResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class HotelOrderDetailInfoResponseBodyModule(DaraModel):
    def __init__(
        self,
        actual_check_in_time: str = None,
        actual_check_out_time: str = None,
        btrip_hotel_cancel_policy_dto: main_models.HotelOrderDetailInfoResponseBodyModuleBtripHotelCancelPolicyDTO = None,
        btrip_order_id: str = None,
        cancel_fine: int = None,
        cancel_info: main_models.HotelOrderDetailInfoResponseBodyModuleCancelInfo = None,
        check_in: str = None,
        check_out: str = None,
        confirm_order_time: str = None,
        contract_name: str = None,
        contract_tel: str = None,
        create_order_time: str = None,
        early_arrival_time: str = None,
        early_departure: bool = None,
        guest_count: int = None,
        hotel_detail_info: main_models.HotelOrderDetailInfoResponseBodyModuleHotelDetailInfo = None,
        hotel_sale_order_room_infos: List[main_models.HotelOrderDetailInfoResponseBodyModuleHotelSaleOrderRoomInfos] = None,
        invoice_info: main_models.HotelOrderDetailInfoResponseBodyModuleInvoiceInfo = None,
        item_id: str = None,
        last_arrival_time: str = None,
        occupant_info_list: List[main_models.HotelOrderDetailInfoResponseBodyModuleOccupantInfoList] = None,
        order_status: int = None,
        order_status_desc: str = None,
        out_confirm_code: str = None,
        pay_time: str = None,
        product_type: int = None,
        purchase_order_id: str = None,
        refund_price: int = None,
        refund_reason: str = None,
        refund_service_fee: int = None,
        room_night_price_info_list: List[main_models.HotelOrderDetailInfoResponseBodyModuleRoomNightPriceInfoList] = None,
        room_number: int = None,
        room_type_name: str = None,
        seller_id: str = None,
        seller_name: str = None,
        service_fee: int = None,
        settle_type: str = None,
        supplier_order_id: str = None,
        total_price: int = None,
    ):
        self.actual_check_in_time = actual_check_in_time
        self.actual_check_out_time = actual_check_out_time
        self.btrip_hotel_cancel_policy_dto = btrip_hotel_cancel_policy_dto
        self.btrip_order_id = btrip_order_id
        self.cancel_fine = cancel_fine
        self.cancel_info = cancel_info
        self.check_in = check_in
        self.check_out = check_out
        self.confirm_order_time = confirm_order_time
        self.contract_name = contract_name
        self.contract_tel = contract_tel
        self.create_order_time = create_order_time
        self.early_arrival_time = early_arrival_time
        self.early_departure = early_departure
        self.guest_count = guest_count
        self.hotel_detail_info = hotel_detail_info
        self.hotel_sale_order_room_infos = hotel_sale_order_room_infos
        self.invoice_info = invoice_info
        self.item_id = item_id
        self.last_arrival_time = last_arrival_time
        self.occupant_info_list = occupant_info_list
        self.order_status = order_status
        self.order_status_desc = order_status_desc
        self.out_confirm_code = out_confirm_code
        self.pay_time = pay_time
        self.product_type = product_type
        self.purchase_order_id = purchase_order_id
        self.refund_price = refund_price
        self.refund_reason = refund_reason
        self.refund_service_fee = refund_service_fee
        self.room_night_price_info_list = room_night_price_info_list
        self.room_number = room_number
        self.room_type_name = room_type_name
        self.seller_id = seller_id
        self.seller_name = seller_name
        self.service_fee = service_fee
        self.settle_type = settle_type
        self.supplier_order_id = supplier_order_id
        self.total_price = total_price

    def validate(self):
        if self.btrip_hotel_cancel_policy_dto:
            self.btrip_hotel_cancel_policy_dto.validate()
        if self.cancel_info:
            self.cancel_info.validate()
        if self.hotel_detail_info:
            self.hotel_detail_info.validate()
        if self.hotel_sale_order_room_infos:
            for v1 in self.hotel_sale_order_room_infos:
                 if v1:
                    v1.validate()
        if self.invoice_info:
            self.invoice_info.validate()
        if self.occupant_info_list:
            for v1 in self.occupant_info_list:
                 if v1:
                    v1.validate()
        if self.room_night_price_info_list:
            for v1 in self.room_night_price_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_check_in_time is not None:
            result['actual_check_in_time'] = self.actual_check_in_time

        if self.actual_check_out_time is not None:
            result['actual_check_out_time'] = self.actual_check_out_time

        if self.btrip_hotel_cancel_policy_dto is not None:
            result['btrip_hotel_cancel_policy_d_t_o'] = self.btrip_hotel_cancel_policy_dto.to_map()

        if self.btrip_order_id is not None:
            result['btrip_order_id'] = self.btrip_order_id

        if self.cancel_fine is not None:
            result['cancel_fine'] = self.cancel_fine

        if self.cancel_info is not None:
            result['cancel_info'] = self.cancel_info.to_map()

        if self.check_in is not None:
            result['check_in'] = self.check_in

        if self.check_out is not None:
            result['check_out'] = self.check_out

        if self.confirm_order_time is not None:
            result['confirm_order_time'] = self.confirm_order_time

        if self.contract_name is not None:
            result['contract_name'] = self.contract_name

        if self.contract_tel is not None:
            result['contract_tel'] = self.contract_tel

        if self.create_order_time is not None:
            result['create_order_time'] = self.create_order_time

        if self.early_arrival_time is not None:
            result['early_arrival_time'] = self.early_arrival_time

        if self.early_departure is not None:
            result['early_departure'] = self.early_departure

        if self.guest_count is not None:
            result['guest_count'] = self.guest_count

        if self.hotel_detail_info is not None:
            result['hotel_detail_info'] = self.hotel_detail_info.to_map()

        result['hotel_sale_order_room_infos'] = []
        if self.hotel_sale_order_room_infos is not None:
            for k1 in self.hotel_sale_order_room_infos:
                result['hotel_sale_order_room_infos'].append(k1.to_map() if k1 else None)

        if self.invoice_info is not None:
            result['invoice_info'] = self.invoice_info.to_map()

        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.last_arrival_time is not None:
            result['last_arrival_time'] = self.last_arrival_time

        result['occupant_info_list'] = []
        if self.occupant_info_list is not None:
            for k1 in self.occupant_info_list:
                result['occupant_info_list'].append(k1.to_map() if k1 else None)

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.order_status_desc is not None:
            result['order_status_desc'] = self.order_status_desc

        if self.out_confirm_code is not None:
            result['out_confirm_code'] = self.out_confirm_code

        if self.pay_time is not None:
            result['pay_time'] = self.pay_time

        if self.product_type is not None:
            result['product_type'] = self.product_type

        if self.purchase_order_id is not None:
            result['purchase_order_id'] = self.purchase_order_id

        if self.refund_price is not None:
            result['refund_price'] = self.refund_price

        if self.refund_reason is not None:
            result['refund_reason'] = self.refund_reason

        if self.refund_service_fee is not None:
            result['refund_service_fee'] = self.refund_service_fee

        result['room_night_price_info_list'] = []
        if self.room_night_price_info_list is not None:
            for k1 in self.room_night_price_info_list:
                result['room_night_price_info_list'].append(k1.to_map() if k1 else None)

        if self.room_number is not None:
            result['room_number'] = self.room_number

        if self.room_type_name is not None:
            result['room_type_name'] = self.room_type_name

        if self.seller_id is not None:
            result['seller_id'] = self.seller_id

        if self.seller_name is not None:
            result['seller_name'] = self.seller_name

        if self.service_fee is not None:
            result['service_fee'] = self.service_fee

        if self.settle_type is not None:
            result['settle_type'] = self.settle_type

        if self.supplier_order_id is not None:
            result['supplier_order_id'] = self.supplier_order_id

        if self.total_price is not None:
            result['total_price'] = self.total_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actual_check_in_time') is not None:
            self.actual_check_in_time = m.get('actual_check_in_time')

        if m.get('actual_check_out_time') is not None:
            self.actual_check_out_time = m.get('actual_check_out_time')

        if m.get('btrip_hotel_cancel_policy_d_t_o') is not None:
            temp_model = main_models.HotelOrderDetailInfoResponseBodyModuleBtripHotelCancelPolicyDTO()
            self.btrip_hotel_cancel_policy_dto = temp_model.from_map(m.get('btrip_hotel_cancel_policy_d_t_o'))

        if m.get('btrip_order_id') is not None:
            self.btrip_order_id = m.get('btrip_order_id')

        if m.get('cancel_fine') is not None:
            self.cancel_fine = m.get('cancel_fine')

        if m.get('cancel_info') is not None:
            temp_model = main_models.HotelOrderDetailInfoResponseBodyModuleCancelInfo()
            self.cancel_info = temp_model.from_map(m.get('cancel_info'))

        if m.get('check_in') is not None:
            self.check_in = m.get('check_in')

        if m.get('check_out') is not None:
            self.check_out = m.get('check_out')

        if m.get('confirm_order_time') is not None:
            self.confirm_order_time = m.get('confirm_order_time')

        if m.get('contract_name') is not None:
            self.contract_name = m.get('contract_name')

        if m.get('contract_tel') is not None:
            self.contract_tel = m.get('contract_tel')

        if m.get('create_order_time') is not None:
            self.create_order_time = m.get('create_order_time')

        if m.get('early_arrival_time') is not None:
            self.early_arrival_time = m.get('early_arrival_time')

        if m.get('early_departure') is not None:
            self.early_departure = m.get('early_departure')

        if m.get('guest_count') is not None:
            self.guest_count = m.get('guest_count')

        if m.get('hotel_detail_info') is not None:
            temp_model = main_models.HotelOrderDetailInfoResponseBodyModuleHotelDetailInfo()
            self.hotel_detail_info = temp_model.from_map(m.get('hotel_detail_info'))

        self.hotel_sale_order_room_infos = []
        if m.get('hotel_sale_order_room_infos') is not None:
            for k1 in m.get('hotel_sale_order_room_infos'):
                temp_model = main_models.HotelOrderDetailInfoResponseBodyModuleHotelSaleOrderRoomInfos()
                self.hotel_sale_order_room_infos.append(temp_model.from_map(k1))

        if m.get('invoice_info') is not None:
            temp_model = main_models.HotelOrderDetailInfoResponseBodyModuleInvoiceInfo()
            self.invoice_info = temp_model.from_map(m.get('invoice_info'))

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('last_arrival_time') is not None:
            self.last_arrival_time = m.get('last_arrival_time')

        self.occupant_info_list = []
        if m.get('occupant_info_list') is not None:
            for k1 in m.get('occupant_info_list'):
                temp_model = main_models.HotelOrderDetailInfoResponseBodyModuleOccupantInfoList()
                self.occupant_info_list.append(temp_model.from_map(k1))

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('order_status_desc') is not None:
            self.order_status_desc = m.get('order_status_desc')

        if m.get('out_confirm_code') is not None:
            self.out_confirm_code = m.get('out_confirm_code')

        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')

        if m.get('product_type') is not None:
            self.product_type = m.get('product_type')

        if m.get('purchase_order_id') is not None:
            self.purchase_order_id = m.get('purchase_order_id')

        if m.get('refund_price') is not None:
            self.refund_price = m.get('refund_price')

        if m.get('refund_reason') is not None:
            self.refund_reason = m.get('refund_reason')

        if m.get('refund_service_fee') is not None:
            self.refund_service_fee = m.get('refund_service_fee')

        self.room_night_price_info_list = []
        if m.get('room_night_price_info_list') is not None:
            for k1 in m.get('room_night_price_info_list'):
                temp_model = main_models.HotelOrderDetailInfoResponseBodyModuleRoomNightPriceInfoList()
                self.room_night_price_info_list.append(temp_model.from_map(k1))

        if m.get('room_number') is not None:
            self.room_number = m.get('room_number')

        if m.get('room_type_name') is not None:
            self.room_type_name = m.get('room_type_name')

        if m.get('seller_id') is not None:
            self.seller_id = m.get('seller_id')

        if m.get('seller_name') is not None:
            self.seller_name = m.get('seller_name')

        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')

        if m.get('settle_type') is not None:
            self.settle_type = m.get('settle_type')

        if m.get('supplier_order_id') is not None:
            self.supplier_order_id = m.get('supplier_order_id')

        if m.get('total_price') is not None:
            self.total_price = m.get('total_price')

        return self

class HotelOrderDetailInfoResponseBodyModuleRoomNightPriceInfoList(DaraModel):
    def __init__(
        self,
        board: str = None,
        board_num: int = None,
        check_in: str = None,
        rate_plan_id: str = None,
        rate_plan_name: str = None,
        room_id: str = None,
        room_name: str = None,
        room_price: int = None,
    ):
        self.board = board
        self.board_num = board_num
        self.check_in = check_in
        self.rate_plan_id = rate_plan_id
        self.rate_plan_name = rate_plan_name
        self.room_id = room_id
        self.room_name = room_name
        self.room_price = room_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.board is not None:
            result['board'] = self.board

        if self.board_num is not None:
            result['board_num'] = self.board_num

        if self.check_in is not None:
            result['check_in'] = self.check_in

        if self.rate_plan_id is not None:
            result['rate_plan_id'] = self.rate_plan_id

        if self.rate_plan_name is not None:
            result['rate_plan_name'] = self.rate_plan_name

        if self.room_id is not None:
            result['room_id'] = self.room_id

        if self.room_name is not None:
            result['room_name'] = self.room_name

        if self.room_price is not None:
            result['room_price'] = self.room_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('board') is not None:
            self.board = m.get('board')

        if m.get('board_num') is not None:
            self.board_num = m.get('board_num')

        if m.get('check_in') is not None:
            self.check_in = m.get('check_in')

        if m.get('rate_plan_id') is not None:
            self.rate_plan_id = m.get('rate_plan_id')

        if m.get('rate_plan_name') is not None:
            self.rate_plan_name = m.get('rate_plan_name')

        if m.get('room_id') is not None:
            self.room_id = m.get('room_id')

        if m.get('room_name') is not None:
            self.room_name = m.get('room_name')

        if m.get('room_price') is not None:
            self.room_price = m.get('room_price')

        return self

class HotelOrderDetailInfoResponseBodyModuleOccupantInfoList(DaraModel):
    def __init__(
        self,
        card_no: str = None,
        card_type: int = None,
        cost_center_info_list: List[main_models.HotelOrderDetailInfoResponseBodyModuleOccupantInfoListCostCenterInfoList] = None,
        customer_type: int = None,
        department_id: str = None,
        department_name: str = None,
        email: str = None,
        employee_type: int = None,
        first_name: str = None,
        is_booker: bool = None,
        last_name: str = None,
        name: str = None,
        phone: str = None,
        room_no: int = None,
        selected: bool = None,
        staff_no: str = None,
        user_type: int = None,
    ):
        self.card_no = card_no
        self.card_type = card_type
        self.cost_center_info_list = cost_center_info_list
        self.customer_type = customer_type
        self.department_id = department_id
        self.department_name = department_name
        self.email = email
        self.employee_type = employee_type
        self.first_name = first_name
        self.is_booker = is_booker
        self.last_name = last_name
        self.name = name
        self.phone = phone
        self.room_no = room_no
        self.selected = selected
        self.staff_no = staff_no
        self.user_type = user_type

    def validate(self):
        if self.cost_center_info_list:
            for v1 in self.cost_center_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_no is not None:
            result['card_no'] = self.card_no

        if self.card_type is not None:
            result['card_type'] = self.card_type

        result['cost_center_info_list'] = []
        if self.cost_center_info_list is not None:
            for k1 in self.cost_center_info_list:
                result['cost_center_info_list'].append(k1.to_map() if k1 else None)

        if self.customer_type is not None:
            result['customer_type'] = self.customer_type

        if self.department_id is not None:
            result['department_id'] = self.department_id

        if self.department_name is not None:
            result['department_name'] = self.department_name

        if self.email is not None:
            result['email'] = self.email

        if self.employee_type is not None:
            result['employee_type'] = self.employee_type

        if self.first_name is not None:
            result['first_name'] = self.first_name

        if self.is_booker is not None:
            result['is_booker'] = self.is_booker

        if self.last_name is not None:
            result['last_name'] = self.last_name

        if self.name is not None:
            result['name'] = self.name

        if self.phone is not None:
            result['phone'] = self.phone

        if self.room_no is not None:
            result['room_no'] = self.room_no

        if self.selected is not None:
            result['selected'] = self.selected

        if self.staff_no is not None:
            result['staff_no'] = self.staff_no

        if self.user_type is not None:
            result['user_type'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('card_no') is not None:
            self.card_no = m.get('card_no')

        if m.get('card_type') is not None:
            self.card_type = m.get('card_type')

        self.cost_center_info_list = []
        if m.get('cost_center_info_list') is not None:
            for k1 in m.get('cost_center_info_list'):
                temp_model = main_models.HotelOrderDetailInfoResponseBodyModuleOccupantInfoListCostCenterInfoList()
                self.cost_center_info_list.append(temp_model.from_map(k1))

        if m.get('customer_type') is not None:
            self.customer_type = m.get('customer_type')

        if m.get('department_id') is not None:
            self.department_id = m.get('department_id')

        if m.get('department_name') is not None:
            self.department_name = m.get('department_name')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('employee_type') is not None:
            self.employee_type = m.get('employee_type')

        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')

        if m.get('is_booker') is not None:
            self.is_booker = m.get('is_booker')

        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('room_no') is not None:
            self.room_no = m.get('room_no')

        if m.get('selected') is not None:
            self.selected = m.get('selected')

        if m.get('staff_no') is not None:
            self.staff_no = m.get('staff_no')

        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')

        return self

class HotelOrderDetailInfoResponseBodyModuleOccupantInfoListCostCenterInfoList(DaraModel):
    def __init__(
        self,
        cost_center_id: str = None,
        cost_center_name: str = None,
        cost_center_no: str = None,
        cost_center_prices: int = None,
        cost_center_ratios: int = None,
        cost_center_subject_code: str = None,
        cost_center_subject_name: str = None,
        settle_subject_id: str = None,
        settle_subject_name: str = None,
        settle_subject_no: str = None,
    ):
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.cost_center_no = cost_center_no
        self.cost_center_prices = cost_center_prices
        self.cost_center_ratios = cost_center_ratios
        self.cost_center_subject_code = cost_center_subject_code
        self.cost_center_subject_name = cost_center_subject_name
        self.settle_subject_id = settle_subject_id
        self.settle_subject_name = settle_subject_name
        self.settle_subject_no = settle_subject_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id

        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name

        if self.cost_center_no is not None:
            result['cost_center_no'] = self.cost_center_no

        if self.cost_center_prices is not None:
            result['cost_center_prices'] = self.cost_center_prices

        if self.cost_center_ratios is not None:
            result['cost_center_ratios'] = self.cost_center_ratios

        if self.cost_center_subject_code is not None:
            result['cost_center_subject_code'] = self.cost_center_subject_code

        if self.cost_center_subject_name is not None:
            result['cost_center_subject_name'] = self.cost_center_subject_name

        if self.settle_subject_id is not None:
            result['settle_subject_id'] = self.settle_subject_id

        if self.settle_subject_name is not None:
            result['settle_subject_name'] = self.settle_subject_name

        if self.settle_subject_no is not None:
            result['settle_subject_no'] = self.settle_subject_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('cost_center_no') is not None:
            self.cost_center_no = m.get('cost_center_no')

        if m.get('cost_center_prices') is not None:
            self.cost_center_prices = m.get('cost_center_prices')

        if m.get('cost_center_ratios') is not None:
            self.cost_center_ratios = m.get('cost_center_ratios')

        if m.get('cost_center_subject_code') is not None:
            self.cost_center_subject_code = m.get('cost_center_subject_code')

        if m.get('cost_center_subject_name') is not None:
            self.cost_center_subject_name = m.get('cost_center_subject_name')

        if m.get('settle_subject_id') is not None:
            self.settle_subject_id = m.get('settle_subject_id')

        if m.get('settle_subject_name') is not None:
            self.settle_subject_name = m.get('settle_subject_name')

        if m.get('settle_subject_no') is not None:
            self.settle_subject_no = m.get('settle_subject_no')

        return self

class HotelOrderDetailInfoResponseBodyModuleInvoiceInfo(DaraModel):
    def __init__(
        self,
        billing_money: int = None,
        buyer_add: str = None,
        buyer_bank_acc: str = None,
        buyer_bank_add: str = None,
        buyer_phone: str = None,
        buyer_tax_num: str = None,
        delivery_address: str = None,
        delivery_area: str = None,
        delivery_city: str = None,
        delivery_province: str = None,
        delivery_street: str = None,
        email: str = None,
        invoice_material: int = None,
        invoice_title: str = None,
        invoice_type: int = None,
        postage: int = None,
        receiver_name: str = None,
        receiver_phone: str = None,
        remark: str = None,
    ):
        self.billing_money = billing_money
        self.buyer_add = buyer_add
        self.buyer_bank_acc = buyer_bank_acc
        self.buyer_bank_add = buyer_bank_add
        self.buyer_phone = buyer_phone
        self.buyer_tax_num = buyer_tax_num
        self.delivery_address = delivery_address
        self.delivery_area = delivery_area
        self.delivery_city = delivery_city
        self.delivery_province = delivery_province
        self.delivery_street = delivery_street
        self.email = email
        self.invoice_material = invoice_material
        self.invoice_title = invoice_title
        self.invoice_type = invoice_type
        self.postage = postage
        self.receiver_name = receiver_name
        self.receiver_phone = receiver_phone
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_money is not None:
            result['billing_money'] = self.billing_money

        if self.buyer_add is not None:
            result['buyer_add'] = self.buyer_add

        if self.buyer_bank_acc is not None:
            result['buyer_bank_acc'] = self.buyer_bank_acc

        if self.buyer_bank_add is not None:
            result['buyer_bank_add'] = self.buyer_bank_add

        if self.buyer_phone is not None:
            result['buyer_phone'] = self.buyer_phone

        if self.buyer_tax_num is not None:
            result['buyer_tax_num'] = self.buyer_tax_num

        if self.delivery_address is not None:
            result['delivery_address'] = self.delivery_address

        if self.delivery_area is not None:
            result['delivery_area'] = self.delivery_area

        if self.delivery_city is not None:
            result['delivery_city'] = self.delivery_city

        if self.delivery_province is not None:
            result['delivery_province'] = self.delivery_province

        if self.delivery_street is not None:
            result['delivery_street'] = self.delivery_street

        if self.email is not None:
            result['email'] = self.email

        if self.invoice_material is not None:
            result['invoice_material'] = self.invoice_material

        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title

        if self.invoice_type is not None:
            result['invoice_type'] = self.invoice_type

        if self.postage is not None:
            result['postage'] = self.postage

        if self.receiver_name is not None:
            result['receiver_name'] = self.receiver_name

        if self.receiver_phone is not None:
            result['receiver_phone'] = self.receiver_phone

        if self.remark is not None:
            result['remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('billing_money') is not None:
            self.billing_money = m.get('billing_money')

        if m.get('buyer_add') is not None:
            self.buyer_add = m.get('buyer_add')

        if m.get('buyer_bank_acc') is not None:
            self.buyer_bank_acc = m.get('buyer_bank_acc')

        if m.get('buyer_bank_add') is not None:
            self.buyer_bank_add = m.get('buyer_bank_add')

        if m.get('buyer_phone') is not None:
            self.buyer_phone = m.get('buyer_phone')

        if m.get('buyer_tax_num') is not None:
            self.buyer_tax_num = m.get('buyer_tax_num')

        if m.get('delivery_address') is not None:
            self.delivery_address = m.get('delivery_address')

        if m.get('delivery_area') is not None:
            self.delivery_area = m.get('delivery_area')

        if m.get('delivery_city') is not None:
            self.delivery_city = m.get('delivery_city')

        if m.get('delivery_province') is not None:
            self.delivery_province = m.get('delivery_province')

        if m.get('delivery_street') is not None:
            self.delivery_street = m.get('delivery_street')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('invoice_material') is not None:
            self.invoice_material = m.get('invoice_material')

        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')

        if m.get('invoice_type') is not None:
            self.invoice_type = m.get('invoice_type')

        if m.get('postage') is not None:
            self.postage = m.get('postage')

        if m.get('receiver_name') is not None:
            self.receiver_name = m.get('receiver_name')

        if m.get('receiver_phone') is not None:
            self.receiver_phone = m.get('receiver_phone')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        return self

class HotelOrderDetailInfoResponseBodyModuleHotelSaleOrderRoomInfos(DaraModel):
    def __init__(
        self,
        checkin_date: str = None,
        checkout_date: str = None,
        penal_sum: int = None,
        real_checkout_date: str = None,
        refund_status: int = None,
        room_no: int = None,
        room_price: int = None,
        room_refund_price: int = None,
        traveler_id: str = None,
        traveler_name: str = None,
    ):
        self.checkin_date = checkin_date
        self.checkout_date = checkout_date
        self.penal_sum = penal_sum
        self.real_checkout_date = real_checkout_date
        self.refund_status = refund_status
        self.room_no = room_no
        self.room_price = room_price
        self.room_refund_price = room_refund_price
        self.traveler_id = traveler_id
        self.traveler_name = traveler_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkin_date is not None:
            result['checkin_date'] = self.checkin_date

        if self.checkout_date is not None:
            result['checkout_date'] = self.checkout_date

        if self.penal_sum is not None:
            result['penal_sum'] = self.penal_sum

        if self.real_checkout_date is not None:
            result['real_checkout_date'] = self.real_checkout_date

        if self.refund_status is not None:
            result['refund_status'] = self.refund_status

        if self.room_no is not None:
            result['room_no'] = self.room_no

        if self.room_price is not None:
            result['room_price'] = self.room_price

        if self.room_refund_price is not None:
            result['room_refund_price'] = self.room_refund_price

        if self.traveler_id is not None:
            result['traveler_id'] = self.traveler_id

        if self.traveler_name is not None:
            result['traveler_name'] = self.traveler_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkin_date') is not None:
            self.checkin_date = m.get('checkin_date')

        if m.get('checkout_date') is not None:
            self.checkout_date = m.get('checkout_date')

        if m.get('penal_sum') is not None:
            self.penal_sum = m.get('penal_sum')

        if m.get('real_checkout_date') is not None:
            self.real_checkout_date = m.get('real_checkout_date')

        if m.get('refund_status') is not None:
            self.refund_status = m.get('refund_status')

        if m.get('room_no') is not None:
            self.room_no = m.get('room_no')

        if m.get('room_price') is not None:
            self.room_price = m.get('room_price')

        if m.get('room_refund_price') is not None:
            self.room_refund_price = m.get('room_refund_price')

        if m.get('traveler_id') is not None:
            self.traveler_id = m.get('traveler_id')

        if m.get('traveler_name') is not None:
            self.traveler_name = m.get('traveler_name')

        return self

class HotelOrderDetailInfoResponseBodyModuleHotelDetailInfo(DaraModel):
    def __init__(
        self,
        address: str = None,
        city_name: str = None,
        hotel_name: str = None,
        hotel_tel: str = None,
        shid: int = None,
    ):
        self.address = address
        self.city_name = city_name
        self.hotel_name = hotel_name
        self.hotel_tel = hotel_tel
        self.shid = shid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.hotel_name is not None:
            result['hotel_name'] = self.hotel_name

        if self.hotel_tel is not None:
            result['hotel_tel'] = self.hotel_tel

        if self.shid is not None:
            result['shid'] = self.shid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('hotel_name') is not None:
            self.hotel_name = m.get('hotel_name')

        if m.get('hotel_tel') is not None:
            self.hotel_tel = m.get('hotel_tel')

        if m.get('shid') is not None:
            self.shid = m.get('shid')

        return self

class HotelOrderDetailInfoResponseBodyModuleCancelInfo(DaraModel):
    def __init__(
        self,
        cancel_end_time: str = None,
        cancel_start_time: str = None,
    ):
        self.cancel_end_time = cancel_end_time
        self.cancel_start_time = cancel_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancel_end_time is not None:
            result['cancel_end_time'] = self.cancel_end_time

        if self.cancel_start_time is not None:
            result['cancel_start_time'] = self.cancel_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cancel_end_time') is not None:
            self.cancel_end_time = m.get('cancel_end_time')

        if m.get('cancel_start_time') is not None:
            self.cancel_start_time = m.get('cancel_start_time')

        return self

class HotelOrderDetailInfoResponseBodyModuleBtripHotelCancelPolicyDTO(DaraModel):
    def __init__(
        self,
        btrip_hotel_cancel_policy_info_dtolist: List[main_models.HotelOrderDetailInfoResponseBodyModuleBtripHotelCancelPolicyDTOBtripHotelCancelPolicyInfoDTOList] = None,
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
                temp_model = main_models.HotelOrderDetailInfoResponseBodyModuleBtripHotelCancelPolicyDTOBtripHotelCancelPolicyInfoDTOList()
                self.btrip_hotel_cancel_policy_info_dtolist.append(temp_model.from_map(k1))

        if m.get('cancel_policy_type') is not None:
            self.cancel_policy_type = m.get('cancel_policy_type')

        return self

class HotelOrderDetailInfoResponseBodyModuleBtripHotelCancelPolicyDTOBtripHotelCancelPolicyInfoDTOList(DaraModel):
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

