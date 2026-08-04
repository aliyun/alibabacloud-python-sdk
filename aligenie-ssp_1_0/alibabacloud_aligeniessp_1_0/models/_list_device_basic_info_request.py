# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ListDeviceBasicInfoRequest(DaraModel):
    def __init__(
        self,
        device_infos: main_models.ListDeviceBasicInfoRequestDeviceInfos = None,
    ):
        # List of device identity information.
        self.device_infos = device_infos

    def validate(self):
        if self.device_infos:
            self.device_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_infos is not None:
            result['DeviceInfos'] = self.device_infos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfos') is not None:
            temp_model = main_models.ListDeviceBasicInfoRequestDeviceInfos()
            self.device_infos = temp_model.from_map(m.get('DeviceInfos'))

        return self

class ListDeviceBasicInfoRequestDeviceInfos(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id_type: str = None,
        ids: List[str] = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type. Enter the Project ID of the project where the product resides. You can view this in the Tmall Genie AI Platform console.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. Enter **PROJECT_ID** here.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Type of device ID:
        # - OPEN_ID: Default device ID identity.
        # - UNION_ID: Organization-dimension device ID identity. You must request an organization in advance on the Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # List of device identity information.
        self.ids = ids
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

        if self.id_type is not None:
            result['IdType'] = self.id_type

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')

        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')

        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        return self

