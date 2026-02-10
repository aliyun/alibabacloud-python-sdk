# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateJenkinsImageRegistryPersistenceDayResponseBody(DaraModel):
    def __init__(
        self,
        data: bool = None,
        http_status_code: int = None,
        request_id: str = None,
        time_cost: int = None,
    ):
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The time consumed. Unit: seconds.
        self.time_cost = time_cost

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.time_cost is not None:
            result['TimeCost'] = self.time_cost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TimeCost') is not None:
            self.time_cost = m.get('TimeCost')

        return self

