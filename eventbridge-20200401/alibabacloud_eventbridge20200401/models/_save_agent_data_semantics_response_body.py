# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class SaveAgentDataSemanticsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code of the operation.
        self.code = code
        # The update result. If the save is successful, an empty object is returned with no additional business fields. If none of the four knowledge categories are specified, the target state is all four categories empty: if a non-empty current version exists, an all-empty version is published. If the current version is already all empty or no current version exists, the operation succeeds idempotently and the current round of pending generation results is finalized.
        self.data = data
        # The response message. If the call fails, an error message is returned.
        self.message = message
        # The unique identifier that Alibaba Cloud generates for the request.
        self.request_id = request_id
        # Indicates whether the call is successful.
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

