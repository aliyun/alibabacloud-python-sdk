# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightModifyOtaSearchV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.FlightModifyOtaSearchV2ResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        # module
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
            temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightModifyOtaSearchV2ResponseBodyModule(DaraModel):
    def __init__(
        self,
        agent_infos: List[main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfos] = None,
        agent_info: main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfo = None,
        cache_key: str = None,
        flight_segment_infos: List[List[main_models.FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfos]] = None,
        passenger_count: main_models.FlightModifyOtaSearchV2ResponseBodyModulePassengerCount = None,
        session_id: str = None,
    ):
        self.agent_infos = agent_infos
        self.agent_info = agent_info
        self.cache_key = cache_key
        self.flight_segment_infos = flight_segment_infos
        self.passenger_count = passenger_count
        self.session_id = session_id

    def validate(self):
        if self.agent_infos:
            for v1 in self.agent_infos:
                 if v1:
                    v1.validate()
        if self.agent_info:
            self.agent_info.validate()
        if self.flight_segment_infos:
            for v1 in self.flight_segment_infos:
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.passenger_count:
            self.passenger_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['agentInfos'] = []
        if self.agent_infos is not None:
            for k1 in self.agent_infos:
                result['agentInfos'].append(k1.to_map() if k1 else None)

        if self.agent_info is not None:
            result['agent_info'] = self.agent_info.to_map()

        if self.cache_key is not None:
            result['cache_key'] = self.cache_key

        result['flight_segment_infos'] = []
        if self.flight_segment_infos is not None:
            for k1 in self.flight_segment_infos:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['flight_segment_infos'].append(l1)

        if self.passenger_count is not None:
            result['passenger_count'] = self.passenger_count.to_map()

        if self.session_id is not None:
            result['session_id'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent_infos = []
        if m.get('agentInfos') is not None:
            for k1 in m.get('agentInfos'):
                temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfos()
                self.agent_infos.append(temp_model.from_map(k1))

        if m.get('agent_info') is not None:
            temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfo()
            self.agent_info = temp_model.from_map(m.get('agent_info'))

        if m.get('cache_key') is not None:
            self.cache_key = m.get('cache_key')

        self.flight_segment_infos = []
        if m.get('flight_segment_infos') is not None:
            for k1 in m.get('flight_segment_infos'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfos()
                    l1.append(temp_model.from_map(k2))
                self.flight_segment_infos.append(l1)

        if m.get('passenger_count') is not None:
            temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModulePassengerCount()
            self.passenger_count = temp_model.from_map(m.get('passenger_count'))

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        return self

class FlightModifyOtaSearchV2ResponseBodyModulePassengerCount(DaraModel):
    def __init__(
        self,
        adult_passenger_num: int = None,
        child_passenger_num: int = None,
        infant_passenger_num: int = None,
    ):
        self.adult_passenger_num = adult_passenger_num
        self.child_passenger_num = child_passenger_num
        self.infant_passenger_num = infant_passenger_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adult_passenger_num is not None:
            result['adult_passenger_num'] = self.adult_passenger_num

        if self.child_passenger_num is not None:
            result['child_passenger_num'] = self.child_passenger_num

        if self.infant_passenger_num is not None:
            result['infant_passenger_num'] = self.infant_passenger_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adult_passenger_num') is not None:
            self.adult_passenger_num = m.get('adult_passenger_num')

        if m.get('child_passenger_num') is not None:
            self.child_passenger_num = m.get('child_passenger_num')

        if m.get('infant_passenger_num') is not None:
            self.infant_passenger_num = m.get('infant_passenger_num')

        return self

class FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfos(DaraModel):
    def __init__(
        self,
        journey_seq: int = None,
        segment_seq: int = None,
        flight_no: str = None,
        dep_city_code: str = None,
        arr_city_code: str = None,
        dep_city_name: str = None,
        arr_city_name: str = None,
        dep_airport_info: main_models.FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosDepAirportInfo = None,
        arr_airport_info: main_models.FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosArrAirportInfo = None,
        dep_time: str = None,
        arr_time: str = None,
        airline_info: main_models.FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosAirlineInfo = None,
        share: bool = None,
        flight_shared_info: main_models.FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosFlightSharedInfo = None,
        stop: bool = None,
        flight_stop_info: main_models.FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosFlightStopInfo = None,
        transfer_time: int = None,
        duration: int = None,
        manufacturer: str = None,
        flight_type: str = None,
        flight_size: str = None,
        meal_desc: str = None,
        on_time_rate: str = None,
    ):
        self.journey_seq = journey_seq
        self.segment_seq = segment_seq
        self.flight_no = flight_no
        self.dep_city_code = dep_city_code
        self.arr_city_code = arr_city_code
        self.dep_city_name = dep_city_name
        self.arr_city_name = arr_city_name
        self.dep_airport_info = dep_airport_info
        self.arr_airport_info = arr_airport_info
        self.dep_time = dep_time
        self.arr_time = arr_time
        self.airline_info = airline_info
        self.share = share
        self.flight_shared_info = flight_shared_info
        self.stop = stop
        self.flight_stop_info = flight_stop_info
        self.transfer_time = transfer_time
        self.duration = duration
        self.manufacturer = manufacturer
        self.flight_type = flight_type
        self.flight_size = flight_size
        self.meal_desc = meal_desc
        self.on_time_rate = on_time_rate

    def validate(self):
        if self.dep_airport_info:
            self.dep_airport_info.validate()
        if self.arr_airport_info:
            self.arr_airport_info.validate()
        if self.airline_info:
            self.airline_info.validate()
        if self.flight_shared_info:
            self.flight_shared_info.validate()
        if self.flight_stop_info:
            self.flight_stop_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.journey_seq is not None:
            result['journey_seq'] = self.journey_seq

        if self.segment_seq is not None:
            result['segment_seq'] = self.segment_seq

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name

        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name

        if self.dep_airport_info is not None:
            result['dep_airport_info'] = self.dep_airport_info.to_map()

        if self.arr_airport_info is not None:
            result['arr_airport_info'] = self.arr_airport_info.to_map()

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.airline_info is not None:
            result['airline_info'] = self.airline_info.to_map()

        if self.share is not None:
            result['share'] = self.share

        if self.flight_shared_info is not None:
            result['flight_shared_info'] = self.flight_shared_info.to_map()

        if self.stop is not None:
            result['stop'] = self.stop

        if self.flight_stop_info is not None:
            result['flight_stop_info'] = self.flight_stop_info.to_map()

        if self.transfer_time is not None:
            result['transfer_time'] = self.transfer_time

        if self.duration is not None:
            result['duration'] = self.duration

        if self.manufacturer is not None:
            result['manufacturer'] = self.manufacturer

        if self.flight_type is not None:
            result['flight_type'] = self.flight_type

        if self.flight_size is not None:
            result['flight_size'] = self.flight_size

        if self.meal_desc is not None:
            result['meal_desc'] = self.meal_desc

        if self.on_time_rate is not None:
            result['on_time_rate'] = self.on_time_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('journey_seq') is not None:
            self.journey_seq = m.get('journey_seq')

        if m.get('segment_seq') is not None:
            self.segment_seq = m.get('segment_seq')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('dep_airport_info') is not None:
            temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosDepAirportInfo()
            self.dep_airport_info = temp_model.from_map(m.get('dep_airport_info'))

        if m.get('arr_airport_info') is not None:
            temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosArrAirportInfo()
            self.arr_airport_info = temp_model.from_map(m.get('arr_airport_info'))

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('airline_info') is not None:
            temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosAirlineInfo()
            self.airline_info = temp_model.from_map(m.get('airline_info'))

        if m.get('share') is not None:
            self.share = m.get('share')

        if m.get('flight_shared_info') is not None:
            temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosFlightSharedInfo()
            self.flight_shared_info = temp_model.from_map(m.get('flight_shared_info'))

        if m.get('stop') is not None:
            self.stop = m.get('stop')

        if m.get('flight_stop_info') is not None:
            temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosFlightStopInfo()
            self.flight_stop_info = temp_model.from_map(m.get('flight_stop_info'))

        if m.get('transfer_time') is not None:
            self.transfer_time = m.get('transfer_time')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('manufacturer') is not None:
            self.manufacturer = m.get('manufacturer')

        if m.get('flight_type') is not None:
            self.flight_type = m.get('flight_type')

        if m.get('flight_size') is not None:
            self.flight_size = m.get('flight_size')

        if m.get('meal_desc') is not None:
            self.meal_desc = m.get('meal_desc')

        if m.get('on_time_rate') is not None:
            self.on_time_rate = m.get('on_time_rate')

        return self

class FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosFlightStopInfo(DaraModel):
    def __init__(
        self,
        stop_city_name: str = None,
        stop_arr_time: str = None,
        stop_dep_time: str = None,
        stop_city_code: str = None,
        stop_airport: str = None,
        stop_arr_term: str = None,
        stop_dep_term: str = None,
    ):
        self.stop_city_name = stop_city_name
        self.stop_arr_time = stop_arr_time
        self.stop_dep_time = stop_dep_time
        self.stop_city_code = stop_city_code
        self.stop_airport = stop_airport
        self.stop_arr_term = stop_arr_term
        self.stop_dep_term = stop_dep_term

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stop_city_name is not None:
            result['stop_city_name'] = self.stop_city_name

        if self.stop_arr_time is not None:
            result['stop_arr_time'] = self.stop_arr_time

        if self.stop_dep_time is not None:
            result['stop_dep_time'] = self.stop_dep_time

        if self.stop_city_code is not None:
            result['stop_city_code'] = self.stop_city_code

        if self.stop_airport is not None:
            result['stop_airport'] = self.stop_airport

        if self.stop_arr_term is not None:
            result['stop_arr_term'] = self.stop_arr_term

        if self.stop_dep_term is not None:
            result['stop_dep_term'] = self.stop_dep_term

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stop_city_name') is not None:
            self.stop_city_name = m.get('stop_city_name')

        if m.get('stop_arr_time') is not None:
            self.stop_arr_time = m.get('stop_arr_time')

        if m.get('stop_dep_time') is not None:
            self.stop_dep_time = m.get('stop_dep_time')

        if m.get('stop_city_code') is not None:
            self.stop_city_code = m.get('stop_city_code')

        if m.get('stop_airport') is not None:
            self.stop_airport = m.get('stop_airport')

        if m.get('stop_arr_term') is not None:
            self.stop_arr_term = m.get('stop_arr_term')

        if m.get('stop_dep_term') is not None:
            self.stop_dep_term = m.get('stop_dep_term')

        return self

class FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosFlightSharedInfo(DaraModel):
    def __init__(
        self,
        operating_flight_no: str = None,
        operating_airline_info: main_models.FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosFlightSharedInfoOperatingAirlineInfo = None,
    ):
        self.operating_flight_no = operating_flight_no
        self.operating_airline_info = operating_airline_info

    def validate(self):
        if self.operating_airline_info:
            self.operating_airline_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no

        if self.operating_airline_info is not None:
            result['operating_airline_info'] = self.operating_airline_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')

        if m.get('operating_airline_info') is not None:
            temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosFlightSharedInfoOperatingAirlineInfo()
            self.operating_airline_info = temp_model.from_map(m.get('operating_airline_info'))

        return self

class FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosFlightSharedInfoOperatingAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_chinese_name: str = None,
        airline_chinese_short_name: str = None,
        airline_icon: str = None,
        cheap_flight: bool = None,
    ):
        self.airline_code = airline_code
        self.airline_chinese_name = airline_chinese_name
        self.airline_chinese_short_name = airline_chinese_short_name
        self.airline_icon = airline_icon
        self.cheap_flight = cheap_flight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_chinese_name is not None:
            result['airline_chinese_name'] = self.airline_chinese_name

        if self.airline_chinese_short_name is not None:
            result['airline_chinese_short_name'] = self.airline_chinese_short_name

        if self.airline_icon is not None:
            result['airline_icon'] = self.airline_icon

        if self.cheap_flight is not None:
            result['cheap_flight'] = self.cheap_flight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_chinese_name') is not None:
            self.airline_chinese_name = m.get('airline_chinese_name')

        if m.get('airline_chinese_short_name') is not None:
            self.airline_chinese_short_name = m.get('airline_chinese_short_name')

        if m.get('airline_icon') is not None:
            self.airline_icon = m.get('airline_icon')

        if m.get('cheap_flight') is not None:
            self.cheap_flight = m.get('cheap_flight')

        return self

class FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_chinese_name: str = None,
        airline_chinese_short_name: str = None,
        airline_icon: str = None,
        cheap_flight: bool = None,
    ):
        self.airline_code = airline_code
        self.airline_chinese_name = airline_chinese_name
        self.airline_chinese_short_name = airline_chinese_short_name
        self.airline_icon = airline_icon
        self.cheap_flight = cheap_flight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_chinese_name is not None:
            result['airline_chinese_name'] = self.airline_chinese_name

        if self.airline_chinese_short_name is not None:
            result['airline_chinese_short_name'] = self.airline_chinese_short_name

        if self.airline_icon is not None:
            result['airline_icon'] = self.airline_icon

        if self.cheap_flight is not None:
            result['cheap_flight'] = self.cheap_flight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_chinese_name') is not None:
            self.airline_chinese_name = m.get('airline_chinese_name')

        if m.get('airline_chinese_short_name') is not None:
            self.airline_chinese_short_name = m.get('airline_chinese_short_name')

        if m.get('airline_icon') is not None:
            self.airline_icon = m.get('airline_icon')

        if m.get('cheap_flight') is not None:
            self.cheap_flight = m.get('cheap_flight')

        return self

class FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosArrAirportInfo(DaraModel):
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

class FlightModifyOtaSearchV2ResponseBodyModuleFlightSegmentInfosDepAirportInfo(DaraModel):
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

class FlightModifyOtaSearchV2ResponseBodyModuleAgentInfo(DaraModel):
    def __init__(
        self,
        attribute_show_info_map: Dict[str, List[main_models.ModuleAgentInfoAttributeShowInfoMapValue]] = None,
        best_discount: float = None,
        cabin_class_info: main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfoCabinClassInfo = None,
        cabin_code: int = None,
        cabin_name: str = None,
        item_id: str = None,
        modify_type_desc: str = None,
        modify_type_name: str = None,
        price_info_dto: main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfoPriceInfoDTO = None,
        quantity: int = None,
        support_child_ticket: bool = None,
    ):
        self.attribute_show_info_map = attribute_show_info_map
        self.best_discount = best_discount
        self.cabin_class_info = cabin_class_info
        self.cabin_code = cabin_code
        self.cabin_name = cabin_name
        # item_id
        self.item_id = item_id
        self.modify_type_desc = modify_type_desc
        self.modify_type_name = modify_type_name
        self.price_info_dto = price_info_dto
        self.quantity = quantity
        self.support_child_ticket = support_child_ticket

    def validate(self):
        if self.attribute_show_info_map:
            for v1 in self.attribute_show_info_map.values():
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.cabin_class_info:
            self.cabin_class_info.validate()
        if self.price_info_dto:
            self.price_info_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['attribute_show_info_map'] = {}
        if self.attribute_show_info_map is not None:
            for k1, v1 in self.attribute_show_info_map.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['attribute_show_info_map'][k1] = l1

        if self.best_discount is not None:
            result['best_discount'] = self.best_discount

        if self.cabin_class_info is not None:
            result['cabin_class_info'] = self.cabin_class_info.to_map()

        if self.cabin_code is not None:
            result['cabin_code'] = self.cabin_code

        if self.cabin_name is not None:
            result['cabin_name'] = self.cabin_name

        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.modify_type_desc is not None:
            result['modify_type_desc'] = self.modify_type_desc

        if self.modify_type_name is not None:
            result['modify_type_name'] = self.modify_type_name

        if self.price_info_dto is not None:
            result['price_info_d_t_o'] = self.price_info_dto.to_map()

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.support_child_ticket is not None:
            result['support_child_ticket'] = self.support_child_ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_show_info_map = {}
        if m.get('attribute_show_info_map') is not None:
            for k1, v1 in m.get('attribute_show_info_map').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.ModuleAgentInfoAttributeShowInfoMapValue()
                    l1.append(temp_model.from_map(k2))
                self.attribute_show_info_map[k1] = l1

        if m.get('best_discount') is not None:
            self.best_discount = m.get('best_discount')

        if m.get('cabin_class_info') is not None:
            temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfoCabinClassInfo()
            self.cabin_class_info = temp_model.from_map(m.get('cabin_class_info'))

        if m.get('cabin_code') is not None:
            self.cabin_code = m.get('cabin_code')

        if m.get('cabin_name') is not None:
            self.cabin_name = m.get('cabin_name')

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('modify_type_desc') is not None:
            self.modify_type_desc = m.get('modify_type_desc')

        if m.get('modify_type_name') is not None:
            self.modify_type_name = m.get('modify_type_name')

        if m.get('price_info_d_t_o') is not None:
            temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfoPriceInfoDTO()
            self.price_info_dto = temp_model.from_map(m.get('price_info_d_t_o'))

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('support_child_ticket') is not None:
            self.support_child_ticket = m.get('support_child_ticket')

        return self

class FlightModifyOtaSearchV2ResponseBodyModuleAgentInfoPriceInfoDTO(DaraModel):
    def __init__(
        self,
        adult_price: int = None,
        adult_tax: int = None,
        adult_total_price: int = None,
        before_control_price: int = None,
        child_price: int = None,
        child_tax: int = None,
        child_total_price: int = None,
        infant_price: int = None,
        infant_tax: int = None,
        infant_total_price: int = None,
        original_adult_price: int = None,
        original_adult_total_price: int = None,
        re_shop_price_info_dto: main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfoPriceInfoDTOReShopPriceInfoDTO = None,
    ):
        self.adult_price = adult_price
        self.adult_tax = adult_tax
        self.adult_total_price = adult_total_price
        self.before_control_price = before_control_price
        self.child_price = child_price
        self.child_tax = child_tax
        self.child_total_price = child_total_price
        self.infant_price = infant_price
        self.infant_tax = infant_tax
        self.infant_total_price = infant_total_price
        self.original_adult_price = original_adult_price
        self.original_adult_total_price = original_adult_total_price
        self.re_shop_price_info_dto = re_shop_price_info_dto

    def validate(self):
        if self.re_shop_price_info_dto:
            self.re_shop_price_info_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adult_price is not None:
            result['adult_price'] = self.adult_price

        if self.adult_tax is not None:
            result['adult_tax'] = self.adult_tax

        if self.adult_total_price is not None:
            result['adult_total_price'] = self.adult_total_price

        if self.before_control_price is not None:
            result['before_control_price'] = self.before_control_price

        if self.child_price is not None:
            result['child_price'] = self.child_price

        if self.child_tax is not None:
            result['child_tax'] = self.child_tax

        if self.child_total_price is not None:
            result['child_total_price'] = self.child_total_price

        if self.infant_price is not None:
            result['infant_price'] = self.infant_price

        if self.infant_tax is not None:
            result['infant_tax'] = self.infant_tax

        if self.infant_total_price is not None:
            result['infant_total_price'] = self.infant_total_price

        if self.original_adult_price is not None:
            result['original_adult_price'] = self.original_adult_price

        if self.original_adult_total_price is not None:
            result['original_adult_total_price'] = self.original_adult_total_price

        if self.re_shop_price_info_dto is not None:
            result['re_shop_price_info_d_t_o'] = self.re_shop_price_info_dto.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adult_price') is not None:
            self.adult_price = m.get('adult_price')

        if m.get('adult_tax') is not None:
            self.adult_tax = m.get('adult_tax')

        if m.get('adult_total_price') is not None:
            self.adult_total_price = m.get('adult_total_price')

        if m.get('before_control_price') is not None:
            self.before_control_price = m.get('before_control_price')

        if m.get('child_price') is not None:
            self.child_price = m.get('child_price')

        if m.get('child_tax') is not None:
            self.child_tax = m.get('child_tax')

        if m.get('child_total_price') is not None:
            self.child_total_price = m.get('child_total_price')

        if m.get('infant_price') is not None:
            self.infant_price = m.get('infant_price')

        if m.get('infant_tax') is not None:
            self.infant_tax = m.get('infant_tax')

        if m.get('infant_total_price') is not None:
            self.infant_total_price = m.get('infant_total_price')

        if m.get('original_adult_price') is not None:
            self.original_adult_price = m.get('original_adult_price')

        if m.get('original_adult_total_price') is not None:
            self.original_adult_total_price = m.get('original_adult_total_price')

        if m.get('re_shop_price_info_d_t_o') is not None:
            temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfoPriceInfoDTOReShopPriceInfoDTO()
            self.re_shop_price_info_dto = temp_model.from_map(m.get('re_shop_price_info_d_t_o'))

        return self

class FlightModifyOtaSearchV2ResponseBodyModuleAgentInfoPriceInfoDTOReShopPriceInfoDTO(DaraModel):
    def __init__(
        self,
        re_shop_adult_change_fee: int = None,
        re_shop_adult_price: int = None,
        re_shop_adult_price_gap: int = None,
        re_shop_child_change_fee: int = None,
        re_shop_child_price: int = None,
        re_shop_child_price_gap: int = None,
        re_shop_inf_change_fee: int = None,
        re_shop_inf_price: int = None,
        re_shop_inf_price_gap: int = None,
    ):
        self.re_shop_adult_change_fee = re_shop_adult_change_fee
        self.re_shop_adult_price = re_shop_adult_price
        self.re_shop_adult_price_gap = re_shop_adult_price_gap
        self.re_shop_child_change_fee = re_shop_child_change_fee
        self.re_shop_child_price = re_shop_child_price
        self.re_shop_child_price_gap = re_shop_child_price_gap
        self.re_shop_inf_change_fee = re_shop_inf_change_fee
        self.re_shop_inf_price = re_shop_inf_price
        self.re_shop_inf_price_gap = re_shop_inf_price_gap

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.re_shop_adult_change_fee is not None:
            result['re_shop_adult_change_fee'] = self.re_shop_adult_change_fee

        if self.re_shop_adult_price is not None:
            result['re_shop_adult_price'] = self.re_shop_adult_price

        if self.re_shop_adult_price_gap is not None:
            result['re_shop_adult_price_gap'] = self.re_shop_adult_price_gap

        if self.re_shop_child_change_fee is not None:
            result['re_shop_child_change_fee'] = self.re_shop_child_change_fee

        if self.re_shop_child_price is not None:
            result['re_shop_child_price'] = self.re_shop_child_price

        if self.re_shop_child_price_gap is not None:
            result['re_shop_child_price_gap'] = self.re_shop_child_price_gap

        if self.re_shop_inf_change_fee is not None:
            result['re_shop_inf_change_fee'] = self.re_shop_inf_change_fee

        if self.re_shop_inf_price is not None:
            result['re_shop_inf_price'] = self.re_shop_inf_price

        if self.re_shop_inf_price_gap is not None:
            result['re_shop_inf_price_gap'] = self.re_shop_inf_price_gap

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('re_shop_adult_change_fee') is not None:
            self.re_shop_adult_change_fee = m.get('re_shop_adult_change_fee')

        if m.get('re_shop_adult_price') is not None:
            self.re_shop_adult_price = m.get('re_shop_adult_price')

        if m.get('re_shop_adult_price_gap') is not None:
            self.re_shop_adult_price_gap = m.get('re_shop_adult_price_gap')

        if m.get('re_shop_child_change_fee') is not None:
            self.re_shop_child_change_fee = m.get('re_shop_child_change_fee')

        if m.get('re_shop_child_price') is not None:
            self.re_shop_child_price = m.get('re_shop_child_price')

        if m.get('re_shop_child_price_gap') is not None:
            self.re_shop_child_price_gap = m.get('re_shop_child_price_gap')

        if m.get('re_shop_inf_change_fee') is not None:
            self.re_shop_inf_change_fee = m.get('re_shop_inf_change_fee')

        if m.get('re_shop_inf_price') is not None:
            self.re_shop_inf_price = m.get('re_shop_inf_price')

        if m.get('re_shop_inf_price_gap') is not None:
            self.re_shop_inf_price_gap = m.get('re_shop_inf_price_gap')

        return self

class FlightModifyOtaSearchV2ResponseBodyModuleAgentInfoCabinClassInfo(DaraModel):
    def __init__(
        self,
        cabin_class: str = None,
        class_name: str = None,
        inner_cabin_class: int = None,
        quantity: str = None,
    ):
        self.cabin_class = cabin_class
        self.class_name = class_name
        # inner_cabin_class
        self.inner_cabin_class = inner_cabin_class
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.class_name is not None:
            result['class_name'] = self.class_name

        if self.inner_cabin_class is not None:
            result['inner_cabin_class'] = self.inner_cabin_class

        if self.quantity is not None:
            result['quantity'] = self.quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('class_name') is not None:
            self.class_name = m.get('class_name')

        if m.get('inner_cabin_class') is not None:
            self.inner_cabin_class = m.get('inner_cabin_class')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        return self

class FlightModifyOtaSearchV2ResponseBodyModuleAgentInfos(DaraModel):
    def __init__(
        self,
        attribute_show_info_map: Dict[str, List[main_models.ModuleAgentInfosAttributeShowInfoMapValue]] = None,
        best_discount: float = None,
        cabin_class_info: main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfosCabinClassInfo = None,
        cabin_code: int = None,
        cabin_name: str = None,
        item_id: str = None,
        modify_type_desc: str = None,
        modify_type_name: str = None,
        price_info_dto: main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfosPriceInfoDTO = None,
        quantity: int = None,
        support_child_ticket: bool = None,
    ):
        self.attribute_show_info_map = attribute_show_info_map
        self.best_discount = best_discount
        self.cabin_class_info = cabin_class_info
        self.cabin_code = cabin_code
        self.cabin_name = cabin_name
        self.item_id = item_id
        self.modify_type_desc = modify_type_desc
        self.modify_type_name = modify_type_name
        self.price_info_dto = price_info_dto
        self.quantity = quantity
        self.support_child_ticket = support_child_ticket

    def validate(self):
        if self.attribute_show_info_map:
            for v1 in self.attribute_show_info_map.values():
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.cabin_class_info:
            self.cabin_class_info.validate()
        if self.price_info_dto:
            self.price_info_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['attribute_show_info_map'] = {}
        if self.attribute_show_info_map is not None:
            for k1, v1 in self.attribute_show_info_map.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['attribute_show_info_map'][k1] = l1

        if self.best_discount is not None:
            result['best_discount'] = self.best_discount

        if self.cabin_class_info is not None:
            result['cabin_class_info'] = self.cabin_class_info.to_map()

        if self.cabin_code is not None:
            result['cabin_code'] = self.cabin_code

        if self.cabin_name is not None:
            result['cabin_name'] = self.cabin_name

        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.modify_type_desc is not None:
            result['modify_type_desc'] = self.modify_type_desc

        if self.modify_type_name is not None:
            result['modify_type_name'] = self.modify_type_name

        if self.price_info_dto is not None:
            result['price_info_d_t_o'] = self.price_info_dto.to_map()

        if self.quantity is not None:
            result['quantity'] = self.quantity

        if self.support_child_ticket is not None:
            result['support_child_ticket'] = self.support_child_ticket

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_show_info_map = {}
        if m.get('attribute_show_info_map') is not None:
            for k1, v1 in m.get('attribute_show_info_map').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.ModuleAgentInfosAttributeShowInfoMapValue()
                    l1.append(temp_model.from_map(k2))
                self.attribute_show_info_map[k1] = l1

        if m.get('best_discount') is not None:
            self.best_discount = m.get('best_discount')

        if m.get('cabin_class_info') is not None:
            temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfosCabinClassInfo()
            self.cabin_class_info = temp_model.from_map(m.get('cabin_class_info'))

        if m.get('cabin_code') is not None:
            self.cabin_code = m.get('cabin_code')

        if m.get('cabin_name') is not None:
            self.cabin_name = m.get('cabin_name')

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('modify_type_desc') is not None:
            self.modify_type_desc = m.get('modify_type_desc')

        if m.get('modify_type_name') is not None:
            self.modify_type_name = m.get('modify_type_name')

        if m.get('price_info_d_t_o') is not None:
            temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfosPriceInfoDTO()
            self.price_info_dto = temp_model.from_map(m.get('price_info_d_t_o'))

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        if m.get('support_child_ticket') is not None:
            self.support_child_ticket = m.get('support_child_ticket')

        return self

class FlightModifyOtaSearchV2ResponseBodyModuleAgentInfosPriceInfoDTO(DaraModel):
    def __init__(
        self,
        adult_price: int = None,
        adult_tax: int = None,
        adult_total_price: int = None,
        before_control_price: int = None,
        child_price: int = None,
        child_tax: int = None,
        child_total_price: int = None,
        infant_price: int = None,
        infant_tax: int = None,
        infant_total_price: int = None,
        original_adult_price: int = None,
        original_adult_total_price: int = None,
        re_shop_price_info_dto: main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfosPriceInfoDTOReShopPriceInfoDTO = None,
    ):
        self.adult_price = adult_price
        self.adult_tax = adult_tax
        self.adult_total_price = adult_total_price
        self.before_control_price = before_control_price
        self.child_price = child_price
        self.child_tax = child_tax
        self.child_total_price = child_total_price
        self.infant_price = infant_price
        self.infant_tax = infant_tax
        self.infant_total_price = infant_total_price
        self.original_adult_price = original_adult_price
        self.original_adult_total_price = original_adult_total_price
        self.re_shop_price_info_dto = re_shop_price_info_dto

    def validate(self):
        if self.re_shop_price_info_dto:
            self.re_shop_price_info_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adult_price is not None:
            result['adult_price'] = self.adult_price

        if self.adult_tax is not None:
            result['adult_tax'] = self.adult_tax

        if self.adult_total_price is not None:
            result['adult_total_price'] = self.adult_total_price

        if self.before_control_price is not None:
            result['before_control_price'] = self.before_control_price

        if self.child_price is not None:
            result['child_price'] = self.child_price

        if self.child_tax is not None:
            result['child_tax'] = self.child_tax

        if self.child_total_price is not None:
            result['child_total_price'] = self.child_total_price

        if self.infant_price is not None:
            result['infant_price'] = self.infant_price

        if self.infant_tax is not None:
            result['infant_tax'] = self.infant_tax

        if self.infant_total_price is not None:
            result['infant_total_price'] = self.infant_total_price

        if self.original_adult_price is not None:
            result['original_adult_price'] = self.original_adult_price

        if self.original_adult_total_price is not None:
            result['original_adult_total_price'] = self.original_adult_total_price

        if self.re_shop_price_info_dto is not None:
            result['re_shop_price_info_d_t_o'] = self.re_shop_price_info_dto.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adult_price') is not None:
            self.adult_price = m.get('adult_price')

        if m.get('adult_tax') is not None:
            self.adult_tax = m.get('adult_tax')

        if m.get('adult_total_price') is not None:
            self.adult_total_price = m.get('adult_total_price')

        if m.get('before_control_price') is not None:
            self.before_control_price = m.get('before_control_price')

        if m.get('child_price') is not None:
            self.child_price = m.get('child_price')

        if m.get('child_tax') is not None:
            self.child_tax = m.get('child_tax')

        if m.get('child_total_price') is not None:
            self.child_total_price = m.get('child_total_price')

        if m.get('infant_price') is not None:
            self.infant_price = m.get('infant_price')

        if m.get('infant_tax') is not None:
            self.infant_tax = m.get('infant_tax')

        if m.get('infant_total_price') is not None:
            self.infant_total_price = m.get('infant_total_price')

        if m.get('original_adult_price') is not None:
            self.original_adult_price = m.get('original_adult_price')

        if m.get('original_adult_total_price') is not None:
            self.original_adult_total_price = m.get('original_adult_total_price')

        if m.get('re_shop_price_info_d_t_o') is not None:
            temp_model = main_models.FlightModifyOtaSearchV2ResponseBodyModuleAgentInfosPriceInfoDTOReShopPriceInfoDTO()
            self.re_shop_price_info_dto = temp_model.from_map(m.get('re_shop_price_info_d_t_o'))

        return self

class FlightModifyOtaSearchV2ResponseBodyModuleAgentInfosPriceInfoDTOReShopPriceInfoDTO(DaraModel):
    def __init__(
        self,
        re_shop_adult_change_fee: int = None,
        re_shop_adult_price: int = None,
        re_shop_adult_price_gap: int = None,
        re_shop_child_change_fee: int = None,
        re_shop_child_price: int = None,
        re_shop_child_price_gap: int = None,
        re_shop_inf_change_fee: int = None,
        re_shop_inf_price: int = None,
        re_shop_inf_price_gap: int = None,
    ):
        self.re_shop_adult_change_fee = re_shop_adult_change_fee
        self.re_shop_adult_price = re_shop_adult_price
        self.re_shop_adult_price_gap = re_shop_adult_price_gap
        self.re_shop_child_change_fee = re_shop_child_change_fee
        self.re_shop_child_price = re_shop_child_price
        self.re_shop_child_price_gap = re_shop_child_price_gap
        self.re_shop_inf_change_fee = re_shop_inf_change_fee
        self.re_shop_inf_price = re_shop_inf_price
        self.re_shop_inf_price_gap = re_shop_inf_price_gap

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.re_shop_adult_change_fee is not None:
            result['re_shop_adult_change_fee'] = self.re_shop_adult_change_fee

        if self.re_shop_adult_price is not None:
            result['re_shop_adult_price'] = self.re_shop_adult_price

        if self.re_shop_adult_price_gap is not None:
            result['re_shop_adult_price_gap'] = self.re_shop_adult_price_gap

        if self.re_shop_child_change_fee is not None:
            result['re_shop_child_change_fee'] = self.re_shop_child_change_fee

        if self.re_shop_child_price is not None:
            result['re_shop_child_price'] = self.re_shop_child_price

        if self.re_shop_child_price_gap is not None:
            result['re_shop_child_price_gap'] = self.re_shop_child_price_gap

        if self.re_shop_inf_change_fee is not None:
            result['re_shop_inf_change_fee'] = self.re_shop_inf_change_fee

        if self.re_shop_inf_price is not None:
            result['re_shop_inf_price'] = self.re_shop_inf_price

        if self.re_shop_inf_price_gap is not None:
            result['re_shop_inf_price_gap'] = self.re_shop_inf_price_gap

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('re_shop_adult_change_fee') is not None:
            self.re_shop_adult_change_fee = m.get('re_shop_adult_change_fee')

        if m.get('re_shop_adult_price') is not None:
            self.re_shop_adult_price = m.get('re_shop_adult_price')

        if m.get('re_shop_adult_price_gap') is not None:
            self.re_shop_adult_price_gap = m.get('re_shop_adult_price_gap')

        if m.get('re_shop_child_change_fee') is not None:
            self.re_shop_child_change_fee = m.get('re_shop_child_change_fee')

        if m.get('re_shop_child_price') is not None:
            self.re_shop_child_price = m.get('re_shop_child_price')

        if m.get('re_shop_child_price_gap') is not None:
            self.re_shop_child_price_gap = m.get('re_shop_child_price_gap')

        if m.get('re_shop_inf_change_fee') is not None:
            self.re_shop_inf_change_fee = m.get('re_shop_inf_change_fee')

        if m.get('re_shop_inf_price') is not None:
            self.re_shop_inf_price = m.get('re_shop_inf_price')

        if m.get('re_shop_inf_price_gap') is not None:
            self.re_shop_inf_price_gap = m.get('re_shop_inf_price_gap')

        return self

class FlightModifyOtaSearchV2ResponseBodyModuleAgentInfosCabinClassInfo(DaraModel):
    def __init__(
        self,
        cabin_class: str = None,
        class_name: str = None,
        inner_cabin_class: int = None,
        quantity: str = None,
    ):
        self.cabin_class = cabin_class
        self.class_name = class_name
        self.inner_cabin_class = inner_cabin_class
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.class_name is not None:
            result['class_name'] = self.class_name

        if self.inner_cabin_class is not None:
            result['inner_cabin_class'] = self.inner_cabin_class

        if self.quantity is not None:
            result['quantity'] = self.quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('class_name') is not None:
            self.class_name = m.get('class_name')

        if m.get('inner_cabin_class') is not None:
            self.inner_cabin_class = m.get('inner_cabin_class')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        return self

