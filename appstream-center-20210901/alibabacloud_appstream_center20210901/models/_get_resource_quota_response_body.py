# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResourceQuotaResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The error code returned when an error occurs during the call. A normal result is not guaranteed to contain this field. You should not use the return of a specific success code as a prerequisite for obtaining the quota.
        self.code = code
        # The maximum resource count quota applicable to the current query conditions. This is not the usage or remaining quota.
        # 
        # - `ResourceType=AppInstanceGroup`: Unit: count.
        # - `ResourceType=AppAuthUser`: Unit: users.
        # - `ResourceType=PoolNodeAmount`: Unit: count.
        # 
        # If no smaller limit is obtained, `2147483647` is returned. This does not mean that the resource inventory is unlimited.
        self.data = data
        # The error message returned when an error occurs during the call. This message and the error code help you identify the cause of the error.
        self.message = message
        # The unique identifier for the request. You can use this ID to troubleshoot issues.
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

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        return self

