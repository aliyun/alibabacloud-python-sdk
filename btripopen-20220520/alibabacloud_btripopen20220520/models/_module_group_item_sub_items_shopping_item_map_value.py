# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class ModuleGroupItemSubItemsShoppingItemMapValue(DaraModel):
    def __init__(
        self,
        search_price: main_models.ModuleGroupItemSubItemsShoppingItemMapValueSearchPrice = None,
    ):
        self.search_price = search_price

    def validate(self):
        if self.search_price:
            self.search_price.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.search_price is not None:
            result['search_price'] = self.search_price.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('search_price') is not None:
            temp_model = main_models.ModuleGroupItemSubItemsShoppingItemMapValueSearchPrice()
            self.search_price = temp_model.from_map(m.get('search_price'))

        return self

class ModuleGroupItemSubItemsShoppingItemMapValueSearchPrice(DaraModel):
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

