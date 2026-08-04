# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class DeviceControlRequest(DaraModel):
    def __init__(
        self,
        control_request: main_models.DeviceControlRequestControlRequest = None,
        device_info: main_models.DeviceControlRequestDeviceInfo = None,
    ):
        # Input parameters for volume control
        self.control_request = control_request
        # List of device ID information.
        # 
        # This parameter is required.
        self.device_info = device_info

    def validate(self):
        if self.control_request:
            self.control_request.validate()
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_request is not None:
            result['ControlRequest'] = self.control_request.to_map()

        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlRequest') is not None:
            temp_model = main_models.DeviceControlRequestControlRequest()
            self.control_request = temp_model.from_map(m.get('ControlRequest'))

        if m.get('DeviceInfo') is not None:
            temp_model = main_models.DeviceControlRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        return self

class DeviceControlRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type. Enter the Project ID of the project where the product resides. You can View this in the Tmall Genie AI platform console.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding Type. Enter PROJECT_ID here.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Device ID. Enter the value of deviceOpenId or deviceUnionId.
        # 
        # This parameter is required.
        self.id = id
        # The type of Device ID:  
        # OPEN_ID: The default Device ID identity.  
        # UNION_ID: The organization-dimension Device ID identity. You must request an organization in advance on the Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID of the device. Required if IdType is UNION_ID.
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

class DeviceControlRequestControlRequest(DaraModel):
    def __init__(
        self,
        muted: bool = None,
        volume: int = None,
    ):
        # Indicates whether mute is enabled. If this field is set to true, you must also specify the volume value as 0.
        self.muted = muted
        # Target volume value
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.muted is not None:
            result['Muted'] = self.muted

        if self.volume is not None:
            result['Volume'] = self.volume

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Muted') is not None:
            self.muted = m.get('Muted')

        if m.get('Volume') is not None:
            self.volume = m.get('Volume')

        return self

