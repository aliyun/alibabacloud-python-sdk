# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class GetCodeEnhanceRequest(DaraModel):
    def __init__(
        self,
        channel_info: main_models.GetCodeEnhanceRequestChannelInfo = None,
        user_info: main_models.GetCodeEnhanceRequestUserInfo = None,
    ):
        # Activation Channel, such as WeChat mini program or third-party app.
        # 
        # This parameter is required.
        self.channel_info = channel_info
        # List of User Identifier information.
        # 
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.channel_info:
            self.channel_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_info is not None:
            result['ChannelInfo'] = self.channel_info.to_map()

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelInfo') is not None:
            temp_model = main_models.GetCodeEnhanceRequestChannelInfo()
            self.channel_info = temp_model.from_map(m.get('ChannelInfo'))

        if m.get('UserInfo') is not None:
            temp_model = main_models.GetCodeEnhanceRequestUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class GetCodeEnhanceRequestUserInfo(DaraModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # The value corresponding to the encoding type. Enter the Project ID of the project to which the product belongs. You can view it in the Tmall Genie AI Platform console.
        # 
        # This parameter is required.
        self.encode_key = encode_key
        # Encoding Type. Enter PROJECT_ID here.
        # 
        # This parameter is required.
        self.encode_type = encode_type
        # User Identifier. Enter the value of userOpenId or userUnionId.
        # 
        # This parameter is required.
        self.id = id
        # Type of User ID:  
        # OPENID: The default User ID identifier.  
        # UNIONID: The organization-dimension User ID identifier. You must request an organization in advance on the Open Platform.
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

class GetCodeEnhanceRequestChannelInfo(DaraModel):
    def __init__(
        self,
        channel: str = None,
        ext_info: str = None,
    ):
        # Activation Channel, such as WeChat or ThirdApp.
        # 
        # This parameter is required.
        self.channel = channel
        # Extension information.
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['Channel'] = self.channel

        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')

        return self

