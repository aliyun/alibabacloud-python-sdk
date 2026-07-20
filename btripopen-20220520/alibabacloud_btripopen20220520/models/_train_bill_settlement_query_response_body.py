# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TrainBillSettlementQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.TrainBillSettlementQueryResponseBodyModule = None,
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
            temp_model = main_models.TrainBillSettlementQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TrainBillSettlementQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        data_list: List[main_models.TrainBillSettlementQueryResponseBodyModuleDataList] = None,
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
                temp_model = main_models.TrainBillSettlementQueryResponseBodyModuleDataList()
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

class TrainBillSettlementQueryResponseBodyModuleDataList(DaraModel):
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
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_date: str = None,
        arr_station: str = None,
        arr_station_location: str = None,
        arr_station_location_code: str = None,
        arr_time: str = None,
        base_location: str = None,
        bill_record_time: str = None,
        book_time: str = None,
        booker_id: str = None,
        booker_job_no: str = None,
        booker_name: str = None,
        business_trip_result: str = None,
        cabin_max_price: float = None,
        capital_direction: str = None,
        cascade_department: str = None,
        category_desc: str = None,
        change_affiliate_no: str = None,
        change_apply_id: str = None,
        change_fee: float = None,
        change_result: str = None,
        coach_no: str = None,
        cost_center: str = None,
        cost_center_number: str = None,
        cost_department: str = None,
        coupon: float = None,
        custom_content: str = None,
        deductible_tax: float = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_station_location: str = None,
        dep_station_location_code: str = None,
        department: str = None,
        department_id: str = None,
        dept_date: str = None,
        dept_station: str = None,
        dept_time: str = None,
        exceed_reason: str = None,
        fee_type: str = None,
        fee_type_desc: str = None,
        foreigners_tag: str = None,
        index: str = None,
        invoice_title: str = None,
        is_transfer_order: str = None,
        location: str = None,
        long_ticket_no: str = None,
        mapping_company_code: str = None,
        max_cabin: str = None,
        order_id: str = None,
        order_price: float = None,
        order_ticket_no: str = None,
        over_apply_id: str = None,
        payment_department_id: str = None,
        payment_department_name: str = None,
        position: str = None,
        position_level: str = None,
        primary_id: int = None,
        print_ticket_price: float = None,
        processor_oa_code: str = None,
        project_code: str = None,
        project_name: str = None,
        refund_affiliate_no: str = None,
        refund_apply_id: str = None,
        refund_fee: float = None,
        refund_reason: str = None,
        remark: str = None,
        reserve_mode: str = None,
        run_time: str = None,
        scene_id: str = None,
        scene_name: str = None,
        seat_no: str = None,
        seat_type: str = None,
        service_fee: float = None,
        settle_type_desc: str = None,
        settlement_fee: float = None,
        settlement_grant_fee: float = None,
        settlement_time: str = None,
        settlement_type: str = None,
        short_ticket_no: str = None,
        sio: str = None,
        speed_package_fee: float = None,
        status: int = None,
        status_desc: str = None,
        tax_rate: str = None,
        third_itinerary_id: str = None,
        ticket_corp_pay_price: str = None,
        ticket_no: str = None,
        ticket_person_pay_price: str = None,
        ticket_price: float = None,
        trade_action_desc: str = None,
        train_no: str = None,
        train_type: str = None,
        traveler_email: str = None,
        traveler_id: str = None,
        traveler_job_no: str = None,
        traveler_member_type: str = None,
        traveler_member_type_name: str = None,
        traveler_name: str = None,
        verify_failed_reason: str = None,
        verify_status: int = None,
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
        self.arr_city_code = arr_city_code
        self.arr_city_name = arr_city_name
        self.arr_date = arr_date
        self.arr_station = arr_station
        self.arr_station_location = arr_station_location
        self.arr_station_location_code = arr_station_location_code
        self.arr_time = arr_time
        self.base_location = base_location
        self.bill_record_time = bill_record_time
        self.book_time = book_time
        self.booker_id = booker_id
        self.booker_job_no = booker_job_no
        self.booker_name = booker_name
        self.business_trip_result = business_trip_result
        self.cabin_max_price = cabin_max_price
        self.capital_direction = capital_direction
        self.cascade_department = cascade_department
        self.category_desc = category_desc
        self.change_affiliate_no = change_affiliate_no
        self.change_apply_id = change_apply_id
        self.change_fee = change_fee
        self.change_result = change_result
        self.coach_no = coach_no
        self.cost_center = cost_center
        self.cost_center_number = cost_center_number
        self.cost_department = cost_department
        self.coupon = coupon
        self.custom_content = custom_content
        self.deductible_tax = deductible_tax
        self.dep_city_code = dep_city_code
        self.dep_city_name = dep_city_name
        self.dep_station_location = dep_station_location
        self.dep_station_location_code = dep_station_location_code
        self.department = department
        self.department_id = department_id
        self.dept_date = dept_date
        self.dept_station = dept_station
        self.dept_time = dept_time
        self.exceed_reason = exceed_reason
        self.fee_type = fee_type
        self.fee_type_desc = fee_type_desc
        self.foreigners_tag = foreigners_tag
        self.index = index
        self.invoice_title = invoice_title
        self.is_transfer_order = is_transfer_order
        self.location = location
        self.long_ticket_no = long_ticket_no
        self.mapping_company_code = mapping_company_code
        self.max_cabin = max_cabin
        self.order_id = order_id
        self.order_price = order_price
        self.order_ticket_no = order_ticket_no
        self.over_apply_id = over_apply_id
        self.payment_department_id = payment_department_id
        self.payment_department_name = payment_department_name
        self.position = position
        self.position_level = position_level
        self.primary_id = primary_id
        self.print_ticket_price = print_ticket_price
        self.processor_oa_code = processor_oa_code
        self.project_code = project_code
        self.project_name = project_name
        self.refund_affiliate_no = refund_affiliate_no
        self.refund_apply_id = refund_apply_id
        self.refund_fee = refund_fee
        self.refund_reason = refund_reason
        self.remark = remark
        self.reserve_mode = reserve_mode
        self.run_time = run_time
        self.scene_id = scene_id
        self.scene_name = scene_name
        self.seat_no = seat_no
        self.seat_type = seat_type
        self.service_fee = service_fee
        self.settle_type_desc = settle_type_desc
        self.settlement_fee = settlement_fee
        self.settlement_grant_fee = settlement_grant_fee
        self.settlement_time = settlement_time
        self.settlement_type = settlement_type
        self.short_ticket_no = short_ticket_no
        self.sio = sio
        self.speed_package_fee = speed_package_fee
        self.status = status
        self.status_desc = status_desc
        # 税率
        self.tax_rate = tax_rate
        self.third_itinerary_id = third_itinerary_id
        self.ticket_corp_pay_price = ticket_corp_pay_price
        self.ticket_no = ticket_no
        self.ticket_person_pay_price = ticket_person_pay_price
        self.ticket_price = ticket_price
        self.trade_action_desc = trade_action_desc
        self.train_no = train_no
        self.train_type = train_type
        self.traveler_email = traveler_email
        self.traveler_id = traveler_id
        self.traveler_job_no = traveler_job_no
        self.traveler_member_type = traveler_member_type
        self.traveler_member_type_name = traveler_member_type_name
        self.traveler_name = traveler_name
        self.verify_failed_reason = verify_failed_reason
        self.verify_status = verify_status
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

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name

        if self.arr_date is not None:
            result['arr_date'] = self.arr_date

        if self.arr_station is not None:
            result['arr_station'] = self.arr_station

        if self.arr_station_location is not None:
            result['arr_station_location'] = self.arr_station_location

        if self.arr_station_location_code is not None:
            result['arr_station_location_code'] = self.arr_station_location_code

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.base_location is not None:
            result['base_location'] = self.base_location

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

        if self.business_trip_result is not None:
            result['business_trip_result'] = self.business_trip_result

        if self.cabin_max_price is not None:
            result['cabin_max_price'] = self.cabin_max_price

        if self.capital_direction is not None:
            result['capital_direction'] = self.capital_direction

        if self.cascade_department is not None:
            result['cascade_department'] = self.cascade_department

        if self.category_desc is not None:
            result['category_desc'] = self.category_desc

        if self.change_affiliate_no is not None:
            result['change_affiliate_no'] = self.change_affiliate_no

        if self.change_apply_id is not None:
            result['change_apply_id'] = self.change_apply_id

        if self.change_fee is not None:
            result['change_fee'] = self.change_fee

        if self.change_result is not None:
            result['change_result'] = self.change_result

        if self.coach_no is not None:
            result['coach_no'] = self.coach_no

        if self.cost_center is not None:
            result['cost_center'] = self.cost_center

        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number

        if self.cost_department is not None:
            result['cost_department'] = self.cost_department

        if self.coupon is not None:
            result['coupon'] = self.coupon

        if self.custom_content is not None:
            result['custom_content'] = self.custom_content

        if self.deductible_tax is not None:
            result['deductible_tax'] = self.deductible_tax

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name

        if self.dep_station_location is not None:
            result['dep_station_location'] = self.dep_station_location

        if self.dep_station_location_code is not None:
            result['dep_station_location_code'] = self.dep_station_location_code

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

        if self.exceed_reason is not None:
            result['exceed_reason'] = self.exceed_reason

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

        if self.is_transfer_order is not None:
            result['is_transfer_order'] = self.is_transfer_order

        if self.location is not None:
            result['location'] = self.location

        if self.long_ticket_no is not None:
            result['long_ticket_no'] = self.long_ticket_no

        if self.mapping_company_code is not None:
            result['mapping_company_code'] = self.mapping_company_code

        if self.max_cabin is not None:
            result['max_cabin'] = self.max_cabin

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.order_price is not None:
            result['order_price'] = self.order_price

        if self.order_ticket_no is not None:
            result['order_ticket_no'] = self.order_ticket_no

        if self.over_apply_id is not None:
            result['over_apply_id'] = self.over_apply_id

        if self.payment_department_id is not None:
            result['payment_department_id'] = self.payment_department_id

        if self.payment_department_name is not None:
            result['payment_department_name'] = self.payment_department_name

        if self.position is not None:
            result['position'] = self.position

        if self.position_level is not None:
            result['position_level'] = self.position_level

        if self.primary_id is not None:
            result['primary_id'] = self.primary_id

        if self.print_ticket_price is not None:
            result['print_ticket_price'] = self.print_ticket_price

        if self.processor_oa_code is not None:
            result['processor_oa_code'] = self.processor_oa_code

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_name is not None:
            result['project_name'] = self.project_name

        if self.refund_affiliate_no is not None:
            result['refund_affiliate_no'] = self.refund_affiliate_no

        if self.refund_apply_id is not None:
            result['refund_apply_id'] = self.refund_apply_id

        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee

        if self.refund_reason is not None:
            result['refund_reason'] = self.refund_reason

        if self.remark is not None:
            result['remark'] = self.remark

        if self.reserve_mode is not None:
            result['reserve_mode'] = self.reserve_mode

        if self.run_time is not None:
            result['run_time'] = self.run_time

        if self.scene_id is not None:
            result['scene_id'] = self.scene_id

        if self.scene_name is not None:
            result['scene_name'] = self.scene_name

        if self.seat_no is not None:
            result['seat_no'] = self.seat_no

        if self.seat_type is not None:
            result['seat_type'] = self.seat_type

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

        if self.short_ticket_no is not None:
            result['short_ticket_no'] = self.short_ticket_no

        if self.sio is not None:
            result['sio'] = self.sio

        if self.speed_package_fee is not None:
            result['speed_package_fee'] = self.speed_package_fee

        if self.status is not None:
            result['status'] = self.status

        if self.status_desc is not None:
            result['status_desc'] = self.status_desc

        if self.tax_rate is not None:
            result['tax_rate'] = self.tax_rate

        if self.third_itinerary_id is not None:
            result['third_itinerary_id'] = self.third_itinerary_id

        if self.ticket_corp_pay_price is not None:
            result['ticket_corp_pay_price'] = self.ticket_corp_pay_price

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        if self.ticket_person_pay_price is not None:
            result['ticket_person_pay_price'] = self.ticket_person_pay_price

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.trade_action_desc is not None:
            result['trade_action_desc'] = self.trade_action_desc

        if self.train_no is not None:
            result['train_no'] = self.train_no

        if self.train_type is not None:
            result['train_type'] = self.train_type

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

        if self.verify_failed_reason is not None:
            result['verify_failed_reason'] = self.verify_failed_reason

        if self.verify_status is not None:
            result['verify_status'] = self.verify_status

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

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')

        if m.get('arr_station') is not None:
            self.arr_station = m.get('arr_station')

        if m.get('arr_station_location') is not None:
            self.arr_station_location = m.get('arr_station_location')

        if m.get('arr_station_location_code') is not None:
            self.arr_station_location_code = m.get('arr_station_location_code')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('base_location') is not None:
            self.base_location = m.get('base_location')

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

        if m.get('business_trip_result') is not None:
            self.business_trip_result = m.get('business_trip_result')

        if m.get('cabin_max_price') is not None:
            self.cabin_max_price = m.get('cabin_max_price')

        if m.get('capital_direction') is not None:
            self.capital_direction = m.get('capital_direction')

        if m.get('cascade_department') is not None:
            self.cascade_department = m.get('cascade_department')

        if m.get('category_desc') is not None:
            self.category_desc = m.get('category_desc')

        if m.get('change_affiliate_no') is not None:
            self.change_affiliate_no = m.get('change_affiliate_no')

        if m.get('change_apply_id') is not None:
            self.change_apply_id = m.get('change_apply_id')

        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')

        if m.get('change_result') is not None:
            self.change_result = m.get('change_result')

        if m.get('coach_no') is not None:
            self.coach_no = m.get('coach_no')

        if m.get('cost_center') is not None:
            self.cost_center = m.get('cost_center')

        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')

        if m.get('cost_department') is not None:
            self.cost_department = m.get('cost_department')

        if m.get('coupon') is not None:
            self.coupon = m.get('coupon')

        if m.get('custom_content') is not None:
            self.custom_content = m.get('custom_content')

        if m.get('deductible_tax') is not None:
            self.deductible_tax = m.get('deductible_tax')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')

        if m.get('dep_station_location') is not None:
            self.dep_station_location = m.get('dep_station_location')

        if m.get('dep_station_location_code') is not None:
            self.dep_station_location_code = m.get('dep_station_location_code')

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

        if m.get('exceed_reason') is not None:
            self.exceed_reason = m.get('exceed_reason')

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

        if m.get('is_transfer_order') is not None:
            self.is_transfer_order = m.get('is_transfer_order')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('long_ticket_no') is not None:
            self.long_ticket_no = m.get('long_ticket_no')

        if m.get('mapping_company_code') is not None:
            self.mapping_company_code = m.get('mapping_company_code')

        if m.get('max_cabin') is not None:
            self.max_cabin = m.get('max_cabin')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('order_price') is not None:
            self.order_price = m.get('order_price')

        if m.get('order_ticket_no') is not None:
            self.order_ticket_no = m.get('order_ticket_no')

        if m.get('over_apply_id') is not None:
            self.over_apply_id = m.get('over_apply_id')

        if m.get('payment_department_id') is not None:
            self.payment_department_id = m.get('payment_department_id')

        if m.get('payment_department_name') is not None:
            self.payment_department_name = m.get('payment_department_name')

        if m.get('position') is not None:
            self.position = m.get('position')

        if m.get('position_level') is not None:
            self.position_level = m.get('position_level')

        if m.get('primary_id') is not None:
            self.primary_id = m.get('primary_id')

        if m.get('print_ticket_price') is not None:
            self.print_ticket_price = m.get('print_ticket_price')

        if m.get('processor_oa_code') is not None:
            self.processor_oa_code = m.get('processor_oa_code')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_name') is not None:
            self.project_name = m.get('project_name')

        if m.get('refund_affiliate_no') is not None:
            self.refund_affiliate_no = m.get('refund_affiliate_no')

        if m.get('refund_apply_id') is not None:
            self.refund_apply_id = m.get('refund_apply_id')

        if m.get('refund_fee') is not None:
            self.refund_fee = m.get('refund_fee')

        if m.get('refund_reason') is not None:
            self.refund_reason = m.get('refund_reason')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('reserve_mode') is not None:
            self.reserve_mode = m.get('reserve_mode')

        if m.get('run_time') is not None:
            self.run_time = m.get('run_time')

        if m.get('scene_id') is not None:
            self.scene_id = m.get('scene_id')

        if m.get('scene_name') is not None:
            self.scene_name = m.get('scene_name')

        if m.get('seat_no') is not None:
            self.seat_no = m.get('seat_no')

        if m.get('seat_type') is not None:
            self.seat_type = m.get('seat_type')

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

        if m.get('short_ticket_no') is not None:
            self.short_ticket_no = m.get('short_ticket_no')

        if m.get('sio') is not None:
            self.sio = m.get('sio')

        if m.get('speed_package_fee') is not None:
            self.speed_package_fee = m.get('speed_package_fee')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('status_desc') is not None:
            self.status_desc = m.get('status_desc')

        if m.get('tax_rate') is not None:
            self.tax_rate = m.get('tax_rate')

        if m.get('third_itinerary_id') is not None:
            self.third_itinerary_id = m.get('third_itinerary_id')

        if m.get('ticket_corp_pay_price') is not None:
            self.ticket_corp_pay_price = m.get('ticket_corp_pay_price')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        if m.get('ticket_person_pay_price') is not None:
            self.ticket_person_pay_price = m.get('ticket_person_pay_price')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('trade_action_desc') is not None:
            self.trade_action_desc = m.get('trade_action_desc')

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        if m.get('train_type') is not None:
            self.train_type = m.get('train_type')

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

        if m.get('verify_failed_reason') is not None:
            self.verify_failed_reason = m.get('verify_failed_reason')

        if m.get('verify_status') is not None:
            self.verify_status = m.get('verify_status')

        if m.get('voucher_type') is not None:
            self.voucher_type = m.get('voucher_type')

        if m.get('voucher_type_desc') is not None:
            self.voucher_type_desc = m.get('voucher_type_desc')

        return self

