# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class PreviousAndNextControlRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.PreviousAndNextControlRequestDeviceInfo = None,
        open_control_playing_list_request: main_models.PreviousAndNextControlRequestOpenControlPlayingListRequest = None,
        user_info: main_models.PreviousAndNextControlRequestUserInfo = None,
    ):
        # Device ID information
        # 
        # This parameter is required.
        self.device_info = device_info
        # Business parameters
        # 
        # This parameter is required.
        self.open_control_playing_list_request = open_control_playing_list_request
        # User identity information
        # 
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_control_playing_list_request:
            self.open_control_playing_list_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        if self.open_control_playing_list_request is not None:
            result['OpenControlPlayingListRequest'] = self.open_control_playing_list_request.to_map()

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = main_models.PreviousAndNextControlRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('OpenControlPlayingListRequest') is not None:
            temp_model = main_models.PreviousAndNextControlRequestOpenControlPlayingListRequest()
            self.open_control_playing_list_request = temp_model.from_map(m.get('OpenControlPlayingListRequest'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.PreviousAndNextControlRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class PreviousAndNextControlRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # The value corresponding to the encoding type.
        # 
        # When the encoding type is `SKILL_ID`, the value is the Skill ID of the application. When the encoding type is `PACKAGE_NAME`, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the user identity from Tmall Genie, and each method corresponds to a different encoding type.
        # 
        # `PACKAGE_NAME`: APK package name, used for Android application client-side flows. `SKILL_ID`: Skill ID, used for cloud-side flows.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User identifier, set to userOpenId or userUnionId.
        # 
        # This parameter is required.
        self.id = id
        # The type of User ID.
        # 
        # `OPEN_ID`: The default user identity. `UNION_ID`: The organization-dimension user identity, which is available only after an organization has been requested on the Tmall Genie Skill Application Open Platform.
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

class PreviousAndNextControlRequestOpenControlPlayingListRequest(DaraModel):
    def __init__(
        self,
        cmd: str = None,
        extend_info: Dict[str, Any] = None,
        is_from_device: bool = None,
    ):
        # Next track: NEXT; Previous track: PREVIOUS
        # 
        # This parameter is required.
        self.cmd = cmd
        self.extend_info = extend_info
        # Whether initiated by the device. Default is false.
        self.is_from_device = is_from_device

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cmd is not None:
            result['Cmd'] = self.cmd

        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.is_from_device is not None:
            result['IsFromDevice'] = self.is_from_device

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')

        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('IsFromDevice') is not None:
            self.is_from_device = m.get('IsFromDevice')

        return self

class PreviousAndNextControlRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # The value corresponding to the encoding type.
        # 
        # When the encoding type is `SKILL_ID`, the value is the Skill ID of the application. When the encoding type is `PACKAGE_NAME`, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the device ID for Tmall Genie, and each method corresponds to a different encoding type.  
        # 
        # `PACKAGE_NAME`: APK package name, used for Android application customer journeys. `SKILL_ID`: Skill ID, used for cloud-based journeys.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Device ID, set to deviceOpenId or deviceUnionId.
        # 
        # This parameter is required.
        self.id = id
        # The type of Device ID.
        # 
        # `OPEN_ID`: The default device identity. `UNION_ID`: The organization-dimension device identity, which is available only after an organization has been requested on the Tmall Genie Skill Application Open Platform.
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

