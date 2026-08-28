# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateAgentIMChannelCredentialRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateAgentIMChannelCredentialRequestBody = None,
        client_token: str = None,
    ):
        # The request body.
        self.body = body
        # A reserved idempotency token. The backend does not provide persistent idempotence guarantee in the current version.
        self.client_token = client_token

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UpdateAgentIMChannelCredentialRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdateAgentIMChannelCredentialRequestBody(DaraModel):
    def __init__(
        self,
        credential: Dict[str, str] = None,
    ):
        # The channel credential. All fields must be provided and field values must be non-empty strings. DingTalk uses clientID and clientSecret. Lark uses appId and appSecret. WeCom uses botId and secret.
        # 
        # This parameter is required.
        self.credential = credential

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential is not None:
            result['credential'] = self.credential

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credential') is not None:
            self.credential = m.get('credential')

        return self

