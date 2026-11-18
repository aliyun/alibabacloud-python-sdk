# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveWorkflowGlobalEnvResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        size: int = None,
        success: bool = None,
    ):
        # The request ID.
        # 
        # This parameter is required.
        self.request_id = request_id
        # The number of UTF-8 bytes in the configuration content.
        # 
        # This parameter is required.
        self.size = size
        # Indicates whether the request is successful.
        # 
        # This parameter is required.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.size is not None:
            result['Size'] = self.size

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

