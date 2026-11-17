# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class EndSessionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        # The business processing status code. A value of OK indicates success. If an exception occurs, the corresponding business error code is returned. The error types and mapping rules follow the current API configuration. No error codes are added or modified for this operation.
        self.code = code
        # The session ID of the terminated text session, which corresponds to the session ID in the request. The service still returns this ID even if the session context has expired.
        self.data = data
        # The HTTP status code recorded in the business response body. A value of 200 indicates a normal response. To determine whether the business operation is successful, you must also check the Code field. You cannot determine the success of the call based solely on the presence of this field.
        self.http_status_code = http_status_code
        # The business response or error message. This field is usually empty or omitted for successful requests. For failed requests, it provides an error description to assist in troubleshooting. Use this field in conjunction with the Code and Params fields to identify the cause of the error. The example shows the error message returned when an instance does not exist, which corresponds to the NotExists.InstanceId error code. This example is for format reference only.
        self.message = message
        # The list of parameters used to localize error messages. These are not scenario variables or business results. A successful response usually returns an empty array. If an error occurs, the parameters corresponding to the error template may be returned.
        self.params = params
        # The ID used to trace and troubleshoot the current POP request. The value in the response corresponds to the current request. System request parameters are injected by the gateway, so you do not need to specify system fields.
        self.request_id = request_id

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

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

