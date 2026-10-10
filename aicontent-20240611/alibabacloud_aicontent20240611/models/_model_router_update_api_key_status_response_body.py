# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ModelRouterUpdateApiKeyStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ModelRouterUpdateApiKeyStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response status code.
        self.code = code
        # The data object.
        self.data = data
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # - **true**: Successful.
        # - **false**: Failed.
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ModelRouterUpdateApiKeyStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ModelRouterUpdateApiKeyStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        id: int = None,
        status: str = None,
    ):
        # ID
        self.id = id
        # The status of the API key. Valid values:
        # 
        # - active: The API key is valid.
        # - disabled: The API key is invalid.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

