# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class DeviceControlRequest(DaraModel):
    def __init__(
        self,
        payload: main_models.DeviceControlRequestPayload = None,
        user_info: main_models.DeviceControlRequestUserInfo = None,
    ):
        self.payload = payload
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
            temp_model = main_models.DeviceControlRequestPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.DeviceControlRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class DeviceControlRequestUserInfo(DaraModel):
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

class DeviceControlRequestPayload(DaraModel):
    def __init__(
        self,
        category: str = None,
        cmd: str = None,
        device_number: str = None,
        extend_info: str = None,
        location: str = None,
        properties: Dict[str, str] = None,
    ):
        # This parameter is required.
        self.category = category
        # This parameter is required.
        self.cmd = cmd
        # This parameter is required.
        self.device_number = device_number
        self.extend_info = extend_info
        # This parameter is required.
        self.location = location
        self.properties = properties

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.cmd is not None:
            result['Cmd'] = self.cmd

        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.location is not None:
            result['Location'] = self.location

        if self.properties is not None:
            result['Properties'] = self.properties

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')

        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        return self

