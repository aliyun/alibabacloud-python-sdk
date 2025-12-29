# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class GetHotelContactByNumberResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: main_models.GetHotelContactByNumberResponseBodyResult = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetHotelContactByNumberResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class GetHotelContactByNumberResponseBodyResult(DaraModel):
    def __init__(
        self,
        expire_at: str = None,
        hotel_id: str = None,
        icon: str = None,
        name: str = None,
        number: str = None,
        status: int = None,
        type: str = None,
        uuid: str = None,
    ):
        self.expire_at = expire_at
        self.hotel_id = hotel_id
        self.icon = icon
        self.name = name
        self.number = number
        self.status = status
        self.type = type
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_at is not None:
            result['ExpireAt'] = self.expire_at

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.name is not None:
            result['Name'] = self.name

        if self.number is not None:
            result['Number'] = self.number

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireAt') is not None:
            self.expire_at = m.get('ExpireAt')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

