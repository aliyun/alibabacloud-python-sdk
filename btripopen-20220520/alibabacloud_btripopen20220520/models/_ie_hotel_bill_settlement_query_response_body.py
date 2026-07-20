# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IeHotelBillSettlementQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.IeHotelBillSettlementQueryResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        # module
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
            temp_model = main_models.IeHotelBillSettlementQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class IeHotelBillSettlementQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        data_list: List[main_models.IeHotelBillSettlementQueryResponseBodyModuleDataList] = None,
        order_id: str = None,
        period_end: str = None,
        period_start: str = None,
        scroll_id: str = None,
        total_size: int = None,
    ):
        self.category = category
        self.corp_id = corp_id
        self.data_list = data_list
        self.order_id = order_id
        self.period_end = period_end
        self.period_start = period_start
        self.scroll_id = scroll_id
        self.total_size = total_size

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

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.period_end is not None:
            result['period_end'] = self.period_end

        if self.period_start is not None:
            result['period_start'] = self.period_start

        if self.scroll_id is not None:
            result['scroll_id'] = self.scroll_id

        if self.total_size is not None:
            result['total_size'] = self.total_size

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
                temp_model = main_models.IeHotelBillSettlementQueryResponseBodyModuleDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('period_end') is not None:
            self.period_end = m.get('period_end')

        if m.get('period_start') is not None:
            self.period_start = m.get('period_start')

        if m.get('scroll_id') is not None:
            self.scroll_id = m.get('scroll_id')

        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')

        return self

class IeHotelBillSettlementQueryResponseBodyModuleDataList(DaraModel):
    def __init__(
        self,
        adjust_time: str = None,
        alipay_trade_no: str = None,
        amount_currency: str = None,
        apply_arr_city_code: str = None,
        apply_arr_city_name: str = None,
        apply_dep_city_code: str = None,
        apply_dep_city_name: str = None,
        apply_extend_field: str = None,
        apply_id: str = None,
        approver_email: str = None,
        approver_id: str = None,
        approver_name: str = None,
        average_nights: float = None,
        base_location: str = None,
        bill_record_time: str = None,
        book_mode: str = None,
        book_reason: str = None,
        book_time: str = None,
        booker_id: str = None,
        booker_job_no: str = None,
        booker_name: str = None,
        brand_group: str = None,
        brand_name: str = None,
        business_expense: int = None,
        business_trip_result: str = None,
        capital_direction: str = None,
        cascade_department: str = None,
        category_desc: str = None,
        check_in_date: str = None,
        checkout_date: str = None,
        city: str = None,
        city_code: str = None,
        corp_refund_fee: float = None,
        corp_total_fee: float = None,
        cost_center: str = None,
        cost_center_number: str = None,
        cost_department: str = None,
        country: str = None,
        country_code: str = None,
        custom_content: str = None,
        deductible_tax: float = None,
        department: str = None,
        department_id: str = None,
        exceed_reason: str = None,
        fee_type: str = None,
        fee_type_desc: str = None,
        fines: float = None,
        foreign_business_expense: int = None,
        foreigners_tag: str = None,
        hotel_name: str = None,
        hotel_star: str = None,
        index: str = None,
        invoice_title: str = None,
        is_early_departure: str = None,
        is_negotiation: str = None,
        is_share_str: str = None,
        location: str = None,
        main_apply_id: str = None,
        mapping_company_code: str = None,
        nights: int = None,
        order_id: str = None,
        order_price: float = None,
        order_status_desc: str = None,
        order_type: str = None,
        original_reserve_rule: str = None,
        over_apply_id: str = None,
        payment_department_id: str = None,
        payment_department_name: str = None,
        person_refund_fee: float = None,
        person_settle_price: float = None,
        position: str = None,
        position_level: str = None,
        primary_id: int = None,
        processor_oa_code: str = None,
        project_code: str = None,
        project_name: str = None,
        promotion_fee: float = None,
        rate: str = None,
        remark: str = None,
        reserve_rule: int = None,
        room_no: str = None,
        room_number: int = None,
        room_price: float = None,
        room_type: str = None,
        service_fee: float = None,
        settle_type_desc: str = None,
        settlement_fee: float = None,
        settlement_grant_fee: float = None,
        settlement_time: str = None,
        settlement_type: str = None,
        sio: str = None,
        status: int = None,
        status_desc: str = None,
        sub_order_id: str = None,
        tax_rate: str = None,
        third_invoice_id: str = None,
        third_itinerary_id: str = None,
        third_part_business_id: str = None,
        thirdpart_apply_id: str = None,
        total_nights: int = None,
        trade_action_desc: str = None,
        traveler_email: str = None,
        traveler_id: str = None,
        traveler_job_no: str = None,
        traveler_member_type: str = None,
        traveler_name: str = None,
        voucher_type: int = None,
        voucher_type_desc: str = None,
    ):
        self.adjust_time = adjust_time
        self.alipay_trade_no = alipay_trade_no
        self.amount_currency = amount_currency
        self.apply_arr_city_code = apply_arr_city_code
        self.apply_arr_city_name = apply_arr_city_name
        self.apply_dep_city_code = apply_dep_city_code
        self.apply_dep_city_name = apply_dep_city_name
        self.apply_extend_field = apply_extend_field
        self.apply_id = apply_id
        self.approver_email = approver_email
        self.approver_id = approver_id
        self.approver_name = approver_name
        self.average_nights = average_nights
        self.base_location = base_location
        self.bill_record_time = bill_record_time
        self.book_mode = book_mode
        self.book_reason = book_reason
        self.book_time = book_time
        self.booker_id = booker_id
        self.booker_job_no = booker_job_no
        self.booker_name = booker_name
        self.brand_group = brand_group
        self.brand_name = brand_name
        self.business_expense = business_expense
        self.business_trip_result = business_trip_result
        self.capital_direction = capital_direction
        self.cascade_department = cascade_department
        self.category_desc = category_desc
        self.check_in_date = check_in_date
        self.checkout_date = checkout_date
        self.city = city
        self.city_code = city_code
        self.corp_refund_fee = corp_refund_fee
        self.corp_total_fee = corp_total_fee
        self.cost_center = cost_center
        self.cost_center_number = cost_center_number
        self.cost_department = cost_department
        self.country = country
        self.country_code = country_code
        self.custom_content = custom_content
        self.deductible_tax = deductible_tax
        self.department = department
        self.department_id = department_id
        self.exceed_reason = exceed_reason
        self.fee_type = fee_type
        self.fee_type_desc = fee_type_desc
        self.fines = fines
        self.foreign_business_expense = foreign_business_expense
        self.foreigners_tag = foreigners_tag
        self.hotel_name = hotel_name
        self.hotel_star = hotel_star
        self.index = index
        self.invoice_title = invoice_title
        self.is_early_departure = is_early_departure
        self.is_negotiation = is_negotiation
        self.is_share_str = is_share_str
        self.location = location
        self.main_apply_id = main_apply_id
        self.mapping_company_code = mapping_company_code
        self.nights = nights
        self.order_id = order_id
        self.order_price = order_price
        self.order_status_desc = order_status_desc
        self.order_type = order_type
        self.original_reserve_rule = original_reserve_rule
        self.over_apply_id = over_apply_id
        self.payment_department_id = payment_department_id
        self.payment_department_name = payment_department_name
        self.person_refund_fee = person_refund_fee
        self.person_settle_price = person_settle_price
        self.position = position
        self.position_level = position_level
        self.primary_id = primary_id
        self.processor_oa_code = processor_oa_code
        self.project_code = project_code
        self.project_name = project_name
        self.promotion_fee = promotion_fee
        self.rate = rate
        self.remark = remark
        self.reserve_rule = reserve_rule
        self.room_no = room_no
        self.room_number = room_number
        self.room_price = room_price
        self.room_type = room_type
        self.service_fee = service_fee
        self.settle_type_desc = settle_type_desc
        self.settlement_fee = settlement_fee
        self.settlement_grant_fee = settlement_grant_fee
        self.settlement_time = settlement_time
        self.settlement_type = settlement_type
        self.sio = sio
        self.status = status
        self.status_desc = status_desc
        self.sub_order_id = sub_order_id
        self.tax_rate = tax_rate
        self.third_invoice_id = third_invoice_id
        self.third_itinerary_id = third_itinerary_id
        self.third_part_business_id = third_part_business_id
        self.thirdpart_apply_id = thirdpart_apply_id
        self.total_nights = total_nights
        self.trade_action_desc = trade_action_desc
        self.traveler_email = traveler_email
        self.traveler_id = traveler_id
        self.traveler_job_no = traveler_job_no
        self.traveler_member_type = traveler_member_type
        self.traveler_name = traveler_name
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

        if self.amount_currency is not None:
            result['amount_currency'] = self.amount_currency

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

        if self.average_nights is not None:
            result['average_nights'] = self.average_nights

        if self.base_location is not None:
            result['base_location'] = self.base_location

        if self.bill_record_time is not None:
            result['bill_record_time'] = self.bill_record_time

        if self.book_mode is not None:
            result['book_mode'] = self.book_mode

        if self.book_reason is not None:
            result['book_reason'] = self.book_reason

        if self.book_time is not None:
            result['book_time'] = self.book_time

        if self.booker_id is not None:
            result['booker_id'] = self.booker_id

        if self.booker_job_no is not None:
            result['booker_job_no'] = self.booker_job_no

        if self.booker_name is not None:
            result['booker_name'] = self.booker_name

        if self.brand_group is not None:
            result['brand_group'] = self.brand_group

        if self.brand_name is not None:
            result['brand_name'] = self.brand_name

        if self.business_expense is not None:
            result['business_expense'] = self.business_expense

        if self.business_trip_result is not None:
            result['business_trip_result'] = self.business_trip_result

        if self.capital_direction is not None:
            result['capital_direction'] = self.capital_direction

        if self.cascade_department is not None:
            result['cascade_department'] = self.cascade_department

        if self.category_desc is not None:
            result['category_desc'] = self.category_desc

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

        if self.cost_department is not None:
            result['cost_department'] = self.cost_department

        if self.country is not None:
            result['country'] = self.country

        if self.country_code is not None:
            result['country_code'] = self.country_code

        if self.custom_content is not None:
            result['custom_content'] = self.custom_content

        if self.deductible_tax is not None:
            result['deductible_tax'] = self.deductible_tax

        if self.department is not None:
            result['department'] = self.department

        if self.department_id is not None:
            result['department_id'] = self.department_id

        if self.exceed_reason is not None:
            result['exceed_reason'] = self.exceed_reason

        if self.fee_type is not None:
            result['fee_type'] = self.fee_type

        if self.fee_type_desc is not None:
            result['fee_type_desc'] = self.fee_type_desc

        if self.fines is not None:
            result['fines'] = self.fines

        if self.foreign_business_expense is not None:
            result['foreign_business_expense'] = self.foreign_business_expense

        if self.foreigners_tag is not None:
            result['foreigners_tag'] = self.foreigners_tag

        if self.hotel_name is not None:
            result['hotel_name'] = self.hotel_name

        if self.hotel_star is not None:
            result['hotel_star'] = self.hotel_star

        if self.index is not None:
            result['index'] = self.index

        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title

        if self.is_early_departure is not None:
            result['is_early_departure'] = self.is_early_departure

        if self.is_negotiation is not None:
            result['is_negotiation'] = self.is_negotiation

        if self.is_share_str is not None:
            result['is_share_str'] = self.is_share_str

        if self.location is not None:
            result['location'] = self.location

        if self.main_apply_id is not None:
            result['main_apply_id'] = self.main_apply_id

        if self.mapping_company_code is not None:
            result['mapping_company_code'] = self.mapping_company_code

        if self.nights is not None:
            result['nights'] = self.nights

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.order_price is not None:
            result['order_price'] = self.order_price

        if self.order_status_desc is not None:
            result['order_status_desc'] = self.order_status_desc

        if self.order_type is not None:
            result['order_type'] = self.order_type

        if self.original_reserve_rule is not None:
            result['original_reserve_rule'] = self.original_reserve_rule

        if self.over_apply_id is not None:
            result['over_apply_id'] = self.over_apply_id

        if self.payment_department_id is not None:
            result['payment_department_id'] = self.payment_department_id

        if self.payment_department_name is not None:
            result['payment_department_name'] = self.payment_department_name

        if self.person_refund_fee is not None:
            result['person_refund_fee'] = self.person_refund_fee

        if self.person_settle_price is not None:
            result['person_settle_price'] = self.person_settle_price

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

        if self.promotion_fee is not None:
            result['promotion_fee'] = self.promotion_fee

        if self.rate is not None:
            result['rate'] = self.rate

        if self.remark is not None:
            result['remark'] = self.remark

        if self.reserve_rule is not None:
            result['reserve_rule'] = self.reserve_rule

        if self.room_no is not None:
            result['room_no'] = self.room_no

        if self.room_number is not None:
            result['room_number'] = self.room_number

        if self.room_price is not None:
            result['room_price'] = self.room_price

        if self.room_type is not None:
            result['room_type'] = self.room_type

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

        if self.status is not None:
            result['status'] = self.status

        if self.status_desc is not None:
            result['status_desc'] = self.status_desc

        if self.sub_order_id is not None:
            result['sub_order_id'] = self.sub_order_id

        if self.tax_rate is not None:
            result['tax_rate'] = self.tax_rate

        if self.third_invoice_id is not None:
            result['third_invoice_id'] = self.third_invoice_id

        if self.third_itinerary_id is not None:
            result['third_itinerary_id'] = self.third_itinerary_id

        if self.third_part_business_id is not None:
            result['third_part_business_id'] = self.third_part_business_id

        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id

        if self.total_nights is not None:
            result['total_nights'] = self.total_nights

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

        if self.traveler_name is not None:
            result['traveler_name'] = self.traveler_name

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

        if m.get('amount_currency') is not None:
            self.amount_currency = m.get('amount_currency')

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

        if m.get('average_nights') is not None:
            self.average_nights = m.get('average_nights')

        if m.get('base_location') is not None:
            self.base_location = m.get('base_location')

        if m.get('bill_record_time') is not None:
            self.bill_record_time = m.get('bill_record_time')

        if m.get('book_mode') is not None:
            self.book_mode = m.get('book_mode')

        if m.get('book_reason') is not None:
            self.book_reason = m.get('book_reason')

        if m.get('book_time') is not None:
            self.book_time = m.get('book_time')

        if m.get('booker_id') is not None:
            self.booker_id = m.get('booker_id')

        if m.get('booker_job_no') is not None:
            self.booker_job_no = m.get('booker_job_no')

        if m.get('booker_name') is not None:
            self.booker_name = m.get('booker_name')

        if m.get('brand_group') is not None:
            self.brand_group = m.get('brand_group')

        if m.get('brand_name') is not None:
            self.brand_name = m.get('brand_name')

        if m.get('business_expense') is not None:
            self.business_expense = m.get('business_expense')

        if m.get('business_trip_result') is not None:
            self.business_trip_result = m.get('business_trip_result')

        if m.get('capital_direction') is not None:
            self.capital_direction = m.get('capital_direction')

        if m.get('cascade_department') is not None:
            self.cascade_department = m.get('cascade_department')

        if m.get('category_desc') is not None:
            self.category_desc = m.get('category_desc')

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

        if m.get('cost_department') is not None:
            self.cost_department = m.get('cost_department')

        if m.get('country') is not None:
            self.country = m.get('country')

        if m.get('country_code') is not None:
            self.country_code = m.get('country_code')

        if m.get('custom_content') is not None:
            self.custom_content = m.get('custom_content')

        if m.get('deductible_tax') is not None:
            self.deductible_tax = m.get('deductible_tax')

        if m.get('department') is not None:
            self.department = m.get('department')

        if m.get('department_id') is not None:
            self.department_id = m.get('department_id')

        if m.get('exceed_reason') is not None:
            self.exceed_reason = m.get('exceed_reason')

        if m.get('fee_type') is not None:
            self.fee_type = m.get('fee_type')

        if m.get('fee_type_desc') is not None:
            self.fee_type_desc = m.get('fee_type_desc')

        if m.get('fines') is not None:
            self.fines = m.get('fines')

        if m.get('foreign_business_expense') is not None:
            self.foreign_business_expense = m.get('foreign_business_expense')

        if m.get('foreigners_tag') is not None:
            self.foreigners_tag = m.get('foreigners_tag')

        if m.get('hotel_name') is not None:
            self.hotel_name = m.get('hotel_name')

        if m.get('hotel_star') is not None:
            self.hotel_star = m.get('hotel_star')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')

        if m.get('is_early_departure') is not None:
            self.is_early_departure = m.get('is_early_departure')

        if m.get('is_negotiation') is not None:
            self.is_negotiation = m.get('is_negotiation')

        if m.get('is_share_str') is not None:
            self.is_share_str = m.get('is_share_str')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('main_apply_id') is not None:
            self.main_apply_id = m.get('main_apply_id')

        if m.get('mapping_company_code') is not None:
            self.mapping_company_code = m.get('mapping_company_code')

        if m.get('nights') is not None:
            self.nights = m.get('nights')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('order_price') is not None:
            self.order_price = m.get('order_price')

        if m.get('order_status_desc') is not None:
            self.order_status_desc = m.get('order_status_desc')

        if m.get('order_type') is not None:
            self.order_type = m.get('order_type')

        if m.get('original_reserve_rule') is not None:
            self.original_reserve_rule = m.get('original_reserve_rule')

        if m.get('over_apply_id') is not None:
            self.over_apply_id = m.get('over_apply_id')

        if m.get('payment_department_id') is not None:
            self.payment_department_id = m.get('payment_department_id')

        if m.get('payment_department_name') is not None:
            self.payment_department_name = m.get('payment_department_name')

        if m.get('person_refund_fee') is not None:
            self.person_refund_fee = m.get('person_refund_fee')

        if m.get('person_settle_price') is not None:
            self.person_settle_price = m.get('person_settle_price')

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

        if m.get('promotion_fee') is not None:
            self.promotion_fee = m.get('promotion_fee')

        if m.get('rate') is not None:
            self.rate = m.get('rate')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('reserve_rule') is not None:
            self.reserve_rule = m.get('reserve_rule')

        if m.get('room_no') is not None:
            self.room_no = m.get('room_no')

        if m.get('room_number') is not None:
            self.room_number = m.get('room_number')

        if m.get('room_price') is not None:
            self.room_price = m.get('room_price')

        if m.get('room_type') is not None:
            self.room_type = m.get('room_type')

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

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('status_desc') is not None:
            self.status_desc = m.get('status_desc')

        if m.get('sub_order_id') is not None:
            self.sub_order_id = m.get('sub_order_id')

        if m.get('tax_rate') is not None:
            self.tax_rate = m.get('tax_rate')

        if m.get('third_invoice_id') is not None:
            self.third_invoice_id = m.get('third_invoice_id')

        if m.get('third_itinerary_id') is not None:
            self.third_itinerary_id = m.get('third_itinerary_id')

        if m.get('third_part_business_id') is not None:
            self.third_part_business_id = m.get('third_part_business_id')

        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')

        if m.get('total_nights') is not None:
            self.total_nights = m.get('total_nights')

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

        if m.get('traveler_name') is not None:
            self.traveler_name = m.get('traveler_name')

        if m.get('voucher_type') is not None:
            self.voucher_type = m.get('voucher_type')

        if m.get('voucher_type_desc') is not None:
            self.voucher_type_desc = m.get('voucher_type_desc')

        return self

