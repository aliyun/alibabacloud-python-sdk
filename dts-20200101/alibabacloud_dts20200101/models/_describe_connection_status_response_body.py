# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DescribeConnectionStatusResponseBody(DaraModel):
    def __init__(
        self,
        destination_connection_status: Dict[str, Any] = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        source_connection_status: Dict[str, Any] = None,
        success: str = None,
    ):
        # The connectivity of DTS servers to the destination database.
        self.destination_connection_status = destination_connection_status
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_message = err_message
        # The ID of the request.
        self.request_id = request_id
        # The connectivity of DTS servers to the source database.
        self.source_connection_status = source_connection_status
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_connection_status is not None:
            result['DestinationConnectionStatus'] = self.destination_connection_status

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_connection_status is not None:
            result['SourceConnectionStatus'] = self.source_connection_status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationConnectionStatus') is not None:
            self.destination_connection_status = m.get('DestinationConnectionStatus')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceConnectionStatus') is not None:
            self.source_connection_status = m.get('SourceConnectionStatus')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

