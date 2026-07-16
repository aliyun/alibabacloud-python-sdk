# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteServiceRolloutResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        # A message indicating the result of the request.
        # 
        # - Type: `string`
        # 
        # - Description: The message that describes the result of the request.
        # 
        # - Example value: `Rollout deleted successfully`
        self.message = message
        # The unique ID of the request. Use this ID for troubleshooting.
        # 
        # - Type: `string`
        # 
        # - Description: The unique identifier for the request. Use this ID to troubleshoot and track issues.
        # 
        # - Example: `40325405-579C-4D82-9B4F-8A7C6D5E4F3A`
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

