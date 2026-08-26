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
        # Interactive Messages application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Terminal device ID, uniquely representing a user terminal device, user-defined. It consists of lowercase letters, numbers, underscores (_), and hyphens (-), with a maximum length of 64 characters. Different terminal devices need to use different DeviceIds. We recommend obtaining it from the terminal device and passing it to the server.
        # 
        # This parameter is required.
        self.device_id = device_id
        # Terminal device type. Valid values:
        # 
        # - ios
        # 
        # - android
        # 
        # - web
        # 
        # - pc
        # 
        # This parameter is required.
        self.device_type = device_type
        # User UserId, user-defined, unique within the AppId. It consists of lowercase letters, numbers, underscores (_), and periods (.), with a maximum length of 32 characters. Different users need to use different UserIds.
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

