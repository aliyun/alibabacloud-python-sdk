# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ListHotelOrderResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        page: main_models.ListHotelOrderResponseBodyPage = None,
        request_id: str = None,
        result: List[main_models.ListHotelOrderResponseBodyResult] = None,
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
            for v1 in self.result:
                 if v1:
                    v1.validate()

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

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Page') is not None:
            temp_model = main_models.ListHotelOrderResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListHotelOrderResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListHotelOrderResponseBodyResult(DaraModel):
    def __init__(
        self,
        amt: int = None,
        apply_amt: int = None,
        delivery_method: str = None,
        delivery_room_name: str = None,
        delivery_time: int = None,
        gmt_create: int = None,
        icon: str = None,
        item_id: int = None,
        item_type: str = None,
        name: str = None,
        order_no: str = None,
        order_status: str = None,
        payment_method: str = None,
        quantity: int = None,
        room_no: str = None,
        start_time: int = None,
        status: str = None,
        sum_amt: int = None,
        type: str = None,
        type_icon_url: str = None,
        type_name: str = None,
    ):
        self.amt = amt
        self.apply_amt = apply_amt
        self.delivery_method = delivery_method
        self.delivery_room_name = delivery_room_name
        self.delivery_time = delivery_time
        self.gmt_create = gmt_create
        self.icon = icon
        self.item_id = item_id
        self.item_type = item_type
        self.name = name
        self.order_no = order_no
        self.order_status = order_status
        self.payment_method = payment_method
        self.quantity = quantity
        self.room_no = room_no
        self.start_time = start_time
        self.status = status
        self.sum_amt = sum_amt
        self.type = type
        self.type_icon_url = type_icon_url
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amt is not None:
            result['Amt'] = self.amt

        if self.apply_amt is not None:
            result['ApplyAmt'] = self.apply_amt

        if self.delivery_method is not None:
            result['DeliveryMethod'] = self.delivery_method

        if self.delivery_room_name is not None:
            result['DeliveryRoomName'] = self.delivery_room_name

        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.item_type is not None:
            result['ItemType'] = self.item_type

        if self.name is not None:
            result['Name'] = self.name

        if self.order_no is not None:
            result['OrderNo'] = self.order_no

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        if self.payment_method is not None:
            result['PaymentMethod'] = self.payment_method

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.sum_amt is not None:
            result['SumAmt'] = self.sum_amt

        if self.type is not None:
            result['Type'] = self.type

        if self.type_icon_url is not None:
            result['TypeIconUrl'] = self.type_icon_url

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amt') is not None:
            self.amt = m.get('Amt')

        if m.get('ApplyAmt') is not None:
            self.apply_amt = m.get('ApplyAmt')

        if m.get('DeliveryMethod') is not None:
            self.delivery_method = m.get('DeliveryMethod')

        if m.get('DeliveryRoomName') is not None:
            self.delivery_room_name = m.get('DeliveryRoomName')

        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        if m.get('PaymentMethod') is not None:
            self.payment_method = m.get('PaymentMethod')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SumAmt') is not None:
            self.sum_amt = m.get('SumAmt')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('TypeIconUrl') is not None:
            self.type_icon_url = m.get('TypeIconUrl')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        return self

class ListHotelOrderResponseBodyPage(DaraModel):
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

