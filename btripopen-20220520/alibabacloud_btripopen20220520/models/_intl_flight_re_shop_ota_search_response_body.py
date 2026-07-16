# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IntlFlightReShopOtaSearchResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.IntlFlightReShopOtaSearchResponseBodyModule = None,
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
            temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class IntlFlightReShopOtaSearchResponseBodyModule(DaraModel):
    def __init__(
        self,
        flight_journey_infos: List[main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfos] = None,
        need_continue: bool = None,
        next_req_wait_time: int = None,
        re_shop_item_list: List[main_models.IntlFlightReShopOtaSearchResponseBodyModuleReShopItemList] = None,
        token: str = None,
    ):
        self.flight_journey_infos = flight_journey_infos
        self.need_continue = need_continue
        self.next_req_wait_time = next_req_wait_time
        self.re_shop_item_list = re_shop_item_list
        self.token = token

    def validate(self):
        if self.flight_journey_infos:
            for v1 in self.flight_journey_infos:
                 if v1:
                    v1.validate()
        if self.re_shop_item_list:
            for v1 in self.re_shop_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['flight_journey_infos'] = []
        if self.flight_journey_infos is not None:
            for k1 in self.flight_journey_infos:
                result['flight_journey_infos'].append(k1.to_map() if k1 else None)

        if self.need_continue is not None:
            result['need_continue'] = self.need_continue

        if self.next_req_wait_time is not None:
            result['next_req_wait_time'] = self.next_req_wait_time

        result['re_shop_item_list'] = []
        if self.re_shop_item_list is not None:
            for k1 in self.re_shop_item_list:
                result['re_shop_item_list'].append(k1.to_map() if k1 else None)

        if self.token is not None:
            result['token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_journey_infos = []
        if m.get('flight_journey_infos') is not None:
            for k1 in m.get('flight_journey_infos'):
                temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfos()
                self.flight_journey_infos.append(temp_model.from_map(k1))

        if m.get('need_continue') is not None:
            self.need_continue = m.get('need_continue')

        if m.get('next_req_wait_time') is not None:
            self.next_req_wait_time = m.get('next_req_wait_time')

        self.re_shop_item_list = []
        if m.get('re_shop_item_list') is not None:
            for k1 in m.get('re_shop_item_list'):
                temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleReShopItemList()
                self.re_shop_item_list.append(temp_model.from_map(k1))

        if m.get('token') is not None:
            self.token = m.get('token')

        return self

class IntlFlightReShopOtaSearchResponseBodyModuleReShopItemList(DaraModel):
    def __init__(
        self,
        item_id: str = None,
        item_type: str = None,
        shopping_item_map: Dict[str, main_models.ModuleReShopItemListShoppingItemMapValue] = None,
        sub_items: List[main_models.IntlFlightReShopOtaSearchResponseBodyModuleReShopItemListSubItems] = None,
    ):
        self.item_id = item_id
        self.item_type = item_type
        self.shopping_item_map = shopping_item_map
        self.sub_items = sub_items

    def validate(self):
        if self.shopping_item_map:
            for v1 in self.shopping_item_map.values():
                 if v1:
                    v1.validate()
        if self.sub_items:
            for v1 in self.sub_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.item_type is not None:
            result['item_type'] = self.item_type

        result['shopping_item_map'] = {}
        if self.shopping_item_map is not None:
            for k1, v1 in self.shopping_item_map.items():
                result['shopping_item_map'][k1] = v1.to_map() if v1 else None

        result['sub_items'] = []
        if self.sub_items is not None:
            for k1 in self.sub_items:
                result['sub_items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('item_type') is not None:
            self.item_type = m.get('item_type')

        self.shopping_item_map = {}
        if m.get('shopping_item_map') is not None:
            for k1, v1 in m.get('shopping_item_map').items():
                temp_model = main_models.ModuleReShopItemListShoppingItemMapValue()
                self.shopping_item_map[k1] = temp_model.from_map(v1)

        self.sub_items = []
        if m.get('sub_items') is not None:
            for k1 in m.get('sub_items'):
                temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleReShopItemListSubItems()
                self.sub_items.append(temp_model.from_map(k1))

        return self

class IntlFlightReShopOtaSearchResponseBodyModuleReShopItemListSubItems(DaraModel):
    def __init__(
        self,
        baggage_rule: main_models.IntlFlightReShopOtaSearchResponseBodyModuleReShopItemListSubItemsBaggageRule = None,
        discount_num: float = None,
        refund_change_rule: main_models.IntlFlightReShopOtaSearchResponseBodyModuleReShopItemListSubItemsRefundChangeRule = None,
        segment_keys: List[str] = None,
        segment_position_list: List[main_models.IntlFlightReShopOtaSearchResponseBodyModuleReShopItemListSubItemsSegmentPositionList] = None,
        shopping_item_map: Dict[str, main_models.ModuleReShopItemListSubItemsShoppingItemMapValue] = None,
        uniq_key: str = None,
    ):
        self.baggage_rule = baggage_rule
        self.discount_num = discount_num
        self.refund_change_rule = refund_change_rule
        self.segment_keys = segment_keys
        self.segment_position_list = segment_position_list
        self.shopping_item_map = shopping_item_map
        self.uniq_key = uniq_key

    def validate(self):
        if self.baggage_rule:
            self.baggage_rule.validate()
        if self.refund_change_rule:
            self.refund_change_rule.validate()
        if self.segment_position_list:
            for v1 in self.segment_position_list:
                 if v1:
                    v1.validate()
        if self.shopping_item_map:
            for v1 in self.shopping_item_map.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baggage_rule is not None:
            result['baggage_rule'] = self.baggage_rule.to_map()

        if self.discount_num is not None:
            result['discount_num'] = self.discount_num

        if self.refund_change_rule is not None:
            result['refund_change_rule'] = self.refund_change_rule.to_map()

        if self.segment_keys is not None:
            result['segment_keys'] = self.segment_keys

        result['segment_position_list'] = []
        if self.segment_position_list is not None:
            for k1 in self.segment_position_list:
                result['segment_position_list'].append(k1.to_map() if k1 else None)

        result['shopping_item_map'] = {}
        if self.shopping_item_map is not None:
            for k1, v1 in self.shopping_item_map.items():
                result['shopping_item_map'][k1] = v1.to_map() if v1 else None

        if self.uniq_key is not None:
            result['uniq_key'] = self.uniq_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baggage_rule') is not None:
            temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleReShopItemListSubItemsBaggageRule()
            self.baggage_rule = temp_model.from_map(m.get('baggage_rule'))

        if m.get('discount_num') is not None:
            self.discount_num = m.get('discount_num')

        if m.get('refund_change_rule') is not None:
            temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleReShopItemListSubItemsRefundChangeRule()
            self.refund_change_rule = temp_model.from_map(m.get('refund_change_rule'))

        if m.get('segment_keys') is not None:
            self.segment_keys = m.get('segment_keys')

        self.segment_position_list = []
        if m.get('segment_position_list') is not None:
            for k1 in m.get('segment_position_list'):
                temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleReShopItemListSubItemsSegmentPositionList()
                self.segment_position_list.append(temp_model.from_map(k1))

        self.shopping_item_map = {}
        if m.get('shopping_item_map') is not None:
            for k1, v1 in m.get('shopping_item_map').items():
                temp_model = main_models.ModuleReShopItemListSubItemsShoppingItemMapValue()
                self.shopping_item_map[k1] = temp_model.from_map(v1)

        if m.get('uniq_key') is not None:
            self.uniq_key = m.get('uniq_key')

        return self

class IntlFlightReShopOtaSearchResponseBodyModuleReShopItemListSubItemsSegmentPositionList(DaraModel):
    def __init__(
        self,
        journey_index: int = None,
        segment_index: int = None,
    ):
        self.journey_index = journey_index
        self.segment_index = segment_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        return self

class IntlFlightReShopOtaSearchResponseBodyModuleReShopItemListSubItemsRefundChangeRule(DaraModel):
    def __init__(
        self,
        cancel_fee_ind: bool = None,
        change_fee_ind: bool = None,
        change_rule_desc: str = None,
        change_rule_show_color: str = None,
        offer_penalty_info_map: Dict[str, List[main_models.ModuleReShopItemListSubItemsRefundChangeRuleOfferPenaltyInfoMapValue]] = None,
        refund_change_digest: str = None,
        refund_change_rule_desc: str = None,
        refund_rule_desc: str = None,
        refund_rule_show_color: str = None,
        structured_refund: bool = None,
    ):
        self.cancel_fee_ind = cancel_fee_ind
        self.change_fee_ind = change_fee_ind
        self.change_rule_desc = change_rule_desc
        self.change_rule_show_color = change_rule_show_color
        self.offer_penalty_info_map = offer_penalty_info_map
        self.refund_change_digest = refund_change_digest
        self.refund_change_rule_desc = refund_change_rule_desc
        self.refund_rule_desc = refund_rule_desc
        self.refund_rule_show_color = refund_rule_show_color
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

        if self.change_rule_show_color is not None:
            result['change_rule_show_color'] = self.change_rule_show_color

        result['offer_penalty_info_map'] = {}
        if self.offer_penalty_info_map is not None:
            for k1, v1 in self.offer_penalty_info_map.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['offer_penalty_info_map'][k1] = l1

        if self.refund_change_digest is not None:
            result['refund_change_digest'] = self.refund_change_digest

        if self.refund_change_rule_desc is not None:
            result['refund_change_rule_desc'] = self.refund_change_rule_desc

        if self.refund_rule_desc is not None:
            result['refund_rule_desc'] = self.refund_rule_desc

        if self.refund_rule_show_color is not None:
            result['refund_rule_show_color'] = self.refund_rule_show_color

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

        if m.get('change_rule_show_color') is not None:
            self.change_rule_show_color = m.get('change_rule_show_color')

        self.offer_penalty_info_map = {}
        if m.get('offer_penalty_info_map') is not None:
            for k1, v1 in m.get('offer_penalty_info_map').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.ModuleReShopItemListSubItemsRefundChangeRuleOfferPenaltyInfoMapValue()
                    l1.append(temp_model.from_map(k2))
                self.offer_penalty_info_map[k1] = l1

        if m.get('refund_change_digest') is not None:
            self.refund_change_digest = m.get('refund_change_digest')

        if m.get('refund_change_rule_desc') is not None:
            self.refund_change_rule_desc = m.get('refund_change_rule_desc')

        if m.get('refund_rule_desc') is not None:
            self.refund_rule_desc = m.get('refund_rule_desc')

        if m.get('refund_rule_show_color') is not None:
            self.refund_rule_show_color = m.get('refund_rule_show_color')

        if m.get('structured_refund') is not None:
            self.structured_refund = m.get('structured_refund')

        return self

class IntlFlightReShopOtaSearchResponseBodyModuleReShopItemListSubItemsBaggageRule(DaraModel):
    def __init__(
        self,
        baggage_desc_show_color: str = None,
        baggage_digest: str = None,
        baggage_rule_desc: str = None,
        offer_baggage_info_map: Dict[str, List[main_models.ModuleReShopItemListSubItemsBaggageRuleOfferBaggageInfoMapValue]] = None,
        structured_baggage: bool = None,
    ):
        self.baggage_desc_show_color = baggage_desc_show_color
        self.baggage_digest = baggage_digest
        self.baggage_rule_desc = baggage_rule_desc
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
        if self.baggage_desc_show_color is not None:
            result['baggage_desc_show_color'] = self.baggage_desc_show_color

        if self.baggage_digest is not None:
            result['baggage_digest'] = self.baggage_digest

        if self.baggage_rule_desc is not None:
            result['baggage_rule_desc'] = self.baggage_rule_desc

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
        if m.get('baggage_desc_show_color') is not None:
            self.baggage_desc_show_color = m.get('baggage_desc_show_color')

        if m.get('baggage_digest') is not None:
            self.baggage_digest = m.get('baggage_digest')

        if m.get('baggage_rule_desc') is not None:
            self.baggage_rule_desc = m.get('baggage_rule_desc')

        self.offer_baggage_info_map = {}
        if m.get('offer_baggage_info_map') is not None:
            for k1, v1 in m.get('offer_baggage_info_map').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.ModuleReShopItemListSubItemsBaggageRuleOfferBaggageInfoMapValue()
                    l1.append(temp_model.from_map(k2))
                self.offer_baggage_info_map[k1] = l1

        if m.get('structured_baggage') is not None:
            self.structured_baggage = m.get('structured_baggage')

        return self

class IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfos(DaraModel):
    def __init__(
        self,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        duration: int = None,
        flight_segment_infos: List[main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfos] = None,
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
                temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfos()
                self.flight_segment_infos.append(temp_model.from_map(k1))

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('transfer_time') is not None:
            self.transfer_time = m.get('transfer_time')

        return self

class IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfos(DaraModel):
    def __init__(
        self,
        airline_info: main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosAirlineInfo = None,
        arr_airport_info: main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosArrAirportInfo = None,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        arr_time_utc: str = None,
        dep_airport_info: main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosDepAirportInfo = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        dep_time_utc: str = None,
        duration: int = None,
        flight_no: str = None,
        flight_share_info: main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightShareInfo = None,
        flight_size: str = None,
        flight_stop_info_list: List[main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightStopInfoList] = None,
        flight_type: str = None,
        journey_index: int = None,
        luggage_direct_info: main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosLuggageDirectInfo = None,
        manufacturer: str = None,
        meal: int = None,
        meal_desc: str = None,
        miles: int = None,
        on_time_rate: str = None,
        one_more: int = None,
        one_more_show: str = None,
        other_info: main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosOtherInfo = None,
        segment_index: int = None,
        segment_key: str = None,
        segment_visa_remark: main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosSegmentVisaRemark = None,
        share: bool = None,
        short_flight_size: str = None,
        stop: bool = None,
        ticketing_airline_info: main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosTicketingAirlineInfo = None,
        total_time: str = None,
    ):
        self.airline_info = airline_info
        self.arr_airport_info = arr_airport_info
        self.arr_city_code = arr_city_code
        self.arr_city_name = arr_city_name
        self.arr_time = arr_time
        self.arr_time_utc = arr_time_utc
        self.dep_airport_info = dep_airport_info
        self.dep_city_code = dep_city_code
        self.dep_city_name = dep_city_name
        self.dep_time = dep_time
        self.dep_time_utc = dep_time_utc
        self.duration = duration
        self.flight_no = flight_no
        self.flight_share_info = flight_share_info
        self.flight_size = flight_size
        self.flight_stop_info_list = flight_stop_info_list
        self.flight_type = flight_type
        self.journey_index = journey_index
        self.luggage_direct_info = luggage_direct_info
        self.manufacturer = manufacturer
        self.meal = meal
        self.meal_desc = meal_desc
        self.miles = miles
        self.on_time_rate = on_time_rate
        self.one_more = one_more
        self.one_more_show = one_more_show
        self.other_info = other_info
        self.segment_index = segment_index
        self.segment_key = segment_key
        self.segment_visa_remark = segment_visa_remark
        self.share = share
        self.short_flight_size = short_flight_size
        self.stop = stop
        self.ticketing_airline_info = ticketing_airline_info
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
        if self.other_info:
            self.other_info.validate()
        if self.segment_visa_remark:
            self.segment_visa_remark.validate()
        if self.ticketing_airline_info:
            self.ticketing_airline_info.validate()

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

        if self.arr_time_utc is not None:
            result['arr_time_u_t_c'] = self.arr_time_utc

        if self.dep_airport_info is not None:
            result['dep_airport_info'] = self.dep_airport_info.to_map()

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.dep_time_utc is not None:
            result['dep_time_u_t_c'] = self.dep_time_utc

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

        if self.meal is not None:
            result['meal'] = self.meal

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

        if self.other_info is not None:
            result['other_info'] = self.other_info.to_map()

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

        if self.ticketing_airline_info is not None:
            result['ticketing_airline_info'] = self.ticketing_airline_info.to_map()

        if self.total_time is not None:
            result['total_time'] = self.total_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_info') is not None:
            temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosAirlineInfo()
            self.airline_info = temp_model.from_map(m.get('airline_info'))

        if m.get('arr_airport_info') is not None:
            temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosArrAirportInfo()
            self.arr_airport_info = temp_model.from_map(m.get('arr_airport_info'))

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('arr_time_u_t_c') is not None:
            self.arr_time_utc = m.get('arr_time_u_t_c')

        if m.get('dep_airport_info') is not None:
            temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosDepAirportInfo()
            self.dep_airport_info = temp_model.from_map(m.get('dep_airport_info'))

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('dep_time_u_t_c') is not None:
            self.dep_time_utc = m.get('dep_time_u_t_c')

        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('flight_share_info') is not None:
            temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightShareInfo()
            self.flight_share_info = temp_model.from_map(m.get('flight_share_info'))

        if m.get('flight_size') is not None:
            self.flight_size = m.get('flight_size')

        self.flight_stop_info_list = []
        if m.get('flight_stop_info_list') is not None:
            for k1 in m.get('flight_stop_info_list'):
                temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightStopInfoList()
                self.flight_stop_info_list.append(temp_model.from_map(k1))

        if m.get('flight_type') is not None:
            self.flight_type = m.get('flight_type')

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('luggage_direct_info') is not None:
            temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosLuggageDirectInfo()
            self.luggage_direct_info = temp_model.from_map(m.get('luggage_direct_info'))

        if m.get('manufacturer') is not None:
            self.manufacturer = m.get('manufacturer')

        if m.get('meal') is not None:
            self.meal = m.get('meal')

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

        if m.get('other_info') is not None:
            temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosOtherInfo()
            self.other_info = temp_model.from_map(m.get('other_info'))

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('segment_key') is not None:
            self.segment_key = m.get('segment_key')

        if m.get('segment_visa_remark') is not None:
            temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosSegmentVisaRemark()
            self.segment_visa_remark = temp_model.from_map(m.get('segment_visa_remark'))

        if m.get('share') is not None:
            self.share = m.get('share')

        if m.get('short_flight_size') is not None:
            self.short_flight_size = m.get('short_flight_size')

        if m.get('stop') is not None:
            self.stop = m.get('stop')

        if m.get('ticketing_airline_info') is not None:
            temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosTicketingAirlineInfo()
            self.ticketing_airline_info = temp_model.from_map(m.get('ticketing_airline_info'))

        if m.get('total_time') is not None:
            self.total_time = m.get('total_time')

        return self

class IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosTicketingAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        cheap_airline: bool = None,
        icon_url: str = None,
        short_name: str = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.cheap_airline = cheap_airline
        self.icon_url = icon_url
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

        if self.cheap_airline is not None:
            result['cheap_airline'] = self.cheap_airline

        if self.icon_url is not None:
            result['icon_url'] = self.icon_url

        if self.short_name is not None:
            result['short_name'] = self.short_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('cheap_airline') is not None:
            self.cheap_airline = m.get('cheap_airline')

        if m.get('icon_url') is not None:
            self.icon_url = m.get('icon_url')

        if m.get('short_name') is not None:
            self.short_name = m.get('short_name')

        return self

class IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosSegmentVisaRemark(DaraModel):
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

class IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosOtherInfo(DaraModel):
    def __init__(
        self,
        aircraft_age: str = None,
        avg_delay_time: str = None,
        flight_cancel_rate: str = None,
        jet_bridge_rate: str = None,
        on_time_rate: str = None,
        wifi: bool = None,
    ):
        self.aircraft_age = aircraft_age
        self.avg_delay_time = avg_delay_time
        self.flight_cancel_rate = flight_cancel_rate
        self.jet_bridge_rate = jet_bridge_rate
        self.on_time_rate = on_time_rate
        self.wifi = wifi

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aircraft_age is not None:
            result['aircraft_age'] = self.aircraft_age

        if self.avg_delay_time is not None:
            result['avg_delay_time'] = self.avg_delay_time

        if self.flight_cancel_rate is not None:
            result['flight_cancel_rate'] = self.flight_cancel_rate

        if self.jet_bridge_rate is not None:
            result['jet_bridge_rate'] = self.jet_bridge_rate

        if self.on_time_rate is not None:
            result['on_time_rate'] = self.on_time_rate

        if self.wifi is not None:
            result['wifi'] = self.wifi

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aircraft_age') is not None:
            self.aircraft_age = m.get('aircraft_age')

        if m.get('avg_delay_time') is not None:
            self.avg_delay_time = m.get('avg_delay_time')

        if m.get('flight_cancel_rate') is not None:
            self.flight_cancel_rate = m.get('flight_cancel_rate')

        if m.get('jet_bridge_rate') is not None:
            self.jet_bridge_rate = m.get('jet_bridge_rate')

        if m.get('on_time_rate') is not None:
            self.on_time_rate = m.get('on_time_rate')

        if m.get('wifi') is not None:
            self.wifi = m.get('wifi')

        return self

class IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosLuggageDirectInfo(DaraModel):
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

class IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightStopInfoList(DaraModel):
    def __init__(
        self,
        stop_airport: str = None,
        stop_airport_county_info: main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightStopInfoListStopAirportCountyInfo = None,
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
        self.stop_airport_county_info = stop_airport_county_info
        self.stop_airport_name = stop_airport_name
        self.stop_arr_term = stop_arr_term
        self.stop_arr_time = stop_arr_time
        self.stop_city_code = stop_city_code
        self.stop_city_name = stop_city_name
        self.stop_dep_term = stop_dep_term
        self.stop_dep_time = stop_dep_time
        self.stop_time = stop_time

    def validate(self):
        if self.stop_airport_county_info:
            self.stop_airport_county_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stop_airport is not None:
            result['stop_airport'] = self.stop_airport

        if self.stop_airport_county_info is not None:
            result['stop_airport_county_info'] = self.stop_airport_county_info.to_map()

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

        if m.get('stop_airport_county_info') is not None:
            temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightStopInfoListStopAirportCountyInfo()
            self.stop_airport_county_info = temp_model.from_map(m.get('stop_airport_county_info'))

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

class IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightStopInfoListStopAirportCountyInfo(DaraModel):
    def __init__(
        self,
        adcode: str = None,
        airport_city_code: str = None,
        airport_city_name: str = None,
        airport_code: str = None,
        airport_name: str = None,
        airport_parent_city_name: str = None,
        county_city_adcode: str = None,
        county_city_name: str = None,
        prefecture_city_adcode: str = None,
        prefecture_city_name: str = None,
    ):
        self.adcode = adcode
        self.airport_city_code = airport_city_code
        self.airport_city_name = airport_city_name
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.airport_parent_city_name = airport_parent_city_name
        self.county_city_adcode = county_city_adcode
        self.county_city_name = county_city_name
        self.prefecture_city_adcode = prefecture_city_adcode
        self.prefecture_city_name = prefecture_city_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adcode is not None:
            result['adcode'] = self.adcode

        if self.airport_city_code is not None:
            result['airport_city_code'] = self.airport_city_code

        if self.airport_city_name is not None:
            result['airport_city_name'] = self.airport_city_name

        if self.airport_code is not None:
            result['airport_code'] = self.airport_code

        if self.airport_name is not None:
            result['airport_name'] = self.airport_name

        if self.airport_parent_city_name is not None:
            result['airport_parent_city_name'] = self.airport_parent_city_name

        if self.county_city_adcode is not None:
            result['county_city_adcode'] = self.county_city_adcode

        if self.county_city_name is not None:
            result['county_city_name'] = self.county_city_name

        if self.prefecture_city_adcode is not None:
            result['prefecture_city_adcode'] = self.prefecture_city_adcode

        if self.prefecture_city_name is not None:
            result['prefecture_city_name'] = self.prefecture_city_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adcode') is not None:
            self.adcode = m.get('adcode')

        if m.get('airport_city_code') is not None:
            self.airport_city_code = m.get('airport_city_code')

        if m.get('airport_city_name') is not None:
            self.airport_city_name = m.get('airport_city_name')

        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('airport_parent_city_name') is not None:
            self.airport_parent_city_name = m.get('airport_parent_city_name')

        if m.get('county_city_adcode') is not None:
            self.county_city_adcode = m.get('county_city_adcode')

        if m.get('county_city_name') is not None:
            self.county_city_name = m.get('county_city_name')

        if m.get('prefecture_city_adcode') is not None:
            self.prefecture_city_adcode = m.get('prefecture_city_adcode')

        if m.get('prefecture_city_name') is not None:
            self.prefecture_city_name = m.get('prefecture_city_name')

        return self

class IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightShareInfo(DaraModel):
    def __init__(
        self,
        operating_airline_info: main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightShareInfoOperatingAirlineInfo = None,
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
            temp_model = main_models.IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightShareInfoOperatingAirlineInfo()
            self.operating_airline_info = temp_model.from_map(m.get('operating_airline_info'))

        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')

        return self

class IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightShareInfoOperatingAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        cheap_airline: bool = None,
        icon_url: str = None,
        short_name: str = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.cheap_airline = cheap_airline
        self.icon_url = icon_url
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

        if self.cheap_airline is not None:
            result['cheap_airline'] = self.cheap_airline

        if self.icon_url is not None:
            result['icon_url'] = self.icon_url

        if self.short_name is not None:
            result['short_name'] = self.short_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('cheap_airline') is not None:
            self.cheap_airline = m.get('cheap_airline')

        if m.get('icon_url') is not None:
            self.icon_url = m.get('icon_url')

        if m.get('short_name') is not None:
            self.short_name = m.get('short_name')

        return self

class IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosDepAirportInfo(DaraModel):
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

class IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosArrAirportInfo(DaraModel):
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

class IntlFlightReShopOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        cheap_airline: bool = None,
        icon_url: str = None,
        short_name: str = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.cheap_airline = cheap_airline
        self.icon_url = icon_url
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

        if self.cheap_airline is not None:
            result['cheap_airline'] = self.cheap_airline

        if self.icon_url is not None:
            result['icon_url'] = self.icon_url

        if self.short_name is not None:
            result['short_name'] = self.short_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('cheap_airline') is not None:
            self.cheap_airline = m.get('cheap_airline')

        if m.get('icon_url') is not None:
            self.icon_url = m.get('icon_url')

        if m.get('short_name') is not None:
            self.short_name = m.get('short_name')

        return self

