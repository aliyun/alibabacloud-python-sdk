# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateSlrPermissionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the service-linked role has been created. Valid values:
        # 
        # - true: The role has been created.
        # - false: The role has not been created.
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

