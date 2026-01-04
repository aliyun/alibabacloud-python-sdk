# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class CreateApplicationTokenResponseBody(DaraModel):
    def __init__(
        self,
        application_tokens: main_models.CreateApplicationTokenResponseBodyApplicationTokens = None,
        request_id: str = None,
    ):
        self.application_tokens = application_tokens
        self.request_id = request_id

    def validate(self):
        if self.application_tokens:
            self.application_tokens.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_tokens is not None:
            result['ApplicationTokens'] = self.application_tokens.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationTokens') is not None:
            temp_model = main_models.CreateApplicationTokenResponseBodyApplicationTokens()
            self.application_tokens = temp_model.from_map(m.get('ApplicationTokens'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateApplicationTokenResponseBodyApplicationTokens(DaraModel):
    def __init__(
        self,
        application_token: str = None,
        application_token_id: str = None,
        application_token_type: str = None,
    ):
        # 应用token
        self.application_token = application_token
        # 应用token ID
        self.application_token_id = application_token_id
        # 应用token类型
        self.application_token_type = application_token_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_token is not None:
            result['ApplicationToken'] = self.application_token

        if self.application_token_id is not None:
            result['ApplicationTokenId'] = self.application_token_id

        if self.application_token_type is not None:
            result['ApplicationTokenType'] = self.application_token_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationToken') is not None:
            self.application_token = m.get('ApplicationToken')

        if m.get('ApplicationTokenId') is not None:
            self.application_token_id = m.get('ApplicationTokenId')

        if m.get('ApplicationTokenType') is not None:
            self.application_token_type = m.get('ApplicationTokenType')

        return self

