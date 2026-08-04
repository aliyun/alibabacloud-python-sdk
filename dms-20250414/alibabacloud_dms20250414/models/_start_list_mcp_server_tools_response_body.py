# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class StartListMcpServerToolsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.StartListMcpServerToolsResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result of the asynchronous detection startup. Only StartTimestamp may be returned if the resources are still being provisioned.
        self.data = data
        # The return code. The value success is returned if the request was successful. An error code is returned if the request failed.
        self.error_code = error_code
        # The error message returned if a system-level request failure occurs.
        self.error_message = error_message
        # The request ID, which is used to locate this call.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.StartListMcpServerToolsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class StartListMcpServerToolsResponseBodyData(DaraModel):
    def __init__(
        self,
        session_id: str = None,
        start_timestamp: str = None,
    ):
        # The temporary session ID for this detection. After the startup succeeds, use this value to call GetListMcpServerToolsResult to poll for the result.
        self.session_id = session_id
        # The UNIX timestamp at which the server started the detection, in milliseconds.
        self.start_timestamp = start_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        return self

