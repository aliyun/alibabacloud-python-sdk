# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IntlFlightReShopDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.IntlFlightReShopDetailResponseBodyModule = None,
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
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class IntlFlightReShopDetailResponseBodyModule(DaraModel):
    def __init__(
        self,
        baggage_rule: main_models.IntlFlightReShopDetailResponseBodyModuleBaggageRule = None,
        close_reason: str = None,
        close_time: str = None,
        close_type: int = None,
        journey_list: List[main_models.IntlFlightReShopDetailResponseBodyModuleJourneyList] = None,
        order_id: int = None,
        origin_journey_list: List[main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyList] = None,
        out_order_id: str = None,
        out_re_shop_apply_id: str = None,
        passenger_list: List[main_models.IntlFlightReShopDetailResponseBodyModulePassengerList] = None,
        passenger_price_info_list: List[main_models.IntlFlightReShopDetailResponseBodyModulePassengerPriceInfoList] = None,
        passenger_ticket_list: List[main_models.IntlFlightReShopDetailResponseBodyModulePassengerTicketList] = None,
        pay_latest_time: str = None,
        pay_status: int = None,
        price_info: main_models.IntlFlightReShopDetailResponseBodyModulePriceInfo = None,
        re_shop_apply_id: int = None,
        re_shop_reason_code: str = None,
        re_shop_reason_desc: str = None,
        refund_change_rule: main_models.IntlFlightReShopDetailResponseBodyModuleRefundChangeRule = None,
        status: int = None,
        success_time: str = None,
        user_intention_memo: str = None,
    ):
        self.baggage_rule = baggage_rule
        self.close_reason = close_reason
        self.close_time = close_time
        self.close_type = close_type
        self.journey_list = journey_list
        self.order_id = order_id
        self.origin_journey_list = origin_journey_list
        self.out_order_id = out_order_id
        self.out_re_shop_apply_id = out_re_shop_apply_id
        self.passenger_list = passenger_list
        self.passenger_price_info_list = passenger_price_info_list
        self.passenger_ticket_list = passenger_ticket_list
        self.pay_latest_time = pay_latest_time
        self.pay_status = pay_status
        self.price_info = price_info
        self.re_shop_apply_id = re_shop_apply_id
        self.re_shop_reason_code = re_shop_reason_code
        self.re_shop_reason_desc = re_shop_reason_desc
        self.refund_change_rule = refund_change_rule
        self.status = status
        self.success_time = success_time
        self.user_intention_memo = user_intention_memo

    def validate(self):
        if self.baggage_rule:
            self.baggage_rule.validate()
        if self.journey_list:
            for v1 in self.journey_list:
                 if v1:
                    v1.validate()
        if self.origin_journey_list:
            for v1 in self.origin_journey_list:
                 if v1:
                    v1.validate()
        if self.passenger_list:
            for v1 in self.passenger_list:
                 if v1:
                    v1.validate()
        if self.passenger_price_info_list:
            for v1 in self.passenger_price_info_list:
                 if v1:
                    v1.validate()
        if self.passenger_ticket_list:
            for v1 in self.passenger_ticket_list:
                 if v1:
                    v1.validate()
        if self.price_info:
            self.price_info.validate()
        if self.refund_change_rule:
            self.refund_change_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baggage_rule is not None:
            result['baggage_rule'] = self.baggage_rule.to_map()

        if self.close_reason is not None:
            result['close_reason'] = self.close_reason

        if self.close_time is not None:
            result['close_time'] = self.close_time

        if self.close_type is not None:
            result['close_type'] = self.close_type

        result['journey_list'] = []
        if self.journey_list is not None:
            for k1 in self.journey_list:
                result['journey_list'].append(k1.to_map() if k1 else None)

        if self.order_id is not None:
            result['order_id'] = self.order_id

        result['origin_journey_list'] = []
        if self.origin_journey_list is not None:
            for k1 in self.origin_journey_list:
                result['origin_journey_list'].append(k1.to_map() if k1 else None)

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.out_re_shop_apply_id is not None:
            result['out_re_shop_apply_id'] = self.out_re_shop_apply_id

        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k1 in self.passenger_list:
                result['passenger_list'].append(k1.to_map() if k1 else None)

        result['passenger_price_info_list'] = []
        if self.passenger_price_info_list is not None:
            for k1 in self.passenger_price_info_list:
                result['passenger_price_info_list'].append(k1.to_map() if k1 else None)

        result['passenger_ticket_list'] = []
        if self.passenger_ticket_list is not None:
            for k1 in self.passenger_ticket_list:
                result['passenger_ticket_list'].append(k1.to_map() if k1 else None)

        if self.pay_latest_time is not None:
            result['pay_latest_time'] = self.pay_latest_time

        if self.pay_status is not None:
            result['pay_status'] = self.pay_status

        if self.price_info is not None:
            result['price_info'] = self.price_info.to_map()

        if self.re_shop_apply_id is not None:
            result['re_shop_apply_id'] = self.re_shop_apply_id

        if self.re_shop_reason_code is not None:
            result['re_shop_reason_code'] = self.re_shop_reason_code

        if self.re_shop_reason_desc is not None:
            result['re_shop_reason_desc'] = self.re_shop_reason_desc

        if self.refund_change_rule is not None:
            result['refund_change_rule'] = self.refund_change_rule.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.success_time is not None:
            result['success_time'] = self.success_time

        if self.user_intention_memo is not None:
            result['user_intention_memo'] = self.user_intention_memo

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baggage_rule') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleBaggageRule()
            self.baggage_rule = temp_model.from_map(m.get('baggage_rule'))

        if m.get('close_reason') is not None:
            self.close_reason = m.get('close_reason')

        if m.get('close_time') is not None:
            self.close_time = m.get('close_time')

        if m.get('close_type') is not None:
            self.close_type = m.get('close_type')

        self.journey_list = []
        if m.get('journey_list') is not None:
            for k1 in m.get('journey_list'):
                temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleJourneyList()
                self.journey_list.append(temp_model.from_map(k1))

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        self.origin_journey_list = []
        if m.get('origin_journey_list') is not None:
            for k1 in m.get('origin_journey_list'):
                temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyList()
                self.origin_journey_list.append(temp_model.from_map(k1))

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('out_re_shop_apply_id') is not None:
            self.out_re_shop_apply_id = m.get('out_re_shop_apply_id')

        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k1 in m.get('passenger_list'):
                temp_model = main_models.IntlFlightReShopDetailResponseBodyModulePassengerList()
                self.passenger_list.append(temp_model.from_map(k1))

        self.passenger_price_info_list = []
        if m.get('passenger_price_info_list') is not None:
            for k1 in m.get('passenger_price_info_list'):
                temp_model = main_models.IntlFlightReShopDetailResponseBodyModulePassengerPriceInfoList()
                self.passenger_price_info_list.append(temp_model.from_map(k1))

        self.passenger_ticket_list = []
        if m.get('passenger_ticket_list') is not None:
            for k1 in m.get('passenger_ticket_list'):
                temp_model = main_models.IntlFlightReShopDetailResponseBodyModulePassengerTicketList()
                self.passenger_ticket_list.append(temp_model.from_map(k1))

        if m.get('pay_latest_time') is not None:
            self.pay_latest_time = m.get('pay_latest_time')

        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')

        if m.get('price_info') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModulePriceInfo()
            self.price_info = temp_model.from_map(m.get('price_info'))

        if m.get('re_shop_apply_id') is not None:
            self.re_shop_apply_id = m.get('re_shop_apply_id')

        if m.get('re_shop_reason_code') is not None:
            self.re_shop_reason_code = m.get('re_shop_reason_code')

        if m.get('re_shop_reason_desc') is not None:
            self.re_shop_reason_desc = m.get('re_shop_reason_desc')

        if m.get('refund_change_rule') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleRefundChangeRule()
            self.refund_change_rule = temp_model.from_map(m.get('refund_change_rule'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('success_time') is not None:
            self.success_time = m.get('success_time')

        if m.get('user_intention_memo') is not None:
            self.user_intention_memo = m.get('user_intention_memo')

        return self

class IntlFlightReShopDetailResponseBodyModuleRefundChangeRule(DaraModel):
    def __init__(
        self,
        refund_change_rule_desc: str = None,
    ):
        self.refund_change_rule_desc = refund_change_rule_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.refund_change_rule_desc is not None:
            result['refund_change_rule_desc'] = self.refund_change_rule_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('refund_change_rule_desc') is not None:
            self.refund_change_rule_desc = m.get('refund_change_rule_desc')

        return self

class IntlFlightReShopDetailResponseBodyModulePriceInfo(DaraModel):
    def __init__(
        self,
        handling_amount: int = None,
        tax_diff_amount: int = None,
        total_amount: int = None,
        upgrade_amount: int = None,
    ):
        self.handling_amount = handling_amount
        self.tax_diff_amount = tax_diff_amount
        self.total_amount = total_amount
        self.upgrade_amount = upgrade_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.handling_amount is not None:
            result['handling_amount'] = self.handling_amount

        if self.tax_diff_amount is not None:
            result['tax_diff_amount'] = self.tax_diff_amount

        if self.total_amount is not None:
            result['total_amount'] = self.total_amount

        if self.upgrade_amount is not None:
            result['upgrade_amount'] = self.upgrade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('handling_amount') is not None:
            self.handling_amount = m.get('handling_amount')

        if m.get('tax_diff_amount') is not None:
            self.tax_diff_amount = m.get('tax_diff_amount')

        if m.get('total_amount') is not None:
            self.total_amount = m.get('total_amount')

        if m.get('upgrade_amount') is not None:
            self.upgrade_amount = m.get('upgrade_amount')

        return self

class IntlFlightReShopDetailResponseBodyModulePassengerTicketList(DaraModel):
    def __init__(
        self,
        passenger_id: int = None,
        ticket_list: List[main_models.IntlFlightReShopDetailResponseBodyModulePassengerTicketListTicketList] = None,
    ):
        self.passenger_id = passenger_id
        self.ticket_list = ticket_list

    def validate(self):
        if self.ticket_list:
            for v1 in self.ticket_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        result['ticket_list'] = []
        if self.ticket_list is not None:
            for k1 in self.ticket_list:
                result['ticket_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        self.ticket_list = []
        if m.get('ticket_list') is not None:
            for k1 in m.get('ticket_list'):
                temp_model = main_models.IntlFlightReShopDetailResponseBodyModulePassengerTicketListTicketList()
                self.ticket_list.append(temp_model.from_map(k1))

        return self

class IntlFlightReShopDetailResponseBodyModulePassengerTicketListTicketList(DaraModel):
    def __init__(
        self,
        issue_time: str = None,
        pnr_no: str = None,
        segment_key_list: List[str] = None,
        ticket_no: str = None,
        ticket_segment_list: List[main_models.IntlFlightReShopDetailResponseBodyModulePassengerTicketListTicketListTicketSegmentList] = None,
    ):
        self.issue_time = issue_time
        self.pnr_no = pnr_no
        self.segment_key_list = segment_key_list
        self.ticket_no = ticket_no
        self.ticket_segment_list = ticket_segment_list

    def validate(self):
        if self.ticket_segment_list:
            for v1 in self.ticket_segment_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.issue_time is not None:
            result['issue_time'] = self.issue_time

        if self.pnr_no is not None:
            result['pnr_no'] = self.pnr_no

        if self.segment_key_list is not None:
            result['segment_key_list'] = self.segment_key_list

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        result['ticket_segment_list'] = []
        if self.ticket_segment_list is not None:
            for k1 in self.ticket_segment_list:
                result['ticket_segment_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('issue_time') is not None:
            self.issue_time = m.get('issue_time')

        if m.get('pnr_no') is not None:
            self.pnr_no = m.get('pnr_no')

        if m.get('segment_key_list') is not None:
            self.segment_key_list = m.get('segment_key_list')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        self.ticket_segment_list = []
        if m.get('ticket_segment_list') is not None:
            for k1 in m.get('ticket_segment_list'):
                temp_model = main_models.IntlFlightReShopDetailResponseBodyModulePassengerTicketListTicketListTicketSegmentList()
                self.ticket_segment_list.append(temp_model.from_map(k1))

        return self

class IntlFlightReShopDetailResponseBodyModulePassengerTicketListTicketListTicketSegmentList(DaraModel):
    def __init__(
        self,
        cabin: str = None,
        cabin_class: str = None,
        modified: bool = None,
        open_ticket_status: str = None,
        refunded: bool = None,
        segment_key: str = None,
    ):
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.modified = modified
        self.open_ticket_status = open_ticket_status
        self.refunded = refunded
        self.segment_key = segment_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.modified is not None:
            result['modified'] = self.modified

        if self.open_ticket_status is not None:
            result['open_ticket_status'] = self.open_ticket_status

        if self.refunded is not None:
            result['refunded'] = self.refunded

        if self.segment_key is not None:
            result['segment_key'] = self.segment_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('modified') is not None:
            self.modified = m.get('modified')

        if m.get('open_ticket_status') is not None:
            self.open_ticket_status = m.get('open_ticket_status')

        if m.get('refunded') is not None:
            self.refunded = m.get('refunded')

        if m.get('segment_key') is not None:
            self.segment_key = m.get('segment_key')

        return self

class IntlFlightReShopDetailResponseBodyModulePassengerPriceInfoList(DaraModel):
    def __init__(
        self,
        passenger_id: int = None,
        price_info: main_models.IntlFlightReShopDetailResponseBodyModulePassengerPriceInfoListPriceInfo = None,
    ):
        self.passenger_id = passenger_id
        self.price_info = price_info

    def validate(self):
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.price_info is not None:
            result['price_info'] = self.price_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('price_info') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModulePassengerPriceInfoListPriceInfo()
            self.price_info = temp_model.from_map(m.get('price_info'))

        return self

class IntlFlightReShopDetailResponseBodyModulePassengerPriceInfoListPriceInfo(DaraModel):
    def __init__(
        self,
        handling_amount: int = None,
        tax_diff_amount: int = None,
        total_amount: int = None,
        upgrade_amount: int = None,
    ):
        self.handling_amount = handling_amount
        self.tax_diff_amount = tax_diff_amount
        self.total_amount = total_amount
        self.upgrade_amount = upgrade_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.handling_amount is not None:
            result['handling_amount'] = self.handling_amount

        if self.tax_diff_amount is not None:
            result['tax_diff_amount'] = self.tax_diff_amount

        if self.total_amount is not None:
            result['total_amount'] = self.total_amount

        if self.upgrade_amount is not None:
            result['upgrade_amount'] = self.upgrade_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('handling_amount') is not None:
            self.handling_amount = m.get('handling_amount')

        if m.get('tax_diff_amount') is not None:
            self.tax_diff_amount = m.get('tax_diff_amount')

        if m.get('total_amount') is not None:
            self.total_amount = m.get('total_amount')

        if m.get('upgrade_amount') is not None:
            self.upgrade_amount = m.get('upgrade_amount')

        return self

class IntlFlightReShopDetailResponseBodyModulePassengerList(DaraModel):
    def __init__(
        self,
        full_name: str = None,
        gender: int = None,
        job_no: str = None,
        nationality: str = None,
        nationality_code: str = None,
        passenger_id: int = None,
        type: int = None,
        user_id: str = None,
        user_type: int = None,
    ):
        self.full_name = full_name
        self.gender = gender
        self.job_no = job_no
        self.nationality = nationality
        self.nationality_code = nationality_code
        self.passenger_id = passenger_id
        self.type = type
        self.user_id = user_id
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.full_name is not None:
            result['full_name'] = self.full_name

        if self.gender is not None:
            result['gender'] = self.gender

        if self.job_no is not None:
            result['job_no'] = self.job_no

        if self.nationality is not None:
            result['nationality'] = self.nationality

        if self.nationality_code is not None:
            result['nationality_code'] = self.nationality_code

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.type is not None:
            result['type'] = self.type

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_type is not None:
            result['user_type'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('full_name') is not None:
            self.full_name = m.get('full_name')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('job_no') is not None:
            self.job_no = m.get('job_no')

        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')

        if m.get('nationality_code') is not None:
            self.nationality_code = m.get('nationality_code')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')

        return self

class IntlFlightReShopDetailResponseBodyModuleOriginJourneyList(DaraModel):
    def __init__(
        self,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        duration: int = None,
        flight_segment_infos: List[main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfos] = None,
        journey_index: int = None,
        transfer_time: int = None,
    ):
        self.arr_city_code = arr_city_code
        self.arr_city_name = arr_city_name
        self.arr_time = arr_time
        self.dep_city_code = dep_city_code
        self.dep_city_name = dep_city_name
        self.dep_time = dep_time
        self.duration = duration
        self.flight_segment_infos = flight_segment_infos
        self.journey_index = journey_index
        self.transfer_time = transfer_time

    def validate(self):
        if self.flight_segment_infos:
            for v1 in self.flight_segment_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.duration is not None:
            result['duration'] = self.duration

        result['flight_segment_infos'] = []
        if self.flight_segment_infos is not None:
            for k1 in self.flight_segment_infos:
                result['flight_segment_infos'].append(k1.to_map() if k1 else None)

        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.transfer_time is not None:
            result['transfer_time'] = self.transfer_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        self.flight_segment_infos = []
        if m.get('flight_segment_infos') is not None:
            for k1 in m.get('flight_segment_infos'):
                temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfos()
                self.flight_segment_infos.append(temp_model.from_map(k1))

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('transfer_time') is not None:
            self.transfer_time = m.get('transfer_time')

        return self

class IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfos(DaraModel):
    def __init__(
        self,
        airline_info: main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosAirlineInfo = None,
        arr_airport_info: main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosArrAirportInfo = None,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        dep_airport_info: main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosDepAirportInfo = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        duration: int = None,
        flight_no: str = None,
        flight_share_info: main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosFlightShareInfo = None,
        flight_size: str = None,
        flight_stop_info_list: List[main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosFlightStopInfoList] = None,
        flight_type: str = None,
        journey_index: int = None,
        luggage_direct_info: main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosLuggageDirectInfo = None,
        manufacturer: str = None,
        meal_desc: str = None,
        one_more: int = None,
        one_more_show: str = None,
        segment_index: int = None,
        segment_key: str = None,
        segment_visa_remark: main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosSegmentVisaRemark = None,
        share: bool = None,
        short_flight_size: str = None,
        stop: bool = None,
        total_time: str = None,
    ):
        self.airline_info = airline_info
        self.arr_airport_info = arr_airport_info
        self.arr_city_code = arr_city_code
        self.arr_city_name = arr_city_name
        self.arr_time = arr_time
        self.dep_airport_info = dep_airport_info
        self.dep_city_code = dep_city_code
        self.dep_city_name = dep_city_name
        self.dep_time = dep_time
        self.duration = duration
        self.flight_no = flight_no
        self.flight_share_info = flight_share_info
        self.flight_size = flight_size
        self.flight_stop_info_list = flight_stop_info_list
        self.flight_type = flight_type
        self.journey_index = journey_index
        self.luggage_direct_info = luggage_direct_info
        self.manufacturer = manufacturer
        self.meal_desc = meal_desc
        self.one_more = one_more
        self.one_more_show = one_more_show
        self.segment_index = segment_index
        self.segment_key = segment_key
        self.segment_visa_remark = segment_visa_remark
        self.share = share
        self.short_flight_size = short_flight_size
        self.stop = stop
        self.total_time = total_time

    def validate(self):
        if self.airline_info:
            self.airline_info.validate()
        if self.arr_airport_info:
            self.arr_airport_info.validate()
        if self.dep_airport_info:
            self.dep_airport_info.validate()
        if self.flight_share_info:
            self.flight_share_info.validate()
        if self.flight_stop_info_list:
            for v1 in self.flight_stop_info_list:
                 if v1:
                    v1.validate()
        if self.luggage_direct_info:
            self.luggage_direct_info.validate()
        if self.segment_visa_remark:
            self.segment_visa_remark.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_info is not None:
            result['airline_info'] = self.airline_info.to_map()

        if self.arr_airport_info is not None:
            result['arr_airport_info'] = self.arr_airport_info.to_map()

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.dep_airport_info is not None:
            result['dep_airport_info'] = self.dep_airport_info.to_map()

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.duration is not None:
            result['duration'] = self.duration

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.flight_share_info is not None:
            result['flight_share_info'] = self.flight_share_info.to_map()

        if self.flight_size is not None:
            result['flight_size'] = self.flight_size

        result['flight_stop_info_list'] = []
        if self.flight_stop_info_list is not None:
            for k1 in self.flight_stop_info_list:
                result['flight_stop_info_list'].append(k1.to_map() if k1 else None)

        if self.flight_type is not None:
            result['flight_type'] = self.flight_type

        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.luggage_direct_info is not None:
            result['luggage_direct_info'] = self.luggage_direct_info.to_map()

        if self.manufacturer is not None:
            result['manufacturer'] = self.manufacturer

        if self.meal_desc is not None:
            result['meal_desc'] = self.meal_desc

        if self.one_more is not None:
            result['one_more'] = self.one_more

        if self.one_more_show is not None:
            result['one_more_show'] = self.one_more_show

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.segment_key is not None:
            result['segment_key'] = self.segment_key

        if self.segment_visa_remark is not None:
            result['segment_visa_remark'] = self.segment_visa_remark.to_map()

        if self.share is not None:
            result['share'] = self.share

        if self.short_flight_size is not None:
            result['short_flight_size'] = self.short_flight_size

        if self.stop is not None:
            result['stop'] = self.stop

        if self.total_time is not None:
            result['total_time'] = self.total_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_info') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosAirlineInfo()
            self.airline_info = temp_model.from_map(m.get('airline_info'))

        if m.get('arr_airport_info') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosArrAirportInfo()
            self.arr_airport_info = temp_model.from_map(m.get('arr_airport_info'))

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_airport_info') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosDepAirportInfo()
            self.dep_airport_info = temp_model.from_map(m.get('dep_airport_info'))

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('flight_share_info') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosFlightShareInfo()
            self.flight_share_info = temp_model.from_map(m.get('flight_share_info'))

        if m.get('flight_size') is not None:
            self.flight_size = m.get('flight_size')

        self.flight_stop_info_list = []
        if m.get('flight_stop_info_list') is not None:
            for k1 in m.get('flight_stop_info_list'):
                temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosFlightStopInfoList()
                self.flight_stop_info_list.append(temp_model.from_map(k1))

        if m.get('flight_type') is not None:
            self.flight_type = m.get('flight_type')

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('luggage_direct_info') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosLuggageDirectInfo()
            self.luggage_direct_info = temp_model.from_map(m.get('luggage_direct_info'))

        if m.get('manufacturer') is not None:
            self.manufacturer = m.get('manufacturer')

        if m.get('meal_desc') is not None:
            self.meal_desc = m.get('meal_desc')

        if m.get('one_more') is not None:
            self.one_more = m.get('one_more')

        if m.get('one_more_show') is not None:
            self.one_more_show = m.get('one_more_show')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('segment_key') is not None:
            self.segment_key = m.get('segment_key')

        if m.get('segment_visa_remark') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosSegmentVisaRemark()
            self.segment_visa_remark = temp_model.from_map(m.get('segment_visa_remark'))

        if m.get('share') is not None:
            self.share = m.get('share')

        if m.get('short_flight_size') is not None:
            self.short_flight_size = m.get('short_flight_size')

        if m.get('stop') is not None:
            self.stop = m.get('stop')

        if m.get('total_time') is not None:
            self.total_time = m.get('total_time')

        return self

class IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosSegmentVisaRemark(DaraModel):
    def __init__(
        self,
        dep_city_visa_remark: str = None,
        dep_city_visa_type: int = None,
        stop_city_visa_remarks: List[str] = None,
        stop_city_visa_types: List[int] = None,
    ):
        self.dep_city_visa_remark = dep_city_visa_remark
        self.dep_city_visa_type = dep_city_visa_type
        self.stop_city_visa_remarks = stop_city_visa_remarks
        self.stop_city_visa_types = stop_city_visa_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dep_city_visa_remark is not None:
            result['dep_city_visa_remark'] = self.dep_city_visa_remark

        if self.dep_city_visa_type is not None:
            result['dep_city_visa_type'] = self.dep_city_visa_type

        if self.stop_city_visa_remarks is not None:
            result['stop_city_visa_remarks'] = self.stop_city_visa_remarks

        if self.stop_city_visa_types is not None:
            result['stop_city_visa_types'] = self.stop_city_visa_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dep_city_visa_remark') is not None:
            self.dep_city_visa_remark = m.get('dep_city_visa_remark')

        if m.get('dep_city_visa_type') is not None:
            self.dep_city_visa_type = m.get('dep_city_visa_type')

        if m.get('stop_city_visa_remarks') is not None:
            self.stop_city_visa_remarks = m.get('stop_city_visa_remarks')

        if m.get('stop_city_visa_types') is not None:
            self.stop_city_visa_types = m.get('stop_city_visa_types')

        return self

class IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosLuggageDirectInfo(DaraModel):
    def __init__(
        self,
        dep_city_luggage_direct: int = None,
        stop_city_luggage_direct: int = None,
    ):
        self.dep_city_luggage_direct = dep_city_luggage_direct
        self.stop_city_luggage_direct = stop_city_luggage_direct

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dep_city_luggage_direct is not None:
            result['dep_city_luggage_direct'] = self.dep_city_luggage_direct

        if self.stop_city_luggage_direct is not None:
            result['stop_city_luggage_direct'] = self.stop_city_luggage_direct

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dep_city_luggage_direct') is not None:
            self.dep_city_luggage_direct = m.get('dep_city_luggage_direct')

        if m.get('stop_city_luggage_direct') is not None:
            self.stop_city_luggage_direct = m.get('stop_city_luggage_direct')

        return self

class IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosFlightStopInfoList(DaraModel):
    def __init__(
        self,
        stop_airport: str = None,
        stop_airport_name: str = None,
        stop_arr_term: str = None,
        stop_arr_time: str = None,
        stop_city_code: str = None,
        stop_city_name: str = None,
        stop_dep_term: str = None,
        stop_dep_time: str = None,
        stop_time: str = None,
    ):
        self.stop_airport = stop_airport
        self.stop_airport_name = stop_airport_name
        self.stop_arr_term = stop_arr_term
        self.stop_arr_time = stop_arr_time
        self.stop_city_code = stop_city_code
        self.stop_city_name = stop_city_name
        self.stop_dep_term = stop_dep_term
        self.stop_dep_time = stop_dep_time
        self.stop_time = stop_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stop_airport is not None:
            result['stop_airport'] = self.stop_airport

        if self.stop_airport_name is not None:
            result['stop_airport_name'] = self.stop_airport_name

        if self.stop_arr_term is not None:
            result['stop_arr_term'] = self.stop_arr_term

        if self.stop_arr_time is not None:
            result['stop_arr_time'] = self.stop_arr_time

        if self.stop_city_code is not None:
            result['stop_city_code'] = self.stop_city_code

        if self.stop_city_name is not None:
            result['stop_city_name'] = self.stop_city_name

        if self.stop_dep_term is not None:
            result['stop_dep_term'] = self.stop_dep_term

        if self.stop_dep_time is not None:
            result['stop_dep_time'] = self.stop_dep_time

        if self.stop_time is not None:
            result['stop_time'] = self.stop_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stop_airport') is not None:
            self.stop_airport = m.get('stop_airport')

        if m.get('stop_airport_name') is not None:
            self.stop_airport_name = m.get('stop_airport_name')

        if m.get('stop_arr_term') is not None:
            self.stop_arr_term = m.get('stop_arr_term')

        if m.get('stop_arr_time') is not None:
            self.stop_arr_time = m.get('stop_arr_time')

        if m.get('stop_city_code') is not None:
            self.stop_city_code = m.get('stop_city_code')

        if m.get('stop_city_name') is not None:
            self.stop_city_name = m.get('stop_city_name')

        if m.get('stop_dep_term') is not None:
            self.stop_dep_term = m.get('stop_dep_term')

        if m.get('stop_dep_time') is not None:
            self.stop_dep_time = m.get('stop_dep_time')

        if m.get('stop_time') is not None:
            self.stop_time = m.get('stop_time')

        return self

class IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosFlightShareInfo(DaraModel):
    def __init__(
        self,
        operating_airline_info: main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosFlightShareInfoOperatingAirlineInfo = None,
        operating_flight_no: str = None,
    ):
        self.operating_airline_info = operating_airline_info
        self.operating_flight_no = operating_flight_no

    def validate(self):
        if self.operating_airline_info:
            self.operating_airline_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operating_airline_info is not None:
            result['operating_airline_info'] = self.operating_airline_info.to_map()

        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operating_airline_info') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosFlightShareInfoOperatingAirlineInfo()
            self.operating_airline_info = temp_model.from_map(m.get('operating_airline_info'))

        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')

        return self

class IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosFlightShareInfoOperatingAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        short_name: str = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.short_name = short_name

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

        if self.short_name is not None:
            result['short_name'] = self.short_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('short_name') is not None:
            self.short_name = m.get('short_name')

        return self

class IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosDepAirportInfo(DaraModel):
    def __init__(
        self,
        airport_code: str = None,
        airport_name: str = None,
        airport_short_name: str = None,
        terminal: str = None,
    ):
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.airport_short_name = airport_short_name
        self.terminal = terminal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airport_code is not None:
            result['airport_code'] = self.airport_code

        if self.airport_name is not None:
            result['airport_name'] = self.airport_name

        if self.airport_short_name is not None:
            result['airport_short_name'] = self.airport_short_name

        if self.terminal is not None:
            result['terminal'] = self.terminal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('airport_short_name') is not None:
            self.airport_short_name = m.get('airport_short_name')

        if m.get('terminal') is not None:
            self.terminal = m.get('terminal')

        return self

class IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosArrAirportInfo(DaraModel):
    def __init__(
        self,
        airport_code: str = None,
        airport_name: str = None,
        airport_short_name: str = None,
        terminal: str = None,
    ):
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.airport_short_name = airport_short_name
        self.terminal = terminal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airport_code is not None:
            result['airport_code'] = self.airport_code

        if self.airport_name is not None:
            result['airport_name'] = self.airport_name

        if self.airport_short_name is not None:
            result['airport_short_name'] = self.airport_short_name

        if self.terminal is not None:
            result['terminal'] = self.terminal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('airport_short_name') is not None:
            self.airport_short_name = m.get('airport_short_name')

        if m.get('terminal') is not None:
            self.terminal = m.get('terminal')

        return self

class IntlFlightReShopDetailResponseBodyModuleOriginJourneyListFlightSegmentInfosAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        short_name: str = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.short_name = short_name

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

        if self.short_name is not None:
            result['short_name'] = self.short_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('short_name') is not None:
            self.short_name = m.get('short_name')

        return self

class IntlFlightReShopDetailResponseBodyModuleJourneyList(DaraModel):
    def __init__(
        self,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        duration: int = None,
        flight_segment_infos: List[main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfos] = None,
        journey_index: int = None,
        transfer_time: int = None,
    ):
        self.arr_city_code = arr_city_code
        self.arr_city_name = arr_city_name
        self.arr_time = arr_time
        self.dep_city_code = dep_city_code
        self.dep_city_name = dep_city_name
        self.dep_time = dep_time
        self.duration = duration
        self.flight_segment_infos = flight_segment_infos
        self.journey_index = journey_index
        self.transfer_time = transfer_time

    def validate(self):
        if self.flight_segment_infos:
            for v1 in self.flight_segment_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.duration is not None:
            result['duration'] = self.duration

        result['flight_segment_infos'] = []
        if self.flight_segment_infos is not None:
            for k1 in self.flight_segment_infos:
                result['flight_segment_infos'].append(k1.to_map() if k1 else None)

        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.transfer_time is not None:
            result['transfer_time'] = self.transfer_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        self.flight_segment_infos = []
        if m.get('flight_segment_infos') is not None:
            for k1 in m.get('flight_segment_infos'):
                temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfos()
                self.flight_segment_infos.append(temp_model.from_map(k1))

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('transfer_time') is not None:
            self.transfer_time = m.get('transfer_time')

        return self

class IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfos(DaraModel):
    def __init__(
        self,
        airline_info: main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosAirlineInfo = None,
        arr_airport_info: main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosArrAirportInfo = None,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        dep_airport_info: main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosDepAirportInfo = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        duration: int = None,
        flight_no: str = None,
        flight_share_info: main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightShareInfo = None,
        flight_size: str = None,
        flight_stop_info_list: List[main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightStopInfoList] = None,
        flight_type: str = None,
        journey_index: int = None,
        luggage_direct_info: main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosLuggageDirectInfo = None,
        manufacturer: str = None,
        meal_desc: str = None,
        one_more: int = None,
        one_more_show: str = None,
        segment_index: int = None,
        segment_key: str = None,
        segment_visa_remark: main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosSegmentVisaRemark = None,
        share: bool = None,
        short_flight_size: str = None,
        stop: bool = None,
        total_time: str = None,
    ):
        self.airline_info = airline_info
        self.arr_airport_info = arr_airport_info
        self.arr_city_code = arr_city_code
        self.arr_city_name = arr_city_name
        self.arr_time = arr_time
        self.dep_airport_info = dep_airport_info
        self.dep_city_code = dep_city_code
        self.dep_city_name = dep_city_name
        self.dep_time = dep_time
        self.duration = duration
        self.flight_no = flight_no
        self.flight_share_info = flight_share_info
        self.flight_size = flight_size
        self.flight_stop_info_list = flight_stop_info_list
        self.flight_type = flight_type
        self.journey_index = journey_index
        self.luggage_direct_info = luggage_direct_info
        self.manufacturer = manufacturer
        self.meal_desc = meal_desc
        self.one_more = one_more
        self.one_more_show = one_more_show
        self.segment_index = segment_index
        self.segment_key = segment_key
        self.segment_visa_remark = segment_visa_remark
        self.share = share
        self.short_flight_size = short_flight_size
        self.stop = stop
        self.total_time = total_time

    def validate(self):
        if self.airline_info:
            self.airline_info.validate()
        if self.arr_airport_info:
            self.arr_airport_info.validate()
        if self.dep_airport_info:
            self.dep_airport_info.validate()
        if self.flight_share_info:
            self.flight_share_info.validate()
        if self.flight_stop_info_list:
            for v1 in self.flight_stop_info_list:
                 if v1:
                    v1.validate()
        if self.luggage_direct_info:
            self.luggage_direct_info.validate()
        if self.segment_visa_remark:
            self.segment_visa_remark.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_info is not None:
            result['airline_info'] = self.airline_info.to_map()

        if self.arr_airport_info is not None:
            result['arr_airport_info'] = self.arr_airport_info.to_map()

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.dep_airport_info is not None:
            result['dep_airport_info'] = self.dep_airport_info.to_map()

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.duration is not None:
            result['duration'] = self.duration

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.flight_share_info is not None:
            result['flight_share_info'] = self.flight_share_info.to_map()

        if self.flight_size is not None:
            result['flight_size'] = self.flight_size

        result['flight_stop_info_list'] = []
        if self.flight_stop_info_list is not None:
            for k1 in self.flight_stop_info_list:
                result['flight_stop_info_list'].append(k1.to_map() if k1 else None)

        if self.flight_type is not None:
            result['flight_type'] = self.flight_type

        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.luggage_direct_info is not None:
            result['luggage_direct_info'] = self.luggage_direct_info.to_map()

        if self.manufacturer is not None:
            result['manufacturer'] = self.manufacturer

        if self.meal_desc is not None:
            result['meal_desc'] = self.meal_desc

        if self.one_more is not None:
            result['one_more'] = self.one_more

        if self.one_more_show is not None:
            result['one_more_show'] = self.one_more_show

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.segment_key is not None:
            result['segment_key'] = self.segment_key

        if self.segment_visa_remark is not None:
            result['segment_visa_remark'] = self.segment_visa_remark.to_map()

        if self.share is not None:
            result['share'] = self.share

        if self.short_flight_size is not None:
            result['short_flight_size'] = self.short_flight_size

        if self.stop is not None:
            result['stop'] = self.stop

        if self.total_time is not None:
            result['total_time'] = self.total_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_info') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosAirlineInfo()
            self.airline_info = temp_model.from_map(m.get('airline_info'))

        if m.get('arr_airport_info') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosArrAirportInfo()
            self.arr_airport_info = temp_model.from_map(m.get('arr_airport_info'))

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_airport_info') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosDepAirportInfo()
            self.dep_airport_info = temp_model.from_map(m.get('dep_airport_info'))

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('flight_share_info') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightShareInfo()
            self.flight_share_info = temp_model.from_map(m.get('flight_share_info'))

        if m.get('flight_size') is not None:
            self.flight_size = m.get('flight_size')

        self.flight_stop_info_list = []
        if m.get('flight_stop_info_list') is not None:
            for k1 in m.get('flight_stop_info_list'):
                temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightStopInfoList()
                self.flight_stop_info_list.append(temp_model.from_map(k1))

        if m.get('flight_type') is not None:
            self.flight_type = m.get('flight_type')

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('luggage_direct_info') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosLuggageDirectInfo()
            self.luggage_direct_info = temp_model.from_map(m.get('luggage_direct_info'))

        if m.get('manufacturer') is not None:
            self.manufacturer = m.get('manufacturer')

        if m.get('meal_desc') is not None:
            self.meal_desc = m.get('meal_desc')

        if m.get('one_more') is not None:
            self.one_more = m.get('one_more')

        if m.get('one_more_show') is not None:
            self.one_more_show = m.get('one_more_show')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('segment_key') is not None:
            self.segment_key = m.get('segment_key')

        if m.get('segment_visa_remark') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosSegmentVisaRemark()
            self.segment_visa_remark = temp_model.from_map(m.get('segment_visa_remark'))

        if m.get('share') is not None:
            self.share = m.get('share')

        if m.get('short_flight_size') is not None:
            self.short_flight_size = m.get('short_flight_size')

        if m.get('stop') is not None:
            self.stop = m.get('stop')

        if m.get('total_time') is not None:
            self.total_time = m.get('total_time')

        return self

class IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosSegmentVisaRemark(DaraModel):
    def __init__(
        self,
        dep_city_visa_remark: str = None,
        dep_city_visa_type: int = None,
        stop_city_visa_remarks: List[str] = None,
        stop_city_visa_types: List[int] = None,
    ):
        self.dep_city_visa_remark = dep_city_visa_remark
        self.dep_city_visa_type = dep_city_visa_type
        self.stop_city_visa_remarks = stop_city_visa_remarks
        self.stop_city_visa_types = stop_city_visa_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dep_city_visa_remark is not None:
            result['dep_city_visa_remark'] = self.dep_city_visa_remark

        if self.dep_city_visa_type is not None:
            result['dep_city_visa_type'] = self.dep_city_visa_type

        if self.stop_city_visa_remarks is not None:
            result['stop_city_visa_remarks'] = self.stop_city_visa_remarks

        if self.stop_city_visa_types is not None:
            result['stop_city_visa_types'] = self.stop_city_visa_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dep_city_visa_remark') is not None:
            self.dep_city_visa_remark = m.get('dep_city_visa_remark')

        if m.get('dep_city_visa_type') is not None:
            self.dep_city_visa_type = m.get('dep_city_visa_type')

        if m.get('stop_city_visa_remarks') is not None:
            self.stop_city_visa_remarks = m.get('stop_city_visa_remarks')

        if m.get('stop_city_visa_types') is not None:
            self.stop_city_visa_types = m.get('stop_city_visa_types')

        return self

class IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosLuggageDirectInfo(DaraModel):
    def __init__(
        self,
        dep_city_luggage_direct: int = None,
        stop_city_luggage_direct: int = None,
    ):
        self.dep_city_luggage_direct = dep_city_luggage_direct
        self.stop_city_luggage_direct = stop_city_luggage_direct

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dep_city_luggage_direct is not None:
            result['dep_city_luggage_direct'] = self.dep_city_luggage_direct

        if self.stop_city_luggage_direct is not None:
            result['stop_city_luggage_direct'] = self.stop_city_luggage_direct

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dep_city_luggage_direct') is not None:
            self.dep_city_luggage_direct = m.get('dep_city_luggage_direct')

        if m.get('stop_city_luggage_direct') is not None:
            self.stop_city_luggage_direct = m.get('stop_city_luggage_direct')

        return self

class IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightStopInfoList(DaraModel):
    def __init__(
        self,
        stop_airport: str = None,
        stop_airport_name: str = None,
        stop_arr_term: str = None,
        stop_arr_time: str = None,
        stop_city_code: str = None,
        stop_city_name: str = None,
        stop_dep_term: str = None,
        stop_dep_time: str = None,
        stop_time: str = None,
    ):
        self.stop_airport = stop_airport
        self.stop_airport_name = stop_airport_name
        self.stop_arr_term = stop_arr_term
        self.stop_arr_time = stop_arr_time
        self.stop_city_code = stop_city_code
        self.stop_city_name = stop_city_name
        self.stop_dep_term = stop_dep_term
        self.stop_dep_time = stop_dep_time
        self.stop_time = stop_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stop_airport is not None:
            result['stop_airport'] = self.stop_airport

        if self.stop_airport_name is not None:
            result['stop_airport_name'] = self.stop_airport_name

        if self.stop_arr_term is not None:
            result['stop_arr_term'] = self.stop_arr_term

        if self.stop_arr_time is not None:
            result['stop_arr_time'] = self.stop_arr_time

        if self.stop_city_code is not None:
            result['stop_city_code'] = self.stop_city_code

        if self.stop_city_name is not None:
            result['stop_city_name'] = self.stop_city_name

        if self.stop_dep_term is not None:
            result['stop_dep_term'] = self.stop_dep_term

        if self.stop_dep_time is not None:
            result['stop_dep_time'] = self.stop_dep_time

        if self.stop_time is not None:
            result['stop_time'] = self.stop_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stop_airport') is not None:
            self.stop_airport = m.get('stop_airport')

        if m.get('stop_airport_name') is not None:
            self.stop_airport_name = m.get('stop_airport_name')

        if m.get('stop_arr_term') is not None:
            self.stop_arr_term = m.get('stop_arr_term')

        if m.get('stop_arr_time') is not None:
            self.stop_arr_time = m.get('stop_arr_time')

        if m.get('stop_city_code') is not None:
            self.stop_city_code = m.get('stop_city_code')

        if m.get('stop_city_name') is not None:
            self.stop_city_name = m.get('stop_city_name')

        if m.get('stop_dep_term') is not None:
            self.stop_dep_term = m.get('stop_dep_term')

        if m.get('stop_dep_time') is not None:
            self.stop_dep_time = m.get('stop_dep_time')

        if m.get('stop_time') is not None:
            self.stop_time = m.get('stop_time')

        return self

class IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightShareInfo(DaraModel):
    def __init__(
        self,
        operating_airline_info: main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightShareInfoOperatingAirlineInfo = None,
        operating_flight_no: str = None,
    ):
        self.operating_airline_info = operating_airline_info
        self.operating_flight_no = operating_flight_no

    def validate(self):
        if self.operating_airline_info:
            self.operating_airline_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operating_airline_info is not None:
            result['operating_airline_info'] = self.operating_airline_info.to_map()

        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operating_airline_info') is not None:
            temp_model = main_models.IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightShareInfoOperatingAirlineInfo()
            self.operating_airline_info = temp_model.from_map(m.get('operating_airline_info'))

        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')

        return self

class IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightShareInfoOperatingAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        short_name: str = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.short_name = short_name

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

        if self.short_name is not None:
            result['short_name'] = self.short_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('short_name') is not None:
            self.short_name = m.get('short_name')

        return self

class IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosDepAirportInfo(DaraModel):
    def __init__(
        self,
        airport_code: str = None,
        airport_name: str = None,
        airport_short_name: str = None,
        terminal: str = None,
    ):
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.airport_short_name = airport_short_name
        self.terminal = terminal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airport_code is not None:
            result['airport_code'] = self.airport_code

        if self.airport_name is not None:
            result['airport_name'] = self.airport_name

        if self.airport_short_name is not None:
            result['airport_short_name'] = self.airport_short_name

        if self.terminal is not None:
            result['terminal'] = self.terminal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('airport_short_name') is not None:
            self.airport_short_name = m.get('airport_short_name')

        if m.get('terminal') is not None:
            self.terminal = m.get('terminal')

        return self

class IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosArrAirportInfo(DaraModel):
    def __init__(
        self,
        airport_code: str = None,
        airport_name: str = None,
        airport_short_name: str = None,
        terminal: str = None,
    ):
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.airport_short_name = airport_short_name
        self.terminal = terminal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airport_code is not None:
            result['airport_code'] = self.airport_code

        if self.airport_name is not None:
            result['airport_name'] = self.airport_name

        if self.airport_short_name is not None:
            result['airport_short_name'] = self.airport_short_name

        if self.terminal is not None:
            result['terminal'] = self.terminal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('airport_short_name') is not None:
            self.airport_short_name = m.get('airport_short_name')

        if m.get('terminal') is not None:
            self.terminal = m.get('terminal')

        return self

class IntlFlightReShopDetailResponseBodyModuleJourneyListFlightSegmentInfosAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        short_name: str = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.short_name = short_name

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

        if self.short_name is not None:
            result['short_name'] = self.short_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('short_name') is not None:
            self.short_name = m.get('short_name')

        return self

class IntlFlightReShopDetailResponseBodyModuleBaggageRule(DaraModel):
    def __init__(
        self,
        baggage_rule_desc: str = None,
    ):
        self.baggage_rule_desc = baggage_rule_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baggage_rule_desc is not None:
            result['baggage_rule_desc'] = self.baggage_rule_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baggage_rule_desc') is not None:
            self.baggage_rule_desc = m.get('baggage_rule_desc')

        return self

