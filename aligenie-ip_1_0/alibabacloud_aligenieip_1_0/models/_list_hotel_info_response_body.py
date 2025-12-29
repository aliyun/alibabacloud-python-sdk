# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ListHotelInfoResponseBody(DaraModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.ListHotelInfoResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extentions is not None:
            result['Extentions'] = self.extentions

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListHotelInfoResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class ListHotelInfoResponseBodyResult(DaraModel):
    def __init__(
        self,
        auth_account: List[main_models.ListHotelInfoResponseBodyResultAuthAccount] = None,
        hotel_address: str = None,
        hotel_id: str = None,
        hotel_name: str = None,
    ):
        self.auth_account = auth_account
        self.hotel_address = hotel_address
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name

    def validate(self):
        if self.auth_account:
            for v1 in self.auth_account:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthAccount'] = []
        if self.auth_account is not None:
            for k1 in self.auth_account:
                result['AuthAccount'].append(k1.to_map() if k1 else None)

        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auth_account = []
        if m.get('AuthAccount') is not None:
            for k1 in m.get('AuthAccount'):
                temp_model = main_models.ListHotelInfoResponseBodyResultAuthAccount()
                self.auth_account.append(temp_model.from_map(k1))

        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')

        return self

class ListHotelInfoResponseBodyResultAuthAccount(DaraModel):
    def __init__(
        self,
        user_name: str = None,
    ):
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

