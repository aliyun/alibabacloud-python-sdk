# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTenantDirectoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        directory_id: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The business status code. A value of 200 indicates success. If the request fails, a specific business error code is returned.
        self.code = code
        # The business ID of the updated directory. You can refresh the configuration content by calling the corresponding configuration read API operation.
        self.directory_id = directory_id
        # The response message. The value is success if the request is successful. If the request fails, the message describes the cause of the error.
        self.message = message
        # The request tracking ID. You can use this ID to troubleshoot issues related to this call.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

