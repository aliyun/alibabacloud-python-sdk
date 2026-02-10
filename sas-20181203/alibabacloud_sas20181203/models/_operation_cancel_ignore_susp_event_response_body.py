# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperationCancelIgnoreSuspEventResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time_cost: int = None,
    ):
        # The status code returned. The status code **200** indicates that the request was is successful. Other status codes indicate that the request fails. You can identify the cause of the failure based on the status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The handling result of an exception. Valid values:
        # 
        # *   **true**: successful
        # *   **false**: failed
        self.success = success
        # The time consumed for the request. Unit: seconds.
        self.time_cost = time_cost

    def validate(self):
        pass

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

        if self.success is not None:
            result['Success'] = self.success

        if self.time_cost is not None:
            result['TimeCost'] = self.time_cost

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

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TimeCost') is not None:
            self.time_cost = m.get('TimeCost')

        return self

