# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMessageTokenRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        device_id: str = None,
        device_type: str = None,
        user_id: str = None,
    ):
        # The ID of the interactive messaging application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the device. Each device has a unique ID. You can specify a custom ID. The ID can be up to 64 characters in length and can contain lowercase letters, digits, underscores (_), and hyphen (-). You can specify multiple device IDs. We recommend that you obtain the IDs from the devices and pass the IDs to the server.
        # 
        # This parameter is required.
        self.device_id = device_id
        # The type of the device. Valid values:
        # 
        # *   ios
        # *   android
        # *   web
        # *   pc
        # 
        # This parameter is required.
        self.device_type = device_type
        # The ID of the user. Each user has a unique ID in the application. The ID can be up to 32 characters in length and can contain lowercase letters, digits, underscores (_), and periods (.). You can specify multiple user IDs.
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

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

