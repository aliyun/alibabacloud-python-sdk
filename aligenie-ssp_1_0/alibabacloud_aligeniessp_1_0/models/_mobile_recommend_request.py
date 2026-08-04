# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class MobileRecommendRequest(DaraModel):
    def __init__(
        self,
        bot_id: str = None,
        count: str = None,
        device_info: main_models.MobileRecommendRequestDeviceInfo = None,
        style: str = None,
        type: str = None,
        user_info: main_models.MobileRecommendRequestUserInfo = None,
    ):
        # Bot ID.
        self.bot_id = bot_id
        # Quantity of recommended Result
        self.count = count
        # Device identification information.
        # 
        # This parameter is required.
        self.device_info = device_info
        # Required when the request type is STYLE.
        self.style = style
        # Request Type: Obtain daily recommendations, hot songs, or genre-based playlists.
        self.type = type
        # User information – userId
        # 
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bot_id is not None:
            result['BotId'] = self.bot_id

        if self.count is not None:
            result['Count'] = self.count

        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()

        if self.style is not None:
            result['Style'] = self.style

        if self.type is not None:
            result['Type'] = self.type

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DeviceInfo') is not None:
            temp_model = main_models.MobileRecommendRequestDeviceInfo()
            self.device_info = temp_model.from_map(m.get('DeviceInfo'))

        if m.get('Style') is not None:
            self.style = m.get('Style')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserInfo') is not None:
            temp_model = main_models.MobileRecommendRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class MobileRecommendRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # The value corresponding to the encoding Type. Enter the Project ID of the project to which this product belongs.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # ID value
        # 
        # This parameter is required.
        self.id = id
        # ID Type
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. This parameter is Required when IdType is set to UNION_ID.
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

class MobileRecommendRequestDeviceInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # Value corresponding to the encoding type. Enter the Project ID of the project to which the product belongs.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding type. Enter PROJECT_ID here.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # Device ID. Enter the value of deviceOpenId or deviceUnionId.
        # 
        # This parameter is required.
        self.id = id
        # Type of the device ID.
        # 
        # OPEN_ID: Default device ID.
        # UNION_ID: Organization-level device ID. This value is available only after an organization has been requested on the Tmall Genie Skill Application Open Platform.
        # 
        # This parameter is required.
        self.id_type = id_type
        # Organization ID. This parameter is required when **IdType** is set to **UNION_ID**.
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

