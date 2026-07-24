# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List, Dict

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class PricingResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: main_models.PricingResponseBodyData = None,
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
        # The HTTP status code. The value is always 200 for successful HTTP requests.
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
            temp_model = main_models.PricingResponseBodyData()
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

class PricingResponseBodyData(DaraModel):
    def __init__(
        self,
        changed_price_info: main_models.PricingResponseBodyDataChangedPriceInfo = None,
        is_changed: bool = None,
        original_price_info: main_models.PricingResponseBodyDataOriginalPriceInfo = None,
        remain_seats: str = None,
        solution: main_models.PricingResponseBodyDataSolution = None,
    ):
        # The price information after the price change.
        self.changed_price_info = changed_price_info
        # Indicates whether the price has changed.
        self.is_changed = is_changed
        # The price information before the price change. This field has a value only when isChanged is true.
        self.original_price_info = original_price_info
        # The number of remaining seats. A indicates more than 9. Values 0 through 9 represent the exact number.
        self.remain_seats = remain_seats
        # solution
        self.solution = solution

    def validate(self):
        if self.changed_price_info:
            self.changed_price_info.validate()
        if self.original_price_info:
            self.original_price_info.validate()
        if self.solution:
            self.solution.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.changed_price_info is not None:
            result['changed_price_info'] = self.changed_price_info.to_map()

        if self.is_changed is not None:
            result['is_changed'] = self.is_changed

        if self.original_price_info is not None:
            result['original_price_info'] = self.original_price_info.to_map()

        if self.remain_seats is not None:
            result['remain_seats'] = self.remain_seats

        if self.solution is not None:
            result['solution'] = self.solution.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('changed_price_info') is not None:
            temp_model = main_models.PricingResponseBodyDataChangedPriceInfo()
            self.changed_price_info = temp_model.from_map(m.get('changed_price_info'))

        if m.get('is_changed') is not None:
            self.is_changed = m.get('is_changed')

        if m.get('original_price_info') is not None:
            temp_model = main_models.PricingResponseBodyDataOriginalPriceInfo()
            self.original_price_info = temp_model.from_map(m.get('original_price_info'))

        if m.get('remain_seats') is not None:
            self.remain_seats = m.get('remain_seats')

        if m.get('solution') is not None:
            temp_model = main_models.PricingResponseBodyDataSolution()
            self.solution = temp_model.from_map(m.get('solution'))

        return self

class PricingResponseBodyDataSolution(DaraModel):
    def __init__(
        self,
        adult_price: float = None,
        adult_tax: float = None,
        child_price: float = None,
        child_tax: float = None,
        infant_price: float = None,
        infant_tax: float = None,
        journey_list: List[main_models.PricingResponseBodyDataSolutionJourneyList] = None,
        segment_baggage_check_in_info_list: List[main_models.PricingResponseBodyDataSolutionSegmentBaggageCheckInInfoList] = None,
        segment_baggage_mapping_list: List[main_models.PricingResponseBodyDataSolutionSegmentBaggageMappingList] = None,
        segment_refund_change_rule_mapping_list: List[main_models.PricingResponseBodyDataSolutionSegmentRefundChangeRuleMappingList] = None,
        solution_attribute: main_models.PricingResponseBodyDataSolutionSolutionAttribute = None,
        solution_id: str = None,
    ):
        # The unit price per adult.
        self.adult_price = adult_price
        # The tax per adult.
        self.adult_tax = adult_tax
        # The unit price per child.
        self.child_price = child_price
        # The tax per child.
        self.child_tax = child_tax
        # The unit price per infant.
        self.infant_price = infant_price
        # The tax per infant.
        self.infant_tax = infant_tax
        # The journey list.
        self.journey_list = journey_list
        # The baggage through-check rules.
        self.segment_baggage_check_in_info_list = segment_baggage_check_in_info_list
        # The free baggage allowance rules.
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
                temp_model = main_models.PricingResponseBodyDataSolutionJourneyList()
                self.journey_list.append(temp_model.from_map(k1))

        self.segment_baggage_check_in_info_list = []
        if m.get('segment_baggage_check_in_info_list') is not None:
            for k1 in m.get('segment_baggage_check_in_info_list'):
                temp_model = main_models.PricingResponseBodyDataSolutionSegmentBaggageCheckInInfoList()
                self.segment_baggage_check_in_info_list.append(temp_model.from_map(k1))

        self.segment_baggage_mapping_list = []
        if m.get('segment_baggage_mapping_list') is not None:
            for k1 in m.get('segment_baggage_mapping_list'):
                temp_model = main_models.PricingResponseBodyDataSolutionSegmentBaggageMappingList()
                self.segment_baggage_mapping_list.append(temp_model.from_map(k1))

        self.segment_refund_change_rule_mapping_list = []
        if m.get('segment_refund_change_rule_mapping_list') is not None:
            for k1 in m.get('segment_refund_change_rule_mapping_list'):
                temp_model = main_models.PricingResponseBodyDataSolutionSegmentRefundChangeRuleMappingList()
                self.segment_refund_change_rule_mapping_list.append(temp_model.from_map(k1))

        if m.get('solution_attribute') is not None:
            temp_model = main_models.PricingResponseBodyDataSolutionSolutionAttribute()
            self.solution_attribute = temp_model.from_map(m.get('solution_attribute'))

        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')

        return self

class PricingResponseBodyDataSolutionSolutionAttribute(DaraModel):
    def __init__(
        self,
        issue_time_info: main_models.PricingResponseBodyDataSolutionSolutionAttributeIssueTimeInfo = None,
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
            temp_model = main_models.PricingResponseBodyDataSolutionSolutionAttributeIssueTimeInfo()
            self.issue_time_info = temp_model.from_map(m.get('issue_time_info'))

        if m.get('supply_source_type') is not None:
            self.supply_source_type = m.get('supply_source_type')

        return self

class PricingResponseBodyDataSolutionSolutionAttributeIssueTimeInfo(DaraModel):
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

class PricingResponseBodyDataSolutionSegmentRefundChangeRuleMappingList(DaraModel):
    def __init__(
        self,
        refund_change_rule_map: Dict[str, main_models.DataSolutionSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue] = None,
        segment_id_list: List[str] = None,
    ):
        # The mapping between passenger types and refund and change rules.
        self.refund_change_rule_map = refund_change_rule_map
        # The list of segment IDs that share the same refund and change rule.
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

class PricingResponseBodyDataSolutionSegmentBaggageMappingList(DaraModel):
    def __init__(
        self,
        passenger_baggage_allowance_mapping: Dict[str, main_models.DataSolutionSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue] = None,
        segment_id_list: List[str] = None,
    ):
        # The mapping between passenger types and free baggage allowances.
        self.passenger_baggage_allowance_mapping = passenger_baggage_allowance_mapping
        # The list of segment IDs that share the same free baggage allowance rule.
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

class PricingResponseBodyDataSolutionSegmentBaggageCheckInInfoList(DaraModel):
    def __init__(
        self,
        luggage_direct_info_type: int = None,
        segment_id_list: List[str] = None,
    ):
        # The baggage through-check rule type. Valid values: 1: baggage is checked through between segments. 2: baggage must be rechecked between segments. 3: baggage is checked through at stopover cities. 4: baggage must be rechecked at stopover cities.
        self.luggage_direct_info_type = luggage_direct_info_type
        # The list of segment IDs that share the same baggage through-check rule.
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

class PricingResponseBodyDataSolutionJourneyList(DaraModel):
    def __init__(
        self,
        segment_list: List[main_models.PricingResponseBodyDataSolutionJourneyListSegmentList] = None,
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
                temp_model = main_models.PricingResponseBodyDataSolutionJourneyListSegmentList()
                self.segment_list.append(temp_model.from_map(k1))

        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')

        return self

class PricingResponseBodyDataSolutionJourneyListSegmentList(DaraModel):
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
        # The cabin code.
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
        # The flight duration in minutes.
        self.flight_duration = flight_duration
        # The marketing airline code (for example, KA).
        self.marketing_airline = marketing_airline
        # The marketing flight number (for example, KA5809).
        self.marketing_flight_no = marketing_flight_no
        # The numeric marketing flight number (for example, 5809).
        self.marketing_flight_no_int = marketing_flight_no_int
        # The operating airline code (for example, CX).
        self.operating_airline = operating_airline
        # The operating flight number (for example, CX601).
        self.operating_flight_no = operating_flight_no
        # The segment ID in the format: flight number + departure airport + arrival airport + departure date (MMdd).
        self.segment_id = segment_id
        # The list of stopover cities. This field has a value when stopQuantity is greater than 0. Multiple cities are separated by commas.
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

class PricingResponseBodyDataOriginalPriceInfo(DaraModel):
    def __init__(
        self,
        adult_price: float = None,
        adult_tax: float = None,
        child_price: float = None,
        child_tax: float = None,
        infant_price: float = None,
        infant_tax: float = None,
    ):
        # The unit price per adult.
        self.adult_price = adult_price
        # The tax per adult.
        self.adult_tax = adult_tax
        # The unit price per child.
        self.child_price = child_price
        # The tax per child.
        self.child_tax = child_tax
        # The unit price per infant.
        self.infant_price = infant_price
        # The tax per infant.
        self.infant_tax = infant_tax

    def validate(self):
        pass

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

        return self

class PricingResponseBodyDataChangedPriceInfo(DaraModel):
    def __init__(
        self,
        adult_price: float = None,
        adult_tax: float = None,
        child_price: float = None,
        child_tax: float = None,
        infant_price: float = None,
        infant_tax: float = None,
    ):
        # The unit price per adult.
        self.adult_price = adult_price
        # The tax per adult.
        self.adult_tax = adult_tax
        # The unit price per child.
        self.child_price = child_price
        # The tax per child.
        self.child_tax = child_tax
        # The unit price per infant.
        self.infant_price = infant_price
        # The tax per infant.
        self.infant_tax = infant_tax

    def validate(self):
        pass

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

        return self

