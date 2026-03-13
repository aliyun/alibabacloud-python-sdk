# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightListingSearchV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.FlightListingSearchV2ResponseBodyModule = None,
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
            temp_model = main_models.FlightListingSearchV2ResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightListingSearchV2ResponseBodyModule(DaraModel):
    def __init__(
        self,
        flight_item_list: List[main_models.FlightListingSearchV2ResponseBodyModuleFlightItemList] = None,
        search_mode: int = None,
        trip_type: int = None,
    ):
        self.flight_item_list = flight_item_list
        self.search_mode = search_mode
        self.trip_type = trip_type

    def validate(self):
        if self.flight_item_list:
            for v1 in self.flight_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['flight_item_list'] = []
        if self.flight_item_list is not None:
            for k1 in self.flight_item_list:
                result['flight_item_list'].append(k1.to_map() if k1 else None)

        if self.search_mode is not None:
            result['search_mode'] = self.search_mode

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_item_list = []
        if m.get('flight_item_list') is not None:
            for k1 in m.get('flight_item_list'):
                temp_model = main_models.FlightListingSearchV2ResponseBodyModuleFlightItemList()
                self.flight_item_list.append(temp_model.from_map(k1))

        if m.get('search_mode') is not None:
            self.search_mode = m.get('search_mode')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        return self

class FlightListingSearchV2ResponseBodyModuleFlightItemList(DaraModel):
    def __init__(
        self,
        best_price_item: main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListBestPriceItem = None,
        flight_journey_infos: List[main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfos] = None,
        item_list: List[main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListItemList] = None,
    ):
        self.best_price_item = best_price_item
        self.flight_journey_infos = flight_journey_infos
        self.item_list = item_list

    def validate(self):
        if self.best_price_item:
            self.best_price_item.validate()
        if self.flight_journey_infos:
            for v1 in self.flight_journey_infos:
                 if v1:
                    v1.validate()
        if self.item_list:
            for v1 in self.item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.best_price_item is not None:
            result['best_price_item'] = self.best_price_item.to_map()

        result['flight_journey_infos'] = []
        if self.flight_journey_infos is not None:
            for k1 in self.flight_journey_infos:
                result['flight_journey_infos'].append(k1.to_map() if k1 else None)

        result['item_list'] = []
        if self.item_list is not None:
            for k1 in self.item_list:
                result['item_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('best_price_item') is not None:
            temp_model = main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListBestPriceItem()
            self.best_price_item = temp_model.from_map(m.get('best_price_item'))

        self.flight_journey_infos = []
        if m.get('flight_journey_infos') is not None:
            for k1 in m.get('flight_journey_infos'):
                temp_model = main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfos()
                self.flight_journey_infos.append(temp_model.from_map(k1))

        self.item_list = []
        if m.get('item_list') is not None:
            for k1 in m.get('item_list'):
                temp_model = main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListItemList()
                self.item_list.append(temp_model.from_map(k1))

        return self

class FlightListingSearchV2ResponseBodyModuleFlightItemListItemList(DaraModel):
    def __init__(
        self,
        flight_rule_infos: Dict[str, main_models.ModuleFlightItemListItemListFlightRuleInfosValue] = None,
        item_id: str = None,
        shopping_item_map: Dict[str, main_models.ModuleFlightItemListItemListShoppingItemMapValue] = None,
        sub_item_position_map: Dict[str, List[main_models.ModuleFlightItemListItemListSubItemPositionMapValue]] = None,
        sub_items: List[main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListItemListSubItems] = None,
    ):
        self.flight_rule_infos = flight_rule_infos
        self.item_id = item_id
        self.shopping_item_map = shopping_item_map
        self.sub_item_position_map = sub_item_position_map
        self.sub_items = sub_items

    def validate(self):
        if self.flight_rule_infos:
            for v1 in self.flight_rule_infos.values():
                 if v1:
                    v1.validate()
        if self.shopping_item_map:
            for v1 in self.shopping_item_map.values():
                 if v1:
                    v1.validate()
        if self.sub_item_position_map:
            for v1 in self.sub_item_position_map.values():
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.sub_items:
            for v1 in self.sub_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['flight_rule_infos'] = {}
        if self.flight_rule_infos is not None:
            for k1, v1 in self.flight_rule_infos.items():
                result['flight_rule_infos'][k1] = v1.to_map() if v1 else None

        if self.item_id is not None:
            result['item_id'] = self.item_id

        result['shopping_item_map'] = {}
        if self.shopping_item_map is not None:
            for k1, v1 in self.shopping_item_map.items():
                result['shopping_item_map'][k1] = v1.to_map() if v1 else None

        result['sub_item_position_map'] = {}
        if self.sub_item_position_map is not None:
            for k1, v1 in self.sub_item_position_map.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['sub_item_position_map'][k1] = l1

        result['sub_items'] = []
        if self.sub_items is not None:
            for k1 in self.sub_items:
                result['sub_items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_rule_infos = {}
        if m.get('flight_rule_infos') is not None:
            for k1, v1 in m.get('flight_rule_infos').items():
                temp_model = main_models.ModuleFlightItemListItemListFlightRuleInfosValue()
                self.flight_rule_infos[k1] = temp_model.from_map(v1)

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        self.shopping_item_map = {}
        if m.get('shopping_item_map') is not None:
            for k1, v1 in m.get('shopping_item_map').items():
                temp_model = main_models.ModuleFlightItemListItemListShoppingItemMapValue()
                self.shopping_item_map[k1] = temp_model.from_map(v1)

        self.sub_item_position_map = {}
        if m.get('sub_item_position_map') is not None:
            for k1, v1 in m.get('sub_item_position_map').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.ModuleFlightItemListItemListSubItemPositionMapValue()
                    l1.append(temp_model.from_map(k2))
                self.sub_item_position_map[k1] = l1

        self.sub_items = []
        if m.get('sub_items') is not None:
            for k1 in m.get('sub_items'):
                temp_model = main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListItemListSubItems()
                self.sub_items.append(temp_model.from_map(k1))

        return self

class FlightListingSearchV2ResponseBodyModuleFlightItemListItemListSubItems(DaraModel):
    def __init__(
        self,
        shopping_item_map: Dict[str, main_models.ModuleFlightItemListItemListSubItemsShoppingItemMapValue] = None,
        tag: str = None,
        uniq_key: str = None,
    ):
        self.shopping_item_map = shopping_item_map
        self.tag = tag
        self.uniq_key = uniq_key

    def validate(self):
        if self.shopping_item_map:
            for v1 in self.shopping_item_map.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['shopping_item_map'] = {}
        if self.shopping_item_map is not None:
            for k1, v1 in self.shopping_item_map.items():
                result['shopping_item_map'][k1] = v1.to_map() if v1 else None

        if self.tag is not None:
            result['tag'] = self.tag

        if self.uniq_key is not None:
            result['uniq_key'] = self.uniq_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.shopping_item_map = {}
        if m.get('shopping_item_map') is not None:
            for k1, v1 in m.get('shopping_item_map').items():
                temp_model = main_models.ModuleFlightItemListItemListSubItemsShoppingItemMapValue()
                self.shopping_item_map[k1] = temp_model.from_map(v1)

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        if m.get('uniq_key') is not None:
            self.uniq_key = m.get('uniq_key')

        return self

class FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfos(DaraModel):
    def __init__(
        self,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        duration: int = None,
        extensions: Dict[str, str] = None,
        flight_segment_infos: List[main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfos] = None,
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
        self.extensions = extensions
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

        if self.extensions is not None:
            result['extensions'] = self.extensions

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

        if m.get('extensions') is not None:
            self.extensions = m.get('extensions')

        self.flight_segment_infos = []
        if m.get('flight_segment_infos') is not None:
            for k1 in m.get('flight_segment_infos'):
                temp_model = main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfos()
                self.flight_segment_infos.append(temp_model.from_map(k1))

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('transfer_time') is not None:
            self.transfer_time = m.get('transfer_time')

        return self

class FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfos(DaraModel):
    def __init__(
        self,
        airline_info: main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosAirlineInfo = None,
        arr_airport_info: main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosArrAirportInfo = None,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        baggage_desc: str = None,
        dep_airport_info: main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosDepAirportInfo = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        duration: int = None,
        extra_info: Dict[str, Any] = None,
        flight_no: str = None,
        flight_share_info: main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosFlightShareInfo = None,
        flight_size: str = None,
        flight_stop_info: main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosFlightStopInfo = None,
        flight_type: str = None,
        manufacturer: str = None,
        meal_desc: str = None,
        miles: int = None,
        on_time_rate: str = None,
        one_more: int = None,
        one_more_show: str = None,
        segment_index: int = None,
        share: bool = None,
        short_flight_size: str = None,
        stop: bool = None,
        total_time: str = None,
        transfer_time: str = None,
        transfer_time_number: int = None,
    ):
        self.airline_info = airline_info
        self.arr_airport_info = arr_airport_info
        self.arr_city_code = arr_city_code
        self.arr_city_name = arr_city_name
        self.arr_time = arr_time
        self.baggage_desc = baggage_desc
        self.dep_airport_info = dep_airport_info
        self.dep_city_code = dep_city_code
        self.dep_city_name = dep_city_name
        self.dep_time = dep_time
        # duration
        self.duration = duration
        self.extra_info = extra_info
        self.flight_no = flight_no
        self.flight_share_info = flight_share_info
        self.flight_size = flight_size
        self.flight_stop_info = flight_stop_info
        self.flight_type = flight_type
        self.manufacturer = manufacturer
        self.meal_desc = meal_desc
        self.miles = miles
        self.on_time_rate = on_time_rate
        self.one_more = one_more
        self.one_more_show = one_more_show
        self.segment_index = segment_index
        self.share = share
        self.short_flight_size = short_flight_size
        self.stop = stop
        self.total_time = total_time
        self.transfer_time = transfer_time
        self.transfer_time_number = transfer_time_number

    def validate(self):
        if self.airline_info:
            self.airline_info.validate()
        if self.arr_airport_info:
            self.arr_airport_info.validate()
        if self.dep_airport_info:
            self.dep_airport_info.validate()
        if self.flight_share_info:
            self.flight_share_info.validate()
        if self.flight_stop_info:
            self.flight_stop_info.validate()

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

        if self.baggage_desc is not None:
            result['baggage_desc'] = self.baggage_desc

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

        if self.extra_info is not None:
            result['extra_info'] = self.extra_info

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.flight_share_info is not None:
            result['flight_share_info'] = self.flight_share_info.to_map()

        if self.flight_size is not None:
            result['flight_size'] = self.flight_size

        if self.flight_stop_info is not None:
            result['flight_stop_info'] = self.flight_stop_info.to_map()

        if self.flight_type is not None:
            result['flight_type'] = self.flight_type

        if self.manufacturer is not None:
            result['manufacturer'] = self.manufacturer

        if self.meal_desc is not None:
            result['meal_desc'] = self.meal_desc

        if self.miles is not None:
            result['miles'] = self.miles

        if self.on_time_rate is not None:
            result['on_time_rate'] = self.on_time_rate

        if self.one_more is not None:
            result['one_more'] = self.one_more

        if self.one_more_show is not None:
            result['one_more_show'] = self.one_more_show

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.share is not None:
            result['share'] = self.share

        if self.short_flight_size is not None:
            result['short_flight_size'] = self.short_flight_size

        if self.stop is not None:
            result['stop'] = self.stop

        if self.total_time is not None:
            result['total_time'] = self.total_time

        if self.transfer_time is not None:
            result['transfer_time'] = self.transfer_time

        if self.transfer_time_number is not None:
            result['transfer_time_number'] = self.transfer_time_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_info') is not None:
            temp_model = main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosAirlineInfo()
            self.airline_info = temp_model.from_map(m.get('airline_info'))

        if m.get('arr_airport_info') is not None:
            temp_model = main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosArrAirportInfo()
            self.arr_airport_info = temp_model.from_map(m.get('arr_airport_info'))

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('baggage_desc') is not None:
            self.baggage_desc = m.get('baggage_desc')

        if m.get('dep_airport_info') is not None:
            temp_model = main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosDepAirportInfo()
            self.dep_airport_info = temp_model.from_map(m.get('dep_airport_info'))

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('extra_info') is not None:
            self.extra_info = m.get('extra_info')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('flight_share_info') is not None:
            temp_model = main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosFlightShareInfo()
            self.flight_share_info = temp_model.from_map(m.get('flight_share_info'))

        if m.get('flight_size') is not None:
            self.flight_size = m.get('flight_size')

        if m.get('flight_stop_info') is not None:
            temp_model = main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosFlightStopInfo()
            self.flight_stop_info = temp_model.from_map(m.get('flight_stop_info'))

        if m.get('flight_type') is not None:
            self.flight_type = m.get('flight_type')

        if m.get('manufacturer') is not None:
            self.manufacturer = m.get('manufacturer')

        if m.get('meal_desc') is not None:
            self.meal_desc = m.get('meal_desc')

        if m.get('miles') is not None:
            self.miles = m.get('miles')

        if m.get('on_time_rate') is not None:
            self.on_time_rate = m.get('on_time_rate')

        if m.get('one_more') is not None:
            self.one_more = m.get('one_more')

        if m.get('one_more_show') is not None:
            self.one_more_show = m.get('one_more_show')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('share') is not None:
            self.share = m.get('share')

        if m.get('short_flight_size') is not None:
            self.short_flight_size = m.get('short_flight_size')

        if m.get('stop') is not None:
            self.stop = m.get('stop')

        if m.get('total_time') is not None:
            self.total_time = m.get('total_time')

        if m.get('transfer_time') is not None:
            self.transfer_time = m.get('transfer_time')

        if m.get('transfer_time_number') is not None:
            self.transfer_time_number = m.get('transfer_time_number')

        return self

class FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosFlightStopInfo(DaraModel):
    def __init__(
        self,
        stop_airport: str = None,
        stop_airport_name: str = None,
        stop_arr_term: str = None,
        stop_arr_time: str = None,
        stop_city_code: str = None,
        stop_city_name: str = None,
        stop_city_names: List[str] = None,
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
        self.stop_city_names = stop_city_names
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

        if self.stop_city_names is not None:
            result['stop_city_names'] = self.stop_city_names

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

        if m.get('stop_city_names') is not None:
            self.stop_city_names = m.get('stop_city_names')

        if m.get('stop_dep_term') is not None:
            self.stop_dep_term = m.get('stop_dep_term')

        if m.get('stop_dep_time') is not None:
            self.stop_dep_time = m.get('stop_dep_time')

        if m.get('stop_time') is not None:
            self.stop_time = m.get('stop_time')

        return self

class FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosFlightShareInfo(DaraModel):
    def __init__(
        self,
        operating_airline_info: main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosFlightShareInfoOperatingAirlineInfo = None,
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
            temp_model = main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosFlightShareInfoOperatingAirlineInfo()
            self.operating_airline_info = temp_model.from_map(m.get('operating_airline_info'))

        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')

        return self

class FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosFlightShareInfoOperatingAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_chinese_name: str = None,
        airline_chinese_short_name: str = None,
        airline_code: str = None,
        airline_icon: str = None,
        cheap_flight: bool = None,
    ):
        self.airline_chinese_name = airline_chinese_name
        self.airline_chinese_short_name = airline_chinese_short_name
        self.airline_code = airline_code
        self.airline_icon = airline_icon
        self.cheap_flight = cheap_flight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_chinese_name is not None:
            result['airline_chinese_name'] = self.airline_chinese_name

        if self.airline_chinese_short_name is not None:
            result['airline_chinese_short_name'] = self.airline_chinese_short_name

        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_icon is not None:
            result['airline_icon'] = self.airline_icon

        if self.cheap_flight is not None:
            result['cheap_flight'] = self.cheap_flight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_chinese_name') is not None:
            self.airline_chinese_name = m.get('airline_chinese_name')

        if m.get('airline_chinese_short_name') is not None:
            self.airline_chinese_short_name = m.get('airline_chinese_short_name')

        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_icon') is not None:
            self.airline_icon = m.get('airline_icon')

        if m.get('cheap_flight') is not None:
            self.cheap_flight = m.get('cheap_flight')

        return self

class FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosDepAirportInfo(DaraModel):
    def __init__(
        self,
        airport_code: str = None,
        airport_name: str = None,
        airport_name_color: str = None,
        airport_short_name: str = None,
        terminal: str = None,
    ):
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.airport_name_color = airport_name_color
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

        if self.airport_name_color is not None:
            result['airport_name_color'] = self.airport_name_color

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

        if m.get('airport_name_color') is not None:
            self.airport_name_color = m.get('airport_name_color')

        if m.get('airport_short_name') is not None:
            self.airport_short_name = m.get('airport_short_name')

        if m.get('terminal') is not None:
            self.terminal = m.get('terminal')

        return self

class FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosArrAirportInfo(DaraModel):
    def __init__(
        self,
        airport_code: str = None,
        airport_name: str = None,
        airport_name_color: str = None,
        airport_short_name: str = None,
        terminal: str = None,
    ):
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.airport_name_color = airport_name_color
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

        if self.airport_name_color is not None:
            result['airport_name_color'] = self.airport_name_color

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

        if m.get('airport_name_color') is not None:
            self.airport_name_color = m.get('airport_name_color')

        if m.get('airport_short_name') is not None:
            self.airport_short_name = m.get('airport_short_name')

        if m.get('terminal') is not None:
            self.terminal = m.get('terminal')

        return self

class FlightListingSearchV2ResponseBodyModuleFlightItemListFlightJourneyInfosFlightSegmentInfosAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_chinese_name: str = None,
        airline_chinese_short_name: str = None,
        airline_code: str = None,
        airline_icon: str = None,
        cheap_flight: bool = None,
    ):
        self.airline_chinese_name = airline_chinese_name
        self.airline_chinese_short_name = airline_chinese_short_name
        self.airline_code = airline_code
        self.airline_icon = airline_icon
        self.cheap_flight = cheap_flight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_chinese_name is not None:
            result['airline_chinese_name'] = self.airline_chinese_name

        if self.airline_chinese_short_name is not None:
            result['airline_chinese_short_name'] = self.airline_chinese_short_name

        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_icon is not None:
            result['airline_icon'] = self.airline_icon

        if self.cheap_flight is not None:
            result['cheap_flight'] = self.cheap_flight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_chinese_name') is not None:
            self.airline_chinese_name = m.get('airline_chinese_name')

        if m.get('airline_chinese_short_name') is not None:
            self.airline_chinese_short_name = m.get('airline_chinese_short_name')

        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_icon') is not None:
            self.airline_icon = m.get('airline_icon')

        if m.get('cheap_flight') is not None:
            self.cheap_flight = m.get('cheap_flight')

        return self

class FlightListingSearchV2ResponseBodyModuleFlightItemListBestPriceItem(DaraModel):
    def __init__(
        self,
        flight_rule_infos: Dict[str, main_models.ModuleFlightItemListBestPriceItemFlightRuleInfosValue] = None,
        item_id: str = None,
        shopping_item_map: Dict[str, main_models.ModuleFlightItemListBestPriceItemShoppingItemMapValue] = None,
        sub_item_position_map: Dict[str, List[main_models.ModuleFlightItemListBestPriceItemSubItemPositionMapValue]] = None,
        sub_items: List[main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListBestPriceItemSubItems] = None,
    ):
        self.flight_rule_infos = flight_rule_infos
        self.item_id = item_id
        self.shopping_item_map = shopping_item_map
        self.sub_item_position_map = sub_item_position_map
        self.sub_items = sub_items

    def validate(self):
        if self.flight_rule_infos:
            for v1 in self.flight_rule_infos.values():
                 if v1:
                    v1.validate()
        if self.shopping_item_map:
            for v1 in self.shopping_item_map.values():
                 if v1:
                    v1.validate()
        if self.sub_item_position_map:
            for v1 in self.sub_item_position_map.values():
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.sub_items:
            for v1 in self.sub_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['flight_rule_infos'] = {}
        if self.flight_rule_infos is not None:
            for k1, v1 in self.flight_rule_infos.items():
                result['flight_rule_infos'][k1] = v1.to_map() if v1 else None

        if self.item_id is not None:
            result['item_id'] = self.item_id

        result['shopping_item_map'] = {}
        if self.shopping_item_map is not None:
            for k1, v1 in self.shopping_item_map.items():
                result['shopping_item_map'][k1] = v1.to_map() if v1 else None

        result['sub_item_position_map'] = {}
        if self.sub_item_position_map is not None:
            for k1, v1 in self.sub_item_position_map.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['sub_item_position_map'][k1] = l1

        result['sub_items'] = []
        if self.sub_items is not None:
            for k1 in self.sub_items:
                result['sub_items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_rule_infos = {}
        if m.get('flight_rule_infos') is not None:
            for k1, v1 in m.get('flight_rule_infos').items():
                temp_model = main_models.ModuleFlightItemListBestPriceItemFlightRuleInfosValue()
                self.flight_rule_infos[k1] = temp_model.from_map(v1)

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        self.shopping_item_map = {}
        if m.get('shopping_item_map') is not None:
            for k1, v1 in m.get('shopping_item_map').items():
                temp_model = main_models.ModuleFlightItemListBestPriceItemShoppingItemMapValue()
                self.shopping_item_map[k1] = temp_model.from_map(v1)

        self.sub_item_position_map = {}
        if m.get('sub_item_position_map') is not None:
            for k1, v1 in m.get('sub_item_position_map').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.ModuleFlightItemListBestPriceItemSubItemPositionMapValue()
                    l1.append(temp_model.from_map(k2))
                self.sub_item_position_map[k1] = l1

        self.sub_items = []
        if m.get('sub_items') is not None:
            for k1 in m.get('sub_items'):
                temp_model = main_models.FlightListingSearchV2ResponseBodyModuleFlightItemListBestPriceItemSubItems()
                self.sub_items.append(temp_model.from_map(k1))

        return self

class FlightListingSearchV2ResponseBodyModuleFlightItemListBestPriceItemSubItems(DaraModel):
    def __init__(
        self,
        shopping_item_map: Dict[str, main_models.ModuleFlightItemListBestPriceItemSubItemsShoppingItemMapValue] = None,
        uniq_key: str = None,
    ):
        self.shopping_item_map = shopping_item_map
        self.uniq_key = uniq_key

    def validate(self):
        if self.shopping_item_map:
            for v1 in self.shopping_item_map.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['shopping_item_map'] = {}
        if self.shopping_item_map is not None:
            for k1, v1 in self.shopping_item_map.items():
                result['shopping_item_map'][k1] = v1.to_map() if v1 else None

        if self.uniq_key is not None:
            result['uniq_key'] = self.uniq_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.shopping_item_map = {}
        if m.get('shopping_item_map') is not None:
            for k1, v1 in m.get('shopping_item_map').items():
                temp_model = main_models.ModuleFlightItemListBestPriceItemSubItemsShoppingItemMapValue()
                self.shopping_item_map[k1] = temp_model.from_map(v1)

        if m.get('uniq_key') is not None:
            self.uniq_key = m.get('uniq_key')

        return self

