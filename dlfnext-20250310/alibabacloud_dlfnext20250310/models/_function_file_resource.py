# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FunctionFileResource(DaraModel):
    def __init__(
        self,
        resource_type: str = None,
        uri: str = None,
    ):
        self.resource_type = resource_type
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.uri is not None:
            result['uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('uri') is not None:
            self.uri = m.get('uri')

        return self

