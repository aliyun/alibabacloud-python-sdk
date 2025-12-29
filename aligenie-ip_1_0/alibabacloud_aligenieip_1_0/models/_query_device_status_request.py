# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class QueryDeviceStatusRequest(DaraModel):
    def __init__(
        self,
        payload: main_models.QueryDeviceStatusRequestPayload = None,
        user_info: main_models.QueryDeviceStatusRequestUserInfo = None,
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
            temp_model = main_models.QueryDeviceStatusRequestPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.QueryDeviceStatusRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class QueryDeviceStatusRequestUserInfo(DaraModel):
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

class QueryDeviceStatusRequestPayload(DaraModel):
    def __init__(
        self,
        location_devices: List[main_models.QueryDeviceStatusRequestPayloadLocationDevices] = None,
        properties: Dict[str, str] = None,
    ):
        self.location_devices = location_devices
        self.properties = properties

    def validate(self):
        if self.location_devices:
            for v1 in self.location_devices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LocationDevices'] = []
        if self.location_devices is not None:
            for k1 in self.location_devices:
                result['LocationDevices'].append(k1.to_map() if k1 else None)

        if self.properties is not None:
            result['Properties'] = self.properties

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.location_devices = []
        if m.get('LocationDevices') is not None:
            for k1 in m.get('LocationDevices'):
                temp_model = main_models.QueryDeviceStatusRequestPayloadLocationDevices()
                self.location_devices.append(temp_model.from_map(k1))

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        return self

class QueryDeviceStatusRequestPayloadLocationDevices(DaraModel):
    def __init__(
        self,
        device_number: str = None,
        device_type: str = None,
        location: str = None,
    ):
        self.device_number = device_number
        self.device_type = device_type
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.location is not None:
            result['Location'] = self.location

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        return self

