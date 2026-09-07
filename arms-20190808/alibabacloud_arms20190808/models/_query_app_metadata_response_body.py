# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class QueryAppMetadataResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The API call status.
        # 
        # - 2xx: The request was successful.
        # 
        # - 3xx: The request was redirected.
        # 
        # - 4xx: A client-side error occurred.
        # 
        # - 5xx: A server-side error occurred.
        self.code = code
        # The returned object.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the query was successful.
        # 
        # - `true`: The query was successful.
        # 
        # - `false`: The query failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            self.data = m.get('Data')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

