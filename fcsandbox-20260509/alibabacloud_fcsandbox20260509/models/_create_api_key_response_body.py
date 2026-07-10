# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class CreateApiKeyResponseBody(DaraModel):
    def __init__(
        self,
        api_key: main_models.ApiKey = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.api_key = api_key
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.api_key:
            self.api_key.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key.to_map()

        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            temp_model = main_models.ApiKey()
            self.api_key = temp_model.from_map(m.get('apiKey'))

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

