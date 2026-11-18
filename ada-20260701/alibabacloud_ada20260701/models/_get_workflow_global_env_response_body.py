# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWorkflowGlobalEnvResponseBody(DaraModel):
    def __init__(
        self,
        content: str = None,
        exists: bool = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        updated_at: int = None,
    ):
        # The configuration content.
        # 
        # This parameter is required.
        self.content = content
        # Indicates whether the configuration is saved.
        # 
        # This parameter is required.
        self.exists = exists
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
        # The timestamp of the last modification in milliseconds.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.exists is not None:
            result['Exists'] = self.exists

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.size is not None:
            result['Size'] = self.size

        if self.success is not None:
            result['Success'] = self.success

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Exists') is not None:
            self.exists = m.get('Exists')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

