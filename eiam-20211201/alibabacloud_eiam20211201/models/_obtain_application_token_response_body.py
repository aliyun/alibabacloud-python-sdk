# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ObtainApplicationTokenResponseBody(DaraModel):
    def __init__(
        self,
        application_token: main_models.ObtainApplicationTokenResponseBodyApplicationToken = None,
        request_id: str = None,
    ):
        self.application_token = application_token
        self.request_id = request_id

    def validate(self):
        if self.application_token:
            self.application_token.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_token is not None:
            result['ApplicationToken'] = self.application_token.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationToken') is not None:
            temp_model = main_models.ObtainApplicationTokenResponseBodyApplicationToken()
            self.application_token = temp_model.from_map(m.get('ApplicationToken'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ObtainApplicationTokenResponseBodyApplicationToken(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_token: str = None,
        application_token_id: str = None,
        application_token_type: str = None,
        create_time: int = None,
        expiration_time: int = None,
        instance_id: str = None,
        last_used_time: int = None,
        status: str = None,
    ):
        # IDaaS EIAM 应用Id
        self.application_id = application_id
        # 客户端密钥
        self.application_token = application_token
        # IDaaS EIAM 客户端ID
        self.application_token_id = application_token_id
        # IDaaS EIAM 客户端密钥Id
        self.application_token_type = application_token_type
        self.create_time = create_time
        self.expiration_time = expiration_time
        # IDaaS EIAM 实例Id
        self.instance_id = instance_id
        # IDaaS EIAM 客户端密钥最近使用时间
        self.last_used_time = last_used_time
        # IDaaS EIAM 客户端密钥状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_token is not None:
            result['ApplicationToken'] = self.application_token

        if self.application_token_id is not None:
            result['ApplicationTokenId'] = self.application_token_id

        if self.application_token_type is not None:
            result['ApplicationTokenType'] = self.application_token_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_used_time is not None:
            result['LastUsedTime'] = self.last_used_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationToken') is not None:
            self.application_token = m.get('ApplicationToken')

        if m.get('ApplicationTokenId') is not None:
            self.application_token_id = m.get('ApplicationTokenId')

        if m.get('ApplicationTokenType') is not None:
            self.application_token_type = m.get('ApplicationTokenType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastUsedTime') is not None:
            self.last_used_time = m.get('LastUsedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

