# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class PlayAndPauseControlRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.PlayAndPauseControlRequestDeviceInfo = None,
        open_play_and_pause_control_param: main_models.PlayAndPauseControlRequestOpenPlayAndPauseControlParam = None,
        user_info: main_models.PlayAndPauseControlRequestUserInfo = None,
    ):
        # Device identity information
        # 
        # This parameter is required.
        self.device_info = device_info
        # Business parameters
        # 
        # This parameter is required.
        self.open_play_and_pause_control_param = open_play_and_pause_control_param
        # User identity information
        # 
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_play_and_pause_control_param:
            self.open_play_and_pause_control_param.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        if self.open_play_and_pause_control_param is not None:
            result['OpenPlayAndPauseControlParam'] = self.open_play_and_pause_control_param.to_map()

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = main_models.PlayAndPauseControlRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('OpenPlayAndPauseControlParam') is not None:
            temp_model = main_models.PlayAndPauseControlRequestOpenPlayAndPauseControlParam()
            self.open_play_and_pause_control_param = temp_model.from_map(m.get('OpenPlayAndPauseControlParam'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.PlayAndPauseControlRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class PlayAndPauseControlRequestUserInfo(DaraModel):
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
        # When the encoding type is `SKILL_ID`, the value is the application\\"s Skill ID. When the encoding type is `PACKAGE_NAME`, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the user identifier from Tmall Genie, and each method corresponds to a different encoding type.
        # 
        # `PACKAGE_NAME`: APK package name, used for the Android application customer flow. `SKILL_ID`: Skill ID, used for the cloud-based flow.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User identifier, set to either userOpenId or userUnionId.
        # 
        # This parameter is required.
        self.id = id
        # The type of User ID.
        # 
        # `OPEN_ID`: The default user ID identity. `UNION_ID`: The organization-dimension user ID identity. This value is available only after an organization has been requested on the Tmall Genie Skill Application Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. Required when IdType is `UNION_ID`.
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

class PlayAndPauseControlRequestOpenPlayAndPauseControlParam(DaraModel):
    def __init__(
        self,
        open_play_and_pause_command: str = None,
    ):
        # Playback: Play; Pause: Pause.
        # 
        # This parameter is required.
        self.open_play_and_pause_command = open_play_and_pause_command

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_play_and_pause_command is not None:
            result['OpenPlayAndPauseCommand'] = self.open_play_and_pause_command

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenPlayAndPauseCommand') is not None:
            self.open_play_and_pause_command = m.get('OpenPlayAndPauseCommand')

        return self

class PlayAndPauseControlRequestDeviceInfo(DaraModel):
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
        # If the encoding type is `SKILL_ID`, the value is the application\\"s Skill ID. If the encoding type is `PACKAGE_NAME`, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the device identity for Tmall Genie, and each method corresponds to a different encoding type.
        # 
        # `PACKAGE_NAME`: APK package name, used for the Android application customer link. `SKILL_ID`: Skill ID, used for the cloud-based link.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Device ID, which can be set to deviceOpenId or deviceUnionId.
        # 
        # This parameter is required.
        self.id = id
        # The type of Device ID.
        # 
        # `OPEN_ID`: The default device ID identity. `UNION_ID`: The organization-dimension device ID identity. This value is available only after an organization has been requested on the Tmall Genie Skill Application Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. This parameter is required if IdType is UNION_ID.
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

