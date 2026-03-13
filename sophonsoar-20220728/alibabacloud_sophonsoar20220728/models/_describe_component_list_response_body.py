# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeComponentListResponseBody(DaraModel):
    def __init__(
        self,
        components: str = None,
        request_id: str = None,
    ):
        # The information about the components. The value is a JSON array.
        self.components = components
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.components is not None:
            result['Components'] = self.components

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Components') is not None:
            self.components = m.get('Components')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

