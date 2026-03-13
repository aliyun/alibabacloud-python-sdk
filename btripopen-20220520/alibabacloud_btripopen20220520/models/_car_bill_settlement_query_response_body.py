# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class CarBillSettlementQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.CarBillSettlementQueryResponseBodyModule = None,
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
            temp_model = main_models.CarBillSettlementQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class CarBillSettlementQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        data_list: List[main_models.CarBillSettlementQueryResponseBodyModuleDataList] = None,
        period_end: str = None,
        period_start: str = None,
        scroll_id: str = None,
        total_num: int = None,
    ):
        self.category = category
        self.corp_id = corp_id
        self.data_list = data_list
        self.period_end = period_end
        self.period_start = period_start
        self.scroll_id = scroll_id
        self.total_num = total_num

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        result['data_list'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['data_list'].append(k1.to_map() if k1 else None)

        if self.period_end is not None:
            result['period_end'] = self.period_end

        if self.period_start is not None:
            result['period_start'] = self.period_start

        if self.scroll_id is not None:
            result['scroll_id'] = self.scroll_id

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
            for k1 in m.get('data_list'):
                temp_model = main_models.CarBillSettlementQueryResponseBodyModuleDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('period_end') is not None:
            self.period_end = m.get('period_end')

        if m.get('period_start') is not None:
            self.period_start = m.get('period_start')

        if m.get('scroll_id') is not None:
            self.scroll_id = m.get('scroll_id')

        if m.get('total_num') is not None:
            self.total_num = m.get('total_num')

        return self

class CarBillSettlementQueryResponseBodyModuleDataList(DaraModel):
    def __init__(
        self,
        adjust_time: str = None,
        alipay_trade_no: str = None,
        apply_arr_city_code: str = None,
        apply_arr_city_name: str = None,
        apply_dep_city_code: str = None,
        apply_dep_city_name: str = None,
        apply_extend_field: str = None,
        apply_id: str = None,
        approver_email: str = None,
        approver_id: str = None,
        approver_name: str = None,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_date: str = None,
        arr_location: str = None,
        arr_time: str = None,
        base_location: str = None,
        bill_record_time: str = None,
        billing_entity: str = None,
        book_model: str = None,
        book_time: str = None,
        booker_id: str = None,
        booker_job_no: str = None,
        booker_name: str = None,
        business_category: str = None,
        capital_direction: str = None,
        car_level: str = None,
        cascade_department: str = None,
        category_desc: str = None,
        cost_center: str = None,
        cost_center_number: str = None,
        cost_department: str = None,
        coupon: float = None,
        coupon_price: float = None,
        custom_content: str = None,
        deductible_tax: float = None,
        dep_city_code: str = None,
        department: str = None,
        department_id: str = None,
        dept_city: str = None,
        dept_date: str = None,
        dept_location: str = None,
        dept_time: str = None,
        driver_add_detail: str = None,
        driver_add_fee: float = None,
        estimate_drive_distance: str = None,
        estimate_price: float = None,
        fee_type: str = None,
        fee_type_desc: str = None,
        foreigners_tag: str = None,
        index: str = None,
        invoice_title: str = None,
        level_name: str = None,
        location: str = None,
        mapping_company_code: str = None,
        memo: str = None,
        order_id: str = None,
        order_price: float = None,
        over_apply_id: str = None,
        payment_department_id: str = None,
        payment_department_name: str = None,
        person_settle_fee: float = None,
        position: str = None,
        position_level: str = None,
        primary_id: int = None,
        processor_oa_code: str = None,
        project_code: str = None,
        project_name: str = None,
        protocol_discount_fee: float = None,
        provider_name: str = None,
        real_drive_distance: str = None,
        real_from_addr: str = None,
        real_to_addr: str = None,
        remark: str = None,
        scene_id: str = None,
        scene_name: str = None,
        service_fee: float = None,
        settle_type_desc: str = None,
        settlement_fee: float = None,
        settlement_grant_fee: float = None,
        settlement_time: str = None,
        settlement_type: str = None,
        sio: str = None,
        special_order: str = None,
        special_reason: str = None,
        status: int = None,
        status_desc: str = None,
        sub_order_id: str = None,
        supplement_apply_id: str = None,
        tax_rate: str = None,
        third_itinerary_id: str = None,
        time_type: str = None,
        trade_action_desc: str = None,
        traveler_email: str = None,
        traveler_id: str = None,
        traveler_job_no: str = None,
        traveler_member_type: str = None,
        traveler_member_type_name: str = None,
        traveler_name: str = None,
        user_confirm_desc: str = None,
        vehicle_scene_id: str = None,
        vehicle_scene_name: str = None,
        voucher_type: int = None,
        voucher_type_desc: str = None,
    ):
        self.adjust_time = adjust_time
        self.alipay_trade_no = alipay_trade_no
        self.apply_arr_city_code = apply_arr_city_code
        self.apply_arr_city_name = apply_arr_city_name
        self.apply_dep_city_code = apply_dep_city_code
        self.apply_dep_city_name = apply_dep_city_name
        # 审批扩展自定义字段
        self.apply_extend_field = apply_extend_field
        self.apply_id = apply_id
        self.approver_email = approver_email
        self.approver_id = approver_id
        self.approver_name = approver_name
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.arr_date = arr_date
        self.arr_location = arr_location
        self.arr_time = arr_time
        self.base_location = base_location
        self.bill_record_time = bill_record_time
        self.billing_entity = billing_entity
        self.book_model = book_model
        self.book_time = book_time
        self.booker_id = booker_id
        self.booker_job_no = booker_job_no
        self.booker_name = booker_name
        self.business_category = business_category
        self.capital_direction = capital_direction
        self.car_level = car_level
        self.cascade_department = cascade_department
        self.category_desc = category_desc
        self.cost_center = cost_center
        self.cost_center_number = cost_center_number
        self.cost_department = cost_department
        self.coupon = coupon
        self.coupon_price = coupon_price
        self.custom_content = custom_content
        self.deductible_tax = deductible_tax
        self.dep_city_code = dep_city_code
        self.department = department
        self.department_id = department_id
        self.dept_city = dept_city
        self.dept_date = dept_date
        self.dept_location = dept_location
        self.dept_time = dept_time
        self.driver_add_detail = driver_add_detail
        self.driver_add_fee = driver_add_fee
        self.estimate_drive_distance = estimate_drive_distance
        self.estimate_price = estimate_price
        self.fee_type = fee_type
        self.fee_type_desc = fee_type_desc
        self.foreigners_tag = foreigners_tag
        self.index = index
        self.invoice_title = invoice_title
        self.level_name = level_name
        self.location = location
        self.mapping_company_code = mapping_company_code
        self.memo = memo
        self.order_id = order_id
        self.order_price = order_price
        self.over_apply_id = over_apply_id
        self.payment_department_id = payment_department_id
        self.payment_department_name = payment_department_name
        self.person_settle_fee = person_settle_fee
        self.position = position
        self.position_level = position_level
        self.primary_id = primary_id
        self.processor_oa_code = processor_oa_code
        self.project_code = project_code
        self.project_name = project_name
        self.protocol_discount_fee = protocol_discount_fee
        self.provider_name = provider_name
        self.real_drive_distance = real_drive_distance
        self.real_from_addr = real_from_addr
        self.real_to_addr = real_to_addr
        self.remark = remark
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.service_fee = service_fee
        self.settle_type_desc = settle_type_desc
        self.settlement_fee = settlement_fee
        self.settlement_grant_fee = settlement_grant_fee
        self.settlement_time = settlement_time
        self.settlement_type = settlement_type
        self.sio = sio
        self.special_order = special_order
        self.special_reason = special_reason
        self.status = status
        self.status_desc = status_desc
        self.sub_order_id = sub_order_id
        self.supplement_apply_id = supplement_apply_id
        # 税率
        self.tax_rate = tax_rate
        self.third_itinerary_id = third_itinerary_id
        self.time_type = time_type
        self.trade_action_desc = trade_action_desc
        self.traveler_email = traveler_email
        self.traveler_id = traveler_id
        self.traveler_job_no = traveler_job_no
        self.traveler_member_type = traveler_member_type
        self.traveler_member_type_name = traveler_member_type_name
        self.traveler_name = traveler_name
        self.user_confirm_desc = user_confirm_desc
        self.vehicle_scene_id = vehicle_scene_id
        self.vehicle_scene_name = vehicle_scene_name
        self.voucher_type = voucher_type
        self.voucher_type_desc = voucher_type_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adjust_time is not None:
            result['adjust_time'] = self.adjust_time

        if self.alipay_trade_no is not None:
            result['alipay_trade_no'] = self.alipay_trade_no

        if self.apply_arr_city_code is not None:
            result['apply_arr_city_code'] = self.apply_arr_city_code

        if self.apply_arr_city_name is not None:
            result['apply_arr_city_name'] = self.apply_arr_city_name

        if self.apply_dep_city_code is not None:
            result['apply_dep_city_code'] = self.apply_dep_city_code

        if self.apply_dep_city_name is not None:
            result['apply_dep_city_name'] = self.apply_dep_city_name

        if self.apply_extend_field is not None:
            result['apply_extend_field'] = self.apply_extend_field

        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.approver_email is not None:
            result['approver_email'] = self.approver_email

        if self.approver_id is not None:
            result['approver_id'] = self.approver_id

        if self.approver_name is not None:
            result['approver_name'] = self.approver_name

        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_date is not None:
            result['arr_date'] = self.arr_date

        if self.arr_location is not None:
            result['arr_location'] = self.arr_location

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.base_location is not None:
            result['base_location'] = self.base_location

        if self.bill_record_time is not None:
            result['bill_record_time'] = self.bill_record_time

        if self.billing_entity is not None:
            result['billing_entity'] = self.billing_entity

        if self.book_model is not None:
            result['book_model'] = self.book_model

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

        if self.category_desc is not None:
            result['category_desc'] = self.category_desc

        if self.cost_center is not None:
            result['cost_center'] = self.cost_center

        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number

        if self.cost_department is not None:
            result['cost_department'] = self.cost_department

        if self.coupon is not None:
            result['coupon'] = self.coupon

        if self.coupon_price is not None:
            result['coupon_price'] = self.coupon_price

        if self.custom_content is not None:
            result['custom_content'] = self.custom_content

        if self.deductible_tax is not None:
            result['deductible_tax'] = self.deductible_tax

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

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

        if self.driver_add_detail is not None:
            result['driver_add_detail'] = self.driver_add_detail

        if self.driver_add_fee is not None:
            result['driver_add_fee'] = self.driver_add_fee

        if self.estimate_drive_distance is not None:
            result['estimate_drive_distance'] = self.estimate_drive_distance

        if self.estimate_price is not None:
            result['estimate_price'] = self.estimate_price

        if self.fee_type is not None:
            result['fee_type'] = self.fee_type

        if self.fee_type_desc is not None:
            result['fee_type_desc'] = self.fee_type_desc

        if self.foreigners_tag is not None:
            result['foreigners_tag'] = self.foreigners_tag

        if self.index is not None:
            result['index'] = self.index

        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title

        if self.level_name is not None:
            result['level_name'] = self.level_name

        if self.location is not None:
            result['location'] = self.location

        if self.mapping_company_code is not None:
            result['mapping_company_code'] = self.mapping_company_code

        if self.memo is not None:
            result['memo'] = self.memo

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.order_price is not None:
            result['order_price'] = self.order_price

        if self.over_apply_id is not None:
            result['over_apply_id'] = self.over_apply_id

        if self.payment_department_id is not None:
            result['payment_department_id'] = self.payment_department_id

        if self.payment_department_name is not None:
            result['payment_department_name'] = self.payment_department_name

        if self.person_settle_fee is not None:
            result['person_settle_fee'] = self.person_settle_fee

        if self.position is not None:
            result['position'] = self.position

        if self.position_level is not None:
            result['position_level'] = self.position_level

        if self.primary_id is not None:
            result['primary_id'] = self.primary_id

        if self.processor_oa_code is not None:
            result['processor_oa_code'] = self.processor_oa_code

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_name is not None:
            result['project_name'] = self.project_name

        if self.protocol_discount_fee is not None:
            result['protocol_discount_fee'] = self.protocol_discount_fee

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

        if self.scene_id is not None:
            result['scene_id'] = self.scene_id

        if self.scene_name is not None:
            result['scene_name'] = self.scene_name

        if self.service_fee is not None:
            result['service_fee'] = self.service_fee

        if self.settle_type_desc is not None:
            result['settle_type_desc'] = self.settle_type_desc

        if self.settlement_fee is not None:
            result['settlement_fee'] = self.settlement_fee

        if self.settlement_grant_fee is not None:
            result['settlement_grant_fee'] = self.settlement_grant_fee

        if self.settlement_time is not None:
            result['settlement_time'] = self.settlement_time

        if self.settlement_type is not None:
            result['settlement_type'] = self.settlement_type

        if self.sio is not None:
            result['sio'] = self.sio

        if self.special_order is not None:
            result['special_order'] = self.special_order

        if self.special_reason is not None:
            result['special_reason'] = self.special_reason

        if self.status is not None:
            result['status'] = self.status

        if self.status_desc is not None:
            result['status_desc'] = self.status_desc

        if self.sub_order_id is not None:
            result['sub_order_id'] = self.sub_order_id

        if self.supplement_apply_id is not None:
            result['supplement_apply_id'] = self.supplement_apply_id

        if self.tax_rate is not None:
            result['tax_rate'] = self.tax_rate

        if self.third_itinerary_id is not None:
            result['third_itinerary_id'] = self.third_itinerary_id

        if self.time_type is not None:
            result['time_type'] = self.time_type

        if self.trade_action_desc is not None:
            result['trade_action_desc'] = self.trade_action_desc

        if self.traveler_email is not None:
            result['traveler_email'] = self.traveler_email

        if self.traveler_id is not None:
            result['traveler_id'] = self.traveler_id

        if self.traveler_job_no is not None:
            result['traveler_job_no'] = self.traveler_job_no

        if self.traveler_member_type is not None:
            result['traveler_member_type'] = self.traveler_member_type

        if self.traveler_member_type_name is not None:
            result['traveler_member_type_name'] = self.traveler_member_type_name

        if self.traveler_name is not None:
            result['traveler_name'] = self.traveler_name

        if self.user_confirm_desc is not None:
            result['user_confirm_desc'] = self.user_confirm_desc

        if self.vehicle_scene_id is not None:
            result['vehicle_scene_id'] = self.vehicle_scene_id

        if self.vehicle_scene_name is not None:
            result['vehicle_scene_name'] = self.vehicle_scene_name

        if self.voucher_type is not None:
            result['voucher_type'] = self.voucher_type

        if self.voucher_type_desc is not None:
            result['voucher_type_desc'] = self.voucher_type_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adjust_time') is not None:
            self.adjust_time = m.get('adjust_time')

        if m.get('alipay_trade_no') is not None:
            self.alipay_trade_no = m.get('alipay_trade_no')

        if m.get('apply_arr_city_code') is not None:
            self.apply_arr_city_code = m.get('apply_arr_city_code')

        if m.get('apply_arr_city_name') is not None:
            self.apply_arr_city_name = m.get('apply_arr_city_name')

        if m.get('apply_dep_city_code') is not None:
            self.apply_dep_city_code = m.get('apply_dep_city_code')

        if m.get('apply_dep_city_name') is not None:
            self.apply_dep_city_name = m.get('apply_dep_city_name')

        if m.get('apply_extend_field') is not None:
            self.apply_extend_field = m.get('apply_extend_field')

        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('approver_email') is not None:
            self.approver_email = m.get('approver_email')

        if m.get('approver_id') is not None:
            self.approver_id = m.get('approver_id')

        if m.get('approver_name') is not None:
            self.approver_name = m.get('approver_name')

        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')

        if m.get('arr_location') is not None:
            self.arr_location = m.get('arr_location')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('base_location') is not None:
            self.base_location = m.get('base_location')

        if m.get('bill_record_time') is not None:
            self.bill_record_time = m.get('bill_record_time')

        if m.get('billing_entity') is not None:
            self.billing_entity = m.get('billing_entity')

        if m.get('book_model') is not None:
            self.book_model = m.get('book_model')

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

        if m.get('category_desc') is not None:
            self.category_desc = m.get('category_desc')

        if m.get('cost_center') is not None:
            self.cost_center = m.get('cost_center')

        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')

        if m.get('cost_department') is not None:
            self.cost_department = m.get('cost_department')

        if m.get('coupon') is not None:
            self.coupon = m.get('coupon')

        if m.get('coupon_price') is not None:
            self.coupon_price = m.get('coupon_price')

        if m.get('custom_content') is not None:
            self.custom_content = m.get('custom_content')

        if m.get('deductible_tax') is not None:
            self.deductible_tax = m.get('deductible_tax')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

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

        if m.get('driver_add_detail') is not None:
            self.driver_add_detail = m.get('driver_add_detail')

        if m.get('driver_add_fee') is not None:
            self.driver_add_fee = m.get('driver_add_fee')

        if m.get('estimate_drive_distance') is not None:
            self.estimate_drive_distance = m.get('estimate_drive_distance')

        if m.get('estimate_price') is not None:
            self.estimate_price = m.get('estimate_price')

        if m.get('fee_type') is not None:
            self.fee_type = m.get('fee_type')

        if m.get('fee_type_desc') is not None:
            self.fee_type_desc = m.get('fee_type_desc')

        if m.get('foreigners_tag') is not None:
            self.foreigners_tag = m.get('foreigners_tag')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')

        if m.get('level_name') is not None:
            self.level_name = m.get('level_name')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('mapping_company_code') is not None:
            self.mapping_company_code = m.get('mapping_company_code')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('order_price') is not None:
            self.order_price = m.get('order_price')

        if m.get('over_apply_id') is not None:
            self.over_apply_id = m.get('over_apply_id')

        if m.get('payment_department_id') is not None:
            self.payment_department_id = m.get('payment_department_id')

        if m.get('payment_department_name') is not None:
            self.payment_department_name = m.get('payment_department_name')

        if m.get('person_settle_fee') is not None:
            self.person_settle_fee = m.get('person_settle_fee')

        if m.get('position') is not None:
            self.position = m.get('position')

        if m.get('position_level') is not None:
            self.position_level = m.get('position_level')

        if m.get('primary_id') is not None:
            self.primary_id = m.get('primary_id')

        if m.get('processor_oa_code') is not None:
            self.processor_oa_code = m.get('processor_oa_code')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_name') is not None:
            self.project_name = m.get('project_name')

        if m.get('protocol_discount_fee') is not None:
            self.protocol_discount_fee = m.get('protocol_discount_fee')

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

        if m.get('scene_id') is not None:
            self.scene_id = m.get('scene_id')

        if m.get('scene_name') is not None:
            self.scene_name = m.get('scene_name')

        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')

        if m.get('settle_type_desc') is not None:
            self.settle_type_desc = m.get('settle_type_desc')

        if m.get('settlement_fee') is not None:
            self.settlement_fee = m.get('settlement_fee')

        if m.get('settlement_grant_fee') is not None:
            self.settlement_grant_fee = m.get('settlement_grant_fee')

        if m.get('settlement_time') is not None:
            self.settlement_time = m.get('settlement_time')

        if m.get('settlement_type') is not None:
            self.settlement_type = m.get('settlement_type')

        if m.get('sio') is not None:
            self.sio = m.get('sio')

        if m.get('special_order') is not None:
            self.special_order = m.get('special_order')

        if m.get('special_reason') is not None:
            self.special_reason = m.get('special_reason')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('status_desc') is not None:
            self.status_desc = m.get('status_desc')

        if m.get('sub_order_id') is not None:
            self.sub_order_id = m.get('sub_order_id')

        if m.get('supplement_apply_id') is not None:
            self.supplement_apply_id = m.get('supplement_apply_id')

        if m.get('tax_rate') is not None:
            self.tax_rate = m.get('tax_rate')

        if m.get('third_itinerary_id') is not None:
            self.third_itinerary_id = m.get('third_itinerary_id')

        if m.get('time_type') is not None:
            self.time_type = m.get('time_type')

        if m.get('trade_action_desc') is not None:
            self.trade_action_desc = m.get('trade_action_desc')

        if m.get('traveler_email') is not None:
            self.traveler_email = m.get('traveler_email')

        if m.get('traveler_id') is not None:
            self.traveler_id = m.get('traveler_id')

        if m.get('traveler_job_no') is not None:
            self.traveler_job_no = m.get('traveler_job_no')

        if m.get('traveler_member_type') is not None:
            self.traveler_member_type = m.get('traveler_member_type')

        if m.get('traveler_member_type_name') is not None:
            self.traveler_member_type_name = m.get('traveler_member_type_name')

        if m.get('traveler_name') is not None:
            self.traveler_name = m.get('traveler_name')

        if m.get('user_confirm_desc') is not None:
            self.user_confirm_desc = m.get('user_confirm_desc')

        if m.get('vehicle_scene_id') is not None:
            self.vehicle_scene_id = m.get('vehicle_scene_id')

        if m.get('vehicle_scene_name') is not None:
            self.vehicle_scene_name = m.get('vehicle_scene_name')

        if m.get('voucher_type') is not None:
            self.voucher_type = m.get('voucher_type')

        if m.get('voucher_type_desc') is not None:
            self.voucher_type_desc = m.get('voucher_type_desc')

        return self

