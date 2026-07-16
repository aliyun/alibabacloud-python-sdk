# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TagResourcesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        request_id: str = None,
    ):
        # The request status code. Valid values:
        # 
        # - OK: The request was successful.
        # - For other error codes, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The result of adding the tags. Valid values:
        # 
        # - **true**: success.
        # - **false**: failure.
        self.data = data
        # The request ID.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

