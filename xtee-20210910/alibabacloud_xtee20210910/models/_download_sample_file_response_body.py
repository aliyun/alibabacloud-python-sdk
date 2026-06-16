# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DownloadSampleFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.DownloadSampleFileResponseBodyResultObject = None,
    ):
        # Status code.
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # Return message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Return Result.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DownloadSampleFileResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class DownloadSampleFileResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        status: str = None,
        url: str = None,
    ):
        # Model status.
        self.status = status
        # OSS download URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

