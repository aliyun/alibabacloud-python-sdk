# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateExtensionsResponseBody(DaraModel):
    def __init__(
        self,
        extensions: str = None,
        request_id: str = None,
    ):
        # The name of the extension that you want to install. Multiple extension names are separated with commas (,).
        self.extensions = extensions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extensions is not None:
            result['Extensions'] = self.extensions

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

