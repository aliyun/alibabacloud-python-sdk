# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieiap_1_0 import models as main_models
from darabonba.model import DaraModel

class WakeUpAppRequest(DaraModel):
    def __init__(
        self,
        is_debug: bool = None,
        path: str = None,
        target_info: main_models.WakeUpAppRequestTargetInfo = None,
    ):
        # The debug identity. When the skill application is in the debugging phase, this setting determines whether the retrieved skill application information is from the editing state or the online state.
        self.is_debug = is_debug
        # The path to launch the application, similar to the Link you enter in the skill application console.
        # 
        # This parameter is required.
        self.path = path
        # Device Information of the target to be launched.
        # 
        # This parameter is required.
        self.target_info = target_info

    def validate(self):
        if self.target_info:
            self.target_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug

        if self.path is not None:
            result['Path'] = self.path

        if self.target_info is not None:
            result['TargetInfo'] = self.target_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('TargetInfo') is not None:
            temp_model = main_models.WakeUpAppRequestTargetInfo()
            self.target_info = temp_model.from_map(m.get('TargetInfo'))

        return self

class WakeUpAppRequestTargetInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        organization_id: str = None,
        target_identity: str = None,
        target_type: str = None,
    ):
        # The value corresponding to the encoding type.  
        # - When the encoding type is SKILLID, the value is the skill ID obtained from the webhook service.  
        # - When the encoding type is PACKAGENAME, the value is the packageName of the corresponding client application.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the MeowGenie device ID, and each method corresponds to a different encoding type:  
        # - PACKAGE_NAME: APK package name  
        # - SKILL_ID: Skill ID
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Organization ID. This is required only when the push type is `XX_UNION_XX`. If you have multiple methods to obtain MeowGenie device IDs and need interoperability among them, you must request an organization from the platform. After approval, the platform will assign an organization ID.
        self.organization_id = organization_id
        # The identity value corresponding to the Push Target Type.
        # 
        # This parameter is required.
        self.target_identity = target_identity
        # Push Target Type, which indicates the type of the obtained device identity:  
        # - `DEVICE_UNION_ID`: Device unionId  
        # - `DEVICE_OPEN_ID`: Device openId
        # 
        # This parameter is required.
        self.target_type = target_type

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

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.target_identity is not None:
            result['TargetIdentity'] = self.target_identity

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')

        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('TargetIdentity') is not None:
            self.target_identity = m.get('TargetIdentity')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

