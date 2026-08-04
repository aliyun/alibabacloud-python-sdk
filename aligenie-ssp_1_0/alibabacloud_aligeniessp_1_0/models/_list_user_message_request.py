# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class ListUserMessageRequest(DaraModel):
    def __init__(
        self,
        before_time: str = None,
        user_info: main_models.ListUserMessageRequestUserInfo = None,
        limit: int = None,
    ):
        # After a specific point in time
        self.before_time = before_time
        # User identifier information
        # 
        # This parameter is required.
        self.user_info = user_info
        # Number of records to query
        self.limit = limit

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        if self.limit is not None:
            result['limit'] = self.limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')

        if m.get('UserInfo') is not None:
            temp_model = main_models.ListUserMessageRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        return self

class ListUserMessageRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type. When the encoding type is SKILLID, this value is the application\\"s Skill ID. When the encoding type is PACKAGENAME, this value is the packageName of the corresponding client app.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. There are multiple ways to obtain the user identifier for Maojing, and each method corresponds to a different encoding type: - PACKAGENAME: APK package name, used for Android application client links - SKILLID: Skill ID, used for cloud-based links
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User identifier (userOpenId or userUnionId)
        # 
        # This parameter is required.
        self.id = id
        # Type of user ID: - OPENID: Default user ID identifier - UNIONID: Organization-level user ID identifier, available only after an organization has been registered on the Maojing skill application Open Platform
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. Required when IdType is UNION_ID
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

