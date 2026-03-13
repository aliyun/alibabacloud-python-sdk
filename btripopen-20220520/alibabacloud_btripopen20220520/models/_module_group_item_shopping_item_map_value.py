# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class ModuleGroupItemShoppingItemMapValue(DaraModel):
    def __init__(
        self,
        cabin_quantity_list: List[main_models.ModuleGroupItemShoppingItemMapValueCabinQuantityList] = None,
        search_price: main_models.ModuleGroupItemShoppingItemMapValueSearchPrice = None,
        segment_price_list: List[main_models.ModuleGroupItemShoppingItemMapValueSegmentPriceList] = None,
    ):
        self.cabin_quantity_list = cabin_quantity_list
        self.search_price = search_price
        self.segment_price_list = segment_price_list

    def validate(self):
        if self.cabin_quantity_list:
            for v1 in self.cabin_quantity_list:
                 if v1:
                    v1.validate()
        if self.search_price:
            self.search_price.validate()
        if self.segment_price_list:
            for v1 in self.segment_price_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['cabin_quantity_list'] = []
        if self.cabin_quantity_list is not None:
            for k1 in self.cabin_quantity_list:
                result['cabin_quantity_list'].append(k1.to_map() if k1 else None)

        if self.search_price is not None:
            result['search_price'] = self.search_price.to_map()

        result['segment_price_list'] = []
        if self.segment_price_list is not None:
            for k1 in self.segment_price_list:
                result['segment_price_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cabin_quantity_list = []
        if m.get('cabin_quantity_list') is not None:
            for k1 in m.get('cabin_quantity_list'):
                temp_model = main_models.ModuleGroupItemShoppingItemMapValueCabinQuantityList()
                self.cabin_quantity_list.append(temp_model.from_map(k1))

        if m.get('search_price') is not None:
            temp_model = main_models.ModuleGroupItemShoppingItemMapValueSearchPrice()
            self.search_price = temp_model.from_map(m.get('search_price'))

        self.segment_price_list = []
        if m.get('segment_price_list') is not None:
            for k1 in m.get('segment_price_list'):
                temp_model = main_models.ModuleGroupItemShoppingItemMapValueSegmentPriceList()
                self.segment_price_list.append(temp_model.from_map(k1))

        return self

class ModuleGroupItemShoppingItemMapValueSegmentPriceList(DaraModel):
    def __init__(
        self,
        segment_position: main_models.ModuleGroupItemShoppingItemMapValueSegmentPriceListSegmentPosition = None,
        search_price: main_models.ModuleGroupItemShoppingItemMapValueSegmentPriceListSearchPrice = None,
    ):
        self.segment_position = segment_position
        self.search_price = search_price

    def validate(self):
        if self.segment_position:
            self.segment_position.validate()
        if self.search_price:
            self.search_price.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.segment_position is not None:
            result['segment_position'] = self.segment_position.to_map()

        if self.search_price is not None:
            result['search_price'] = self.search_price.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('segment_position') is not None:
            temp_model = main_models.ModuleGroupItemShoppingItemMapValueSegmentPriceListSegmentPosition()
            self.segment_position = temp_model.from_map(m.get('segment_position'))

        if m.get('search_price') is not None:
            temp_model = main_models.ModuleGroupItemShoppingItemMapValueSegmentPriceListSearchPrice()
            self.search_price = temp_model.from_map(m.get('search_price'))

        return self

class ModuleGroupItemShoppingItemMapValueSegmentPriceListSearchPrice(DaraModel):
    def __init__(
        self,
        ticket_price: int = None,
        sell_price: int = None,
        tax: int = None,
    ):
        self.ticket_price = ticket_price
        self.sell_price = sell_price
        self.tax = tax

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.sell_price is not None:
            result['sell_price'] = self.sell_price

        if self.tax is not None:
            result['tax'] = self.tax

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('sell_price') is not None:
            self.sell_price = m.get('sell_price')

        if m.get('tax') is not None:
            self.tax = m.get('tax')

        return self

class ModuleGroupItemShoppingItemMapValueSegmentPriceListSegmentPosition(DaraModel):
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

class ModuleGroupItemShoppingItemMapValueSearchPrice(DaraModel):
    def __init__(
        self,
        ticket_price: int = None,
        sell_price: int = None,
        tax: int = None,
    ):
        self.ticket_price = ticket_price
        self.sell_price = sell_price
        self.tax = tax

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.sell_price is not None:
            result['sell_price'] = self.sell_price

        if self.tax is not None:
            result['tax'] = self.tax

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('sell_price') is not None:
            self.sell_price = m.get('sell_price')

        if m.get('tax') is not None:
            self.tax = m.get('tax')

        return self

class ModuleGroupItemShoppingItemMapValueCabinQuantityList(DaraModel):
    def __init__(
        self,
        segment_position: main_models.ModuleGroupItemShoppingItemMapValueCabinQuantityListSegmentPosition = None,
        cabin: main_models.ModuleGroupItemShoppingItemMapValueCabinQuantityListCabin = None,
    ):
        self.segment_position = segment_position
        self.cabin = cabin

    def validate(self):
        if self.segment_position:
            self.segment_position.validate()
        if self.cabin:
            self.cabin.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.segment_position is not None:
            result['segment_position'] = self.segment_position.to_map()

        if self.cabin is not None:
            result['cabin'] = self.cabin.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('segment_position') is not None:
            temp_model = main_models.ModuleGroupItemShoppingItemMapValueCabinQuantityListSegmentPosition()
            self.segment_position = temp_model.from_map(m.get('segment_position'))

        if m.get('cabin') is not None:
            temp_model = main_models.ModuleGroupItemShoppingItemMapValueCabinQuantityListCabin()
            self.cabin = temp_model.from_map(m.get('cabin'))

        return self

class ModuleGroupItemShoppingItemMapValueCabinQuantityListCabin(DaraModel):
    def __init__(
        self,
        cabin: str = None,
        cabin_class: str = None,
        cabin_class_name: str = None,
        quantity: str = None,
    ):
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.cabin_class_name = cabin_class_name
        self.quantity = quantity

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

        if self.quantity is not None:
            result['quantity'] = self.quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('cabin_class_name') is not None:
            self.cabin_class_name = m.get('cabin_class_name')

        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')

        return self

class ModuleGroupItemShoppingItemMapValueCabinQuantityListSegmentPosition(DaraModel):
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

