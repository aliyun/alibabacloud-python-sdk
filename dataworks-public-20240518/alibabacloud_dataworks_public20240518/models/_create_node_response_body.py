# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNodeResponseBody(DaraModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        # The unique identifier of the data development node.
        # 
        # >Notice: This field was of the Long type in SDK versions earlier than 8.0.0 and is of the String type in SDK 8.0.0 and later. **This change does not affect normal SDK usage, and the parameter is still returned in the type defined in the SDK**. Only when you upgrade across SDK version 8.0.0, the type change may cause project compilation failures, and you need to manually correct the data type.
        self.id = id
        # The request ID. You can use this ID to locate logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

