# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ListHotelSceneItemResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        page: main_models.ListHotelSceneItemResponseBodyPage = None,
        request_id: str = None,
        result: main_models.ListHotelSceneItemResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.page = page
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Page') is not None:
            temp_model = main_models.ListHotelSceneItemResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListHotelSceneItemResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListHotelSceneItemResponseBodyResult(DaraModel):
    def __init__(
        self,
        second_category_list: List[main_models.ListHotelSceneItemResponseBodyResultSecondCategoryList] = None,
    ):
        self.second_category_list = second_category_list

    def validate(self):
        if self.second_category_list:
            for v1 in self.second_category_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SecondCategoryList'] = []
        if self.second_category_list is not None:
            for k1 in self.second_category_list:
                result['SecondCategoryList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.second_category_list = []
        if m.get('SecondCategoryList') is not None:
            for k1 in m.get('SecondCategoryList'):
                temp_model = main_models.ListHotelSceneItemResponseBodyResultSecondCategoryList()
                self.second_category_list.append(temp_model.from_map(k1))

        return self

class ListHotelSceneItemResponseBodyResultSecondCategoryList(DaraModel):
    def __init__(
        self,
        item_list: List[main_models.ListHotelSceneItemResponseBodyResultSecondCategoryListItemList] = None,
        second_category_name: str = None,
    ):
        self.item_list = item_list
        self.second_category_name = second_category_name

    def validate(self):
        if self.item_list:
            for v1 in self.item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ItemList'] = []
        if self.item_list is not None:
            for k1 in self.item_list:
                result['ItemList'].append(k1.to_map() if k1 else None)

        if self.second_category_name is not None:
            result['SecondCategoryName'] = self.second_category_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_list = []
        if m.get('ItemList') is not None:
            for k1 in m.get('ItemList'):
                temp_model = main_models.ListHotelSceneItemResponseBodyResultSecondCategoryListItemList()
                self.item_list.append(temp_model.from_map(k1))

        if m.get('SecondCategoryName') is not None:
            self.second_category_name = m.get('SecondCategoryName')

        return self

class ListHotelSceneItemResponseBodyResultSecondCategoryListItemList(DaraModel):
    def __init__(
        self,
        category: str = None,
        icon: str = None,
        id: str = None,
        name: str = None,
        price: int = None,
        residue_limit: int = None,
        status: str = None,
        type: str = None,
    ):
        self.category = category
        self.icon = icon
        self.id = id
        self.name = name
        self.price = price
        self.residue_limit = residue_limit
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.price is not None:
            result['Price'] = self.price

        if self.residue_limit is not None:
            result['ResidueLimit'] = self.residue_limit

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('ResidueLimit') is not None:
            self.residue_limit = m.get('ResidueLimit')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListHotelSceneItemResponseBodyPage(DaraModel):
    def __init__(
        self,
        has_next: bool = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
        total_page: int = None,
    ):
        self.has_next = has_next
        self.page_number = page_number
        self.page_size = page_size
        self.total = total
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_next is not None:
            result['HasNext'] = self.has_next

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

