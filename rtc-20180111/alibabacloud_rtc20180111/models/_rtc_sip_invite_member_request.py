# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RtcSipInviteMemberRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_token: str = None,
        call_number: str = None,
        channel_id: str = None,
        device_type: str = None,
        registered: bool = None,
        server_address: str = None,
        sip_display_name: str = None,
        sip_room_id: str = None,
        sip_uri: str = None,
        sip_user_agent: str = None,
        sip_user_id: str = None,
        sip_user_password: str = None,
        task_id: str = None,
        uid: str = None,
    ):
        # The application ID. You can create and query the ID in the console. Only a single ID is supported.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The meeting token. For code generation, refer to https://help.aliyun.com/document_detail/2689025.html.
        self.app_token = app_token
        # The custom line number in PSTN scenarios.
        self.call_number = call_number
        # The channel ID. Only a single ID is supported.
        # 
        # This parameter is required.
        self.channel_id = channel_id
        # The type of the device used to call the third-party SIP endpoint. Valid values:
        # - sip_device
        # - mcu
        # - phone
        # 
        # Note: Currently, only the phone type is supported.
        # 
        # This parameter is required.
        self.device_type = device_type
        # Specifies whether the third-party meeting system requires registration for inbound calls.
        # 
        # This parameter is required.
        self.registered = registered
        # 1. The IP address of the nearest RTC SIP server.
        # 2. You can resolve the domain name rtcsip.dingtalk.com locally to obtain the nearest access address.
        # For example, run dig rtcsip.dingtalk.com to obtain the address.
        self.server_address = server_address
        # The username displayed on the third-party system.
        # 
        # This parameter is required.
        self.sip_display_name = sip_display_name
        # 1. When the device is mcu, it indicates the channel number of the third-party meeting system to be called.
        # 2. When the device is sip_device, it indicates the registration number of the registered device to be invited.
        # 3. When the device is phone, it indicates the called phone number.
        # 
        # This parameter is required.
        self.sip_room_id = sip_room_id
        # 1. When the device is mcu, it indicates the address information of the third-party meeting system in the format of ip:port;transport=tcp/udp/tls.
        # Example: "30.240.160.66:5060;transport=tcp"
        # 2. When the device is sip_device, it indicates the registration address of the registered device to be invited.
        # Example: 39.101.232.13
        # 3. When the device is phone, it indicates the address information of the telephone gateway.
        # Example: "30.240.160.66:5060;transport=tcp"
        self.sip_uri = sip_uri
        # The brand and model of the third-party SIP endpoint being called, such as polycom, cisco, tencent, zoom, or pstn.
        self.sip_user_agent = sip_user_agent
        # 1. When DeviceType is mcu, it represents the third-party meeting system.
        # 2. When DeviceType is sip_device, it represents the registered device.
        # 3. If the third-party meeting system requires registration for inbound calls, it is the account provided by the third-party system to create an account.
        # 4. If registration is not required, it is the SIP username or RTC user ID for calling the third-party system.
        # 
        # This parameter is required.
        self.sip_user_id = sip_user_id
        # The registration password that matches the SipUserId if the third-party system requires registration for inbound calls.
        self.sip_user_password = sip_user_password
        # The task ID.
        self.task_id = task_id
        # The user ID.
        # 
        # This parameter is required.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_token is not None:
            result['AppToken'] = self.app_token

        if self.call_number is not None:
            result['CallNumber'] = self.call_number

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.registered is not None:
            result['Registered'] = self.registered

        if self.server_address is not None:
            result['ServerAddress'] = self.server_address

        if self.sip_display_name is not None:
            result['SipDisplayName'] = self.sip_display_name

        if self.sip_room_id is not None:
            result['SipRoomId'] = self.sip_room_id

        if self.sip_uri is not None:
            result['SipUri'] = self.sip_uri

        if self.sip_user_agent is not None:
            result['SipUserAgent'] = self.sip_user_agent

        if self.sip_user_id is not None:
            result['SipUserId'] = self.sip_user_id

        if self.sip_user_password is not None:
            result['SipUserPassword'] = self.sip_user_password

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppToken') is not None:
            self.app_token = m.get('AppToken')

        if m.get('CallNumber') is not None:
            self.call_number = m.get('CallNumber')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('Registered') is not None:
            self.registered = m.get('Registered')

        if m.get('ServerAddress') is not None:
            self.server_address = m.get('ServerAddress')

        if m.get('SipDisplayName') is not None:
            self.sip_display_name = m.get('SipDisplayName')

        if m.get('SipRoomId') is not None:
            self.sip_room_id = m.get('SipRoomId')

        if m.get('SipUri') is not None:
            self.sip_uri = m.get('SipUri')

        if m.get('SipUserAgent') is not None:
            self.sip_user_agent = m.get('SipUserAgent')

        if m.get('SipUserId') is not None:
            self.sip_user_id = m.get('SipUserId')

        if m.get('SipUserPassword') is not None:
            self.sip_user_password = m.get('SipUserPassword')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

