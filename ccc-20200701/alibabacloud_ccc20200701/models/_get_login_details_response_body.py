# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class GetLoginDetailsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetLoginDetailsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetLoginDetailsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetLoginDetailsResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_server_url: str = None,
        avatar_url: str = None,
        chat_app_id: str = None,
        chat_app_key: str = None,
        chat_device_id: str = None,
        chat_login_token: str = None,
        chat_server_url: str = None,
        chat_user_id: str = None,
        device_ext: str = None,
        device_id: str = None,
        device_state: str = None,
        display_name: str = None,
        extension: str = None,
        nickname: str = None,
        signature: str = None,
        signature_2: str = None,
        sip_server_url: str = None,
        user_id: str = None,
        user_key: str = None,
        user_key_2: str = None,
        work_mode: str = None,
    ):
        self.agent_server_url = agent_server_url
        self.avatar_url = avatar_url
        self.chat_app_id = chat_app_id
        self.chat_app_key = chat_app_key
        self.chat_device_id = chat_device_id
        self.chat_login_token = chat_login_token
        self.chat_server_url = chat_server_url
        self.chat_user_id = chat_user_id
        self.device_ext = device_ext
        self.device_id = device_id
        self.device_state = device_state
        self.display_name = display_name
        self.extension = extension
        self.nickname = nickname
        self.signature = signature
        self.signature_2 = signature_2
        self.sip_server_url = sip_server_url
        self.user_id = user_id
        self.user_key = user_key
        self.user_key_2 = user_key_2
        self.work_mode = work_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_server_url is not None:
            result['AgentServerUrl'] = self.agent_server_url

        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url

        if self.chat_app_id is not None:
            result['ChatAppId'] = self.chat_app_id

        if self.chat_app_key is not None:
            result['ChatAppKey'] = self.chat_app_key

        if self.chat_device_id is not None:
            result['ChatDeviceId'] = self.chat_device_id

        if self.chat_login_token is not None:
            result['ChatLoginToken'] = self.chat_login_token

        if self.chat_server_url is not None:
            result['ChatServerUrl'] = self.chat_server_url

        if self.chat_user_id is not None:
            result['ChatUserId'] = self.chat_user_id

        if self.device_ext is not None:
            result['DeviceExt'] = self.device_ext

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.device_state is not None:
            result['DeviceState'] = self.device_state

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.nickname is not None:
            result['Nickname'] = self.nickname

        if self.signature is not None:
            result['Signature'] = self.signature

        if self.signature_2 is not None:
            result['Signature2'] = self.signature_2

        if self.sip_server_url is not None:
            result['SipServerUrl'] = self.sip_server_url

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_key is not None:
            result['UserKey'] = self.user_key

        if self.user_key_2 is not None:
            result['UserKey2'] = self.user_key_2

        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentServerUrl') is not None:
            self.agent_server_url = m.get('AgentServerUrl')

        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')

        if m.get('ChatAppId') is not None:
            self.chat_app_id = m.get('ChatAppId')

        if m.get('ChatAppKey') is not None:
            self.chat_app_key = m.get('ChatAppKey')

        if m.get('ChatDeviceId') is not None:
            self.chat_device_id = m.get('ChatDeviceId')

        if m.get('ChatLoginToken') is not None:
            self.chat_login_token = m.get('ChatLoginToken')

        if m.get('ChatServerUrl') is not None:
            self.chat_server_url = m.get('ChatServerUrl')

        if m.get('ChatUserId') is not None:
            self.chat_user_id = m.get('ChatUserId')

        if m.get('DeviceExt') is not None:
            self.device_ext = m.get('DeviceExt')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DeviceState') is not None:
            self.device_state = m.get('DeviceState')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('Signature2') is not None:
            self.signature_2 = m.get('Signature2')

        if m.get('SipServerUrl') is not None:
            self.sip_server_url = m.get('SipServerUrl')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserKey') is not None:
            self.user_key = m.get('UserKey')

        if m.get('UserKey2') is not None:
            self.user_key_2 = m.get('UserKey2')

        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')

        return self

