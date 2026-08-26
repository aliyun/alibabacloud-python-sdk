# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRoomRealTimeStreamAddressRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        display_name: str = None,
        expire_time: int = None,
        user_id: str = None,
    ):
        # The ID of the ApsaraVideo Real-time Communication application. Only a single ID is supported. The value can contain uppercase and lowercase letters, digits, underscores, and hyphens (-), with a maximum of 64 characters. You can view your application IDs by navigating to **ApsaraVideo Live > Live+ > Real-time Communication > Application Management**. If no application exists, create one by clicking **Create Application**.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the channel to join. Only a single ID is supported. The value can contain uppercase and lowercase letters, digits, underscores, and hyphens (-), with a maximum of 64 characters.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The display name of the RTMP stream in the channel. Maximum length: 40 characters.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The validity period of the RTMP URL. Unit: seconds. Default value: 36000 (10 hours).
        self.expire_time = expire_time
        # The user ID for the RTMP stream ingest. This value must not duplicate any other user ID in the channel. The value can contain uppercase and lowercase letters, digits, underscores, and hyphens (-), with a maximum of 64 characters.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

