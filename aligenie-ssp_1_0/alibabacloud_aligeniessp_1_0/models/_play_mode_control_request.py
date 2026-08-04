# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class PlayModeControlRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.PlayModeControlRequestDeviceInfo = None,
        open_play_mode_control_request: main_models.PlayModeControlRequestOpenPlayModeControlRequest = None,
        user_info: main_models.PlayModeControlRequestUserInfo = None,
    ):
        # Device identity information
        # 
        # This parameter is required.
        self.device_info = device_info
        # Business parameters
        # 
        # This parameter is required.
        self.open_play_mode_control_request = open_play_mode_control_request
        # User Identifier information
        # 
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_play_mode_control_request:
            self.open_play_mode_control_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        if self.open_play_mode_control_request is not None:
            result['OpenPlayModeControlRequest'] = self.open_play_mode_control_request.to_map()

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = main_models.PlayModeControlRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('OpenPlayModeControlRequest') is not None:
            temp_model = main_models.PlayModeControlRequestOpenPlayModeControlRequest()
            self.open_play_mode_control_request = temp_model.from_map(m.get('OpenPlayModeControlRequest'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.PlayModeControlRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class PlayModeControlRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type.
        # 
        # When the encoding type is `SKILL_ID`, the value is the application\\"s Skill ID. When the encoding type is `PACKAGE_NAME`, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the User Identifier for Tmall Genie, and each method corresponds to a different encoding type.
        # 
        # `PACKAGE_NAME`: APK package name, used for the Android application customer ingest endpoint. `SKILL_ID`: Skill ID, used for the cloud-side ingest endpoint.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User Identifier, set to userOpenId or userUnionId.
        # 
        # This parameter is required.
        self.id = id
        # Type of User ID
        # 
        # `OPEN_ID`: The default User ID identity. `UNION_ID`: Organization-dimension User ID identity. This value is available only after an organization has been requested on the Tmall Genie Skill Application Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. Required when IdType is UNION_ID.
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

class PlayModeControlRequestOpenPlayModeControlRequest(DaraModel):
    def __init__(
        self,
        open_play_mode: str = None,
    ):
        # Playback mode
        # 
        # List loop: Repeat; Shuffle: Shuffle; Single track loop: RepeatOne; NAT mode: Normal;
        # 
        # This parameter is required.
        self.open_play_mode = open_play_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_play_mode is not None:
            result['OpenPlayMode'] = self.open_play_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenPlayMode') is not None:
            self.open_play_mode = m.get('OpenPlayMode')

        return self

class PlayModeControlRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type
        # 
        # When the encoding type is `SKILL_ID`, the value is the application\\"s Skill ID. When the encoding type is `PACKAGE_NAME`, the value is the packageName of the corresponding client app.
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
        # Type of device ID
        # 
        # `OPEN_ID`: Default device ID identity. `UNION_ID`: Organization-dimension device ID identity, available only after an organization has been requested on the Tmall Genie Skill Application Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. Required when IdType is UNION_ID.
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

