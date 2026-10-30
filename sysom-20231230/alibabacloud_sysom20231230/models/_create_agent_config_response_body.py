# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class CreateAgentConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateAgentConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        # - If `code` is `Success`, the authorization is successful.
        # - Other status codes indicate that the authorization failed. If the authorization failed, check the `message` field for the detailed fault message.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        # - If `code` is `Success`, this field is empty.
        # - Otherwise, this field contains the error message of the request.
        self.message = message
        # Id of the request
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
            temp_model = main_models.CreateAgentConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CreateAgentConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        config_id: str = None,
    ):
        # The ID of the created component configuration.
        self.config_id = config_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['configId'] = self.config_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configId') is not None:
            self.config_id = m.get('configId')

        return self

