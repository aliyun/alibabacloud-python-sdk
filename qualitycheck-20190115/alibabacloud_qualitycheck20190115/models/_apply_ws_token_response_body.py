# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class ApplyWsTokenResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ApplyWsTokenResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ApplyWsTokenResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ApplyWsTokenResponseBodyData(DaraModel):
    def __init__(
        self,
        session_id: str = None,
        token: str = None,
        ws_endpoint: str = None,
    ):
        self.session_id = session_id
        self.token = token
        self.ws_endpoint = ws_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.token is not None:
            result['Token'] = self.token

        if self.ws_endpoint is not None:
            result['WsEndpoint'] = self.ws_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('WsEndpoint') is not None:
            self.ws_endpoint = m.get('WsEndpoint')

        return self

