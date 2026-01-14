# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRegistryNamespaceResponseBody(DaraModel):
    def __init__(
        self,
        namespace_name: str = None,
        request_id: str = None,
    ):
        self.namespace_name = namespace_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

