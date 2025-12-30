# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetAvatarResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetAvatarResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetAvatarResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAvatarResponseBodyData(DaraModel):
    def __init__(
        self,
        avatar: main_models.GetAvatarResponseBodyDataAvatar = None,
    ):
        # The information about the digital human.
        self.avatar = avatar

    def validate(self):
        if self.avatar:
            self.avatar.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar is not None:
            result['Avatar'] = self.avatar.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            temp_model = main_models.GetAvatarResponseBodyDataAvatar()
            self.avatar = temp_model.from_map(m.get('Avatar'))

        return self

class GetAvatarResponseBodyDataAvatar(DaraModel):
    def __init__(
        self,
        avatar_description: str = None,
        avatar_id: str = None,
        avatar_name: str = None,
        avatar_type: str = None,
        height: int = None,
        portrait: str = None,
        thumbnail: str = None,
        transparent: bool = None,
        width: int = None,
    ):
        # The description of the digital human.
        self.avatar_description = avatar_description
        # The ID of the digital human.
        self.avatar_id = avatar_id
        # The name of the digital human.
        self.avatar_name = avatar_name
        # The type of the digital human.
        self.avatar_type = avatar_type
        # The height of the digital human image in pixels.
        self.height = height
        # The media asset ID of the portrait image.
        self.portrait = portrait
        # The thumbnail URL.
        self.thumbnail = thumbnail
        # Indicates whether the digital human supports alpha channels.
        self.transparent = transparent
        # The width of the digital human image in pixels.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar_description is not None:
            result['AvatarDescription'] = self.avatar_description

        if self.avatar_id is not None:
            result['AvatarId'] = self.avatar_id

        if self.avatar_name is not None:
            result['AvatarName'] = self.avatar_name

        if self.avatar_type is not None:
            result['AvatarType'] = self.avatar_type

        if self.height is not None:
            result['Height'] = self.height

        if self.portrait is not None:
            result['Portrait'] = self.portrait

        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail

        if self.transparent is not None:
            result['Transparent'] = self.transparent

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarDescription') is not None:
            self.avatar_description = m.get('AvatarDescription')

        if m.get('AvatarId') is not None:
            self.avatar_id = m.get('AvatarId')

        if m.get('AvatarName') is not None:
            self.avatar_name = m.get('AvatarName')

        if m.get('AvatarType') is not None:
            self.avatar_type = m.get('AvatarType')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Portrait') is not None:
            self.portrait = m.get('Portrait')

        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')

        if m.get('Transparent') is not None:
            self.transparent = m.get('Transparent')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

