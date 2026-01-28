# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bailianvoicebot20250101 import models as main_models
from darabonba.model import DaraModel

class BridgeWebCallResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.BridgeWebCallResponseBodyData = None,
        error_msg: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

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

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.BridgeWebCallResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class BridgeWebCallResponseBodyData(DaraModel):
    def __init__(
        self,
        channel_id: str = None,
        expiration_time: str = None,
        instance_id: str = None,
        server_url: str = None,
        session_id: str = None,
        token: str = None,
    ):
        self.channel_id = channel_id
        self.expiration_time = expiration_time
        self.instance_id = instance_id
        self.server_url = server_url
        self.session_id = session_id
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.server_url is not None:
            result['ServerUrl'] = self.server_url

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ServerUrl') is not None:
            self.server_url = m.get('ServerUrl')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

