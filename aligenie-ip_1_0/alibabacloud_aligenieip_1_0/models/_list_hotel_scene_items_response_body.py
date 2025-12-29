# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ListHotelSceneItemsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.ListHotelSceneItemsResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.ListHotelSceneItemsResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListHotelSceneItemsResponseBodyResult(DaraModel):
    def __init__(
        self,
        page: main_models.ListHotelSceneItemsResponseBodyResultPage = None,
        scene_item_list: List[main_models.ListHotelSceneItemsResponseBodyResultSceneItemList] = None,
    ):
        self.page = page
        self.scene_item_list = scene_item_list

    def validate(self):
        if self.page:
            self.page.validate()
        if self.scene_item_list:
            for v1 in self.scene_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page.to_map()

        result['SceneItemList'] = []
        if self.scene_item_list is not None:
            for k1 in self.scene_item_list:
                result['SceneItemList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = main_models.ListHotelSceneItemsResponseBodyResultPage()
            self.page = temp_model.from_map(m.get('Page'))

        self.scene_item_list = []
        if m.get('SceneItemList') is not None:
            for k1 in m.get('SceneItemList'):
                temp_model = main_models.ListHotelSceneItemsResponseBodyResultSceneItemList()
                self.scene_item_list.append(temp_model.from_map(k1))

        return self

class ListHotelSceneItemsResponseBodyResultSceneItemList(DaraModel):
    def __init__(
        self,
        beyond_limit_reply: str = None,
        category: str = None,
        delivery_method: str = None,
        icon: str = None,
        id: int = None,
        limit_number: int = None,
        limit_switch: int = None,
        name: str = None,
        payment_method: str = None,
        price: int = None,
        robot_name: str = None,
        status: str = None,
        type: str = None,
        update_time: int = None,
    ):
        self.beyond_limit_reply = beyond_limit_reply
        self.category = category
        self.delivery_method = delivery_method
        self.icon = icon
        # id
        self.id = id
        self.limit_number = limit_number
        self.limit_switch = limit_switch
        self.name = name
        self.payment_method = payment_method
        self.price = price
        self.robot_name = robot_name
        self.status = status
        self.type = type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.beyond_limit_reply is not None:
            result['BeyondLimitReply'] = self.beyond_limit_reply

        if self.category is not None:
            result['Category'] = self.category

        if self.delivery_method is not None:
            result['DeliveryMethod'] = self.delivery_method

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.id is not None:
            result['Id'] = self.id

        if self.limit_number is not None:
            result['LimitNumber'] = self.limit_number

        if self.limit_switch is not None:
            result['LimitSwitch'] = self.limit_switch

        if self.name is not None:
            result['Name'] = self.name

        if self.payment_method is not None:
            result['PaymentMethod'] = self.payment_method

        if self.price is not None:
            result['Price'] = self.price

        if self.robot_name is not None:
            result['RobotName'] = self.robot_name

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeyondLimitReply') is not None:
            self.beyond_limit_reply = m.get('BeyondLimitReply')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeliveryMethod') is not None:
            self.delivery_method = m.get('DeliveryMethod')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LimitNumber') is not None:
            self.limit_number = m.get('LimitNumber')

        if m.get('LimitSwitch') is not None:
            self.limit_switch = m.get('LimitSwitch')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PaymentMethod') is not None:
            self.payment_method = m.get('PaymentMethod')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListHotelSceneItemsResponseBodyResultPage(DaraModel):
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

