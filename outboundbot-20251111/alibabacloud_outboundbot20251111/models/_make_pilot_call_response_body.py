# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class MakePilotCallResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.MakePilotCallResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        # The business processing status code. OK indicates success. When an exception occurs, the corresponding business error code is returned. Error types and mapping rules follow the current API configuration. No error codes are added or modified in this operation.
        self.code = code
        # The session ID of the current real-number outbound call test. The return of this object does not indicate that the called party has answered.
        self.data = data
        # The HTTP status code recorded in the business response body. A normal return value is 200. To determine whether the business operation is successful, you must also check Code. You cannot determine the success of the call solely based on the presence of this field.
        self.http_status_code = http_status_code
        # The business response or error description. This field is usually empty or not returned upon success. A fixed text cannot be required upon success. Upon failure, this field contains an error description to assist in troubleshooting. Combine this field with Code and Params to understand the cause of the error. The example shows an error message when the instance does not exist, where Code is NotExists.InstanceId. This is for format reference only.
        self.message = message
        # The list of parameters used for the localized display of error messages. This is not a scenario variable or business result. A normal successful response usually returns an empty array. When an error occurs, parameters corresponding to the error template may be returned.
        self.params = params
        # The ID used to associate and troubleshoot the current POP request. The value in the response corresponds to the current request. System request parameters are injected by the gateway. Callers do not need to fill in system fields.
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
            temp_model = main_models.MakePilotCallResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class MakePilotCallResponseBodyData(DaraModel):
    def __init__(
        self,
        session_id: str = None,
    ):
        # The session ID used to uniquely associate the current interaction. For a text session, it is the text- ID returned when the session is started. For web voice, it is the ws- ID. For a real-number outbound call test, it is the test- ID. Subsequent calls must use the actual return value.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

