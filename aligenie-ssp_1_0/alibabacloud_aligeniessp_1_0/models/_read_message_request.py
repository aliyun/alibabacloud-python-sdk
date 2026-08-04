# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ReadMessageRequest(DaraModel):
    def __init__(
        self,
        message_id: int = None,
        user_info: main_models.ReadMessageRequestUserInfo = None,
    ):
        # Message ID
        self.message_id = message_id
        # User information
        # 
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('UserInfo') is not None:
            temp_model = main_models.ReadMessageRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class ReadMessageRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type. When the encoding type is SKILLID, this value is the Skill ID of the application. When the encoding type is PACKAGENAME, this value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the User Identifier in Maojing, and each method corresponds to a different encoding type: PACKAGENAME for the APK package name used in Android client application links, and SKILLID for the skill ID used in cloud-based links.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User Identifier (userOpenId or userUnionId)
        # 
        # This parameter is required.
        self.id = id
        # Type of User ID: OPENID is the default User ID identity. UNIONID is the organization-dimension User ID identity, which is available only after an organization has been registered on the Maojing Skill Application Open Platform.
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

