# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class SubmitHotelOrderRequest(DaraModel):
    def __init__(
        self,
        payload: main_models.SubmitHotelOrderRequestPayload = None,
        user_info: main_models.SubmitHotelOrderRequestUserInfo = None,
    ):
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Payload') is not None:
            temp_model = main_models.SubmitHotelOrderRequestPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.SubmitHotelOrderRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class SubmitHotelOrderRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key

        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type

        if self.id is not None:
            result['Id'] = self.id

        if self.id_type is not None:
            result['IdType'] = self.id_type

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')

        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        return self

class SubmitHotelOrderRequestPayload(DaraModel):
    def __init__(
        self,
        item_list: List[main_models.SubmitHotelOrderRequestPayloadItemList] = None,
        type: str = None,
    ):
        # This parameter is required.
        self.item_list = item_list
        # This parameter is required.
        self.type = type

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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_list = []
        if m.get('ItemList') is not None:
            for k1 in m.get('ItemList'):
                temp_model = main_models.SubmitHotelOrderRequestPayloadItemList()
                self.item_list.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SubmitHotelOrderRequestPayloadItemList(DaraModel):
    def __init__(
        self,
        item_id: int = None,
        quantity: int = None,
        remark: str = None,
    ):
        # This parameter is required.
        self.item_id = item_id
        # This parameter is required.
        self.quantity = quantity
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

