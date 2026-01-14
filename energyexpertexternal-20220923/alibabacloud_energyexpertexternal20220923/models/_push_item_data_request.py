# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class PushItemDataRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        items: main_models.PushItemDataRequestItems = None,
        year: str = None,
    ):
        # The enterprise code.
        # 
        # This parameter is required.
        self.code = code
        # List of data to be pushed.
        # 
        # This parameter is required.
        self.items = items
        # The year of the data created.
        # 
        # This parameter is required.
        self.year = year

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.items is not None:
            result['items'] = self.items.to_map()

        if self.year is not None:
            result['year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('items') is not None:
            temp_model = main_models.PushItemDataRequestItems()
            self.items = temp_model.from_map(m.get('items'))

        if m.get('year') is not None:
            self.year = m.get('year')

        return self

class PushItemDataRequestItems(DaraModel):
    def __init__(
        self,
        code: str = None,
        month: str = None,
        value: float = None,
    ):
        # API data identification.<props="intl">For details: [GetDataItemList ](https://www.alibabacloud.com/help/en/energy-expert/developer-reference/api-energyexpertexternal-2022-09-23-getdataitemlist)
        # 
        # This parameter is required.
        self.code = code
        # The month.
        # 
        # This parameter is required.
        self.month = month
        # The value of the data item.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.month is not None:
            result['month'] = self.month

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('month') is not None:
            self.month = m.get('month')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

