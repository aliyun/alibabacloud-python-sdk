# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeComponentsJsResponseBody(DaraModel):
    def __init__(
        self,
        components_js: str = None,
        request_id: str = None,
    ):
        # The configuration of the JavaScript file for the component.
        self.components_js = components_js
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.components_js is not None:
            result['ComponentsJs'] = self.components_js

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentsJs') is not None:
            self.components_js = m.get('ComponentsJs')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

