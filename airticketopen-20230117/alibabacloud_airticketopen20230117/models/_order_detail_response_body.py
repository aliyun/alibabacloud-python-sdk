# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List, Dict

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class OrderDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: main_models.OrderDetailResponseBodyData = None,
        error_code: str = None,
        error_data: Any = None,
        error_msg: str = None,
        status: int = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The data returned for a successful request.
        self.data = data
        # The business error code.
        self.error_code = error_code
        # The data returned with the error.
        self.error_data = error_data
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code. The value is always 200 for successful requests.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['error_code'] = self.error_code

        if self.error_data is not None:
            result['error_data'] = self.error_data

        if self.error_msg is not None:
            result['error_msg'] = self.error_msg

        if self.status is not None:
            result['status'] = self.status

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('data') is not None:
            temp_model = main_models.OrderDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')

        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')

        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class OrderDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        ancillary_item_detail_list: List[main_models.OrderDetailResponseBodyDataAncillaryItemDetailList] = None,
        baggage_allowance_map: Dict[str, main_models.DataBaggageAllowanceMapValue] = None,
        book_time: int = None,
        flight_item_detail_list: List[main_models.OrderDetailResponseBodyDataFlightItemDetailList] = None,
        order_num: int = None,
        order_status: int = None,
        out_order_num: str = None,
        passenger_list: List[main_models.OrderDetailResponseBodyDataPassengerList] = None,
        pay_status: int = None,
        pay_time: int = None,
        promotion_price: float = None,
        real_pay_price: float = None,
        refund_change_rule_map: Dict[str, main_models.DataRefundChangeRuleMapValue] = None,
        session_nick: str = None,
        solution: main_models.OrderDetailResponseBodyDataSolution = None,
        succeed_time: int = None,
        total_price: float = None,
        transaction_no: str = None,
    ):
        # The ancillary product fulfillment details.
        self.ancillary_item_detail_list = ancillary_item_detail_list
        # The mapping of passenger types to baggage rules.
        self.baggage_allowance_map = baggage_allowance_map
        # The booking time (order creation time). The value is a 13-digit timestamp.
        self.book_time = book_time
        # The flight ticket fulfillment details.
        self.flight_item_detail_list = flight_item_detail_list
        # The order number.
        self.order_num = order_num
        # The order status. Valid values:
        # - 1: Booking in progress.
        # - 2: Booking succeeded.
        # - 3: Order paid.
        # - 4: Order succeeded.
        # - 5: Order closed.
        self.order_status = order_status
        # The external order number.
        self.out_order_num = out_order_num
        # The passenger list.
        self.passenger_list = passenger_list
        # The payment status. Valid values:
        # - 0: Initialized.
        # - 1: Created.
        # - 2: Payment succeeded.
        # - 4: Transaction closed.
        self.pay_status = pay_status
        # The payment time. The value is a 13-digit timestamp.
        self.pay_time = pay_time
        # The discount amount. Unit: CNY.
        self.promotion_price = promotion_price
        # The actual payment amount. Unit: CNY.
        self.real_pay_price = real_pay_price
        # The mapping of passenger types to refund and change rules.
        self.refund_change_rule_map = refund_change_rule_map
        # The buyer nickname.
        self.session_nick = session_nick
        # The flight information.
        self.solution = solution
        # The ticketing time. The value is a 13-digit timestamp. This parameter has a value only after ticketing is complete.
        self.succeed_time = succeed_time
        # The total order price. Unit: CNY.
        self.total_price = total_price
        # The transaction number.
        self.transaction_no = transaction_no

    def validate(self):
        if self.ancillary_item_detail_list:
            for v1 in self.ancillary_item_detail_list:
                 if v1:
                    v1.validate()
        if self.baggage_allowance_map:
            for v1 in self.baggage_allowance_map.values():
                 if v1:
                    v1.validate()
        if self.flight_item_detail_list:
            for v1 in self.flight_item_detail_list:
                 if v1:
                    v1.validate()
        if self.passenger_list:
            for v1 in self.passenger_list:
                 if v1:
                    v1.validate()
        if self.refund_change_rule_map:
            for v1 in self.refund_change_rule_map.values():
                 if v1:
                    v1.validate()
        if self.solution:
            self.solution.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ancillary_item_detail_list'] = []
        if self.ancillary_item_detail_list is not None:
            for k1 in self.ancillary_item_detail_list:
                result['ancillary_item_detail_list'].append(k1.to_map() if k1 else None)

        result['baggage_allowance_map'] = {}
        if self.baggage_allowance_map is not None:
            for k1, v1 in self.baggage_allowance_map.items():
                result['baggage_allowance_map'][k1] = v1.to_map() if v1 else None

        if self.book_time is not None:
            result['book_time'] = self.book_time

        result['flight_item_detail_list'] = []
        if self.flight_item_detail_list is not None:
            for k1 in self.flight_item_detail_list:
                result['flight_item_detail_list'].append(k1.to_map() if k1 else None)

        if self.order_num is not None:
            result['order_num'] = self.order_num

        if self.order_status is not None:
            result['order_status'] = self.order_status

        if self.out_order_num is not None:
            result['out_order_num'] = self.out_order_num

        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k1 in self.passenger_list:
                result['passenger_list'].append(k1.to_map() if k1 else None)

        if self.pay_status is not None:
            result['pay_status'] = self.pay_status

        if self.pay_time is not None:
            result['pay_time'] = self.pay_time

        if self.promotion_price is not None:
            result['promotion_price'] = self.promotion_price

        if self.real_pay_price is not None:
            result['real_pay_price'] = self.real_pay_price

        result['refund_change_rule_map'] = {}
        if self.refund_change_rule_map is not None:
            for k1, v1 in self.refund_change_rule_map.items():
                result['refund_change_rule_map'][k1] = v1.to_map() if v1 else None

        if self.session_nick is not None:
            result['session_nick'] = self.session_nick

        if self.solution is not None:
            result['solution'] = self.solution.to_map()

        if self.succeed_time is not None:
            result['succeed_time'] = self.succeed_time

        if self.total_price is not None:
            result['total_price'] = self.total_price

        if self.transaction_no is not None:
            result['transaction_no'] = self.transaction_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ancillary_item_detail_list = []
        if m.get('ancillary_item_detail_list') is not None:
            for k1 in m.get('ancillary_item_detail_list'):
                temp_model = main_models.OrderDetailResponseBodyDataAncillaryItemDetailList()
                self.ancillary_item_detail_list.append(temp_model.from_map(k1))

        self.baggage_allowance_map = {}
        if m.get('baggage_allowance_map') is not None:
            for k1, v1 in m.get('baggage_allowance_map').items():
                temp_model = main_models.DataBaggageAllowanceMapValue()
                self.baggage_allowance_map[k1] = temp_model.from_map(v1)

        if m.get('book_time') is not None:
            self.book_time = m.get('book_time')

        self.flight_item_detail_list = []
        if m.get('flight_item_detail_list') is not None:
            for k1 in m.get('flight_item_detail_list'):
                temp_model = main_models.OrderDetailResponseBodyDataFlightItemDetailList()
                self.flight_item_detail_list.append(temp_model.from_map(k1))

        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        if m.get('out_order_num') is not None:
            self.out_order_num = m.get('out_order_num')

        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k1 in m.get('passenger_list'):
                temp_model = main_models.OrderDetailResponseBodyDataPassengerList()
                self.passenger_list.append(temp_model.from_map(k1))

        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')

        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')

        if m.get('promotion_price') is not None:
            self.promotion_price = m.get('promotion_price')

        if m.get('real_pay_price') is not None:
            self.real_pay_price = m.get('real_pay_price')

        self.refund_change_rule_map = {}
        if m.get('refund_change_rule_map') is not None:
            for k1, v1 in m.get('refund_change_rule_map').items():
                temp_model = main_models.DataRefundChangeRuleMapValue()
                self.refund_change_rule_map[k1] = temp_model.from_map(v1)

        if m.get('session_nick') is not None:
            self.session_nick = m.get('session_nick')

        if m.get('solution') is not None:
            temp_model = main_models.OrderDetailResponseBodyDataSolution()
            self.solution = temp_model.from_map(m.get('solution'))

        if m.get('succeed_time') is not None:
            self.succeed_time = m.get('succeed_time')

        if m.get('total_price') is not None:
            self.total_price = m.get('total_price')

        if m.get('transaction_no') is not None:
            self.transaction_no = m.get('transaction_no')

        return self

class OrderDetailResponseBodyDataSolution(DaraModel):
    def __init__(
        self,
        adult_price: float = None,
        adult_tax: float = None,
        child_price: float = None,
        child_tax: float = None,
        infant_price: float = None,
        infant_tax: float = None,
        journey_list: List[main_models.OrderDetailResponseBodyDataSolutionJourneyList] = None,
        segment_baggage_check_in_info_list: List[main_models.OrderDetailResponseBodyDataSolutionSegmentBaggageCheckInInfoList] = None,
        segment_baggage_mapping_list: List[main_models.OrderDetailResponseBodyDataSolutionSegmentBaggageMappingList] = None,
        segment_refund_change_rule_mapping_list: List[main_models.OrderDetailResponseBodyDataSolutionSegmentRefundChangeRuleMappingList] = None,
        solution_attribute: main_models.OrderDetailResponseBodyDataSolutionSolutionAttribute = None,
        solution_id: str = None,
    ):
        # The unit price for an adult.
        self.adult_price = adult_price
        # The tax for an adult.
        self.adult_tax = adult_tax
        # The unit price for a child.
        self.child_price = child_price
        # The tax for a child.
        self.child_tax = child_tax
        # The unit price for an infant.
        self.infant_price = infant_price
        # The tax for an infant.
        self.infant_tax = infant_tax
        # The journey list.
        self.journey_list = journey_list
        # The baggage through-check rules.
        self.segment_baggage_check_in_info_list = segment_baggage_check_in_info_list
        # The complimentary baggage rules.
        self.segment_baggage_mapping_list = segment_baggage_mapping_list
        # The refund and change rules.
        self.segment_refund_change_rule_mapping_list = segment_refund_change_rule_mapping_list
        self.solution_attribute = solution_attribute
        # solution_id
        self.solution_id = solution_id

    def validate(self):
        if self.journey_list:
            for v1 in self.journey_list:
                 if v1:
                    v1.validate()
        if self.segment_baggage_check_in_info_list:
            for v1 in self.segment_baggage_check_in_info_list:
                 if v1:
                    v1.validate()
        if self.segment_baggage_mapping_list:
            for v1 in self.segment_baggage_mapping_list:
                 if v1:
                    v1.validate()
        if self.segment_refund_change_rule_mapping_list:
            for v1 in self.segment_refund_change_rule_mapping_list:
                 if v1:
                    v1.validate()
        if self.solution_attribute:
            self.solution_attribute.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adult_price is not None:
            result['adult_price'] = self.adult_price

        if self.adult_tax is not None:
            result['adult_tax'] = self.adult_tax

        if self.child_price is not None:
            result['child_price'] = self.child_price

        if self.child_tax is not None:
            result['child_tax'] = self.child_tax

        if self.infant_price is not None:
            result['infant_price'] = self.infant_price

        if self.infant_tax is not None:
            result['infant_tax'] = self.infant_tax

        result['journey_list'] = []
        if self.journey_list is not None:
            for k1 in self.journey_list:
                result['journey_list'].append(k1.to_map() if k1 else None)

        result['segment_baggage_check_in_info_list'] = []
        if self.segment_baggage_check_in_info_list is not None:
            for k1 in self.segment_baggage_check_in_info_list:
                result['segment_baggage_check_in_info_list'].append(k1.to_map() if k1 else None)

        result['segment_baggage_mapping_list'] = []
        if self.segment_baggage_mapping_list is not None:
            for k1 in self.segment_baggage_mapping_list:
                result['segment_baggage_mapping_list'].append(k1.to_map() if k1 else None)

        result['segment_refund_change_rule_mapping_list'] = []
        if self.segment_refund_change_rule_mapping_list is not None:
            for k1 in self.segment_refund_change_rule_mapping_list:
                result['segment_refund_change_rule_mapping_list'].append(k1.to_map() if k1 else None)

        if self.solution_attribute is not None:
            result['solution_attribute'] = self.solution_attribute.to_map()

        if self.solution_id is not None:
            result['solution_id'] = self.solution_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adult_price') is not None:
            self.adult_price = m.get('adult_price')

        if m.get('adult_tax') is not None:
            self.adult_tax = m.get('adult_tax')

        if m.get('child_price') is not None:
            self.child_price = m.get('child_price')

        if m.get('child_tax') is not None:
            self.child_tax = m.get('child_tax')

        if m.get('infant_price') is not None:
            self.infant_price = m.get('infant_price')

        if m.get('infant_tax') is not None:
            self.infant_tax = m.get('infant_tax')

        self.journey_list = []
        if m.get('journey_list') is not None:
            for k1 in m.get('journey_list'):
                temp_model = main_models.OrderDetailResponseBodyDataSolutionJourneyList()
                self.journey_list.append(temp_model.from_map(k1))

        self.segment_baggage_check_in_info_list = []
        if m.get('segment_baggage_check_in_info_list') is not None:
            for k1 in m.get('segment_baggage_check_in_info_list'):
                temp_model = main_models.OrderDetailResponseBodyDataSolutionSegmentBaggageCheckInInfoList()
                self.segment_baggage_check_in_info_list.append(temp_model.from_map(k1))

        self.segment_baggage_mapping_list = []
        if m.get('segment_baggage_mapping_list') is not None:
            for k1 in m.get('segment_baggage_mapping_list'):
                temp_model = main_models.OrderDetailResponseBodyDataSolutionSegmentBaggageMappingList()
                self.segment_baggage_mapping_list.append(temp_model.from_map(k1))

        self.segment_refund_change_rule_mapping_list = []
        if m.get('segment_refund_change_rule_mapping_list') is not None:
            for k1 in m.get('segment_refund_change_rule_mapping_list'):
                temp_model = main_models.OrderDetailResponseBodyDataSolutionSegmentRefundChangeRuleMappingList()
                self.segment_refund_change_rule_mapping_list.append(temp_model.from_map(k1))

        if m.get('solution_attribute') is not None:
            temp_model = main_models.OrderDetailResponseBodyDataSolutionSolutionAttribute()
            self.solution_attribute = temp_model.from_map(m.get('solution_attribute'))

        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')

        return self

class OrderDetailResponseBodyDataSolutionSolutionAttribute(DaraModel):
    def __init__(
        self,
        issue_time_info: main_models.OrderDetailResponseBodyDataSolutionSolutionAttributeIssueTimeInfo = None,
        supply_source_type: str = None,
    ):
        self.issue_time_info = issue_time_info
        self.supply_source_type = supply_source_type

    def validate(self):
        if self.issue_time_info:
            self.issue_time_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.issue_time_info is not None:
            result['issue_time_info'] = self.issue_time_info.to_map()

        if self.supply_source_type is not None:
            result['supply_source_type'] = self.supply_source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('issue_time_info') is not None:
            temp_model = main_models.OrderDetailResponseBodyDataSolutionSolutionAttributeIssueTimeInfo()
            self.issue_time_info = temp_model.from_map(m.get('issue_time_info'))

        if m.get('supply_source_type') is not None:
            self.supply_source_type = m.get('supply_source_type')

        return self

class OrderDetailResponseBodyDataSolutionSolutionAttributeIssueTimeInfo(DaraModel):
    def __init__(
        self,
        issue_ticket_type: int = None,
        issue_time_limit: int = None,
    ):
        self.issue_ticket_type = issue_ticket_type
        self.issue_time_limit = issue_time_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.issue_ticket_type is not None:
            result['issue_ticket_type'] = self.issue_ticket_type

        if self.issue_time_limit is not None:
            result['issue_time_limit'] = self.issue_time_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('issue_ticket_type') is not None:
            self.issue_ticket_type = m.get('issue_ticket_type')

        if m.get('issue_time_limit') is not None:
            self.issue_time_limit = m.get('issue_time_limit')

        return self

class OrderDetailResponseBodyDataSolutionSegmentRefundChangeRuleMappingList(DaraModel):
    def __init__(
        self,
        refund_change_rule_map: Dict[str, main_models.DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue] = None,
        segment_id_list: List[str] = None,
    ):
        # The mapping of passenger types to refund and change rules.
        self.refund_change_rule_map = refund_change_rule_map
        # The list of segment IDs. These segments share the same refund and change rule.
        self.segment_id_list = segment_id_list

    def validate(self):
        if self.refund_change_rule_map:
            for v1 in self.refund_change_rule_map.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['refund_change_rule_map'] = {}
        if self.refund_change_rule_map is not None:
            for k1, v1 in self.refund_change_rule_map.items():
                result['refund_change_rule_map'][k1] = v1.to_map() if v1 else None

        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.refund_change_rule_map = {}
        if m.get('refund_change_rule_map') is not None:
            for k1, v1 in m.get('refund_change_rule_map').items():
                temp_model = main_models.DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue()
                self.refund_change_rule_map[k1] = temp_model.from_map(v1)

        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')

        return self

class OrderDetailResponseBodyDataSolutionSegmentBaggageMappingList(DaraModel):
    def __init__(
        self,
        passenger_baggage_allowance_mapping: Dict[str, main_models.DataSolutionSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue] = None,
        segment_id_list: List[str] = None,
    ):
        # The mapping of passenger types to complimentary baggage allowances.
        self.passenger_baggage_allowance_mapping = passenger_baggage_allowance_mapping
        # The list of segment IDs. These segments share the same complimentary baggage rule.
        self.segment_id_list = segment_id_list

    def validate(self):
        if self.passenger_baggage_allowance_mapping:
            for v1 in self.passenger_baggage_allowance_mapping.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['passenger_baggage_allowance_mapping'] = {}
        if self.passenger_baggage_allowance_mapping is not None:
            for k1, v1 in self.passenger_baggage_allowance_mapping.items():
                result['passenger_baggage_allowance_mapping'][k1] = v1.to_map() if v1 else None

        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.passenger_baggage_allowance_mapping = {}
        if m.get('passenger_baggage_allowance_mapping') is not None:
            for k1, v1 in m.get('passenger_baggage_allowance_mapping').items():
                temp_model = main_models.DataSolutionSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue()
                self.passenger_baggage_allowance_mapping[k1] = temp_model.from_map(v1)

        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')

        return self

class OrderDetailResponseBodyDataSolutionSegmentBaggageCheckInInfoList(DaraModel):
    def __init__(
        self,
        luggage_direct_info_type: int = None,
        segment_id_list: List[str] = None,
    ):
        # The baggage through-check rule type. Valid values:
        # - 1: baggage is checked through between segments.
        # - 2: baggage must be rechecked between segments.
        # - 3: baggage is checked through at stopover cities.
        # - 4: baggage must be rechecked at stopover cities.
        self.luggage_direct_info_type = luggage_direct_info_type
        # The list of segment IDs. These segments share the same baggage through-check rule.
        self.segment_id_list = segment_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.luggage_direct_info_type is not None:
            result['luggage_direct_info_type'] = self.luggage_direct_info_type

        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('luggage_direct_info_type') is not None:
            self.luggage_direct_info_type = m.get('luggage_direct_info_type')

        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')

        return self

class OrderDetailResponseBodyDataSolutionJourneyList(DaraModel):
    def __init__(
        self,
        segment_list: List[main_models.OrderDetailResponseBodyDataSolutionJourneyListSegmentList] = None,
        transfer_count: int = None,
    ):
        # The segment information.
        self.segment_list = segment_list
        # The number of transfers.
        self.transfer_count = transfer_count

    def validate(self):
        if self.segment_list:
            for v1 in self.segment_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['segment_list'] = []
        if self.segment_list is not None:
            for k1 in self.segment_list:
                result['segment_list'].append(k1.to_map() if k1 else None)

        if self.transfer_count is not None:
            result['transfer_count'] = self.transfer_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k1 in m.get('segment_list'):
                temp_model = main_models.OrderDetailResponseBodyDataSolutionJourneyListSegmentList()
                self.segment_list.append(temp_model.from_map(k1))

        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')

        return self

class OrderDetailResponseBodyDataSolutionJourneyListSegmentList(DaraModel):
    def __init__(
        self,
        arrival_airport: str = None,
        arrival_city: str = None,
        arrival_terminal: str = None,
        arrival_time: str = None,
        availability: str = None,
        cabin: str = None,
        cabin_class: str = None,
        code_share: bool = None,
        departure_airport: str = None,
        departure_city: str = None,
        departure_terminal: str = None,
        departure_time: str = None,
        equip_type: str = None,
        flight_duration: int = None,
        marketing_airline: str = None,
        marketing_flight_no: str = None,
        marketing_flight_no_int: int = None,
        operating_airline: str = None,
        operating_flight_no: str = None,
        segment_id: str = None,
        stop_city_list: str = None,
        stop_quantity: int = None,
    ):
        # The three-letter IATA code of the arrival airport (uppercase).
        self.arrival_airport = arrival_airport
        # The three-letter IATA code of the arrival city (uppercase).
        self.arrival_city = arrival_city
        # The arrival terminal.
        self.arrival_terminal = arrival_terminal
        # The arrival date and time in string format (yyyy-MM-dd HH:mm:ss).
        self.arrival_time = arrival_time
        # The number of remaining seats.
        self.availability = availability
        # The cabin.
        self.cabin = cabin
        # The cabin class.
        self.cabin_class = cabin_class
        # Indicates whether the flight is a codeshare flight.
        self.code_share = code_share
        # The three-letter IATA code of the departure airport (uppercase).
        self.departure_airport = departure_airport
        # The three-letter IATA code of the departure city (uppercase).
        self.departure_city = departure_city
        # The departure terminal.
        self.departure_terminal = departure_terminal
        # The departure date and time in string format (yyyy-MM-dd HH:mm:ss).
        self.departure_time = departure_time
        # The aircraft type.
        self.equip_type = equip_type
        # The flight duration. Unit: minutes.
        self.flight_duration = flight_duration
        # The marketing airline code (for example, HO).
        self.marketing_airline = marketing_airline
        # The marketing flight number (for example, HO1295).
        self.marketing_flight_no = marketing_flight_no
        # The numeric marketing flight number (for example, 1295).
        self.marketing_flight_no_int = marketing_flight_no_int
        # The operating airline code (for example, CX).
        self.operating_airline = operating_airline
        # The operating flight number (for example, CX601).
        self.operating_flight_no = operating_flight_no
        # The segment ID. Format: flight number + departure airport + arrival airport + departure date (MMdd).
        self.segment_id = segment_id
        # The list of stopover cities. This parameter has a value when stopQuantity is greater than 0. Multiple cities are separated by commas.
        self.stop_city_list = stop_city_list
        # The number of stopover cities.
        self.stop_quantity = stop_quantity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport

        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city

        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal

        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time

        if self.availability is not None:
            result['availability'] = self.availability

        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.code_share is not None:
            result['code_share'] = self.code_share

        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport

        if self.departure_city is not None:
            result['departure_city'] = self.departure_city

        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal

        if self.departure_time is not None:
            result['departure_time'] = self.departure_time

        if self.equip_type is not None:
            result['equip_type'] = self.equip_type

        if self.flight_duration is not None:
            result['flight_duration'] = self.flight_duration

        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline

        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no

        if self.marketing_flight_no_int is not None:
            result['marketing_flight_no_int'] = self.marketing_flight_no_int

        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline

        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no

        if self.segment_id is not None:
            result['segment_id'] = self.segment_id

        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list

        if self.stop_quantity is not None:
            result['stop_quantity'] = self.stop_quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')

        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')

        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')

        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')

        if m.get('availability') is not None:
            self.availability = m.get('availability')

        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')

        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')

        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')

        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')

        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')

        if m.get('equip_type') is not None:
            self.equip_type = m.get('equip_type')

        if m.get('flight_duration') is not None:
            self.flight_duration = m.get('flight_duration')

        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')

        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')

        if m.get('marketing_flight_no_int') is not None:
            self.marketing_flight_no_int = m.get('marketing_flight_no_int')

        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')

        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')

        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')

        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')

        if m.get('stop_quantity') is not None:
            self.stop_quantity = m.get('stop_quantity')

        return self

class OrderDetailResponseBodyDataPassengerList(DaraModel):
    def __init__(
        self,
        birthday: str = None,
        credential: main_models.OrderDetailResponseBodyDataPassengerListCredential = None,
        first_name: str = None,
        gender: int = None,
        last_name: str = None,
        mobile_country_code: str = None,
        mobile_phone_number: str = None,
        nationality: str = None,
        type: int = None,
    ):
        # The date of birth in yyyyMMdd format.
        self.birthday = birthday
        # The credential information.
        self.credential = credential
        # The first name.
        self.first_name = first_name
        # The gender. Valid values:
        # - 0: MALE.
        # - 1: FEMALE.
        self.gender = gender
        # The last name.
        self.last_name = last_name
        # The country code of the mobile phone number.
        self.mobile_country_code = mobile_country_code
        # The mobile phone number.
        self.mobile_phone_number = mobile_phone_number
        # The two-letter nationality code.
        self.nationality = nationality
        # The passenger type. Valid values:
        # - 0: adult.
        # - 1: child.
        # - 8: infant.
        self.type = type

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birthday is not None:
            result['birthday'] = self.birthday

        if self.credential is not None:
            result['credential'] = self.credential.to_map()

        if self.first_name is not None:
            result['first_name'] = self.first_name

        if self.gender is not None:
            result['gender'] = self.gender

        if self.last_name is not None:
            result['last_name'] = self.last_name

        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code

        if self.mobile_phone_number is not None:
            result['mobile_phone_number'] = self.mobile_phone_number

        if self.nationality is not None:
            result['nationality'] = self.nationality

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        if m.get('credential') is not None:
            temp_model = main_models.OrderDetailResponseBodyDataPassengerListCredential()
            self.credential = temp_model.from_map(m.get('credential'))

        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')

        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')

        if m.get('mobile_phone_number') is not None:
            self.mobile_phone_number = m.get('mobile_phone_number')

        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class OrderDetailResponseBodyDataPassengerListCredential(DaraModel):
    def __init__(
        self,
        cert_issue_place: str = None,
        credential_num: str = None,
        credential_type: int = None,
        expire_date: str = None,
    ):
        # The place of issuance, represented as a two-letter code.
        self.cert_issue_place = cert_issue_place
        # The credential number.
        self.credential_num = credential_num
        # The credential type. Valid values:
        # - 0: ID card.
        # - 1: passport.
        # - 4: Home Return Permit.
        # - 5: Mainland Travel Permit for Taiwan Residents.
        # - 6: Exit-Entry Permit for Hong Kong and Macao Residents.
        # - 12: Taiwan Travel Permit.
        # - 19: no credential.
        self.credential_type = credential_type
        # The credential expiration date.
        self.expire_date = expire_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_issue_place is not None:
            result['cert_issue_place'] = self.cert_issue_place

        if self.credential_num is not None:
            result['credential_num'] = self.credential_num

        if self.credential_type is not None:
            result['credential_type'] = self.credential_type

        if self.expire_date is not None:
            result['expire_date'] = self.expire_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_issue_place') is not None:
            self.cert_issue_place = m.get('cert_issue_place')

        if m.get('credential_num') is not None:
            self.credential_num = m.get('credential_num')

        if m.get('credential_type') is not None:
            self.credential_type = m.get('credential_type')

        if m.get('expire_date') is not None:
            self.expire_date = m.get('expire_date')

        return self

class OrderDetailResponseBodyDataFlightItemDetailList(DaraModel):
    def __init__(
        self,
        b_pnr_list: List[str] = None,
        c_pnr_list: List[str] = None,
        flight_price: main_models.OrderDetailResponseBodyDataFlightItemDetailListFlightPrice = None,
        flight_segment_cabin_relation: List[main_models.OrderDetailResponseBodyDataFlightItemDetailListFlightSegmentCabinRelation] = None,
        passenger: main_models.OrderDetailResponseBodyDataFlightItemDetailListPassenger = None,
        ticket_air_line: str = None,
        ticket_nos: List[str] = None,
    ):
        # The list of bPnr values.
        self.b_pnr_list = b_pnr_list
        # The list of cPnr values.
        self.c_pnr_list = c_pnr_list
        # The passenger price information.
        self.flight_price = flight_price
        # The list of segment-cabin information.
        self.flight_segment_cabin_relation = flight_segment_cabin_relation
        # The passenger information.
        self.passenger = passenger
        # The ticketing airline. Multiple ticketing airlines may be concatenated.
        self.ticket_air_line = ticket_air_line
        # The list of ticket numbers.
        self.ticket_nos = ticket_nos

    def validate(self):
        if self.flight_price:
            self.flight_price.validate()
        if self.flight_segment_cabin_relation:
            for v1 in self.flight_segment_cabin_relation:
                 if v1:
                    v1.validate()
        if self.passenger:
            self.passenger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b_pnr_list is not None:
            result['b_pnr_list'] = self.b_pnr_list

        if self.c_pnr_list is not None:
            result['c_pnr_list'] = self.c_pnr_list

        if self.flight_price is not None:
            result['flight_price'] = self.flight_price.to_map()

        result['flight_segment_cabin_relation'] = []
        if self.flight_segment_cabin_relation is not None:
            for k1 in self.flight_segment_cabin_relation:
                result['flight_segment_cabin_relation'].append(k1.to_map() if k1 else None)

        if self.passenger is not None:
            result['passenger'] = self.passenger.to_map()

        if self.ticket_air_line is not None:
            result['ticket_air_line'] = self.ticket_air_line

        if self.ticket_nos is not None:
            result['ticket_nos'] = self.ticket_nos

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('b_pnr_list') is not None:
            self.b_pnr_list = m.get('b_pnr_list')

        if m.get('c_pnr_list') is not None:
            self.c_pnr_list = m.get('c_pnr_list')

        if m.get('flight_price') is not None:
            temp_model = main_models.OrderDetailResponseBodyDataFlightItemDetailListFlightPrice()
            self.flight_price = temp_model.from_map(m.get('flight_price'))

        self.flight_segment_cabin_relation = []
        if m.get('flight_segment_cabin_relation') is not None:
            for k1 in m.get('flight_segment_cabin_relation'):
                temp_model = main_models.OrderDetailResponseBodyDataFlightItemDetailListFlightSegmentCabinRelation()
                self.flight_segment_cabin_relation.append(temp_model.from_map(k1))

        if m.get('passenger') is not None:
            temp_model = main_models.OrderDetailResponseBodyDataFlightItemDetailListPassenger()
            self.passenger = temp_model.from_map(m.get('passenger'))

        if m.get('ticket_air_line') is not None:
            self.ticket_air_line = m.get('ticket_air_line')

        if m.get('ticket_nos') is not None:
            self.ticket_nos = m.get('ticket_nos')

        return self

class OrderDetailResponseBodyDataFlightItemDetailListPassenger(DaraModel):
    def __init__(
        self,
        birthday: str = None,
        credential: main_models.OrderDetailResponseBodyDataFlightItemDetailListPassengerCredential = None,
        first_name: str = None,
        gender: int = None,
        last_name: str = None,
        mobile_country_code: str = None,
        mobile_phone_number: str = None,
        nationality: str = None,
        type: int = None,
    ):
        # The date of birth in yyyyMMdd format.
        self.birthday = birthday
        # The credential information.
        self.credential = credential
        # The first name.
        self.first_name = first_name
        # The gender. Valid values:
        # - 0: MALE.
        # - 1: FEMALE.
        self.gender = gender
        # The last name.
        self.last_name = last_name
        # The country code of the mobile phone number.
        self.mobile_country_code = mobile_country_code
        # The mobile phone number.
        self.mobile_phone_number = mobile_phone_number
        # The two-letter nationality code.
        self.nationality = nationality
        # The passenger type. Valid values:
        # - 0: adult.
        # - 1: child.
        # - 8: infant.
        self.type = type

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birthday is not None:
            result['birthday'] = self.birthday

        if self.credential is not None:
            result['credential'] = self.credential.to_map()

        if self.first_name is not None:
            result['first_name'] = self.first_name

        if self.gender is not None:
            result['gender'] = self.gender

        if self.last_name is not None:
            result['last_name'] = self.last_name

        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code

        if self.mobile_phone_number is not None:
            result['mobile_phone_number'] = self.mobile_phone_number

        if self.nationality is not None:
            result['nationality'] = self.nationality

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        if m.get('credential') is not None:
            temp_model = main_models.OrderDetailResponseBodyDataFlightItemDetailListPassengerCredential()
            self.credential = temp_model.from_map(m.get('credential'))

        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')

        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')

        if m.get('mobile_phone_number') is not None:
            self.mobile_phone_number = m.get('mobile_phone_number')

        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class OrderDetailResponseBodyDataFlightItemDetailListPassengerCredential(DaraModel):
    def __init__(
        self,
        cert_issue_place: str = None,
        credential_num: str = None,
        credential_type: int = None,
        expire_date: str = None,
    ):
        # The place of issuance, represented as a two-letter code.
        self.cert_issue_place = cert_issue_place
        # The credential number.
        self.credential_num = credential_num
        # The credential type. Valid values:
        # - 0: ID card.
        # - 1: passport.
        # - 4: Home Return Permit.
        # - 5: Mainland Travel Permit for Taiwan Residents.
        # - 6: Exit-Entry Permit for Hong Kong and Macao Residents.
        # - 12: Taiwan Travel Permit.
        # - 19: no credential.
        self.credential_type = credential_type
        # The credential expiration date.
        self.expire_date = expire_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_issue_place is not None:
            result['cert_issue_place'] = self.cert_issue_place

        if self.credential_num is not None:
            result['credential_num'] = self.credential_num

        if self.credential_type is not None:
            result['credential_type'] = self.credential_type

        if self.expire_date is not None:
            result['expire_date'] = self.expire_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_issue_place') is not None:
            self.cert_issue_place = m.get('cert_issue_place')

        if m.get('credential_num') is not None:
            self.credential_num = m.get('credential_num')

        if m.get('credential_type') is not None:
            self.credential_type = m.get('credential_type')

        if m.get('expire_date') is not None:
            self.expire_date = m.get('expire_date')

        return self

class OrderDetailResponseBodyDataFlightItemDetailListFlightSegmentCabinRelation(DaraModel):
    def __init__(
        self,
        cabin: str = None,
        cabin_class: str = None,
        cabin_class_name: str = None,
        cabin_quantity: str = None,
        segment_id: str = None,
    ):
        # The cabin.
        self.cabin = cabin
        # The cabin class.
        self.cabin_class = cabin_class
        # The cabin class description.
        self.cabin_class_name = cabin_class_name
        # The number of available tickets.
        self.cabin_quantity = cabin_quantity
        # The segment ID.
        self.segment_id = segment_id

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

        if self.cabin_class_name is not None:
            result['cabin_class_name'] = self.cabin_class_name

        if self.cabin_quantity is not None:
            result['cabin_quantity'] = self.cabin_quantity

        if self.segment_id is not None:
            result['segment_id'] = self.segment_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('cabin_class_name') is not None:
            self.cabin_class_name = m.get('cabin_class_name')

        if m.get('cabin_quantity') is not None:
            self.cabin_quantity = m.get('cabin_quantity')

        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')

        return self

class OrderDetailResponseBodyDataFlightItemDetailListFlightPrice(DaraModel):
    def __init__(
        self,
        sell_price: float = None,
        tax: float = None,
    ):
        # The selling price. Unit: CNY.
        self.sell_price = sell_price
        # The tax.
        self.tax = tax

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sell_price') is not None:
            self.sell_price = m.get('sell_price')

        if m.get('tax') is not None:
            self.tax = m.get('tax')

        return self

class OrderDetailResponseBodyDataAncillaryItemDetailList(DaraModel):
    def __init__(
        self,
        ancillary: main_models.OrderDetailResponseBodyDataAncillaryItemDetailListAncillary = None,
        passenger: main_models.OrderDetailResponseBodyDataAncillaryItemDetailListPassenger = None,
        segment_id_list: List[str] = None,
    ):
        # The ancillary product details.
        self.ancillary = ancillary
        # The passenger information.
        self.passenger = passenger
        # The segment IDs to which the ancillary product applies.
        self.segment_id_list = segment_id_list

    def validate(self):
        if self.ancillary:
            self.ancillary.validate()
        if self.passenger:
            self.passenger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ancillary is not None:
            result['ancillary'] = self.ancillary.to_map()

        if self.passenger is not None:
            result['passenger'] = self.passenger.to_map()

        if self.segment_id_list is not None:
            result['segment_id_list'] = self.segment_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ancillary') is not None:
            temp_model = main_models.OrderDetailResponseBodyDataAncillaryItemDetailListAncillary()
            self.ancillary = temp_model.from_map(m.get('ancillary'))

        if m.get('passenger') is not None:
            temp_model = main_models.OrderDetailResponseBodyDataAncillaryItemDetailListPassenger()
            self.passenger = temp_model.from_map(m.get('passenger'))

        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')

        return self

class OrderDetailResponseBodyDataAncillaryItemDetailListPassenger(DaraModel):
    def __init__(
        self,
        birthday: str = None,
        credential: main_models.OrderDetailResponseBodyDataAncillaryItemDetailListPassengerCredential = None,
        first_name: str = None,
        gender: int = None,
        last_name: str = None,
        mobile_country_code: str = None,
        mobile_phone_number: str = None,
        nationality: str = None,
        type: int = None,
    ):
        # The date of birth in yyyyMMdd format.
        self.birthday = birthday
        # The credential information.
        self.credential = credential
        # The first name.
        self.first_name = first_name
        # The gender. Valid values:
        # - 0: MALE.
        # - 1: FEMALE.
        self.gender = gender
        # The last name.
        self.last_name = last_name
        # The country code of the mobile phone number.
        self.mobile_country_code = mobile_country_code
        # The mobile phone number.
        self.mobile_phone_number = mobile_phone_number
        # The two-letter nationality code.
        self.nationality = nationality
        # The passenger type. Valid values:
        # - 0: adult.
        # - 1: child.
        # - 8: infant.
        self.type = type

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birthday is not None:
            result['birthday'] = self.birthday

        if self.credential is not None:
            result['credential'] = self.credential.to_map()

        if self.first_name is not None:
            result['first_name'] = self.first_name

        if self.gender is not None:
            result['gender'] = self.gender

        if self.last_name is not None:
            result['last_name'] = self.last_name

        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code

        if self.mobile_phone_number is not None:
            result['mobile_phone_number'] = self.mobile_phone_number

        if self.nationality is not None:
            result['nationality'] = self.nationality

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        if m.get('credential') is not None:
            temp_model = main_models.OrderDetailResponseBodyDataAncillaryItemDetailListPassengerCredential()
            self.credential = temp_model.from_map(m.get('credential'))

        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')

        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')

        if m.get('mobile_phone_number') is not None:
            self.mobile_phone_number = m.get('mobile_phone_number')

        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class OrderDetailResponseBodyDataAncillaryItemDetailListPassengerCredential(DaraModel):
    def __init__(
        self,
        cert_issue_place: str = None,
        credential_num: str = None,
        credential_type: int = None,
        expire_date: str = None,
    ):
        # The place of issuance, represented as a two-letter code.
        self.cert_issue_place = cert_issue_place
        # The credential number.
        self.credential_num = credential_num
        # The credential type. Valid values:
        # - 0: ID card.
        # - 1: passport.
        # - 4: Home Return Permit.
        # - 5: Mainland Travel Permit for Taiwan Residents.
        # - 6: Exit-Entry Permit for Hong Kong and Macao Residents.
        # - 12: Taiwan Travel Permit.
        # - 19: no credential.
        self.credential_type = credential_type
        # The credential expiration date.
        self.expire_date = expire_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_issue_place is not None:
            result['cert_issue_place'] = self.cert_issue_place

        if self.credential_num is not None:
            result['credential_num'] = self.credential_num

        if self.credential_type is not None:
            result['credential_type'] = self.credential_type

        if self.expire_date is not None:
            result['expire_date'] = self.expire_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_issue_place') is not None:
            self.cert_issue_place = m.get('cert_issue_place')

        if m.get('credential_num') is not None:
            self.credential_num = m.get('credential_num')

        if m.get('credential_type') is not None:
            self.credential_type = m.get('credential_type')

        if m.get('expire_date') is not None:
            self.expire_date = m.get('expire_date')

        return self

class OrderDetailResponseBodyDataAncillaryItemDetailListAncillary(DaraModel):
    def __init__(
        self,
        ancillary_id: str = None,
        ancillary_type: int = None,
        baggage_ancillary: main_models.OrderDetailResponseBodyDataAncillaryItemDetailListAncillaryBaggageAncillary = None,
    ):
        # The ancillary product ID.
        self.ancillary_id = ancillary_id
        # The ancillary product type. Currently supported value: 4 (paid baggage).
        self.ancillary_type = ancillary_type
        # The baggage ancillary details.
        self.baggage_ancillary = baggage_ancillary

    def validate(self):
        if self.baggage_ancillary:
            self.baggage_ancillary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ancillary_id is not None:
            result['ancillary_id'] = self.ancillary_id

        if self.ancillary_type is not None:
            result['ancillary_type'] = self.ancillary_type

        if self.baggage_ancillary is not None:
            result['baggage_ancillary'] = self.baggage_ancillary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ancillary_id') is not None:
            self.ancillary_id = m.get('ancillary_id')

        if m.get('ancillary_type') is not None:
            self.ancillary_type = m.get('ancillary_type')

        if m.get('baggage_ancillary') is not None:
            temp_model = main_models.OrderDetailResponseBodyDataAncillaryItemDetailListAncillaryBaggageAncillary()
            self.baggage_ancillary = temp_model.from_map(m.get('baggage_ancillary'))

        return self

class OrderDetailResponseBodyDataAncillaryItemDetailListAncillaryBaggageAncillary(DaraModel):
    def __init__(
        self,
        baggage_amount: int = None,
        baggage_weight: int = None,
        baggage_weight_unit: str = None,
        is_all_weight: bool = None,
        price: float = None,
    ):
        # The number of baggage pieces. Valid values: 3, 2, 1, 0, and -2. A value of -2 indicates weight-based calculation.
        self.baggage_amount = baggage_amount
        # The baggage weight, ranging from 0 to 50. When isAllWeight is set to true, this value represents the total weight of all pieces.
        self.baggage_weight = baggage_weight
        # The baggage weight unit.
        self.baggage_weight_unit = baggage_weight_unit
        # Indicates whether the weight represents the total weight of all baggage pieces.
        self.is_all_weight = is_all_weight
        # The total price.
        self.price = price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baggage_amount is not None:
            result['baggage_amount'] = self.baggage_amount

        if self.baggage_weight is not None:
            result['baggage_weight'] = self.baggage_weight

        if self.baggage_weight_unit is not None:
            result['baggage_weight_unit'] = self.baggage_weight_unit

        if self.is_all_weight is not None:
            result['is_all_weight'] = self.is_all_weight

        if self.price is not None:
            result['price'] = self.price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baggage_amount') is not None:
            self.baggage_amount = m.get('baggage_amount')

        if m.get('baggage_weight') is not None:
            self.baggage_weight = m.get('baggage_weight')

        if m.get('baggage_weight_unit') is not None:
            self.baggage_weight_unit = m.get('baggage_weight_unit')

        if m.get('is_all_weight') is not None:
            self.is_all_weight = m.get('is_all_weight')

        if m.get('price') is not None:
            self.price = m.get('price')

        return self

