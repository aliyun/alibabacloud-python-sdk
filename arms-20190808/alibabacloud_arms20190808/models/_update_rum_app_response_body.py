# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class UpdateRumAppResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.UpdateRumAppResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The details of the returned results.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`
        # *   `false`
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.UpdateRumAppResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateRumAppResponseBodyData(DaraModel):
    def __init__(
        self,
        config: str = None,
        limit: int = None,
        limited: bool = None,
        usage: int = None,
    ):
        # The user configurations. This is a reserved parameter.
        self.config = config
        # The QPS limit. Unit: bytes.
        self.limit = limit
        # Indicates whether the request is throttled due to the QPS limit. Valid values: true and false.
        self.limited = limited
        # The usage. Unit: bytes.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.limited is not None:
            result['Limited'] = self.limited

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Limited') is not None:
            self.limited = m.get('Limited')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

