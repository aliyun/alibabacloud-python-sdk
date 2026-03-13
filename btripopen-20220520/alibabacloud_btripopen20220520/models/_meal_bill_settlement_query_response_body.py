# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class MealBillSettlementQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        module: main_models.MealBillSettlementQueryResponseBodyModule = None,
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
            temp_model = main_models.MealBillSettlementQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class MealBillSettlementQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        category: int = None,
        corp_id: str = None,
        items: List[main_models.MealBillSettlementQueryResponseBodyModuleItems] = None,
        order_id: str = None,
        period_end: str = None,
        period_start: str = None,
        scroll_id: str = None,
        total_num: int = None,
        total_size: int = None,
    ):
        self.category = category
        self.corp_id = corp_id
        self.items = items
        self.order_id = order_id
        self.period_end = period_end
        self.period_start = period_start
        self.scroll_id = scroll_id
        self.total_num = total_num
        self.total_size = total_size

    def validate(self):
        if self.items:
            for v1 in self.items:
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

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.period_end is not None:
            result['period_end'] = self.period_end

        if self.period_start is not None:
            result['period_start'] = self.period_start

        if self.scroll_id is not None:
            result['scroll_id'] = self.scroll_id

        if self.total_num is not None:
            result['total_num'] = self.total_num

        if self.total_size is not None:
            result['total_size'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.MealBillSettlementQueryResponseBodyModuleItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('period_end') is not None:
            self.period_end = m.get('period_end')

        if m.get('period_start') is not None:
            self.period_start = m.get('period_start')

        if m.get('scroll_id') is not None:
            self.scroll_id = m.get('scroll_id')

        if m.get('total_num') is not None:
            self.total_num = m.get('total_num')

        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')

        return self

class MealBillSettlementQueryResponseBodyModuleItems(DaraModel):
    def __init__(
        self,
        adjust_time: str = None,
        apply_extend_field: str = None,
        apply_id: str = None,
        bill_record_time: str = None,
        book_time: str = None,
        booker_id: str = None,
        booker_job_no: str = None,
        booker_name: str = None,
        capital_direction: str = None,
        cascade_department: str = None,
        category_desc: str = None,
        consume_report_address: str = None,
        consume_report_city: str = None,
        consume_report_city_code: str = None,
        consumer_scene: str = None,
        corp_settle_fee: float = None,
        cost_center: str = None,
        cost_center_number: str = None,
        cost_department: str = None,
        department: str = None,
        department_id: str = None,
        fee_type: str = None,
        fee_type_desc: str = None,
        index: str = None,
        invoice_title: str = None,
        main_apply_id: str = None,
        mapping_company_code: str = None,
        meal_address: str = None,
        meal_city: str = None,
        meal_city_code: str = None,
        meal_reason: str = None,
        meal_rule: str = None,
        meal_scene: str = None,
        merchant_category: str = None,
        merchant_name: str = None,
        order_id: str = None,
        order_price: float = None,
        order_status_desc: str = None,
        person_settle_price: float = None,
        primary_id: int = None,
        processor_oa_code: str = None,
        project_code: str = None,
        project_name: str = None,
        remark: str = None,
        service_fee: float = None,
        settle_type_desc: str = None,
        settlement_fee: float = None,
        settlement_time: str = None,
        settlement_type: str = None,
        share_dinner: str = None,
        status: int = None,
        status_desc: str = None,
        store_address: str = None,
        tax_rate: str = None,
        third_invoice_id: str = None,
        third_part_business_id: str = None,
        thirdpart_apply_id: str = None,
        trade_action_desc: str = None,
        traveler_id: str = None,
        traveler_job_no: str = None,
        traveler_member_type: str = None,
        traveler_member_type_name: str = None,
        traveler_name: str = None,
        voucher_type: int = None,
        voucher_type_desc: str = None,
    ):
        self.adjust_time = adjust_time
        self.apply_extend_field = apply_extend_field
        self.apply_id = apply_id
        self.bill_record_time = bill_record_time
        self.book_time = book_time
        self.booker_id = booker_id
        self.booker_job_no = booker_job_no
        self.booker_name = booker_name
        self.capital_direction = capital_direction
        self.cascade_department = cascade_department
        self.category_desc = category_desc
        self.consume_report_address = consume_report_address
        self.consume_report_city = consume_report_city
        self.consume_report_city_code = consume_report_city_code
        self.consumer_scene = consumer_scene
        self.corp_settle_fee = corp_settle_fee
        self.cost_center = cost_center
        self.cost_center_number = cost_center_number
        self.cost_department = cost_department
        self.department = department
        self.department_id = department_id
        self.fee_type = fee_type
        self.fee_type_desc = fee_type_desc
        self.index = index
        self.invoice_title = invoice_title
        self.main_apply_id = main_apply_id
        self.mapping_company_code = mapping_company_code
        self.meal_address = meal_address
        self.meal_city = meal_city
        self.meal_city_code = meal_city_code
        self.meal_reason = meal_reason
        self.meal_rule = meal_rule
        self.meal_scene = meal_scene
        self.merchant_category = merchant_category
        self.merchant_name = merchant_name
        self.order_id = order_id
        self.order_price = order_price
        self.order_status_desc = order_status_desc
        self.person_settle_price = person_settle_price
        self.primary_id = primary_id
        self.processor_oa_code = processor_oa_code
        self.project_code = project_code
        self.project_name = project_name
        self.remark = remark
        self.service_fee = service_fee
        self.settle_type_desc = settle_type_desc
        self.settlement_fee = settlement_fee
        self.settlement_time = settlement_time
        self.settlement_type = settlement_type
        self.share_dinner = share_dinner
        self.status = status
        self.status_desc = status_desc
        self.store_address = store_address
        self.tax_rate = tax_rate
        self.third_invoice_id = third_invoice_id
        self.third_part_business_id = third_part_business_id
        self.thirdpart_apply_id = thirdpart_apply_id
        self.trade_action_desc = trade_action_desc
        self.traveler_id = traveler_id
        self.traveler_job_no = traveler_job_no
        self.traveler_member_type = traveler_member_type
        self.traveler_member_type_name = traveler_member_type_name
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

        if self.apply_extend_field is not None:
            result['apply_extend_field'] = self.apply_extend_field

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

        if self.category_desc is not None:
            result['category_desc'] = self.category_desc

        if self.consume_report_address is not None:
            result['consume_report_address'] = self.consume_report_address

        if self.consume_report_city is not None:
            result['consume_report_city'] = self.consume_report_city

        if self.consume_report_city_code is not None:
            result['consume_report_city_code'] = self.consume_report_city_code

        if self.consumer_scene is not None:
            result['consumer_scene'] = self.consumer_scene

        if self.corp_settle_fee is not None:
            result['corp_settle_fee'] = self.corp_settle_fee

        if self.cost_center is not None:
            result['cost_center'] = self.cost_center

        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number

        if self.cost_department is not None:
            result['cost_department'] = self.cost_department

        if self.department is not None:
            result['department'] = self.department

        if self.department_id is not None:
            result['department_id'] = self.department_id

        if self.fee_type is not None:
            result['fee_type'] = self.fee_type

        if self.fee_type_desc is not None:
            result['fee_type_desc'] = self.fee_type_desc

        if self.index is not None:
            result['index'] = self.index

        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title

        if self.main_apply_id is not None:
            result['main_apply_id'] = self.main_apply_id

        if self.mapping_company_code is not None:
            result['mapping_company_code'] = self.mapping_company_code

        if self.meal_address is not None:
            result['meal_address'] = self.meal_address

        if self.meal_city is not None:
            result['meal_city'] = self.meal_city

        if self.meal_city_code is not None:
            result['meal_city_code'] = self.meal_city_code

        if self.meal_reason is not None:
            result['meal_reason'] = self.meal_reason

        if self.meal_rule is not None:
            result['meal_rule'] = self.meal_rule

        if self.meal_scene is not None:
            result['meal_scene'] = self.meal_scene

        if self.merchant_category is not None:
            result['merchant_category'] = self.merchant_category

        if self.merchant_name is not None:
            result['merchant_name'] = self.merchant_name

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.order_price is not None:
            result['order_price'] = self.order_price

        if self.order_status_desc is not None:
            result['order_status_desc'] = self.order_status_desc

        if self.person_settle_price is not None:
            result['person_settle_price'] = self.person_settle_price

        if self.primary_id is not None:
            result['primary_id'] = self.primary_id

        if self.processor_oa_code is not None:
            result['processor_oa_code'] = self.processor_oa_code

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_name is not None:
            result['project_name'] = self.project_name

        if self.remark is not None:
            result['remark'] = self.remark

        if self.service_fee is not None:
            result['service_fee'] = self.service_fee

        if self.settle_type_desc is not None:
            result['settle_type_desc'] = self.settle_type_desc

        if self.settlement_fee is not None:
            result['settlement_fee'] = self.settlement_fee

        if self.settlement_time is not None:
            result['settlement_time'] = self.settlement_time

        if self.settlement_type is not None:
            result['settlement_type'] = self.settlement_type

        if self.share_dinner is not None:
            result['share_dinner'] = self.share_dinner

        if self.status is not None:
            result['status'] = self.status

        if self.status_desc is not None:
            result['status_desc'] = self.status_desc

        if self.store_address is not None:
            result['store_address'] = self.store_address

        if self.tax_rate is not None:
            result['tax_rate'] = self.tax_rate

        if self.third_invoice_id is not None:
            result['third_invoice_id'] = self.third_invoice_id

        if self.third_part_business_id is not None:
            result['third_part_business_id'] = self.third_part_business_id

        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id

        if self.trade_action_desc is not None:
            result['trade_action_desc'] = self.trade_action_desc

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

        if self.voucher_type is not None:
            result['voucher_type'] = self.voucher_type

        if self.voucher_type_desc is not None:
            result['voucher_type_desc'] = self.voucher_type_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adjust_time') is not None:
            self.adjust_time = m.get('adjust_time')

        if m.get('apply_extend_field') is not None:
            self.apply_extend_field = m.get('apply_extend_field')

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

        if m.get('category_desc') is not None:
            self.category_desc = m.get('category_desc')

        if m.get('consume_report_address') is not None:
            self.consume_report_address = m.get('consume_report_address')

        if m.get('consume_report_city') is not None:
            self.consume_report_city = m.get('consume_report_city')

        if m.get('consume_report_city_code') is not None:
            self.consume_report_city_code = m.get('consume_report_city_code')

        if m.get('consumer_scene') is not None:
            self.consumer_scene = m.get('consumer_scene')

        if m.get('corp_settle_fee') is not None:
            self.corp_settle_fee = m.get('corp_settle_fee')

        if m.get('cost_center') is not None:
            self.cost_center = m.get('cost_center')

        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')

        if m.get('cost_department') is not None:
            self.cost_department = m.get('cost_department')

        if m.get('department') is not None:
            self.department = m.get('department')

        if m.get('department_id') is not None:
            self.department_id = m.get('department_id')

        if m.get('fee_type') is not None:
            self.fee_type = m.get('fee_type')

        if m.get('fee_type_desc') is not None:
            self.fee_type_desc = m.get('fee_type_desc')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')

        if m.get('main_apply_id') is not None:
            self.main_apply_id = m.get('main_apply_id')

        if m.get('mapping_company_code') is not None:
            self.mapping_company_code = m.get('mapping_company_code')

        if m.get('meal_address') is not None:
            self.meal_address = m.get('meal_address')

        if m.get('meal_city') is not None:
            self.meal_city = m.get('meal_city')

        if m.get('meal_city_code') is not None:
            self.meal_city_code = m.get('meal_city_code')

        if m.get('meal_reason') is not None:
            self.meal_reason = m.get('meal_reason')

        if m.get('meal_rule') is not None:
            self.meal_rule = m.get('meal_rule')

        if m.get('meal_scene') is not None:
            self.meal_scene = m.get('meal_scene')

        if m.get('merchant_category') is not None:
            self.merchant_category = m.get('merchant_category')

        if m.get('merchant_name') is not None:
            self.merchant_name = m.get('merchant_name')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('order_price') is not None:
            self.order_price = m.get('order_price')

        if m.get('order_status_desc') is not None:
            self.order_status_desc = m.get('order_status_desc')

        if m.get('person_settle_price') is not None:
            self.person_settle_price = m.get('person_settle_price')

        if m.get('primary_id') is not None:
            self.primary_id = m.get('primary_id')

        if m.get('processor_oa_code') is not None:
            self.processor_oa_code = m.get('processor_oa_code')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_name') is not None:
            self.project_name = m.get('project_name')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')

        if m.get('settle_type_desc') is not None:
            self.settle_type_desc = m.get('settle_type_desc')

        if m.get('settlement_fee') is not None:
            self.settlement_fee = m.get('settlement_fee')

        if m.get('settlement_time') is not None:
            self.settlement_time = m.get('settlement_time')

        if m.get('settlement_type') is not None:
            self.settlement_type = m.get('settlement_type')

        if m.get('share_dinner') is not None:
            self.share_dinner = m.get('share_dinner')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('status_desc') is not None:
            self.status_desc = m.get('status_desc')

        if m.get('store_address') is not None:
            self.store_address = m.get('store_address')

        if m.get('tax_rate') is not None:
            self.tax_rate = m.get('tax_rate')

        if m.get('third_invoice_id') is not None:
            self.third_invoice_id = m.get('third_invoice_id')

        if m.get('third_part_business_id') is not None:
            self.third_part_business_id = m.get('third_part_business_id')

        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')

        if m.get('trade_action_desc') is not None:
            self.trade_action_desc = m.get('trade_action_desc')

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

        if m.get('voucher_type') is not None:
            self.voucher_type = m.get('voucher_type')

        if m.get('voucher_type_desc') is not None:
            self.voucher_type_desc = m.get('voucher_type_desc')

        return self

