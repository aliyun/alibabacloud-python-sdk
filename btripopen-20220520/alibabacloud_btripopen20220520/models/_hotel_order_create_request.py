# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class HotelOrderCreateRequest(DaraModel):
    def __init__(
        self,
        btrip_user_id: str = None,
        check_in: str = None,
        check_out: str = None,
        contract_email: str = None,
        contract_name: str = None,
        contract_phone: str = None,
        corp_pay_price: int = None,
        dis_order_id: str = None,
        extra: str = None,
        invoice_info: main_models.HotelOrderCreateRequestInvoiceInfo = None,
        item_id: int = None,
        itinerary_no: str = None,
        member_info: main_models.HotelOrderCreateRequestMemberInfo = None,
        occupant_info_list: List[main_models.HotelOrderCreateRequestOccupantInfoList] = None,
        person_pay_price: int = None,
        promotion_info: main_models.HotelOrderCreateRequestPromotionInfo = None,
        rate_plan_id: int = None,
        room_id: int = None,
        room_num: int = None,
        seller_id: int = None,
        shid: int = None,
        total_order_price: int = None,
        validate_res_key: str = None,
    ):
        # This parameter is required.
        self.btrip_user_id = btrip_user_id
        # This parameter is required.
        self.check_in = check_in
        # This parameter is required.
        self.check_out = check_out
        self.contract_email = contract_email
        self.contract_name = contract_name
        # This parameter is required.
        self.contract_phone = contract_phone
        # This parameter is required.
        self.corp_pay_price = corp_pay_price
        # This parameter is required.
        self.dis_order_id = dis_order_id
        self.extra = extra
        self.invoice_info = invoice_info
        # This parameter is required.
        self.item_id = item_id
        # This parameter is required.
        self.itinerary_no = itinerary_no
        self.member_info = member_info
        # This parameter is required.
        self.occupant_info_list = occupant_info_list
        # This parameter is required.
        self.person_pay_price = person_pay_price
        self.promotion_info = promotion_info
        # This parameter is required.
        self.rate_plan_id = rate_plan_id
        # This parameter is required.
        self.room_id = room_id
        # This parameter is required.
        self.room_num = room_num
        # This parameter is required.
        self.seller_id = seller_id
        # This parameter is required.
        self.shid = shid
        # This parameter is required.
        self.total_order_price = total_order_price
        # This parameter is required.
        self.validate_res_key = validate_res_key

    def validate(self):
        if self.invoice_info:
            self.invoice_info.validate()
        if self.member_info:
            self.member_info.validate()
        if self.occupant_info_list:
            for v1 in self.occupant_info_list:
                 if v1:
                    v1.validate()
        if self.promotion_info:
            self.promotion_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.check_in is not None:
            result['check_in'] = self.check_in

        if self.check_out is not None:
            result['check_out'] = self.check_out

        if self.contract_email is not None:
            result['contract_email'] = self.contract_email

        if self.contract_name is not None:
            result['contract_name'] = self.contract_name

        if self.contract_phone is not None:
            result['contract_phone'] = self.contract_phone

        if self.corp_pay_price is not None:
            result['corp_pay_price'] = self.corp_pay_price

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.extra is not None:
            result['extra'] = self.extra

        if self.invoice_info is not None:
            result['invoice_info'] = self.invoice_info.to_map()

        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.itinerary_no is not None:
            result['itinerary_no'] = self.itinerary_no

        if self.member_info is not None:
            result['member_info'] = self.member_info.to_map()

        result['occupant_info_list'] = []
        if self.occupant_info_list is not None:
            for k1 in self.occupant_info_list:
                result['occupant_info_list'].append(k1.to_map() if k1 else None)

        if self.person_pay_price is not None:
            result['person_pay_price'] = self.person_pay_price

        if self.promotion_info is not None:
            result['promotion_info'] = self.promotion_info.to_map()

        if self.rate_plan_id is not None:
            result['rate_plan_id'] = self.rate_plan_id

        if self.room_id is not None:
            result['room_id'] = self.room_id

        if self.room_num is not None:
            result['room_num'] = self.room_num

        if self.seller_id is not None:
            result['seller_id'] = self.seller_id

        if self.shid is not None:
            result['shid'] = self.shid

        if self.total_order_price is not None:
            result['total_order_price'] = self.total_order_price

        if self.validate_res_key is not None:
            result['validate_res_key'] = self.validate_res_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('check_in') is not None:
            self.check_in = m.get('check_in')

        if m.get('check_out') is not None:
            self.check_out = m.get('check_out')

        if m.get('contract_email') is not None:
            self.contract_email = m.get('contract_email')

        if m.get('contract_name') is not None:
            self.contract_name = m.get('contract_name')

        if m.get('contract_phone') is not None:
            self.contract_phone = m.get('contract_phone')

        if m.get('corp_pay_price') is not None:
            self.corp_pay_price = m.get('corp_pay_price')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('invoice_info') is not None:
            temp_model = main_models.HotelOrderCreateRequestInvoiceInfo()
            self.invoice_info = temp_model.from_map(m.get('invoice_info'))

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('itinerary_no') is not None:
            self.itinerary_no = m.get('itinerary_no')

        if m.get('member_info') is not None:
            temp_model = main_models.HotelOrderCreateRequestMemberInfo()
            self.member_info = temp_model.from_map(m.get('member_info'))

        self.occupant_info_list = []
        if m.get('occupant_info_list') is not None:
            for k1 in m.get('occupant_info_list'):
                temp_model = main_models.HotelOrderCreateRequestOccupantInfoList()
                self.occupant_info_list.append(temp_model.from_map(k1))

        if m.get('person_pay_price') is not None:
            self.person_pay_price = m.get('person_pay_price')

        if m.get('promotion_info') is not None:
            temp_model = main_models.HotelOrderCreateRequestPromotionInfo()
            self.promotion_info = temp_model.from_map(m.get('promotion_info'))

        if m.get('rate_plan_id') is not None:
            self.rate_plan_id = m.get('rate_plan_id')

        if m.get('room_id') is not None:
            self.room_id = m.get('room_id')

        if m.get('room_num') is not None:
            self.room_num = m.get('room_num')

        if m.get('seller_id') is not None:
            self.seller_id = m.get('seller_id')

        if m.get('shid') is not None:
            self.shid = m.get('shid')

        if m.get('total_order_price') is not None:
            self.total_order_price = m.get('total_order_price')

        if m.get('validate_res_key') is not None:
            self.validate_res_key = m.get('validate_res_key')

        return self

class HotelOrderCreateRequestPromotionInfo(DaraModel):
    def __init__(
        self,
        promotion_detail_info_list: List[main_models.HotelOrderCreateRequestPromotionInfoPromotionDetailInfoList] = None,
        promotion_total_price: int = None,
    ):
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
        result['promotion_detail_info_list'] = []
        if self.promotion_detail_info_list is not None:
            for k1 in self.promotion_detail_info_list:
                result['promotion_detail_info_list'].append(k1.to_map() if k1 else None)

        if self.promotion_total_price is not None:
            result['promotion_total_price'] = self.promotion_total_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.promotion_detail_info_list = []
        if m.get('promotion_detail_info_list') is not None:
            for k1 in m.get('promotion_detail_info_list'):
                temp_model = main_models.HotelOrderCreateRequestPromotionInfoPromotionDetailInfoList()
                self.promotion_detail_info_list.append(temp_model.from_map(k1))

        if m.get('promotion_total_price') is not None:
            self.promotion_total_price = m.get('promotion_total_price')

        return self

class HotelOrderCreateRequestPromotionInfoPromotionDetailInfoList(DaraModel):
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

class HotelOrderCreateRequestOccupantInfoList(DaraModel):
    def __init__(
        self,
        card_no: str = None,
        card_type: int = None,
        cascade_dept_name: str = None,
        cost_center_info: main_models.HotelOrderCreateRequestOccupantInfoListCostCenterInfo = None,
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
        staff_no: str = None,
        user_type: int = None,
    ):
        self.card_no = card_no
        self.card_type = card_type
        self.cascade_dept_name = cascade_dept_name
        self.cost_center_info = cost_center_info
        self.customer_type = customer_type
        self.department_id = department_id
        self.department_name = department_name
        self.email = email
        self.employee_type = employee_type
        self.first_name = first_name
        self.is_booker = is_booker
        self.last_name = last_name
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.phone = phone
        self.room_no = room_no
        self.staff_no = staff_no
        self.user_type = user_type

    def validate(self):
        if self.cost_center_info:
            self.cost_center_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_no is not None:
            result['card_no'] = self.card_no

        if self.card_type is not None:
            result['card_type'] = self.card_type

        if self.cascade_dept_name is not None:
            result['cascade_dept_name'] = self.cascade_dept_name

        if self.cost_center_info is not None:
            result['cost_center_info'] = self.cost_center_info.to_map()

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

        if m.get('cascade_dept_name') is not None:
            self.cascade_dept_name = m.get('cascade_dept_name')

        if m.get('cost_center_info') is not None:
            temp_model = main_models.HotelOrderCreateRequestOccupantInfoListCostCenterInfo()
            self.cost_center_info = temp_model.from_map(m.get('cost_center_info'))

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

        if m.get('staff_no') is not None:
            self.staff_no = m.get('staff_no')

        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')

        return self

class HotelOrderCreateRequestOccupantInfoListCostCenterInfo(DaraModel):
    def __init__(
        self,
        cost_center_id: str = None,
        cost_center_name: str = None,
        cost_center_no: str = None,
        invoice_id: str = None,
        invoice_title: str = None,
        project_code: str = None,
        project_title: str = None,
    ):
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.cost_center_no = cost_center_no
        self.invoice_id = invoice_id
        self.invoice_title = invoice_title
        self.project_code = project_code
        self.project_title = project_title

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

        if self.invoice_id is not None:
            result['invoice_id'] = self.invoice_id

        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('cost_center_no') is not None:
            self.cost_center_no = m.get('cost_center_no')

        if m.get('invoice_id') is not None:
            self.invoice_id = m.get('invoice_id')

        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        return self

class HotelOrderCreateRequestMemberInfo(DaraModel):
    def __init__(
        self,
        card_no: str = None,
        real_name: str = None,
    ):
        self.card_no = card_no
        self.real_name = real_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_no is not None:
            result['card_no'] = self.card_no

        if self.real_name is not None:
            result['real_name'] = self.real_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('card_no') is not None:
            self.card_no = m.get('card_no')

        if m.get('real_name') is not None:
            self.real_name = m.get('real_name')

        return self

class HotelOrderCreateRequestInvoiceInfo(DaraModel):
    def __init__(
        self,
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
        receiver_name: str = None,
        receiver_phone: str = None,
        remark: str = None,
    ):
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

        if self.receiver_name is not None:
            result['receiver_name'] = self.receiver_name

        if self.receiver_phone is not None:
            result['receiver_phone'] = self.receiver_phone

        if self.remark is not None:
            result['remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('receiver_name') is not None:
            self.receiver_name = m.get('receiver_name')

        if m.get('receiver_phone') is not None:
            self.receiver_phone = m.get('receiver_phone')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        return self

