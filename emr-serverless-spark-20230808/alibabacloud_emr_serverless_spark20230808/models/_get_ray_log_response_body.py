# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class GetRayLogResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetRayLogResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code. A value of 1000000 indicates a successful request. Other values indicate a failed request. You can view the specific error description in the message parameter.
        self.code = code
        # The response data.
        self.data = data
        # The error message.
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
            temp_model = main_models.GetRayLogResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetRayLogResponseBodyData(DaraModel):
    def __init__(
        self,
        access_url: str = None,
    ):
        # The file download URL.
        self.access_url = access_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_url is not None:
            result['accessUrl'] = self.access_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessUrl') is not None:
            self.access_url = m.get('accessUrl')

        return self

