# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class QueryReimbursementOrderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.QueryReimbursementOrderResponseBodyModule = None,
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
            temp_model = main_models.QueryReimbursementOrderResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class QueryReimbursementOrderResponseBodyModule(DaraModel):
    def __init__(
        self,
        company_amount: str = None,
        company_pay_amount: str = None,
        corp_id: str = None,
        cost_center_code: str = None,
        cost_center_name: str = None,
        expenses: List[main_models.QueryReimbursementOrderResponseBodyModuleExpenses] = None,
        expenses_cover_dept_id: str = None,
        expenses_cover_dept_name: str = None,
        expenses_cover_invoice_title: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        is_deleted: str = None,
        itineraries: List[main_models.QueryReimbursementOrderResponseBodyModuleItineraries] = None,
        payment_finish_time: str = None,
        payment_infos: List[main_models.QueryReimbursementOrderResponseBodyModulePaymentInfos] = None,
        personal_amount: str = None,
        process_end_time: str = None,
        project_code: str = None,
        project_name: str = None,
        reason: str = None,
        reimbursement_no: str = None,
        remark: str = None,
        status: str = None,
        travel_third_apply_id: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.company_amount = company_amount
        self.company_pay_amount = company_pay_amount
        self.corp_id = corp_id
        self.cost_center_code = cost_center_code
        self.cost_center_name = cost_center_name
        self.expenses = expenses
        self.expenses_cover_dept_id = expenses_cover_dept_id
        self.expenses_cover_dept_name = expenses_cover_dept_name
        self.expenses_cover_invoice_title = expenses_cover_invoice_title
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.is_deleted = is_deleted
        self.itineraries = itineraries
        self.payment_finish_time = payment_finish_time
        self.payment_infos = payment_infos
        self.personal_amount = personal_amount
        self.process_end_time = process_end_time
        self.project_code = project_code
        self.project_name = project_name
        self.reason = reason
        self.reimbursement_no = reimbursement_no
        self.remark = remark
        self.status = status
        self.travel_third_apply_id = travel_third_apply_id
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.expenses:
            for v1 in self.expenses:
                 if v1:
                    v1.validate()
        if self.itineraries:
            for v1 in self.itineraries:
                 if v1:
                    v1.validate()
        if self.payment_infos:
            for v1 in self.payment_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_amount is not None:
            result['company_amount'] = self.company_amount

        if self.company_pay_amount is not None:
            result['company_pay_amount'] = self.company_pay_amount

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.cost_center_code is not None:
            result['cost_center_code'] = self.cost_center_code

        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name

        result['expenses'] = []
        if self.expenses is not None:
            for k1 in self.expenses:
                result['expenses'].append(k1.to_map() if k1 else None)

        if self.expenses_cover_dept_id is not None:
            result['expenses_cover_dept_id'] = self.expenses_cover_dept_id

        if self.expenses_cover_dept_name is not None:
            result['expenses_cover_dept_name'] = self.expenses_cover_dept_name

        if self.expenses_cover_invoice_title is not None:
            result['expenses_cover_invoice_title'] = self.expenses_cover_invoice_title

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified

        if self.is_deleted is not None:
            result['is_deleted'] = self.is_deleted

        result['itineraries'] = []
        if self.itineraries is not None:
            for k1 in self.itineraries:
                result['itineraries'].append(k1.to_map() if k1 else None)

        if self.payment_finish_time is not None:
            result['payment_finish_time'] = self.payment_finish_time

        result['payment_infos'] = []
        if self.payment_infos is not None:
            for k1 in self.payment_infos:
                result['payment_infos'].append(k1.to_map() if k1 else None)

        if self.personal_amount is not None:
            result['personal_amount'] = self.personal_amount

        if self.process_end_time is not None:
            result['process_end_time'] = self.process_end_time

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_name is not None:
            result['project_name'] = self.project_name

        if self.reason is not None:
            result['reason'] = self.reason

        if self.reimbursement_no is not None:
            result['reimbursement_no'] = self.reimbursement_no

        if self.remark is not None:
            result['remark'] = self.remark

        if self.status is not None:
            result['status'] = self.status

        if self.travel_third_apply_id is not None:
            result['travel_third_apply_id'] = self.travel_third_apply_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('company_amount') is not None:
            self.company_amount = m.get('company_amount')

        if m.get('company_pay_amount') is not None:
            self.company_pay_amount = m.get('company_pay_amount')

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('cost_center_code') is not None:
            self.cost_center_code = m.get('cost_center_code')

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        self.expenses = []
        if m.get('expenses') is not None:
            for k1 in m.get('expenses'):
                temp_model = main_models.QueryReimbursementOrderResponseBodyModuleExpenses()
                self.expenses.append(temp_model.from_map(k1))

        if m.get('expenses_cover_dept_id') is not None:
            self.expenses_cover_dept_id = m.get('expenses_cover_dept_id')

        if m.get('expenses_cover_dept_name') is not None:
            self.expenses_cover_dept_name = m.get('expenses_cover_dept_name')

        if m.get('expenses_cover_invoice_title') is not None:
            self.expenses_cover_invoice_title = m.get('expenses_cover_invoice_title')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')

        if m.get('is_deleted') is not None:
            self.is_deleted = m.get('is_deleted')

        self.itineraries = []
        if m.get('itineraries') is not None:
            for k1 in m.get('itineraries'):
                temp_model = main_models.QueryReimbursementOrderResponseBodyModuleItineraries()
                self.itineraries.append(temp_model.from_map(k1))

        if m.get('payment_finish_time') is not None:
            self.payment_finish_time = m.get('payment_finish_time')

        self.payment_infos = []
        if m.get('payment_infos') is not None:
            for k1 in m.get('payment_infos'):
                temp_model = main_models.QueryReimbursementOrderResponseBodyModulePaymentInfos()
                self.payment_infos.append(temp_model.from_map(k1))

        if m.get('personal_amount') is not None:
            self.personal_amount = m.get('personal_amount')

        if m.get('process_end_time') is not None:
            self.process_end_time = m.get('process_end_time')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_name') is not None:
            self.project_name = m.get('project_name')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('reimbursement_no') is not None:
            self.reimbursement_no = m.get('reimbursement_no')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('travel_third_apply_id') is not None:
            self.travel_third_apply_id = m.get('travel_third_apply_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class QueryReimbursementOrderResponseBodyModulePaymentInfos(DaraModel):
    def __init__(
        self,
        amount: str = None,
        payee_account_number: str = None,
        payee_user_id: str = None,
    ):
        self.amount = amount
        self.payee_account_number = payee_account_number
        self.payee_user_id = payee_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.payee_account_number is not None:
            result['payee_account_number'] = self.payee_account_number

        if self.payee_user_id is not None:
            result['payee_user_id'] = self.payee_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('payee_account_number') is not None:
            self.payee_account_number = m.get('payee_account_number')

        if m.get('payee_user_id') is not None:
            self.payee_user_id = m.get('payee_user_id')

        return self

class QueryReimbursementOrderResponseBodyModuleItineraries(DaraModel):
    def __init__(
        self,
        arr_city: str = None,
        arr_date: str = None,
        dep_city: str = None,
        dep_date: str = None,
        traffic_way: str = None,
        trip_way: str = None,
    ):
        self.arr_city = arr_city
        self.arr_date = arr_date
        self.dep_city = dep_city
        self.dep_date = dep_date
        self.traffic_way = traffic_way
        self.trip_way = trip_way

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_date is not None:
            result['arr_date'] = self.arr_date

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.traffic_way is not None:
            result['traffic_way'] = self.traffic_way

        if self.trip_way is not None:
            result['trip_way'] = self.trip_way

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_date') is not None:
            self.arr_date = m.get('arr_date')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('traffic_way') is not None:
            self.traffic_way = m.get('traffic_way')

        if m.get('trip_way') is not None:
            self.trip_way = m.get('trip_way')

        return self

class QueryReimbursementOrderResponseBodyModuleExpenses(DaraModel):
    def __init__(
        self,
        amount: str = None,
        currency: str = None,
        expense_city: str = None,
        expense_compositions: List[main_models.QueryReimbursementOrderResponseBodyModuleExpensesExpenseCompositions] = None,
        expense_time: str = None,
        expense_type: str = None,
        expense_type_code: str = None,
        invoice_infos: List[main_models.QueryReimbursementOrderResponseBodyModuleExpensesInvoiceInfos] = None,
        reimb_expense_id: int = None,
        remark: str = None,
        settlement_type: str = None,
    ):
        self.amount = amount
        self.currency = currency
        self.expense_city = expense_city
        self.expense_compositions = expense_compositions
        self.expense_time = expense_time
        self.expense_type = expense_type
        self.expense_type_code = expense_type_code
        self.invoice_infos = invoice_infos
        self.reimb_expense_id = reimb_expense_id
        self.remark = remark
        self.settlement_type = settlement_type

    def validate(self):
        if self.expense_compositions:
            for v1 in self.expense_compositions:
                 if v1:
                    v1.validate()
        if self.invoice_infos:
            for v1 in self.invoice_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.currency is not None:
            result['currency'] = self.currency

        if self.expense_city is not None:
            result['expense_city'] = self.expense_city

        result['expense_compositions'] = []
        if self.expense_compositions is not None:
            for k1 in self.expense_compositions:
                result['expense_compositions'].append(k1.to_map() if k1 else None)

        if self.expense_time is not None:
            result['expense_time'] = self.expense_time

        if self.expense_type is not None:
            result['expense_type'] = self.expense_type

        if self.expense_type_code is not None:
            result['expense_type_code'] = self.expense_type_code

        result['invoice_infos'] = []
        if self.invoice_infos is not None:
            for k1 in self.invoice_infos:
                result['invoice_infos'].append(k1.to_map() if k1 else None)

        if self.reimb_expense_id is not None:
            result['reimb_expense_id'] = self.reimb_expense_id

        if self.remark is not None:
            result['remark'] = self.remark

        if self.settlement_type is not None:
            result['settlement_type'] = self.settlement_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('currency') is not None:
            self.currency = m.get('currency')

        if m.get('expense_city') is not None:
            self.expense_city = m.get('expense_city')

        self.expense_compositions = []
        if m.get('expense_compositions') is not None:
            for k1 in m.get('expense_compositions'):
                temp_model = main_models.QueryReimbursementOrderResponseBodyModuleExpensesExpenseCompositions()
                self.expense_compositions.append(temp_model.from_map(k1))

        if m.get('expense_time') is not None:
            self.expense_time = m.get('expense_time')

        if m.get('expense_type') is not None:
            self.expense_type = m.get('expense_type')

        if m.get('expense_type_code') is not None:
            self.expense_type_code = m.get('expense_type_code')

        self.invoice_infos = []
        if m.get('invoice_infos') is not None:
            for k1 in m.get('invoice_infos'):
                temp_model = main_models.QueryReimbursementOrderResponseBodyModuleExpensesInvoiceInfos()
                self.invoice_infos.append(temp_model.from_map(k1))

        if m.get('reimb_expense_id') is not None:
            self.reimb_expense_id = m.get('reimb_expense_id')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('settlement_type') is not None:
            self.settlement_type = m.get('settlement_type')

        return self

class QueryReimbursementOrderResponseBodyModuleExpensesInvoiceInfos(DaraModel):
    def __init__(
        self,
        amount: str = None,
        invoice_code: str = None,
        invoice_data: str = None,
        invoice_date: str = None,
        invoice_number: str = None,
        invoice_type: str = None,
    ):
        self.amount = amount
        self.invoice_code = invoice_code
        self.invoice_data = invoice_data
        self.invoice_date = invoice_date
        self.invoice_number = invoice_number
        self.invoice_type = invoice_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.invoice_code is not None:
            result['invoice_code'] = self.invoice_code

        if self.invoice_data is not None:
            result['invoice_data'] = self.invoice_data

        if self.invoice_date is not None:
            result['invoice_date'] = self.invoice_date

        if self.invoice_number is not None:
            result['invoice_number'] = self.invoice_number

        if self.invoice_type is not None:
            result['invoice_type'] = self.invoice_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('invoice_code') is not None:
            self.invoice_code = m.get('invoice_code')

        if m.get('invoice_data') is not None:
            self.invoice_data = m.get('invoice_data')

        if m.get('invoice_date') is not None:
            self.invoice_date = m.get('invoice_date')

        if m.get('invoice_number') is not None:
            self.invoice_number = m.get('invoice_number')

        if m.get('invoice_type') is not None:
            self.invoice_type = m.get('invoice_type')

        return self

class QueryReimbursementOrderResponseBodyModuleExpensesExpenseCompositions(DaraModel):
    def __init__(
        self,
        bill_settlement_id: int = None,
        capital_direction: str = None,
        fee_type: str = None,
        order_id: str = None,
        remark: str = None,
        remind_tag_list: List[str] = None,
        settlement_amount: str = None,
        settlement_time: str = None,
        voucher_type: int = None,
    ):
        self.bill_settlement_id = bill_settlement_id
        self.capital_direction = capital_direction
        self.fee_type = fee_type
        self.order_id = order_id
        self.remark = remark
        self.remind_tag_list = remind_tag_list
        self.settlement_amount = settlement_amount
        self.settlement_time = settlement_time
        self.voucher_type = voucher_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_settlement_id is not None:
            result['bill_settlement_id'] = self.bill_settlement_id

        if self.capital_direction is not None:
            result['capital_direction'] = self.capital_direction

        if self.fee_type is not None:
            result['fee_type'] = self.fee_type

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.remark is not None:
            result['remark'] = self.remark

        if self.remind_tag_list is not None:
            result['remind_tag_list'] = self.remind_tag_list

        if self.settlement_amount is not None:
            result['settlement_amount'] = self.settlement_amount

        if self.settlement_time is not None:
            result['settlement_time'] = self.settlement_time

        if self.voucher_type is not None:
            result['voucher_type'] = self.voucher_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bill_settlement_id') is not None:
            self.bill_settlement_id = m.get('bill_settlement_id')

        if m.get('capital_direction') is not None:
            self.capital_direction = m.get('capital_direction')

        if m.get('fee_type') is not None:
            self.fee_type = m.get('fee_type')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('remind_tag_list') is not None:
            self.remind_tag_list = m.get('remind_tag_list')

        if m.get('settlement_amount') is not None:
            self.settlement_amount = m.get('settlement_amount')

        if m.get('settlement_time') is not None:
            self.settlement_time = m.get('settlement_time')

        if m.get('voucher_type') is not None:
            self.voucher_type = m.get('voucher_type')

        return self

