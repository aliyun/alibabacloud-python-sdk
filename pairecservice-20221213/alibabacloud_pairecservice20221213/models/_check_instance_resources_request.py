# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckInstanceResourcesRequest(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        type: str = None,
        uri: str = None,
    ):
        self.resource_id = resource_id
        # This parameter is required.
        self.type = type
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.type is not None:
            result['Type'] = self.type

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

