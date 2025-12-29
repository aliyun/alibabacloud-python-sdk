# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ListHotelsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.ListHotelsResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        # RequestId
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
            temp_model = main_models.ListHotelsResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class ListHotelsResponseBodyResult(DaraModel):
    def __init__(
        self,
        hotel_info_list: List[main_models.ListHotelsResponseBodyResultHotelInfoList] = None,
        page: main_models.ListHotelsResponseBodyResultPage = None,
    ):
        self.hotel_info_list = hotel_info_list
        self.page = page

    def validate(self):
        if self.hotel_info_list:
            for v1 in self.hotel_info_list:
                 if v1:
                    v1.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HotelInfoList'] = []
        if self.hotel_info_list is not None:
            for k1 in self.hotel_info_list:
                result['HotelInfoList'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hotel_info_list = []
        if m.get('HotelInfoList') is not None:
            for k1 in m.get('HotelInfoList'):
                temp_model = main_models.ListHotelsResponseBodyResultHotelInfoList()
                self.hotel_info_list.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            temp_model = main_models.ListHotelsResponseBodyResultPage()
            self.page = temp_model.from_map(m.get('Page'))

        return self

class ListHotelsResponseBodyResultPage(DaraModel):
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

class ListHotelsResponseBodyResultHotelInfoList(DaraModel):
    def __init__(
        self,
        account_names: List[str] = None,
        create_time: int = None,
        hotel_address: str = None,
        hotel_id: str = None,
        hotel_name: str = None,
        industry_type: str = None,
        phone_number: str = None,
        related_product_name: str = None,
        room_num: int = None,
        status: int = None,
    ):
        self.account_names = account_names
        self.create_time = create_time
        self.hotel_address = hotel_address
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.industry_type = industry_type
        self.phone_number = phone_number
        self.related_product_name = related_product_name
        self.room_num = room_num
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_names is not None:
            result['AccountNames'] = self.account_names

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name

        if self.industry_type is not None:
            result['IndustryType'] = self.industry_type

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.related_product_name is not None:
            result['RelatedProductName'] = self.related_product_name

        if self.room_num is not None:
            result['RoomNum'] = self.room_num

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNames') is not None:
            self.account_names = m.get('AccountNames')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')

        if m.get('IndustryType') is not None:
            self.industry_type = m.get('IndustryType')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('RelatedProductName') is not None:
            self.related_product_name = m.get('RelatedProductName')

        if m.get('RoomNum') is not None:
            self.room_num = m.get('RoomNum')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

