# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRumAppResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        # The status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The message that appears when the application is deleted.
        self.result = result
        # Indicates whether the request is successful. Valid values: true and false.
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.result is not None:
            result['Result'] = self.result

        if self.success is not None:
            result['Success'] = self.success

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

