# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class GetDeviceTagRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.GetDeviceTagRequestDeviceInfo = None,
    ):
        # List of device identity information.
        # 
        # This parameter is required.
        self.device_info = device_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = main_models.GetDeviceTagRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        return self

class GetDeviceTagRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # The value corresponding to the encoding type. Enter the Project ID of the project in the Tmall Genie AI platform where the product\\"s ProductKey resides.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. Enter **PROJECT_ID** here.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Device identifier. Enter the value of deviceOpenId or deviceUnionId.
        # 
        # This parameter is required.
        self.id = id
        # The type of Device ID:
        #  - OPEN_ID: The default device identity.
        # - UNION_ID: The device identity at the organization dimension, which requires a prior request for an organization on the Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. Required if IdType is UNION_ID.
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

