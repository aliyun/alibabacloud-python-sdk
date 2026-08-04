# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class IndexControlPlayingListRequest(DaraModel):
    def __init__(
        self,
        device_info: main_models.IndexControlPlayingListRequestDeviceInfo = None,
        open_index_control_request: main_models.IndexControlPlayingListRequestOpenIndexControlRequest = None,
        user_info: main_models.IndexControlPlayingListRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # Business parameters
        # 
        # This parameter is required.
        self.open_index_control_request = open_index_control_request
        # User Identifier information
        # 
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_index_control_request:
            self.open_index_control_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        if self.open_index_control_request is not None:
            result['OpenIndexControlRequest'] = self.open_index_control_request.to_map()

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = main_models.IndexControlPlayingListRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('OpenIndexControlRequest') is not None:
            temp_model = main_models.IndexControlPlayingListRequestOpenIndexControlRequest()
            self.open_index_control_request = temp_model.from_map(m.get('OpenIndexControlRequest'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.IndexControlPlayingListRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class IndexControlPlayingListRequestUserInfo(DaraModel):
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
        # When the encoding type is `SKILL_ID`, the value is the Skill ID of the application. When the encoding type is `PACKAGE_NAME`, the value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the User Identifier for Tmall Genie, and each method corresponds to a different encoding type.
        # 
        # `PACKAGE_NAME`: APK package name, used for the Android application customer link. `SKILL_ID`: Skill ID, used for the cloud-based link.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User Identifier, set to userOpenId or userUnionId.
        # 
        # This parameter is required.
        self.id = id
        # Type of User ID
        # 
        # `OPEN_ID`: The default User ID identity. `UNION_ID`: The organization-dimension User ID identity, which is available only after an organization has been requested on the Tmall Genie Skills Application Open Platform.
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

class IndexControlPlayingListRequestOpenIndexControlRequest(DaraModel):
    def __init__(
        self,
        extend_info: Dict[str, Any] = None,
        index: int = None,
        need_content_continued: bool = None,
    ):
        # Extension information
        self.extend_info = extend_info
        # The index to be played back
        # 
        # This parameter is required.
        self.index = index
        # Whether content playback should continue. Default is false.
        self.need_content_continued = need_content_continued

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.index is not None:
            result['Index'] = self.index

        if self.need_content_continued is not None:
            result['NeedContentContinued'] = self.need_content_continued

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('NeedContentContinued') is not None:
            self.need_content_continued = m.get('NeedContentContinued')

        return self

class IndexControlPlayingListRequestDeviceInfo(DaraModel):
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
        # `PACKAGE_NAME`: APK package name, used for the Android application customer link. `SKILL_ID`: Skill ID, used for the cloud-based link.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Device ID, set to either deviceOpenId or deviceUnionId.
        # 
        # This parameter is required.
        self.id = id
        # Type of device ID
        # 
        # `OPEN_ID`: The default device ID identity. `UNION_ID`: Device ID identity at the organization dimension. This value is available only after an organization has been requested on the Tmall Genie Skill Application Open Platform.
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

