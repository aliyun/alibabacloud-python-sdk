# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IntlFlightOtaSearchResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.IntlFlightOtaSearchResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        # module。
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
            temp_model = main_models.IntlFlightOtaSearchResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class IntlFlightOtaSearchResponseBodyModule(DaraModel):
    def __init__(
        self,
        flight_journey_infos: List[main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfos] = None,
        item_list: List[main_models.IntlFlightOtaSearchResponseBodyModuleItemList] = None,
    ):
        self.flight_journey_infos = flight_journey_infos
        self.item_list = item_list

    def validate(self):
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
        self.flight_journey_infos = []
        if m.get('flight_journey_infos') is not None:
            for k1 in m.get('flight_journey_infos'):
                temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfos()
                self.flight_journey_infos.append(temp_model.from_map(k1))

        self.item_list = []
        if m.get('item_list') is not None:
            for k1 in m.get('item_list'):
                temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleItemList()
                self.item_list.append(temp_model.from_map(k1))

        return self

class IntlFlightOtaSearchResponseBodyModuleItemList(DaraModel):
    def __init__(
        self,
        agreement_price_codes: List[main_models.IntlFlightOtaSearchResponseBodyModuleItemListAgreementPriceCodes] = None,
        item_id: str = None,
        item_type: str = None,
        label_list: List[main_models.IntlFlightOtaSearchResponseBodyModuleItemListLabelList] = None,
        shopping_item_map: Dict[str, main_models.ModuleItemListShoppingItemMapValue] = None,
        sub_items: List[main_models.IntlFlightOtaSearchResponseBodyModuleItemListSubItems] = None,
    ):
        self.agreement_price_codes = agreement_price_codes
        self.item_id = item_id
        self.item_type = item_type
        self.label_list = label_list
        self.shopping_item_map = shopping_item_map
        self.sub_items = sub_items

    def validate(self):
        if self.agreement_price_codes:
            for v1 in self.agreement_price_codes:
                 if v1:
                    v1.validate()
        if self.label_list:
            for v1 in self.label_list:
                 if v1:
                    v1.validate()
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
        result['agreement_price_codes'] = []
        if self.agreement_price_codes is not None:
            for k1 in self.agreement_price_codes:
                result['agreement_price_codes'].append(k1.to_map() if k1 else None)

        if self.item_id is not None:
            result['item_id'] = self.item_id

        if self.item_type is not None:
            result['item_type'] = self.item_type

        result['label_list'] = []
        if self.label_list is not None:
            for k1 in self.label_list:
                result['label_list'].append(k1.to_map() if k1 else None)

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
        self.agreement_price_codes = []
        if m.get('agreement_price_codes') is not None:
            for k1 in m.get('agreement_price_codes'):
                temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleItemListAgreementPriceCodes()
                self.agreement_price_codes.append(temp_model.from_map(k1))

        if m.get('item_id') is not None:
            self.item_id = m.get('item_id')

        if m.get('item_type') is not None:
            self.item_type = m.get('item_type')

        self.label_list = []
        if m.get('label_list') is not None:
            for k1 in m.get('label_list'):
                temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleItemListLabelList()
                self.label_list.append(temp_model.from_map(k1))

        self.shopping_item_map = {}
        if m.get('shopping_item_map') is not None:
            for k1, v1 in m.get('shopping_item_map').items():
                temp_model = main_models.ModuleItemListShoppingItemMapValue()
                self.shopping_item_map[k1] = temp_model.from_map(v1)

        self.sub_items = []
        if m.get('sub_items') is not None:
            for k1 in m.get('sub_items'):
                temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleItemListSubItems()
                self.sub_items.append(temp_model.from_map(k1))

        return self

class IntlFlightOtaSearchResponseBodyModuleItemListSubItems(DaraModel):
    def __init__(
        self,
        baggage_rule: main_models.IntlFlightOtaSearchResponseBodyModuleItemListSubItemsBaggageRule = None,
        refund_change_rule: main_models.IntlFlightOtaSearchResponseBodyModuleItemListSubItemsRefundChangeRule = None,
        segment_keys: List[str] = None,
        segment_position_list: List[main_models.IntlFlightOtaSearchResponseBodyModuleItemListSubItemsSegmentPositionList] = None,
        shopping_item_map: Dict[str, main_models.ModuleItemListSubItemsShoppingItemMapValue] = None,
        uniq_key: str = None,
    ):
        self.baggage_rule = baggage_rule
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
            temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleItemListSubItemsBaggageRule()
            self.baggage_rule = temp_model.from_map(m.get('baggage_rule'))

        if m.get('refund_change_rule') is not None:
            temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleItemListSubItemsRefundChangeRule()
            self.refund_change_rule = temp_model.from_map(m.get('refund_change_rule'))

        if m.get('segment_keys') is not None:
            self.segment_keys = m.get('segment_keys')

        self.segment_position_list = []
        if m.get('segment_position_list') is not None:
            for k1 in m.get('segment_position_list'):
                temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleItemListSubItemsSegmentPositionList()
                self.segment_position_list.append(temp_model.from_map(k1))

        self.shopping_item_map = {}
        if m.get('shopping_item_map') is not None:
            for k1, v1 in m.get('shopping_item_map').items():
                temp_model = main_models.ModuleItemListSubItemsShoppingItemMapValue()
                self.shopping_item_map[k1] = temp_model.from_map(v1)

        if m.get('uniq_key') is not None:
            self.uniq_key = m.get('uniq_key')

        return self

class IntlFlightOtaSearchResponseBodyModuleItemListSubItemsSegmentPositionList(DaraModel):
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

class IntlFlightOtaSearchResponseBodyModuleItemListSubItemsRefundChangeRule(DaraModel):
    def __init__(
        self,
        cancel_fee_ind: bool = None,
        change_fee_ind: bool = None,
        change_rule_desc: str = None,
        offer_penalty_info_map: Dict[str, List[main_models.ModuleItemListSubItemsRefundChangeRuleOfferPenaltyInfoMapValue]] = None,
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
                    temp_model = main_models.ModuleItemListSubItemsRefundChangeRuleOfferPenaltyInfoMapValue()
                    l1.append(temp_model.from_map(k2))
                self.offer_penalty_info_map[k1] = l1

        if m.get('refund_change_digest') is not None:
            self.refund_change_digest = m.get('refund_change_digest')

        if m.get('refund_rule_desc') is not None:
            self.refund_rule_desc = m.get('refund_rule_desc')

        if m.get('structured_refund') is not None:
            self.structured_refund = m.get('structured_refund')

        return self

class IntlFlightOtaSearchResponseBodyModuleItemListSubItemsBaggageRule(DaraModel):
    def __init__(
        self,
        baggage_digest: str = None,
        offer_baggage_info_map: Dict[str, List[main_models.ModuleItemListSubItemsBaggageRuleOfferBaggageInfoMapValue]] = None,
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
                    temp_model = main_models.ModuleItemListSubItemsBaggageRuleOfferBaggageInfoMapValue()
                    l1.append(temp_model.from_map(k2))
                self.offer_baggage_info_map[k1] = l1

        if m.get('structured_baggage') is not None:
            self.structured_baggage = m.get('structured_baggage')

        return self

class IntlFlightOtaSearchResponseBodyModuleItemListLabelList(DaraModel):
    def __init__(
        self,
        label_code: int = None,
        label_name: str = None,
    ):
        self.label_code = label_code
        self.label_name = label_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_code is not None:
            result['labelCode'] = self.label_code

        if self.label_name is not None:
            result['labelName'] = self.label_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelCode') is not None:
            self.label_code = m.get('labelCode')

        if m.get('labelName') is not None:
            self.label_name = m.get('labelName')

        return self

class IntlFlightOtaSearchResponseBodyModuleItemListAgreementPriceCodes(DaraModel):
    def __init__(
        self,
        code: str = None,
        type: int = None,
    ):
        self.code = code
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfos(DaraModel):
    def __init__(
        self,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        duration: int = None,
        flight_segment_infos: List[main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfos] = None,
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
                temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfos()
                self.flight_segment_infos.append(temp_model.from_map(k1))

        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('transfer_time') is not None:
            self.transfer_time = m.get('transfer_time')

        return self

class IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfos(DaraModel):
    def __init__(
        self,
        airline_info: main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosAirlineInfo = None,
        arr_airport_info: main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosArrAirportInfo = None,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        dep_airport_info: main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosDepAirportInfo = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        duration: int = None,
        flight_no: str = None,
        flight_share_info: main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightShareInfo = None,
        flight_size: str = None,
        flight_stop_info_list: List[main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightStopInfoList] = None,
        flight_type: str = None,
        luggage_direct_info: main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosLuggageDirectInfo = None,
        manufacturer: str = None,
        meal_desc: str = None,
        one_more: int = None,
        one_more_show: str = None,
        segment_index: int = None,
        segment_key: str = None,
        segment_visa_remark: main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosSegmentVisaRemark = None,
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
            temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosAirlineInfo()
            self.airline_info = temp_model.from_map(m.get('airline_info'))

        if m.get('arr_airport_info') is not None:
            temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosArrAirportInfo()
            self.arr_airport_info = temp_model.from_map(m.get('arr_airport_info'))

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('dep_airport_info') is not None:
            temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosDepAirportInfo()
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
            temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightShareInfo()
            self.flight_share_info = temp_model.from_map(m.get('flight_share_info'))

        if m.get('flight_size') is not None:
            self.flight_size = m.get('flight_size')

        self.flight_stop_info_list = []
        if m.get('flight_stop_info_list') is not None:
            for k1 in m.get('flight_stop_info_list'):
                temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightStopInfoList()
                self.flight_stop_info_list.append(temp_model.from_map(k1))

        if m.get('flight_type') is not None:
            self.flight_type = m.get('flight_type')

        if m.get('luggage_direct_info') is not None:
            temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosLuggageDirectInfo()
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
            temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosSegmentVisaRemark()
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

class IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosSegmentVisaRemark(DaraModel):
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

class IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosLuggageDirectInfo(DaraModel):
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

class IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightStopInfoList(DaraModel):
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

class IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightShareInfo(DaraModel):
    def __init__(
        self,
        operating_airline_info: main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightShareInfoOperatingAirlineInfo = None,
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
            temp_model = main_models.IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightShareInfoOperatingAirlineInfo()
            self.operating_airline_info = temp_model.from_map(m.get('operating_airline_info'))

        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')

        return self

class IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosFlightShareInfoOperatingAirlineInfo(DaraModel):
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

class IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosDepAirportInfo(DaraModel):
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

class IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosArrAirportInfo(DaraModel):
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

class IntlFlightOtaSearchResponseBodyModuleFlightJourneyInfosFlightSegmentInfosAirlineInfo(DaraModel):
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

