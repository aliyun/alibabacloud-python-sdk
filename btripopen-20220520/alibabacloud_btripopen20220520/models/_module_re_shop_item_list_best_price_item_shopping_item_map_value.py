# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class ModuleReShopItemListBestPriceItemShoppingItemMapValue(DaraModel):
    def __init__(
        self,
        cabin_quantity_list: List[main_models.ModuleReShopItemListBestPriceItemShoppingItemMapValueCabinQuantityList] = None,
        search_price: main_models.ModuleReShopItemListBestPriceItemShoppingItemMapValueSearchPrice = None,
        segment_price_list: List[main_models.ModuleReShopItemListBestPriceItemShoppingItemMapValueSegmentPriceList] = None,
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
                temp_model = main_models.ModuleReShopItemListBestPriceItemShoppingItemMapValueCabinQuantityList()
                self.cabin_quantity_list.append(temp_model.from_map(k1))

        if m.get('search_price') is not None:
            temp_model = main_models.ModuleReShopItemListBestPriceItemShoppingItemMapValueSearchPrice()
            self.search_price = temp_model.from_map(m.get('search_price'))

        self.segment_price_list = []
        if m.get('segment_price_list') is not None:
            for k1 in m.get('segment_price_list'):
                temp_model = main_models.ModuleReShopItemListBestPriceItemShoppingItemMapValueSegmentPriceList()
                self.segment_price_list.append(temp_model.from_map(k1))

        return self

class ModuleReShopItemListBestPriceItemShoppingItemMapValueSegmentPriceList(DaraModel):
    def __init__(
        self,
        segment_position: main_models.ModuleReShopItemListBestPriceItemShoppingItemMapValueSegmentPriceListSegmentPosition = None,
        search_price: main_models.ModuleReShopItemListBestPriceItemShoppingItemMapValueSegmentPriceListSearchPrice = None,
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
            temp_model = main_models.ModuleReShopItemListBestPriceItemShoppingItemMapValueSegmentPriceListSegmentPosition()
            self.segment_position = temp_model.from_map(m.get('segment_position'))

        if m.get('search_price') is not None:
            temp_model = main_models.ModuleReShopItemListBestPriceItemShoppingItemMapValueSegmentPriceListSearchPrice()
            self.search_price = temp_model.from_map(m.get('search_price'))

        return self

class ModuleReShopItemListBestPriceItemShoppingItemMapValueSegmentPriceListSearchPrice(DaraModel):
    def __init__(
        self,
        total_amount: int = None,
        handling_amount: int = None,
        upgrade_amount: int = None,
        tax_diff_amount: int = None,
        has_price: bool = None,
        non_price_text: str = None,
    ):
        self.total_amount = total_amount
        self.handling_amount = handling_amount
        self.upgrade_amount = upgrade_amount
        self.tax_diff_amount = tax_diff_amount
        self.has_price = has_price
        self.non_price_text = non_price_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_amount is not None:
            result['total_amount'] = self.total_amount

        if self.handling_amount is not None:
            result['handling_amount'] = self.handling_amount

        if self.upgrade_amount is not None:
            result['upgrade_amount'] = self.upgrade_amount

        if self.tax_diff_amount is not None:
            result['tax_diff_amount'] = self.tax_diff_amount

        if self.has_price is not None:
            result['has_price'] = self.has_price

        if self.non_price_text is not None:
            result['non_price_text'] = self.non_price_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total_amount') is not None:
            self.total_amount = m.get('total_amount')

        if m.get('handling_amount') is not None:
            self.handling_amount = m.get('handling_amount')

        if m.get('upgrade_amount') is not None:
            self.upgrade_amount = m.get('upgrade_amount')

        if m.get('tax_diff_amount') is not None:
            self.tax_diff_amount = m.get('tax_diff_amount')

        if m.get('has_price') is not None:
            self.has_price = m.get('has_price')

        if m.get('non_price_text') is not None:
            self.non_price_text = m.get('non_price_text')

        return self

class ModuleReShopItemListBestPriceItemShoppingItemMapValueSegmentPriceListSegmentPosition(DaraModel):
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

class ModuleReShopItemListBestPriceItemShoppingItemMapValueSearchPrice(DaraModel):
    def __init__(
        self,
        total_amount: int = None,
        handling_amount: int = None,
        upgrade_amount: int = None,
        tax_diff_amount: int = None,
        has_price: bool = None,
        non_price_text: str = None,
    ):
        self.total_amount = total_amount
        self.handling_amount = handling_amount
        self.upgrade_amount = upgrade_amount
        self.tax_diff_amount = tax_diff_amount
        self.has_price = has_price
        self.non_price_text = non_price_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_amount is not None:
            result['total_amount'] = self.total_amount

        if self.handling_amount is not None:
            result['handling_amount'] = self.handling_amount

        if self.upgrade_amount is not None:
            result['upgrade_amount'] = self.upgrade_amount

        if self.tax_diff_amount is not None:
            result['tax_diff_amount'] = self.tax_diff_amount

        if self.has_price is not None:
            result['has_price'] = self.has_price

        if self.non_price_text is not None:
            result['non_price_text'] = self.non_price_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total_amount') is not None:
            self.total_amount = m.get('total_amount')

        if m.get('handling_amount') is not None:
            self.handling_amount = m.get('handling_amount')

        if m.get('upgrade_amount') is not None:
            self.upgrade_amount = m.get('upgrade_amount')

        if m.get('tax_diff_amount') is not None:
            self.tax_diff_amount = m.get('tax_diff_amount')

        if m.get('has_price') is not None:
            self.has_price = m.get('has_price')

        if m.get('non_price_text') is not None:
            self.non_price_text = m.get('non_price_text')

        return self

class ModuleReShopItemListBestPriceItemShoppingItemMapValueCabinQuantityList(DaraModel):
    def __init__(
        self,
        segment_position: main_models.ModuleReShopItemListBestPriceItemShoppingItemMapValueCabinQuantityListSegmentPosition = None,
        cabin_info: main_models.ModuleReShopItemListBestPriceItemShoppingItemMapValueCabinQuantityListCabinInfo = None,
    ):
        self.segment_position = segment_position
        self.cabin_info = cabin_info

    def validate(self):
        if self.segment_position:
            self.segment_position.validate()
        if self.cabin_info:
            self.cabin_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.segment_position is not None:
            result['segment_position'] = self.segment_position.to_map()

        if self.cabin_info is not None:
            result['cabin_info'] = self.cabin_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('segment_position') is not None:
            temp_model = main_models.ModuleReShopItemListBestPriceItemShoppingItemMapValueCabinQuantityListSegmentPosition()
            self.segment_position = temp_model.from_map(m.get('segment_position'))

        if m.get('cabin_info') is not None:
            temp_model = main_models.ModuleReShopItemListBestPriceItemShoppingItemMapValueCabinQuantityListCabinInfo()
            self.cabin_info = temp_model.from_map(m.get('cabin_info'))

        return self

class ModuleReShopItemListBestPriceItemShoppingItemMapValueCabinQuantityListCabinInfo(DaraModel):
    def __init__(
        self,
        cabin: str = None,
        cabin_class: str = None,
        cabin_class_name: str = None,
        quantity: str = None,
        cabin_class_memo: str = None,
        specification: str = None,
    ):
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.cabin_class_name = cabin_class_name
        self.quantity = quantity
        self.cabin_class_memo = cabin_class_memo
        self.specification = specification

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

        if self.cabin_class_memo is not None:
            result['cabin_class_memo'] = self.cabin_class_memo

        if self.specification is not None:
            result['specification'] = self.specification

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

        if m.get('cabin_class_memo') is not None:
            self.cabin_class_memo = m.get('cabin_class_memo')

        if m.get('specification') is not None:
            self.specification = m.get('specification')

        return self

class ModuleReShopItemListBestPriceItemShoppingItemMapValueCabinQuantityListSegmentPosition(DaraModel):
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

