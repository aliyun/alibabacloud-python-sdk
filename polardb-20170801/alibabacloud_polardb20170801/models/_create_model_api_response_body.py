# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateModelApiResponseBody(DaraModel):
    def __init__(
        self,
        invoke_endpoint: str = None,
        model_api_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.invoke_endpoint = invoke_endpoint
        self.model_api_id = model_api_id
        # Id of the request
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invoke_endpoint is not None:
            result['InvokeEndpoint'] = self.invoke_endpoint

        if self.model_api_id is not None:
            result['ModelApiId'] = self.model_api_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeEndpoint') is not None:
            self.invoke_endpoint = m.get('InvokeEndpoint')

        if m.get('ModelApiId') is not None:
            self.model_api_id = m.get('ModelApiId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

