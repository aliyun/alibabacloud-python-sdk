# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IntlFlightRefundDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.IntlFlightRefundDetailResponseBodyModule = None,
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
            temp_model = main_models.IntlFlightRefundDetailResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class IntlFlightRefundDetailResponseBodyModule(DaraModel):
    def __init__(
        self,
        passenge_refund_fee_detail_list: List[main_models.IntlFlightRefundDetailResponseBodyModulePassengeRefundFeeDetailList] = None,
        passenger_list: List[main_models.IntlFlightRefundDetailResponseBodyModulePassengerList] = None,
        refund_order_info: main_models.IntlFlightRefundDetailResponseBodyModuleRefundOrderInfo = None,
        segment_list: List[main_models.IntlFlightRefundDetailResponseBodyModuleSegmentList] = None,
    ):
        self.passenge_refund_fee_detail_list = passenge_refund_fee_detail_list
        self.passenger_list = passenger_list
        self.refund_order_info = refund_order_info
        self.segment_list = segment_list

    def validate(self):
        if self.passenge_refund_fee_detail_list:
            for v1 in self.passenge_refund_fee_detail_list:
                 if v1:
                    v1.validate()
        if self.passenger_list:
            for v1 in self.passenger_list:
                 if v1:
                    v1.validate()
        if self.refund_order_info:
            self.refund_order_info.validate()
        if self.segment_list:
            for v1 in self.segment_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['passenge_refund_fee_detail_list'] = []
        if self.passenge_refund_fee_detail_list is not None:
            for k1 in self.passenge_refund_fee_detail_list:
                result['passenge_refund_fee_detail_list'].append(k1.to_map() if k1 else None)

        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k1 in self.passenger_list:
                result['passenger_list'].append(k1.to_map() if k1 else None)

        if self.refund_order_info is not None:
            result['refund_order_info'] = self.refund_order_info.to_map()

        result['segment_list'] = []
        if self.segment_list is not None:
            for k1 in self.segment_list:
                result['segment_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.passenge_refund_fee_detail_list = []
        if m.get('passenge_refund_fee_detail_list') is not None:
            for k1 in m.get('passenge_refund_fee_detail_list'):
                temp_model = main_models.IntlFlightRefundDetailResponseBodyModulePassengeRefundFeeDetailList()
                self.passenge_refund_fee_detail_list.append(temp_model.from_map(k1))

        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k1 in m.get('passenger_list'):
                temp_model = main_models.IntlFlightRefundDetailResponseBodyModulePassengerList()
                self.passenger_list.append(temp_model.from_map(k1))

        if m.get('refund_order_info') is not None:
            temp_model = main_models.IntlFlightRefundDetailResponseBodyModuleRefundOrderInfo()
            self.refund_order_info = temp_model.from_map(m.get('refund_order_info'))

        self.segment_list = []
        if m.get('segment_list') is not None:
            for k1 in m.get('segment_list'):
                temp_model = main_models.IntlFlightRefundDetailResponseBodyModuleSegmentList()
                self.segment_list.append(temp_model.from_map(k1))

        return self

class IntlFlightRefundDetailResponseBodyModuleSegmentList(DaraModel):
    def __init__(
        self,
        airline_info: main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListAirlineInfo = None,
        arr_airport_info: main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListArrAirportInfo = None,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        dep_airport_info: main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListDepAirportInfo = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        duration: int = None,
        flight_no: str = None,
        flight_share_info: main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListFlightShareInfo = None,
        flight_size: str = None,
        flight_stop_info_list: List[main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListFlightStopInfoList] = None,
        flight_type: str = None,
        journey_index: int = None,
        luggage_direct_info: main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListLuggageDirectInfo = None,
        manufacturer: str = None,
        meal_desc: str = None,
        one_more: int = None,
        one_more_show: str = None,
        segment_index: int = None,
        segment_key: str = None,
        segment_visa_remark: main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListSegmentVisaRemark = None,
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
            temp_model = main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListAirlineInfo()
            self.airline_info = temp_model.from_map(m.get('airline_info'))

        if m.get('arr_airport_info') is not None:
            temp_model = main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListArrAirportInfo()
            self.arr_airport_info = temp_model.from_map(m.get('arr_airport_info'))

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_airport_info') is not None:
            temp_model = main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListDepAirportInfo()
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
            temp_model = main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListFlightShareInfo()
            self.flight_share_info = temp_model.from_map(m.get('flight_share_info'))

        if m.get('flight_size') is not None:
            self.flight_size = m.get('flight_size')

        self.flight_stop_info_list = []
        if m.get('flight_stop_info_list') is not None:
            for k1 in m.get('flight_stop_info_list'):
                temp_model = main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListFlightStopInfoList()
                self.flight_stop_info_list.append(temp_model.from_map(k1))

        if m.get('flight_type') is not None:
            self.flight_type = m.get('flight_type')

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('luggage_direct_info') is not None:
            temp_model = main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListLuggageDirectInfo()
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
            temp_model = main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListSegmentVisaRemark()
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

class IntlFlightRefundDetailResponseBodyModuleSegmentListSegmentVisaRemark(DaraModel):
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

class IntlFlightRefundDetailResponseBodyModuleSegmentListLuggageDirectInfo(DaraModel):
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

class IntlFlightRefundDetailResponseBodyModuleSegmentListFlightStopInfoList(DaraModel):
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

class IntlFlightRefundDetailResponseBodyModuleSegmentListFlightShareInfo(DaraModel):
    def __init__(
        self,
        operating_airline_info: main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListFlightShareInfoOperatingAirlineInfo = None,
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
            temp_model = main_models.IntlFlightRefundDetailResponseBodyModuleSegmentListFlightShareInfoOperatingAirlineInfo()
            self.operating_airline_info = temp_model.from_map(m.get('operating_airline_info'))

        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')

        return self

class IntlFlightRefundDetailResponseBodyModuleSegmentListFlightShareInfoOperatingAirlineInfo(DaraModel):
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

class IntlFlightRefundDetailResponseBodyModuleSegmentListDepAirportInfo(DaraModel):
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

class IntlFlightRefundDetailResponseBodyModuleSegmentListArrAirportInfo(DaraModel):
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

class IntlFlightRefundDetailResponseBodyModuleSegmentListAirlineInfo(DaraModel):
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

class IntlFlightRefundDetailResponseBodyModuleRefundOrderInfo(DaraModel):
    def __init__(
        self,
        apply_time: str = None,
        close_reason: str = None,
        handing_amount: int = None,
        out_refund_apply_id: str = None,
        reason_code: str = None,
        reason_desc: str = None,
        refund_amount: int = None,
        refund_apply_id: str = None,
        relation_refund_apply_id: int = None,
        status: int = None,
        success_time: str = None,
        voluntary: bool = None,
    ):
        self.apply_time = apply_time
        self.close_reason = close_reason
        self.handing_amount = handing_amount
        self.out_refund_apply_id = out_refund_apply_id
        self.reason_code = reason_code
        self.reason_desc = reason_desc
        self.refund_amount = refund_amount
        self.refund_apply_id = refund_apply_id
        self.relation_refund_apply_id = relation_refund_apply_id
        self.status = status
        self.success_time = success_time
        self.voluntary = voluntary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_time is not None:
            result['apply_time'] = self.apply_time

        if self.close_reason is not None:
            result['close_reason'] = self.close_reason

        if self.handing_amount is not None:
            result['handing_amount'] = self.handing_amount

        if self.out_refund_apply_id is not None:
            result['out_refund_apply_id'] = self.out_refund_apply_id

        if self.reason_code is not None:
            result['reason_code'] = self.reason_code

        if self.reason_desc is not None:
            result['reason_desc'] = self.reason_desc

        if self.refund_amount is not None:
            result['refund_amount'] = self.refund_amount

        if self.refund_apply_id is not None:
            result['refund_apply_id'] = self.refund_apply_id

        if self.relation_refund_apply_id is not None:
            result['relation_refund_apply_id'] = self.relation_refund_apply_id

        if self.status is not None:
            result['status'] = self.status

        if self.success_time is not None:
            result['success_time'] = self.success_time

        if self.voluntary is not None:
            result['voluntary'] = self.voluntary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_time') is not None:
            self.apply_time = m.get('apply_time')

        if m.get('close_reason') is not None:
            self.close_reason = m.get('close_reason')

        if m.get('handing_amount') is not None:
            self.handing_amount = m.get('handing_amount')

        if m.get('out_refund_apply_id') is not None:
            self.out_refund_apply_id = m.get('out_refund_apply_id')

        if m.get('reason_code') is not None:
            self.reason_code = m.get('reason_code')

        if m.get('reason_desc') is not None:
            self.reason_desc = m.get('reason_desc')

        if m.get('refund_amount') is not None:
            self.refund_amount = m.get('refund_amount')

        if m.get('refund_apply_id') is not None:
            self.refund_apply_id = m.get('refund_apply_id')

        if m.get('relation_refund_apply_id') is not None:
            self.relation_refund_apply_id = m.get('relation_refund_apply_id')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('success_time') is not None:
            self.success_time = m.get('success_time')

        if m.get('voluntary') is not None:
            self.voluntary = m.get('voluntary')

        return self

class IntlFlightRefundDetailResponseBodyModulePassengerList(DaraModel):
    def __init__(
        self,
        birthday: str = None,
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
        self.birthday = birthday
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
        if self.birthday is not None:
            result['birthday'] = self.birthday

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
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

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

class IntlFlightRefundDetailResponseBodyModulePassengeRefundFeeDetailList(DaraModel):
    def __init__(
        self,
        passenger_id: int = None,
        refund_fee_detail: main_models.IntlFlightRefundDetailResponseBodyModulePassengeRefundFeeDetailListRefundFeeDetail = None,
        ticket_list: List[main_models.IntlFlightRefundDetailResponseBodyModulePassengeRefundFeeDetailListTicketList] = None,
    ):
        self.passenger_id = passenger_id
        self.refund_fee_detail = refund_fee_detail
        self.ticket_list = ticket_list

    def validate(self):
        if self.refund_fee_detail:
            self.refund_fee_detail.validate()
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

        if self.refund_fee_detail is not None:
            result['refund_fee_detail'] = self.refund_fee_detail.to_map()

        result['ticket_list'] = []
        if self.ticket_list is not None:
            for k1 in self.ticket_list:
                result['ticket_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('refund_fee_detail') is not None:
            temp_model = main_models.IntlFlightRefundDetailResponseBodyModulePassengeRefundFeeDetailListRefundFeeDetail()
            self.refund_fee_detail = temp_model.from_map(m.get('refund_fee_detail'))

        self.ticket_list = []
        if m.get('ticket_list') is not None:
            for k1 in m.get('ticket_list'):
                temp_model = main_models.IntlFlightRefundDetailResponseBodyModulePassengeRefundFeeDetailListTicketList()
                self.ticket_list.append(temp_model.from_map(k1))

        return self

class IntlFlightRefundDetailResponseBodyModulePassengeRefundFeeDetailListTicketList(DaraModel):
    def __init__(
        self,
        segment_key_list: List[str] = None,
        ticket_no: str = None,
    ):
        self.segment_key_list = segment_key_list
        self.ticket_no = ticket_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.segment_key_list is not None:
            result['segment_key_list'] = self.segment_key_list

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('segment_key_list') is not None:
            self.segment_key_list = m.get('segment_key_list')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        return self

class IntlFlightRefundDetailResponseBodyModulePassengeRefundFeeDetailListRefundFeeDetail(DaraModel):
    def __init__(
        self,
        already_used_total_amount: int = None,
        non_refundable_re_shop_handling_fee: int = None,
        non_refundable_re_shop_upgrade_fee: int = None,
        non_refundable_tax_diff_fee: int = None,
        re_shop_refund_amount: int = None,
        re_shop_service_refund_amount: int = None,
        re_shop_upgrade_refund_amount: int = None,
        refund_re_shop_fee_detail_list: List[main_models.IntlFlightRefundDetailResponseBodyModulePassengeRefundFeeDetailListRefundFeeDetailRefundReShopFeeDetailList] = None,
        refund_tax_diff_amount: int = None,
        refund_tax_fee: int = None,
        refund_ticket_fee: int = None,
        tax_refund_amount: int = None,
        ticket_refund_amount: int = None,
        total_refund_amount: int = None,
    ):
        self.already_used_total_amount = already_used_total_amount
        self.non_refundable_re_shop_handling_fee = non_refundable_re_shop_handling_fee
        self.non_refundable_re_shop_upgrade_fee = non_refundable_re_shop_upgrade_fee
        self.non_refundable_tax_diff_fee = non_refundable_tax_diff_fee
        self.re_shop_refund_amount = re_shop_refund_amount
        self.re_shop_service_refund_amount = re_shop_service_refund_amount
        self.re_shop_upgrade_refund_amount = re_shop_upgrade_refund_amount
        self.refund_re_shop_fee_detail_list = refund_re_shop_fee_detail_list
        self.refund_tax_diff_amount = refund_tax_diff_amount
        self.refund_tax_fee = refund_tax_fee
        self.refund_ticket_fee = refund_ticket_fee
        self.tax_refund_amount = tax_refund_amount
        self.ticket_refund_amount = ticket_refund_amount
        self.total_refund_amount = total_refund_amount

    def validate(self):
        if self.refund_re_shop_fee_detail_list:
            for v1 in self.refund_re_shop_fee_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.already_used_total_amount is not None:
            result['already_used_total_amount'] = self.already_used_total_amount

        if self.non_refundable_re_shop_handling_fee is not None:
            result['non_refundable_re_shop_handling_fee'] = self.non_refundable_re_shop_handling_fee

        if self.non_refundable_re_shop_upgrade_fee is not None:
            result['non_refundable_re_shop_upgrade_fee'] = self.non_refundable_re_shop_upgrade_fee

        if self.non_refundable_tax_diff_fee is not None:
            result['non_refundable_tax_diff_fee'] = self.non_refundable_tax_diff_fee

        if self.re_shop_refund_amount is not None:
            result['re_shop_refund_amount'] = self.re_shop_refund_amount

        if self.re_shop_service_refund_amount is not None:
            result['re_shop_service_refund_amount'] = self.re_shop_service_refund_amount

        if self.re_shop_upgrade_refund_amount is not None:
            result['re_shop_upgrade_refund_amount'] = self.re_shop_upgrade_refund_amount

        result['refund_re_shop_fee_detail_list'] = []
        if self.refund_re_shop_fee_detail_list is not None:
            for k1 in self.refund_re_shop_fee_detail_list:
                result['refund_re_shop_fee_detail_list'].append(k1.to_map() if k1 else None)

        if self.refund_tax_diff_amount is not None:
            result['refund_tax_diff_amount'] = self.refund_tax_diff_amount

        if self.refund_tax_fee is not None:
            result['refund_tax_fee'] = self.refund_tax_fee

        if self.refund_ticket_fee is not None:
            result['refund_ticket_fee'] = self.refund_ticket_fee

        if self.tax_refund_amount is not None:
            result['tax_refund_amount'] = self.tax_refund_amount

        if self.ticket_refund_amount is not None:
            result['ticket_refund_amount'] = self.ticket_refund_amount

        if self.total_refund_amount is not None:
            result['total_refund_amount'] = self.total_refund_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('already_used_total_amount') is not None:
            self.already_used_total_amount = m.get('already_used_total_amount')

        if m.get('non_refundable_re_shop_handling_fee') is not None:
            self.non_refundable_re_shop_handling_fee = m.get('non_refundable_re_shop_handling_fee')

        if m.get('non_refundable_re_shop_upgrade_fee') is not None:
            self.non_refundable_re_shop_upgrade_fee = m.get('non_refundable_re_shop_upgrade_fee')

        if m.get('non_refundable_tax_diff_fee') is not None:
            self.non_refundable_tax_diff_fee = m.get('non_refundable_tax_diff_fee')

        if m.get('re_shop_refund_amount') is not None:
            self.re_shop_refund_amount = m.get('re_shop_refund_amount')

        if m.get('re_shop_service_refund_amount') is not None:
            self.re_shop_service_refund_amount = m.get('re_shop_service_refund_amount')

        if m.get('re_shop_upgrade_refund_amount') is not None:
            self.re_shop_upgrade_refund_amount = m.get('re_shop_upgrade_refund_amount')

        self.refund_re_shop_fee_detail_list = []
        if m.get('refund_re_shop_fee_detail_list') is not None:
            for k1 in m.get('refund_re_shop_fee_detail_list'):
                temp_model = main_models.IntlFlightRefundDetailResponseBodyModulePassengeRefundFeeDetailListRefundFeeDetailRefundReShopFeeDetailList()
                self.refund_re_shop_fee_detail_list.append(temp_model.from_map(k1))

        if m.get('refund_tax_diff_amount') is not None:
            self.refund_tax_diff_amount = m.get('refund_tax_diff_amount')

        if m.get('refund_tax_fee') is not None:
            self.refund_tax_fee = m.get('refund_tax_fee')

        if m.get('refund_ticket_fee') is not None:
            self.refund_ticket_fee = m.get('refund_ticket_fee')

        if m.get('tax_refund_amount') is not None:
            self.tax_refund_amount = m.get('tax_refund_amount')

        if m.get('ticket_refund_amount') is not None:
            self.ticket_refund_amount = m.get('ticket_refund_amount')

        if m.get('total_refund_amount') is not None:
            self.total_refund_amount = m.get('total_refund_amount')

        return self

class IntlFlightRefundDetailResponseBodyModulePassengeRefundFeeDetailListRefundFeeDetailRefundReShopFeeDetailList(DaraModel):
    def __init__(
        self,
        non_refundable_re_shop_handling_fee: int = None,
        non_refundable_re_shop_upgrade_fee: int = None,
        non_refundable_tax_diff_fee: int = None,
        re_shop_apply_id: str = None,
        re_shop_refund_amount: int = None,
        re_shop_service_refund_amount: int = None,
        re_shop_upgrade_refund_amount: int = None,
        refund_tax_diff_amount: int = None,
    ):
        self.non_refundable_re_shop_handling_fee = non_refundable_re_shop_handling_fee
        self.non_refundable_re_shop_upgrade_fee = non_refundable_re_shop_upgrade_fee
        self.non_refundable_tax_diff_fee = non_refundable_tax_diff_fee
        self.re_shop_apply_id = re_shop_apply_id
        self.re_shop_refund_amount = re_shop_refund_amount
        self.re_shop_service_refund_amount = re_shop_service_refund_amount
        self.re_shop_upgrade_refund_amount = re_shop_upgrade_refund_amount
        self.refund_tax_diff_amount = refund_tax_diff_amount

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.non_refundable_re_shop_handling_fee is not None:
            result['non_refundable_re_shop_handling_fee'] = self.non_refundable_re_shop_handling_fee

        if self.non_refundable_re_shop_upgrade_fee is not None:
            result['non_refundable_re_shop_upgrade_fee'] = self.non_refundable_re_shop_upgrade_fee

        if self.non_refundable_tax_diff_fee is not None:
            result['non_refundable_tax_diff_fee'] = self.non_refundable_tax_diff_fee

        if self.re_shop_apply_id is not None:
            result['re_shop_apply_id'] = self.re_shop_apply_id

        if self.re_shop_refund_amount is not None:
            result['re_shop_refund_amount'] = self.re_shop_refund_amount

        if self.re_shop_service_refund_amount is not None:
            result['re_shop_service_refund_amount'] = self.re_shop_service_refund_amount

        if self.re_shop_upgrade_refund_amount is not None:
            result['re_shop_upgrade_refund_amount'] = self.re_shop_upgrade_refund_amount

        if self.refund_tax_diff_amount is not None:
            result['refund_tax_diff_amount'] = self.refund_tax_diff_amount

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('non_refundable_re_shop_handling_fee') is not None:
            self.non_refundable_re_shop_handling_fee = m.get('non_refundable_re_shop_handling_fee')

        if m.get('non_refundable_re_shop_upgrade_fee') is not None:
            self.non_refundable_re_shop_upgrade_fee = m.get('non_refundable_re_shop_upgrade_fee')

        if m.get('non_refundable_tax_diff_fee') is not None:
            self.non_refundable_tax_diff_fee = m.get('non_refundable_tax_diff_fee')

        if m.get('re_shop_apply_id') is not None:
            self.re_shop_apply_id = m.get('re_shop_apply_id')

        if m.get('re_shop_refund_amount') is not None:
            self.re_shop_refund_amount = m.get('re_shop_refund_amount')

        if m.get('re_shop_service_refund_amount') is not None:
            self.re_shop_service_refund_amount = m.get('re_shop_service_refund_amount')

        if m.get('re_shop_upgrade_refund_amount') is not None:
            self.re_shop_upgrade_refund_amount = m.get('re_shop_upgrade_refund_amount')

        if m.get('refund_tax_diff_amount') is not None:
            self.refund_tax_diff_amount = m.get('refund_tax_diff_amount')

        return self

