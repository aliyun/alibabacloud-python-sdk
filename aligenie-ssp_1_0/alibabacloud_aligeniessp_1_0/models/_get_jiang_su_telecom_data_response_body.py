# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class GetJiangSuTelecomDataResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetJiangSuTelecomDataResponseBodyResult = None,
    ):
        # Status code. Returns 200 for normal responses.
        self.code = code
        # Id of the request
        self.message = message
        # Request ID
        self.request_id = request_id
        # Actual return result of the service
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetJiangSuTelecomDataResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetJiangSuTelecomDataResponseBodyResult(DaraModel):
    def __init__(
        self,
        oss_url: str = None,
    ):
        # OSS object URL, valid for 10 minutes
        self.oss_url = oss_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')

        return self

