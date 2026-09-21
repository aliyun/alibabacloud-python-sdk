# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteStopGatewayResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The returned status code.
        self.code = code
        # The status code indicating the result of the deletion:
        # 
        # - **0**: Success. The metadata was deleted.
        # 
        # - **-1**: A system error occurred.
        # 
        # - **-2**: The specified database gateway does not exist.
        # 
        # - **-3**: The database gateway is still active (not stopped) and its metadata cannot be deleted.
        # 
        # - **-4**: Failed to delete the metadata.
        self.data = data
        # The returned message.
        # 
        # > When the request is successful, this parameter returns **Successful**. When the request fails, this parameter returns exception information such as error codes.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful:
        # 
        # - **true**: The operation is successful.
        # 
        # - **false**: The operation failed.
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

        if self.message is not None:
            result['Message'] = self.message

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

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

