# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightOtaItemDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.FlightOtaItemDetailResponseBodyModule = None,
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
            temp_model = main_models.FlightOtaItemDetailResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightOtaItemDetailResponseBodyModule(DaraModel):
    def __init__(
        self,
        baggage_rule: List[main_models.FlightOtaItemDetailResponseBodyModuleBaggageRule] = None,
        change_rule: List[main_models.FlightOtaItemDetailResponseBodyModuleChangeRule] = None,
        refund_rule: List[main_models.FlightOtaItemDetailResponseBodyModuleRefundRule] = None,
        sell_price: int = None,
        sell_price_list: List[int] = None,
        trip_type: int = None,
    ):
        self.baggage_rule = baggage_rule
        self.change_rule = change_rule
        self.refund_rule = refund_rule
        self.sell_price = sell_price
        self.sell_price_list = sell_price_list
        self.trip_type = trip_type

    def validate(self):
        if self.baggage_rule:
            for v1 in self.baggage_rule:
                 if v1:
                    v1.validate()
        if self.change_rule:
            for v1 in self.change_rule:
                 if v1:
                    v1.validate()
        if self.refund_rule:
            for v1 in self.refund_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['baggage_rule'] = []
        if self.baggage_rule is not None:
            for k1 in self.baggage_rule:
                result['baggage_rule'].append(k1.to_map() if k1 else None)

        result['change_rule'] = []
        if self.change_rule is not None:
            for k1 in self.change_rule:
                result['change_rule'].append(k1.to_map() if k1 else None)

        result['refund_rule'] = []
        if self.refund_rule is not None:
            for k1 in self.refund_rule:
                result['refund_rule'].append(k1.to_map() if k1 else None)

        if self.sell_price is not None:
            result['sell_price'] = self.sell_price

        if self.sell_price_list is not None:
            result['sell_price_list'] = self.sell_price_list

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baggage_rule = []
        if m.get('baggage_rule') is not None:
            for k1 in m.get('baggage_rule'):
                temp_model = main_models.FlightOtaItemDetailResponseBodyModuleBaggageRule()
                self.baggage_rule.append(temp_model.from_map(k1))

        self.change_rule = []
        if m.get('change_rule') is not None:
            for k1 in m.get('change_rule'):
                temp_model = main_models.FlightOtaItemDetailResponseBodyModuleChangeRule()
                self.change_rule.append(temp_model.from_map(k1))

        self.refund_rule = []
        if m.get('refund_rule') is not None:
            for k1 in m.get('refund_rule'):
                temp_model = main_models.FlightOtaItemDetailResponseBodyModuleRefundRule()
                self.refund_rule.append(temp_model.from_map(k1))

        if m.get('sell_price') is not None:
            self.sell_price = m.get('sell_price')

        if m.get('sell_price_list') is not None:
            self.sell_price_list = m.get('sell_price_list')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        return self

class FlightOtaItemDetailResponseBodyModuleRefundRule(DaraModel):
    def __init__(
        self,
        extra_contents: List[main_models.FlightOtaItemDetailResponseBodyModuleRefundRuleExtraContents] = None,
        flight_no: str = None,
        free_baggage: int = None,
        index: int = None,
        level: int = None,
        refund_sub_items: List[main_models.FlightOtaItemDetailResponseBodyModuleRefundRuleRefundSubItems] = None,
        sub_table_head: List[str] = None,
        table_head: str = None,
        title: str = None,
        type: int = None,
    ):
        self.extra_contents = extra_contents
        self.flight_no = flight_no
        self.free_baggage = free_baggage
        self.index = index
        self.level = level
        self.refund_sub_items = refund_sub_items
        # subTableHead
        self.sub_table_head = sub_table_head
        self.table_head = table_head
        self.title = title
        self.type = type

    def validate(self):
        if self.extra_contents:
            for v1 in self.extra_contents:
                 if v1:
                    v1.validate()
        if self.refund_sub_items:
            for v1 in self.refund_sub_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['extra_contents'] = []
        if self.extra_contents is not None:
            for k1 in self.extra_contents:
                result['extra_contents'].append(k1.to_map() if k1 else None)

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.free_baggage is not None:
            result['free_baggage'] = self.free_baggage

        if self.index is not None:
            result['index'] = self.index

        if self.level is not None:
            result['level'] = self.level

        result['refund_sub_items'] = []
        if self.refund_sub_items is not None:
            for k1 in self.refund_sub_items:
                result['refund_sub_items'].append(k1.to_map() if k1 else None)

        if self.sub_table_head is not None:
            result['sub_table_head'] = self.sub_table_head

        if self.table_head is not None:
            result['table_head'] = self.table_head

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extra_contents = []
        if m.get('extra_contents') is not None:
            for k1 in m.get('extra_contents'):
                temp_model = main_models.FlightOtaItemDetailResponseBodyModuleRefundRuleExtraContents()
                self.extra_contents.append(temp_model.from_map(k1))

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('free_baggage') is not None:
            self.free_baggage = m.get('free_baggage')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('level') is not None:
            self.level = m.get('level')

        self.refund_sub_items = []
        if m.get('refund_sub_items') is not None:
            for k1 in m.get('refund_sub_items'):
                temp_model = main_models.FlightOtaItemDetailResponseBodyModuleRefundRuleRefundSubItems()
                self.refund_sub_items.append(temp_model.from_map(k1))

        if m.get('sub_table_head') is not None:
            self.sub_table_head = m.get('sub_table_head')

        if m.get('table_head') is not None:
            self.table_head = m.get('table_head')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightOtaItemDetailResponseBodyModuleRefundRuleRefundSubItems(DaraModel):
    def __init__(
        self,
        is_struct: bool = None,
        ptc: str = None,
        refund_sub_contents: List[main_models.FlightOtaItemDetailResponseBodyModuleRefundRuleRefundSubItemsRefundSubContents] = None,
        title: str = None,
    ):
        self.is_struct = is_struct
        self.ptc = ptc
        self.refund_sub_contents = refund_sub_contents
        self.title = title

    def validate(self):
        if self.refund_sub_contents:
            for v1 in self.refund_sub_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_struct is not None:
            result['is_struct'] = self.is_struct

        if self.ptc is not None:
            result['ptc'] = self.ptc

        result['refund_sub_contents'] = []
        if self.refund_sub_contents is not None:
            for k1 in self.refund_sub_contents:
                result['refund_sub_contents'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('is_struct') is not None:
            self.is_struct = m.get('is_struct')

        if m.get('ptc') is not None:
            self.ptc = m.get('ptc')

        self.refund_sub_contents = []
        if m.get('refund_sub_contents') is not None:
            for k1 in m.get('refund_sub_contents'):
                temp_model = main_models.FlightOtaItemDetailResponseBodyModuleRefundRuleRefundSubItemsRefundSubContents()
                self.refund_sub_contents.append(temp_model.from_map(k1))

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaItemDetailResponseBodyModuleRefundRuleRefundSubItemsRefundSubContents(DaraModel):
    def __init__(
        self,
        fee_desc: str = None,
        fee_range: str = None,
        style: int = None,
    ):
        self.fee_desc = fee_desc
        self.fee_range = fee_range
        self.style = style

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fee_desc is not None:
            result['fee_desc'] = self.fee_desc

        if self.fee_range is not None:
            result['fee_range'] = self.fee_range

        if self.style is not None:
            result['style'] = self.style

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fee_desc') is not None:
            self.fee_desc = m.get('fee_desc')

        if m.get('fee_range') is not None:
            self.fee_range = m.get('fee_range')

        if m.get('style') is not None:
            self.style = m.get('style')

        return self

class FlightOtaItemDetailResponseBodyModuleRefundRuleExtraContents(DaraModel):
    def __init__(
        self,
        content: str = None,
        title: str = None,
    ):
        self.content = content
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaItemDetailResponseBodyModuleChangeRule(DaraModel):
    def __init__(
        self,
        extra_contents: List[main_models.FlightOtaItemDetailResponseBodyModuleChangeRuleExtraContents] = None,
        flight_no: str = None,
        free_baggage: int = None,
        index: int = None,
        level: int = None,
        refund_sub_items: List[main_models.FlightOtaItemDetailResponseBodyModuleChangeRuleRefundSubItems] = None,
        sub_table_head: List[str] = None,
        table_head: str = None,
        title: str = None,
        type: int = None,
    ):
        self.extra_contents = extra_contents
        self.flight_no = flight_no
        self.free_baggage = free_baggage
        self.index = index
        self.level = level
        self.refund_sub_items = refund_sub_items
        # subTableHead
        self.sub_table_head = sub_table_head
        self.table_head = table_head
        self.title = title
        self.type = type

    def validate(self):
        if self.extra_contents:
            for v1 in self.extra_contents:
                 if v1:
                    v1.validate()
        if self.refund_sub_items:
            for v1 in self.refund_sub_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['extra_contents'] = []
        if self.extra_contents is not None:
            for k1 in self.extra_contents:
                result['extra_contents'].append(k1.to_map() if k1 else None)

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.free_baggage is not None:
            result['free_baggage'] = self.free_baggage

        if self.index is not None:
            result['index'] = self.index

        if self.level is not None:
            result['level'] = self.level

        result['refund_sub_items'] = []
        if self.refund_sub_items is not None:
            for k1 in self.refund_sub_items:
                result['refund_sub_items'].append(k1.to_map() if k1 else None)

        if self.sub_table_head is not None:
            result['sub_table_head'] = self.sub_table_head

        if self.table_head is not None:
            result['table_head'] = self.table_head

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extra_contents = []
        if m.get('extra_contents') is not None:
            for k1 in m.get('extra_contents'):
                temp_model = main_models.FlightOtaItemDetailResponseBodyModuleChangeRuleExtraContents()
                self.extra_contents.append(temp_model.from_map(k1))

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('free_baggage') is not None:
            self.free_baggage = m.get('free_baggage')

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('level') is not None:
            self.level = m.get('level')

        self.refund_sub_items = []
        if m.get('refund_sub_items') is not None:
            for k1 in m.get('refund_sub_items'):
                temp_model = main_models.FlightOtaItemDetailResponseBodyModuleChangeRuleRefundSubItems()
                self.refund_sub_items.append(temp_model.from_map(k1))

        if m.get('sub_table_head') is not None:
            self.sub_table_head = m.get('sub_table_head')

        if m.get('table_head') is not None:
            self.table_head = m.get('table_head')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightOtaItemDetailResponseBodyModuleChangeRuleRefundSubItems(DaraModel):
    def __init__(
        self,
        is_struct: bool = None,
        ptc: str = None,
        refund_sub_contents: List[main_models.FlightOtaItemDetailResponseBodyModuleChangeRuleRefundSubItemsRefundSubContents] = None,
        title: str = None,
    ):
        self.is_struct = is_struct
        self.ptc = ptc
        self.refund_sub_contents = refund_sub_contents
        self.title = title

    def validate(self):
        if self.refund_sub_contents:
            for v1 in self.refund_sub_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_struct is not None:
            result['is_struct'] = self.is_struct

        if self.ptc is not None:
            result['ptc'] = self.ptc

        result['refund_sub_contents'] = []
        if self.refund_sub_contents is not None:
            for k1 in self.refund_sub_contents:
                result['refund_sub_contents'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('is_struct') is not None:
            self.is_struct = m.get('is_struct')

        if m.get('ptc') is not None:
            self.ptc = m.get('ptc')

        self.refund_sub_contents = []
        if m.get('refund_sub_contents') is not None:
            for k1 in m.get('refund_sub_contents'):
                temp_model = main_models.FlightOtaItemDetailResponseBodyModuleChangeRuleRefundSubItemsRefundSubContents()
                self.refund_sub_contents.append(temp_model.from_map(k1))

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaItemDetailResponseBodyModuleChangeRuleRefundSubItemsRefundSubContents(DaraModel):
    def __init__(
        self,
        fee_desc: str = None,
        fee_range: str = None,
        style: int = None,
    ):
        self.fee_desc = fee_desc
        self.fee_range = fee_range
        self.style = style

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fee_desc is not None:
            result['fee_desc'] = self.fee_desc

        if self.fee_range is not None:
            result['fee_range'] = self.fee_range

        if self.style is not None:
            result['style'] = self.style

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fee_desc') is not None:
            self.fee_desc = m.get('fee_desc')

        if m.get('fee_range') is not None:
            self.fee_range = m.get('fee_range')

        if m.get('style') is not None:
            self.style = m.get('style')

        return self

class FlightOtaItemDetailResponseBodyModuleChangeRuleExtraContents(DaraModel):
    def __init__(
        self,
        content: str = None,
        title: str = None,
    ):
        self.content = content
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaItemDetailResponseBodyModuleBaggageRule(DaraModel):
    def __init__(
        self,
        baggage_sub_items: List[main_models.FlightOtaItemDetailResponseBodyModuleBaggageRuleBaggageSubItems] = None,
        index: int = None,
        table_head: str = None,
        tips: main_models.FlightOtaItemDetailResponseBodyModuleBaggageRuleTips = None,
        title: str = None,
        type: int = None,
    ):
        self.baggage_sub_items = baggage_sub_items
        self.index = index
        self.table_head = table_head
        self.tips = tips
        self.title = title
        self.type = type

    def validate(self):
        if self.baggage_sub_items:
            for v1 in self.baggage_sub_items:
                 if v1:
                    v1.validate()
        if self.tips:
            self.tips.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['baggage_sub_items'] = []
        if self.baggage_sub_items is not None:
            for k1 in self.baggage_sub_items:
                result['baggage_sub_items'].append(k1.to_map() if k1 else None)

        if self.index is not None:
            result['index'] = self.index

        if self.table_head is not None:
            result['table_head'] = self.table_head

        if self.tips is not None:
            result['tips'] = self.tips.to_map()

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baggage_sub_items = []
        if m.get('baggage_sub_items') is not None:
            for k1 in m.get('baggage_sub_items'):
                temp_model = main_models.FlightOtaItemDetailResponseBodyModuleBaggageRuleBaggageSubItems()
                self.baggage_sub_items.append(temp_model.from_map(k1))

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('table_head') is not None:
            self.table_head = m.get('table_head')

        if m.get('tips') is not None:
            temp_model = main_models.FlightOtaItemDetailResponseBodyModuleBaggageRuleTips()
            self.tips = temp_model.from_map(m.get('tips'))

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightOtaItemDetailResponseBodyModuleBaggageRuleTips(DaraModel):
    def __init__(
        self,
        logo: str = None,
        tips_desc: str = None,
        tips_image: str = None,
    ):
        self.logo = logo
        self.tips_desc = tips_desc
        self.tips_image = tips_image

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logo is not None:
            result['logo'] = self.logo

        if self.tips_desc is not None:
            result['tips_desc'] = self.tips_desc

        if self.tips_image is not None:
            result['tips_image'] = self.tips_image

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logo') is not None:
            self.logo = m.get('logo')

        if m.get('tips_desc') is not None:
            self.tips_desc = m.get('tips_desc')

        if m.get('tips_image') is not None:
            self.tips_image = m.get('tips_image')

        return self

class FlightOtaItemDetailResponseBodyModuleBaggageRuleBaggageSubItems(DaraModel):
    def __init__(
        self,
        baggage_sub_content_visualizes: List[main_models.FlightOtaItemDetailResponseBodyModuleBaggageRuleBaggageSubItemsBaggageSubContentVisualizes] = None,
        extra_content_visualizes: List[Any] = None,
        is_struct: bool = None,
        ptc: str = None,
        title: str = None,
    ):
        self.baggage_sub_content_visualizes = baggage_sub_content_visualizes
        self.extra_content_visualizes = extra_content_visualizes
        self.is_struct = is_struct
        self.ptc = ptc
        self.title = title

    def validate(self):
        if self.baggage_sub_content_visualizes:
            for v1 in self.baggage_sub_content_visualizes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['baggage_sub_content_visualizes'] = []
        if self.baggage_sub_content_visualizes is not None:
            for k1 in self.baggage_sub_content_visualizes:
                result['baggage_sub_content_visualizes'].append(k1.to_map() if k1 else None)

        if self.extra_content_visualizes is not None:
            result['extra_content_visualizes'] = self.extra_content_visualizes

        if self.is_struct is not None:
            result['is_struct'] = self.is_struct

        if self.ptc is not None:
            result['ptc'] = self.ptc

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baggage_sub_content_visualizes = []
        if m.get('baggage_sub_content_visualizes') is not None:
            for k1 in m.get('baggage_sub_content_visualizes'):
                temp_model = main_models.FlightOtaItemDetailResponseBodyModuleBaggageRuleBaggageSubItemsBaggageSubContentVisualizes()
                self.baggage_sub_content_visualizes.append(temp_model.from_map(k1))

        if m.get('extra_content_visualizes') is not None:
            self.extra_content_visualizes = m.get('extra_content_visualizes')

        if m.get('is_struct') is not None:
            self.is_struct = m.get('is_struct')

        if m.get('ptc') is not None:
            self.ptc = m.get('ptc')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class FlightOtaItemDetailResponseBodyModuleBaggageRuleBaggageSubItemsBaggageSubContentVisualizes(DaraModel):
    def __init__(
        self,
        baggage_desc: List[str] = None,
        baggage_sub_content_type: int = None,
        description: main_models.FlightOtaItemDetailResponseBodyModuleBaggageRuleBaggageSubItemsBaggageSubContentVisualizesDescription = None,
        image_do: main_models.FlightOtaItemDetailResponseBodyModuleBaggageRuleBaggageSubItemsBaggageSubContentVisualizesImageDO = None,
        is_highlight: bool = None,
        sub_title: str = None,
    ):
        # baggage_desc
        self.baggage_desc = baggage_desc
        self.baggage_sub_content_type = baggage_sub_content_type
        self.description = description
        self.image_do = image_do
        self.is_highlight = is_highlight
        self.sub_title = sub_title

    def validate(self):
        if self.description:
            self.description.validate()
        if self.image_do:
            self.image_do.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baggage_desc is not None:
            result['baggage_desc'] = self.baggage_desc

        if self.baggage_sub_content_type is not None:
            result['baggage_sub_content_type'] = self.baggage_sub_content_type

        if self.description is not None:
            result['description'] = self.description.to_map()

        if self.image_do is not None:
            result['image_d_o'] = self.image_do.to_map()

        if self.is_highlight is not None:
            result['is_highlight'] = self.is_highlight

        if self.sub_title is not None:
            result['sub_title'] = self.sub_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baggage_desc') is not None:
            self.baggage_desc = m.get('baggage_desc')

        if m.get('baggage_sub_content_type') is not None:
            self.baggage_sub_content_type = m.get('baggage_sub_content_type')

        if m.get('description') is not None:
            temp_model = main_models.FlightOtaItemDetailResponseBodyModuleBaggageRuleBaggageSubItemsBaggageSubContentVisualizesDescription()
            self.description = temp_model.from_map(m.get('description'))

        if m.get('image_d_o') is not None:
            temp_model = main_models.FlightOtaItemDetailResponseBodyModuleBaggageRuleBaggageSubItemsBaggageSubContentVisualizesImageDO()
            self.image_do = temp_model.from_map(m.get('image_d_o'))

        if m.get('is_highlight') is not None:
            self.is_highlight = m.get('is_highlight')

        if m.get('sub_title') is not None:
            self.sub_title = m.get('sub_title')

        return self

class FlightOtaItemDetailResponseBodyModuleBaggageRuleBaggageSubItemsBaggageSubContentVisualizesImageDO(DaraModel):
    def __init__(
        self,
        image: str = None,
        largest: str = None,
        middle: str = None,
        smallest: str = None,
    ):
        self.image = image
        self.largest = largest
        self.middle = middle
        self.smallest = smallest

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['image'] = self.image

        if self.largest is not None:
            result['largest'] = self.largest

        if self.middle is not None:
            result['middle'] = self.middle

        if self.smallest is not None:
            result['smallest'] = self.smallest

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('largest') is not None:
            self.largest = m.get('largest')

        if m.get('middle') is not None:
            self.middle = m.get('middle')

        if m.get('smallest') is not None:
            self.smallest = m.get('smallest')

        return self

class FlightOtaItemDetailResponseBodyModuleBaggageRuleBaggageSubItemsBaggageSubContentVisualizesDescription(DaraModel):
    def __init__(
        self,
        desc: str = None,
        icon: str = None,
        image: str = None,
        title: str = None,
    ):
        self.desc = desc
        self.icon = icon
        self.image = image
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.icon is not None:
            result['icon'] = self.icon

        if self.image is not None:
            result['image'] = self.image

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('icon') is not None:
            self.icon = m.get('icon')

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

