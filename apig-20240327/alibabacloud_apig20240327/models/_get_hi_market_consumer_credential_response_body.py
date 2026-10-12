# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetHiMarketConsumerCredentialResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHiMarketConsumerCredentialResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetHiMarketConsumerCredentialResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetHiMarketConsumerCredentialResponseBodyData(DaraModel):
    def __init__(
        self,
        api_key_config: main_models.HiMarketApiKeyConfig = None,
        hmac_config: main_models.HiMarketHmacConfig = None,
    ):
        # The API key credential configuration of the consumer. This corresponds to the common data structure HiMarketApiKeyConfig and includes the key, source, and credentials list members. Each item in the credentials list contains an apiKey.
        self.api_key_config = api_key_config
        # The HMAC credential configuration of the consumer. This corresponds to the common data structure HiMarketHmacConfig and includes the credentials list member. Each item in the credentials list contains an ak and an sk.
        self.hmac_config = hmac_config

    def validate(self):
        if self.api_key_config:
            self.api_key_config.validate()
        if self.hmac_config:
            self.hmac_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_config is not None:
            result['apiKeyConfig'] = self.api_key_config.to_map()

        if self.hmac_config is not None:
            result['hmacConfig'] = self.hmac_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyConfig') is not None:
            temp_model = main_models.HiMarketApiKeyConfig()
            self.api_key_config = temp_model.from_map(m.get('apiKeyConfig'))

        if m.get('hmacConfig') is not None:
            temp_model = main_models.HiMarketHmacConfig()
            self.hmac_config = temp_model.from_map(m.get('hmacConfig'))

        return self

