# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class QueryTraceExtractJobResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.QueryTraceExtractJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The status code.
        self.status_code = status_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.QueryTraceExtractJobResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class QueryTraceExtractJobResponseBodyData(DaraModel):
    def __init__(
        self,
        trace: str = None,
    ):
        # The trace watermark information.
        self.trace = trace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.trace is not None:
            result['Trace'] = self.trace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Trace') is not None:
            self.trace = m.get('Trace')

        return self

