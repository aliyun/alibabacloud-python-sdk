# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List, Dict

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class SearchResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: main_models.SearchResponseBodyData = None,
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
        # Indicates whether the request is successful.
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
            temp_model = main_models.SearchResponseBodyData()
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

class SearchResponseBodyData(DaraModel):
    def __init__(
        self,
        solution_list: List[main_models.SearchResponseBodyDataSolutionList] = None,
    ):
        # The search quote results.
        self.solution_list = solution_list

    def validate(self):
        if self.solution_list:
            for v1 in self.solution_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['solution_list'] = []
        if self.solution_list is not None:
            for k1 in self.solution_list:
                result['solution_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.solution_list = []
        if m.get('solution_list') is not None:
            for k1 in m.get('solution_list'):
                temp_model = main_models.SearchResponseBodyDataSolutionList()
                self.solution_list.append(temp_model.from_map(k1))

        return self

class SearchResponseBodyDataSolutionList(DaraModel):
    def __init__(
        self,
        adult_price: float = None,
        adult_tax: float = None,
        child_price: float = None,
        child_tax: float = None,
        infant_price: float = None,
        infant_tax: float = None,
        journey_list: List[main_models.SearchResponseBodyDataSolutionListJourneyList] = None,
        segment_baggage_check_in_info_list: List[main_models.SearchResponseBodyDataSolutionListSegmentBaggageCheckInInfoList] = None,
        segment_baggage_mapping_list: List[main_models.SearchResponseBodyDataSolutionListSegmentBaggageMappingList] = None,
        segment_refund_change_rule_mapping_list: List[main_models.SearchResponseBodyDataSolutionListSegmentRefundChangeRuleMappingList] = None,
        solution_attribute: main_models.SearchResponseBodyDataSolutionListSolutionAttribute = None,
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
        # The journey.
        self.journey_list = journey_list
        # The baggage through-check rules.
        self.segment_baggage_check_in_info_list = segment_baggage_check_in_info_list
        # The free baggage rules.
        self.segment_baggage_mapping_list = segment_baggage_mapping_list
        # The refund and change rules.
        self.segment_refund_change_rule_mapping_list = segment_refund_change_rule_mapping_list
        # The quote attributes.
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
                temp_model = main_models.SearchResponseBodyDataSolutionListJourneyList()
                self.journey_list.append(temp_model.from_map(k1))

        self.segment_baggage_check_in_info_list = []
        if m.get('segment_baggage_check_in_info_list') is not None:
            for k1 in m.get('segment_baggage_check_in_info_list'):
                temp_model = main_models.SearchResponseBodyDataSolutionListSegmentBaggageCheckInInfoList()
                self.segment_baggage_check_in_info_list.append(temp_model.from_map(k1))

        self.segment_baggage_mapping_list = []
        if m.get('segment_baggage_mapping_list') is not None:
            for k1 in m.get('segment_baggage_mapping_list'):
                temp_model = main_models.SearchResponseBodyDataSolutionListSegmentBaggageMappingList()
                self.segment_baggage_mapping_list.append(temp_model.from_map(k1))

        self.segment_refund_change_rule_mapping_list = []
        if m.get('segment_refund_change_rule_mapping_list') is not None:
            for k1 in m.get('segment_refund_change_rule_mapping_list'):
                temp_model = main_models.SearchResponseBodyDataSolutionListSegmentRefundChangeRuleMappingList()
                self.segment_refund_change_rule_mapping_list.append(temp_model.from_map(k1))

        if m.get('solution_attribute') is not None:
            temp_model = main_models.SearchResponseBodyDataSolutionListSolutionAttribute()
            self.solution_attribute = temp_model.from_map(m.get('solution_attribute'))

        if m.get('solution_id') is not None:
            self.solution_id = m.get('solution_id')

        return self

class SearchResponseBodyDataSolutionListSolutionAttribute(DaraModel):
    def __init__(
        self,
        issue_time_info: main_models.SearchResponseBodyDataSolutionListSolutionAttributeIssueTimeInfo = None,
        supply_source_type: str = None,
    ):
        self.issue_time_info = issue_time_info
        # The supply source type. Valid values: 1: self-operated. 2: agent. 3: flagship store.
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
            temp_model = main_models.SearchResponseBodyDataSolutionListSolutionAttributeIssueTimeInfo()
            self.issue_time_info = temp_model.from_map(m.get('issue_time_info'))

        if m.get('supply_source_type') is not None:
            self.supply_source_type = m.get('supply_source_type')

        return self

class SearchResponseBodyDataSolutionListSolutionAttributeIssueTimeInfo(DaraModel):
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

class SearchResponseBodyDataSolutionListSegmentRefundChangeRuleMappingList(DaraModel):
    def __init__(
        self,
        refund_change_rule_map: Dict[str, main_models.DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue] = None,
        segment_id_list: List[str] = None,
    ):
        # The mapping between passenger types and refund and change rules.
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
                temp_model = main_models.DataSolutionListSegmentRefundChangeRuleMappingListRefundChangeRuleMapValue()
                self.refund_change_rule_map[k1] = temp_model.from_map(v1)

        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')

        return self

class SearchResponseBodyDataSolutionListSegmentBaggageMappingList(DaraModel):
    def __init__(
        self,
        passenger_baggage_allowance_mapping: Dict[str, main_models.DataSolutionListSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue] = None,
        segment_id_list: List[str] = None,
    ):
        # The mapping between passenger types and free baggage allowances.
        self.passenger_baggage_allowance_mapping = passenger_baggage_allowance_mapping
        # The list of segment IDs. These segments share the same free baggage rule.
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
                temp_model = main_models.DataSolutionListSegmentBaggageMappingListPassengerBaggageAllowanceMappingValue()
                self.passenger_baggage_allowance_mapping[k1] = temp_model.from_map(v1)

        if m.get('segment_id_list') is not None:
            self.segment_id_list = m.get('segment_id_list')

        return self

class SearchResponseBodyDataSolutionListSegmentBaggageCheckInInfoList(DaraModel):
    def __init__(
        self,
        luggage_direct_info_type: int = None,
        segment_id_list: List[str] = None,
    ):
        # The baggage through-check rule type. Valid values: 1: baggage is checked through between segments. 2: baggage must be rechecked between segments. 3: baggage is checked through at stopover cities. 4: baggage must be rechecked at stopover cities.
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

class SearchResponseBodyDataSolutionListJourneyList(DaraModel):
    def __init__(
        self,
        segment_list: List[main_models.SearchResponseBodyDataSolutionListJourneyListSegmentList] = None,
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
                temp_model = main_models.SearchResponseBodyDataSolutionListJourneyListSegmentList()
                self.segment_list.append(temp_model.from_map(k1))

        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')

        return self

class SearchResponseBodyDataSolutionListJourneyListSegmentList(DaraModel):
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
        # The three-letter code of the arrival airport (uppercase).
        self.arrival_airport = arrival_airport
        # The three-letter code of the arrival city (uppercase).
        self.arrival_city = arrival_city
        # The arrival terminal.
        self.arrival_terminal = arrival_terminal
        # The arrival date and time in string format (yyyy-MM-dd HH:mm:ss).
        self.arrival_time = arrival_time
        # The number of remaining seats. Valid values: 1, 2, 3, 4, 5, 6, 7, 8, 9, and A. A indicates that more than 9 seats are available.
        self.availability = availability
        # The booking class.
        self.cabin = cabin
        # The cabin class.
        self.cabin_class = cabin_class
        # Indicates whether the flight is a codeshare flight.
        self.code_share = code_share
        # The three-letter code of the departure airport (uppercase).
        self.departure_airport = departure_airport
        # The three-letter code of the departure city (uppercase).
        self.departure_city = departure_city
        # The departure terminal.
        self.departure_terminal = departure_terminal
        # The departure date and time in string format (yyyy-MM-dd HH:mm:ss).
        self.departure_time = departure_time
        # The aircraft type.
        self.equip_type = equip_type
        # The flight duration. Unit: minutes.
        self.flight_duration = flight_duration
        # The marketing airline (such as KA).
        self.marketing_airline = marketing_airline
        # The marketing flight number (such as KA5809).
        self.marketing_flight_no = marketing_flight_no
        # The numeric marketing flight number (such as 5809).
        self.marketing_flight_no_int = marketing_flight_no_int
        # The operating airline (such as CX).
        self.operating_airline = operating_airline
        # The operating flight number (such as CX601).
        self.operating_flight_no = operating_flight_no
        # The segment ID. Format: flight number + departure airport + arrival airport + departure date (MMdd).
        self.segment_id = segment_id
        # The list of stopover cities. This parameter has a value when stopQuantity is greater than 0. Multiple values are separated by commas.
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

