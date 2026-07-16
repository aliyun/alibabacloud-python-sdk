# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aisearchengine20260417 import models as main_models
from darabonba.model import DaraModel

class GetDatasetResourceUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetDatasetResourceUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The business status code. A value of `200` indicates a successful request. Other values indicate an exception. For more information, see error codes.
        self.code = code
        # The business data body.
        self.data = data
        # The status description. The value is "success" for successful requests and a specific error message for failed requests.
        self.message = message
        # The unique request ID, used for troubleshooting.
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
            temp_model = main_models.GetDatasetResourceUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetDatasetResourceUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        url: str = None,
    ):
        # The temporary OSS access URL with a signature and expiration time (valid for 24 hours). The URL can be used directly for frontend display or download.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')

        return self

