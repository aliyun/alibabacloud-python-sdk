# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class QueryRtmpKeyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryRtmpKeyResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

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
            temp_model = main_models.QueryRtmpKeyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryRtmpKeyResponseBodyData(DaraModel):
    def __init__(
        self,
        pull_auth_key: str = None,
        pull_key_expire_time: int = None,
        push_auth_key: str = None,
        push_key_expire_time: int = None,
        stream_name: str = None,
    ):
        self.pull_auth_key = pull_auth_key
        self.pull_key_expire_time = pull_key_expire_time
        self.push_auth_key = push_auth_key
        self.push_key_expire_time = push_key_expire_time
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pull_auth_key is not None:
            result['PullAuthKey'] = self.pull_auth_key

        if self.pull_key_expire_time is not None:
            result['PullKeyExpireTime'] = self.pull_key_expire_time

        if self.push_auth_key is not None:
            result['PushAuthKey'] = self.push_auth_key

        if self.push_key_expire_time is not None:
            result['PushKeyExpireTime'] = self.push_key_expire_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PullAuthKey') is not None:
            self.pull_auth_key = m.get('PullAuthKey')

        if m.get('PullKeyExpireTime') is not None:
            self.pull_key_expire_time = m.get('PullKeyExpireTime')

        if m.get('PushAuthKey') is not None:
            self.push_auth_key = m.get('PushAuthKey')

        if m.get('PushKeyExpireTime') is not None:
            self.push_key_expire_time = m.get('PushKeyExpireTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

