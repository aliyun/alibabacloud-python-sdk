# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RtcSendSipDtmfRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        channel_id: str = None,
        channel_user_id: str = None,
        device_type: str = None,
        digits: str = None,
    ):
        # The application ID. You can create and query the ID in the console. Only a single ID is supported.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of an existing channel. Only a single ID is supported.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The user ID (sipUserId) in the target OneRTC SIP call.
        # 
        # This parameter is required.
        self.channel_user_id = channel_user_id
        # The device type of the third-party Session Initiation Protocol (SIP) device. Valid values:
        # - sip_device
        # - mcu
        # - phone
        # 
        # This parameter is required.
        self.device_type = device_type
        # The keys to be sent. Supported keys include 0-9, A-D, a-d, *, #, W or w (wait), and F or f (flash). The keys are sent in the original order and case.
        # 
        # This parameter is required.
        self.digits = digits

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

        if self.channel_user_id is not None:
            result['ChannelUserId'] = self.channel_user_id

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.digits is not None:
            result['Digits'] = self.digits

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ChannelUserId') is not None:
            self.channel_user_id = m.get('ChannelUserId')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('Digits') is not None:
            self.digits = m.get('Digits')

        return self

