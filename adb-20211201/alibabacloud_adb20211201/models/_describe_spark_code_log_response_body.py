# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSparkCodeLogResponseBody(DaraModel):
    def __init__(
        self,
        log: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The log content.
        self.log = log
        # The additional information about the call result. Valid values:
        # - If the request succeeds, **Success** is returned. 
        # - If an exception occurs, the specific error code is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - **true**: The call was successful.
        # - **false**: The call failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log is not None:
            result['Log'] = self.log

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Log') is not None:
            self.log = m.get('Log')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

