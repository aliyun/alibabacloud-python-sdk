# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightOrderListQueryV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[main_models.FlightOrderListQueryV2ResponseBodyModule] = None,
        page_info: main_models.FlightOrderListQueryV2ResponseBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.page_info = page_info
        self.request_id = request_id
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        result['module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['module'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['pageInfo'] = self.page_info.to_map()

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

        self.module = []
        if m.get('module') is not None:
            for k1 in m.get('module'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('pageInfo') is not None:
            temp_model = main_models.FlightOrderListQueryV2ResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('pageInfo'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightOrderListQueryV2ResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        number: int = None,
        scroll_id: str = None,
        total_number: int = None,
    ):
        self.number = number
        self.scroll_id = scroll_id
        self.total_number = total_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.number is not None:
            result['number'] = self.number

        if self.scroll_id is not None:
            result['scroll_id'] = self.scroll_id

        if self.total_number is not None:
            result['total_number'] = self.total_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('number') is not None:
            self.number = m.get('number')

        if m.get('scroll_id') is not None:
            self.scroll_id = m.get('scroll_id')

        if m.get('total_number') is not None:
            self.total_number = m.get('total_number')

        return self

class FlightOrderListQueryV2ResponseBodyModule(DaraModel):
    def __init__(
        self,
        approve: main_models.FlightOrderListQueryV2ResponseBodyModuleApprove = None,
        corp_id: str = None,
        corp_name: str = None,
        depart_id: str = None,
        depart_name: str = None,
        flight_order_ticket_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleFlightOrderTicketList] = None,
        flight_order_user_fee_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleFlightOrderUserFeeList] = None,
        flight_refund_apply_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleFlightRefundApplyList] = None,
        flight_reshop_apply_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleFlightReshopApplyList] = None,
        flight_segment_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleFlightSegmentList] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: str = None,
        insure_info_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleInsureInfoList] = None,
        mix_pay: bool = None,
        order_reserve_amount: float = None,
        passenger_count: int = None,
        pay_time: str = None,
        price_info_list: List[main_models.FlightOrderListQueryV2ResponseBodyModulePriceInfoList] = None,
        status: int = None,
        supplier: str = None,
        thirdpart_itinerary_id: List[str] = None,
        ticket_corp_reserve_amount: float = None,
        ticket_person_reserve_amount: float = None,
        trip_mode: int = None,
        trip_type: int = None,
        user_affiliate_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleUserAffiliateList] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.approve = approve
        self.corp_id = corp_id
        self.corp_name = corp_name
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.flight_order_ticket_list = flight_order_ticket_list
        self.flight_order_user_fee_list = flight_order_user_fee_list
        self.flight_refund_apply_list = flight_refund_apply_list
        self.flight_reshop_apply_list = flight_reshop_apply_list
        self.flight_segment_list = flight_segment_list
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.insure_info_list = insure_info_list
        self.mix_pay = mix_pay
        self.order_reserve_amount = order_reserve_amount
        self.passenger_count = passenger_count
        self.pay_time = pay_time
        self.price_info_list = price_info_list
        self.status = status
        self.supplier = supplier
        self.thirdpart_itinerary_id = thirdpart_itinerary_id
        self.ticket_corp_reserve_amount = ticket_corp_reserve_amount
        self.ticket_person_reserve_amount = ticket_person_reserve_amount
        self.trip_mode = trip_mode
        self.trip_type = trip_type
        self.user_affiliate_list = user_affiliate_list
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.approve:
            self.approve.validate()
        if self.flight_order_ticket_list:
            for v1 in self.flight_order_ticket_list:
                 if v1:
                    v1.validate()
        if self.flight_order_user_fee_list:
            for v1 in self.flight_order_user_fee_list:
                 if v1:
                    v1.validate()
        if self.flight_refund_apply_list:
            for v1 in self.flight_refund_apply_list:
                 if v1:
                    v1.validate()
        if self.flight_reshop_apply_list:
            for v1 in self.flight_reshop_apply_list:
                 if v1:
                    v1.validate()
        if self.flight_segment_list:
            for v1 in self.flight_segment_list:
                 if v1:
                    v1.validate()
        if self.insure_info_list:
            for v1 in self.insure_info_list:
                 if v1:
                    v1.validate()
        if self.price_info_list:
            for v1 in self.price_info_list:
                 if v1:
                    v1.validate()
        if self.user_affiliate_list:
            for v1 in self.user_affiliate_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approve is not None:
            result['approve'] = self.approve.to_map()

        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.corp_name is not None:
            result['corp_name'] = self.corp_name

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        result['flight_order_ticket_list'] = []
        if self.flight_order_ticket_list is not None:
            for k1 in self.flight_order_ticket_list:
                result['flight_order_ticket_list'].append(k1.to_map() if k1 else None)

        result['flight_order_user_fee_list'] = []
        if self.flight_order_user_fee_list is not None:
            for k1 in self.flight_order_user_fee_list:
                result['flight_order_user_fee_list'].append(k1.to_map() if k1 else None)

        result['flight_refund_apply_list'] = []
        if self.flight_refund_apply_list is not None:
            for k1 in self.flight_refund_apply_list:
                result['flight_refund_apply_list'].append(k1.to_map() if k1 else None)

        result['flight_reshop_apply_list'] = []
        if self.flight_reshop_apply_list is not None:
            for k1 in self.flight_reshop_apply_list:
                result['flight_reshop_apply_list'].append(k1.to_map() if k1 else None)

        result['flight_segment_list'] = []
        if self.flight_segment_list is not None:
            for k1 in self.flight_segment_list:
                result['flight_segment_list'].append(k1.to_map() if k1 else None)

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmt_modified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        result['insure_info_list'] = []
        if self.insure_info_list is not None:
            for k1 in self.insure_info_list:
                result['insure_info_list'].append(k1.to_map() if k1 else None)

        if self.mix_pay is not None:
            result['mix_pay'] = self.mix_pay

        if self.order_reserve_amount is not None:
            result['order_reserve_amount'] = self.order_reserve_amount

        if self.passenger_count is not None:
            result['passenger_count'] = self.passenger_count

        if self.pay_time is not None:
            result['pay_time'] = self.pay_time

        result['price_info_list'] = []
        if self.price_info_list is not None:
            for k1 in self.price_info_list:
                result['price_info_list'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.supplier is not None:
            result['supplier'] = self.supplier

        if self.thirdpart_itinerary_id is not None:
            result['thirdpart_itinerary_id'] = self.thirdpart_itinerary_id

        if self.ticket_corp_reserve_amount is not None:
            result['ticket_corp_reserve_amount'] = self.ticket_corp_reserve_amount

        if self.ticket_person_reserve_amount is not None:
            result['ticket_person_reserve_amount'] = self.ticket_person_reserve_amount

        if self.trip_mode is not None:
            result['trip_mode'] = self.trip_mode

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        result['user_affiliate_list'] = []
        if self.user_affiliate_list is not None:
            for k1 in self.user_affiliate_list:
                result['user_affiliate_list'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('approve') is not None:
            temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleApprove()
            self.approve = temp_model.from_map(m.get('approve'))

        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('corp_name') is not None:
            self.corp_name = m.get('corp_name')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        self.flight_order_ticket_list = []
        if m.get('flight_order_ticket_list') is not None:
            for k1 in m.get('flight_order_ticket_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleFlightOrderTicketList()
                self.flight_order_ticket_list.append(temp_model.from_map(k1))

        self.flight_order_user_fee_list = []
        if m.get('flight_order_user_fee_list') is not None:
            for k1 in m.get('flight_order_user_fee_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleFlightOrderUserFeeList()
                self.flight_order_user_fee_list.append(temp_model.from_map(k1))

        self.flight_refund_apply_list = []
        if m.get('flight_refund_apply_list') is not None:
            for k1 in m.get('flight_refund_apply_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleFlightRefundApplyList()
                self.flight_refund_apply_list.append(temp_model.from_map(k1))

        self.flight_reshop_apply_list = []
        if m.get('flight_reshop_apply_list') is not None:
            for k1 in m.get('flight_reshop_apply_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleFlightReshopApplyList()
                self.flight_reshop_apply_list.append(temp_model.from_map(k1))

        self.flight_segment_list = []
        if m.get('flight_segment_list') is not None:
            for k1 in m.get('flight_segment_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleFlightSegmentList()
                self.flight_segment_list.append(temp_model.from_map(k1))

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_modified') is not None:
            self.gmt_modified = m.get('gmt_modified')

        if m.get('id') is not None:
            self.id = m.get('id')

        self.insure_info_list = []
        if m.get('insure_info_list') is not None:
            for k1 in m.get('insure_info_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleInsureInfoList()
                self.insure_info_list.append(temp_model.from_map(k1))

        if m.get('mix_pay') is not None:
            self.mix_pay = m.get('mix_pay')

        if m.get('order_reserve_amount') is not None:
            self.order_reserve_amount = m.get('order_reserve_amount')

        if m.get('passenger_count') is not None:
            self.passenger_count = m.get('passenger_count')

        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')

        self.price_info_list = []
        if m.get('price_info_list') is not None:
            for k1 in m.get('price_info_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModulePriceInfoList()
                self.price_info_list.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('supplier') is not None:
            self.supplier = m.get('supplier')

        if m.get('thirdpart_itinerary_id') is not None:
            self.thirdpart_itinerary_id = m.get('thirdpart_itinerary_id')

        if m.get('ticket_corp_reserve_amount') is not None:
            self.ticket_corp_reserve_amount = m.get('ticket_corp_reserve_amount')

        if m.get('ticket_person_reserve_amount') is not None:
            self.ticket_person_reserve_amount = m.get('ticket_person_reserve_amount')

        if m.get('trip_mode') is not None:
            self.trip_mode = m.get('trip_mode')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        self.user_affiliate_list = []
        if m.get('user_affiliate_list') is not None:
            for k1 in m.get('user_affiliate_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleUserAffiliateList()
                self.user_affiliate_list.append(temp_model.from_map(k1))

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class FlightOrderListQueryV2ResponseBodyModuleUserAffiliateList(DaraModel):
    def __init__(
        self,
        cost_center: main_models.FlightOrderListQueryV2ResponseBodyModuleUserAffiliateListCostCenter = None,
        department: main_models.FlightOrderListQueryV2ResponseBodyModuleUserAffiliateListDepartment = None,
        invoice: main_models.FlightOrderListQueryV2ResponseBodyModuleUserAffiliateListInvoice = None,
        project: main_models.FlightOrderListQueryV2ResponseBodyModuleUserAffiliateListProject = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.cost_center = cost_center
        self.department = department
        self.invoice = invoice
        self.project = project
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.cost_center:
            self.cost_center.validate()
        if self.department:
            self.department.validate()
        if self.invoice:
            self.invoice.validate()
        if self.project:
            self.project.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center is not None:
            result['cost_center'] = self.cost_center.to_map()

        if self.department is not None:
            result['department'] = self.department.to_map()

        if self.invoice is not None:
            result['invoice'] = self.invoice.to_map()

        if self.project is not None:
            result['project'] = self.project.to_map()

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost_center') is not None:
            temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleUserAffiliateListCostCenter()
            self.cost_center = temp_model.from_map(m.get('cost_center'))

        if m.get('department') is not None:
            temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleUserAffiliateListDepartment()
            self.department = temp_model.from_map(m.get('department'))

        if m.get('invoice') is not None:
            temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleUserAffiliateListInvoice()
            self.invoice = temp_model.from_map(m.get('invoice'))

        if m.get('project') is not None:
            temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleUserAffiliateListProject()
            self.project = temp_model.from_map(m.get('project'))

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

class FlightOrderListQueryV2ResponseBodyModuleUserAffiliateListProject(DaraModel):
    def __init__(
        self,
        project_id: str = None,
        project_title: str = None,
        thirdpart_project_id: str = None,
    ):
        self.project_id = project_id
        self.project_title = project_title
        self.thirdpart_project_id = thirdpart_project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id is not None:
            result['project_id'] = self.project_id

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.thirdpart_project_id is not None:
            result['thirdpart_project_id'] = self.thirdpart_project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('thirdpart_project_id') is not None:
            self.thirdpart_project_id = m.get('thirdpart_project_id')

        return self

class FlightOrderListQueryV2ResponseBodyModuleUserAffiliateListInvoice(DaraModel):
    def __init__(
        self,
        id: int = None,
        title: str = None,
    ):
        self.id = id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOrderListQueryV2ResponseBodyModuleUserAffiliateListDepartment(DaraModel):
    def __init__(
        self,
        depart_id: str = None,
        depart_name: str = None,
    ):
        self.depart_id = depart_id
        self.depart_name = depart_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        return self

class FlightOrderListQueryV2ResponseBodyModuleUserAffiliateListCostCenter(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        id: int = None,
        name: str = None,
        number: str = None,
    ):
        self.corp_id = corp_id
        self.id = id
        self.name = name
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_id is not None:
            result['corp_id'] = self.corp_id

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.number is not None:
            result['number'] = self.number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corp_id') is not None:
            self.corp_id = m.get('corp_id')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('number') is not None:
            self.number = m.get('number')

        return self

class FlightOrderListQueryV2ResponseBodyModulePriceInfoList(DaraModel):
    def __init__(
        self,
        category_code: int = None,
        category_type: int = None,
        gmt_create: str = None,
        pay_type: int = None,
        price: float = None,
        sub_order_id: str = None,
        trade_id: str = None,
        type: int = None,
    ):
        self.category_code = category_code
        self.category_type = category_type
        self.gmt_create = gmt_create
        self.pay_type = pay_type
        self.price = price
        self.sub_order_id = sub_order_id
        self.trade_id = trade_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_code is not None:
            result['category_code'] = self.category_code

        if self.category_type is not None:
            result['category_type'] = self.category_type

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.pay_type is not None:
            result['pay_type'] = self.pay_type

        if self.price is not None:
            result['price'] = self.price

        if self.sub_order_id is not None:
            result['sub_order_id'] = self.sub_order_id

        if self.trade_id is not None:
            result['trade_id'] = self.trade_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category_code') is not None:
            self.category_code = m.get('category_code')

        if m.get('category_type') is not None:
            self.category_type = m.get('category_type')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('sub_order_id') is not None:
            self.sub_order_id = m.get('sub_order_id')

        if m.get('trade_id') is not None:
            self.trade_id = m.get('trade_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightOrderListQueryV2ResponseBodyModuleInsureInfoList(DaraModel):
    def __init__(
        self,
        insure_id: str = None,
        insure_order_amount: float = None,
        insure_price: float = None,
        insure_type: str = None,
        name_list: List[str] = None,
        number: int = None,
        status: int = None,
    ):
        self.insure_id = insure_id
        self.insure_order_amount = insure_order_amount
        self.insure_price = insure_price
        self.insure_type = insure_type
        self.name_list = name_list
        self.number = number
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.insure_id is not None:
            result['insure_id'] = self.insure_id

        if self.insure_order_amount is not None:
            result['insure_order_amount'] = self.insure_order_amount

        if self.insure_price is not None:
            result['insure_price'] = self.insure_price

        if self.insure_type is not None:
            result['insure_type'] = self.insure_type

        if self.name_list is not None:
            result['name_list'] = self.name_list

        if self.number is not None:
            result['number'] = self.number

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('insure_id') is not None:
            self.insure_id = m.get('insure_id')

        if m.get('insure_order_amount') is not None:
            self.insure_order_amount = m.get('insure_order_amount')

        if m.get('insure_price') is not None:
            self.insure_price = m.get('insure_price')

        if m.get('insure_type') is not None:
            self.insure_type = m.get('insure_type')

        if m.get('name_list') is not None:
            self.name_list = m.get('name_list')

        if m.get('number') is not None:
            self.number = m.get('number')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class FlightOrderListQueryV2ResponseBodyModuleFlightSegmentList(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        arr_apt: str = None,
        arr_apt_code: str = None,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_terminal: str = None,
        arr_time: str = None,
        dep_apt: str = None,
        dep_apt_code: str = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_terminal: str = None,
        dep_time: str = None,
        flight_mile: int = None,
        flight_no: str = None,
        journey_index: int = None,
        segment_index: int = None,
        stop_city: List[str] = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.arr_apt = arr_apt
        self.arr_apt_code = arr_apt_code
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.arr_terminal = arr_terminal
        self.arr_time = arr_time
        self.dep_apt = dep_apt
        self.dep_apt_code = dep_apt_code
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.dep_terminal = dep_terminal
        self.dep_time = dep_time
        self.flight_mile = flight_mile
        self.flight_no = flight_no
        self.journey_index = journey_index
        self.segment_index = segment_index
        self.stop_city = stop_city

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_name is not None:
            result['airline_name'] = self.airline_name

        if self.arr_apt is not None:
            result['arr_apt'] = self.arr_apt

        if self.arr_apt_code is not None:
            result['arr_apt_code'] = self.arr_apt_code

        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_terminal is not None:
            result['arr_terminal'] = self.arr_terminal

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.dep_apt is not None:
            result['dep_apt'] = self.dep_apt

        if self.dep_apt_code is not None:
            result['dep_apt_code'] = self.dep_apt_code

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_terminal is not None:
            result['dep_terminal'] = self.dep_terminal

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.flight_mile is not None:
            result['flight_mile'] = self.flight_mile

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.stop_city is not None:
            result['stop_city'] = self.stop_city

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('arr_apt') is not None:
            self.arr_apt = m.get('arr_apt')

        if m.get('arr_apt_code') is not None:
            self.arr_apt_code = m.get('arr_apt_code')

        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_terminal') is not None:
            self.arr_terminal = m.get('arr_terminal')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_apt') is not None:
            self.dep_apt = m.get('dep_apt')

        if m.get('dep_apt_code') is not None:
            self.dep_apt_code = m.get('dep_apt_code')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_terminal') is not None:
            self.dep_terminal = m.get('dep_terminal')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('flight_mile') is not None:
            self.flight_mile = m.get('flight_mile')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('stop_city') is not None:
            self.stop_city = m.get('stop_city')

        return self

class FlightOrderListQueryV2ResponseBodyModuleFlightReshopApplyList(DaraModel):
    def __init__(
        self,
        flight_reshop_apply_ticket_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleFlightReshopApplyListFlightReshopApplyTicketList] = None,
        flight_reshop_segment_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleFlightReshopApplyListFlightReshopSegmentList] = None,
        flight_reshop_user_fee_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleFlightReshopApplyListFlightReshopUserFeeList] = None,
        relate_reshop_apply_id: int = None,
        reshop_apply_id: int = None,
        reshop_approve_id: str = None,
        reshop_corp_total_amount: float = None,
        reshop_person_total_amount: float = None,
        reshop_reason: str = None,
        reshop_reason_code: str = None,
        reshop_total_amount: float = None,
        user_id_list: List[str] = None,
    ):
        self.flight_reshop_apply_ticket_list = flight_reshop_apply_ticket_list
        self.flight_reshop_segment_list = flight_reshop_segment_list
        self.flight_reshop_user_fee_list = flight_reshop_user_fee_list
        self.relate_reshop_apply_id = relate_reshop_apply_id
        self.reshop_apply_id = reshop_apply_id
        self.reshop_approve_id = reshop_approve_id
        self.reshop_corp_total_amount = reshop_corp_total_amount
        self.reshop_person_total_amount = reshop_person_total_amount
        self.reshop_reason = reshop_reason
        self.reshop_reason_code = reshop_reason_code
        self.reshop_total_amount = reshop_total_amount
        self.user_id_list = user_id_list

    def validate(self):
        if self.flight_reshop_apply_ticket_list:
            for v1 in self.flight_reshop_apply_ticket_list:
                 if v1:
                    v1.validate()
        if self.flight_reshop_segment_list:
            for v1 in self.flight_reshop_segment_list:
                 if v1:
                    v1.validate()
        if self.flight_reshop_user_fee_list:
            for v1 in self.flight_reshop_user_fee_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['flight_reshop_apply_ticket_list'] = []
        if self.flight_reshop_apply_ticket_list is not None:
            for k1 in self.flight_reshop_apply_ticket_list:
                result['flight_reshop_apply_ticket_list'].append(k1.to_map() if k1 else None)

        result['flight_reshop_segment_list'] = []
        if self.flight_reshop_segment_list is not None:
            for k1 in self.flight_reshop_segment_list:
                result['flight_reshop_segment_list'].append(k1.to_map() if k1 else None)

        result['flight_reshop_user_fee_list'] = []
        if self.flight_reshop_user_fee_list is not None:
            for k1 in self.flight_reshop_user_fee_list:
                result['flight_reshop_user_fee_list'].append(k1.to_map() if k1 else None)

        if self.relate_reshop_apply_id is not None:
            result['relate_reshop_apply_id'] = self.relate_reshop_apply_id

        if self.reshop_apply_id is not None:
            result['reshop_apply_id'] = self.reshop_apply_id

        if self.reshop_approve_id is not None:
            result['reshop_approve_id'] = self.reshop_approve_id

        if self.reshop_corp_total_amount is not None:
            result['reshop_corp_total_amount'] = self.reshop_corp_total_amount

        if self.reshop_person_total_amount is not None:
            result['reshop_person_total_amount'] = self.reshop_person_total_amount

        if self.reshop_reason is not None:
            result['reshop_reason'] = self.reshop_reason

        if self.reshop_reason_code is not None:
            result['reshop_reason_code'] = self.reshop_reason_code

        if self.reshop_total_amount is not None:
            result['reshop_total_amount'] = self.reshop_total_amount

        if self.user_id_list is not None:
            result['user_id_list'] = self.user_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_reshop_apply_ticket_list = []
        if m.get('flight_reshop_apply_ticket_list') is not None:
            for k1 in m.get('flight_reshop_apply_ticket_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleFlightReshopApplyListFlightReshopApplyTicketList()
                self.flight_reshop_apply_ticket_list.append(temp_model.from_map(k1))

        self.flight_reshop_segment_list = []
        if m.get('flight_reshop_segment_list') is not None:
            for k1 in m.get('flight_reshop_segment_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleFlightReshopApplyListFlightReshopSegmentList()
                self.flight_reshop_segment_list.append(temp_model.from_map(k1))

        self.flight_reshop_user_fee_list = []
        if m.get('flight_reshop_user_fee_list') is not None:
            for k1 in m.get('flight_reshop_user_fee_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleFlightReshopApplyListFlightReshopUserFeeList()
                self.flight_reshop_user_fee_list.append(temp_model.from_map(k1))

        if m.get('relate_reshop_apply_id') is not None:
            self.relate_reshop_apply_id = m.get('relate_reshop_apply_id')

        if m.get('reshop_apply_id') is not None:
            self.reshop_apply_id = m.get('reshop_apply_id')

        if m.get('reshop_approve_id') is not None:
            self.reshop_approve_id = m.get('reshop_approve_id')

        if m.get('reshop_corp_total_amount') is not None:
            self.reshop_corp_total_amount = m.get('reshop_corp_total_amount')

        if m.get('reshop_person_total_amount') is not None:
            self.reshop_person_total_amount = m.get('reshop_person_total_amount')

        if m.get('reshop_reason') is not None:
            self.reshop_reason = m.get('reshop_reason')

        if m.get('reshop_reason_code') is not None:
            self.reshop_reason_code = m.get('reshop_reason_code')

        if m.get('reshop_total_amount') is not None:
            self.reshop_total_amount = m.get('reshop_total_amount')

        if m.get('user_id_list') is not None:
            self.user_id_list = m.get('user_id_list')

        return self

class FlightOrderListQueryV2ResponseBodyModuleFlightReshopApplyListFlightReshopUserFeeList(DaraModel):
    def __init__(
        self,
        change_fee: float = None,
        reshop_corp_amount: float = None,
        reshop_person_amount: float = None,
        upgrade_fee: float = None,
        user_id: str = None,
    ):
        self.change_fee = change_fee
        self.reshop_corp_amount = reshop_corp_amount
        self.reshop_person_amount = reshop_person_amount
        self.upgrade_fee = upgrade_fee
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_fee is not None:
            result['change_fee'] = self.change_fee

        if self.reshop_corp_amount is not None:
            result['reshop_corp_amount'] = self.reshop_corp_amount

        if self.reshop_person_amount is not None:
            result['reshop_person_amount'] = self.reshop_person_amount

        if self.upgrade_fee is not None:
            result['upgrade_fee'] = self.upgrade_fee

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_fee') is not None:
            self.change_fee = m.get('change_fee')

        if m.get('reshop_corp_amount') is not None:
            self.reshop_corp_amount = m.get('reshop_corp_amount')

        if m.get('reshop_person_amount') is not None:
            self.reshop_person_amount = m.get('reshop_person_amount')

        if m.get('upgrade_fee') is not None:
            self.upgrade_fee = m.get('upgrade_fee')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class FlightOrderListQueryV2ResponseBodyModuleFlightReshopApplyListFlightReshopSegmentList(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        arr_apt: str = None,
        arr_apt_code: str = None,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_terminal: str = None,
        arr_time: str = None,
        dep_apt: str = None,
        dep_apt_code: str = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_terminal: str = None,
        dep_time: str = None,
        flight_mile: int = None,
        flight_no: str = None,
        journey_index: int = None,
        segment_index: int = None,
        stop_city: List[str] = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.arr_apt = arr_apt
        self.arr_apt_code = arr_apt_code
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.arr_terminal = arr_terminal
        self.arr_time = arr_time
        self.dep_apt = dep_apt
        self.dep_apt_code = dep_apt_code
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.dep_terminal = dep_terminal
        self.dep_time = dep_time
        self.flight_mile = flight_mile
        self.flight_no = flight_no
        self.journey_index = journey_index
        self.segment_index = segment_index
        self.stop_city = stop_city

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_name is not None:
            result['airline_name'] = self.airline_name

        if self.arr_apt is not None:
            result['arr_apt'] = self.arr_apt

        if self.arr_apt_code is not None:
            result['arr_apt_code'] = self.arr_apt_code

        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_terminal is not None:
            result['arr_terminal'] = self.arr_terminal

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.dep_apt is not None:
            result['dep_apt'] = self.dep_apt

        if self.dep_apt_code is not None:
            result['dep_apt_code'] = self.dep_apt_code

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_terminal is not None:
            result['dep_terminal'] = self.dep_terminal

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.flight_mile is not None:
            result['flight_mile'] = self.flight_mile

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.stop_city is not None:
            result['stop_city'] = self.stop_city

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('arr_apt') is not None:
            self.arr_apt = m.get('arr_apt')

        if m.get('arr_apt_code') is not None:
            self.arr_apt_code = m.get('arr_apt_code')

        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_terminal') is not None:
            self.arr_terminal = m.get('arr_terminal')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_apt') is not None:
            self.dep_apt = m.get('dep_apt')

        if m.get('dep_apt_code') is not None:
            self.dep_apt_code = m.get('dep_apt_code')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_terminal') is not None:
            self.dep_terminal = m.get('dep_terminal')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('flight_mile') is not None:
            self.flight_mile = m.get('flight_mile')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('stop_city') is not None:
            self.stop_city = m.get('stop_city')

        return self

class FlightOrderListQueryV2ResponseBodyModuleFlightReshopApplyListFlightReshopApplyTicketList(DaraModel):
    def __init__(
        self,
        flight_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleFlightReshopApplyListFlightReshopApplyTicketListFlightList] = None,
        relate_ticket_no_list: List[str] = None,
        ticket_no_list: List[str] = None,
        user_id: str = None,
    ):
        self.flight_list = flight_list
        self.relate_ticket_no_list = relate_ticket_no_list
        self.ticket_no_list = ticket_no_list
        self.user_id = user_id

    def validate(self):
        if self.flight_list:
            for v1 in self.flight_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['flight_list'] = []
        if self.flight_list is not None:
            for k1 in self.flight_list:
                result['flight_list'].append(k1.to_map() if k1 else None)

        if self.relate_ticket_no_list is not None:
            result['relate_ticket_no_list'] = self.relate_ticket_no_list

        if self.ticket_no_list is not None:
            result['ticket_no_list'] = self.ticket_no_list

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_list = []
        if m.get('flight_list') is not None:
            for k1 in m.get('flight_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleFlightReshopApplyListFlightReshopApplyTicketListFlightList()
                self.flight_list.append(temp_model.from_map(k1))

        if m.get('relate_ticket_no_list') is not None:
            self.relate_ticket_no_list = m.get('relate_ticket_no_list')

        if m.get('ticket_no_list') is not None:
            self.ticket_no_list = m.get('ticket_no_list')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class FlightOrderListQueryV2ResponseBodyModuleFlightReshopApplyListFlightReshopApplyTicketListFlightList(DaraModel):
    def __init__(
        self,
        arr_time: str = None,
        cabin: str = None,
        cabin_class: str = None,
        cabin_class_name: str = None,
        dep_time: str = None,
        flight_no: str = None,
    ):
        self.arr_time = arr_time
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.cabin_class_name = cabin_class_name
        self.dep_time = dep_time
        self.flight_no = flight_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.cabin_class_name is not None:
            result['cabin_class_name'] = self.cabin_class_name

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('cabin_class_name') is not None:
            self.cabin_class_name = m.get('cabin_class_name')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        return self

class FlightOrderListQueryV2ResponseBodyModuleFlightRefundApplyList(DaraModel):
    def __init__(
        self,
        flight_refund_apply_ticket_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleFlightRefundApplyListFlightRefundApplyTicketList] = None,
        flight_refund_segment_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleFlightRefundApplyListFlightRefundSegmentList] = None,
        flight_refund_user_fee_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleFlightRefundApplyListFlightRefundUserFeeList] = None,
        refund_apply_id: str = None,
        refund_approve_id: str = None,
        refund_corp_total_amount: float = None,
        refund_hand_fee: float = None,
        refund_person_total_amount: float = None,
        refund_reason: str = None,
        refund_reason_code: str = None,
        refund_total_amount: float = None,
        relate_refund_apply_id: str = None,
        user_id_list: List[str] = None,
    ):
        self.flight_refund_apply_ticket_list = flight_refund_apply_ticket_list
        self.flight_refund_segment_list = flight_refund_segment_list
        self.flight_refund_user_fee_list = flight_refund_user_fee_list
        self.refund_apply_id = refund_apply_id
        self.refund_approve_id = refund_approve_id
        self.refund_corp_total_amount = refund_corp_total_amount
        self.refund_hand_fee = refund_hand_fee
        self.refund_person_total_amount = refund_person_total_amount
        self.refund_reason = refund_reason
        self.refund_reason_code = refund_reason_code
        self.refund_total_amount = refund_total_amount
        self.relate_refund_apply_id = relate_refund_apply_id
        self.user_id_list = user_id_list

    def validate(self):
        if self.flight_refund_apply_ticket_list:
            for v1 in self.flight_refund_apply_ticket_list:
                 if v1:
                    v1.validate()
        if self.flight_refund_segment_list:
            for v1 in self.flight_refund_segment_list:
                 if v1:
                    v1.validate()
        if self.flight_refund_user_fee_list:
            for v1 in self.flight_refund_user_fee_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['flight_refund_apply_ticket_list'] = []
        if self.flight_refund_apply_ticket_list is not None:
            for k1 in self.flight_refund_apply_ticket_list:
                result['flight_refund_apply_ticket_list'].append(k1.to_map() if k1 else None)

        result['flight_refund_segment_list'] = []
        if self.flight_refund_segment_list is not None:
            for k1 in self.flight_refund_segment_list:
                result['flight_refund_segment_list'].append(k1.to_map() if k1 else None)

        result['flight_refund_user_fee_list'] = []
        if self.flight_refund_user_fee_list is not None:
            for k1 in self.flight_refund_user_fee_list:
                result['flight_refund_user_fee_list'].append(k1.to_map() if k1 else None)

        if self.refund_apply_id is not None:
            result['refund_apply_id'] = self.refund_apply_id

        if self.refund_approve_id is not None:
            result['refund_approve_id'] = self.refund_approve_id

        if self.refund_corp_total_amount is not None:
            result['refund_corp_total_amount'] = self.refund_corp_total_amount

        if self.refund_hand_fee is not None:
            result['refund_hand_fee'] = self.refund_hand_fee

        if self.refund_person_total_amount is not None:
            result['refund_person_total_amount'] = self.refund_person_total_amount

        if self.refund_reason is not None:
            result['refund_reason'] = self.refund_reason

        if self.refund_reason_code is not None:
            result['refund_reason_code'] = self.refund_reason_code

        if self.refund_total_amount is not None:
            result['refund_total_amount'] = self.refund_total_amount

        if self.relate_refund_apply_id is not None:
            result['relate_refund_apply_id'] = self.relate_refund_apply_id

        if self.user_id_list is not None:
            result['user_id_list'] = self.user_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_refund_apply_ticket_list = []
        if m.get('flight_refund_apply_ticket_list') is not None:
            for k1 in m.get('flight_refund_apply_ticket_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleFlightRefundApplyListFlightRefundApplyTicketList()
                self.flight_refund_apply_ticket_list.append(temp_model.from_map(k1))

        self.flight_refund_segment_list = []
        if m.get('flight_refund_segment_list') is not None:
            for k1 in m.get('flight_refund_segment_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleFlightRefundApplyListFlightRefundSegmentList()
                self.flight_refund_segment_list.append(temp_model.from_map(k1))

        self.flight_refund_user_fee_list = []
        if m.get('flight_refund_user_fee_list') is not None:
            for k1 in m.get('flight_refund_user_fee_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleFlightRefundApplyListFlightRefundUserFeeList()
                self.flight_refund_user_fee_list.append(temp_model.from_map(k1))

        if m.get('refund_apply_id') is not None:
            self.refund_apply_id = m.get('refund_apply_id')

        if m.get('refund_approve_id') is not None:
            self.refund_approve_id = m.get('refund_approve_id')

        if m.get('refund_corp_total_amount') is not None:
            self.refund_corp_total_amount = m.get('refund_corp_total_amount')

        if m.get('refund_hand_fee') is not None:
            self.refund_hand_fee = m.get('refund_hand_fee')

        if m.get('refund_person_total_amount') is not None:
            self.refund_person_total_amount = m.get('refund_person_total_amount')

        if m.get('refund_reason') is not None:
            self.refund_reason = m.get('refund_reason')

        if m.get('refund_reason_code') is not None:
            self.refund_reason_code = m.get('refund_reason_code')

        if m.get('refund_total_amount') is not None:
            self.refund_total_amount = m.get('refund_total_amount')

        if m.get('relate_refund_apply_id') is not None:
            self.relate_refund_apply_id = m.get('relate_refund_apply_id')

        if m.get('user_id_list') is not None:
            self.user_id_list = m.get('user_id_list')

        return self

class FlightOrderListQueryV2ResponseBodyModuleFlightRefundApplyListFlightRefundUserFeeList(DaraModel):
    def __init__(
        self,
        already_use_amount: float = None,
        non_refundable_reshop_change_amount: float = None,
        non_refundable_reshop_upgrade_amount: float = None,
        refund_amount: float = None,
        refund_corp_amount: float = None,
        refund_hand_fee: float = None,
        refund_person_amount: float = None,
        user_id: str = None,
    ):
        self.already_use_amount = already_use_amount
        self.non_refundable_reshop_change_amount = non_refundable_reshop_change_amount
        self.non_refundable_reshop_upgrade_amount = non_refundable_reshop_upgrade_amount
        self.refund_amount = refund_amount
        self.refund_corp_amount = refund_corp_amount
        self.refund_hand_fee = refund_hand_fee
        self.refund_person_amount = refund_person_amount
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.already_use_amount is not None:
            result['already_use_amount'] = self.already_use_amount

        if self.non_refundable_reshop_change_amount is not None:
            result['non_refundable_reshop_change_amount'] = self.non_refundable_reshop_change_amount

        if self.non_refundable_reshop_upgrade_amount is not None:
            result['non_refundable_reshop_upgrade_amount'] = self.non_refundable_reshop_upgrade_amount

        if self.refund_amount is not None:
            result['refund_amount'] = self.refund_amount

        if self.refund_corp_amount is not None:
            result['refund_corp_amount'] = self.refund_corp_amount

        if self.refund_hand_fee is not None:
            result['refund_hand_fee'] = self.refund_hand_fee

        if self.refund_person_amount is not None:
            result['refund_person_amount'] = self.refund_person_amount

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('already_use_amount') is not None:
            self.already_use_amount = m.get('already_use_amount')

        if m.get('non_refundable_reshop_change_amount') is not None:
            self.non_refundable_reshop_change_amount = m.get('non_refundable_reshop_change_amount')

        if m.get('non_refundable_reshop_upgrade_amount') is not None:
            self.non_refundable_reshop_upgrade_amount = m.get('non_refundable_reshop_upgrade_amount')

        if m.get('refund_amount') is not None:
            self.refund_amount = m.get('refund_amount')

        if m.get('refund_corp_amount') is not None:
            self.refund_corp_amount = m.get('refund_corp_amount')

        if m.get('refund_hand_fee') is not None:
            self.refund_hand_fee = m.get('refund_hand_fee')

        if m.get('refund_person_amount') is not None:
            self.refund_person_amount = m.get('refund_person_amount')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class FlightOrderListQueryV2ResponseBodyModuleFlightRefundApplyListFlightRefundSegmentList(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        arr_apt: str = None,
        arr_apt_code: str = None,
        arr_city: str = None,
        arr_city_code: str = None,
        arr_terminal: str = None,
        arr_time: str = None,
        dep_apt: str = None,
        dep_apt_code: str = None,
        dep_city: str = None,
        dep_city_code: str = None,
        dep_terminal: str = None,
        dep_time: str = None,
        flight_mile: int = None,
        flight_no: str = None,
        journey_index: int = None,
        segment_index: int = None,
        stop_city: List[str] = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.arr_apt = arr_apt
        self.arr_apt_code = arr_apt_code
        self.arr_city = arr_city
        self.arr_city_code = arr_city_code
        self.arr_terminal = arr_terminal
        self.arr_time = arr_time
        self.dep_apt = dep_apt
        self.dep_apt_code = dep_apt_code
        self.dep_city = dep_city
        self.dep_city_code = dep_city_code
        self.dep_terminal = dep_terminal
        self.dep_time = dep_time
        self.flight_mile = flight_mile
        self.flight_no = flight_no
        self.journey_index = journey_index
        self.segment_index = segment_index
        self.stop_city = stop_city

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_name is not None:
            result['airline_name'] = self.airline_name

        if self.arr_apt is not None:
            result['arr_apt'] = self.arr_apt

        if self.arr_apt_code is not None:
            result['arr_apt_code'] = self.arr_apt_code

        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_terminal is not None:
            result['arr_terminal'] = self.arr_terminal

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.dep_apt is not None:
            result['dep_apt'] = self.dep_apt

        if self.dep_apt_code is not None:
            result['dep_apt_code'] = self.dep_apt_code

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_terminal is not None:
            result['dep_terminal'] = self.dep_terminal

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.flight_mile is not None:
            result['flight_mile'] = self.flight_mile

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.stop_city is not None:
            result['stop_city'] = self.stop_city

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('arr_apt') is not None:
            self.arr_apt = m.get('arr_apt')

        if m.get('arr_apt_code') is not None:
            self.arr_apt_code = m.get('arr_apt_code')

        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_terminal') is not None:
            self.arr_terminal = m.get('arr_terminal')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_apt') is not None:
            self.dep_apt = m.get('dep_apt')

        if m.get('dep_apt_code') is not None:
            self.dep_apt_code = m.get('dep_apt_code')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_terminal') is not None:
            self.dep_terminal = m.get('dep_terminal')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('flight_mile') is not None:
            self.flight_mile = m.get('flight_mile')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('stop_city') is not None:
            self.stop_city = m.get('stop_city')

        return self

class FlightOrderListQueryV2ResponseBodyModuleFlightRefundApplyListFlightRefundApplyTicketList(DaraModel):
    def __init__(
        self,
        flight_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleFlightRefundApplyListFlightRefundApplyTicketListFlightList] = None,
        ticket_no_list: List[str] = None,
        user_id: str = None,
    ):
        self.flight_list = flight_list
        self.ticket_no_list = ticket_no_list
        self.user_id = user_id

    def validate(self):
        if self.flight_list:
            for v1 in self.flight_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['flight_list'] = []
        if self.flight_list is not None:
            for k1 in self.flight_list:
                result['flight_list'].append(k1.to_map() if k1 else None)

        if self.ticket_no_list is not None:
            result['ticket_no_list'] = self.ticket_no_list

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_list = []
        if m.get('flight_list') is not None:
            for k1 in m.get('flight_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleFlightRefundApplyListFlightRefundApplyTicketListFlightList()
                self.flight_list.append(temp_model.from_map(k1))

        if m.get('ticket_no_list') is not None:
            self.ticket_no_list = m.get('ticket_no_list')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class FlightOrderListQueryV2ResponseBodyModuleFlightRefundApplyListFlightRefundApplyTicketListFlightList(DaraModel):
    def __init__(
        self,
        arr_time: str = None,
        cabin: str = None,
        cabin_class: str = None,
        cabin_class_name: str = None,
        dep_time: str = None,
        flight_no: str = None,
    ):
        self.arr_time = arr_time
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.cabin_class_name = cabin_class_name
        self.dep_time = dep_time
        self.flight_no = flight_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.cabin_class_name is not None:
            result['cabin_class_name'] = self.cabin_class_name

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('cabin_class_name') is not None:
            self.cabin_class_name = m.get('cabin_class_name')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        return self

class FlightOrderListQueryV2ResponseBodyModuleFlightOrderUserFeeList(DaraModel):
    def __init__(
        self,
        build_fee: float = None,
        corp_pay_amount: float = None,
        oil_fee: float = None,
        person_pay_amount: float = None,
        ticket_price: float = None,
        user_id: str = None,
    ):
        self.build_fee = build_fee
        self.corp_pay_amount = corp_pay_amount
        self.oil_fee = oil_fee
        self.person_pay_amount = person_pay_amount
        self.ticket_price = ticket_price
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_fee is not None:
            result['build_fee'] = self.build_fee

        if self.corp_pay_amount is not None:
            result['corp_pay_amount'] = self.corp_pay_amount

        if self.oil_fee is not None:
            result['oil_fee'] = self.oil_fee

        if self.person_pay_amount is not None:
            result['person_pay_amount'] = self.person_pay_amount

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('build_fee') is not None:
            self.build_fee = m.get('build_fee')

        if m.get('corp_pay_amount') is not None:
            self.corp_pay_amount = m.get('corp_pay_amount')

        if m.get('oil_fee') is not None:
            self.oil_fee = m.get('oil_fee')

        if m.get('person_pay_amount') is not None:
            self.person_pay_amount = m.get('person_pay_amount')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class FlightOrderListQueryV2ResponseBodyModuleFlightOrderTicketList(DaraModel):
    def __init__(
        self,
        flight_list: List[main_models.FlightOrderListQueryV2ResponseBodyModuleFlightOrderTicketListFlightList] = None,
        ticket_no_list: List[str] = None,
        user_id: str = None,
    ):
        self.flight_list = flight_list
        self.ticket_no_list = ticket_no_list
        self.user_id = user_id

    def validate(self):
        if self.flight_list:
            for v1 in self.flight_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['flight_list'] = []
        if self.flight_list is not None:
            for k1 in self.flight_list:
                result['flight_list'].append(k1.to_map() if k1 else None)

        if self.ticket_no_list is not None:
            result['ticket_no_list'] = self.ticket_no_list

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_list = []
        if m.get('flight_list') is not None:
            for k1 in m.get('flight_list'):
                temp_model = main_models.FlightOrderListQueryV2ResponseBodyModuleFlightOrderTicketListFlightList()
                self.flight_list.append(temp_model.from_map(k1))

        if m.get('ticket_no_list') is not None:
            self.ticket_no_list = m.get('ticket_no_list')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class FlightOrderListQueryV2ResponseBodyModuleFlightOrderTicketListFlightList(DaraModel):
    def __init__(
        self,
        arr_time: str = None,
        cabin: str = None,
        cabin_class: str = None,
        cabin_class_name: str = None,
        dep_time: str = None,
        flight_no: str = None,
    ):
        self.arr_time = arr_time
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.cabin_class_name = cabin_class_name
        self.dep_time = dep_time
        self.flight_no = flight_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.cabin_class_name is not None:
            result['cabin_class_name'] = self.cabin_class_name

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('cabin_class_name') is not None:
            self.cabin_class_name = m.get('cabin_class_name')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        return self

class FlightOrderListQueryV2ResponseBodyModuleApprove(DaraModel):
    def __init__(
        self,
        approve_id: int = None,
        btrip_title: str = None,
        exceed_approve_id: str = None,
        thirdpart_approve_id: str = None,
        thirdpart_exceed_approve_id: str = None,
    ):
        self.approve_id = approve_id
        self.btrip_title = btrip_title
        self.exceed_approve_id = exceed_approve_id
        self.thirdpart_approve_id = thirdpart_approve_id
        self.thirdpart_exceed_approve_id = thirdpart_exceed_approve_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approve_id is not None:
            result['approve_id'] = self.approve_id

        if self.btrip_title is not None:
            result['btrip_title'] = self.btrip_title

        if self.exceed_approve_id is not None:
            result['exceed_approve_id'] = self.exceed_approve_id

        if self.thirdpart_approve_id is not None:
            result['thirdpart_approve_id'] = self.thirdpart_approve_id

        if self.thirdpart_exceed_approve_id is not None:
            result['thirdpart_exceed_approve_id'] = self.thirdpart_exceed_approve_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('approve_id') is not None:
            self.approve_id = m.get('approve_id')

        if m.get('btrip_title') is not None:
            self.btrip_title = m.get('btrip_title')

        if m.get('exceed_approve_id') is not None:
            self.exceed_approve_id = m.get('exceed_approve_id')

        if m.get('thirdpart_approve_id') is not None:
            self.thirdpart_approve_id = m.get('thirdpart_approve_id')

        if m.get('thirdpart_exceed_approve_id') is not None:
            self.thirdpart_exceed_approve_id = m.get('thirdpart_exceed_approve_id')

        return self

