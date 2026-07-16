# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelservice20220614 import models as main_models
from darabonba.model import DaraModel

class GetUserResponseBody(DaraModel):
    def __init__(
        self,
        anthropic_host: str = None,
        api_keys: List[main_models.GetUserResponseBodyApiKeys] = None,
        app_id: str = None,
        code: str = None,
        dashscope_host: str = None,
        host: str = None,
        inner_token: str = None,
        message: str = None,
        request_id: str = None,
        token: str = None,
    ):
        self.anthropic_host = anthropic_host
        self.api_keys = api_keys
        self.app_id = app_id
        self.code = code
        self.dashscope_host = dashscope_host
        self.host = host
        self.inner_token = inner_token
        self.message = message
        self.request_id = request_id
        self.token = token

    def validate(self):
        if self.api_keys:
            for v1 in self.api_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anthropic_host is not None:
            result['AnthropicHost'] = self.anthropic_host

        result['ApiKeys'] = []
        if self.api_keys is not None:
            for k1 in self.api_keys:
                result['ApiKeys'].append(k1.to_map() if k1 else None)

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.code is not None:
            result['Code'] = self.code

        if self.dashscope_host is not None:
            result['DashscopeHost'] = self.dashscope_host

        if self.host is not None:
            result['Host'] = self.host

        if self.inner_token is not None:
            result['InnerToken'] = self.inner_token

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnthropicHost') is not None:
            self.anthropic_host = m.get('AnthropicHost')

        self.api_keys = []
        if m.get('ApiKeys') is not None:
            for k1 in m.get('ApiKeys'):
                temp_model = main_models.GetUserResponseBodyApiKeys()
                self.api_keys.append(temp_model.from_map(k1))

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DashscopeHost') is not None:
            self.dashscope_host = m.get('DashscopeHost')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InnerToken') is not None:
            self.inner_token = m.get('InnerToken')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self



class GetUserResponseBodyApiKeys(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        inner_api_key: str = None,
    ):
        self.api_key = api_key
        self.inner_api_key = inner_api_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.inner_api_key is not None:
            result['InnerApiKey'] = self.inner_api_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('InnerApiKey') is not None:
            self.inner_api_key = m.get('InnerApiKey')

        return self

