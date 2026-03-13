# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IntlFlightOrderDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.IntlFlightOrderDetailResponseBodyModule = None,
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
            temp_model = main_models.IntlFlightOrderDetailResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class IntlFlightOrderDetailResponseBodyModule(DaraModel):
    def __init__(
        self,
        booker_user_id: str = None,
        booker_user_name: str = None,
        close_reason: str = None,
        close_time: str = None,
        contact_info: main_models.IntlFlightOrderDetailResponseBodyModuleContactInfo = None,
        journey_list: List[main_models.IntlFlightOrderDetailResponseBodyModuleJourneyList] = None,
        order_id: str = None,
        order_item_list: List[main_models.IntlFlightOrderDetailResponseBodyModuleOrderItemList] = None,
        order_status: int = None,
        out_order_id: str = None,
        passenger_list: List[main_models.IntlFlightOrderDetailResponseBodyModulePassengerList] = None,
        passenger_ticket_list: List[main_models.IntlFlightOrderDetailResponseBodyModulePassengerTicketList] = None,
        pay_latest_time: str = None,
        pay_status: int = None,
        pay_time: str = None,
        pay_type: int = None,
        success_time: str = None,
        total_price: int = None,
        total_tax_price: int = None,
        total_ticket_price: int = None,
        trip_type: int = None,
    ):
        self.booker_user_id = booker_user_id
        self.booker_user_name = booker_user_name
        self.close_reason = close_reason
        self.close_time = close_time
        self.contact_info = contact_info
        self.journey_list = journey_list
        self.order_id = order_id
        self.order_item_list = order_item_list
        self.order_status = order_status
        self.out_order_id = out_order_id
        self.passenger_list = passenger_list
        self.passenger_ticket_list = passenger_ticket_list
        self.pay_latest_time = pay_latest_time
        self.pay_status = pay_status
        self.pay_time = pay_time
        self.pay_type = pay_type
        self.success_time = success_time
        self.total_price = total_price
        self.total_tax_price = total_tax_price
        self.total_ticket_price = total_ticket_price
        self.trip_type = trip_type

    def validate(self):
        if self.contact_info:
            self.contact_info.validate()
        if self.journey_list:
            for v1 in self.journey_list:
                 if v1:
                    v1.validate()
        if self.order_item_list:
            for v1 in self.order_item_list:
                 if v1:
                    v1.validate()
        if self.passenger_list:
            for v1 in self.passenger_list:
                 if v1:
                    v1.validate()
        if self.passenger_ticket_list:
            for v1 in self.passenger_ticket_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.booker_user_id is not None:
            result['booker_user_id'] = self.booker_user_id

        if self.booker_user_name is not None:
            result['booker_user_name'] = self.booker_user_name

        if self.close_reason is not None:
            result['close_reason'] = self.close_reason

        if self.close_time is not None:
            result['close_time'] = self.close_time

        if self.contact_info is not None:
            result['contact_info'] = self.contact_info.to_map()

        result['journey_list'] = []
        if self.journey_list is not None:
            for k1 in self.journey_list:
                result['journey_list'].append(k1.to_map() if k1 else None)

        if self.order_id is not None:
            result['order_id'] = self.order_id

        result['order_item_list'] = []
        if self.order_item_list is not None:
            for k1 in self.order_item_list:
                result['order_item_list'].append(k1.to_map() if k1 else None)

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k1 in self.passenger_list:
                result['passenger_list'].append(k1.to_map() if k1 else None)

        result['passenger_ticket_list'] = []
        if self.passenger_ticket_list is not None:
            for k1 in self.passenger_ticket_list:
                result['passenger_ticket_list'].append(k1.to_map() if k1 else None)

        if self.pay_latest_time is not None:
            result['pay_latest_time'] = self.pay_latest_time

        if self.pay_status is not None:
            result['pay_status'] = self.pay_status

        if self.pay_time is not None:
            result['pay_time'] = self.pay_time

        if self.pay_type is not None:
            result['pay_type'] = self.pay_type

        if self.success_time is not None:
            result['success_time'] = self.success_time

        if self.total_price is not None:
            result['total_price'] = self.total_price

        if self.total_tax_price is not None:
            result['total_tax_price'] = self.total_tax_price

        if self.total_ticket_price is not None:
            result['total_ticket_price'] = self.total_ticket_price

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('booker_user_id') is not None:
            self.booker_user_id = m.get('booker_user_id')

        if m.get('booker_user_name') is not None:
            self.booker_user_name = m.get('booker_user_name')

        if m.get('close_reason') is not None:
            self.close_reason = m.get('close_reason')

        if m.get('close_time') is not None:
            self.close_time = m.get('close_time')

        if m.get('contact_info') is not None:
            temp_model = main_models.IntlFlightOrderDetailResponseBodyModuleContactInfo()
            self.contact_info = temp_model.from_map(m.get('contact_info'))

        self.journey_list = []
        if m.get('journey_list') is not None:
            for k1 in m.get('journey_list'):
                temp_model = main_models.IntlFlightOrderDetailResponseBodyModuleJourneyList()
                self.journey_list.append(temp_model.from_map(k1))

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        self.order_item_list = []
        if m.get('order_item_list') is not None:
            for k1 in m.get('order_item_list'):
                temp_model = main_models.IntlFlightOrderDetailResponseBodyModuleOrderItemList()
                self.order_item_list.append(temp_model.from_map(k1))

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k1 in m.get('passenger_list'):
                temp_model = main_models.IntlFlightOrderDetailResponseBodyModulePassengerList()
                self.passenger_list.append(temp_model.from_map(k1))

        self.passenger_ticket_list = []
        if m.get('passenger_ticket_list') is not None:
            for k1 in m.get('passenger_ticket_list'):
                temp_model = main_models.IntlFlightOrderDetailResponseBodyModulePassengerTicketList()
                self.passenger_ticket_list.append(temp_model.from_map(k1))

        if m.get('pay_latest_time') is not None:
            self.pay_latest_time = m.get('pay_latest_time')

        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')

        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')

        if m.get('pay_type') is not None:
            self.pay_type = m.get('pay_type')

        if m.get('success_time') is not None:
            self.success_time = m.get('success_time')

        if m.get('total_price') is not None:
            self.total_price = m.get('total_price')

        if m.get('total_tax_price') is not None:
            self.total_tax_price = m.get('total_tax_price')

        if m.get('total_ticket_price') is not None:
            self.total_ticket_price = m.get('total_ticket_price')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        return self

class IntlFlightOrderDetailResponseBodyModulePassengerTicketList(DaraModel):
    def __init__(
        self,
        passenger_id: int = None,
        ticket_list: List[main_models.IntlFlightOrderDetailResponseBodyModulePassengerTicketListTicketList] = None,
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
                temp_model = main_models.IntlFlightOrderDetailResponseBodyModulePassengerTicketListTicketList()
                self.ticket_list.append(temp_model.from_map(k1))

        return self

class IntlFlightOrderDetailResponseBodyModulePassengerTicketListTicketList(DaraModel):
    def __init__(
        self,
        issue_time: str = None,
        pnr_no: str = None,
        price_info: main_models.IntlFlightOrderDetailResponseBodyModulePassengerTicketListTicketListPriceInfo = None,
        segment_key_list: List[str] = None,
        ticket_no: str = None,
        ticket_segment_list: List[main_models.IntlFlightOrderDetailResponseBodyModulePassengerTicketListTicketListTicketSegmentList] = None,
    ):
        self.issue_time = issue_time
        self.pnr_no = pnr_no
        self.price_info = price_info
        self.segment_key_list = segment_key_list
        self.ticket_no = ticket_no
        self.ticket_segment_list = ticket_segment_list

    def validate(self):
        if self.price_info:
            self.price_info.validate()
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

        if self.price_info is not None:
            result['price_info'] = self.price_info.to_map()

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

        if m.get('price_info') is not None:
            temp_model = main_models.IntlFlightOrderDetailResponseBodyModulePassengerTicketListTicketListPriceInfo()
            self.price_info = temp_model.from_map(m.get('price_info'))

        if m.get('segment_key_list') is not None:
            self.segment_key_list = m.get('segment_key_list')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        self.ticket_segment_list = []
        if m.get('ticket_segment_list') is not None:
            for k1 in m.get('ticket_segment_list'):
                temp_model = main_models.IntlFlightOrderDetailResponseBodyModulePassengerTicketListTicketListTicketSegmentList()
                self.ticket_segment_list.append(temp_model.from_map(k1))

        return self

class IntlFlightOrderDetailResponseBodyModulePassengerTicketListTicketListTicketSegmentList(DaraModel):
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

class IntlFlightOrderDetailResponseBodyModulePassengerTicketListTicketListPriceInfo(DaraModel):
    def __init__(
        self,
        sell_price: int = None,
        tax: int = None,
        ticket_price: int = None,
    ):
        self.sell_price = sell_price
        self.tax = tax
        self.ticket_price = ticket_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sell_price is not None:
            result['sell_price'] = self.sell_price

        if self.tax is not None:
            result['tax'] = self.tax

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sell_price') is not None:
            self.sell_price = m.get('sell_price')

        if m.get('tax') is not None:
            self.tax = m.get('tax')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        return self

class IntlFlightOrderDetailResponseBodyModulePassengerList(DaraModel):
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

class IntlFlightOrderDetailResponseBodyModuleOrderItemList(DaraModel):
    def __init__(
        self,
        baggage_rule: main_models.IntlFlightOrderDetailResponseBodyModuleOrderItemListBaggageRule = None,
        passenger_price_list: List[main_models.IntlFlightOrderDetailResponseBodyModuleOrderItemListPassengerPriceList] = None,
        refund_change_rule: main_models.IntlFlightOrderDetailResponseBodyModuleOrderItemListRefundChangeRule = None,
        segment_key_list: List[str] = None,
    ):
        self.baggage_rule = baggage_rule
        self.passenger_price_list = passenger_price_list
        self.refund_change_rule = refund_change_rule
        self.segment_key_list = segment_key_list

    def validate(self):
        if self.baggage_rule:
            self.baggage_rule.validate()
        if self.passenger_price_list:
            for v1 in self.passenger_price_list:
                 if v1:
                    v1.validate()
        if self.refund_change_rule:
            self.refund_change_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baggage_rule is not None:
            result['baggage_rule'] = self.baggage_rule.to_map()

        result['passenger_price_list'] = []
        if self.passenger_price_list is not None:
            for k1 in self.passenger_price_list:
                result['passenger_price_list'].append(k1.to_map() if k1 else None)

        if self.refund_change_rule is not None:
            result['refund_change_rule'] = self.refund_change_rule.to_map()

        if self.segment_key_list is not None:
            result['segment_key_list'] = self.segment_key_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baggage_rule') is not None:
            temp_model = main_models.IntlFlightOrderDetailResponseBodyModuleOrderItemListBaggageRule()
            self.baggage_rule = temp_model.from_map(m.get('baggage_rule'))

        self.passenger_price_list = []
        if m.get('passenger_price_list') is not None:
            for k1 in m.get('passenger_price_list'):
                temp_model = main_models.IntlFlightOrderDetailResponseBodyModuleOrderItemListPassengerPriceList()
                self.passenger_price_list.append(temp_model.from_map(k1))

        if m.get('refund_change_rule') is not None:
            temp_model = main_models.IntlFlightOrderDetailResponseBodyModuleOrderItemListRefundChangeRule()
            self.refund_change_rule = temp_model.from_map(m.get('refund_change_rule'))

        if m.get('segment_key_list') is not None:
            self.segment_key_list = m.get('segment_key_list')

        return self

class IntlFlightOrderDetailResponseBodyModuleOrderItemListRefundChangeRule(DaraModel):
    def __init__(
        self,
        cancel_fee_ind: bool = None,
        change_fee_ind: bool = None,
        change_rule_desc: str = None,
        offer_penalty_info_map: Dict[str, List[main_models.ModuleOrderItemListRefundChangeRuleOfferPenaltyInfoMapValue]] = None,
        refund_change_digest: str = None,
        refund_rule_desc: str = None,
        structured_refund: bool = None,
    ):
        self.cancel_fee_ind = cancel_fee_ind
        self.change_fee_ind = change_fee_ind
        self.change_rule_desc = change_rule_desc
        self.offer_penalty_info_map = offer_penalty_info_map
        self.refund_change_digest = refund_change_digest
        self.refund_rule_desc = refund_rule_desc
        self.structured_refund = structured_refund

    def validate(self):
        if self.offer_penalty_info_map:
            for v1 in self.offer_penalty_info_map.values():
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancel_fee_ind is not None:
            result['cancel_fee_ind'] = self.cancel_fee_ind

        if self.change_fee_ind is not None:
            result['change_fee_ind'] = self.change_fee_ind

        if self.change_rule_desc is not None:
            result['change_rule_desc'] = self.change_rule_desc

        result['offer_penalty_info_map'] = {}
        if self.offer_penalty_info_map is not None:
            for k1, v1 in self.offer_penalty_info_map.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['offer_penalty_info_map'][k1] = l1

        if self.refund_change_digest is not None:
            result['refund_change_digest'] = self.refund_change_digest

        if self.refund_rule_desc is not None:
            result['refund_rule_desc'] = self.refund_rule_desc

        if self.structured_refund is not None:
            result['structured_refund'] = self.structured_refund

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cancel_fee_ind') is not None:
            self.cancel_fee_ind = m.get('cancel_fee_ind')

        if m.get('change_fee_ind') is not None:
            self.change_fee_ind = m.get('change_fee_ind')

        if m.get('change_rule_desc') is not None:
            self.change_rule_desc = m.get('change_rule_desc')

        self.offer_penalty_info_map = {}
        if m.get('offer_penalty_info_map') is not None:
            for k1, v1 in m.get('offer_penalty_info_map').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.ModuleOrderItemListRefundChangeRuleOfferPenaltyInfoMapValue()
                    l1.append(temp_model.from_map(k2))
                self.offer_penalty_info_map[k1] = l1

        if m.get('refund_change_digest') is not None:
            self.refund_change_digest = m.get('refund_change_digest')

        if m.get('refund_rule_desc') is not None:
            self.refund_rule_desc = m.get('refund_rule_desc')

        if m.get('structured_refund') is not None:
            self.structured_refund = m.get('structured_refund')

        return self

class IntlFlightOrderDetailResponseBodyModuleOrderItemListPassengerPriceList(DaraModel):
    def __init__(
        self,
        passenger_type: int = None,
        sell_price: int = None,
        tax: int = None,
        ticket_price: int = None,
    ):
        self.passenger_type = passenger_type
        self.sell_price = sell_price
        self.tax = tax
        self.ticket_price = ticket_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_type is not None:
            result['passenger_type'] = self.passenger_type

        if self.sell_price is not None:
            result['sell_price'] = self.sell_price

        if self.tax is not None:
            result['tax'] = self.tax

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_type') is not None:
            self.passenger_type = m.get('passenger_type')

        if m.get('sell_price') is not None:
            self.sell_price = m.get('sell_price')

        if m.get('tax') is not None:
            self.tax = m.get('tax')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        return self

class IntlFlightOrderDetailResponseBodyModuleOrderItemListBaggageRule(DaraModel):
    def __init__(
        self,
        baggage_digest: str = None,
        offer_baggage_info_map: Dict[str, List[main_models.ModuleOrderItemListBaggageRuleOfferBaggageInfoMapValue]] = None,
        structured_baggage: bool = None,
    ):
        self.baggage_digest = baggage_digest
        self.offer_baggage_info_map = offer_baggage_info_map
        self.structured_baggage = structured_baggage

    def validate(self):
        if self.offer_baggage_info_map:
            for v1 in self.offer_baggage_info_map.values():
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baggage_digest is not None:
            result['baggage_digest'] = self.baggage_digest

        result['offer_baggage_info_map'] = {}
        if self.offer_baggage_info_map is not None:
            for k1, v1 in self.offer_baggage_info_map.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['offer_baggage_info_map'][k1] = l1

        if self.structured_baggage is not None:
            result['structured_baggage'] = self.structured_baggage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baggage_digest') is not None:
            self.baggage_digest = m.get('baggage_digest')

        self.offer_baggage_info_map = {}
        if m.get('offer_baggage_info_map') is not None:
            for k1, v1 in m.get('offer_baggage_info_map').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.ModuleOrderItemListBaggageRuleOfferBaggageInfoMapValue()
                    l1.append(temp_model.from_map(k2))
                self.offer_baggage_info_map[k1] = l1

        if m.get('structured_baggage') is not None:
            self.structured_baggage = m.get('structured_baggage')

        return self

class IntlFlightOrderDetailResponseBodyModuleJourneyList(DaraModel):
    def __init__(
        self,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        duration: int = None,
        flight_segment_infos: List[main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfos] = None,
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
                temp_model = main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfos()
                self.flight_segment_infos.append(temp_model.from_map(k1))

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('transfer_time') is not None:
            self.transfer_time = m.get('transfer_time')

        return self

class IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfos(DaraModel):
    def __init__(
        self,
        airline_info: main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosAirlineInfo = None,
        arr_airport_info: main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosArrAirportInfo = None,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        dep_airport_info: main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosDepAirportInfo = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        duration: int = None,
        flight_no: str = None,
        flight_share_info: main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightShareInfo = None,
        flight_size: str = None,
        flight_stop_info_list: List[main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightStopInfoList] = None,
        flight_type: str = None,
        luggage_direct_info: main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosLuggageDirectInfo = None,
        manufacturer: str = None,
        meal_desc: str = None,
        one_more: int = None,
        one_more_show: str = None,
        segment_index: int = None,
        segment_key: str = None,
        segment_visa_remark: main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosSegmentVisaRemark = None,
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
            temp_model = main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosAirlineInfo()
            self.airline_info = temp_model.from_map(m.get('airline_info'))

        if m.get('arr_airport_info') is not None:
            temp_model = main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosArrAirportInfo()
            self.arr_airport_info = temp_model.from_map(m.get('arr_airport_info'))

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_airport_info') is not None:
            temp_model = main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosDepAirportInfo()
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
            temp_model = main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightShareInfo()
            self.flight_share_info = temp_model.from_map(m.get('flight_share_info'))

        if m.get('flight_size') is not None:
            self.flight_size = m.get('flight_size')

        self.flight_stop_info_list = []
        if m.get('flight_stop_info_list') is not None:
            for k1 in m.get('flight_stop_info_list'):
                temp_model = main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightStopInfoList()
                self.flight_stop_info_list.append(temp_model.from_map(k1))

        if m.get('flight_type') is not None:
            self.flight_type = m.get('flight_type')

        if m.get('luggage_direct_info') is not None:
            temp_model = main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosLuggageDirectInfo()
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
            temp_model = main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosSegmentVisaRemark()
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

class IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosSegmentVisaRemark(DaraModel):
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

class IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosLuggageDirectInfo(DaraModel):
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

class IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightStopInfoList(DaraModel):
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

class IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightShareInfo(DaraModel):
    def __init__(
        self,
        operating_airline_info: main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightShareInfoOperatingAirlineInfo = None,
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
            temp_model = main_models.IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightShareInfoOperatingAirlineInfo()
            self.operating_airline_info = temp_model.from_map(m.get('operating_airline_info'))

        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')

        return self

class IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosFlightShareInfoOperatingAirlineInfo(DaraModel):
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

class IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosDepAirportInfo(DaraModel):
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

class IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosArrAirportInfo(DaraModel):
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

class IntlFlightOrderDetailResponseBodyModuleJourneyListFlightSegmentInfosAirlineInfo(DaraModel):
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

class IntlFlightOrderDetailResponseBodyModuleContactInfo(DaraModel):
    def __init__(
        self,
        contact_name: str = None,
    ):
        self.contact_name = contact_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_name is not None:
            result['contact_name'] = self.contact_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contact_name') is not None:
            self.contact_name = m.get('contact_name')

        return self

